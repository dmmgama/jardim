---
created: 2026-09-19 20:05
chat: Arquitectura de governo de projectos com agentes
summary: >
  Arquitectura de governo para projectos multi-frente conduzidos por agentes: mandato,
  árvore, caminho, desenvolvimento por níveis, evolução, garantias e tensões em aberto.
---

# Arquitectura de governo de projectos com agentes

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
- Não se aplica a projectos de frente única — sem paralelismo, a maior parte dos mecanismos não tem o que detectar.
- Não garante qualidade do trabalho. Garante alinhamento e rastreabilidade.

### 1.4 Critérios de sucesso

| Critério | Medição |
|---|---|
| Retoma a frio | uma sessão sem histórico retoma qualquer frente a partir do handoff |
| Alerta silencioso | o ficheiro de alertas vazio é o caso normal, não a excepção |
| Zero decisões órfãs | nenhuma sessão fecha com decisão registada e não aplicada |
| Frentes sob tecto | frentes abertas nunca excedem o tecto declarado |
| Caminho vivo | todo o pressuposto invalidado produziu reavaliação registada |
| Árvores mortais | nenhuma árvore aberta sem condição de morte declarada |
| Rumo rastreável | toda a alteração ao mandato tem data e alternativa rejeitada registada |
| Detecção rápida | conflito entre frentes sinalizado no fecho seguinte |
| Governo estável | o corpo de regras não cresce sem um modo de falha observado |

Se ao fim de três meses o alerta dispara sempre, o detector está mal calibrado. Se nunca dispara e há colisões reais, as declarações estão mal preenchidas. Ambos são falhas do sistema, não do projecto.

---

## 2 · Arquitectura

### 2.1 Nascimento do projecto

Nada arranca antes desta fase estar fechada. Um projecto sem mandato produz trabalho, mas não produz alinhamento — e o custo só aparece semanas depois.

#### O que é preciso estabelecer

| Artefacto | Conteúdo | Quem escreve |
|---|---|---|
| `MANDATO` | objectivos, não-objectivos, critério de fim | agente, por reformulação; autoria do humano |
| `CASOS` | vazio no arranque | preenchido por divergência |
| Perfis e zonas | que perfis existem e onde cada um escreve | o humano responsável |
| `HALT` | ausente; o caminho existe | — |

Se o humano não conseguir enunciar o que quer, o mandato não se força: desenha-se uma árvore de mandato (§2.2) e o mandato sai dela.

#### Protocolo P0 — Nascimento

*Vocabulário: **deve** = obrigatório; **não pode** = proibido; **pode** = permitido.*

- **P0.1** — O mandato **deve** declarar entre um e cinco objectivos, cada um com slug.
- **P0.2** — O mandato **deve** declarar duas a três não-objectivos por objectivo.
- **P0.3** — O mandato **não pode** exceder uma página.
- **P0.4** — O mandato **deve** declarar o critério pelo qual o projecto se considera terminado.
- **P0.5** — O mandato **deve** ser redigido por agente, por reformulação da intenção do humano responsável.
- **P0.6** — O agente **não pode** acrescentar objectivo ou não-objectivo que o humano não tenha enunciado.
- **P0.7** — O mandato **deve** passar o teste de reformulação e o teste de discriminação.
- **P0.8** — Nenhuma frente **pode** ser aberta antes de P0.7 devolver verdadeiro.

#### Critério de desbloqueio da fase

Dois testes. O primeiro verifica compreensão; o segundo verifica precisão. Ambos têm de passar.

**Teste de reformulação.** O agente enuncia o mandato por palavras próprias e o humano confirma ou rejeita. Reformulação não é paráfrase: um agente que devolve as mesmas palavras por outra ordem não demonstrou nada. Compreendeu se consegue:

- derivar não-objectivos que o humano não enunciou, e acertar;
- classificar um caso-fronteira inventado na hora;
- dizer o que o mandato **exclui**, não apenas o que persegue;
- nomear a tensão entre dois objectivos e dizer qual cede.

O último é o mais difícil de fingir: qual objectivo cede numa colisão não está no texto, está na intenção.

Falha em qualquer um → o mandato volta a ser discutido, não reescrito. O que falhou foi a transmissão da intenção, não a redacção.

**Teste de discriminação.** Três tarefas plausíveis: duas dentro do mandato, uma fora mas superficialmente parecida. Três sessões limpas, cada uma com o mandato e nada mais. As três classificam igual e correctamente → fase desbloqueada. Qualquer divergência → o mandato falha.

**Correcção em caso de falha:** acrescentar não-objectivos e registar em `CASOS` a tarefa que gerou a divergência, com a classificação correcta. Nunca acrescentar princípios — um princípio novo aumenta o espaço interpretativo em vez de o reduzir.

---

### 2.2 A árvore

A árvore é o instrumento de partição. Não é um nível da hierarquia nem uma fase: é uma ferramenta que se usa sempre que há um espaço a dividir, e serve quatro propósitos distintos. É ela que produz os cortes que o caminho depois testa.

#### Quatro propósitos

| Propósito | Pergunta que responde | Exaustividade | Forma |
|---|---|---|---|
| **Problema** | porque é que isto acontece | estrita, desde o início | fechada |
| **Caracterização** | o que é este objecto | aspiracional, verificada no fim | **aberta** — ramos nascem da investigação |
| **Decisão** | o que é que eu quero | sobre o espaço de opções | profundidade deliberadamente desigual |
| **Mandato** | o que é que eu quero, afinal | emergente | morre ao produzir o mandato |

#### MECE, com uma distinção

**Mutuamente exclusivo aplica-se sempre.** Sobreposição entre ramos é erro em qualquer árvore: produz dupla contagem e duplica esforço.

**Colectivamente exaustivo varia com o propósito.** Numa árvore de problema é estrito desde o início — a soma das partes é o problema todo, e uma lacuna esconde a causa. Numa árvore de caracterização é aspiracional: exigir exaustividade antes de investigar bloqueia a árvore no primeiro nó, porque implica conhecer o espaço total antes de o conhecer. Verifica-se ao fechar, não ao abrir.

**Um eixo por nó.** Num nó só se aplica um eixo de corte. Partir facturação por geografia *ou* por tipo de cliente, nunca ambos no mesmo nível. Iterar níveis é permitido e é como se compõem eixos: nível 1 por geografia, nível 2 cada geografia por tipo de cliente. Misturar eixos no mesmo nível é a violação de MECE mais frequente na prática.

**Profundidade desigual não é defeito.** Numa árvore de decisão, aprofundar um ramo e deixar outro em esboço é alocação de esforço. O defeito seria o ramo raso desaparecer sem ficar registado que se decidiu não o aprofundar.

#### Critério de corte

Um corte vale se passar dois filtros, ambos aplicáveis antes de haver dados.

**Assimetria.** O melhor corte é o que cria maior diferença entre ramos e isola o problema numa área. Se a produtividade caiu 10% em todo o lado, cortar por geografia não serve. Serve se revelar que uma região caiu 40% e o resto está estável.

**Acionabilidade.** O corte tem de recair sobre variável que se consiga controlar ou influenciar. Um corte perfeito sobre algo inalterável não produz decisão.

#### Triagem antes de dados

Antes de recolher evidência, estimativa de ordem de grandeza e cenário extremo: *se este ramo variasse dez vezes, mudava a decisão final?* Se não, descarta-se o ramo sem o testar empiricamente.

Esta triagem é gratuita e é o que impede a árvore de gerar frentes a mais. Sem ela, todos os ramos viram trabalho.

#### Árvores múltiplas e árvores acopladas

No arranque desenham-se árvores concorrentes com eixos conceptuais distintos sobre o mesmo problema. Vivem em simultâneo até a triagem preliminar matar as estéreis. Uma árvore só é o mesmo erro que um caminho só: não é escolha, é inércia.

Árvores de propósito diferente sobre o mesmo objecto **não se fundem**. Uma árvore de caracterização cresce com evidência; uma de decisão fecha com escolha. Fundidas, a decisão nunca fecha, porque há sempre mais para caracterizar.

Acoplam-se por dependência declarada: um ramo de decisão declara que depende de um ramo de caracterização. Quando o segundo devolve resultado, o primeiro reavalia, com duas saídas apenas — aprofundar ou podar.

O caso típico: a árvore de estudo devolve o que as opções significam naquele contexto concreto; a árvore de decisão aprofunda dois ramos e poda os restantes. A evidência não decidiu — mudou o significado das opções, que é o que a torna útil.

#### Estado de ramo

`por abrir` · `em desenvolvimento` · `fechado` · `podado` · `suspenso: <dependência>`

**Podado não é rejeitado.** É "decidiu-se não aprofundar", e a razão fica registada. Sem isso o ramo volta dentro de dois meses com outro nome.

#### Protocolo P1 — Árvore

- **P1.1** — Cada árvore **deve** declarar, ao nascer, o seu propósito e a condição em que morre.
- **P1.2** — Num nó **não pode** ser aplicado mais de um eixo de corte.
- **P1.3** — Ramos irmãos **não podem** sobrepor-se.
- **P1.4** — Um ramo **deve** declarar as suas dependências no momento em que é desenhado.
- **P1.5** — Um ramo **não pode** passar a trabalho sem ter passado a triagem de ordem de grandeza.
- **P1.6** — Um ramo podado **deve** registar a razão.
- **P1.7** — Árvores de propósito diferente **não podem** ser fundidas.

Uma árvore sem condição de morte é uma árvore eterna, e uma árvore eterna transforma-se na lista de tarefas que geram tarefas — com melhor genealogia, o que a torna mais difícil de matar.

---

### 2.3 O caminho

Entre o mandato e as frentes há uma camada que decide **por onde**. Sem ela, cada frente deriva directamente do mandato e é uma aposta isolada que ninguém consegue avaliar.

**Caminho** é a hipótese, hoje, sobre como se chega ao mandato. Não é um plano: é uma aposta entre apostas possíveis, com os pressupostos que a sustentam declarados e testáveis.

A árvore e o caminho dividem o trabalho: **a árvore gera os cortes, o caminho testa-os.** E testam em momentos diferentes — a triagem de ordem de grandeza mata ramos antes de haver dados, de graça; o caminho testa com dados reais o que sobreviveu, e é caro. Juntar os dois testes faz desaparecer a triagem e transforma todos os cortes em frentes.

#### Método de procura

O caminho não se escolhe no início. Escolhe-se depois do primeiro teste que elimina alternativas.

```
M1  Enunciar o mandato como pergunta de decisão
M2  Desenhar as árvores concorrentes e triar as estéreis
M3  Por árvore sobrevivente, extrair o que tem de ser verdade — os pressupostos
M4  Marcar os discriminantes: pressupostos cuja resposta elimina caminhos
M5  Ordenar por (incerteza × custo de descobrir tarde) ÷ custo de testar
M6  A primeira frente testa o discriminante do topo
M7  Nenhum caminho é declarado escolhido antes de M6 devolver resultado
```

O discriminante de M4 é o corte de maior assimetria da árvore que sobreviveu. As frentes derivam do caminho, não do mandato: uma frente que não testa um pressuposto nem executa um caminho já escolhido não tem razão para existir.

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

#### Como se avalia

Um milestone não é um entregável: é um teste de pressuposto. A pergunta não é *o que fica pronto* mas *o que fica a saber-se*.

| Resultado | Significado | Consequência |
|---|---|---|
| `confirmado` | o pressuposto aguenta | avança para o seguinte na ordem |
| `invalidado` | o pressuposto cai | reavaliação obrigatória |
| `inconclusivo` | o teste não decidiu | redesenhar o teste, não repetir |

`inconclusivo` diz algo sobre o sistema, não sobre o projecto: a regra de paragem foi escrita sem critério verificável.

#### Como se reavalia

Três disparos: pressuposto invalidado, cadência fixa, ou vontade do humano.

```
reavaliação → quatro saídas, mutuamente exclusivas

  manter             nada mudou que altere a ordem
  reordenar          mudou a ordem de ataque, não o caminho
  trocar de caminho  o caminho actual cai; outro dos abertos assume
  escalar            o mandato é que está errado → modo rumo
```

**Mudar de caminho não é mudar de rumo.** É o que evita que cada surpresa técnica se transforme numa discussão existencial. Só a quarta saída toca no mandato.

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

**Um nível nunca escreve no nível acima.** Uma sessão não altera o estado; uma frente não altera o caminho. O que sobe é um pedido, não uma alteração.

#### 2.4.2 Escopo de contexto

Corolário directo da hierarquia: **cada nível classifica o seu trabalho contra o nível imediatamente acima, nunca contra o topo.**

| Quem | Classifica contra | Não precisa de |
|---|---|---|
| Sessão | o mandato da frente | o caminho, o mandato |
| Frente | o pressuposto que testa e a regra de paragem | o mandato |
| Triagem | os ramos que o alerta toca | o projecto inteiro |
| Caminho | o mandato | a intenção por trás |
| Rumo | a intenção do humano | — |

Uma frente sem o mandato geral continua a detectar que derrapou, porque derrapar é sair do **seu pressuposto**. O `challenges` que emite significa "o meu pressuposto caiu", não "o projecto está errado" — a tradução para eventual emenda é feita por quem tem o mandato.

Consequência: a projecção de uma frente não se redige, **deriva-se** do caminho. Objectivo = o pressuposto mais a regra de paragem. Fronteiras negativas = os pressupostos atribuídos às outras frentes.

**Uma excepção.** Os objectivos são escopáveis; os não-objectivos não são. Uma fronteira que não está carregada não bloqueia nada, e o erro provável não é cair fora de um objectivo específico — é cair fora do mandato todo. Os não-objectivos são baratos e vão inteiros em qualquer sessão que classifique seja o que for.

#### 2.4.3 Actores

| Actor | É agente | Dispara por | Escreve em |
|---|---|---|---|
| **Humano responsável** | não | vontade | tudo |
| **Arquitecto · triagem** | sim | alerta | `ESTADO`, `FRENTES`, `REJEICOES` |
| **Arquitecto · rumo** | sim | só o humano | emenda ao mandato, ou nada |
| **Frente** | sim | trabalho | a sua worktree, `INBOX` |
| **Auditor** | sim | cadência | relatório |
| **Watcher** | **não** | cada merge | `ALERTA` |

O watcher não tem modelo. É um script. O processo que vigia está sempre ligado; o que julga é sempre uma sessão fria e curta. Um agente permanente acumula contexto e deriva — e seria o pior sítio do sistema para isso acontecer.

#### 2.4.4 Ferramentas

| Ferramenta | Função | Substitui |
|---|---|---|
| **Árvore** | partição do espaço, geração de cortes | ataque por um ângulo só |
| **Worktree** | isolamento, paralelismo, merge como verificação | disciplina de não mexer na pasta alheia |
| **Hook de caminho** | confinamento de leitura e escrita por perfil | regras escritas em prosa |
| **Índice de decisões** | liga slugs a decisões; protege o que foi debatido | memória de quem estava presente |
| **Watcher** | cruzar declarações e seguir dependências | reuniões de coordenação |
| **Cold-read** | verificar auto-suficiência de um output | confiança |
| **Proveniência selada** | registo imutável, fora do índice de pesquisa | memória |
| **HALT** | paragem imediata de todas as escritas | — |

#### 2.4.5 Ficheiros

| Ficheiro | O que é | Escrita | Quem |
|---|---|---|---|
| `MANDATO` | a lei do projecto | emenda datada | agente redige, humano valida |
| `CAMINHO` | a hipótese de como se lá chega | substituição | humano com agente |
| `arvores/*` | partições do espaço, por propósito | substituição | humano com agente |
| `CASOS` | casos-fronteira decididos | acrescento | humano, triagem |
| `ESTADO` | o que é verdade agora | **substituição** | triagem |
| `FRENTES` | índice de frentes e ramos | substituição | triagem |
| `REJEICOES` | o que foi descartado e porquê | acrescento | triagem |
| `ALERTA` | o que o watcher detectou | substituição | watcher |
| `INBOX/*.json` | descobertas por processar | acrescento | frentes |
| `debates/*.json` | decisões, com alternativa rejeitada e o que afectam | acrescento | rumo |
| `indice-decisoes.json` | slug → decisão | **gerado** | script |
| `estado.json` | estado da frente face ao seu pressuposto | substituição | frente |
| `handoff.json` | como retomar | substituição | frente |
| `research/` | exploração | livre | frente |
| `entregue/` | o que sobe | acrescento | frente |
| `Rascunhos` | travão intra-sessão | termina vazio | frente |
| `sealed/` | pedido, output, referências | write-once | hook |
| `HALT` | interruptor | presença | humano |

- **Estado substitui-se, evidência acumula-se.** Nunca no mesmo ficheiro.
- **O caos tem lugar próprio.** `research/` e `Rascunhos` existem para a exploração não contaminar o estado. Não se disciplinam.
- **Nada que uma ferramenta possa reconstruir entra em memória.** A proveniência guarda referências, não conteúdo.

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

A coluna da direita não é proibida. É o que não entra no estado curado — vive na proveniência selada, recuperável e não lida.

#### 2.4.7 Fluxos, do geral ao átomo

**L0–L2 · Projecto**

```
MANDATO → ÁRVORES → CAMINHO → frentes → merges → watcher → ALERTA

ALERTA vazio            → nada acontece
ALERTA com item         → triagem
triagem toca no mandato → escala ao humano → rumo → emenda → MANDATO
```

**L3 · Frente**

```
F1  Abre com projecção derivada do caminho
F2  Sessões de trabalho, N ≥ 1
F3  Fecho de cada sessão: gate
F4  Pressuposto resolvido → frente fecha → resultado ao caminho
```

**L4 · Sessão — o átomo**

```
S1  HALT presente?                    sim → recusa
S2  Perfil declarado?                 não → recusa
S3  Monta contexto por perfil e por escopo
S4  Trabalha
      escrita fora da zona            → bloqueia, devolve zona, continua
      edição de slug com decisão      → bloqueia ou alerta, conforme o nível
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

Não existe estado de espera. Uma sessão nunca fica bloqueada à espera de outro actor: declara o pressuposto que assumiu e prossegue.

#### 2.4.8 Mecanismos

**Gate de fecho.** Dois níveis. Divergência dura — o que a frente tocou saiu do que declarou, ou o que produziu não serve pressuposto nenhum — bloqueia o fecho. Divergência branda — pressuposto novo, cold-read fraco — deixa fechar com marca e sobe ao alerta. O primeiro protege o projecto; o segundo protege o ritmo.

**Detecção, três passagens.**

| Passagem | Base | Confiança | Apanha |
|---|---|---|---|
| Colisão | campo `toca` | facto | duas frentes na mesma coisa |
| **Dependência** | arestas da árvore | **facto** | conclusão que muda outro ramo |
| Semântico | chamada única de modelo | sugestão | o que ninguém declarou |

A passagem de dependência é a mais valiosa e a mais barata: quando uma frente fecha um ramo, o script segue as arestas já declaradas e vê quem ficava à espera daquilo. Apanha o conflito sem colisão de ficheiros — duas frentes em pastas separadas onde a conclusão de uma altera o significado do trabalho da outra.

O detector semântico desce a rede de segurança, que é o lugar certo para uma detecção probabilística. E ganha uma função nova: **quando apanha um conflito que a árvore não previa, falta uma aresta.**

**Alerta com estado.** Cada alerta é `novo`, `visto` ou `descartado`, com hash do conteúdo. Um descartado não reaparece para o mesmo par no mesmo estado. Sem isto o ficheiro dispara sempre e deixa de ser lido em duas semanas.

**Protecção do que foi decidido.** Tudo tem slug — documentos, regras, decisões, ramos, pressupostos. Os slugs são globais, nunca se reutilizam e nunca se renumeram. A decisão declara o que afecta; o índice é gerado por inversão e nunca é escrito à mão.

Ao editar, o hook extrai o slug e consulta o índice:

| Nível | Origem | Comportamento |
|---|---|---|
| `livre` | sem decisão | edita |
| `decidido` | decisão registada | alerta, pede confirmação humana |
| `selado` | decisão com `selado` | bloqueia; só nova decisão desbloqueia |
| `morto` | slug retirado por decisão | bloqueia a recriação |

O alerta devolve o identificador da decisão e o facto de existir. **Nunca o conteúdo do debate, a alternativa rejeitada ou a razão.** O agente recebe material para parar, não para formar opinião. Assim o protocolo não contém uma única referência a decisões e continua protegido.

Uma regra retirada sai da vista do agente e vive no arquivo, dada como morta. O quarto nível impede ressurreição silenciosa — o mesmo mecanismo que impede reabrir becos sem saída, aplicado ao governo. Limite: só apanha reintrodução pelo mesmo slug; conteúdo equivalente com slug novo é trabalho do auditor.

**Cold-read.** Um agente sem histórico lê o output ou o handoff e responde a uma pergunta fechada. Para um handoff: *consegues enunciar o próximo passo e o critério que o dá por feito?* Se não consegue, é inválido. O teste é sobre a acção seguinte, não sobre compreensão do tema.

**Paragem.** A presença do ficheiro `HALT` faz o hook recusar arranque e qualquer escrita. As sessões vivas ficam inertes na operação seguinte. Não se terminam processos: matar a meio deixa ficheiros parciais. O `HALT` é removido à mão, e o caminho dos hooks e o índice de decisões estão fora de todas as zonas de escrita.

#### 2.4.9 Regra de saída

Transversal a todos os níveis: handoff, entregue, alerta, relatório.

**A resposta primeiro.** A recomendação ou conclusão encabeça o documento. Abaixo, três ou quatro pilares de suporte, MECE entre si. Na base, a evidência que sustenta cada pilar.

A árvore é lógica de partição do problema; esta é lógica de comunicação do resultado. Confundi-las produz documentos que expõem a análise em vez de a concluir. O cold-read é a verificação mecânica desta regra: um output que não é decifrável de cima, sem contexto, não a cumpre.

#### 2.4.10 Escolha de agente por papel

Os papéis da §2.4.3 são funções, não produtos. Cada um tem requisitos que derivam da arquitectura, e é por eles que se escolhe onde corre — não pela preferência de ferramenta.

**Seis critérios**

| Critério | Pergunta |
|---|---|
| Duração | o papel vive enquanto trabalha, ou tem de estar sempre ligado? |
| Disparo | quem o invoca: humano, evento, ou calendário? |
| Filesystem | precisa de worktree, git e ficheiros locais? |
| Enforcement | precisa de hooks que **bloqueiem** uma operação antes de executar? |
| Escopo | o contexto tem de ser montado por perfil e cortado? |
| Julgamento | o papel decide, ou só detecta? |

O critério de enforcement é eliminatório. Um papel que escreve em zonas protegidas só pode correr onde existam hooks bloqueantes. Sem isso, as regras voltam a ser prosa.

**Requisitos por papel**

| Papel | Duração | Disparo | Precisa de | Natural em |
|---|---|---|---|---|
| **Frente** | efémera | humano ou orquestrador | filesystem, git, hooks bloqueantes | runner de código local |
| **Arquitecto · triagem** | efémera, curta | evento (alerta) | leitura ampla, escrita escopada, invocação por máquina | runner invocável programaticamente |
| **Arquitecto · rumo** | efémera | só o humano | conversa, sem escrita automática | interface de chat |
| **Auditor** | efémera | calendário | leitura total, sem escrita | infraestrutura agendada |
| **Watcher** | **persistente** | cada merge | nenhum modelo; processo e disco | infraestrutura sempre ligada |
| **Detector semântico** | por chamada | dentro do watcher | uma chamada sem estado | API directa, sem agente |

**Três regras de alocação**

**O que está sempre ligado não julga.** Infraestrutura persistente serve para vigiar, disparar e agendar. Todo o papel que decide corre numa sessão fria e curta, arrancada por ela. Um agente permanente a julgar acumula contexto e deriva — e seria o pior sítio do sistema para isso acontecer.

**O enforcement vive no runner que executa, não no que orquestra.** Se uma infraestrutura persistente dispara uma sessão de trabalho noutro runner, os hooks têm de estar do lado do runner que escreve. Um orquestrador que valida caminhos mas delega a escrita a um processo sem hooks não protege nada.

**Um papel pode mudar de runner; o contrato não muda.** O que define a frente é a projecção, a zona e o gate de fecho — não onde corre. Mudar de ferramenta é substituição de implementação, e como tal passa por decisão registada.

**Falha de runner é recusa, não passagem.** Se o runner de um papel está indisponível, o comportamento é bloquear, nunca deixar passar. Um hook que não responde equivale a `HALT` para as operações que dependiam dele.



Um sistema que só impede movimento é uma jaula. Este distingue três formas de mudar.

Antes das três: a maior parte da mudança num projecto saudável é de **ramo ou de caminho**, não de rumo, e resolve-se nas camadas §2.2 e §2.3 sem tocar no mandato. Só chega aqui o que elas não conseguem absorver.

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

A frente nunca pára à espera desta cadeia. Continua com o pressuposto declarado.

#### Por vontade

O humano decide reavaliar sem que nada tenha falhado. Abre o modo rumo, o único modo que nenhum agente pode abrir. Produz uma emenda **ou nada** — e "nada" é resultado frequente e legítimo. **Nunca escreve no estado:** se escrevesse, cada alerta reabriria a discussão de rumo.

#### Por falha do próprio sistema

Um mecanismo não funciona. Entra no inbox, é triado, e se alterar como o projecto se governa, é emenda.

#### Deriva e inflexão

| | Deriva | Inflexão |
|---|---|---|
| Alteração do objectivo | real | real |
| Declarada | não | sim |
| Datada | não | sim |
| Alternativa registada | não | sim |
| Tratamento | é o que o sistema existe para impedir | é saudável |

Abrir frentes novas não é patologia. O que mata o projecto é a frente que altera o mandato sem o dizer. O sistema não impede movimento: torna impossível alterar o mandato sem emendar o mandato.

#### Registo de debates

Cada decisão produz um ficheiro com campos fechados: a decisão, a alternativa rejeitada, a razão, e os slugs que afecta. Não a discussão.

Serve duas funções: quando um mecanismo falhar daqui a meses, diz o que havia em alternativa e porque foi posto de lado; e alimenta o índice que protege o que foi decidido. É rastreabilidade, não história.

---

## 3 · Garantias permanentes

### 3.1 Tabela

| Garantia | Como se obtém | Como se mantém | Como se detecta a falha |
|---|---|---|---|
| **Existe um mandato** | P0, com os dois testes | tecto de uma página bloqueia emendas que inchem | nenhuma frente declara pressuposto válido |
| **É interpretado igual** | não-objectivos e casos decididos | cada divergência vira caso | sondas de fronteira divergem entre sessões |
| **Chega a quem precisa** | injecção por escopo, não pesquisa | hook monta o contexto por perfil | sessão produz output sem pressuposto |
| **O problema foi partido** | árvores concorrentes, um eixo por nó | triagem mata as estéreis | árvore única, ou ramos sobrepostos |
| **As árvores morrem** | condição de morte declarada ao nascer | auditor lista as que a excederam | árvore aberta há mais tempo que a sua condição |
| **O caminho é explícito** | método de procura, mínimo dois | reavaliação a cada pressuposto invalidado | frente sem pressuposto declarado |
| **Ninguém sai da sua zona** | worktree e hook de caminho | hooks fora de todas as zonas | tentativa bloqueada no log |
| **O decidido não é mexido** | slugs, índice gerado, quatro níveis | slugs nunca reutilizados | regra alterada sem decisão correspondente |
| **O estado não apodrece** | substituição com orçamento | auditor com cadência fixa | contradições entre estado e frentes |
| **O lixo não entra** | quota, campos fechados, árbitro em código | `0` é resultado legítimo e frequente | inbox cresce mais do que se esvazia |
| **Conflitos aparecem** | três passagens do watcher | arestas declaradas ao desenhar o ramo | colisão descoberta por acaso |
| **Decisões são aplicadas** | verificação no fecho | — | decisão sem item correspondente |
| **Becos não reabrem** | razão de fecho e de poda registadas | slug morto bloqueia recriação | frente repete trabalho já fechado |
| **O rumo é rastreável** | emenda datada com alternativa | registo de debates | alteração no mandato sem entrada |
| **Cada papel corre onde deve** | requisitos por papel, enforcement eliminatório | mudança de runner passa por decisão | papel que escreve a correr sem hooks bloqueantes |
| **O governo não incha** | toda a regra nova exige falha observada | revisão por cadência | regras sem incidente que as justifique |

### 3.2 Manutenção no tempo

| Quando | O quê |
|---|---|
| **A cada fecho de sessão** | automático: gate, selagem, merge, watcher, regeneração do índice |
| **A cada alerta** | sessão fria de triagem; não existe se o alerta estiver vazio |
| **Por cadência fixa** | auditoria |

A auditoria é o único mecanismo que olha para o próprio sistema. Verifica: sondas de fronteira, contradições entre estado e frentes, alertas descartados que voltaram, árvores que excederam a condição de morte, ramos abertos sem dependências declaradas, regras alteradas sem decisão, e regras sem incidente que as justifique.

Sem ela, o governo cresce e ninguém nota; a correr mais do que uma vez por mês, o governo consome o projecto.

### 3.3 A garantia que nenhum mecanismo dá

Confinamento impede uma frente de estragar outra. Não impede que faça a coisa errada com perfeição dentro da sua própria zona.

Por isso a projecção — o pressuposto que testa e a regra de paragem — não é burocracia: é o único sítio onde fica escrito para que existe aquela frente. E deriva-se do caminho, pelo que não custa nada escrever.

Um sistema sem ela continua a funcionar, continua a bloquear escritas indevidas, continua a detectar colisões — e produz, com total ordem e rastreabilidade, trabalho que não serve para nada.

---

## 4 · Tensões em aberto

**T1 · Custo de declarar arestas.** Se declarar dependências não for barato no momento em que o ramo nasce, as arestas ficam vazias e o detector cala-se — pior do que não existir, porque parece estar a vigiar.
*Resolução adoptada:* tarefa no protocolo, no acto de desenhar o ramo (P1.4). Deixa de ser preenchimento posterior.
*Por verificar na prática.* Sinal gratuito: ramos abertos sem nenhuma aresta e que não são raiz. O auditor lista; a frequência responde sem ninguém ter de julgar.

**T2 · Completude das dependências.** A tarefa resolve o custo, não a completude. Declara-se o que se vê; o conflito caro é o que não se viu.
*Mitigação:* o detector semântico fica como rede de segurança e indica arestas em falta.

**T3 · Reintrodução por slug novo.** A protecção do decidido só apanha recriação pelo mesmo slug. Conteúdo equivalente com slug diferente escapa ao hook.
*Mitigação:* detecção semântica no auditor, não no momento da escrita.

**T4 · Dependência de runner.** Um papel alocado a um runner específico pára quando esse runner está indisponível.
*Resolução adoptada:* falha é recusa, nunca passagem — um hook que não responde equivale a `HALT` para as operações que dependiam dele.
*Custo assumido:* indisponibilidade de infraestrutura pára trabalho em vez de o deixar correr sem protecção. É a troca correcta.

**T5 · Inchaço por multiplicação de árvores.** Quatro propósitos e árvores múltiplas por projecto é o ponto onde o sistema pode crescer sem limite.
*Travão único:* P1.1 — condição de morte declarada ao nascer, verificada pelo auditor.
