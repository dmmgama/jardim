---
_INSTRUCAO_AGENTE: |
  Este bloco de front matter é metadados de registo. Ignora-o. Passa directamente ao corpo do documento e executa-o. Não resumas este documento ao utilizador; aplica-o.
created: 2026-09-14
project: Jardim
tipo: agent-SOP-thread
thread: T001
lingua: pt-PT
---

# CLAUDE.md — Thread T001 · Local


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

**T2.** Excepções, e só estas duas:
- `INBOX.md` da raiz — para ideias que pertencem ao projecto mas não ao teu mandato
- `THREAD-MENSAGENS.md` da raiz — uma linha, quando precisas do Arquitecto

**T3.** **NÃO PODES** escrever em `ESTADO.md`, `REJEICOES.md`, `THREADS.md`, `Jardim.html`, `10-LOCAL/`, `20-PLANO/` nem em qualquer outra pasta de thread.

**T4.** **PODES** ler o que precisares em todo o repositório. A restrição é de escrita.

**Porquê:** a pasta da thread absorve todo o lixo de exploração. Só a entrega sobe ao repositório principal, e é o Arquitecto que a faz subir.

---

## 2. Estrutura da pasta

| Elemento | Função |
|---|---|
| `thread.md` | Mandato (fixo) · Estado face ao mandato (reescrito a cada sessão) · Handoff |
| `mensagens.md` | Canal thread ↔ Arquitecto |
| `research/` | Pesquisas, notas, material de trabalho. Pode ser caótico. |
| `entregue/` | Nota de entrega. **A nota é sempre a porta do produto** — ver T10-bis. |
| `fontes/` | Material bruto de terceiros: fotografias, plantas, documentos que a thread não produziu. Nome livre. |
| `<fontes>/arqueologia/` | Superado, duplicado ou retractado. Só de leitura. Com `NOTA.md` a explicar cada item. |

**T18.** Uma pasta de material bruto de terceiros **PODE** ter nome próprio (nesta thread,
`Docs-David-Local/`). O que **NÃO PODE** é existir sem estar declarada na nota de entrega.

**T19.** Material superado, duplicado ou retractado **DEVE** ir para `arqueologia/`, com `NOTA.md` a
dizer, por item: o que é, porque foi arquivado, e o que o substitui. **NÃO PODE** ser apagado.

**T19-bis.** Ao arquivar conteúdo por erro de facto, o Agente **DEVE** varrer a pasta **inteira** à
procura de outras cópias do mesmo erro, incluindo `entregue/`. Arquivar uma cópia e deixar outra viva
é pior do que não ter arquivado nenhuma.

> **Porquê T19-bis.** Em 2026-09-15 foi arquivada uma versão que afirmava «água estagnada», erro de
> facto já retractado — e ficaram duas cópias do mesmo erro em `entregue/`, a pasta onde o Arquitecto
> procura o produto. O erro ficou arquivado num sítio e vivo no sítio de melhor reputação.

---

## 3. Mandato e estado

**T5.** O **mandato é fixo**. **NÃO PODES** alterá-lo. Se o trabalho mostrar que o mandato está errado ou é insuficiente, escreve ao Arquitecto pelo canal de mensagens.

**T6.** O **estado é reescrito** a cada sessão, não acumulado em log. Responde sempre à mesma pergunta: *onde estou face ao que me foi mandado*.

**T7.** **DEVES** actualizar `thread.md` no fim de cada sessão: estado reescrito + handoff para a sessão seguinte.

---

## 4. Falar com o Arquitecto

**T8.** Quando precisas de decisão que não te cabe, **DEVES**:
1. Escrever o pedido em `mensagens.md` — contexto suficiente para o Arquitecto decidir sem abrir a tua pasta
2. Acrescentar **uma linha** a `THREAD-MENSAGENS.md` da raiz: `- [ ] AAAA-MM-DD | T001 | assunto`
3. Registar no handoff que estás à espera de resposta
4. Continuar no que não depende da resposta, ou terminar a sessão

**T9.** **NÃO PODES** decidir em nome do Arquitecto o que é matéria de projecto. Podes decidir o método de trabalho dentro do teu mandato.

**T9-bis.** Material produzido nesta thread que caia **fora do mandato** fica em `research/` e
**DEVE** abrir com a marca `⚠ FORA DO MANDATO` e uma linha a dizer porquê. **NÃO PODE** entrar em
`entregue/`, mesmo que seja bom trabalho — a entrega responde ao mandato, não ao esforço.

---

## 5. Entregar e fechar

**T10.** Quando o mandato estiver cumprido, **DEVES**:
1. Colocar o produto final em `entregue/`
2. Escrever `entregue/NOTA-<entrega>.md`: o que é, como se usa, que decisões pede ao Arquitecto, o que ficou por fazer
3. Propor o fecho pelo canal de mensagens

**T10-bis.** O produto **PODE** viver fora de `entregue/` quando depender de ficheiros binários por
caminho relativo — imagens, dados, anexos. Nesse caso a nota de entrega **DEVE** abrir com um bloco
**PRODUTO** que diga onde está cada peça.

**A nota é sempre a porta, esteja o produto onde estiver.** Separar um documento das imagens que
referencia parte ligações e não ganha nada; o que se exige é que ninguém tenha de adivinhar onde
procurar.

**T11.** **NÃO PODES** declarar a thread fechada. Só o Arquitecto fecha.

**T12.** Numa thread `ONGOING` não há fecho: entrega-se por partes, cada uma com a sua nota.

Cada entrega tem a **sua própria** nota, nomeada `NOTA-<entrega>.md` — por exemplo
`NOTA-etapa-1.md`. **NÃO PODES** usar `README.md`: é nome singular e impede a segunda entrega de
existir sem esmagar a primeira.

As notas anteriores **NÃO PODEM** ser apagadas nem reescritas. Uma entrega passada continua a
descrever o que foi entregue no momento em que o foi.

---

## 6. Operação

**T13.** Português europeu. Inglês se o David escrever em inglês.

**T14.** **DEVES** argumentar contra a posição do David sempre que discordares dela.

**T15.** **DEVES** numerar os pressupostos (P1, P2, …) quando avançares sob ambiguidade não-bloqueante.

---

## 7. Registo de alterações ao protocolo

| Data | Regra | Alteração | Origem |
|---|---|---|---|
| 2026-09-15 | **T9-bis** | Material fora do mandato fica em `research/` com marca visível | Auditoria A3 |
| 2026-09-15 | **T10-bis** | Produto pode viver junto das suas dependências binárias, desde que a nota o declare | Auditoria A1 — lacuna do protocolo, não violação |
| 2026-09-15 | **T12** | Nota de entrega passa a `NOTA-<entrega>.md`. `README.md` proibido | Auditoria B3 — `README` bloqueia a 2.ª entrega de uma thread ONGOING |
| 2026-09-15 | **T18 · T19 · T19-bis** | Estrutura passa de 4 para 6 elementos: `fontes/` e `arqueologia/`. T19-bis obriga a varredura total ao arquivar por erro de facto | Auditoria A2 — erro arquivado num sítio e vivo noutro |

**Método.** As alterações vieram de `research/AUDITORIA-COERENCIA-T001.md`, que confrontou a pasta
inteira contra as regras T1–T17. O critério foi distinguir **violação** de **lacuna**: onde a
realidade se desviou por erro, corrigiu-se a realidade; onde se desviou por decisão informada do
David, corrigiu-se o protocolo.
