---
created: 2026-09-19 21:50
chat: Arquitectura de governo de projectos com agentes
summary: >
  Proposta de arquitectura apresentada na estrutura do fluxo existente (Governo §1-§6,
  Projecto §2-§6), com as alterações marcadas A1 a A18 para comparação directa.
---

# Arquitectura proposta

Apresentada na estrutura do fluxo existente, secção a secção, para comparação directa.

**Convenção de leitura**

- Texto sem marca — mantém-se como está.
- `[A_n]` — alteração proposta. A justificação de cada uma está no relatório, com o mesmo número.
- `[=]` — peça que examinei e decidi manter sem alteração.

**Contagem:** 18 alterações. 14 peças mantidas explicitamente.

---

# Parte I · Governo

## §1 · A raiz e os três modos

A raiz roteia: Governo, Arquitecto ou Threads. Cada modo tem o seu governo local, que substitui o da raiz.

**`[A1]` A raiz passa a carregar o mandato.** Hoje a raiz declara que não sabe o que é o projecto. Passa a ter uma linha: o ponteiro para `MANDATO.md`. Continua a não saber o conteúdo — carrega o ficheiro, não o conhecimento.

**`[A2]` Acrescenta-se um quarto ponto de entrada, não-interactivo: o Watcher.** Não é modo nem sessão — é um processo sem modelo, disparado por cada commit, que escreve em `ALERTA.md` e não fala com ninguém.

`[=]` Os três modos mantêm-se. `[=]` O governo local a substituir o da raiz mantém-se — é isolamento por construção.

## §2 · Entrada numa sessão

Roteamento → Enquadramento → escolha de modo ou vista geral → mandato → entra no modo.

**`[A3]` O Enquadramento passa a ser montagem de contexto por perfil.** Deixa de ser leitura de protocolos pela sessão e passa a ser contexto montado à entrada, cortado pelo perfil: cada nível recebe o nível imediatamente acima, não o topo. Uma thread recebe a sua projecção; não recebe o mandato do projecto. Os não-objectivos são a excepção e vão sempre inteiros.

**`[A4]` O mandato da sessão deixa de ter três origens e passa a ter uma.** Hoje vem de handoff, inbox ou prompt. Passa a vir sempre da mesma fonte — derivado do `CAMINHO.md` — e as três origens anteriores passam a ser apenas o **gatilho** que o invoca, não a sua fonte.

`[=]` A vista geral (`TEMAS.md`) mantém-se, como resposta à pergunta "o que temos".

## §3 · Ciclo da sessão

### §3a · Abertura

Copiar template → `Registo-Sessao.md` com prompt e bloco Propósito/Resultado/Estado → se vem de handoff, apresentar mandato, critério de sucesso, plano e dúvidas → confirmação → segue.

**`[A5]` O critério de sucesso passa a ter de ser verificável sem julgamento.** Se o campo "resultado mínimo" não puder ser avaliado por comparação objectiva no fecho, a sessão não arranca. É o mesmo padrão que já aplicas na `Vista-Geral` — "serve para · feito quando".

`[=]` `Registos-david.md`, com citação literal, mantém-se. É proveniência do pedido e não tem substituto.
`[=]` A apresentação do mandato antes de começar mantém-se.
`[=]` A correcção a meio ir para `Registos-david.md` com o novo plano no `Registo-Sessao.md` mantém-se.

### §3b · Durante

Governam a sessão o `CLAUDE.md` do modo, os Protocolos e o Mandato-do-Modo. Decisões à medida em `Decisoes.md`; outputs pelo protocolo de registo; ideias de outras áreas no `INBOX`. Travões: `Rascunhos.md`, `Arvore.md`, âncora.

**`[A6]` Dúvida não bloqueia: declara-se pressuposto e continua.** Hoje as dúvidas concentram-se na abertura. Durante a sessão, perante decisão que não tem, a sessão regista o pressuposto assumido com grau de confiança e prossegue. Não existe estado de espera.

**`[A7]` A sessão mantém um `estado.json` com campos fechados.** Substitui prosa por estrutura: o que serve, o que **toca**, de que **depende**, que pressupostos assumiu. É o que torna possível qualquer detecção automática.

`[=]` `Decisoes.md`, `INBOX`, `Arvore.md` e a âncora mantêm-se.
`[=]` O protocolo de registo de outputs mantém-se.

### §3c · Fecho

Resumir o feito → acordo → registo final com decisões, anti-decisões e abertos → apagar lixo → handoff por tema → commit → texto de arranque.

**`[A8]` O acordo deixa de ser condição única de fecho e passa a ter dois níveis.** Divergência dura — o que a sessão tocou saiu do que declarou, ou o que produziu não serve nada — bloqueia o fecho. Divergência branda — pressuposto novo, handoff fraco — fecha com marca `carece_aprovacao` e sobe ao alerta. A sessão nunca fica refém da tua disponibilidade.

**`[A9]` Verificação de aplicação antes do commit.** Nenhuma decisão registada pode sobreviver ao fecho sem item de aplicação correspondente ou linha de rejeição.

**`[A10]` O handoff passa a ser JSON com campos obrigatórios e é validado por leitura a frio.** Um agente sem histórico lê só o handoff e tem de conseguir enunciar o próximo passo e o critério que o dá por feito. Se não consegue, a sessão não fecha.

**`[A11]` "Apagar lixo" é substituído por quota à entrada.** Em vez de escrever tudo e limpar no fim, a sessão promove no máximo dois itens, e zero é resultado legítimo e frequente.

`[=]` O commit e o texto de arranque no chat mantêm-se.
`[=]` O handoff por tema, com actualização de `TEMA.md` e `TEMAS.md`, mantém-se.

## §4 · Rascunhos

Questão fundamental fora do tema → sinalizar tensão → o David autoriza → escrita rápida → continua sem derivar. Só se lê em dois casos: o David sugere, ou ao registar decisão irreversível. No fecho, acaba em branco.

`[=]` **Mantém-se inteiro, sem uma única alteração.** É a peça mais bem desenhada do sistema existente: um registo cuja função é não ser lido, e que já trata o caso da decisão irreversível — que é precisamente o que um projecto físico exige e que nenhum mecanismo automático dá.

## §5 · Modos e temas

Index-Modos: Geral (activo) e Auditor (por definir). Três temas do Geral: Meta-Governo, Governo-do-Projeto, Auditoria. `TEMAS.md` como quadro.

**`[A12]` O modo Auditor fica definido.** Disparo por cadência fixa, nunca por evento. Leitura total, escrita apenas no relatório. Verifica: sondas de fronteira do mandato, contradições entre estado e threads, alertas descartados que voltaram, ramos abertos sem dependências declaradas, decisões sem aplicação, e regras do governo sem incidente que as justifique. Sucesso continua a ser duas páginas lidas a frio.

**`[A13]` O tema Meta-Governo ganha uma regra de admissão.** Nenhuma regra nova de governo entra sem um modo de falha observado que a justifique. É o único travão ao crescimento do próprio governo, e o Auditor verifica-o.

`[=]` Os três temas mantêm-se. `[=]` `TEMAS.md` mantém-se.

## §6 · Estrutura de pastas

**`[A14]` Sete ficheiros novos na raiz do governo.**

| Ficheiro | O que é |
|---|---|
| `MANDATO.md` | objectivos, não-objectivos, critério de fim. Uma página |
| `CAMINHO.md` | pressupostos por testar, ordem de ataque, regras de paragem |
| `arvores/` | partições do espaço, uma por propósito |
| `CASOS.md` | casos-fronteira decididos |
| `ALERTA.md` | o que o watcher detectou |
| `debates/*.json` | decisões com alternativa rejeitada e slugs afectados |
| `indice-decisoes.json` | slug → decisão. **Gerado**, nunca escrito |

`[=]` Toda a estrutura existente se mantém.

---

# Parte II · Projecto

## §2 · Arranque: Arquitecto ou Thread

Via Arquitecto: lê `ESTADO`, `THREADS`, `MENSAGENS` por ordem, reporta e debate. Via Thread: escolhe em `THREADS.md`, o `CLAUDE.md` local passa a governar, lê e trabalha.

**`[A15]` A thread lê uma projecção derivada, não um mandato redigido.** O `thread.md` deixa de ser escrito à mão e passa a ser gerado do `CAMINHO.md`: objectivo é o pressuposto mais a regra de paragem; fronteiras negativas são os pressupostos atribuídos às outras threads.

`[=]` A bifurcação Arquitecto/Thread mantém-se. `[=]` A ordem de leitura mantém-se. `[=]` O governo local a substituir o da raiz mantém-se.

## §3 · Ciclo de decisão

`INBOX` → Arquitecto consulta `ESTADO` e `REJEICOES` → descarta com porquê, decide já, ou abre thread → `ESTADO.md` → `Jardim.html` → Notion.

**`[A16]` O Arquitecto passa a ter dois modos, com disparos diferentes.** *Triagem*: disparada por alerta, sessão fria e curta, escreve no estado. *Rumo*: aberta só por ti, produz emenda ao mandato **ou nada**, e nunca escreve no estado. Se o mesmo modo fizesse as duas coisas, cada alerta reabriria a discussão de rumo.

**`[A17]` Os itens do `INBOX` passam a ter schema obrigatório:** `serves`, `effect` (confirma, estende, contraria, órfão), `toca`, `depende_de`. Sem os campos, o item não é aceite.

`[=]` As três saídas — descartar com porquê, decidir já, abrir thread — mantêm-se.
`[=]` `REJEICOES.md` com o porquê mantém-se.
`[=]` "Nenhuma decisão existe fora do `ESTADO.md`" mantém-se.
`[=]` A publicação em Notion mantém-se.

## §4 · Comunicação thread ↔ arquitecto

A thread pede em `mensagens.md`, sinaliza uma linha na raiz, regista que espera e **termina**. O Arquitecto vê o sinal ao arrancar, responde, marca `[RESPONDIDO]`. A sessão seguinte da thread lê e destrava.

**`[A18]` Este canal é eliminado.** A thread nunca espera: declara o pressuposto que assumiu, prossegue e regista a questão no `INBOX`. O Arquitecto processa em lote. Desaparecem `mensagens.md`, `THREAD-MENSAGENS.md`, o estado "à espera de resposta" e o ciclo de três sessões para uma pergunta.

É a alteração de maior impacto e a de maior risco. A justificação e o custo estão no relatório.

## §5 · Anatomia de uma thread

`CLAUDE.md` governa localmente; `thread.md` com mandato, estado e handoff; `mensagens.md` como canal; `research/` que pode ser caótico; `entregue/` com produto e `NOTA.md` — só isto sobe.

**`[A15]`** `thread.md` derivado, como acima. **`[A18]`** `mensagens.md` sai. Acrescentam-se `estado.json` e `handoff.json`.

`[=]` **`research/` e `entregue/` mantêm-se exactamente como estão.** A separação entre exploração livre e entrega destilada, com `NOTA.md`, é a segunda peça mais bem desenhada do sistema — dá lugar próprio ao caos, que é o que impede a exploração de contaminar o estado.
`[=]` "Só a entrega sobe" mantém-se.

## §6 · As três camadas

`10-LOCAL` factual e sem versões ← `20-PLANO` onde se decide ← `90-ARQUEOLOGIA` que se consulta mas não obedece. `ESTADO.md` alimenta o plano.

`[=]` **As três camadas mantêm-se sem alteração.** A distinção entre o que é facto, o que está em decisão e o que é histórico consultável já resolve, no domínio do projecto, o mesmo problema que o mandato resolve no domínio do governo.

A única nota: o `20-PLANO` é onde o `CAMINHO.md` se encaixa — um plano de pressupostos por testar, em vez de um plano de entregáveis por produzir. Não é alteração de estrutura, é alteração de conteúdo, e está coberta por `[A14]`.

---

## Resumo

| | Governo | Projecto |
|---|---|---|
| Alterações | A1–A14 | A15–A18 |
| Peças mantidas | 9 | 5 |
| Secções sem alteração | §4 | §6 |

Duas peças ficam intactas por mérito, depois de examinadas: o `Rascunhos.md` e o par `research/` + `entregue/`. Uma alteração é eliminação pura: o canal síncrono entre thread e arquitecto.
