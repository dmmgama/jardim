---
created: 2026-09-18
updated: 2026-09-18
branch: Governo-correcao-v1
tipo: readme
summary: |
  Como funciona o governo da repo e o seu fluxo. Os protocolos em Protocolos/ são os instrumentos aplicados ao fluxo.
---

# Governo — como funciona

Trabalho sobre a forma como o projecto se trabalha. Uma sessão de Governo trata **só** de governo da repo.

## O fluxo em cinco linhas

1. `CLAUDE.md` da raiz pergunta **GOVERNO ou PROJETO**. Governo → `Governo/CLAUDE.md`.
2. Lê `Protocolos/Governo-Enquadramento.md` (função, regra inegociável, âncora) e o índice de modos.
3. **Modo ou vista geral.** Vista geral = handoffs por tema + inboxes. Escolhe-se; entra-se no modo.
4. Sessão: template copiado, bloco Propósito/Resultado/Estado, Árvore, decisões, Rascunhos. Diagramas em `fluxo-governo.md`.
5. Fecho: registo final, lixo fora, Rascunhos em branco, handoff por tema, commit, texto de arranque.

## Pastas

| Pasta | Função |
|---|---|
| `Protocolos/` | Os instrumentos base, aplicados ao fluxo. Afináveis. Vivem **só aqui**, não nos modos. |
| `Raiz-Teste/` | Laboratório: constrói-se aqui o que vai para a raiz da repo antes de aplicar. |
| `Modos-Governo/` | Os modos. Servem **só para isolar trabalho**. Índice em `Index-Modos-Governo.md`. |
| `fluxo-governo.md` | Os diagramas do fluxo. Versão actual no front matter. |

## Modos de governo — explicação e funções

### Geral — activo
Trata de tudo o que é governo. Função de **vista geral**: o David fala com ele, ou vê handoffs e inboxes. Divide as
tarefas e arruma-as em temas. Quadro em `Geral/TEMAS.md`; cada tema é uma pasta em `Geral/Handoffs/<Tema>/` com
`TEMA.md` (mandato · estado · por fazer) e os handoffs. Temas iniciais:

| Tema | O que é |
|---|---|
| **Meta-Governo** | O próprio governo: modos, fluxos, protocolos. (Esta branch.) |
| **Governo-do-Projeto** | O regime do Arquitecto e das Threads. |
| **Auditoria** | O que se manda ao Auditor. |

### Auditor — por definir
Um mandato só: **ver se tudo está simples e coerente.** Sucesso: um agente a frio, sem conhecer a repo, reconstrói o
fluxo de governo pelos ficheiros e explica as peças em 2 folhas A4. Setup em `Data-Setup-Auditor`.
