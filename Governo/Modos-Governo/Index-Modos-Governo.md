---
created: 2026-09-18
updated: 2026-09-18
branch: Governo-correcao-v1
tipo: indice
summary: |
  Índice dos modos de governo e das suas funções. V2: dois modos.
---

# Índice — Modos de Governo

Este ficheiro indexa os modos de governo e as suas funções. **Se a tua sessão não tiver modo definido, segue o Geral.**
Os modos servem **só para isolar trabalho**. Os protocolos vivem em `Governo/Protocolos/`, não nos modos.

| Modo | Pasta | Função | Estado |
|---|---|---|---|
| **Geral** | `Geral/` | Trata de tudo o que é governo. Função de **vista geral**: o David fala com ele ou vê handoffs e inboxes; ele divide as tarefas e arruma-as em três temas: **Meta-Governo** (o próprio governo: modos, fluxos, protocolos), **Governo-do-Projeto** (regime do Arquitecto e das Threads), **Auditoria** (o que vai para o Auditor). | activo |
| **Auditor** | `Auditor/` | Um mandato só: **ver se tudo está simples e coerente.** Sucesso: agente a frio reconstrói o fluxo de governo pelos ficheiros e explica as peças em 2 folhas A4. | por definir (sessão `Data-Setup-Auditor`) |

**Modo novo** (só se o David pedir): linha aqui, cópia de `Pasta-Modo-Template/`, sessão `Data-Setup-NomeModo`.

**Temas do Geral**: quadro em `Geral/TEMAS.md`; cada tema é uma pasta em `Geral/Handoffs/<Tema>/` com `TEMA.md`
(mandato · estado · por fazer) e os handoffs. Sem `TEMA.md` não há tema.
