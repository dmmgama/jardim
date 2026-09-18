---
created: 2026-09-18
branch: Governo-correcao-v1
tipo: roteamento-governo
summary: |
  Entrada do modo Governo. Lê o enquadramento, pergunta modo ou vista geral, entra no modo e corre o fluxo.
---

# Governo — CLAUDE.md

1. Lê `Protocolos/Governo-Enquadramento.md`. É a tua função e a tua âncora.
2. Lê `Modos-Governo/Index-Modos-Governo.md`. Dois modos: **Geral** e **Auditor**.
3. Pergunta ao David, se ele ainda não disse:

```
Modo (Geral · Auditor) ou VISTA GERAL?
```

| Resposta | O que fazes |
|---|---|
| **Vista geral** | Lê `Modos-Governo/Geral/TEMAS.md` (o quadro: temas, estado, último handoff, por fazer) e as `INBOX.md`. Dizes ao David «temos isto e aquilo». Ele escolhe. Entras no modo dono. |
| **Modo** | Entras em `Modos-Governo/<Modo>/`. O mandato é o handoff que o David indicar, a inbox, ou o prompt. |

4. Abre a sessão: copia `Active-Session/Sessao-Template/` para `Active-Session/<id-da-sessão>/` e preenche
   `Registo-Sessao.md` (bloco Propósito · Resultado mínimo · Estado) e `Arvore.md` (objectivo na raiz).
5. Corre o fluxo de `fluxo-governo.md` §3. Protocolos aplicáveis em `Protocolos/`. Laboratório da raiz da repo em
   `Raiz-Teste/`.
6. Fecho: registo final · lixo apagado · Rascunhos em branco · handoff em `Handoffs/<Tema>/` se continua · **commit**
   · **texto de arranque da sessão seguinte, no chat, pronto a colar.**
