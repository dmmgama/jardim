---
created: 2026-09-17
thread: T005
tipo: report
fase: 1
autor: agente da thread T005
destinatario: Arquitecto / David
summary: |
  Report da fase 1 da T005 — quatro pesquisas de estado da arte lançadas em paralelo
  (especialidades envolvidas, software de digital twin, monitorização e actuação, e
  levantamento por nuvem de pontos), mais uma análise prévia e uma síntese cruzada.
  Achado central: três pesquisas independentes convergiram, sem combinação, na mesma
  reclassificação do projecto — um jardim sobre laje impermeabilizada é tecnicamente
  uma cobertura ajardinada, com corpo normativo, modos de falha e ferramentas próprios
  que nenhum documento do projecto tinha. Consequência urgente: os +0,50 m estão
  fixados como cota mas não decompostos em camadas, e a decomposição é geometria — é
  matéria da T004, que está no caminho crítico da obra.
---

# REPORT T005 — Fase 1: pesquisa e definição de regras para caracterização do espaço

**Data:** 2026-09-17 · **Thread:** T005 · **Fase:** 1 de 2 · **Estado:** entregue ao Arquitecto

---

## 1. O que foi feito, e com que objectivo

### 1.1 O problema que motivou a thread

O projecto acumulou muita informação — o `DOSSIER-LOCAL.md` tem 827 linhas, há um modelo
solar em Python validado, um catálogo vegetal, pesquisas dispersas. **O problema não é falta
de informação. É que está organizada por objecto físico e por fenómeno** — geometria,
estruturas, água, superfícies, vegetação — **e não por disciplina.**

Essa organização descreve bem. **Falha noutra coisa: não sabe dizer quando pode parar.**

O dossier tem duas listas de lacunas (§10 «secções por instruir» e §12 «por inspeccionar»).
Ambas foram construídas **por observação do que não estava documentado**, não por confronto
com o que uma disciplina exige. Daí o ponto cego que a T005 existe para fechar:

> **Um parâmetro que ninguém se lembrou de procurar não aparece em lista nenhuma de lacunas.**

### 1.2 O objectivo da fase 1

**Não era recolher informação — era descobrir o que as disciplinas relevantes consideram ser
caracterização mínima**, antes de decidir o que se mede. Três frentes lançadas em paralelo,
com enunciados separados e sem conhecimento umas das outras:

1. **Quem são os especialistas** — que disciplinas intervêm, o que cada uma caracteriza, com
   que métodos e normas, e que decisões bloqueiam se não forem consultadas.
2. **Digital twin** — software open source e comercial que permita modelar o existente **e
   fazer experiências** («se eu puser esta árvore aqui, o que acontece à sombra?»).
3. **Monitorização e actuação** — do sensor ao actuador, com rega, iluminação e nutrição
   accionadas a partir de medições em contínuo.

**Uma quarta pesquisa foi encomendada a meio da sessão**, por instrução directa do David:
levantamento por **nuvem de pontos com equipamento profissional**, com o peso do enunciado
no pós-processamento.

### 1.3 Método

- **Paralelismo deliberado.** As frentes não se conheciam. **Convergência entre pesquisas
  independentes é evidência; convergência entre pesquisas que se leram é eco.**
- **Análise prévia escrita antes das pesquisas chegarem** (`00-PONTO-DE-PARTIDA.md`), de
  propósito — para ser possível testar depois se as respostas correspondiam à pergunta certa,
  sem contaminar o diagnóstico com o vocabulário das respostas.
- **Um teste de falsificação fixado à cabeça:** se a T005 não fizesse aparecer pelo menos um
  parâmetro ausente das duas listas de lacunas do dossier, teria produzido formatação.
- **Regra de rigor imposta a todas as pesquisas:** facto e fonte; «não apurado» em vez de
  estimativa; **instrução explícita para contrariar o enunciado se a evidência o exigisse.**

---

## 2. Sumário executivo

**1. Três pesquisas independentes convergiram na mesma reclassificação do projecto.** Um
jardim que sobe +0,50 m sobre laje impermeabilizada **é tecnicamente uma cobertura
ajardinada** — não um jardim de terreno. Isto activa um corpo normativo (FLL), um modo de
falha próprio (substrato fino seca em dias, não semanas) e uma ferramenta de simulação
gratuita (SWMM, módulo Green Roof) que **nenhum documento do projecto tinha.**

**2. O teste de falsificação passou.** A cobertura ajardinada não aparece em nenhuma das
listas de lacunas do dossier — **e não por descuido:** quando o dossier foi escrito, o jardim
ainda era de chão. Nenhum método de levantamento por observação a podia antecipar, porque a
coisa ainda não existe no espaço para ser observada.

**3. Há uma consequência urgente para a T004.** Os +0,50 m estão fixados como *cota* mas
**não decompostos em camadas** (drenante / filtrante / substrato). **A decomposição é
geometria, não acabamento** — define a cota final, o peso e o comportamento hidráulico. Já
sinalizado em `THREAD-MENSAGENS.md`.

**4. O conflito técnico mais valioso do projecto está identificado e por arbitrar:** retenção
de água para a planta *vs.* drenagem rápida para proteger a impermeabilização. **O mesmo
sistema mata a planta pelos dois lados.** Não há optimização — só arbitragem.

**5. A copa da palmeira bloqueia por três razões independentes**, não por uma: arboricultura,
modelação solar e sanidade fitossanitária. A quarta pesquisa diz **como medi-la**.

**6. Padrão transversal às quatro pesquisas:** a esta escala, a tentação é comprar a
ferramenta da escala acima. ENVI-met a 3.000 €/ano, LoRaWAN, fertirrega Dosatron a 3.799 €,
software de fabricante para nuvem de pontos — **todos cortados, com alternativa gratuita ou
de dezenas de euros.**

---

## 3. As pesquisas

| # | Título | Objectivo do prompt | Resumo extraído | Ficheiro |
|---|---|---|---|---|
| **00** | **Ponto de partida** | *(não é pesquisa — análise própria)* Diagnosticar a estrutura de informação existente **antes** de as pesquisas chegarem, para poder testar se respondem à pergunta certa. | O dossier está organizado por objecto físico e fenómeno. Descreve bem, mas **não sabe dizer quando pode parar**: o semáforo 🟢🟡🔴 mede fiabilidade da *fonte*, não tolerância do *valor*. Fixou o teste de falsificação da thread. | [[00-PONTO-DE-PARTIDA]] |
| **01** | **Especialidades envolvidas** | Mapear exaustivamente que disciplinas intervêm na caracterização deste espaço: o que cada uma caracteriza, métodos, normas (com equivalente português), fase de intervenção, e que decisões bloqueiam. Atenção especial ao caso de jardim sobre laje. | **16 disciplinas.** Abriu uma secção não pedida — «**§6-bis. Impermeabilização de coberturas ajardinadas — a disciplina que faltava nomear**» — e pô-la em **#1 das cinco que mais valem**. Matriz de conflitos entre disciplinas, com *retenção vs. drenagem* marcado como «o conflito mais valioso identificado». Fitopatologia é **a única disciplina com obrigação legal externa confirmada**. | [[01-ESPECIALIDADES]] |
| **02** | **Digital twin — software** | Levantar software open source e comercial para modelar o jardim e **fazer experiências**: geometria, sol, vegetação, água, microclima, luminância, captura, plataformas integradas, cola Python. Cepticismo obrigatório sobre o termo «digital twin». | **Não existe plataforma única a esta escala** — «digital twin» é uma arquitectura de ficheiros e scripts que se monta. Recomenda pilha Rhino + Grasshopper + Ladybug/Honeybee (≈1.800-2.500 €, investimento único). Identificou a **vegetação como «o eixo mais subestimado»**: cilindro *vs.* copa real muda o resultado da análise de sombra. Encontrou SWMM com módulo **Green Roof** e SOLWEIG/UMEP gratuito em vez de ENVI-met a 3.000 €/ano. | [[02-DIGITAL-TWIN-SOFTWARE]] |
| **03** | **Monitorização e actuação** | Do sensor ao actuador: o que se mede e com quê, como se transmite, onde vive a inteligência, o que se acciona, estratégias de controlo. Três configurações com custo. **O que NÃO vale a pena medir.** Modos de falha. | **A humidade do substrato é o parâmetro mestre** — o único cuja falha mata plantas em dias. Achado mais valioso: **detecção acústica precoce do escaravelho da palmeira, >90% de sucesso** em ensaios publicados, capaz de detectar larvas com duas semanas. Recomenda Home Assistant + ESPHome **locais, sem cloud**. Corta fertirrega, LoRaWAN, CO2, NDVI e sensores de vegetação. Classifica modos de falha em «**mata**» *vs.* «só irrita». | [[03-MONITORIZACAO-ACTUACAO]] |
| **04** | **Nuvem de pontos** | *(encomendada a meio da sessão, por instrução do David)* Avaliar levantamento com **equipamento profissional** — TLS, SLAM, fotogrametria DSLR, drone — e, sobretudo, **como se trata o que daí vem**. Testar de novo a conclusão anterior sobre captura por telemóvel. | **Veredicto dividido:** vale a pena **para a copa da palmeira** (forma 3D real, erro de poucos cm); **não justifica sozinha para os muros** (telémetro de 30 € continua a ganhar). **Inversão de intuição:** o reboco liso é o **pior caso para fotogrametria e um dos melhores para TLS**. SLAM handheld ganha ao TLS de tripé (acesso pela casa, 7 degraus). **Cadeia de tratamento 100% gratuita em Windows 10** (CloudCompare até à malha). | [[04-NUVEM-DE-PONTOS]] |
| **05** | **Síntese cruzada** | *(não é pesquisa — produto da thread)* O que só aparece quando as quatro se cruzam. | A peça principal da fase 1. Documenta a convergência não encomendada, o conflito retenção-vs-drenagem, a tripla razão da palmeira, e propõe **dois campos novos** para a grelha da fase 2. | [[05-SINTESE-FASE-1]] |

### 3.1 Os prompts, em resumo

Todos partilharam o mesmo bloco de contexto factual (geometria do recinto, azimute, altura
solar, muros, árvores, a subida de +0,50 m sobre betonilha) e as mesmas regras de método:

- **Facto e fonte** — cada afirmação técnica com origem; WebSearch e WebFetch em profundidade.
- **«Não apurado» em vez de estimativa.** Proibição explícita de inventar preços, normas ou
  designações. **Um buraco declarado vale mais que um plausível inventado.**
- **Distinguir facto de interpretação**, sempre.
- **Contexto português e mediterrânico** quando exista; assinalar quando a fonte internacional
  não transpõe bem.
- **Licença para contrariar o enunciado.** Dada a todas, com o precedente citado: uma pesquisa
  anterior contrariou o pedido com que foi encomendada e a correcção foi aceite e valorizada.
- **Secção obrigatória «o que NÃO vale a pena»**, com conteúdo real.

---

## 4. O meu report sobre o que recebi

### 4.1 A convergência — e porque é que ela é o resultado, não um detalhe

**As três primeiras pesquisas chegaram independentemente à mesma reclassificação.** Nenhuma
foi instruída a fazê-lo; o facto dos +0,50 m entrou nos três enunciados como contexto.

| Pesquisa | O que disse, sem saber das outras |
|---|---|
| **01** | Abriu a secção **«§6-bis — a disciplina que faltava nomear»**, fora da lista que lhe dei, e classificou-a como **#1 das cinco que mais valem**: *«é a disciplina ausente do vocabulário do projecto e a que, se ignorada, produz o erro mais caro e mais difícil de corrigir depois de construído.»* |
| **02** | *«O jardim sobe +0,50 m sobre laje — isto é, estruturalmente, uma cobertura verde em escala doméstica.»* E tirou daí a ferramenta: SWMM tem módulo Green Roof dedicado e gratuito. |
| **03** | *«Substratos finos falham cedo e falham mal em clima mediterrânico, porque não há reserva de água lateral nem drenagem profunda para absorver um erro.»* |

**Grau de certeza: alto.** Três enunciados separados, três domínios diferentes, a mesma
conclusão. É a natureza do objecto a impor-se, não opinião de um analista.

**O que isto significa em termos práticos:** o projecto tem estado a raciocinar sobre o jardim
com o vocabulário errado. Não «errado» no sentido de falso — os factos do dossier mantêm-se —
mas **incompleto de uma maneira que não é detectável de dentro**, porque o que falta não está
no espaço para ser observado.

### 4.2 O conflito que manda, e que ninguém arbitrou

Citando a pesquisa 01, que o marca como o achado mais valioso da sua matriz:

> **Retenção de água para vegetação vs. drenagem rápida para proteger a impermeabilização.**
> O substrato ideal para a planta retém água; o ideal para a laje escoa depressa. A FLL
> resolve com camadas sobrepostas, **mas a espessura de cada camada é uma decisão de
> compromisso, não uma optimização única — e ainda não foi tomada neste projecto.**

**As outras duas pesquisas confirmam os dois lados sem saberem que alimentavam um conflito:**

- **Lado da planta (03):** num substrato de 0,50 m sobre laje, **a humidade é o único parâmetro
  cuja falha mata plantas em dias.** Não há reserva lateral. Um erro de rega em Agosto não se
  corrige na semana seguinte.
- **Lado da laje (03, modos de falha):** sensor preso a «seco», rega em excesso contínua, e
  **sobre laje impermeável a água acumula sem drenar** — asfixia radicular e sobrecarga de peso.

**Grau de certeza: alto quanto à existência do conflito; nulo quanto à solução.** A arbitragem
exige dados que o projecto não tem (percolação, carga admissível da laje, escolha de substrato).

### 4.3 A consequência urgente para a T004

**Interpretação minha, sinalizada como tal:** se a T004 desenhar os 50 cm como um bloco
homogéneo de terra, desenha uma coisa que não vai ser construída assim. `ESTADO.md` §02 diz
«o jardim sobe +0,50 m por cima dela»; §04 fixa os quatro planos de cota. **Em lado nenhum se
diz quanto disso é dreno, quanto é filtro e quanto é terra.**

**Não proponho espessuras** — não é o meu mandato e não tenho os dados. Sinalizo que **falta
uma decisão que a geometria pressupõe**, e que a obra tem relógio a contar.

### 4.4 A palmeira — três razões independentes

| Pesquisa | Razão |
|---|---|
| **01** | *«Não há como resolver este conflito sem primeiro medir a árvore.»* E: subir a cota à volta de um tronco existente é **«uma das causas mais comuns e mais lentas de declínio arbóreo»**. |
| **02** | Cilindro *vs.* copa real **muda o resultado da análise de sombra** — não é detalhe estético. |
| **03** | Detecção acústica de *R. ferrugineus* com **>90% de sucesso**; e o argumento económico: sendo a palmeira dado fixo de projecto, **o limiar de «vale a pena» é muito mais permissivo aqui.** |

**Grau de certeza: alto.** Três domínios, três razões que não dependem umas das outras.

### 4.5 A quarta pesquisa — a inversão de intuição

**Citando directamente:** o reboco liso sem textura é **o pior caso possível para fotogrametria
e um dos melhores para TLS.** A fotogrametria procura pontos homólogos e não os encontra numa
superfície homogénea — **é limitação do método, não da câmara.** O TLS mede tempo de voo do
laser e não precisa de textura; investigação dedicada mostra que rebocos **com** textura dão
**~26% mais dispersão** que rebocos lisos.

> **Isto não contradiz `REJEICOES.md` §11.** A rejeição registada era de **captura por
> telemóvel**, e mantém-se intacta. O que separa os dois casos é **física da superfície, não
> qualidade de equipamento.** Não peço reabertura da rejeição — peço que fique claro que ela
> não cobre este caso.

**Grau de certeza: alto quanto à física; médio quanto à execução.** O número de estações TLS
para este recinto é **extrapolação de protocolos florestais, não valor verificado**; e o erro
de folhagem em movimento com vento não foi quantificado em fonte nenhuma.

### 4.6 Tensões que ficam por resolver

| # | Tensão | Estado |
|---|---|---|
| **T1** | **Sensor lux *vs.* modelo solar da T003.** Ambos produzem «horas de sol por zona», por vias diferentes. | **Não é conflito, é validação.** A pesquisa 03 declarou a fronteira e **recusou-se a arbitrá-la**, como instruído. Proposta para a fase 2. |
| **T2** | **Python existente *vs.* Rhino/Ladybug.** A 02 recomenda Rhino (≈1.800-2.500 €) mas admite que a pilha só-Python é «a segunda escolha honesta», porque já existe modelo validado. | **Decisão do Arquitecto.** Registo o facto técnico: o modelo da T002 resolve posição solar e **não** resolve sombreamento por geometria 3D complexa — que é o que a copa exige. |
| **T3** | **Custo de instrumentação *vs.* orçamento inexistente.** A 03 recomenda ≈460-800 €; a 04 exige aluguer de máquina com preço não apurado. | **`ESTADO.md` §10: o filtro de custo nunca foi aplicado a V2.** A T005 sinaliza que estas recomendações entram numa conta que ainda não existe. |
| **T4** | **Sobreposição T003 × T005.** A 02 pesquisou software que inclui a parte solar, que é da T003. | **Declarada em `ESTADO.md` §11, não arbitrada.** É do Arquitecto, e por instrução dele: depois de ver as duas. |

### 4.7 Grau de certeza, por bloco

| Bloco | Certeza | Porquê |
|---|---|---|
| **Reclassificação como cobertura ajardinada** | **Alta** | Convergência de três pesquisas independentes. |
| **Existência do conflito retenção/drenagem** | **Alta** | Identificado por uma, confirmado nos dois lados por outra, sem coordenação. |
| **A tripla razão da palmeira** | **Alta** | Três domínios independentes. |
| **Física TLS *vs.* fotogrametria** | **Alta** | Investigação dedicada citada, com número (~26%). |
| **Espessuras de camadas concretas** | **Nula** | **Ninguém as propôs. Exigem dados que não existem.** |
| **Preços e custos** | **Baixa a média** | Muito «não apurado»: aluguer em PT, Picusan, The Grove, ClimateStudio, estação meteorológica. |
| **Número de estações TLS para este recinto** | **Baixa** | Extrapolação declarada, não valor verificado. |
| **Detecção acústica como compra concreta** | **Média** | A eficácia está publicada; **a disponibilidade comercial a particular em Portugal não foi confirmada.** |

### 4.8 Uma auto-crítica, para constar

O risco registado à cabeça no mandato era **«produzir uma enciclopédia em vez de uma regra»**.
Quatro pesquisas densas são exactamente o material com que se produz uma enciclopédia. **A
fase 1 ainda não falhou nesse teste, mas também ainda não o passou** — quem o passa ou falha é
a fase 2, e o critério é simples: **uma grelha de oito parâmetros que se preenche numa tarde
vale mais que uma de trinta que ninguém preenche.**

---

## 5. Conclusão

**A T005 justificou-se pelo teste que ela própria fixou antes de começar.**

Estava escrito em `00-PONTO-DE-PARTIDA.md`, antes de qualquer pesquisa ter chegado, que a
thread só valeria a pena se fizesse aparecer **pelo menos um parâmetro ausente das duas listas
de lacunas do dossier**. Apareceu — e não um qualquer: **a natureza técnica do objecto que se
vai construir.**

E apareceu **exactamente pela razão que motivou a thread**: as listas de lacunas do dossier
foram construídas por observação do que não estava documentado. **A cobertura ajardinada não
podia lá estar, porque não há nada no espaço para observar.** Só aparece a quem pergunte *«que
disciplina trata disto, e o que é que ela exige saber?»* — que é a pergunta que a T005 existe
para fazer.

**O que muda concretamente no projecto:**

1. O vocabulário técnico — deixa de ser «jardim» e passa a ser «cobertura ajardinada», com
   normativo e modos de falha próprios.
2. **Uma decisão de geometria que falta à T004**, com relógio a contar.
3. Um conflito técnico central identificado e por arbitrar.
4. Um método concreto para medir a copa da palmeira, com cadeia de tratamento gratuita.
5. Uma obrigação legal externa que não estava registada em lado nenhum.

**O que não mudou e não devia mudar:** nenhum facto do `DOSSIER-LOCAL.md` foi contrariado. A
T005 não reescreveu nada, não mediu nada e não decidiu nada de projecto. **Acrescentou a
grelha pela qual o que já existe passa a poder ser avaliado.**

---

## 6. Próximos passos

### 6.1 Do Arquitecto — três pedidos em aberto

| # | Pedido | Urgência |
|---|---|---|
| **A1** | **Encaminhar à T004 a questão das camadas.** Os +0,50 m como cota *vs.* decomposição drenante/filtrante/substrato. | ⚠ **URGENTE** — único item com relógio a contar. |
| **A2** | **Ler a síntese** ([[05-SINTESE-FASE-1]]) antes de instruir a fase 2. | Alta |
| **A3** | **Instruir ou adiar a fase 2.** O mandato proíbe arrancá-la sem o Arquitecto ver a fase 1 — **e não arranco.** | Alta |

### 6.2 Proposta para a fase 2 — a grelha, com dois campos novos

A grelha proposta em `00-PONTO-DE-PARTIDA.md` **confirma-se na forma e corrige-se no
conteúdo** — faltavam dois campos, ambos revelados pelo cruzamento:

| Campo | Estado | Porquê |
|---|---|---|
| Parâmetro · Disciplina · Para que decisão serve · Método · Tolerância exigida · Critério de suficiência · Estado actual · Custo | **Confirmados** | Proposta original |
| **Quando tem de estar medido** *(antes da obra / durante / depois)* | **Novo** | A 03 mostra que condutas, cabos e passagens **têm de ser decididos ao mesmo tempo que a geometria** — depois de impermeabilizado e coberto, é obra a refazer. **Um parâmetro com a tolerância certa e o timing errado é inútil.** |
| **O que acontece se estiver errado** *(classe de falha)* | **Novo** | «Mata» *vs.* «só irrita». **Este campo reordena a lista inteira: a consequência do erro deve mandar, não o custo de medir.** |

### 6.3 Decisões que não são da T005, mas que a fase 1 põe na mesa

| # | Decisão | De quem | Nota |
|---|---|---|---|
| **D1** | **Arbitrar a sobreposição T003 × T005** | Arquitecto | Declarada em `ESTADO.md` §11. Depois de ver as duas. |
| **D2** | **Alugar ou não máquina de varrimento** | David / Arquitecto | **Custo em PT não apurado** — exige telefonar a Topogis, Grupo Acre ou Geonorth. Vale para a copa; não vale só pelos muros. |
| **D3** | **Rever a compra do Apogee DLI-500 (≈460 €)** | Arquitecto | A 03 sugere **um** sensor de referência a calibrar vários BH1750 de 6 € — o problema é variabilidade espacial, não precisão pontual. Ver `INBOX.md`. |
| **D4** | **Escolher a pilha de modelação** | Arquitecto | Rhino (≈1.800-2.500 €, único) *vs.* só-Python (0 €, mais montagem manual). |
| **D5** | **Orçamento de V2** | Arquitecto | O filtro de custo **nunca foi aplicado**. Todas as recomendações desta fase entram numa conta que não existe. |

### 6.4 O que não depende de ninguém, e continua a ser o melhor negócio do projecto

> **A copa da palmeira continua por medir e continua a custar uma hora.**
>
> Bloqueia a T004, bloqueia o pedido 5 à T003, impede avaliar o risco de soterrar o colo e
> impede dimensionar a carga.
>
> **Há dois caminhos e não competem:** fita, vara e fotografia resolvem a **projecção
> horizontal** e desbloqueiam a T004 numa tarde; a nuvem de pontos resolve a **forma 3D**, que
> é o que o motor solar precisa. **Se a máquina demorar, a T004 não tem de esperar por ela.**

---

## Anexo — inventário de ficheiros da fase 1

| Ficheiro | Tipo | Linhas |
|---|---|---|
| [[00-PONTO-DE-PARTIDA]] | Análise prévia | 150 |
| [[01-ESPECIALIDADES]] | Pesquisa | 984 |
| [[02-DIGITAL-TWIN-SOFTWARE]] | Pesquisa | 232 |
| [[03-MONITORIZACAO-ACTUACAO]] | Pesquisa | 481 |
| [[04-NUVEM-DE-PONTOS]] | Pesquisa | 654 |
| [[05-SINTESE-FASE-1]] | Síntese | 272 |
| `mensagens.md` | Canal com o Arquitecto | — |
| `thread.md` | Mandato, estado e handoff | — |

**Commits:** `fb07883` (abertura) · `e8e8d2a` (fase 1) · `9645572` (nuvem de pontos)
