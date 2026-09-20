---
created: 2026-09-19 20:05
revised: 2026-09-20 06:10
chat: Arquitectura de governo de projectos com agentes
summary: >
  Arquitectura de governo para projectos multi-frente conduzidos por agentes: definições,
  mandato, árvore (definição, porta de entrada, roteamento e modos), caminho, desenvolvimento
  por níveis, evolução, regra de saída, garantias, auditoria, tensões e esquemas dos ficheiros.
---

# Arquitectura de governo de projectos com agentes

**Convenção de leitura.** Cada §2.x tem três blocos, por esta ordem: *Conceitos* (define o que as regras usam), *Regras* (só alíneas identificadas `Pn.m`, cada uma com detector e consequência) e *Nota* (racional; não vincula). Uma obrigação só existe se tiver identificador; prosa a negrito não obriga.

**Vocabulário normativo.** **deve** = obrigatório; **não pode** = proibido; **pode** = permitido.

**Colunas das regras.** *Detector* ∈ {hook, gate, watcher, auditor, humano}. *Consequência* ∈ {bloqueia, fecha com marca, alerta, relatório}.

**Numeração aditiva.** Uma regra nova recebe o número seguinte do seu protocolo. Nunca se insere no meio, nunca se renumera. Uma regra retirada mantém o identificador com grau `morto` (P5.5).

---

## 0 · Definições

Entrada única por termo. Todos os usos posteriores remetem para aqui.

| Termo | Definição |
|---|---|
| **Frente** | Unidade de trabalho de nível L3 que testa um pressuposto ou executa um caminho. Tem projecção, zona e gate de fecho. |
| **Ramo** | Nó de uma árvore. Estados: `por abrir`, `em desenvolvimento`, `fechado`, `podado`, `retido`, `suspenso: <ramo>`. |
| **`suspenso: <ramo>`** | Ramo bloqueado por dependência declarada. Tem sempre referente. |
| **`retido`** | Ramo que não discrimina, guardado sem poda. Não tem referente. Só em modo Caracterização. |
| **Aresta** | Dependência declarada entre ramos (P1.4). |
| **Cone** | Conjunto de ramos alcançáveis a jusante por travessia de arestas a partir de um ramo. |
| **Driver** | Variável cuja variação muda o resultado. Um corte não a deve repartir por ramos. |
| **Transversal** | Factor que condiciona todos os ramos de uma árvore. Declara-se ao nível da árvore, com slug; não é ramo nem aresta (P1.10). |
| **Modo de árvore** | Um de Problema, Caracterização, Decisão, Mandato (§2.2.1). Determina raiz, forma, crivo, poda e morte. |
| **Árvore** | Partição de um espaço por eixos. Quatro modos (§2.2.1). Detalhe operacional no canon `protocolo-arvore-definicao-e-uso` v2. |
| **Eixo** | Critério de divisão de um nó em ramos. |
| **Caminho** | Hipótese, hoje, sobre como se chega ao mandato (§2.3). Nunca designa uma localização no sistema de ficheiros. |
| **Trajecto** | Localização no sistema de ficheiros. O *hook de trajecto* confina leitura e escrita por perfil. |
| **Pressuposto** | Afirmação que tem de ser verdade para um caminho valer. Estados: `por testar`, `confirmado`, `invalidado`, `inconclusivo`. |
| **Discriminante** | Pressuposto cuja resposta elimina caminhos. |
| **Regra de paragem** | Critério, escrito antes de a frente abrir, que dá o teste de um pressuposto por decidido. |
| **Projecção** | O objectivo de uma frente: o pressuposto que testa mais a regra de paragem. Fronteiras negativas: os pressupostos atribuídos às outras frentes. Deriva-se do caminho; não se redige. Único nome deste conceito. |
| **Perfil** | Papel que uma sessão declara ao arrancar (`frente`, `triagem`, `rumo`, `auditor`). Determina o contexto montado e a zona. |
| **Zona** | Conjunto de trajectos onde um perfil pode escrever. Declaradas em "Perfis e zonas" (§2.1.1). |
| **Toca** | Lista de slugs e trajectos que uma frente declara ir alterar. Base da passagem de colisão. |
| **Slug** | Identificador global e único de documentos, regras, decisões, ramos e pressupostos. Nunca reutilizado nem renumerado. |
| **Alerta** | Item produzido pelo watcher em `ALERTA`. O seu estado vive em `ALERTA-ESTADO`. |
| **Triagem** | Actor: sessão fria de agente, disparada por alerta, que escreve `ESTADO`, `FRENTES`, `REJEICOES`, `CASOS`, `ALERTA-ESTADO`. Designa só o actor. |
| **Crivo de ordem de grandeza** | Filtro pré-dados que descarta um ramo cuja variação por um factor de dez não alteraria a causa provável (Problema) ou a opção escolhida (Decisão). Não é a triagem. O canon operacional chama-lhe "triagem". |
| **Watcher** | Script sem modelo, disparado a cada merge, que corre as três passagens de detecção (§2.4.8). |
| **Detector semântico** | Chamada única de modelo, sem estado, invocada pelo watcher. Devolve sugestão, nunca facto. |
| **Gate** | Verificação no fecho de sessão (S5). Dois patamares: *duro* bloqueia o fecho; *brando* fecha com marca. |
| **Cold-read** | Verificação de um output por agente sem histórico, com pergunta fechada sobre a acção seguinte. Valor: `passa` ou `falha`. |
| **`carece_aprovacao`** | Marca que um fecho brando deixa em `estado.json`. |
| **Modo rumo** | Sessão aberta só pelo humano para reavaliar o mandato. Produz emenda ou nada. |
| **Emenda** | Alteração datada ao `MANDATO`, com decisão em `debates/` que regista a alternativa rejeitada. |
| **Sonda de fronteira** | Tarefa-fronteira classificada por três sessões limpas contra o mandato: o teste de discriminação (§2.1.1) repetido em auditoria. |
| **Página** | 500 palavras, contadas pelo hook. Aplica-se a `MANDATO` e `CAMINHO`. |
| **Worktree** | Cópia de trabalho isolada de uma frente. O merge é a verificação. |
| **ME / CE** | Mutuamente exclusivo / colectivamente exaustivo. |
| **Nível** | Só designa L0–L4 (§2.4.1). Os patamares do gate e os graus de protecção não são níveis. |
| **Grau de protecção** | Estado de um slug face ao índice de decisões: `livre`, `decidido`, `selado`, `morto` (§2.4.8). |
| **Incidente** | Item de `INBOX` do tipo `falha_de_sistema`. Pré-condição de qualquer regra nova (P5.4). |

---

## 1 · Mandato deste documento

### 1.1 Porque existe

Um projecto conduzido por várias sessões de agentes perde o objectivo sem que ninguém decida perdê-lo. Não há um momento de falha: há acumulação. Ao fim de algumas semanas o projecto é uma lista de tarefas que geram tarefas, e ninguém sabe dizer para que serve nenhuma delas.

Este documento descreve o sistema que impede isso.

### 1.2 Sintomas que resolve

| Sintoma | Mecanismo subjacente |
|---|---|
| Tarefas geram tarefas sem se saber para que servem | o objectivo não chega à sessão, ou chega e é reinterpretado |
| Não se sabe porque se escolheu este caminho e não outro | as frentes derivam do mandato sem camada de estratégia |
| O problema foi atacado por um ângulo só | não se geraram alternativas antes de decidir |
| Sessões contradizem-se sobre factos do projecto | o estado acumula em vez de ser substituído |
| Ficheiros de registo que ninguém lê | escrever é grátis e não há árbitro |
| Duas frentes a mexer na mesma coisa sem saberem | nada cruza o que cada uma declara tocar |
| Uma frente conclui algo que invalida outra, e ninguém liga | as dependências entre ramos não estão declaradas |
| Decisões tomadas e nunca aplicadas | o fecho não verifica aplicação |
| Becos sem saída reabertos meses depois | o fecho de uma frente não regista a razão |
| Regras de governo alteradas sem se saber que foram debatidas | nada liga documentos a decisões |
| Governo que cresce mais depressa que o projecto | procedimentos sem teste de utilidade |

### 1.3 O que este sistema não faz

- Não impede uma frente de fazer a coisa errada dentro da sua própria zona.
- Não substitui julgamento humano sobre o rumo.
- Não se aplica a projectos de frente única: sem paralelismo, a maior parte dos mecanismos não tem o que detectar.
- Não garante qualidade do trabalho. Garante alinhamento e rastreabilidade.

### 1.4 Critérios de sucesso

| Critério | Medição | Garantia (§3.1) |
|---|---|---|
| Retoma a frio | uma sessão sem histórico retoma qualquer frente a partir do handoff | G17 |
| Alerta silencioso | `ALERTA` vazio é o caso normal, não a excepção | G11 |
| Zero decisões órfãs | nenhuma sessão fecha com decisão registada e não aplicada | G12 |
| Caminho vivo | todo o pressuposto invalidado produziu reavaliação registada | G6 |
| Árvores mortais | nenhuma árvore aberta sem condição de morte declarada | G5 |
| Rumo rastreável | toda a alteração ao mandato tem data e alternativa rejeitada registada | G14 |
| Detecção rápida | conflito entre frentes sinalizado no fecho seguinte | G11 |
| Governo estável | o corpo de regras não cresce sem um modo de falha observado | G16 |

*Nota.* Se o alerta dispara sempre, o detector está mal calibrado. Se nunca dispara e há colisões reais, as declarações estão mal preenchidas. Ambos são falhas do sistema, não do projecto. A calibração é item da auditoria (P7.2, proporção de alertas descartados).

### 1.5 Mapa do documento

| Protocolo | Secção | Regras | Garantias que sustenta |
|---|---|---|---|
| P0 · Nascimento | §2.1.2 | P0.1–P0.8 | G1, G2 |
| P1 · Árvore | §2.2.2 | P1.1–P1.11 | G4, G5, G11, G13 |
| P2 · Caminho | §2.3.2 | P2.1–P2.7 | G6, G11 |
| P3 · Desenvolvimento | §2.4.9 | P3.1–P3.17 | G3, G7, G8, G9, G10, G11, G12 |
| P4 · Alocação de papéis | §2.4.10 | P4.1–P4.5 | G7, G15 |
| P5 · Evolução | §2.5.6 | P5.1–P5.6 | G8, G13, G14, G16 |
| P6 · Saída | §2.6 | P6.1–P6.2 | G17 |
| P7 · Auditoria | §3.2 | P7.1–P7.4 | G2, G16 e manutenção de G4, G5, G9, G12, G13, G15 |

Esquemas dos ficheiros: Anexo A.

---

## 2 · Arquitectura

### 2.1 Nascimento do projecto

Nada arranca antes desta fase estar fechada.

#### 2.1.1 Conceitos

**O que é preciso estabelecer**

| Artefacto | Conteúdo | Quem escreve |
|---|---|---|
| `MANDATO` | objectivos, não-objectivos, critério de fim, data de desbloqueio | agente, por reformulação; autoria do humano |
| `CASOS` | vazio no arranque | preenchido por divergência |
| Perfis e zonas | que perfis existem e onde cada um escreve | o humano responsável |
| `HALT` | ausente; o trajecto existe | — |

Se o humano não conseguir enunciar o que quer, o mandato não se força: desenha-se uma árvore em modo Mandato (§2.2.1) e o mandato sai dela.

**Teste de reformulação.** O agente enuncia o mandato por palavras próprias e o humano confirma ou rejeita. Reformulação não é paráfrase: um agente que devolve as mesmas palavras por outra ordem não demonstrou nada. Compreendeu se consegue:

- derivar não-objectivos que o humano não enunciou, e acertar;
- classificar um caso-fronteira inventado na hora;
- dizer o que o mandato **exclui**, não apenas o que persegue;
- nomear a tensão entre dois objectivos e dizer qual cede.

**Teste de discriminação.** Três tarefas plausíveis: duas dentro do mandato, uma fora mas superficialmente parecida. Três sessões limpas, cada uma com o mandato e nada mais. As três classificam igual e correctamente: passa. Qualquer divergência: falha.

**Correcção em caso de falha.** Acrescentar não-objectivos e registar em `CASOS` a tarefa que gerou a divergência, com a classificação correcta. Nunca acrescentar princípios.

#### 2.1.2 Regras — Protocolo P0

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P0.1** | O mandato **deve** declarar entre um e cinco objectivos, cada um com slug. | hook (esquema, Anexo A) | bloqueia |
| **P0.2** | O mandato **deve** declarar dois a três não-objectivos por objectivo. | hook (esquema) | bloqueia |
| **P0.3** | O mandato **não pode** exceder uma página. | hook (contagem) | bloqueia |
| **P0.4** | O mandato **deve** declarar o critério pelo qual o projecto se considera terminado. | hook (esquema) | bloqueia |
| **P0.5** | O mandato **deve** ser redigido por agente, por reformulação da intenção do humano responsável. | humano | bloqueia |
| **P0.6** | O agente **não pode** acrescentar objectivo ou não-objectivo que o humano não tenha enunciado. | humano (teste de reformulação) | bloqueia |
| **P0.7** | O mandato **deve** passar o teste de reformulação e o teste de discriminação. | humano | bloqueia |
| **P0.8** | Uma frente **não pode** ser aberta antes de P0.7 devolver verdadeiro. | hook (campo `desbloqueado` do `MANDATO`) | bloqueia |

#### 2.1.3 Nota

Um projecto sem mandato produz trabalho, mas não produz alinhamento, e o custo só aparece semanas depois.

O quarto item do teste de reformulação é o mais difícil de fingir: qual objectivo cede numa colisão não está no texto, está na intenção. Falha em qualquer item devolve o mandato à discussão, não à reescrita: o que falhou foi a transmissão da intenção, não a redacção.

Um princípio novo aumenta o espaço interpretativo em vez de o reduzir. Por isso a correcção de uma falha é sempre não-objectivo ou caso, nunca princípio.

---

### 2.2 A árvore

Este documento define **o que é** uma árvore, **quando** se abre e **qual** se abre. O detalhe fino e operacional (cartões por modo, desempates entre concorrentes, regras comuns R1–R9 com acção de reparação) vive no canon `protocolo-arvore-definicao-e-uso` v2. Este §2.2 é o roteamento; aquele é o manual.

#### 2.2.1 Conceitos

Uma árvore é uma **partição de um espaço por eixos**. Não é um plano: o plano é o caminho. Não é um índice: o índice deriva do que existe. Não é o entregável decomposto. A árvore gera os cortes; o caminho testa-os.

**Porta de entrada: precisa-se de árvore?** Se qualquer sinal for verdadeiro, não se abre árvore nenhuma (P1.8).

| Sinal | Para onde vai |
|---|---|
| A definição do problema muda a cada interlocutor | ainda é mandato ou rumo; não é árvore |
| Não se consegue escrever a condição de morte | P1.1 impede |
| O que interessa só existe no todo (coerência, confiança, cultura) | não tem ramo possível |
| A causalidade tem retorno: X afecta Y que afecta X | cortar o ciclo **é** decidir; outra representação |
| Decisão pequena e reversível | o custo de estruturar excede o valor; decide-se |

**Roteamento: qual ou quais?** Quatro perguntas; podem sair várias, e é isso que responde a "de quantas árvores preciso".

```
Q1  Há um estado indesejado cuja causa se procura?
    âncora: "as entregas atrasam três semanas e não se sabe porquê"
      sim ──────────────────────────────────► modo PROBLEMA

Q2  O humano não consegue enunciar o que quer?
    âncora: "quero uma solução boa", sem dizer o que a faz boa
      sim ──────────────────────────────────► modo MANDATO (abre antes de tudo; morre antes de tudo)

Q3  Falta conhecer o objecto ou o terreno antes de se poder escolher?
    âncora: "não sabemos o que distingue uma boa proposta neste mercado"
      sim ──────────────────────────────────► modo CARACTERIZAÇÃO

Q4  Há opções nomeadas, postas na mesa por quem decide, entre as quais escolher?
    âncora: "A, B ou C: qual delas"
      sim ──────────────────────────────────► modo DECISÃO
```

Desempate: Q1 exige estado indesejado declarado; Q3 não tem estado indesejado, procura o que o objecto é. Saírem ambas é normal. Em Q4, opções implícitas, sugeridas pelo agente ou por gerar **não contam**: se ninguém as nomeou, o caso é Q2 ou Q3.

**Quantas, por que ordem, como acoplam**

| Saiu | Concorrentes | Ordem | Acoplamento |
|---|---|---|---|
| só Problema | ≥2 em Problema | — | — |
| só Caracterização | 1; não concorre | — | — |
| só Decisão | ≥2 em Decisão | — | — |
| Problema + Caracterização | ≥2 em Problema | Caracterização primeiro se a causa depende de terreno desconhecido; senão, em paralelo | ramos de Problema que dependem do terreno ficam `suspenso: <ramo>`; ao receber resultado, reavaliam com duas saídas: aprofundar ou podar |
| Problema + Decisão | ≥2 em cada | Problema primeiro; Decisão abre em paralelo com ramos suspensos | ramos de Decisão ficam `suspenso: <ramo de Problema>`; mesma reavaliação |
| Caracterização + Decisão | ≥2 em Decisão | Caracterização primeiro; Decisão abre em paralelo com ramos suspensos | ramos de Decisão ficam `suspenso: <ramo de Caracterização>`; mesma reavaliação |
| As três | ≥2 em Problema e em Decisão | Caracterização, depois Problema, depois Decisão; as três abrem já, com dependências declaradas (P1.4) | Decisão suspensa em Problema; Problema suspensa em Caracterização onde depende de terreno |
| Mandato, só ou acompanhado | 1; não concorre | morre primeiro, produz o `MANDATO`, e volta-se ao roteamento | nenhum; não acopla |

**Os quatro modos, em síntese**

| | **Problema** | **Caracterização** | **Decisão** | **Mandato** |
|---|---|---|---|---|
| Pergunta | porque é que isto acontece | o que é este objecto | qual destas | o que é que eu quero, afinal |
| Quando | Q1: estado indesejado com causa por achar | Q3: falta terreno antes de escolher | Q4: opções nomeadas por quem decide | Q2: o humano não enuncia o que quer |
| Raiz | pergunta fechada: *porque é que `<estado>`* | o objecto, não uma pergunta | a escolha, com espaço de opções declarado | o humano responsável |
| Eixos | um por nó | coexistem no 1.º nível; dois registos: eixos do real, eixos de preferência | um por nó | coexistem; obtidos por contraste entre exemplos, nas palavras do humano |
| ME / CE | ambos, estritos, dentro do eixo | dentro de cada eixo ambos; entre eixos nenhum | ME estrita; CE só sobre o espaço declarado | dentro do eixo ambos; conjunto de eixos aberto |
| Forma | fechada ao desenhar o nó | aberta; eixo novo é resultado | fechada sobre o espaço; opção nova reabre a raiz | aberta |
| Crivo | sim: *variando dez vezes, muda a causa provável?* | não; substitui-se por *este eixo discrimina bom de mau?* → senão `retido` | sim: *variando dez vezes, muda a opção?* | não; é generativa |
| Concorrência | ≥2 árvores com eixos distintos | não há | ≥2 árvores com eixos distintos | não há |
| Profundidade desigual | priorização | ritmos diferentes por eixo | alocação; o ramo raso fica registado | defeito |
| Poda | com razão no ramo | não enquanto aberta; `retido` | com razão; `suspenso` não se poda antes do referente devolver | nunca |
| Morte | causa confirmada, ou cone prioritário esgotado → escala ao humano | saturação: dois ciclos sem eixo novo | opção escolhida, com alternativa rejeitada | produz o `MANDATO`; não reabre |
| Entrega ao caminho | a causa, como pressuposto testável | significado: o que as opções passam a querer dizer aqui; não decide | a opção, como caminho ou pressuposto | o `MANDATO`; volta ao roteamento |

Folha, em Problema e Decisão: hipótese falsificável por **uma** análise discreta; se não é, ramifica mais. Uma árvore madura é maioritariamente morta: o ramo morto diz o que não se voltará a fazer.

#### 2.2.2 Regras — Protocolo P1

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P1.1** | Cada árvore **deve** declarar, ao nascer, o seu modo e a condição em que morre. | hook (esquema de `arvores/*`) | bloqueia |
| **P1.2** | Num nó de árvore em modo Problema ou Decisão **não pode** ser aplicado mais de um eixo de corte. | auditor | relatório |
| **P1.3** | Ramos irmãos dentro de um eixo **não podem** sobrepor-se. | auditor | relatório |
| **P1.4** | Um ramo **deve** declarar as suas dependências no momento em que é desenhado. | hook (campo `depende`); auditor (ramos não-raiz com lista vazia) | bloqueia; relatório |
| **P1.5** | Um ramo de árvore em modo Problema ou Decisão **não pode** passar a frente sem ter passado o crivo de ordem de grandeza. | hook (campo `crivo` do ramo) | bloqueia |
| **P1.6** | Um ramo podado **deve** registar a razão. | hook (esquema) | bloqueia |
| **P1.7** | Árvores de modo diferente **não podem** ser fundidas. | auditor | relatório |
| **P1.8** | Uma árvore **não pode** ser aberta com qualquer sinal da porta de entrada verdadeiro. | humano (abertura) | bloqueia |
| **P1.9** | Em modo Problema e em modo Decisão **devem** abrir-se duas ou mais árvores concorrentes com eixos distintos. | auditor | relatório |
| **P1.10** | Um factor que condiciona todos os ramos **deve** ser declarado `transversal` ao nível da árvore, com slug, e **não pode** ser ramo nem aresta. | hook (esquema); auditor (ramo com arestas para todos os irmãos) | bloqueia; relatório |
| **P1.11** | Uma árvore em modo Mandato **deve** morrer ao produzir o `MANDATO` e **não pode** reabrir. | hook (estado da árvore) | bloqueia |

#### 2.2.3 Nota

Uma árvore só, em Problema ou Decisão, é inércia, não escolha; o crivo mata as estéreis. Fundir Caracterização com Decisão faz com que a decisão nunca feche, porque há sempre mais para caracterizar. Sem razão de poda, o ramo volta dentro de dois meses com outro nome. Uma árvore sem condição de morte é eterna, e uma árvore eterna é a lista de tarefas que geram tarefas, com melhor genealogia.

O canon operacional usa "triagem" para o que aqui se chama crivo de ordem de grandeza; neste documento "triagem" designa só o actor (§0).

---

### 2.3 O caminho

#### 2.3.1 Conceitos

Entre o mandato e as frentes há uma camada que decide **por onde**. O caminho é a hipótese, hoje, sobre como se chega ao mandato: uma aposta entre apostas possíveis, com os pressupostos que a sustentam declarados e testáveis.

A árvore gera os cortes; o caminho testa-os. O crivo mata ramos antes de haver dados, de graça; o caminho testa com dados reais o que sobreviveu, e é caro.

**Método de procura**

```
MP1  Enunciar o mandato como pergunta de decisão
MP2  Desenhar as árvores concorrentes e passar as estéreis pelo crivo
MP3  Por árvore sobrevivente, extrair o que tem de ser verdade: os pressupostos
MP4  Marcar os discriminantes: pressupostos cuja resposta elimina caminhos
MP5  Ordenar por (incerteza × custo de descobrir tarde) ÷ custo de testar
MP6  A primeira frente testa o discriminante do topo
MP7  Aplicar P2.4
```

O discriminante de MP4 é o corte de maior assimetria da árvore que sobreviveu. As frentes derivam do caminho, não do mandato.

**`CAMINHO`**

| Campo | Conteúdo |
|---|---|
| Pergunta de decisão | o mandato reformulado como pergunta |
| Caminhos em aberto | dois ou mais, com uma linha cada |
| Caminho actual | um, ou `não escolhido` |
| Pressupostos | estado: `por testar`, `confirmado`, `invalidado`, `inconclusivo` |
| Ordem de ataque | os pressupostos por ordem de MP5 |
| Regras de paragem | por pressuposto, escritas antes de a frente abrir |

Uma página. Muda mais que o mandato, menos que o estado.

**Como se avalia.** Um milestone não é um entregável: é um teste de pressuposto.

| Resultado | Significado | Consequência |
|---|---|---|
| `confirmado` | o pressuposto aguenta | avança para o seguinte na ordem |
| `invalidado` | o pressuposto cai | reavaliação obrigatória (P2.5) |
| `inconclusivo` | o teste não decidiu | redesenhar o teste, não repetir |

**Como se reavalia.** Três disparos: pressuposto invalidado, cadência fixa (a auditoria, P7.1), ou vontade do humano.

```
reavaliação → quatro saídas, mutuamente exclusivas

  manter             nada mudou que altere a ordem
  reordenar          mudou a ordem de ataque, não o caminho
  trocar de caminho  o caminho actual cai; outro dos abertos assume
  escalar            o mandato é que está errado → modo rumo
```

Mudar de caminho não é mudar de rumo. Só a quarta saída toca no mandato.

#### 2.3.2 Regras — Protocolo P2

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P2.1** | O caminho **deve** declarar dois ou mais caminhos plausíveis. | hook (lê `CAMINHO` ao abrir frente) | bloqueia |
| **P2.2** | Cada frente **deve** declarar que pressuposto testa ou que caminho executa. | gate | bloqueia |
| **P2.3** | Cada pressuposto **deve** ter regra de paragem escrita antes de a frente abrir. | hook (abertura) | bloqueia |
| **P2.4** | Um caminho **não pode** ser declarado escolhido com discriminante por testar. | hook (esquema de `CAMINHO`) | bloqueia |
| **P2.5** | Um pressuposto invalidado **deve** disparar reavaliação antes de abrir frente nova. | hook (abertura: `invalidado` sem reavaliação datada) | bloqueia |
| **P2.6** | O caminho **não pode** exceder uma página. | hook (contagem) | bloqueia |
| **P2.7** | Cada frente **deve** declarar o que toca antes de abrir. | hook (abertura: campo `toca`) | bloqueia |

#### 2.3.3 Nota

Sem esta camada, cada frente deriva directamente do mandato e é uma aposta isolada que ninguém consegue avaliar. Juntar o crivo e o teste do caminho faz desaparecer o crivo e transforma todos os cortes em frentes.

O caminho não se escolhe no início. Escolhe-se depois do primeiro teste que elimina alternativas. Uma frente que não testa um pressuposto nem executa um caminho já escolhido não tem razão para existir.

A pergunta de um milestone não é *o que fica pronto* mas *o que fica a saber-se*. `inconclusivo` diz algo sobre o sistema, não sobre o projecto: a regra de paragem foi escrita sem critério verificável.

Separar mudança de caminho de mudança de rumo é o que evita que cada surpresa técnica se transforme numa discussão existencial.

---

### 2.4 Desenvolvimento

#### 2.4.1 Hierarquia

| Nível | Artefacto | Muda por | Ritmo |
|---|---|---|---|
| **L0 · Projecto** | `MANDATO` | emenda datada | meses |
| **L1 · Caminho** | `CAMINHO`, árvores | reavaliação | semanas |
| **L2 · Estado** | `ESTADO`, `FRENTES` | triagem | dias |
| **L3 · Frente** | `estado.json`, projecção | fecho de sessão | sessões |
| **L4 · Sessão** | worktree, `INBOX` | trabalho | horas |

O que sobe é um pedido, não uma alteração (P3.1).

#### 2.4.2 Escopo de contexto

Corolário da hierarquia: cada nível classifica o seu trabalho contra o nível imediatamente acima, nunca contra o topo (P3.2).

| Quem | Classifica contra | Não precisa de |
|---|---|---|
| Sessão | a projecção da frente | o caminho, o mandato |
| Frente | o pressuposto que testa e a regra de paragem | o mandato |
| Triagem | os ramos que o alerta toca | o projecto inteiro |
| Caminho | o mandato | a intenção por trás |
| Rumo | a intenção do humano | — |

Uma frente sem o mandato geral continua a detectar que derrapou, porque derrapar é sair do **seu pressuposto**. O item `pressuposto_caido` que emite no `INBOX` significa "o meu pressuposto caiu", não "o projecto está errado"; a tradução para eventual emenda é feita por quem tem o mandato.

**Uma excepção.** Os objectivos são escopáveis; os não-objectivos não (P3.3). Uma fronteira que não está carregada não bloqueia nada, e o erro provável não é cair fora de um objectivo específico: é cair fora do mandato todo.

#### 2.4.3 Actores

Tabela única de actores. §2.4.10 acrescenta requisitos de execução; não acrescenta actores.

| Actor | É agente | Dispara por | Escreve em |
|---|---|---|---|
| **Humano responsável** | não | vontade | tudo |
| **Arquitecto · triagem** | sim | alerta | `ESTADO`, `FRENTES`, `REJEICOES`, `CASOS`, `ALERTA-ESTADO` |
| **Arquitecto · rumo** | sim | só o humano | emenda ao `MANDATO` e `debates/`, ou nada. Nunca `ESTADO` (P5.2) |
| **Frente** | sim | trabalho | a sua worktree, `INBOX` |
| **Auditor** | sim | cadência (P7.1) | relatório |
| **Watcher** | não | cada merge | `ALERTA` |
| **Detector semântico** | não (chamada única) | o watcher | nada; devolve sugestão ao watcher |
| **Script de indexação** | não | cada merge | `indice-decisoes.json` |
| **Hook de trajecto** | não | arranque, leitura, escrita e fecho de sessão | `sealed/` |

O watcher não tem modelo. É um script. O processo que vigia está sempre ligado; o que julga é sempre uma sessão fria e curta (P4.1).

#### 2.4.4 Ferramentas

| Ferramenta | Função | Substitui |
|---|---|---|
| **Árvore** | partição do espaço, geração de cortes | ataque por um ângulo só |
| **Worktree** | isolamento, paralelismo, merge como verificação | disciplina de não mexer na pasta alheia |
| **Hook de trajecto** | confinamento de leitura e escrita por perfil | regras escritas em prosa |
| **Índice de decisões** | liga slugs a decisões; protege o que foi debatido | memória de quem estava presente |
| **Watcher** | cruzar declarações e seguir dependências | reuniões de coordenação |
| **Cold-read** | verificar auto-suficiência de um output | confiança |
| **Proveniência selada** | registo imutável, fora do índice de pesquisa | memória |
| **HALT** | paragem imediata de todas as escritas | — |

#### 2.4.5 Ficheiros

Esquema de cada ficheiro `.json`: Anexo A.

| Ficheiro | O que é | Escrita | Quem |
|---|---|---|---|
| `MANDATO` | a lei do projecto | emenda datada | agente redige, humano valida |
| `CAMINHO` | a hipótese de como se lá chega | substituição | humano com agente |
| `arvores/*` | partições do espaço, por modo | substituição | humano com agente |
| `CASOS` | casos-fronteira decididos | acrescento | humano, triagem |
| `ESTADO` | o que é verdade agora | substituição | triagem |
| `FRENTES` | índice de frentes e ramos | substituição | triagem |
| `REJEICOES` | o que foi descartado e porquê | acrescento | triagem |
| `ALERTA` | o que o watcher detectou na última corrida | substituição | watcher |
| `ALERTA-ESTADO` | estado de cada item de alerta, por hash do par | acrescento | triagem |
| `INBOX/*.json` | descobertas, pressupostos caídos e incidentes por processar | acrescento | frentes |
| `debates/*.json` | decisões, com alternativa rejeitada e o que afectam | acrescento | rumo |
| `indice-decisoes.json` | slug → decisão | gerado | script |
| `estado.json` | estado da frente face ao seu pressuposto | substituição | frente |
| `handoff.json` | como retomar | substituição | frente |
| `research/` | exploração | livre | frente |
| `entregue/` | o que sobe | acrescento | frente |
| `Rascunhos` | travão intra-sessão | termina vazio | frente |
| `sealed/` | pedido, output, referências | write-once | hook |
| `HALT` | interruptor | presença | humano |

Estado substitui-se, evidência acumula-se; nunca no mesmo ficheiro (P3.4). `research/` e `Rascunhos` existem para a exploração não contaminar o estado; não se disciplinam. A proveniência guarda referências, não conteúdo (P3.5).

#### 2.4.6 O que é importante e o que não é

| Importante | Não é importante |
|---|---|
| O que cada frente declara **tocar** e de que **depende** | o que cada frente fez |
| O que ficou **fechado ou podado** e porquê | o que ficou aberto na conversa |
| O **próximo passo** e o seu critério de conclusão | a narrativa do percurso |
| A **alternativa rejeitada** numa decisão | a discussão que levou à decisão |
| Que o alerta esteja **vazio** | quantos alertas já foram resolvidos |
| Que o output seja **auto-suficiente** | que a sessão tenha sido produtiva |
| Pressupostos **declarados** | pressupostos correctos |

A coluna da direita não é proibida. É o que não entra no estado curado: vive na proveniência selada, recuperável e não lida.

#### 2.4.7 Fluxos, do geral ao átomo

**L0–L2 · Projecto**

```
MANDATO → ÁRVORES → CAMINHO → frentes → merges → watcher → ALERTA

ALERTA vazio            → nada acontece
ALERTA com item         → triagem
triagem toca no mandato → escala ao humano (P3.15) → rumo → emenda → MANDATO
```

**L3 · Frente**

```
F1  Abre com projecção derivada do caminho
F2  Sessões de trabalho, N ≥ 1
F3  Fecho de cada sessão: gate (P3.16)
F4  Pressuposto resolvido → frente fecha → resultado ao caminho
```

**L4 · Sessão — o átomo**

```
S1  HALT presente?                    sim → recusa (P3.13)
S2  Perfil declarado?                 não → recusa
S3  Monta contexto por perfil e por escopo (P3.2, P3.3)
S4  Trabalha
      escrita fora da zona            → bloqueia, devolve zona, continua
      edição de slug com decisão      → conforme o grau de protecção (§2.4.8)
      dúvida                          → declara pressuposto, continua (P3.12)
      tema fora da projecção          → Rascunhos, volta ao tema
S5  Fecho (P3.16)
      toca fora do declarado          → não fecha
      sem pressuposto nem caminho     → não fecha
      Rascunhos não vazio             → não fecha
      pressuposto novo                → fecha com carece_aprovacao
      cold_read = falha               → fecha com carece_aprovacao
      trabalho continua               → handoff.json, validado por cold-read
S6  Sela, faz merge, dispara watcher (P3.17)
```

Não existe estado de espera (P3.12).

#### 2.4.8 Mecanismos

**Gate de fecho.** Dois patamares. Divergência dura, quando o que a frente tocou saiu do que declarou, ou o que produziu não serve pressuposto nenhum, bloqueia o fecho. Divergência branda, quando há pressuposto novo ou `cold_read = falha`, deixa fechar com a marca `carece_aprovacao` e sobe ao alerta. O primeiro protege o projecto; o segundo protege o ritmo.

**Detecção, três passagens.**

| Passagem | Base | Confiança | Apanha |
|---|---|---|---|
| Colisão | campo `toca` (P2.7) | facto | duas frentes na mesma coisa |
| Dependência | arestas da árvore (P1.4) | facto | conclusão que muda outro ramo |
| Semântico | chamada única de modelo | sugestão | o que ninguém declarou |

Quando uma frente fecha um ramo, o watcher segue as arestas declaradas e vê quem ficava à espera daquilo. Apanha o conflito sem colisão de ficheiros. O detector semântico é a rede de segurança: quando apanha um conflito que a árvore não previa, falta uma aresta.

**Alerta com estado.** `ALERTA` é substituído pelo watcher a cada corrida. `ALERTA-ESTADO` acumula, por hash do par, o estado `novo`, `visto` ou `descartado` que a triagem atribui (P3.10). Um item cujo hash está `descartado` não é reemitido (P3.11).

**Protecção do que foi decidido.** Tudo tem slug (P3.6). A decisão declara o que afecta; o índice é gerado por inversão (P3.7). Ao editar, o hook extrai o slug e consulta o índice (P3.8):

| Grau de protecção | Origem | Comportamento |
|---|---|---|
| `livre` | sem decisão | edita |
| `decidido` | decisão registada | alerta; a sessão continua e fecha com `carece_aprovacao` |
| `selado` | decisão com `selado` | bloqueia; só nova decisão desbloqueia |
| `morto` | slug retirado por decisão | bloqueia a recriação |

O alerta devolve o identificador da decisão e o facto de existir (P3.9). O agente recebe material para parar, não para formar opinião. Assim o contexto montado para a sessão não contém uma única referência a decisões e continua protegido.

Uma regra retirada sai da vista do agente e vive no arquivo com grau `morto` (P5.5). Limite: só apanha reintrodução pelo mesmo slug; ver T3.

**Cold-read.** Um agente sem histórico lê o output ou o handoff e responde a uma pergunta fechada (P6.2). Para um handoff: *consegues enunciar o próximo passo e o critério que o dá por feito?* Devolve `passa` ou `falha`.

**Paragem.** A presença de `HALT` faz o hook recusar arranque e qualquer escrita (P3.13). As sessões vivas ficam inertes na operação seguinte. Não se terminam processos: matar a meio deixa ficheiros parciais. `HALT` é removido à mão.

#### 2.4.9 Regras — Protocolo P3

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P3.1** | Um nível **não pode** escrever no nível acima. | hook | bloqueia |
| **P3.2** | O contexto de uma sessão **deve** ser montado por perfil e escopo (§2.4.2) e **não pode** incluir níveis acima do imediato. | hook | bloqueia |
| **P3.3** | Os não-objectivos **devem** ser carregados inteiros em toda a sessão que classifique. | hook | bloqueia |
| **P3.4** | Um ficheiro de substituição **não pode** acumular evidência; um ficheiro de acrescento **não pode** ser substituído. | hook (modo de escrita, §2.4.5) | bloqueia |
| **P3.5** | A proveniência selada **não pode** conter conteúdo reconstruível por ferramenta; só referências. | hook (selagem) | bloqueia |
| **P3.6** | Todo o artefacto **deve** ter slug; um slug **não pode** ser reutilizado nem renumerado. | hook | bloqueia |
| **P3.7** | `indice-decisoes.json` **não pode** ser escrito por agente. | hook (índice fora das zonas) | bloqueia |
| **P3.8** | Em cada edição o hook **deve** consultar o índice e aplicar o comportamento do grau de protecção (§2.4.8). | hook | bloqueia ou alerta |
| **P3.9** | O alerta de protecção **não pode** devolver o conteúdo do debate, a alternativa rejeitada nem a razão; só o identificador da decisão. | auditor (amostra de alertas) | relatório |
| **P3.10** | Cada item de `ALERTA` **deve** ter estado em `ALERTA-ESTADO`, com chave igual ao hash do par; só a triagem escreve. | hook | bloqueia |
| **P3.11** | O watcher **não pode** reemitir um item cujo hash está `descartado`. | auditor | relatório |
| **P3.12** | Uma sessão **não pode** ficar à espera de outro actor; declara o pressuposto que assumiu e prossegue. | gate (pressuposto novo) | fecha com marca |
| **P3.13** | Com `HALT` presente, o hook **deve** recusar arranque e qualquer escrita. | hook | bloqueia |
| **P3.14** | Os hooks, o índice de decisões e `HALT` **devem** residir fora de todas as zonas de escrita. | auditor | relatório |
| **P3.15** | A triagem **não pode** resolver um item que toque no mandato; escala ao humano e deixa o item `novo`. | hook (a triagem não tem zona em `MANDATO`) | bloqueia |
| **P3.16** | O gate **deve** bloquear o fecho em divergência dura e, em divergência branda, fechar com `carece_aprovacao` e produzir item em `ALERTA`. | gate | bloqueia; fecha com marca |
| **P3.17** | Todo o fecho **deve** selar, fazer merge e disparar o watcher. | auditor (sessões seladas sem corrida do watcher) | relatório |

#### 2.4.10 Escolha de agente por papel

Os papéis de §2.4.3 são funções, não produtos. Cada um tem requisitos que derivam da arquitectura, e é por eles que se escolhe onde corre.

**Seis critérios**

| Critério | Pergunta |
|---|---|
| Duração | o papel vive enquanto trabalha, ou tem de estar sempre ligado? |
| Disparo | quem o invoca: humano, evento, ou calendário? |
| Filesystem | precisa de worktree, git e ficheiros locais? |
| Enforcement | precisa de hooks que bloqueiem uma operação antes de executar? |
| Escopo | o contexto tem de ser montado por perfil e cortado? |
| Julgamento | o papel decide, ou só detecta? |

O critério de enforcement é eliminatório (P4.2).

**Requisitos por papel**

| Papel | Duração | Disparo | Precisa de | Natural em |
|---|---|---|---|---|
| **Frente** | efémera | humano ou orquestrador | filesystem, git, hooks bloqueantes | runner de código local |
| **Arquitecto · triagem** | efémera, curta | evento (alerta) | leitura ampla, escrita escopada, invocação por máquina | runner invocável programaticamente |
| **Arquitecto · rumo** | efémera | só o humano | conversa; escrita só validada pelo humano (§2.4.3) | interface de chat |
| **Auditor** | efémera | calendário | leitura total, sem escrita | infraestrutura agendada |
| **Watcher** | persistente | cada merge | nenhum modelo; processo e disco | infraestrutura sempre ligada |
| **Detector semântico** | por chamada | o watcher | uma chamada sem estado | API directa, sem agente |
| **Script de indexação** | por corrida | cada merge | disco | o runner do watcher |
| **Hook de trajecto** | por operação | cada operação | acesso bloqueante ao runner que escreve | o runner que escreve |

**Regras — Protocolo P4**

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P4.1** | Um processo permanente **não pode** julgar. | humano (decisão de alocação) | bloqueia |
| **P4.2** | Um papel que escreve em zona **não pode** correr em runner sem hooks bloqueantes. | hook (S2) | bloqueia |
| **P4.3** | Os hooks **devem** residir no runner que executa a escrita. | humano (decisão de alocação) | bloqueia |
| **P4.4** | Uma mudança de runner **deve** ser precedida de decisão registada. | auditor | relatório |
| **P4.5** | Um hook indisponível **deve** produzir recusa da operação que dele dependia. | hook (verificação de presença no arranque) | bloqueia |

#### 2.4.11 Nota

Infraestrutura persistente serve para vigiar, disparar e agendar. Um agente permanente a julgar acumula contexto e deriva, e seria o pior sítio do sistema para isso acontecer.

Um orquestrador que valida trajectos mas delega a escrita a um processo sem hooks não protege nada. O que define a frente é a projecção, a zona e o gate de fecho, não onde corre; mudar de ferramenta é substituição de implementação. Um hook que não responde equivale a `HALT` para as operações que dependiam dele; ver T4.

---

### 2.5 Evolução

Um sistema que só impede movimento é uma jaula. Este distingue três formas de mudar.

A maior parte da mudança num projecto saudável é de ramo ou de caminho, não de rumo, e resolve-se em §2.2 e §2.3 sem tocar no mandato. Só chega aqui o que elas não conseguem absorver.

#### 2.5.1 Por necessidade

```
frente marca pressuposto_caido no INBOX
  → watcher ou triagem detecta
  → toca no mandato?
      não  → triagem resolve: estado, frente nova, ou rejeição
      sim  → escala; item fica novo (P3.15)
  → humano abre modo rumo (P5.1)
  → emenda datada (P5.3), ou nada
```

A frente nunca pára à espera desta cadeia (P3.12).

#### 2.5.2 Por vontade

O humano decide reavaliar sem que nada tenha falhado. Abre o modo rumo, o único modo que nenhum agente pode abrir (P5.1). Produz uma emenda ou nada; "nada" é resultado frequente e legítimo. O rumo não escreve no estado (P5.2): se escrevesse, cada alerta reabriria a discussão de rumo.

#### 2.5.3 Por falha do próprio sistema

Um mecanismo não funciona. Entra no `INBOX` como `falha_de_sistema`, é triado, e se alterar como o projecto se governa, é emenda. Só um incidente assim justifica regra nova (P5.4).

#### 2.5.4 Deriva e inflexão

| | Deriva | Inflexão |
|---|---|---|
| Alteração do objectivo | real | real |
| Declarada | não | sim |
| Datada | não | sim |
| Alternativa registada | não | sim |
| Tratamento | é o que o sistema existe para impedir | é saudável |

Abrir frentes novas não é patologia. O que mata o projecto é a frente que altera o mandato sem o dizer. O sistema não impede movimento: torna impossível alterar o mandato sem emendar o mandato.

#### 2.5.5 Registo de debates

Cada decisão produz um ficheiro em `debates/` com campos fechados (Anexo A): a decisão, a alternativa rejeitada, a razão, e os slugs que afecta. Não a discussão.

Serve duas funções: quando um mecanismo falhar daqui a meses, diz o que havia em alternativa e porque foi posto de lado; e alimenta o índice que protege o que foi decidido. É rastreabilidade, não história.

#### 2.5.6 Regras — Protocolo P5

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P5.1** | Só o humano **pode** abrir o modo rumo. | hook (perfil `rumo` exige humano) | bloqueia |
| **P5.2** | O modo rumo **não pode** escrever fora de `MANDATO` e `debates/`. | hook | bloqueia |
| **P5.3** | Toda a alteração ao `MANDATO` **deve** ser emenda datada com decisão em `debates/` que registe a alternativa rejeitada. | hook (esquema) | bloqueia |
| **P5.4** | Uma regra nova **não pode** ser acrescentada ao canon sem incidente registado no `INBOX` que a motive. | auditor | relatório |
| **P5.5** | Uma regra retirada **deve** manter o slug com grau `morto`. | hook | bloqueia |
| **P5.6** | Cada decisão **deve** produzir ficheiro em `debates/` com os campos do Anexo A. | hook (esquema) | bloqueia |

---

### 2.6 Regra de saída

Transversal a todos os níveis: handoff, entregue, alerta, relatório.

**A resposta primeiro.** A recomendação ou conclusão encabeça o documento. Abaixo, três ou quatro pilares de suporte, ME entre si. Na base, a evidência que sustenta cada pilar.

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P6.1** | Todo o output que sobe **deve** encabeçar com a conclusão, seguida de três ou quatro pilares ME e da evidência. | gate (cold-read) | fecha com marca |
| **P6.2** | O cold-read **deve** ser feito por agente sem histórico, com pergunta fechada sobre a acção seguinte, e devolver `passa` ou `falha`. | gate | fecha com marca |

*Nota.* A árvore é lógica de partição do problema; esta é lógica de comunicação do resultado. Confundi-las produz documentos que expõem a análise em vez de a concluir. Um output que não é decifrável de cima, sem contexto, não cumpre a regra, e o cold-read é a sua verificação mecânica.

---

## 3 · Garantias permanentes

### 3.1 Tabela

| Id | Garantia | Regras | Como se obtém | Como se mantém | Falha observável | Detector · cadência |
|---|---|---|---|---|---|---|
| **G1** | Existe um mandato | P0.1–P0.8 | P0, com os dois testes | tecto de uma página bloqueia emendas que inchem | frente aberta sem `desbloqueado` | hook · cada abertura de frente |
| **G2** | É interpretado igual | P0.2, P0.6, P0.7, P3.3 | não-objectivos e casos decididos | cada divergência vira caso em `CASOS` | sondas de fronteira divergem | auditor · mensal |
| **G3** | Chega a quem precisa | P3.2, P3.3 | injecção por escopo, não pesquisa | hook monta o contexto por perfil | sessão produz output sem pressuposto | gate · cada fecho |
| **G4** | O problema foi partido | P1.2, P1.3, P1.5, P1.8–P1.10 | árvores concorrentes, um eixo por nó | crivo mata as estéreis | árvore única, nó com dois eixos, ramos sobrepostos | auditor · mensal |
| **G5** | As árvores morrem | P1.1, P1.11 | condição de morte declarada ao nascer | auditor lista as que a excederam | árvore aberta além da condição | auditor · mensal |
| **G6** | O caminho é explícito | P2.1–P2.6 | método de procura, mínimo dois | reavaliação a cada pressuposto invalidado | frente sem pressuposto declarado | gate · cada fecho |
| **G7** | Ninguém sai da sua zona | P3.1, P3.14, P4.2 | worktree e hook de trajecto | hooks fora de todas as zonas | tentativa bloqueada no log; escrita fora da zona depois do merge | hook · cada escrita; auditor · mensal |
| **G8** | O decidido não é mexido | P3.6–P3.9, P5.5 | slugs, índice gerado, quatro graus | slugs nunca reutilizados | regra alterada sem decisão | hook · cada edição; auditor · mensal |
| **G9** | O estado não apodrece | P3.4 | substituição | auditor compara `ESTADO` e `FRENTES` | contradições entre estado e frentes | auditor · mensal |
| **G10** | O lixo não entra | P3.4, P3.10, P5.6 | campos fechados (Anexo A); triagem como árbitro | `0` itens é resultado legítimo e frequente | `INBOX` cresce mais do que se esvazia | watcher · cada merge (contagem); auditor · mensal |
| **G11** | Conflitos aparecem | P1.4, P2.7, P3.17 | três passagens do watcher | arestas declaradas ao desenhar o ramo | colisão descoberta por acaso: item de `INBOX` sem alerta prévio | auditor · mensal |
| **G12** | Decisões são aplicadas | P3.16 | verificação no fecho | auditor lista decisões sem item | decisão sem item correspondente | gate · cada fecho; auditor · mensal |
| **G13** | Becos não reabrem | P1.6, P5.5 | razão de poda registada | slug morto bloqueia recriação | frente repete trabalho já podado | hook · cada edição; auditor · mensal |
| **G14** | O rumo é rastreável | P5.1–P5.3, P5.6 | emenda datada com alternativa | registo de debates | alteração ao `MANDATO` sem entrada em `debates/` | hook · cada escrita no `MANDATO` |
| **G15** | Cada papel corre onde deve | P4.1–P4.5 | requisitos por papel | mudança de runner passa por decisão | papel que escreve a correr sem hooks bloqueantes | hook · cada arranque; auditor · mensal |
| **G16** | O governo não incha | P5.4, P7.1–P7.3 | toda a regra nova exige incidente | auditoria mensal | regras sem incidente que as justifique | auditor · mensal |
| **G17** | Os outputs são auto-suficientes | P6.1, P6.2 | regra de saída | cold-read em cada fecho | handoff que não devolve o próximo passo | gate · cada fecho |

### 3.2 Manutenção no tempo

| Quando | O quê |
|---|---|
| **A cada fecho de sessão** | automático: gate, selagem, merge, watcher, regeneração do índice |
| **A cada alerta** | sessão fria de triagem; não existe se `ALERTA` estiver vazio |
| **Mensalmente** | auditoria (P7.1) |

A auditoria é o único mecanismo que olha para o próprio sistema.

**Regras — Protocolo P7**

| Id | Regra | Detector | Consequência |
|---|---|---|---|
| **P7.1** | A auditoria **deve** correr uma vez por mês, nem mais nem menos. | humano | relatório |
| **P7.2** | O auditor **deve** verificar a listagem fixa: sondas de fronteira; contradições entre `ESTADO` e `FRENTES`; alertas descartados que reapareceram; árvores que excederam a condição de morte; ramos não-raiz sem dependência declarada; nós com mais de um eixo e ramos irmãos sobrepostos; árvores de modo diferente fundidas; árvore única em modo Problema ou Decisão; transversal alojado como ramo; regras alteradas sem decisão; regras sem incidente; decisões sem aplicação; conteúdo equivalente sob slugs distintos; mudanças de runner sem decisão; sessões seladas sem corrida do watcher; calibração do alerta (proporção de itens descartados). | humano | relatório |
| **P7.3** | O auditor **deve** verificar o próprio canon: obrigações em prosa sem identificador; regras sem detector ou sem consequência; garantias sem regra; referências cruzadas não resolvidas; termos sem entrada em §0. | humano | relatório |
| **P7.4** | O auditor **não pode** escrever fora do relatório. | hook | bloqueia |

*Nota.* Sem auditoria, o governo cresce e ninguém nota. A correr mais do que uma vez por mês, o governo consome o projecto.

### 3.3 A garantia que nenhum mecanismo dá

Confinamento impede uma frente de estragar outra. Não impede que faça a coisa errada com perfeição dentro da sua própria zona.

Por isso a projecção não é burocracia: é o único sítio onde fica escrito para que existe aquela frente. E deriva-se do caminho, pelo que não custa nada escrever.

Um sistema sem ela continua a funcionar, continua a bloquear escritas indevidas, continua a detectar colisões, e produz, com total ordem e rastreabilidade, trabalho que não serve para nada.

---

## 4 · Tensões em aberto

**T1 · Custo de declarar arestas.** Se declarar dependências não for barato no momento em que o ramo nasce, as arestas ficam vazias e o detector cala-se, pior do que não existir, porque parece estar a vigiar.
*Resolução adoptada:* obrigação no acto de desenhar o ramo (P1.4).
*Por verificar na prática.* Sinal gratuito: ramos não-raiz sem nenhuma aresta. O auditor lista (P7.2); a frequência responde sem ninguém ter de julgar.

**T2 · Completude das dependências.** A obrigação resolve o custo, não a completude. Declara-se o que se vê; o conflito caro é o que não se viu.
*Mitigação:* o detector semântico fica como rede de segurança e indica arestas em falta.

**T3 · Reintrodução por slug novo.** A protecção do decidido só apanha recriação pelo mesmo slug. Conteúdo equivalente com slug diferente escapa ao hook.
*Mitigação:* detecção no auditor (P7.2, conteúdo equivalente sob slugs distintos), não no momento da escrita.

**T4 · Dependência de runner.** Um papel alocado a um runner específico pára quando esse runner está indisponível.
*Resolução adoptada:* P4.5.
*Custo assumido:* indisponibilidade de infraestrutura pára trabalho em vez de o deixar correr sem protecção. É a troca correcta.

**T5 · Inchaço por multiplicação de árvores.** Quatro modos e árvores múltiplas por projecto é o ponto onde o sistema pode crescer sem limite.
*Travão único:* P1.1, condição de morte declarada ao nascer, verificada pelo auditor (P7.2).

---

## Anexo A · Esquemas dos ficheiros

Campos obrigatórios. O hook rejeita a escrita que não os tenha. Tipos de item do `INBOX`: `descoberta`, `pressuposto_caido`, `falha_de_sistema`.

| Ficheiro | Campos obrigatórios |
|---|---|
| `MANDATO` | `objectivos[]{slug, texto, nao_objectivos[]}` (1–5; 2–3 não-objectivos cada) · `criterio_fim` · `desbloqueado: data \| null` · `emendas[]{data, decisao_slug}` |
| `CAMINHO` | `pergunta` · `caminhos_abertos[]{slug, linha}` (≥2) · `caminho_actual: slug \| null` · `pressupostos[]{slug, estado, discriminante: bool, regra_paragem}` · `ordem_ataque[]` · `reavaliacoes[]{data, saida}` |
| `arvores/*` | `slug` · `modo: problema \| caracterizacao \| decisao \| mandato` · `condicao_morte` · `transversais[]{slug, texto}` · `nos[]{slug, eixo, estado, depende[], crivo: passou \| descartado \| null, razao: texto \| null}` |
| `INBOX/*.json` | `frente` · `tipo` · `ramo` · `pressuposto` · `toca[]` · `texto` · `data` |
| `estado.json` | `frente` · `pressuposto` · `regra_paragem` · `estado` · `toca[]` · `depende[]` · `proximo_passo` · `criterio_conclusao` · `cold_read: passa \| falha` · `carece_aprovacao: bool` |
| `handoff.json` | `frente` · `proximo_passo` · `criterio_conclusao` · `pressupostos_assumidos[]` · `referencias[]` |
| `debates/*.json` | `slug` · `data` · `decisao` · `alternativa_rejeitada` · `razao` · `afecta[]` · `selado: bool` |
| `indice-decisoes.json` | `{slug_afectado: [decisao_slug]}`, gerado por inversão de `debates/` |
| `ALERTA` | `itens[]{hash, passagem: colisao \| dependencia \| semantico, par[2], ramo, decisao_slug \| null}` |
| `ALERTA-ESTADO` | `{hash: novo \| visto \| descartado}`, acrescento |
| `ESTADO` | `data` · `frentes_abertas[]` · `factos[]{slug, texto}` |
| `FRENTES` | `frentes[]{slug, ramo, pressuposto, estado, toca[]}` |
| `REJEICOES` | `itens[]{data, origem, razao}` |
| `CASOS` | `casos[]{tarefa, classificacao, data}` |
