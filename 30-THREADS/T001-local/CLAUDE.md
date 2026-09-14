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
2. Acrescentar **uma linha** a `THREAD-MENSAGENS.md` da raiz: `- [ ] AAAA-MM-DD | T001 | assunto`
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
