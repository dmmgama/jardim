---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Anexo de implementação do protocolo de governo: por cada função, as vias disponíveis,
  o que cada uma exige, o que cada uma custa e a regra que serve.
---

# Protocolo de governo de projectos multi-frente · Anexo de implementação

Esta secção é informativa. Não contém obrigação.

Cada função abaixo tem uma ou duas vias. Onde existem duas, ambas satisfazem a regra; diferem em custo, em alcance e no que deixam por cobrir. A escolha entre vias constitui decisão registável.

---

## A1 · Substrato de arestas

Serve P5.1, P5.2, P5.3, P5.7.

**Via 1 — ficheiros de declaração.** Cada ramo declara as suas arestas num campo do seu próprio ficheiro de registo. Um script percorre os ficheiros e constrói o grafo em memória a cada execução.

Exige: nada além do que já existe no repositório.
Custo: a travessia transitiva é código próprio; o grafo é reconstruído a cada passagem; os ficheiros são legíveis pelo agente que os contém, o que não satisfaz P5.3 sem os deslocar para fora da worktree.

**Via 2 — base relacional de ficheiro único.** As arestas residem em SQLite, fora de todas as zonas de escrita. O cone afectado obtém-se por expressão de tabela comum recursiva numa única consulta.

Exige: SQLite, presente na biblioteca padrão do Python.
Custo: um esquema a manter; um ponto de escrita adicional no fluxo de fecho.
Cobre P5.3 por construção: o ficheiro não está em nenhuma zona de leitura de agente.

**Diferença decisiva.** A Via 1 satisfaz a declaração das arestas; a Via 2 satisfaz também a sua invisibilidade e a travessia. Projectos sem exigência de P5.3 podem usar a Via 1.

---

## A2 · Imposição por hook

Serve P3.2, P4.1, P4.2, P4.7, P6.7, P6.8, P6.9, P9.1, P9.2, P9.3, P9.9.

**Via 1 — hooks do runner de agente.** Ganchos de pré-execução que inspeccionam a operação e devolvem código de recusa. Residem na configuração do runner.

Exige: runner com ganchos bloqueantes.
Custo: a lógica vive em código imperativo; a correspondência entre regra e hook é convenção.

**Via 2 — política declarativa.** As regras exprimem-se como políticas avaliadas sobre a representação da operação em JSON, com identificador por política. Um avaliador corre no hook e na integração contínua.

Exige: motor de políticas e a sua linguagem.
Custo: linguagem adicional; sobrecarga desproporcionada para conjuntos de regras pequenos.
Ganho: correspondência directa entre identificador de regra e identificador de política, verificável por teste.

**Comum às duas vias.** Os hooks devem viajar com o projecto. A configuração do repositório permite apontar o caminho dos ganchos para pasta versionada, em vez da pasta interna que existe por cópia local. Um arnês de gestão de hooks acrescenta versões fixas e execução sobre ficheiros preparados.

---

## A3 · Contrato dos ficheiros de troca

Serve P4.9, P4.10, P4.11, P6.4, P7.10.

**Via única — validação por esquema.** Os ficheiros de inbox, de estado de frente, de handoff e de decisão são validados contra esquema JSON no momento da escrita. Um campo ausente ou fora do domínio produz recusa.

Exige: validador de esquema no hook.
Cobre a única condição que torna a noção de campo fechado verificável.

---

## A4 · Isolamento e integração

Serve P3.2, P4.14, P7.3.

**Via única — árvores de trabalho paralelas.** Cada frente ocupa uma árvore de trabalho própria sobre o mesmo repositório. A integração é o momento de verificação, e o gancho de pós-integração dispara o watcher.

Exige: controlo de versões distribuído.
Nota: sem paralelismo, a árvore de trabalho continua a servir o confinamento de escrita.

---

## A5 · Proveniência selada

Serve P4.14, P8.8, P8.9.

**Via 1 — pasta de escrita única.** Um directório fora das zonas de escrita recebe ficheiros que o hook cria e nunca reabre.

Exige: hook que recuse reescrita.
Custo: a pasta entra no índice de pesquisa salvo exclusão explícita, o que contraria P8.9.

**Via 2 — anotações do controlo de versões.** O registo fica em anotações associadas às revisões, fora da árvore de trabalho e fora do índice de conteúdo.

Exige: controlo de versões com suporte de anotações.
Custo: recuperação menos directa; exige comando próprio para leitura.
Cobre P8.9 por construção.

---

## A6 · Cold-read

Serve P4.13, P8.3, P8.4.

**Via 1 — sessão dedicada.** Uma sessão sem histórico recebe o documento e responde à pergunta fechada.

Custo: é uma sessão; consome o orçamento que o protocolo procura poupar.

**Via 2 — chamada sem sessão.** O gancho de pós-integração emite uma chamada única ao modelo com o documento e a pergunta, e converte a resposta em código de saída.

Exige: acesso programático a um modelo.
Custo: uma chamada por fecho de sessão.
Diferença: a Via 2 não produz conversa nem contexto persistente.

---

## A7 · Equivalência de conteúdo

Serve P6.14, P6.15, P6.16, P7.8, P10.11.

**Via 1 — correspondência por slug.** O confronto compara identificadores. Conteúdo equivalente registado sob slug distinto não é detectado.

Exige: o índice de decisões, que já existe.
Custo: cobertura parcial declarada.

**Via 2 — pesquisa vectorial no mesmo substrato.** Cada pressuposto, ramo e pergunta é vectorizado ao nascer. Uma pesquisa lançada é comparada por distância contra os ramos fechados e podados.

Exige: extensão de pesquisa vectorial sobre SQLite, escrita em C sem dependências, e uma fonte de vectorização.
Custo: a extensão está em fase anterior à versão 1, com alterações incompatíveis previstas, e existe uma fork comunitária criada para integrar contribuições pendentes. A versão deve ser fixada.
Cobre a lacuna que a Via 1 declara.

---

## A8 · Entrega do alerta

Serve P7.12.

**Via 1 — ficheiro consultado.** O watcher escreve num ficheiro. O alerta é lido quando alguém o abre.

Custo: um ficheiro vazio e um ficheiro não lido são indistinguíveis.

**Via 2 — canal empurrado.** O watcher emite para um canal que notifica sem intervenção, e a triagem é invocada do lado receptor.

Exige: canal de notificação e invocação programática da triagem.
Cobre P7.2 sem depender de hábito.

---

## A9 · Auditoria por cadência

Serve P10.2, P10.3.

**Via 1 — temporizador local.** Agendador do sistema operativo no runner onde o projecto reside.
Custo: depende de a máquina estar ligada.

**Via 2 — agendamento remoto.** Tarefa agendada na integração contínua do repositório.
Custo: exige o repositório acessível remotamente.

---

## A10 · Materialização do mapa

Serve P6.13 e a leitura humana.

**Via 1 — ficheiro de grafo mantido.** Um documento com a sintaxe de grafo é editado quando a árvore muda.
Custo: segunda fonte de verdade; dessincroniza em silêncio.

**Via 2 — projecção gerada.** O grafo é produzido por consulta ao substrato de arestas e regravado no mesmo acto em que o estado é escrito. A omissão das razões de fecho é uma selecção de colunas.
Exige: gerador de sintaxe de grafo a partir da consulta.
Cobre P6.13 por construção.

---

## A11 · Geração de mandatos de frente

Serve P3.1, P1.4.

**Via 1 — derivação manual.** A projecção deriva-se do caminho por escrita directa: o objectivo é o pressuposto e a regra de paragem; as fronteiras negativas são os pressupostos atribuídos às outras frentes.
Custo: nenhum além do tempo de escrita.

**Via 2 — planeador com briefs autónomos.** Uma ferramenta de planeamento converte o objectivo em passos com contexto autónomo por passo, mapa de dependências e detecção de paralelismo.
Exige: instalação da ferramenta e leitura das suas instruções.
Custo: o plano é gerado de uma vez; a incorporação de resultado posterior faz-se por regeneração.
Ganho: as arestas iniciais saem prontas, o que reduz o custo de P1.4.

---

## A12 · Ficheiros

| Ficheiro | Conteúdo | Modo de escrita | Autor |
|---|---|---|---|
| `MANDATO` | objectivos, não-objectivos, critério de fim, tectos, canal de alerta, cadência de auditoria | emenda datada | agente redige, humano valida |
| `CAMINHO` | caminhos plausíveis, pressupostos, ordem de ataque, regras de paragem | substituição | humano com agente |
| `arvores/` | ramos, propósito, condição de morte, estados | substituição | humano com agente |
| `CASOS` | tarefas-fronteira classificadas | acrescento | humano, triagem |
| `ESTADO` | proposições verdadeiras no presente | substituição | triagem |
| `FRENTES` | índice de frentes e ramos | substituição | triagem |
| `REJEICOES` | itens descartados e razão | acrescento | triagem |
| `decisoes/` | escolha, alternativa, razão, slugs afectados | acrescento | modo rumo |
| `INBOX/` | matéria por processar | acrescento | frentes |
| `arestas.db` | arestas, níveis, vectores | escrita por hook | máquina |
| `indice-decisoes` | slug para decisão | gerado | máquina |
| `<frente>/estado` | estado da frente face ao pressuposto | substituição | frente |
| `<frente>/handoff` | retoma | substituição | frente |
| `<frente>/research/` | exploração | livre | frente |
| `<frente>/entregue/` | entrega | acrescento | frente |
| `<frente>/rascunhos` | matéria fora da projecção | termina vazio | frente |
| `selado/` | pedido, resposta, referências | escrita única | hook |
| `HALT` | interruptor | presença | humano |

---

## A13 · Ordem de montagem

1. Árvores de trabalho e confinamento de escrita por zona.
2. Validação de esquema nos ficheiros de troca.
3. Substrato de arestas e cálculo do cone afectado.
4. Slugs, registo de decisões e índice gerado.
5. Gate de fecho.
6. Watcher e passagens de colisão e de dependência.
7. Entrega do alerta e invocação da triagem.
8. Cold-read.
9. Proveniência selada.
10. Auditoria por cadência.
11. Passagem de equivalência.

Os passos 1 a 5 impõem. Os passos 6 a 8 detectam e encaminham. Os passos 9 a 11 verificam o sistema.

---

## A14 · Correspondência entre regra e via

| Regra | Função | Vias |
|---|---|---|
| P1.4, P5.1 a P5.10 | arestas e cone | A1 |
| P3.2, P4.1, P4.2, P4.7, P6.7 a P6.9, P9.1 a P9.3, P9.9 | imposição | A2 |
| P4.9 a P4.11, P6.4, P7.10 | contrato de ficheiros | A3 |
| P3.2, P4.14, P7.3 | isolamento e integração | A4 |
| P4.14, P8.8, P8.9 | proveniência | A5 |
| P4.13, P8.3, P8.4 | cold-read | A6 |
| P6.14 a P6.16, P7.8, P10.11 | equivalência | A7 |
| P7.12 | entrega do alerta | A8 |
| P10.2, P10.3 | auditoria | A9 |
| P6.13 | mapa legível | A10 |
| P1.4, P3.1 | mandatos de frente | A11 |

---

## A15 · Funções sem ferramenta

Duas funções do protocolo não correspondem a nenhuma ferramenta disponível e são inteiramente escrita própria:

**A camada de caminho.** P2.1 a P2.18. Nenhuma ferramenta examinada representa a hipótese corrente, os seus pressupostos, os discriminantes e as regras de paragem. As ferramentas de planeamento representam a ordem do trabalho, não a sua condição de validade.

**O escopo por nível.** P4.4 e P4.5. Nenhuma ferramenta examinada monta o contexto de uma sessão por corte hierárquico. A montagem é código no hook, a partir do perfil declarado.
