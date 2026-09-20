---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Leitura da proposta de arquitectura recebida: conteúdo, críticas emitidas, alternativas
  propostas, complementos sugeridos e retractações.
---

# R2 · Leitura da proposta recebida

## 1 · O que o documento contém

**Estrutura.** Quatro partes: mandato do documento, arquitectura, garantias permanentes, tensões em aberto.

**Camadas declaradas.** Cinco níveis — projecto, caminho, estado, frente, sessão — com regra de não-escrita ascendente.

**Protocolos com identificador.** P0 nascimento, P1 árvore, P2 caminho.

**Actores.** Humano responsável, arquitecto em modo triagem, arquitecto em modo rumo, frente, auditor, watcher. O watcher não contém modelo.

**Mecanismos.** Gate de fecho em dois níveis; detecção em três passagens; alerta com estado e hash; protecção do decidido por slug em quatro níveis; cold-read; paragem por ficheiro.

**Garantias.** Dezasseis, cada uma com obtenção, manutenção e sinal de falha.

**Tensões declaradas pelo autor.** Cinco — custo de declarar arestas, completude das dependências, reintrodução por slug novo, dependência de runner, inchaço por multiplicação de árvores.

## 2 · Elementos identificados como superiores ao proposto

| Elemento | Conteúdo |
|---|---|
| Camada de caminho | a frente existe para testar um pressuposto com regra de paragem escrita antes de abrir |
| Escopo por nível | cada nível classifica contra o nível imediatamente acima, nunca contra o topo |
| Teste de discriminação do mandato | três sessões limpas classificam três tarefas, uma fora do mandato mas semelhante |
| Passagem de dependência | travessia das arestas declaradas ao fechar um ramo, sem colisão de ficheiros |
| Alerta com estado | hash de conteúdo impede reaparecimento de item descartado |
| Bloqueio sem razão | o hook devolve o identificador da decisão e nunca o conteúdo do debate |

## 3 · Críticas emitidas

| Identificador | Crítica |
|---|---|
| F1 | O caminho tem seis regras de forma e nenhuma verificação de conteúdo, enquanto o mandato tem dois testes falsificáveis |
| F2 | Existem tectos de extensão — uma página para mandato e caminho — e nenhum tecto numérico de árvores ou de frentes |
| F3 | Normas em prosa sem identificador: substituição de estado contra acumulação de evidência; excepção dos não-objectivos; três regras de alocação de runner; recusa por falha de runner; regra de saída; exigência de falha observada para regra nova |
| F4 | Lei e justificação no mesmo parágrafo |
| F5 | O âmbito declarado exclui projectos de frente única |

## 4 · Alternativas propostas

| Identificador | Alternativa | Estado |
|---|---|---|
| A-1 | Regra P2.7 — teste de discriminação aplicado ao caminho, por simetria com o do mandato | adoptada |
| A-2 | Tecto numérico de árvores e de frentes simultaneamente abertas, declarado no mandato | adoptada |
| A-3 | Identificador para cada norma em prosa | adoptada |
| A-4 | Separação do documento em lei e anexo de implementação | adoptada |
| A-5 | Coluna de implementação de origem na tabela de ferramentas | adoptada |
| A-6 | Perfil reduzido sem repositório nem hooks | retirada |
| A-7 | Mecanismo de ingestão por disciplina de leitura do arquitecto | retirada |

## 5 · Complementos sugeridos

| Complemento | Função |
|---|---|
| SQLite como substrato de arestas | armazenamento fora das zonas de escrita e travessia recursiva para o cone afectado |
| `sqlite-vec` | equivalência de conteúdo e sinalização de pesquisa já realizada |
| JSON Schema no hook | recusa mecânica de campos fora do contrato |
| `core.hooksPath` versionado e framework `pre-commit` | hooks que viajam com o repositório, com versões fixas |
| `git notes` | proveniência selada, imutável e fora do índice de pesquisa |
| Chamada de modelo sem sessão no merge | cold-read executado como verificação, não como conversa |
| OPA e `conftest` | gate de fecho e níveis de protecção como políticas declarativas com identificador |
| Alerta empurrado para canal | remove a dependência de alguém abrir um ficheiro |

**Ressalva registada.** `sqlite-vec` está em fase anterior à versão 1, com alterações incompatíveis previstas, e existe uma fork comunitária criada para integrar contribuições pendentes.

## 6 · Retractações

| Identificador | Elemento retirado | Fundamento aceite |
|---|---|---|
| A-6 | perfil reduzido por razão de custo | o custo do governo está no desenho dos mecanismos, já incorrido; um hook é execução |
| A-7 | disciplina de ingestão do arquitecto | um mecanismo que depende de convocação humana não é mecanismo |

## 7 · Lacuna identificada por aplicação do critério do próprio documento

O alerta é obtido por consulta. A arquitectura exclui sessões convocadas para verificar alinhamento; pela mesma regra, exclui ficheiros que alguém tenha de abrir. Um ficheiro de alerta vazio e um ficheiro de alerta não lido são indistinguíveis.
