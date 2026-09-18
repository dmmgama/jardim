---
created: 2026-09-18
project: Jardim
tipo: governo
branch: Governo-correcao-v1
summary: |
  Índice dos temas de trabalho em modo Arquitecto, com o protocolo de arranque e o último handoff de cada um.
---

# Índice — Handoffs do Arquitecto

**Como funciona.** Um **Tema** é um assunto que se trabalha em modo Arquitecto e a que se dá nome. Cada tema tem:

- um **protocolo de arranque** — `TEMA-Protocolo-arranque.md` — que diz que ficheiros ler antes de trabalhar nesse tema;
- um **handoff por sessão** — `YYYY-MM-DD-ARQ-HANDOFF-TEMA-Sn.md` — onde `Sn` é o número da sessão nesse tema.

**Arranque.** Quando o David diz «Arranque Arquiteto», a sessão lê este índice, lista os temas e pergunta qual. Quando diz «Arranque TEMA», vai directo. Em ambos os casos lê **primeiro o protocolo de arranque do tema, depois o último handoff**.

**Fecho.** Toda a sessão escreve o handoff do seu tema (front matter com `branch` obrigatório), actualiza esta tabela, e **commita sem excepção**.

| Tema | Protocolo de arranque | Último handoff | Sessões | Branch do último |
|---|---|---|---|---|
| **GERAL** | `GERAL-Protocolo-arranque.md` | `2026-09-17-ARQ-HANDOFF-GERAL-S1.md` | 1 | `master` |
| **GOVERNO** | `GOVERNO-Protocolo-arranque.md` | `2026-09-18-ARQ-HANDOFF-GOVERNO-S1.md` | 1 | `Governo-correcao-v1` |
| **REGISTOS-ARQUITETO** | `REGISTOS-ARQUITETO-Protocolo-arranque.md` | — | 0 | — |

**Nota sobre o GERAL S1:** é o antigo `HANDOFF.md` da raiz, movido sem reescrita a 2026-09-18. Está desactualizado face às sessões T005 de 2026-09-17/18 — ler com essa reserva.
