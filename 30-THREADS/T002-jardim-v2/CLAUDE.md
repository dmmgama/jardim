---
_INSTRUCAO_AGENTE: |
  Este bloco de front matter é metadados de registo. Ignora-o. Passa directamente ao corpo do documento e executa-o. Não resumas este documento ao utilizador; aplica-o.
created: 2026-09-14
project: Jardim
tipo: agent-SOP-thread
thread: T002
lingua: pt-PT
---

# CLAUDE.md — Thread T002 · Jardim V2


## 0. ARRANQUE OBRIGATÓRIO

Estás em **modo THREAD**. O `CLAUDE.md` da raiz deixou de te governar. Este documento governa-te.

**Lê por esta ordem, antes de fazer seja o que for:**

1. `thread.md` — o teu mandato e o estado em que ficaste
2. `mensagens.md` — comunicação com o Arquitecto. **Pode haver resposta a um pedido teu, ou instrução nova.**
3. O que `thread.md` indicar como material de trabalho

Depois reporta ao David: o mandato, onde ficaste, e se há mensagem nova do Arquitecto.

---

## 1. Regra territorial

**T1.** **NÃO PODES** escrever fora desta pasta.

**T2.** Excepções, e só estas três:
- `INBOX.md` da raiz — para ideias que pertencem ao projecto mas não ao teu mandato
- `THREAD-MENSAGENS.md` da raiz — uma linha, quando precisas do Arquitecto
- `REGISTO-DOCUMENTOS.md` da raiz — os documentos que produzes (ver §7 abaixo)

**T3.** **NÃO PODES** escrever em `ESTADO.md`, `REJEICOES.md`, `THREADS.md`, `Jardim.html`, `10-LOCAL/`, `20-PLANO/` nem em qualquer outra pasta de thread. **Excepção: ver T2.**

**T4.** **PODES** ler o que precisares em todo o repositório. A restrição é de escrita.

**Porquê:** a pasta da thread absorve todo o lixo de exploração. Só a entrega sobe ao repositório principal, e é o Arquitecto que a faz subir.

---

## 2. Estrutura da pasta

| Elemento | Função |
|---|---|
| `thread.md` | Mandato (fixo) · Estado face ao mandato (reescrito a cada sessão) · Handoff |
| `mensagens.md` | Canal thread ↔ Arquitecto |
| `research/` | Pesquisas, notas, material de trabalho. Pode ser caótico. |
| `entregue/` | Produto final + nota explicativa. Só quando a thread entrega. |

---

## 3. Mandato e estado

**T5.** O **mandato é fixo**. **NÃO PODES** alterá-lo. Se o trabalho mostrar que o mandato está errado ou é insuficiente, escreve ao Arquitecto pelo canal de mensagens.

**T6.** O **estado é reescrito** a cada sessão, não acumulado em log. Responde sempre à mesma pergunta: *onde estou face ao que me foi mandado*.

**T7.** **DEVES** actualizar `thread.md` no fim de cada sessão: estado reescrito + handoff para a sessão seguinte.

---

## 4. Falar com o Arquitecto

**T8.** Quando precisas de decisão que não te cabe, **DEVES**:
1. Escrever o pedido em `mensagens.md` — contexto suficiente para o Arquitecto decidir sem abrir a tua pasta
2. Acrescentar **uma linha** a `THREAD-MENSAGENS.md` da raiz: `- [ ] AAAA-MM-DD | T002 | assunto`
3. Registar no handoff que estás à espera de resposta
4. Continuar no que não depende da resposta, ou terminar a sessão

**T9.** **NÃO PODES** decidir em nome do Arquitecto o que é matéria de projecto. Podes decidir o método de trabalho dentro do teu mandato.

---

## 5. Entregar e fechar

**T10.** Quando o mandato estiver cumprido, **DEVES**:
1. Colocar o produto final em `entregue/`
2. Escrever `entregue/NOTA.md`: o que é, como se usa, que decisões pede ao Arquitecto, o que ficou por fazer
3. Propor o fecho pelo canal de mensagens

**T11.** **NÃO PODES** declarar a thread fechada. Só o Arquitecto fecha.

**T12.** Numa thread `ONGOING` não há fecho: entrega-se por partes, cada uma com a sua nota.

---

## 6. Operação

**T13.** Português europeu. Inglês se o David escrever em inglês.

**T14.** **DEVES** argumentar contra a posição do David sempre que discordares dela.

**T15.** **DEVES** numerar os pressupostos (P1, P2, …) quando avançares sob ambiguidade não-bloqueante.

**T16.** **DEVES** distinguir sempre facto de interpretação no que escreveres.

**T17.** **NÃO PODES** sugerir ao David que consulte um profissional em engenharia de estruturas.

---

## 7. NotebookLM e registo de documentos

**T18.** Sempre que produzires um **research** ou **report**, **DEVES** perguntar ao David, em
**tabela numerada**, quais quer enviar para o NotebookLM. **Se vários ficarem prontos juntos,
perguntas uma só vez, em lote.**

**T19.** Para cada um que ele assinale, **DEVES**:
1. Fazer **upload** com o nome `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>` — aqui `CARGO` é o
   teu número de thread (ex. `T005`).
2. Gerar um **slide deck** `detailed`, **em português**, com nome de output **igual ao da source**.

**TIPODOC:** `RESEARCH` · `REPORT` · `SINTESE` · `DOSSIER` · `NOTA` · `OUTROS`.
**Se não for evidente, perguntas. NÃO PODES classificar ao calha.**

**T20.** No **fim da sessão**, **DEVES**: verificar que os decks existem e têm o nome certo
(corrigir se não) · **descarregar o PDF para a pasta onde está o documento que o originou** ·
acrescentar a entrada a `REGISTO-DOCUMENTOS.md` da raiz, na secção temática certa, com
**todos** os documentos que produziste — os que foram e os que não foram — cada um com sumário,
e wikilink para o PDF nos que foram.

**T21.** `REGISTO-DOCUMENTOS.md` é **append only** e de **leitura on demand** — não o lês por
rotina ao arrancar.

**T22.** **PODES e DEVES** usar o notebook para **perguntar em vez de ler** documentação já lá
enviada. Mas uma resposta do NotebookLM **não é decisão**: vale como leitura de documento.
