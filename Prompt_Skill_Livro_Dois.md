# Prompt para criar a skill "Os Últimos Dias de Tudo — Livro Dois"

*Copie tudo abaixo da linha e cole numa conversa nova com qualquer LLM (Claude, ChatGPT, Gemini ou outro). O próprio prompt traz todo o conhecimento da série, então funciona mesmo que o modelo nunca tenha visto o Livro Um.*

---

## TAREFA

Você vai criar uma **skill de escrita**: um pacote de instruções e de referência que transforma um assistente de IA num **parceiro de escrita especializado no Livro Dois** da série *The Last Days of Everything* (*Os Últimos Dias de Tudo*). A skill deve permitir que o autor, em qualquer conversa futura, planeje, escreva, revise e explore o Livro Dois com total coerência com o Livro Um, mesmo quando ainda não decidiu todos os rumos da história.

Todo o conhecimento necessário está neste prompt, nas seções "BÍBLIA DA SÉRIE" e "DECISÕES". **Não invente fatos sobre o Livro Um além do que está aqui.** Onde algo não estiver definido, a skill deve tratar o ponto como **decisão em aberto** e oferecer opções ao autor, nunca decidir em silêncio.

## O QUE VOCÊ DEVE ENTREGAR

Produza os arquivos abaixo, cada um num bloco separado, com o nome do arquivo no topo:

1. **`SKILL.md`** — o arquivo principal, curto (no máximo 400 linhas). Comece com um cabeçalho YAML:
   ```
   ---
   name: last-days-book-two
   description: Parceiro de escrita do Livro Dois de "The Last Days of Everything". Use sempre que o autor pedir para planejar, escrever, reescrever, revisar ou explorar capítulos, cenas, personagens, diálogos, cronologia ou decisões do Livro Dois, ou quando ele mencionar Kate, Sophie, Ethan, Noah, Lucas, Emma, Pepper, a caverna, Camp Blanding ou a jornada pela I-75.
   ---
   ```
   Depois do cabeçalho, inclua: a missão, os modos de trabalho, o fluxo obrigatório antes de escrever, as regras invioláveis e um índice das referências que diga quando ler cada uma.
2. **`references/mundo.md`** — as regras físicas, tecnológicas e sociais do mundo, o cronograma solar e a geografia.
3. **`references/cronologia.md`** — a linha do tempo do Livro Um e a do Livro Dois (planejada).
4. **`references/personagens.md`** — uma ficha completa de cada personagem: perfil, história pregressa, trauma, desejo e necessidade, voz, estado físico, o que carrega, o que sabe, arco no Livro Dois e destinos possíveis.
5. **`references/estilo.md`** — o guia de voz e de formato, com exemplos.
6. **`references/fios.md`** — as sementes do Livro Um, os fios em aberto, as variações possíveis e os ganchos para o Livro Três.
7. **`references/escaleta.md`** — a estrutura em quatro atos e a escaleta capítulo a capítulo.
8. **`references/decisoes.md`** — o **registro de decisões**: o que está decidido, o que está em aberto (com opções e recomendação) e um espaço para o autor atualizar.
9. **`references/continuidade.md`** — o checklist de continuidade e os inventários (armas, munição, remédios, comida, água, combustível, relógios, ferimentos).

Se o LLM que for usar a skill não aceitar skills com arquivos (por exemplo, um chat comum), entregue **também** uma versão única, `INSTRUCOES_PROJETO.md`, com tudo concatenado, para colar como "instruções do projeto" ou "prompt de sistema".

## COMO A SKILL DEVE SE COMPORTAR

Escreva no `SKILL.md` estas regras de comportamento:

**Modos de trabalho.** O autor pode pedir, em palavras livres, qualquer um destes modos. A skill reconhece o modo e segue o roteiro dele.

1. **Planejar.** Montar ou ajustar a escaleta, um ato ou um capítulo. A saída é uma lista de batidas (*beats*) com hora, lugar, ponto de vista, objetivo da cena, conflito, virada e o que muda no estado da história.
2. **Escrever.** Redigir um capítulo ou uma cena completa no estilo da série. Antes de escrever, a skill lê o registro de decisões, a ficha dos personagens presentes, a cronologia (para saber dia, hora, clima e céu) e o inventário. Depois de escrever, entrega um **bloco de atualização de estado** (veja abaixo).
3. **Revisar.** Ler um capítulo do autor e apontar problemas de continuidade, de voz, de ritmo e de coerência científica. A saída é uma lista de problemas com sugestões, sem reescrever tudo, a menos que o autor peça.
4. **Explorar.** Quando o autor não sabe que caminho seguir, oferecer **de duas a quatro opções** com prós, contras e impacto nos capítulos seguintes, e indicar uma recomendação justificada.
5. **Personagem.** Aprofundar ou criar um personagem: ficha completa no mesmo formato de `personagens.md`, e a checagem de que o nome não colide com nenhum nome existente.
6. **Diálogo.** Escrever ou testar a voz de um personagem numa situação.
7. **Atualizar.** Registrar uma decisão nova do autor em `decisoes.md` e propagar as consequências (o que muda na escaleta, nas fichas e na continuidade).

**Fluxo obrigatório antes de escrever qualquer cena:**
1. Identificar data, hora e lugar.
2. Conferir em `mundo.md` o estado do céu, a temperatura, o UV e as tempestades daquele momento.
3. Conferir em `personagens.md` o estado físico, o que cada personagem carrega e o que sabe naquele ponto. **Ninguém sabe o que ainda não descobriu.**
4. Conferir em `decisoes.md` se a cena toca uma decisão em aberto. Se tocar, **pergunte ao autor ou ofereça opções**; não escolha sozinho. Se o autor pedir para seguir mesmo assim, use a recomendação marcada e avise.
5. Conferir o inventário em `continuidade.md`.

**Bloco de atualização de estado.** Ao fim de cada capítulo escrito, a skill entrega:
```
ESTADO APÓS O CAPÍTULO [n] — [data, hora]
- Localização de cada personagem:
- Ferimentos e saúde (mudanças):
- Inventário (o que entrou, o que saiu):
- O que cada personagem passou a saber:
- Fios abertos ou fechados:
- Decisões tomadas nesta cena (para registrar em decisoes.md):
```

**Regras invioláveis da série:**
- Nunca contradizer o Livro Um.
- Ninguém é salvo por milagre. Nenhum resgate do governo no fim.
- No quarto ato (debaixo da terra), **nenhum ponto de vista lá fora**. O evento principal é sentido, nunca visto.
- Carros e aparelhos só funcionam se forem antigos e mecânicos, ou se tiverem sido protegidos do pulso.
- A cachorra Pepper não morre.
- O final reúne Kate, Lucas, Emma, Sophie, Ethan, Noah e Pepper vivos, debaixo da terra.
- Ciência em frases curtas, ligada a uma decisão; nunca em monólogo.
- A violência humana é realista, cresce a cada dia e não tem vilões caricatos.
- Contar balas, comprimidos, comida, água e combustível.

**Idioma.** O original da série é em **inglês**. Por padrão, a skill escreve a prosa do livro em inglês e conversa com o autor em português. Se o autor pedir a prosa em português do Brasil, use as convenções da tradução: diálogo com travessão, sistema métrico, Celsius e títulos de capítulo no formato "HHhMM — Lugar". Em inglês, use aspas, unidades americanas (Fahrenheit, milhas) e títulos no formato "HH:MMam - Place".

---

# BÍBLIA DA SÉRIE (conteúdo para as referências)

## 1. Premissa da série

Thriller de catástrofe em tempo quase real, na Flórida. A erupção do monte **Tambora** (Indonésia, 12 de maio) joga enxofre na estratosfera e corrói o ozônio: "afina o telhado". Dias depois, uma sequência de tempestades solares vindas de um complexo magnético na face oculta do Sol atinge a Terra. Separados, os dois fenômenos seriam sobrevivíveis. Juntos, "se multiplicam" (a tese do dr. Karl Richter no prólogo: "estaríamos vivendo os últimos dias de… tudo").

## 2. Resumo do Livro Um (14 a 17 de maio)

- **14/05, noite.** Talk show *Late Night with Tom Maya*: o geofísico Karl Richter explica que, se uma grande tempestade solar chegasse com o ozônio fino, "não haveria plano".
- **15/05, manhã.** Kate Brennan, meteorologista da WSUN-13 de Tampa, chama a névoa do Tambora de "bonita" no jornal das 5h23 e vê a previsão falhar: frio vindo de cima, vento de nordeste, uma camada fria anômala. Sophie Davis, aluna de física da USF, recebe do orientador, o dr. Vance, a missão de testar o SOMA (uma IA que "escuta" o Sol pela heliossismologia) antes da visita do professor Santiago, de Cornell, na sexta-feira. Às 10h42, o SOMA acha uma anomalia escondida atrás do limbo leste (S23E95) e Sophie lança uma varredura de 847 janelas.
- **15/05, 10h50.** Ethan Cole, filho do magnata da energia Harrison Cole, invade o arquivo da empresa do pai e descobre a reserva de **340 transformadores de alta tensão com mitigação de GIC**, a confirmar até o dia 18, logo depois de um documento sigiloso do Departamento de Segurança Interna (DHS).
- **15/05, meio-dia.** Uma tempestade súbita e correntes induzidas derrubam a rede de Tampa; a vidraça do centro estudantil explode. O laboratório de física é atingido por uma sobretensão e a rodada do SOMA se perde. Ethan relança o SOMA na nuvem da Cole Energy.
- **15/05, noite.** Aviões caem por erro de GPS: Delta 2847 em Orlando, um da American em Miami, helicópteros, um regional em Kansas City. Suspensão nacional de voos às 21h47. O resultado do SOMA, montado com post-its na parede do apartamento de Ethan e Noah, mostra **um nó preto enorme na face oculta, girando em direção à Terra**. Sophie posta no fórum de física solar. Apagão total. Uma única resposta: "Acho que tem um problema na sua correção do limbo."
- **16/05, madrugada.** Aurora vermelha sobre Tampa; aves desorientadas voando para o norte. Kate faz o jornal das 5h e contraria em parte a previsão oficial.
- **16/05, 8h05.** **Kate e Sophie se conhecem** na sala vazia de Vance, que desapareceu. Kate leva um pen drive com os dados de Sophie e os e-mails dela e de Ethan.
- **16/05, 10h25.** Starlink conectado na caçamba da caminhonete de Ethan. Harrison liga: há um bunker e "a lista"; ele quer o filho, mas recusa Sophie e Noah. Ethan desliga e quebra o celular.
- **16/05, 10h45.** Na emissora, Kate lê que a correção do limbo **subestimava** a região, e que o boletim de Bruxelas mostra o complexo surgindo no limbo sudeste. Ela manda tudo por e-mail para Sophie e Ethan (eles **nunca recebem**) e salva no pen drive.
- **16/05, 10h58.** **O pulso**: tudo o que tem chip morre (celulares, notebooks, carros modernos, câmeras). O Corolla velho de Kate funciona, com o painel morto.
- **16/05, ~13h.** Tornados eletrificados. O Holly B é destruído. Noah leva uma lasca de madeira no ombro e Ethan um prego nas costas. Em Bloomingdale, **Melissa e James morrem** protegendo os filhos; Kate sobrevive amarrada ao vaso sanitário pelo cinto, com Lucas e Emma.
- **16/05, tarde.** No hospital AdventHealth, sem energia, Sophie sabe por Jonas que **Vance morreu** (atingido por um galho ao salvar uma caloura; morreu no respirador quando a energia acabou). Ela rouba antibióticos e ibuprofeno. O sargento-mor Dale Whitaker leva Kate e as crianças para a Base Aérea de MacDill.
- **16/05, 19h00.** O presidente culpa um "ataque cibernético" que teria usado o vulcão e o Sol como cobertura. As bases militares abrem os portões.
- **16/05, noite.** Na St. Luke's, o padre Patrick sugere a **Warren's Cave**, uma caverna seca em San Felasco Hammock, a noroeste de Gainesville, a uns 210 km. Plano: dois dias de bicicleta, mais um de margem.
- **17/05, madrugada.** Kate recebe boletins militares: tempestade G5 "escala excedida", e a região na face oculta com índice de tamanho **4, depois 6, depois 9** num dia, entrando no campo de visão **entre 19 e 20 de maio**. Ela conta a verdade a Emma e decide ir para **Camp Blanding**, onde o coronel Jimmy Warren, padrinho de Lucas, comanda o posto e há paióis enterrados sob três metros de terra. Dale lhe dá roupas, mantimentos, dois galões de gasolina e o seu **revólver .38**.
- **17/05, ~5h.** Os dois grupos partem para o norte: Kate num caminhão militar até a saída de Bloomingdale; o trio de bicicleta pela I-75, depois da bênção do padre, que dá a Noah a **medalha de São Cristóvão**.

## 3. Regras do mundo

- **Rede elétrica:** caída em quase todo o Hemisfério Norte; os transformadores queimados levam meses para serem substituídos. Só há geradores isolados.
- **Depois do pulso:** só funcionam aparelhos simples, antigos ou protegidos. Lanternas simples funcionam, rádios a pilha antigos funcionam às vezes, carros de carburador e caminhões militares antigos funcionam. Relógios de corda funcionam.
- **Comunicação:** só ondas curtas, radioamadores e gravações militares. O GPS mente.
- **Clima:** frio de inverno vindo de cima (o ozônio, que aquece a alta atmosfera, está sendo destruído), geada em Tampa, tempestades súbitas com o Golfo ainda quente a uns 27-29 °C sob ar frio, granizo, tornados eletrificados e fogo de santelmo.
- **Céu:** névoa marrom-acobreada de dia; sol pálido "que dá luz sem calor"; aurora vermelha à noite até a Flórida.
- **UV:** cresce a cada dia; queimaduras mesmo sob céu fechado; risco de cegueira de neve. Os óculos de esqui de Sophie são preciosos.
- **Sociedade:** dinheiro vivo; saques; armas; postos de controle; bases militares lotadas; a elite foi para bunkers (Raven Rock, Mount Weather, Cheyenne Mountain), segundo uma "lista".
- **Cronograma solar (Sophie e os boletins):** três regiões já viradas (valores 22, 25 e 24) causaram tudo até agora. Uma de **31** passa da borda na noite de **17/05**; uma de **34** em **18/05**; depois um **"dia calmo"** (19/05), em que todos acham que acabou. **O nó preto** (valores na casa dos 80) começa a se virar em **19-20/05**. Se a grande erupção for de dia para os EUA, o clarão atinge as Américas; se for de noite, atinge a Ásia. As nuvens de plasma (CMEs) chegam de 18 a 48 horas depois, com radiação, colapso do ozônio e mais frio.
- **Cenário adotado:** o "do meio": o clarão na noite americana e as CMEs depois. O grupo sobrevive porque está debaixo da terra.

## 4. Geografia da jornada

I-75 para o norte: Tampa/USF (Fletcher) → Wesley Chapel → Brooksville (SR-50) → ponte do rio Withlacoochee → Bushnell → Wildwood (entroncamento com a Turnpike) → arredores de The Villages → Ocala (haras de cavalos) → Micanopy → **Paynes Prairie** (pradaria aberta e alagável, com jacarés e cavalos selvagens) → Gainesville → San Felasco Hammock (a caverna). De Gainesville para nordeste, por umas dezenas de quilômetros, ficam Starke, **Camp Blanding** e as prisões de Raiford. De bicicleta com feridos, rende-se de 50 a 70 km por dia. **A Warren's Cave é real e protegida: mantenha os detalhes ficcionais** (sumidouro, escada antiga de madeira, passagens secas, câmara principal, lago subterrâneo), sem descrever o acesso real.

## 5. Personagens do núcleo principal

Para cada um, o arquivo de personagens deve ter: perfil, história pregressa, trauma, ferida, desejo, necessidade, voz e tiques, estado físico no início do Livro Dois, o que carrega, o que sabe, arco planejado, destinos possíveis e frases de exemplo.

**Kate Brennan.** 32 anos. Meteorologista da WSUN-13 há seis anos, com cerca de quinze de carreira. Viúva de Ryan, soldado do Exército morto há treze meses (a causa nunca foi dita; está em aberto). Mãe de Lucas e, agora, de Emma.
- **Trauma:** a morte de Ryan (dois oficiais à porta); a previsão errada de 15/05, que levou gente para a tempestade; a morte de Melissa e James diante dela.
- **Competência:** lê o céu sem instrumentos e mede a certeza em porcentagem ("setenta por cento"). Conta os choques no caderno.
- **Tiques:** pressiona a mão no joelho para ele parar de tremer; esconde as mãos que tremem; ouve as instruções de Ryan na cabeça ("Dois é um. Um é nenhum").
- **Estado físico:** sete pontos na testa, possível concussão, lasca de madeira no antebraço (já retirada), palma cortada, costelas e coxa machucadas, pulso marcado pelo cinto.
- **Carrega:** a bolsa de Dale (roupas de inverno da família Whitaker, kit de primeiros socorros, rações, água), dois galões de gasolina, o .38 (seis balas e uma caixa), o mapa com Blanding circulado, a jaqueta SGM WHITAKER, o caderno, a Maglite, o pen drive.
- **Sabe:** os boletins militares (o índice 4, 6, 9 e a janela 19-20), os mapas corrigidos (a região é maior do que Sophie pensa), Blanding, que o general do CENTCOM levou a família. Não sabe da caverna até ler o bilhete na St. Luke's.
- **Desejo:** levar as crianças para um lugar seguro (Blanding). **Necessidade:** agir sem certeza e confiar em uma pessoa em vez de instituições.
- **Arco:** de confiar nos militares a escolher a rocha; vitória profissional ao ler o granizo; vira mãe de Emma.

**Lucas Brennan.** 6 anos. Tem os olhos e a atenção paciente de Ryan. Come tudo, pergunta "O papai está vendo?", pisa no gelo para ouvi-lo estalar, agarra a blusa da mãe com o punho fechado. Tem bochechas e nuca queimadas de UV (uma semente). No Livro Dois, é o "irmão" de Emma; pode se perder numa multidão; é carregado por Noah no rio.

**Emma Torres.** 6 anos. Filha de Melissa e James, os dois mortos no tornado de 16/05. Não viu a mãe morrer. Kate contou a verdade às 2h de 17/05. É "a quieta", a que Denise mandou observar. Volta a falar por causa da cachorra Pepper. **Trauma:** luto agudo, manifestado no corpo (não comer, segurar os dedos de Kate, raiva súbita). **Arco:** do silêncio à pergunta difícil feita na caverna; chama Kate de "mãe" por engano.

**Sophie Davis.** Cerca de 21 anos, terceiro ano de física na USF. Órfã: os pais morreram na Geórgia quando ela tinha 10 anos (o policial à porta da avó; dois caixões); depois a avó morreu; passou por lares adotivos.
- **Trauma e crença:** "quem fica perto de mim, alguma coisa vem buscar". Teve uma crise de pânico ao saber da morte de Vance.
- **Competência:** criou o SOMA; é a única que entende o nó preto; conta o tempo pela rotação do Sol.
- **Fé:** perdida.
- **Gesto moral:** roubou antibióticos (amoxicilina com clavulanato de 875 mg) e ibuprofeno de 800 mg.
- **Estado físico:** joelho machucado e inchado; corte nas costas da mão.
- **Carrega:** a mochila com latas e pasta de amendoim, o notebook morto, o caderno de calibração, a foto dos pais (o pai de gorro de Papai Noel; um canto molhado e desbotado), os post-its numerados, os óculos de esqui, a parca vermelha.
- **Sabe:** o cronograma solar; a caverna; os bunkers, por Ethan. Não sabe que a região é maior.
- **Semente:** sonhou com os pais "como se a estivessem chamando".
- **Fio solto:** perguntou ao padre "mais uma coisa" (não revelada) e deixou um bilhete no quadro da igreja para Jonas ou Kate.
- **Arco:** de "a culpa é minha" a "eu sei o que fazer"; vira a "relojoeira" da caverna; escolhe viver em vez de ir com os pais do sonho; o primeiro beijo com Ethan, no escuro da caverna.

**Ethan Cole.** Cerca de 21 anos, estudante de engenharia, hacker.
- **Trauma:** a mãe morreu num hospital enquanto ele ligava para o pai, que nunca atendeu. Sonha com isso (o fone balançando no fio).
- **Escolha que o define:** recusou o bunker sem Sophie e Noah: "Vocês dois são a minha família."
- **Sabe:** o e-mail do DHS, os 340 transformadores, a data do dia 18, "a lista", os bunkers.
- **Estado físico:** perfuração de prego nas costas, lado esquerdo; mexe pouco o braço esquerdo.
- **Perdeu:** a caminhonete, o Starlink e o celular. **Ganhou:** as luvas de couro do padre e uma jaqueta de esqui com o zíper fechado com fita.
- **Voz:** sarcástico, protetor, rápido nas piadas.
- **Arco:** encontrar valor sem tecnologia; uma possível segunda oferta do pai, que ele recusa ou que oferece a Noah.

**Noah Calloway.** (O sobrenome é uma sugestão: confirme no registro de decisões.) Cerca de 21 anos, estudante de engenharia, da Carolina do Norte, de família operária (pai em obras, com as costas ruins; mãe com o joelho ruim). Católico praticante da St. Luke's.
- **Competência:** mãos de mecânico e eletricista; o organizador das listas; calmo; forte.
- **Traços:** odeia briga, mas sabe parecer perigoso; faz o sinal da cruz quando tem medo; ainda sofre pelo fim com Victoria.
- **Ferimento grave:** lasca de 25 cm no ombro esquerdo, arrancada por ele mesmo; febre; risco de fragmento retido e de infecção. No início do Livro Dois, a febre baixou.
- **Objeto:** a medalha de São Cristóvão ("Vocês é que têm um rio para atravessar").
- **Tentação:** seguir pela I-75 até a Geórgia e as Carolinas, onde estão os pais.
- **Arco:** a infecção e o dilema do antibiótico; **carrega uma criança ao atravessar um rio**; aceita ser carregado; pode ficar com sequela no braço.

**Coadjuvantes do Livro Um:**
- **Padre Patrick O'Connor:** sessenta e poucos anos, de Boston, ex-carpinteiro; fica na St. Luke's com 47 abrigados. Guarda o bilhete. Tem uma inconsistência de idade sacerdotal (22 anos de padre versus 41 desde o seminário).
- **Jonas:** colega de laboratório de Sophie; está no hospital esperando a filha de Vance; tem "St. Luke's" escrito na mão.
- **Dale Whitaker:** sargento-mor em MacDill; a mulher Linda e os filhos Abby (16) e Danny (11) estão em Chattanooga; guarda a carta de Kate para o coronel Kessler sobre o Hangar 4.
- **Coronel Kessler:** comandante interino de MacDill.
- **Harrison Cole:** magnata, num bunker, com "a lista".
- **Marcus, Don Hargrave, Marty e Bob:** a equipe da emissora.
- **Doyle:** ex-bombeiro, vizinho de Bloomingdale.
- **Denise:** enfermeira do St. Joseph's.
- **Malik:** estudante de enfermagem.
- **Tess:** monitora do Holly B.

## 6. Personagens novos do Livro Dois (propostos)

Inclua uma ficha de cada um, no formato do núcleo, marcando-os como **"propostos: confirmar no registro de decisões"**:

- **Pepper.** Cachorra vira-lata com traços de pastor-australiano, 4 anos, olhos de cores diferentes. Era dos vizinhos Nguyen; Emma a adota. É o "magnetômetro vivo", que sente as tempestades geomagnéticas antes de todos. Não morre.
- **Curtis Hale.** 44 anos, técnico de refrigeração de Zephyrhills, com uma picape Ford F-100 de 1979. A mulher, Marisol (asmática), e o filho, Tyler (9). O antagonista-espelho em quatro encontros; no fim, dá a vaga da família na caverna e fica do lado de fora.
- **Coronel Jimmy Warren.** 52 anos, comandante de Camp Blanding, padrinho de Lucas, dívida com Ryan. A família é antiga dona da terra da caverna, e o bisavô construiu a escada. Não pode abrir os paióis (há uma "lista" de oficiais), mas dá antibiótico injetável, gasolina, uma chave da caverna e o relógio de corda do pai.
- **Dra. Ruth Ambler.** 68 anos, geóloga de carste aposentada, espeleóloga, viúva (o marido se afogou numa caverna alagada em 1997). Tem medo de água escura. Lidera o "outro grupo" na caverna e é uma figura de mentora com limites para Sophie.
- **Wade Corliss.** 38 anos, ex-sargento, segurança da universidade, armado; tem uma filha em Orlando. Disputa o comando, sobe escondido para buscar a filha e volta cego e queimado: a única "janela" para o mundo lá fora.
- **Bea Thornton.** 74 anos, radioamadora de Inverness; a filha morreu no furacão Michael. Aparece em capítulos-documento de rádio; a última transmissão dela se corta no dia 20.
- **Xerife Earl Mabry.** 61 anos, o senhor do posto de controle de Bushnell; a mulher depende de diálise.
- **Pastor Amos Reddick.** O Tabernáculo do Último Sol; o fanatismo que quer "ficar" com as crianças. Opcional.
- **Rafael Ochoa.** 57 anos, cavalariço mexicano num haras abandonado de Ocala; abriga o grupo no celeiro, sabe tratar feridas e solta os cavalos.
- **Isaiah Booker.** 29 anos, preso de Raiford que ajuda Kate; reconhece a "moça do tempo". Segue a pé.
- **Mara Voss.** Chefe de segurança da Cole Energy, enviada de Harrison com a oferta de "mais uma pessoa". Deixa um rádio com Ethan. Opcional.
- **Especialista Kayla Moreno.** 22 anos, soldado no portão de Blanding.
- **Deion Price e Hanna Lind.** Alunos de Ruth. Um deles pode morrer.
- **Opal Jenkins.** 81 anos, de uma igreja batista de Brooksville.
- **Krista.** A mãe do bebê na I-75.
- **Linh e Tuan Nguyen.** Os donos de Pepper.

## 7. Estilo

- **Capítulos curtos com título de hora e lugar.** Em inglês: "05:40am - I-75, Fletcher Avenue Exit". Em português: "05h40 — I-75, saída da Fletcher".
- **Ponto de vista** em terceira pessoa próxima, um por capítulo, alternando entre Kate, Sophie, Ethan e Noah; raramente Emma.
- **Documentos inseridos** como respiros: transcrições de rádio, boletins, bilhetes.
- **Prosa enxuta e sensorial;** frases curtas na tensão; repetição intencional; detalhes concretos que carregam emoção.
- **Ciência** pela boca de personagens competentes, em poucas frases e ligada a uma decisão.
- **Os personagens medem a própria certeza** ("Posso estar errada", "Não é prova").
- **Humor seco** nos piores momentos.
- **Bondade** em meio ao horror, a cada dois ou três capítulos de violência.
- **Motivos recorrentes:** o Sol que ressoa como sino; cerca e telhado; os post-its; "contar os choques"; a cortina vermelha; aves enviadas para o norte; mãos; a pergunta "O papai está vendo?"; "Dois é um. Um é nenhum."
- **Evitar:** monólogos científicos, clichês de filme de zumbi, vilões caricatos, estereótipos de grupos (presos, moradores rurais, religiosos), repetir a sequência de aviões do Livro Um, resolver o romance por completo.

## 8. Estrutura planejada (resumo para `escaleta.md`)

- **Primeiro ato, 17/05 — Partida.** Kate recupera o Corolla em Bloomingdale com Doyle; Emma recebe Pepper dos Nguyen; Kate lê o bilhete na St. Luke's e escolhe Blanding. O trio pedala; encontra Krista e o bebê, e Curtis Hale; paga pedágio no Withlacoochee. Bea no rádio. Opal em Brooksville. À noite, a aurora da região de 31.
- **Segundo ato, 18/05 — A estrada piora.** A febre de Noah e o dilema do antibiótico. O posto de Bushnell (o xerife Mabry). O comboio em Wildwood. A ironia de se cruzarem sem se ver. A tempestade de granizo, em que Kate salva pessoas lendo o céu. O trio quebrado. **O reencontro**: Kate salva o trio de Curtis. O celeiro de Rafael em Ocala e a troca de dados ("Você estava certa"). A decisão de tentar Blanding.
- **Terceiro ato, 19/05 — A rocha.** O "dia calmo". **Noah carrega Lucas pela pradaria alagada.** A chave em Gainesville. Kate em Starke: Isaiah, Kayla, Jimmy Warren e o colapso de Blanding. A corrida até a caverna; o carro sem gasolina; Pepper sente que "está começando"; o portão aberto; o grupo de Ruth; Curtis fica fora; a descida.
- **Quarto ato, 20/05 em diante — Debaixo da terra.** O calor constante da caverna; a última transmissão; **o evento sentido** (a cachorra, a bússola, o ar que inverte, um clarão pela escada); a disputa por subir; Wade volta cego; a pergunta de Emma; a crise da água e o medo de Ruth; o beijo no escuro; **o final**: a vela, "O papai está vendo?", e Pepper olhando para cima e abanando o rabo.

## 9. Fios e ganchos (para `fios.md`)

Liste estes, com o status "aberto" e as opções conhecidas:
- o bilhete e a "mais uma coisa" de Sophie;
- o pen drive ilegível sem um computador protegido;
- a medalha e o rio;
- o UV e os óculos;
- a comida e a água contadas;
- o SOMA rodando na nuvem da Cole Energy;
- a carta ao coronel Kessler e o Hangar 4;
- Harrison e a lista;
- os pais de Noah;
- a família de Dale em Chattanooga;
- o Corolla e o combustível;
- o .38 e as balas;
- o sonho dos pais de Sophie;
- a morte de Ryan;
- os animais e o campo magnético;
- a caverna trancada;
- as passagens apertadas;
- o "dia calmo";
- Jonas e o padre na St. Luke's.

**Ganchos para o Livro Três:** o que aconteceu lá fora; os pais de Noah; Harrison; o Hangar 4; o SOMA; Blanding; a St. Luke's; Marcus e a emissora; o romance de Ethan e Sophie; reconstruir ou fugir.

---

# DECISÕES (para `decisoes.md`)

Crie uma tabela com: decisão, status (DECIDIDO, ABERTO ou PROPOSTO), opções, recomendação e consequências. Preencha assim:

**Decidido pelo autor:**
- Os personagens chegam à caverna e se salvam.
- O evento principal acontece enquanto estão debaixo da terra, e eles não veem o que acontece lá fora.
- O final tem Kate, Lucas, Emma, Sophie, Ethan, Noah e um cachorro juntos.
- O livro tem muita tensão humana (armas, pessoas fugindo e desesperadas), não só de clima.

**Proposto (recomendação, a confirmar):**
- Os grupos se reencontram no dia 18 (rota híbrida).
- A cachorra é Pepper, dos Nguyen.
- Blanding cai, mas Jimmy Warren ajuda.
- O clarão acontece na noite americana.
- Um único tiro do .38 em todo o livro, e ele custa caro.
- Noah fica com sequela no braço.
- Curtis Hale fica do lado de fora da caverna.
- Ruth lidera o outro grupo.
- O beijo acontece na caverna.
- Título: *The Turning* (*A Virada*).
- Sobrenome de Noah: Calloway.

**Aberto:**
- A causa da morte de Ryan.
- O que Sophie perguntou ao padre.
- Se Harrison reaparece.
- Se Mara Voss existe.
- Se o Pastor Reddick existe.
- Quem morre no grupo da caverna.
- O destino dos Nguyen.
- O que diz a última transmissão.
- Qual dos finais (A a E).

**Deixe uma seção vazia "Decisões novas"** para o autor preencher. A skill deve sempre lê-la primeiro.

---

# CONTINUIDADE (para `continuidade.md`)

Crie inventários com valores iniciais em 17/05 às 5h e um campo "atual" que o autor atualiza:
- munição do .38 (6 balas e uma caixa);
- antibiótico (um frasco de amoxicilina com clavulanato de 875 mg, de 12 em 12 horas);
- ibuprofeno de 800 mg (uma caixa);
- comida (8 latas, um pote de pasta de amendoim, as rações de Dale);
- água (9 garrafas, dois galões do trio, mais a água de Dale);
- combustível (o tanque desconhecido do Corolla, porque o medidor está morto, e dois galões);
- relógios (quem tem um que funciona?);
- luz (a Maglite, lanternas, velas, pilhas);
- objetos-chave (o pen drive, a foto, a medalha, o caderno, o atlas, a bússola, os óculos de esqui, a parca vermelha, as luvas do padre, a jaqueta SGM WHITAKER);
- ferimentos de cada personagem.

Inclua também a lista de inconsistências do Livro Um a corrigir: "Canal 8" deve ser "Canal 13"; a audiência de duzentas mil ou de meio milhão; os anos de sacerdócio do padre Patrick.

---

## INSTRUÇÕES FINAIS PARA VOCÊ, MODELO QUE ESTÁ CRIANDO A SKILL

1. Escreva tudo em **português do Brasil**. Só os exemplos de prosa do livro, em `estilo.md`, devem vir em inglês e em português.
2. Em `estilo.md`, inclua **três parágrafos de exemplo originais** (não copiados do Livro Um) que mostrem a voz: um de tensão, um de ciência na boca de um personagem e um de ternura. Escreva cada um em inglês e em português.
3. Em `personagens.md`, inclua para cada personagem do núcleo **três frases típicas** que ele poderia dizer no Livro Dois.
4. Em `SKILL.md`, inclua uma seção **"Como começar"** com exemplos de pedidos do autor, como:
   - "Escreva o capítulo 3 em inglês."
   - "Quais são as opções para a cena do rio?"
   - "Revise este capítulo."
   - "Crie um personagem para o posto de controle."
   - "Registre que Ryan morreu numa emboscada no Iraque."
5. Não omita nenhuma informação da Bíblia da Série. Se precisar resumir, resuma a forma, nunca os fatos.
6. Ao terminar, liste o que ficou como decisão em aberto e pergunte ao autor por qual delas ele quer começar.
