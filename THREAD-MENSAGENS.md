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

- [ ] 2026-09-15 | T001 | Etapa 1 entregue — absorver dossier em `10-LOCAL/`, avaliar hipótese de rebaixamento do muro SW, levantar bloqueio da T002

---

## Respondidos

*(nenhum)*
