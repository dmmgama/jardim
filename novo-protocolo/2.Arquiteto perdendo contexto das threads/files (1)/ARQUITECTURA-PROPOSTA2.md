---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Arquitectura de governo para projectos multi-frente conduzidos por agentes, em estrutura
  paralela à versão de referência, com trinta e quatro alterações marcadas [M01] a [M34].
---

# Arquitectura de governo de projectos com agentes · versão paralela

**Convenção de leitura.** As secções seguem a estrutura da versão de referência, secção a secção, para permitir comparação directa. Toda a divergência está marcada com `[Mnn]` no ponto exacto em que ocorre. Secções sem marcador são idênticas em substância.

---

## 1 · Mandato deste documento

### 1.1 Porque existe

Um projecto conduzido por várias sessões de agentes perde o objectivo sem que ninguém decida perdê-lo. Não há momento de falha: há acumulação. Ao fim de algumas semanas o projecto é uma lista de tarefas que geram tarefas, e ninguém sabe dizer para que serve nenhuma delas.

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
| **`[M01]` O alerta existe, está correcto, e ninguém o abriu** | a detecção produz ficheiro, não notificação |
| **`[M02]` Investigação repetida sobre matéria já fechada** | a protecção do decidido actua na escrita, não na pesquisa |

### 1.3 O que este sistema não faz

- Não impede uma frente de fazer a coisa errada dentro da sua própria zona.
- Não substitui julgamento humano sobre o rumo.
- Não garante qualidade do trabalho. Garante alinhamento e rastreabilidade.
- `[M03]` **A exclusão de projectos de frente única é retirada.** O confinamento de escrita, a protecção do decidido, o registo de razões de fecho e a camada de caminho operam com uma frente de cada vez. Sem paralelismo perde-se apenas a passagem de colisão.

### 1.4 Critérios de sucesso

| Critério | Medição |
|---|---|
| Retoma a frio | uma sessão sem histórico retoma qualquer frente a partir do handoff |
| Alerta silencioso | o ficheiro de alertas vazio é o caso normal |
| Zero decisões órfãs | nenhuma sessão fecha com decisão registada e não aplicada |
| Caminho vivo | todo o pressuposto invalidado produziu reavaliação registada |
| Árvores mortais | nenhuma árvore aberta sem condição de morte declarada |
| Rumo rastreável | toda a alteração ao mandato tem data e alternativa rejeitada registada |
| Detecção rápida | conflito entre frentes sinalizado no fecho seguinte |
| Governo estável | o corpo de regras não cresce sem um modo de falha observado |
| **`[M04]` Zero sessões de verificação** | nenhuma sessão é convocada com a função única de verificar alinhamento |
| **`[M05]` Tectos numéricos respeitados** | árvores e frentes simultaneamente abertas nunca excedem os tectos inscritos no mandato |

`[M04]` é o critério de topo. Os restantes são condições dele.

Se ao fim de três meses o alerta dispara sempre, o detector está mal calibrado. Se nunca dispara e há colisões reais, as declarações estão mal preenchidas. Ambos são falhas do sistema, não do projecto.

---

## 2 · Arquitectura

### 2.1 Nascimento do projecto

Nada arranca antes desta fase estar fechada.

#### O que é preciso estabelecer

| Artefacto | Conteúdo | Quem escreve |
|---|---|---|
| `MANDATO` | objectivos, não-objectivos, critério de fim, **`[M06]` tectos, canal de alerta, cadência de auditoria** | agente, por reformulação; autoria do humano |
| `CASOS` | vazio no arranque | preenchido por divergência |
| Perfis e zonas | que perfis existem e onde cada um escreve | o humano responsável |
| `HALT` | ausente; o caminho existe | — |

Se o humano não conseguir enunciar o que quer, o mandato não se força: desenha-se uma árvore de mandato e o mandato sai dela.

#### Protocolo P0 — Nascimento

*Vocabulário: **deve** = obrigatório; **não pode** = proibido; **pode** = permitido.*

- **P0.1** — O mandato **deve** declarar entre um e cinco objectivos, cada um com slug.
- **P0.2** — O mandato **deve** declarar dois a três não-objectivos por objectivo.
- **P0.3** — O mandato **não pode** exceder uma página.
- **P0.4** — O mandato **deve** declarar o critério pelo qual o projecto se considera terminado.
- **P0.5** — `[M06]` O mandato **deve** declarar o tecto de árvores e o tecto de frentes simultaneamente abertas.
- **P0.6** — `[M06]` O mandato **deve** declarar o canal de alerta e a cadência de auditoria.
- **P0.7** — O mandato **deve** ser redigido por agente, por reformulação da intenção do humano responsável.
- **P0.8** — O agente **não pode** acrescentar objectivo ou não-objectivo que o humano não tenha enunciado.
- **P0.9** — `[M07]` O mandato **deve** passar o teste de reformulação.
- **P0.10** — `[M07]` O mandato **deve** passar o teste de discriminação de tarefa.
- **P0.11** — Nenhuma frente **pode** ser aberta antes de P0.9 e P0.10 devolverem verdadeiro.
- **P0.12** — Uma falha em P0.9 ou P0.10 **deve** produzir não-objectivo novo ou caso registado, e **não pode** produzir princípio novo.

#### Critério de desbloqueio da fase

Dois testes. O primeiro verifica compreensão; o segundo verifica precisão. Ambos têm de passar.

**Teste de reformulação.** Reformulação não é paráfrase. Compreendeu se consegue derivar não-objectivos que o humano não enunciou e acertar; classificar um caso-fronteira inventado na hora; dizer o que o mandato exclui; e nomear a tensão entre dois objectivos e dizer qual cede. O último é o mais difícil de fingir.

Falha em qualquer um: o mandato volta a ser discutido, não reescrito.

**Teste de discriminação de tarefa.** Três tarefas plausíveis, duas dentro e uma fora mas superficialmente parecida. Três sessões limpas, cada uma com o mandato e nada mais. Classificação idêntica e correcta desbloqueia a fase.

**Correcção em caso de falha:** acrescentar não-objectivos e registar em `CASOS` a tarefa que gerou a divergência. Nunca acrescentar princípios.

---

### 2.2 A árvore

A árvore é o instrumento de partição. Serve quatro propósitos distintos e produz os cortes que o caminho depois testa.

`[M17]` **A árvore tem duas existências.** A existência epistémica é a partição, desenhada e lida por humanos. A existência mecânica são os nós e as arestas num substrato próprio, consultado por travessia e nunca lido. Um agente não acede a nenhuma das duas: vê o seu ramo e as fronteiras negativas dos vizinhos.

#### Quatro propósitos

| Propósito | Pergunta que responde | Exaustividade | Forma |
|---|---|---|---|
| **Problema** | porque é que isto acontece | estrita, desde o início | fechada |
| **Caracterização** | o que é este objecto | aspiracional, verificada no fim | aberta |
| **Decisão** | o que é que eu quero | sobre o espaço de opções | profundidade desigual |
| **Mandato** | o que é que eu quero, afinal | emergente | morre ao produzir o mandato |

#### MECE, com uma distinção

**Mutuamente exclusivo aplica-se sempre.** Sobreposição entre ramos produz dupla contagem e duplica esforço.

**Colectivamente exaustivo varia com o propósito.** Estrito numa árvore de problema; aspiracional numa de caracterização, verificado ao fechar.

**Um eixo por nó.** Iterar níveis é permitido e é como se compõem eixos. Misturar eixos no mesmo nível é a violação mais frequente.

**Profundidade desigual não é defeito** numa árvore de decisão. O defeito é o ramo raso desaparecer sem ficar registado que se decidiu não o aprofundar.

#### Critério de corte

**Assimetria.** O corte vale se criar maior diferença entre ramos e isolar o problema numa área.

**Accionabilidade.** O corte tem de recair sobre variável controlável ou influenciável.

#### Triagem antes de dados

Estimativa de ordem de grandeza e cenário extremo antes de recolher evidência. Um ramo cuja variação por um factor de dez não alteraria a decisão final descarta-se sem teste empírico. A triagem é gratuita e é o que impede a árvore de gerar frentes a mais.

#### Árvores múltiplas e árvores acopladas

Árvores concorrentes com eixos conceptuais distintos sobre o mesmo problema. Uma árvore só é inércia, não escolha.

Árvores de propósito diferente não se fundem. Acoplam-se por dependência declarada.

`[M10]` **Tecto numérico.** O número de árvores simultaneamente abertas não pode exceder o tecto inscrito no mandato. Uma árvore cuja condição de morte se verificou não recebe ramos novos.

#### Estado de ramo

`por abrir` · `em desenvolvimento` · `fechado` · `podado` · `suspenso: <dependência>`

**Podado não é rejeitado.** É "decidiu-se não aprofundar", com razão registada.

`[M11]` **Fechado regista igualmente.** O fecho de um ramo regista resultado e razão, pela mesma razão pela qual a poda regista: o que impede a reabertura é o registo, e um ramo fechado reabre tão facilmente como um podado.

`[M24]` **A projecção legível omite as razões.** A vista da árvore destinada a leitura humana contém nós, estados e arestas, e não contém as razões de fecho nem de poda. Estas residem no substrato e são devolvidas apenas por mecanismo de bloqueio.

#### Protocolo P1 — Árvore

- **P1.1** — Cada árvore **deve** declarar, ao nascer, o seu propósito e a condição em que morre.
- **P1.2** — Num nó **não pode** ser aplicado mais de um eixo de corte.
- **P1.3** — Ramos irmãos **não podem** sobrepor-se.
- **P1.4** — Um ramo **deve** declarar as suas dependências no momento em que é desenhado.
- **P1.5** — Um ramo **não pode** passar a trabalho sem ter passado a triagem de ordem de grandeza.
- **P1.6** — Um ramo podado **deve** registar a razão.
- **P1.7** — `[M11]` Um ramo fechado **deve** registar o resultado e a razão.
- **P1.8** — Árvores de propósito diferente **não podem** ser fundidas.
- **P1.9** — `[M10]` O número de árvores simultaneamente abertas **não pode** exceder o tecto declarado.
- **P1.10** — `[M10]` Uma árvore cuja condição de morte se verificou **não pode** receber ramos novos.
- **P1.11** — `[M08]` Numa árvore de propósito problema, os ramos irmãos **devem** cobrir integralmente o nó de origem no momento em que são desenhados.
- **P1.12** — `[M08]` Numa árvore de propósito caracterização, a cobertura integral **deve** ser verificada no fecho da árvore.
- **P1.13** — `[M09]` Um ramo só **pode** passar a frente se o seu eixo de corte recair sobre variável controlável ou influenciável.

---

### 2.3 O caminho

Entre o mandato e as frentes há uma camada que decide **por onde**. Caminho é a hipótese, hoje, sobre como se chega ao mandato: uma aposta entre apostas possíveis, com pressupostos declarados e testáveis.

A árvore gera os cortes; o caminho testa-os. A triagem mata ramos antes de haver dados, de graça; o caminho testa com dados reais o que sobreviveu, e é caro.

#### Método de procura

```
M1  Enunciar o mandato como pergunta de decisão
M2  Desenhar as árvores concorrentes e triar as estéreis
M3  Por árvore sobrevivente, extrair o que tem de ser verdade — os pressupostos
M4  Marcar os discriminantes: pressupostos cuja resposta elimina caminhos
M5  Ordenar por (incerteza × custo de descobrir tarde) ÷ custo de testar
M6  A primeira frente testa o discriminante do topo
M7  Nenhum caminho é declarado escolhido antes de M6 devolver resultado
```

As frentes derivam do caminho, não do mandato.

#### `CAMINHO`

| Campo | Conteúdo |
|---|---|
| Pergunta de decisão | o mandato reformulado como pergunta |
| Caminhos em aberto | dois ou mais, com uma linha cada |
| Caminho actual | um, ou `não escolhido` |
| Pressupostos | estado: `por testar`, `confirmado`, `invalidado`, `inconclusivo` |
| Ordem de ataque | os pressupostos por ordem de M5 |
| Regras de paragem | por pressuposto, escritas antes de a frente abrir |

Uma página. Muda mais que o mandato, menos que o estado.

#### Protocolo P2 — Caminho

- **P2.1** — O caminho **deve** declarar dois ou mais caminhos plausíveis.
- **P2.2** — Cada frente **deve** declarar que pressuposto testa ou que caminho executa.
- **P2.3** — Cada pressuposto **deve** ter regra de paragem escrita antes de a frente abrir.
- **P2.4** — Um caminho **não pode** ser declarado escolhido com discriminante por testar.
- **P2.5** — Um pressuposto invalidado **deve** disparar reavaliação antes de abrir frente nova.
- **P2.6** — O caminho **não pode** exceder uma página.
- **P2.7** — `[M12]` O caminho **deve** passar o teste de discriminação de frente.
- **P2.8** — `[M13]` O número de frentes simultaneamente abertas **não pode** exceder o tecto declarado.
- **P2.9** — `[M14]` Um pressuposto inconclusivo **deve** produzir redesenho da regra de paragem e **não pode** produzir repetição do mesmo teste.

#### `[M12]` Critério de desbloqueio do caminho

Simétrico ao de P0. Três frentes plausíveis: duas que testam pressupostos declarados no caminho, uma que não testa nenhum mas é formulada em termos semelhantes. Três sessões limpas, cada uma com o caminho e nada mais. Classificação idêntica e correcta valida o caminho.

Falha: o pressuposto ou a regra de paragem é reformulada. Não se acrescenta princípio.

#### Como se avalia

Um milestone não é um entregável: é um teste de pressuposto. A pergunta não é o que fica pronto, mas o que fica a saber-se.

| Resultado | Significado | Consequência |
|---|---|---|
| `confirmado` | o pressuposto aguenta | avança para o seguinte na ordem |
| `invalidado` | o pressuposto cai | reavaliação obrigatória |
| `inconclusivo` | o teste não decidiu | redesenhar o teste, não repetir |

#### Como se reavalia

Três disparos: pressuposto invalidado, cadência fixa, ou vontade do humano.

```
reavaliação → quatro saídas, mutuamente exclusivas

  manter             nada mudou que altere a ordem
  reordenar          mudou a ordem de ataque, não o caminho
  trocar de caminho  o caminho actual cai; outro dos abertos assume
  escalar            o mandato é que está errado → modo rumo
```

Mudar de caminho não é mudar de rumo. Só a quarta saída toca no mandato.

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

**Um nível nunca escreve no nível acima.** O que sobe é um pedido, não uma alteração.

#### 2.4.2 Escopo de contexto

Corolário directo da hierarquia: cada nível classifica o seu trabalho contra o nível imediatamente acima, nunca contra o topo.

| Quem | Classifica contra | Não precisa de |
|---|---|---|
| Sessão | o mandato da frente | o caminho, o mandato |
| Frente | o pressuposto que testa e a regra de paragem | o mandato |
| Triagem | os ramos que o alerta toca | o projecto inteiro |
| Caminho | o mandato | a intenção por trás |
| Rumo | a intenção do humano | — |

Uma frente sem o mandato geral continua a detectar que derrapou, porque derrapar é sair do seu pressuposto.

Consequência: a projecção de uma frente não se redige, deriva-se do caminho.

**Uma excepção.** Os objectivos são escopáveis; os não-objectivos não. Vão inteiros em qualquer sessão que classifique.

#### 2.4.3 Actores

| Actor | É agente | Dispara por | Escreve em |
|---|---|---|---|
| **Humano responsável** | não | vontade | tudo |
| **Arquitecto · triagem** | sim | **`[M15]` invocação do watcher** | `ESTADO`, `FRENTES`, `REJEICOES` |
| **Arquitecto · rumo** | sim | só o humano | emenda ao mandato, ou nada |
| **Frente** | sim | trabalho | a sua worktree, `INBOX` |
| **Auditor** | sim | cadência | relatório |
| **Watcher** | **não** | cada merge | `ALERTA`, **`[M15]` canal, invocação da triagem** |

O watcher não tem modelo. É um script. `[M15]` Emite para o canal declarado e invoca a triagem; não a espera.

#### 2.4.4 Ferramentas

`[M16]` Coluna de origem acrescentada. Separa o que se monta do que se escreve.

| Ferramenta | Função | Substitui | `[M16]` Origem |
|---|---|---|---|
| **Árvore** | partição do espaço, geração de cortes | ataque por um ângulo só | escrita própria |
| **`[M17]` Substrato de arestas** | armazenamento das arestas fora das zonas; travessia transitiva | arestas implícitas na leitura da árvore | base relacional de ficheiro único |
| **Worktree** | isolamento, paralelismo, merge como verificação | disciplina de não mexer na pasta alheia | controlo de versões |
| **Hook de caminho** | confinamento de leitura e escrita por perfil | regras escritas em prosa | ganchos do runner |
| **Índice de decisões** | liga slugs a decisões | memória de quem estava presente | registo de decisões e inversão |
| **Watcher** | cruzar declarações e seguir dependências | reuniões de coordenação | ganchos de integração |
| **Cold-read** | verificar auto-suficiência de um output | confiança | chamada de modelo sem sessão |
| **Proveniência selada** | registo imutável, fora do índice de pesquisa | memória | anotações do controlo de versões |
| **HALT** | paragem imediata de todas as escritas | — | verificação de presença no hook |
| **`[M15]` Canal de alerta** | entrega da detecção sem consulta | ficheiro que alguém abre | serviço de notificação |

#### 2.4.5 Ficheiros

| Ficheiro | O que é | Escrita | Quem |
|---|---|---|---|
| `MANDATO` | a lei do projecto | emenda datada | agente redige, humano valida |
| `CAMINHO` | a hipótese de como se lá chega | substituição | humano com agente |
| `arvores/*` | partições do espaço, por propósito | substituição | humano com agente |
| `CASOS` | casos-fronteira decididos | acrescento | humano, triagem |
| `ESTADO` | o que é verdade agora | substituição | triagem |
| `FRENTES` | índice de frentes e ramos | substituição | triagem |
| `REJEICOES` | o que foi descartado e porquê | acrescento | triagem |
| `ALERTA` | o que o watcher detectou | substituição | watcher |
| **`[M18]` `arestas.db`** | **nós, arestas, níveis; fora de todas as zonas** | **escrita por hook** | **máquina** |
| `INBOX/*.json` | descobertas por processar | acrescento | frentes |
| `debates/*.json` | decisões, com alternativa rejeitada e o que afectam | acrescento | rumo |
| `indice-decisoes.json` | slug → decisão | gerado | script |
| **`[M24]` `mapa.mmd`** | **projecção legível, sem razões de fecho** | **gerado** | **script** |
| `estado.json` | estado da frente face ao seu pressuposto | substituição | frente |
| `handoff.json` | como retomar | substituição | frente |
| `research/` | exploração | livre | frente |
| `entregue/` | o que sobe | acrescento | frente |
| `Rascunhos` | travão intra-sessão | termina vazio | frente |
| `sealed/` | pedido, output, referências | write-once | hook |
| `HALT` | interruptor | presença | humano |

- **Estado substitui-se, evidência acumula-se.** Nunca no mesmo ficheiro.
- **O caos tem lugar próprio.** `research/` e `Rascunhos` não se disciplinam.
- **Nada que uma ferramenta possa reconstruir entra em memória.**
- `[M18]` **As arestas não vivem em ficheiro de projecto.** Um ficheiro na worktree é legível pelo agente que a ocupa; o substrato fica fora de todas as zonas.

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

A coluna da direita vive na proveniência selada, recuperável e não lida.

#### 2.4.7 Fluxos, do geral ao átomo

**L0–L2 · Projecto**

```
MANDATO → ÁRVORES → CAMINHO → frentes → merges → watcher → ALERTA

ALERTA vazio            → nada acontece
ALERTA com item         → [M20] emite para o canal e invoca a triagem
triagem toca no mandato → escala ao humano → rumo → emenda → MANDATO
```

**L3 · Frente**

```
F1  Abre com projecção derivada do caminho
F2  Sessões de trabalho, N ≥ 1
F3  Fecho de cada sessão: gate
F4  Pressuposto resolvido → frente fecha → resultado ao caminho
F5  [M22] Fecho de ramo → travessia transitiva das arestas → cone afectado → alerta
```

**L4 · Sessão — o átomo**

```
S1  HALT presente?                    sim → recusa
S2  Perfil declarado?                 não → recusa
S3  Monta contexto por perfil e por escopo
S4  Trabalha
      escrita fora da zona            → bloqueia, devolve zona, continua
      edição de slug com decisão      → bloqueia ou alerta, conforme o nível
      [M21] pesquisa lançada          → confronta com ramos fechados e podados
      dúvida                          → declara pressuposto, continua
      tema fora do mandato da frente  → Rascunhos, volta ao tema
S5  Fecho
      toca fora do declarado          → não fecha
      sem pressuposto nem caminho     → não fecha
      Rascunhos não vazio             → não fecha
      pressuposto novo                → fecha com carece_aprovacao
      cold-read falha                 → fecha com carece_aprovacao
      trabalho continua               → handoff.json, validado
S6  Sela, faz merge, dispara watcher
```

Não existe estado de espera.

#### 2.4.8 Mecanismos

**Gate de fecho.** Dois níveis. Divergência dura bloqueia o fecho; divergência branda deixa fechar com marca e sobe ao alerta.

**Detecção, três passagens.**

| Passagem | Base | Confiança | Apanha |
|---|---|---|---|
| Colisão | campo `toca` | facto | duas frentes na mesma coisa |
| **Dependência** | **`[M22]` travessia transitiva das arestas** | facto | **o cone inteiro a jusante, não só o vizinho** |
| Semântico | chamada única de modelo | sugestão | o que ninguém declarou |

`[M22]` **A passagem de dependência calcula o cone afectado.** Quando um ramo fecha, é podado, ou uma decisão se altera, a travessia percorre as arestas transitivamente e produz um item de alerta por ramo alcançado. A versão que segue apenas as arestas directas deixa escapar a propagação de segunda ordem, que é onde vive a invalidação cara.

`[M23]` **A passagem semântica ganha o confronto de pesquisa.** Uma pesquisa lançada é comparada contra os ramos fechados e podados antes de ser executada. A correspondência produz sugestão, nunca bloqueio.

O detector semântico é a rede de segurança. Quando apanha um conflito que a árvore não previa, falta uma aresta.

**Alerta com estado.** Cada alerta é `novo`, `visto` ou `descartado`, com hash do conteúdo. Um descartado não reaparece para o mesmo par no mesmo estado.

`[M19]` **O alerta é empurrado.** A escrita no ficheiro persiste como registo. A entrega faz-se para o canal declarado no mandato, e a triagem é invocada pelo watcher. Um alerta vazio não produz sessão.

**Protecção do que foi decidido.** Tudo tem slug. Os slugs são globais, nunca se reutilizam e nunca se renumeram. A decisão declara o que afecta; o índice é gerado por inversão.

| Nível | Origem | Comportamento |
|---|---|---|
| `livre` | sem decisão | edita |
| `decidido` | decisão registada | alerta, pede confirmação humana |
| `selado` | decisão com `selado` | bloqueia; só nova decisão desbloqueia |
| `morto` | slug retirado por decisão | bloqueia a recriação |

O alerta devolve o identificador da decisão e o facto de existir. Nunca o conteúdo do debate, a alternativa rejeitada ou a razão.

`[M24]` **A omissão estende-se à projecção legível.** A vista do mapa não mostra por que razão um caminho foi anulado. Quem olha vê que está fechado e não recebe o material com que o reabriria.

**Cold-read.** Um agente sem histórico lê o output ou o handoff e responde a uma pergunta fechada sobre a acção seguinte.

**Paragem.** A presença de `HALT` faz o hook recusar arranque e qualquer escrita. Removido à mão.

#### 2.4.9 Regra de saída

**A resposta primeiro.** A conclusão encabeça o documento; abaixo, três ou quatro pilares MECE; na base, a evidência.

A árvore é lógica de partição do problema; esta é lógica de comunicação do resultado.

`[M25]` **Convertida em regra.** O cold-read verifica-a mecanicamente, e uma regra verificável por mecanismo tem identificador e consequência de incumprimento, como as restantes.

#### 2.4.10 Escolha de agente por papel

Os papéis são funções, não produtos.

**Seis critérios**

| Critério | Pergunta |
|---|---|
| Duração | o papel vive enquanto trabalha, ou tem de estar sempre ligado? |
| Disparo | quem o invoca: humano, evento, ou calendário? |
| Filesystem | precisa de worktree, git e ficheiros locais? |
| Enforcement | precisa de hooks que **bloqueiem** uma operação antes de executar? |
| Escopo | o contexto tem de ser montado por perfil e cortado? |
| Julgamento | o papel decide, ou só detecta? |

O critério de enforcement é eliminatório.

**Requisitos por papel**

| Papel | Duração | Disparo | Precisa de | Natural em |
|---|---|---|---|---|
| **Frente** | efémera | humano ou orquestrador | filesystem, git, hooks bloqueantes | runner de código local |
| **Arquitecto · triagem** | efémera, curta | evento | leitura ampla, escrita escopada, invocação por máquina | runner invocável programaticamente |
| **Arquitecto · rumo** | efémera | só o humano | conversa, sem escrita automática | interface de chat |
| **Auditor** | efémera | calendário | leitura total, sem escrita | infraestrutura agendada |
| **Watcher** | persistente | cada merge | nenhum modelo; processo e disco | infraestrutura sempre ligada |
| **Detector semântico** | por chamada | dentro do watcher | uma chamada sem estado | API directa, sem agente |

**`[M26]` Quatro regras de alocação, com identificador**

- **P9.4** — Um processo permanente **não pode** julgar.
- **P9.1** — Um papel que escreve em zona protegida **não pode** correr em runner sem hooks bloqueantes, e os hooks **devem** residir no runner que executa a escrita.
- **P9.6** — Uma mudança de runner **deve** ser precedida de decisão registada.
- **P9.3** — Um hook indisponível **deve** produzir recusa.

---

### 2.5 Evolução

Um sistema que só impede movimento é uma jaula. Este distingue três formas de mudar. A maior parte da mudança é de ramo ou de caminho, e resolve-se sem tocar no mandato.

#### Por necessidade

```
frente marca challenges no INBOX
  → watcher ou triagem detecta
  → toca no mandato?
      não  → triagem resolve: estado, frente nova, ou rejeição
      sim  → escala. A triagem não resolve. Alerta fica novo.
  → humano abre modo rumo
  → emenda datada, ou nada
```

A frente nunca pára à espera desta cadeia.

#### Por vontade

O humano decide reavaliar sem que nada tenha falhado. Produz emenda ou nada. Nunca escreve no estado.

#### Por falha do próprio sistema

Um mecanismo não funciona. Entra no inbox, é triado, e se alterar como o projecto se governa, é emenda.

`[M27]` **Condição de adopção.** Uma regra nova não pode ser adoptada sem incidente registado que a motive. A condição é regra, com identificador, e o auditor lista as regras que não a cumprem.

#### Deriva e inflexão

| | Deriva | Inflexão |
|---|---|---|
| Alteração do objectivo | real | real |
| Declarada | não | sim |
| Datada | não | sim |
| Alternativa registada | não | sim |
| Tratamento | é o que o sistema existe para impedir | é saudável |

#### Registo de debates

Cada decisão produz ficheiro com campos fechados: a decisão, a alternativa rejeitada, a razão, os slugs que afecta. Não a discussão.

`[M28]` **Campos fechados exigem validador.** A noção de campo fechado só é verificável se houver esquema validado no momento da escrita. Sem ele, é convenção.

---

## 3 · Garantias permanentes

### 3.1 Tabela

`[M29]` Coluna de via acrescentada.

| Garantia | Como se obtém | Como se detecta a falha | `[M29]` Via |
|---|---|---|---|
| **Existe um mandato** | P0, com os dois testes | nenhuma frente declara pressuposto válido | escrita própria |
| **É interpretado igual** | não-objectivos e casos decididos | sondas de fronteira divergem | escrita própria |
| **Chega a quem precisa** | injecção por escopo, não pesquisa | sessão produz output sem pressuposto | hook |
| **O problema foi partido** | árvores concorrentes, um eixo por nó | árvore única, ou ramos sobrepostos | método |
| **As árvores morrem** | condição de morte declarada ao nascer | árvore aberta além da condição | auditor |
| **O caminho é explícito** | método de procura, mínimo dois | frente sem pressuposto declarado | escrita própria |
| **`[M12]` O caminho discrimina** | teste de discriminação de frente | três sessões classificam diferente | escrita própria |
| **Ninguém sai da sua zona** | worktree e hook de caminho | tentativa bloqueada no log | worktree e ganchos |
| **O decidido não é mexido** | slugs, índice gerado, quatro níveis | regra alterada sem decisão | registo de decisões |
| **O estado não apodrece** | substituição com orçamento | contradições entre estado e frentes | esquema e auditor |
| **O lixo não entra** | quota, campos fechados, árbitro em código | inbox cresce mais do que se esvazia | validador de esquema |
| **Conflitos aparecem** | três passagens do watcher | colisão descoberta por acaso | substrato de arestas |
| **`[M22]` A propagação é completa** | travessia transitiva | invalidação descoberta dois ramos adiante | consulta recursiva |
| **Decisões são aplicadas** | verificação no fecho | decisão sem item correspondente | gate |
| **Becos não reabrem** | razão de fecho e de poda registadas | frente repete trabalho já fechado | índice de decisões |
| **`[M30]` A pesquisa não repete** | confronto contra ramos fechados | investigação duplicada meses depois | pesquisa vectorial |
| **`[M31]` O alerta chega** | emissão para canal declarado | alerta correcto e não lido | serviço de notificação |
| **O rumo é rastreável** | emenda datada com alternativa | alteração sem entrada | registo de debates |
| **Cada papel corre onde deve** | requisitos por papel | papel que escreve sem hooks bloqueantes | decisão registada |
| **O governo não incha** | toda a regra nova exige falha observada | regras sem incidente | auditor |
| **`[M05]` O sistema não consome sessões** | vigilância executada, nunca convocada | existe sessão cuja função é verificar alinhamento | watcher e canal |

### 3.2 Manutenção no tempo

| Quando | O quê |
|---|---|
| **A cada fecho de sessão** | automático: gate, selagem, merge, watcher, regeneração do índice, **`[M22]` cálculo do cone**, **`[M24]` regeneração do mapa** |
| **A cada alerta** | sessão fria de triagem, **`[M15]` invocada pelo watcher**; não existe se o alerta estiver vazio |
| **Por cadência fixa** | auditoria |

A auditoria é o único mecanismo que olha para o próprio sistema. A correr mais do que uma vez por mês, o governo consome o projecto.

`[M32]` **Listagem fixa do auditor.** Ramos não-raiz sem aresta declarada; árvores que excederam a condição de morte; alertas descartados que reapareceram; regras sem incidente; contradições entre estado e frentes; decisões sem aplicação; conteúdos equivalentes sob slugs distintos.

### 3.3 A garantia que nenhum mecanismo dá

Confinamento impede uma frente de estragar outra. Não impede que faça a coisa errada com perfeição dentro da sua própria zona.

`[M12]` **A garantia deixa de ser nula e passa a parcial.** O teste de discriminação de frente verifica que o pressuposto e a regra de paragem são lidos de forma idêntica por sessões independentes. Não verifica que o pressuposto seja o pressuposto certo — isso permanece julgamento humano — mas elimina a categoria de falha em que a frente é bem executada contra um objectivo que ninguém lê da mesma maneira.

O que resta sem mecanismo: a qualidade do caminho enquanto escolha. Um caminho bem formado, bem testado e bem executado pode ser o caminho errado.

---

## 4 · Tensões em aberto

**T1 · Custo de declarar arestas.** Se declarar dependências não for barato no momento em que o ramo nasce, as arestas ficam vazias e o detector cala-se — pior do que não existir. `[M33]` **Mitigação parcial:** um planeador que gere briefs autónomos produz o mapa de dependências inicial, o que desloca o custo do momento do desenho para o momento da revisão.

**T2 · Completude das dependências.** Declara-se o que se vê; o conflito caro é o que não se viu. Sem mitigação.

**T3 · Reintrodução por slug novo.** `[M33]` **Mitigação parcial:** a passagem de equivalência por distância vectorial apanha conteúdo equivalente sob slug distinto. A ferramenta está em fase anterior à versão 1, o que torna a mitigação datada.

**T4 · Dependência de runner.** Um papel alocado a um runner específico pára quando esse runner está indisponível. Sem mitigação; a recusa é a escolha deliberada.

**T5 · Inchaço por multiplicação de árvores.** `[M33]` **Mitigação:** tecto numérico declarado no mandato e verificado pelo auditor. A condição de morte auto-declarada deixa de ser o único travão.

**`[M34]` T6 · O substrato de arestas é ponto único de verdade fora do controlo de versões.** As arestas residem num ficheiro binário que não tem histórico, não tem diff e não tem merge. Uma corrupção é silenciosa e um conflito de escrita concorrente é resolvido por última escrita. A alternativa — arestas em ficheiros de texto versionados — recupera o histórico e perde a invisibilidade ao agente. Nenhuma das duas resolve as duas coisas.

---

## 5 · `[M35]` Índice de alterações

| Marca | Secção | Alteração |
|---|---|---|
| M01 | 1.2 | sintoma: alerta correcto e não lido |
| M02 | 1.2 | sintoma: investigação repetida |
| M03 | 1.3 | retirada a exclusão de projectos de frente única |
| M04 | 1.4 | critério: zero sessões de verificação |
| M05 | 1.4, 3.1 | critério e garantia: tectos numéricos |
| M06 | 2.1, P0.5, P0.6 | mandato declara tectos, canal e cadência |
| M07 | P0.9, P0.10 | os dois testes separados em regras próprias |
| M08 | P1.11, P1.12 | exaustividade por propósito como regra |
| M09 | P1.13 | accionabilidade do corte como regra |
| M10 | 2.2, P1.9, P1.10 | tecto de árvores e árvore morta |
| M11 | 2.2, P1.7 | ramo fechado regista resultado e razão |
| M12 | 2.3, P2.7, 3.1, 3.3 | teste de discriminação de frente |
| M13 | P2.8 | tecto de frentes |
| M14 | P2.9 | inconclusivo redesenha, não repete |
| M15 | 2.4.3, 2.4.4, 3.2 | watcher emite e invoca a triagem |
| M16 | 2.4.4 | coluna de origem nas ferramentas |
| M17 | 2.2, 2.4.4 | substrato de arestas como ferramenta |
| M18 | 2.4.5 | `arestas.db` fora de todas as zonas |
| M19 | 2.4.8 | alerta empurrado |
| M20 | 2.4.7 | fluxo com emissão e invocação |
| M21 | 2.4.7 | confronto de pesquisa em S4 |
| M22 | 2.4.7, 2.4.8, 3.1, 3.2 | cone afectado por travessia transitiva |
| M23 | 2.4.8 | passagem semântica confronta pesquisa |
| M24 | 2.2, 2.4.5, 2.4.8 | projecção legível sem razões de fecho |
| M25 | 2.4.9 | regra de saída com identificador |
| M26 | 2.4.10 | regras de alocação com identificador |
| M27 | 2.5 | condição de adopção de regra nova |
| M28 | 2.5 | campos fechados exigem validador |
| M29 | 3.1 | coluna de via nas garantias |
| M30 | 3.1 | garantia: a pesquisa não repete |
| M31 | 3.1 | garantia: o alerta chega |
| M32 | 3.2 | listagem fixa do auditor |
| M33 | 4 | mitigações de T1, T3 e T5 |
| M34 | 4 | tensão nova T6 |
| M35 | 5 | este índice |
