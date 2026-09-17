---
created: 2026-09-14
project: Jardim
tipo: governo
summary: |
  Sinalizador global de pedidos das threads ao Arquitecto. Uma linha por pedido. A conversa vive no mensagens.md de cada thread.
---

# THREAD-MENSAGENS

> **Regra G14:** quando uma thread precisa de decisão, escreve o pedido em `30-THREADS/<thread>/mensagens.md` **e** acrescenta uma linha aqui.
> **Regra G15:** o Arquitecto responde no `mensagens.md` da thread e marca a linha aqui como `[RESPONDIDO]` com data.

**Porquê dois canais:** o Arquitecto não pode ter de abrir sete pastas para descobrir se alguém precisa dele. Lê uma linha aqui e sabe. A conversa fica onde pertence; o sinal fica onde é visto.

---

## Formato

```
- [ ] AAAA-MM-DD | T00X | assunto em uma linha
- [x] AAAA-MM-DD | T00X | assunto  → [RESPONDIDO AAAA-MM-DD]
```

`[ ]` = por responder. `[x]` = respondido.

**As linhas não se apagam.** Ficam como histórico; deixam apenas de pedir atenção.

---

## Pendentes

*(nenhum)*

---

## Respondidos

- [x] 2026-09-16 | T002 | Base de trabalho fixada (subir cota +0,50 m sobre betonilha) — pede 3 threads novas (impermeabilizacao, peso por zona, afinacao da cota), sinaliza acao n.1 (tracador no dreno) e 2 factos para a T001  → **[RESPONDIDO 2026-09-17]** Base absorvida em `ESTADO.md` §02/§04. **Questão de mandato resolvida:** a base do David substituiu a necessidade de leque de opções — a T002 fecha sem as 2–4 opções, e o Arquitecto ratifica o desvio. **Afinação da cota:** o âmbito de geometria foi absorvido pela T004; o resto fica pendente. **Impermeabilização e peso por zona: ainda por criar.** Acção n.º 1 e os 2 factos da T001 registados em `ESTADO.md` §05 e em `INBOX.md`.
- [x] 2026-09-17 | T002 | Entrega da thread + proposta de criação da T004 (geometria do jardim)  → **[RESPONDIDO 2026-09-17]** Entrega absorvida. **T002 FECHADA.** **T004 criada** por autorização expressa do David, mandato ratificado sem alterações. Ver `THREADS.md`.
- [x] 2026-09-15 | T001 | Etapa 1 entregue — absorver dossier, avaliar hipótese de rebaixamento do muro SW, levantar bloqueio da T002  → **[RESPONDIDO 2026-09-16]** Dossier declarado canónico onde está (não migra). Muro SW vai para debate na T002. Bloqueio da T002 levantado.
