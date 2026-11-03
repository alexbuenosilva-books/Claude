import io, wave, sys
import numpy as np
from scipy import signal
from piper import PiperVoice, SynthesisConfig

VOICE = sys.argv[1] if len(sys.argv) > 1 else "voices/en_US-ryan-high.onnx"
OUT = sys.argv[2] if len(sys.argv) > 2 else "radio.wav"
rng = np.random.default_rng(7)
TS = float(sys.argv[3]) if len(sys.argv) > 3 else 0.22  # timing scale for pauses
TD = float(sys.argv[4]) if len(sys.argv) > 4 else 0.45  # timing scale for dropouts
voice = PiperVoice.load(VOICE)
SR = voice.config.sample_rate
cfg = SynthesisConfig(length_scale=1.0, noise_scale=0.5, noise_w_scale=0.6)


def tts(text):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        voice.synthesize_wav(text, w, syn_config=cfg)
    buf.seek(0)
    with wave.open(buf, "rb") as r:
        a = np.frombuffer(r.readframes(r.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    # trim leading/trailing silence
    idx = np.where(np.abs(a) > 0.01)[0]
    a = a[max(idx[0] - 200, 0): idx[-1] + 400]
    return a / (np.max(np.abs(a)) + 1e-9) * 0.9


def sil(sec):
    return np.zeros(int(sec * SR), np.float32)


def fade(a, fin=0.005, fout=0.005):
    a = a.copy()
    ni, no = int(fin * SR), int(fout * SR)
    if ni: a[:ni] *= np.linspace(0, 1, ni)
    if no: a[-no:] *= np.linspace(1, 0, no)
    return a


def breath(sec=0.45):
    n = int(sec * SR)
    b = rng.normal(0, 1, n).astype(np.float32)
    bb, ab = signal.butter(2, [500 / (SR / 2), 2500 / (SR / 2)], "band")
    b = signal.lfilter(bb, ab, b)
    env = np.sin(np.linspace(0, np.pi, n)) ** 1.5
    return (b * env * 0.12).astype(np.float32)


# timeline: voice track + "dropout" mask (1 = clear signal, 0 = lost)
voice_track, mask = [], []


def add(a, m=1.0):
    voice_track.append(a.astype(np.float32))
    mask.append(np.full(len(a), m, np.float32))


def say(text, keep=1.0, fin=0.004):
    a = tts(text)
    if keep < 1.0:  # signal cut mid-word
        a = fade(a[: int(len(a) * keep)], fin, 0.002)
    else:
        a = fade(a, fin, 0.01)
    add(a)


def drop(sec):  # reception failure: no voice, static surges
    sec *= TD
    add(sil(sec), 0.0)


def pause(sec):
    sec *= TS
    add(sil(sec))


def tone(sec=1.6):  # two-tone attention signal
    t = np.arange(int(sec * SR)) / SR
    a = 0.22 * (np.sin(2 * np.pi * 853 * t) + np.sin(2 * np.pi * 960 * t))
    add(fade(a.astype(np.float32), 0.01, 0.01))


# ---------- script ----------
pause(0.6)
drop(0.4)
tone(0.9)
drop(0.35)
pause(0.4)
say("This is")
drop(0.45)
say("Emergency Operations", keep=0.42)
drop(0.25)
say("Operations at MacDill")
drop(0.5)
say("Air Force")
drop(0.35)
say("Base.")
pause(0.55)
say("This is a")
drop(0.3)
say("recorded")
drop(0.3)
say("message.")
pause(1.1)

# "Se <breath> ek refuge immediately."
seek = tts("Seek refuge immediately.")
cut = int(0.16 * SR)
add(fade(seek[:cut], 0.004, 0.003))
drop(0.12)
add(breath(0.5))
add(fade(seek[cut:], 0.003, 0.01))
pause(0.35)
say("This is a life threatening", keep=0.80)
drop(0.4)
say("threatening situation.")
pause(0.45)
say("Get inside the nearest")
drop(0.5)
say("secure building.")
pause(0.35)
say("Stay away from windows.")
pause(0.45)
say("If you are in a vehicle")
drop(0.45)
say("leave the road.")
pause(0.3)
say("Find shelter.")
pause(1.2)
say("This is not")
drop(0.55)
say("a test.")
pause(1.0)
say("This message will")
drop(0.6)
say("repeat.")
pause(1.4)
# loop restarts, then signal is lost for good
say("This is")
drop(0.35)
say("Emergency Operations", keep=0.30)
drop(1.6)

v = np.concatenate(voice_track)
m = np.concatenate(mask)
N = len(v)

# smooth the mask so dropouts swell instead of clicking
m = signal.filtfilt(*signal.butter(2, 40 / (SR / 2)), m)
m = np.clip(m, 0, 1)

# ---------- radio processing on voice ----------
# light slap echo (recorded PA message)
d = int(0.075 * SR)
v = v + 0.22 * np.concatenate([np.zeros(d), v[:-d]])
# narrow comms bandpass
b, a = signal.butter(4, [320 / (SR / 2), 3000 / (SR / 2)], "band")
v = signal.lfilter(b, a, v)
# overdriven transmitter
v = np.tanh(v * 3.2) / np.tanh(3.2)
# bit-crush / sample-hold grit
hold = 2
v = np.repeat(v[::hold], hold)[:N]
v = np.round(v * 64) / 64
v = signal.lfilter(*signal.butter(2, 3400 / (SR / 2)), v)
# slow fading (multipath / skywave)
t = np.arange(N) / SR
fadeLFO = 0.78 + 0.14 * np.sin(2 * np.pi * 0.23 * t + 1) + 0.08 * np.sin(2 * np.pi * 0.71 * t)
# fast flutter
flut = 1 - 0.25 * (signal.filtfilt(*signal.butter(1, 12 / (SR / 2)), rng.normal(0, 1, N)) > 0.35)
v = v * fadeLFO * flut * m

# ---------- noise bed ----------
white = rng.normal(0, 1, N)
hiss = signal.lfilter(*signal.butter(2, [200 / (SR / 2), 6000 / (SR / 2)], "band"), white)
hiss /= np.max(np.abs(hiss))
hum = 0.5 * np.sin(2 * np.pi * 60 * t) + 0.25 * np.sin(2 * np.pi * 120 * t)
# crackle: sparse impulses
crack = np.zeros(N)
idx = rng.choice(N, size=int(N / SR * 22), replace=False)
crack[idx] = rng.uniform(-1, 1, len(idx))
crack = signal.lfilter(*signal.butter(2, [800 / (SR / 2), 5000 / (SR / 2)], "band"), crack) * 4
# heterodyne whistle drifting, louder when signal drops
whfreq = 1150 + 300 * np.sin(2 * np.pi * 0.07 * t) + 80 * np.sin(2 * np.pi * 0.9 * t)
whistle = np.sin(2 * np.pi * np.cumsum(whfreq) / SR)
lost = 1 - m
# static bursts on dropouts, gurgly
burst = signal.lfilter(*signal.butter(2, [400 / (SR / 2), 4500 / (SR / 2)], "band"), rng.normal(0, 1, N))
burst /= np.max(np.abs(burst))
gurgle = 0.5 + 0.5 * (signal.filtfilt(*signal.butter(1, 25 / (SR / 2)), rng.normal(0, 1, N)) > 0)

noise = (0.075 + 0.03 * np.sin(2 * np.pi * 0.31 * t)) * hiss \
    + 0.012 * hum \
    + 0.18 * crack \
    + (0.006 + 0.03 * lost) * whistle \
    + 1.5 * lost * gurgle * burst

mix = v * 0.85 + noise
# squelch clicks at start/end
for pos in [int(0.33 * SR), N - int(0.8 * SR)]:
    mix[pos:pos + 80] += rng.uniform(-0.8, 0.8, 80)
mix[: int(0.3 * SR)] *= np.linspace(0, 1, int(0.3 * SR))
mix[N - int(0.6 * SR):] *= np.linspace(1, 0, int(0.6 * SR)) ** 2
# hard cutoff after squelch tail
mix = np.concatenate([mix, np.zeros(int(0.5 * SR))])
mix = mix / np.max(np.abs(mix)) * 0.95

with wave.open(OUT, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())
print(OUT, len(mix) / SR, "s")
