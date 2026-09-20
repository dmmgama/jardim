---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Mandato desta sessão, ramificações que produziu, ferramentas descobertas, objectos
  propostos, mecanismos de enforcement e juízo de viabilidade.
---

# R1 · Mandato e exploração

## 1 · Mandato

**Enunciado.** Localizar frameworks, sistemas de governo ou repositórios existentes que endereçassem a perda de enquadramento do arquitecto perante outputs de threads isoladas.

**Objectivo com slug.** `mandato/encontrar-existente`

**Não-objectivos declarados.**

| Slug | Não-objectivo | Origem |
|---|---|---|
| `nobj/construir-governo` | construir um sistema de governo de raiz | declarado pelo humano |
| `nobj/versao-degradada` | produzir versão reduzida por razões de custo | declarado pelo humano |
| `nobj/disciplina-humana` | propor mecanismos que dependam de sessões de controlo | declarado pelo humano |

**Critério de fim.** Lista de mecanismos necessários, cada um classificado como montável a partir de ferramenta existente ou como autoral.

## 2 · Ramificações produzidas

O mandato foi partido por eixo de disciplina de origem. Sete ramos.

| Slug | Ramo | Resultado | Estado |
|---|---|---|---|
| `ramo/orquestracao` | orquestração de agentes | endereça delegação, não composição | podado |
| `ramo/spec-driven` | desenvolvimento dirigido por especificação | correcto em princípio, ligado a artefactos de código | podado |
| `ramo/memoria` | memória persistente e bancos de contexto | fértil na estrutura de ficheiros, sem enforcement | parcial |
| `ramo/decomposicao` | engenharia de sistemas e decomposição | o mais fértil; método, não ferramenta | fértil |
| `ramo/atencao` | atenção e janela de contexto | fértil no diagnóstico, estéril na solução | podado |
| `ramo/planeadores` | planeadores de tarefa com briefs autónomos | cobre a geração de mandatos | fértil |
| `ramo/enforcement` | infraestrutura de bloqueio e detecção | cobre a maioria dos mecanismos | fértil |

**Razões de poda.**

`ramo/orquestracao` — a literatura assume que o orquestrador retém o contexto global e que os subagentes são invocados dentro da sua sessão. A estrutura em causa tem threads como repositórios isolados com entrega diferida.

`ramo/spec-driven` — os planos são listas ordenadas com caixas de verificação. Uma lista não representa arestas; adoptá-la reproduz o modo de falha que o mandato pedia para resolver.

`ramo/atencao` — as correcções conhecidas são disciplina de leitura e reescrita de objectivo. Colidem com `nobj/disciplina-humana`.

## 3 · Discriminante

**Pressuposto testado.** As arestas entre unidades de trabalho são recuperáveis a partir dos artefactos produzidos.

**Resultado.** Invalidado fora de software. Em código as dependências estão inscritas nos artefactos — importações, chamadas, árvore de módulos — e o compilador é o detector. Fora de código não há inscrição nem detector: as arestas só existem se forem declaradas.

**Consequência.** Nenhuma ferramenta orientada a repositórios de código resolve o problema por transposição. O que é transponível é a camada de enforcement, não a camada de detecção semântica.

## 4 · Ferramentas descobertas

| Ferramenta | O que faz | Aplicação ao mandato |
|---|---|---|
| Blueprint (skill de planeamento) | gera planos modulares com briefs autónomos por passo, mapa de dependências e detecção de paralelismo | cobre a geração de mandatos e o desenho inicial de arestas |
| `git worktree` | árvores de trabalho paralelas sobre o mesmo repositório | isolamento de frentes e merge como verificação |
| Hooks de agente e de repositório | interceptam operações antes da execução e recusam por código de saída | única via de imposição não sugestiva |
| `core.hooksPath` versionado | desloca os hooks para pasta versionada, fora de `.git/hooks` | os hooks viajam com o repositório em vez de viverem por clone |
| Framework `pre-commit` | declaração de hooks em YAML com versões fixas e execução sobre ficheiros preparados | arnês de gestão dos hooks |
| SQLite | base relacional de ficheiro único, sem servidor, com travessia recursiva em SQL | substrato de arestas e cálculo do cone afectado |
| `sqlite-vec` | pesquisa vectorial dentro de SQLite, em C puro, sem dependências | detecção de equivalência de conteúdo e sinalização de pesquisa repetida |
| JSON Schema | validação declarativa de estrutura de dados | converte campos fechados em recusa mecânica |
| OPA / `conftest` | motor de políticas declarativas avaliadas sobre JSON, com identificadores | expressa o gate de fecho e os níveis de protecção como políticas versionadas |
| `git notes` | anotações imutáveis fora da árvore de trabalho e fora do índice de pesquisa | proveniência selada |
| Registo de decisões arquitecturais | formato e utilitários de decisão datada com alternativa e supersessão | índice de decisões e protecção do decidido |
| Mermaid | grafo declarativo renderizável em Markdown | materialização legível do mapa |
| Temporizador de sistema ou agendamento de integração contínua | execução por cadência | auditoria |

**Método, sem ferramenta.**

| Método | O que dá |
|---|---|
| Matriz de estrutura de desenho | representação matricial de trocas de informação e dependências entre actividades; distingue decomposição de integração |
| Arquitectura de quadro negro | fontes de conhecimento independentes que não se conhecem, publicando soluções parciais e restrições num repositório partilhado, com um componente de controlo |
| Árvore de questões | partição por eixo único com critério de assimetria e de accionabilidade |

## 5 · Objectos propostos

| Objecto | Forma | Razão da proposta | Destino |
|---|---|---|---|
| Quadro | modelo do entregável com estados por posição | uma lista de tarefas não tem arestas | substituído |
| Matriz de interfaces | tabela alimenta / é alimentado por | recompor exige declarar o fluxo de informação | substituído |
| Registo de restrições | ficheiro de acrescento puro | o estado substitui-se, a evidência acumula-se | substituído |
| Ficha de retorno | uma página com premissas, decisões e exclusões | a intenção não é recuperável do produto | substituído |
| Grafo | projecção Mermaid com arestas etiquetadas | a mesma informação num canal que torna visíveis a propagação e os nós órfãos | mantido, com origem alterada |

**Substituições.** Os quatro primeiros objectos foram desenhados como ficheiros mantidos por leitura humana. A proposta recebida resolve as mesmas funções por mecanismo automático.

| Objecto proposto | Substituído por | Ganho |
|---|---|---|
| Quadro | camada de caminho com pressuposto e regra de paragem | a frente passa a ter razão de existir, não posição |
| Matriz de interfaces | arestas em substrato fora das zonas de escrita | invisíveis ao agente, consultáveis pelo hook |
| Registo de restrições | decisões com alternativa e índice gerado por inversão | protecção activa contra reabertura |
| Ficha de retorno | pasta de entrega, ficheiro de retoma e cold-read | verificação mecânica de auto-suficiência |
| Recitação do quadro antes de avaliar | escopo por nível | nenhum nível precisa do global, logo não há global a esquecer |
| Avaliação por gabarito humano | gate de fecho e watcher | nenhuma sessão de avaliação |

O grafo manteve-se. Alterou-se a origem: deixa de ser ficheiro escrito e passa a ser projecção gerada por consulta ao substrato.

## 6 · Mecanismos de enforcement

| Mecanismo | Ferramenta | Natureza |
|---|---|---|
| Confinamento de escrita por zona | hook de caminho sobre worktree | bloqueio |
| Campos fechados nos ficheiros de troca | JSON Schema no hook | recusa na escrita |
| Gate de fecho de sessão | hook de fecho, ou política declarativa | bloqueio ou marca |
| Protecção do decidido | slug, índice gerado, quatro níveis | bloqueio, alerta ou recusa de recriação |
| Cone afectado | travessia recursiva no substrato de arestas | disparo de alerta |
| Colisão entre frentes | cruzamento do campo de toque no merge | disparo de alerta |
| Equivalência de conteúdo | pesquisa vectorial | sugestão |
| Auto-suficiência de saída | cold-read por chamada sem sessão | marca de aprovação pendente |
| Paragem total | presença de ficheiro verificada no hook | recusa de arranque |
| Indisponibilidade de hook | comportamento de recusa | recusa |

**Três a montar; um a construir.** A detecção de equivalência, o cone afectado e o confinamento existem como ferramenta. A camada de caminho — pressuposto, discriminante e regra de paragem — não existe em nenhuma ferramenta encontrada.

## 7 · Materialização do mapa

A árvore não é um ficheiro. É uma relação com quatro projecções, todas derivadas do mesmo substrato.

| Projecção | Destinatário | Conteúdo | Geração |
|---|---|---|---|
| Tabela de nós e arestas | hook e watcher | completa, com razões e níveis | fonte |
| Grafo legível | humano responsável | nós, estados e arestas, sem razões de fecho | consulta filtrada |
| Cone afectado | alerta | subconjunto transitivo a jusante de um nó | travessia recursiva |
| Índice de decisões | hook de protecção | slug para decisão, sem conteúdo de debate | inversão do registo de decisões |

A projecção legível omite por desenho a razão de fecho de cada ramo. A omissão é uma selecção de colunas, não uma disciplina de leitura.

## 8 · Conclusão

**O mandato é viável, com resultado parcialmente negativo.**

**Não existe.** Nenhum sistema único cobre o problema. Todos os candidatos examinados pressupõem repositório de código, onde as arestas estão inscritas nos artefactos.

**Existe por montagem.** Oito dos dez mecanismos necessários são ferramentas maduras. O trabalho é integração, não invenção.

**É autoral.** Dois mecanismos não têm equivalente:

1. A camada de caminho — a frente existe para testar um pressuposto declarado, com regra de paragem escrita antes de abrir.
2. O enforcement de ingestão sem sessão — a avaliação do impacto de um output no conjunto executada por máquina, com alerta empurrado.

**Proposta.** Montar oito, construir dois. O documento de protocolo que acompanha este relatório fixa os dois como regra e o resto como escolha de implementação.
