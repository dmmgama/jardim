---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Lei do protocolo de governo de projectos conduzidos por múltiplas sessões de agentes:
  definições, vocabulário modal e onze conjuntos de regras com identificador.
---

# Protocolo de governo de projectos multi-frente · Lei

## 0 · Aplicabilidade

Este documento governa projectos executados por múltiplas sessões de agentes sobre um corpo de trabalho comum, com ou sem paralelismo.

Este documento contém apenas regras. A informação sobre como as aplicar consta do anexo de implementação.

## 1 · Vocabulário modal

As palavras que carregam obrigação neste documento são três, e só três:

| Palavra | Significado |
|---|---|
| **deve** | obrigatório; a operação que o contrarie é inválida |
| **não pode** | proibido; a operação que o contrarie é recusada |
| **pode** | permitido; a ausência não constitui falha |

Nenhuma outra forma verbal carrega obrigação. Secções marcadas como informativas não contêm obrigação.

## 2 · Definições

Os termos abaixo são definidos uma única vez e nesta ordem.

**Projecto** — corpo de trabalho sujeito a um mandato único.

**Humano responsável** — pessoa singular que detém a intenção de que o mandato é reformulação.

**Agente** — processo que executa trabalho por inferência de modelo.

**Runner** — ambiente de execução onde um agente ou um processo corre.

**Hook** — programa que intercepta uma operação antes da sua execução e a permite ou recusa.

**Zona** — conjunto de caminhos em que um actor está autorizado a escrever.

**Slug** — identificador textual estável, único no projecto, atribuído a um objecto do projecto.

**Mandato** — documento que declara os objectivos do projecto, os seus não-objectivos e o critério de fim.

**Objectivo** — resultado que o projecto persegue.

**Não-objectivo** — resultado que o projecto exclui.

**Caso** — tarefa concreta cuja classificação dentro ou fora do mandato foi decidida e registada.

**Árvore** — partição de um espaço em ramos, com um propósito declarado.

**Propósito de árvore** — um de quatro: problema, caracterização, decisão, mandato.

**Ramo** — nó de uma árvore.

**Eixo de corte** — critério segundo o qual um nó é partido em ramos.

**Condição de morte** — critério declarado ao nascer de uma árvore, cuja verificação a encerra.

**Poda** — encerramento de um ramo por decisão de não o aprofundar.

**Triagem de ordem de grandeza** — estimativa que determina se a variação extrema de um ramo alteraria a decisão final.

**Aresta** — dependência declarada entre dois ramos.

**Substrato de arestas** — armazenamento onde as arestas residem.

**Cone afectado** — conjunto dos ramos alcançáveis a jusante de um ramo por travessia transitiva das arestas.

**Caminho** — hipótese corrente sobre como se atinge o mandato, sustentada por pressupostos declarados.

**Pressuposto** — proposição que tem de ser verdadeira para que um caminho se sustente.

**Discriminante** — pressuposto cuja resolução elimina pelo menos um caminho.

**Regra de paragem** — critério verificável que determina quando um pressuposto se considera resolvido.

**Estado de pressuposto** — um de quatro: por testar, confirmado, invalidado, inconclusivo.

**Reavaliação** — procedimento desencadeado pela resolução de um pressuposto ou pela vontade do humano responsável.

**Frente** — unidade de trabalho que testa um pressuposto ou executa um caminho já escolhido.

**Projecção de frente** — objectivo da frente e fronteiras negativas, derivados do caminho.

**Sessão** — período contínuo de trabalho de um agente dentro de uma frente.

**Perfil** — papel declarado por uma sessão, do qual decorrem a sua zona e o seu escopo de contexto.

**Escopo de contexto** — conjunto de documentos carregados numa sessão.

**Rascunhos** — depósito intra-sessão de matéria fora da projecção da frente.

**Inbox** — depósito de matéria destinada a processamento fora da frente.

**Gate de fecho** — verificação executada no encerramento de uma sessão.

**Cold-read** — verificação em que um agente sem histórico lê um documento e responde a uma pergunta fechada sobre a acção seguinte.

**Entrega** — documento que uma frente devolve ao projecto.

**Handoff** — documento que permite a retoma de uma frente por sessão sem histórico.

**Estado** — conjunto das proposições verdadeiras no momento presente.

**Evidência** — registo de facto ocorrido.

**Proveniência selada** — registo imutável de pedido, resposta e referências, fora do índice de pesquisa.

**Decisão** — registo datado que fixa uma escolha, a alternativa rejeitada, a razão e os slugs afectados.

**Índice de decisões** — correspondência de slug para decisão.

**Nível de protecção** — um de quatro: livre, decidido, selado, morto.

**Watcher** — processo sem modelo que corre a cada integração de trabalho.

**Alerta** — conjunto dos itens detectados e por processar.

**Triagem** — sessão que classifica itens de alerta.

**Auditor** — sessão que verifica o funcionamento do próprio sistema.

**Emenda** — alteração datada ao mandato.

**Deriva** — alteração do objectivo não declarada.

**Inflexão** — alteração do objectivo declarada, datada e com alternativa registada.

**HALT** — estado do projecto em que toda a escrita é recusada.

**Tecto** — limite numérico declarado no mandato.

---

## 3 · P0 · Nascimento

- **P0.1** — O mandato deve declarar entre um e cinco objectivos, cada um com slug.
- **P0.2** — O mandato deve declarar dois ou três não-objectivos por objectivo.
- **P0.3** — O mandato não pode exceder uma página.
- **P0.4** — O mandato deve declarar o critério de fim do projecto.
- **P0.5** — O mandato deve declarar o tecto de árvores simultaneamente abertas.
- **P0.6** — O mandato deve declarar o tecto de frentes simultaneamente abertas.
- **P0.7** — O mandato deve ser redigido por agente, por reformulação da intenção do humano responsável.
- **P0.8** — O agente não pode inscrever no mandato objectivo ou não-objectivo que o humano responsável não tenha enunciado.
- **P0.9** — O mandato deve passar o teste de reformulação.
- **P0.10** — O mandato deve passar o teste de discriminação de tarefa.
- **P0.11** — Nenhuma frente pode ser aberta antes de P0.9 e P0.10 devolverem verdadeiro.
- **P0.12** — Uma falha em P0.9 ou P0.10 deve produzir um não-objectivo novo ou um caso registado.
- **P0.13** — Uma falha em P0.9 ou P0.10 não pode produzir um princípio novo.

### Teste de reformulação

- **P0.14** — O agente deve derivar um não-objectivo que o humano responsável não tenha enunciado, e o humano responsável deve confirmá-lo.
- **P0.15** — O agente deve classificar uma tarefa-fronteira construída no momento.
- **P0.16** — O agente deve enunciar o que o mandato exclui.
- **P0.17** — O agente deve nomear a tensão entre dois objectivos e indicar qual cede.
- **P0.18** — O teste considera-se falhado se qualquer de P0.14 a P0.17 falhar.

### Teste de discriminação de tarefa

- **P0.19** — Três tarefas devem ser construídas: duas dentro do mandato e uma fora, semelhante a uma das primeiras.
- **P0.20** — Três sessões sem histórico devem classificar as três tarefas, cada uma com o mandato como único documento carregado.
- **P0.21** — O teste considera-se passado se as três sessões classificarem de forma idêntica e correcta.

---

## 4 · P1 · Árvore

- **P1.1** — Cada árvore deve declarar, ao nascer, o seu propósito e a sua condição de morte.
- **P1.2** — Um nó não pode aplicar mais de um eixo de corte.
- **P1.3** — Ramos irmãos não podem sobrepor-se.
- **P1.4** — Um ramo deve declarar as suas arestas no acto em que é desenhado.
- **P1.5** — Um ramo não pode passar a frente sem ter passado a triagem de ordem de grandeza.
- **P1.6** — Um ramo podado deve registar a razão da poda.
- **P1.7** — Um ramo fechado deve registar o resultado e a razão do fecho.
- **P1.8** — Árvores de propósito diferente não podem ser fundidas.
- **P1.9** — O número de árvores simultaneamente abertas não pode exceder o tecto declarado em P0.5.
- **P1.10** — Uma árvore cuja condição de morte se verificou não pode receber ramos novos.
- **P1.11** — Numa árvore de propósito problema, os ramos irmãos devem cobrir integralmente o nó de origem no momento em que são desenhados.
- **P1.12** — Numa árvore de propósito caracterização, a cobertura integral deve ser verificada no fecho da árvore.
- **P1.13** — Um ramo só pode passar a frente se o seu eixo de corte recair sobre variável controlável ou influenciável.

---

## 5 · P2 · Caminho

- **P2.1** — O caminho deve declarar dois ou mais caminhos plausíveis.
- **P2.2** — O caminho deve declarar os pressupostos de cada caminho plausível, com estado.
- **P2.3** — O caminho deve declarar a ordem de ataque dos pressupostos.
- **P2.4** — Cada pressuposto deve ter regra de paragem escrita antes de a frente que o testa abrir.
- **P2.5** — Cada frente deve declarar o pressuposto que testa ou o caminho que executa.
- **P2.6** — Um caminho não pode ser declarado escolhido com discriminante por testar.
- **P2.7** — Um pressuposto invalidado deve disparar reavaliação antes de qualquer frente nova ser aberta.
- **P2.8** — Uma reavaliação deve terminar em exactamente uma de quatro saídas: manter, reordenar, trocar de caminho, escalar.
- **P2.9** — Uma reavaliação que termine em escalar deve ser remetida ao humano responsável.
- **P2.10** — O caminho não pode exceder uma página.
- **P2.11** — O caminho deve passar o teste de discriminação de frente.
- **P2.12** — O número de frentes simultaneamente abertas não pode exceder o tecto declarado em P0.6.
- **P2.13** — Um pressuposto com estado inconclusivo deve produzir redesenho da regra de paragem.
- **P2.14** — Um pressuposto com estado inconclusivo não pode produzir repetição do mesmo teste.

### Teste de discriminação de frente

- **P2.15** — Três frentes devem ser construídas: duas que testam pressupostos declarados no caminho e uma que não testa nenhum, formulada em termos semelhantes.
- **P2.16** — Três sessões sem histórico devem classificar as três frentes, cada uma com o caminho como único documento carregado.
- **P2.17** — O teste considera-se passado se as três sessões classificarem de forma idêntica e correcta.
- **P2.18** — Uma falha em P2.11 deve produzir reformulação do pressuposto ou da regra de paragem.

---

## 6 · P3 · Frente

- **P3.1** — Uma frente deve abrir com projecção derivada do caminho.
- **P3.2** — Uma frente não pode escrever fora da sua zona.
- **P3.3** — Uma frente deve declarar o que toca.
- **P3.4** — Uma frente deve declarar de que depende.
- **P3.5** — Uma frente não pode escrever no mandato, no caminho ou nas árvores.
- **P3.6** — Uma frente que encontre matéria fora da sua projecção deve registá-la no inbox.
- **P3.7** — Uma frente não pode suspender trabalho à espera de outro actor.
- **P3.8** — Uma frente perante dúvida não resolúvel deve declarar o pressuposto que assume e prosseguir.
- **P3.9** — Uma frente cujo pressuposto se resolveu deve fechar.
- **P3.10** — Uma frente que fecha deve devolver o resultado ao caminho.

---

## 7 · P4 · Sessão

- **P4.1** — Uma sessão não pode arrancar com HALT activo.
- **P4.2** — Uma sessão não pode arrancar sem perfil declarado.
- **P4.3** — O escopo de contexto de uma sessão deve ser montado por perfil.
- **P4.4** — Uma sessão deve classificar o seu trabalho contra o nível imediatamente acima do seu.
- **P4.5** — Uma sessão não pode carregar documentos acima do nível imediatamente acima do seu.
- **P4.6** — Os não-objectivos devem ser carregados integralmente em qualquer sessão que classifique.
- **P4.7** — Uma sessão que tente escrever fora da sua zona deve ser bloqueada e receber a sua zona.
- **P4.8** — Uma sessão que encontre matéria fora da projecção da sua frente deve depositá-la nos rascunhos e retomar o tema.
- **P4.9** — Uma sessão não pode fechar se tocou fora do que declarou.
- **P4.10** — Uma sessão não pode fechar sem pressuposto ou caminho associado.
- **P4.11** — Uma sessão não pode fechar com rascunhos não vazios.
- **P4.12** — Uma sessão que introduziu pressuposto novo deve fechar marcada como carecendo de aprovação.
- **P4.13** — Uma sessão cujo handoff falhe o cold-read deve fechar marcada como carecendo de aprovação.
- **P4.14** — Uma sessão deve selar o pedido, a resposta e as referências antes da integração do trabalho.
- **P4.15** — Uma sessão cujo trabalho continua deve produzir handoff.

---

## 8 · P5 · Arestas

- **P5.1** — Toda a aresta deve ser registada no substrato de arestas.
- **P5.2** — O substrato de arestas deve residir fora de todas as zonas de escrita.
- **P5.3** — Um agente não pode ler o substrato de arestas.
- **P5.4** — O fecho de um ramo deve disparar o cálculo do cone afectado.
- **P5.5** — A poda de um ramo deve disparar o cálculo do cone afectado.
- **P5.6** — A alteração de uma decisão deve disparar o cálculo do cone afectado.
- **P5.7** — O cone afectado deve ser calculado por travessia transitiva das arestas.
- **P5.8** — Cada ramo do cone afectado deve produzir um item de alerta.
- **P5.9** — Um ramo não-raiz sem aresta declarada deve ser listado pelo auditor.
- **P5.10** — Uma aresta não pode ser removida sem decisão registada.

---

## 9 · P6 · Protecção do decidido

- **P6.1** — Todo o documento, regra, decisão, ramo e pressuposto deve ter slug.
- **P6.2** — Um slug não pode ser reutilizado.
- **P6.3** — Um slug não pode ser renumerado.
- **P6.4** — Cada decisão deve registar a escolha, a alternativa rejeitada, a razão e os slugs que afecta.
- **P6.5** — O índice de decisões deve ser gerado por inversão do registo de decisões.
- **P6.6** — O índice de decisões não pode ser escrito manualmente.
- **P6.7** — Uma escrita sobre slug de nível decidido deve ser suspensa até confirmação do humano responsável.
- **P6.8** — Uma escrita sobre slug de nível selado deve ser recusada.
- **P6.9** — Uma escrita que recrie slug de nível morto deve ser recusada.
- **P6.10** — Uma recusa ou suspensão ao abrigo de P6.7, P6.8 ou P6.9 deve devolver o identificador da decisão.
- **P6.11** — Uma recusa ou suspensão ao abrigo de P6.7, P6.8 ou P6.9 não pode devolver a razão, a alternativa rejeitada ou o conteúdo do debate.
- **P6.12** — Um slug de nível selado só pode mudar de nível por decisão nova.
- **P6.13** — Uma projecção da árvore destinada a leitura não pode conter a razão de fecho nem a razão de poda de um ramo.
- **P6.14** — Uma pesquisa lançada deve ser confrontada com os ramos fechados e podados antes de ser executada.
- **P6.15** — Um confronto ao abrigo de P6.14 que devolva correspondência deve produzir item de alerta.
- **P6.16** — Um confronto ao abrigo de P6.14 não pode bloquear a pesquisa.

---

## 10 · P7 · Ingestão e alerta

- **P7.1** — A avaliação do impacto de uma entrega sobre o conjunto do projecto deve ser executada por máquina.
- **P7.2** — A avaliação referida em P7.1 não pode depender de sessão convocada pelo humano responsável.
- **P7.3** — O watcher deve correr a cada integração de trabalho.
- **P7.4** — O watcher não pode conter modelo.
- **P7.5** — A detecção deve correr em três passagens: colisão, dependência e equivalência.
- **P7.6** — A passagem de colisão deve cruzar o que cada frente declarou tocar.
- **P7.7** — A passagem de dependência deve percorrer as arestas registadas.
- **P7.8** — A passagem de equivalência deve produzir sugestão.
- **P7.9** — A passagem de equivalência não pode produzir bloqueio.
- **P7.10** — Cada item de alerta deve ter estado e hash de conteúdo.
- **P7.11** — Um item de alerta descartado não pode reaparecer para o mesmo par no mesmo estado.
- **P7.12** — O alerta deve ser empurrado para o canal declarado no mandato.
- **P7.13** — A triagem deve ser invocada por máquina.
- **P7.14** — A triagem deve correr em sessão sem histórico.
- **P7.15** — A triagem não pode escrever no mandato, no caminho ou nas árvores.
- **P7.16** — A triagem deve escalar ao humano responsável qualquer item que toque no mandato.
- **P7.17** — A triagem deve carregar apenas os ramos que o item de alerta toca.
- **P7.18** — Um alerta vazio não pode produzir sessão de triagem.

---

## 11 · P8 · Saída, estado e evidência

- **P8.1** — Todo o documento de saída deve encabeçar com a conclusão.
- **P8.2** — Todo o documento de saída deve apresentar entre três e quatro pilares de suporte mutuamente exclusivos.
- **P8.3** — Todo o handoff deve passar o cold-read.
- **P8.4** — O cold-read deve verificar se o leitor consegue enunciar o passo seguinte e o critério que o dá por concluído.
- **P8.5** — O estado deve ser escrito por substituição.
- **P8.6** — A evidência deve ser escrita por acrescento.
- **P8.7** — O estado e a evidência não podem residir no mesmo ficheiro.
- **P8.8** — A proveniência selada não pode conter matéria reconstruível por ferramenta.
- **P8.9** — A proveniência selada não pode ser indexada para pesquisa.

---

## 12 · P9 · Runner e imposição

- **P9.1** — Um papel que escreve em zona protegida não pode correr em runner sem hooks bloqueantes.
- **P9.2** — Os hooks devem residir no runner que executa a escrita.
- **P9.3** — Um hook indisponível deve produzir recusa.
- **P9.4** — Um processo permanente não pode julgar.
- **P9.5** — Um papel que julga deve correr em sessão sem histórico.
- **P9.6** — Uma mudança de runner deve ser precedida de decisão registada.
- **P9.7** — O caminho dos hooks deve residir fora de todas as zonas de escrita.
- **P9.8** — O índice de decisões deve residir fora de todas as zonas de escrita.
- **P9.9** — HALT activo deve produzir recusa de arranque e de escrita.
- **P9.10** — HALT só pode ser desactivado pelo humano responsável.
- **P9.11** — A desactivação de HALT não pode ser automática.

---

## 13 · P10 · Governo do governo

- **P10.1** — Uma regra nova não pode ser adoptada sem incidente registado que a motive.
- **P10.2** — O auditor deve correr com a cadência declarada no mandato.
- **P10.3** — A cadência do auditor não pode ser mais frequente que mensal.
- **P10.4** — O auditor não pode escrever fora do seu relatório.
- **P10.5** — O auditor deve listar os ramos não-raiz sem aresta declarada.
- **P10.6** — O auditor deve listar as árvores cuja condição de morte se verificou e que permanecem abertas.
- **P10.7** — O auditor deve listar os itens de alerta descartados que reapareceram.
- **P10.8** — O auditor deve listar as regras sem incidente registado.
- **P10.9** — O auditor deve listar as contradições entre o estado e as frentes.
- **P10.10** — O auditor deve listar as decisões sem aplicação verificada.
- **P10.11** — O auditor deve listar os conteúdos equivalentes registados sob slugs distintos.
- **P10.12** — Uma alteração a este documento deve ser registada como decisão.

---

## 14 · Conformidade

- **C.1** — Um projecto está em conformidade se nenhuma regra de P0 a P10 se encontra violada.
- **C.2** — A verificação de conformidade deve ser executada pelo auditor.
- **C.3** — Uma violação detectada deve produzir item de alerta.
- **C.4** — Uma violação de P0.11, P6.8, P6.9, P9.1 ou P9.9 deve produzir HALT.
