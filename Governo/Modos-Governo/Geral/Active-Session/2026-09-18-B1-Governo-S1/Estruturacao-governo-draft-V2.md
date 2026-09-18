---
branch: Governo-correcao-v1
data: 2026-09-18
modo: Geral
id_sessao: 2026-09-18-B1-Governo-S1
tipo: draft
versao: V2
supera: Estruturacao-governo-draft.md (V1)
summary: |
  Estruturação do governo, V2: os três níveis (repo, fluxo do Governo, átomo da sessão) num diagrama simples, e o
  que mudou desde o V1. Diagramas detalhados em Governo/fluxo-governo.md.
---

# Estruturação do governo — DRAFT V2

> V1 está em `Estruturacao-governo-draft.md`: como se pensou ao princípio da sessão. Este V2 é como ficou no fim.

## 0. Os três níveis

```
┌─ 1. A REPO ──────────────────────────────────────────────────────┐
│                                                                  │
│   CLAUDE.md raiz ── GOVERNO ou PROJETO?                          │
│         │                        │                               │
│      GOVERNO                  PROJETO                            │
│   (fluxo do Governo)     (CLAUDE-projeto.md:                     │
│         │                 Arquitecto · Threads · regime antigo)  │
└─────────┼────────────────────────┼───────────────────────────────┘
          │                        │
┌─ 2. FLUXO DO GOVERNO ────────────┼───────────────────────────────┐
│                                  │                               │
│   Governo/CLAUDE.md → Enquadramento → Modo ou VISTA GERAL?       │
│                                        │                         │
│                                   TEMAS.md ── «temos isto e aquilo»
│                                        │                         │
│      ┌── GERAL ───────────────┐      AUDITOR                     │
│      │  Meta-Governo          │      simples e coerente?         │
│      │  Governo-do-Projeto    │                                  │
│      │  Auditoria             │                                  │
│      └────────────────────────┘                                  │
│   cada tema = pasta: TEMA.md (mandato · estado · por fazer)      │
│                      + Handoff-S1, S2, …                         │
│                        │                                         │
│              abre-se UMA SESSÃO (o átomo)                        │
└────────────────────────┼─────────────────────────────────────────┘
                         │
┌─ 3. O ÁTOMO: qualquer sessão, em qualquer lado ──────────────────┐
│                                                                  │
│   pasta Active-Session/<sessão>/                                 │
│     Registo-Sessao.md ── Propósito · Resultado mínimo · Estado   │
│     Arvore.md ───────── onde estou                               │
│     Rascunhos.md ────── onde estaciono                           │
│     Decisoes.md ─────── o que decidi                             │
│     Registos-david.md ─ o que o David disse                      │
│                                                                  │
│   ABRE   copiar template → mandato (handoff · inbox · prompt)    │
│   CORRE  tarefa → olhar árvore → âncora: serve ou hiperespaço?   │
│   FECHA  registo final → lixo fora → Rascunhos em branco         │
│          → handoff + TEMA.md + TEMAS.md → commit → texto arranque│
└──────────────────────────────────────────────────────────────────┘
```

O átomo é o mesmo em Governo, Arquitecto e Thread. Só muda quem o abre e para que tema.

## 1. O que mudou de V1 para V2

| V1 (início da sessão) | V2 (fim da sessão) | Porquê |
|---|---|---|
| Três pastas na raiz: Governo, Arquiteto, Threads; CLAUDE.md só roteamento | Raiz pergunta GOVERNO ou PROJETO; PROJETO vai para `CLAUDE-projeto.md` intacto | Não partir o regime das threads antes de haver substituto. Arquiteto/ e Threads/ ficam vazias até ao tema Governo-do-Projeto. |
| Quatro modos: Geral, Debate, Auditor, Construtor | Dois: Geral, Auditor | Simplificar. Debate e Construtor eram o Geral com outro nome. |
| `Governo/CLAUDE.md` com os instrumentos comuns | `Governo/CLAUDE.md` de 6 linhas; instrumentos em `Protocolos/Governo-Enquadramento.md` | Um ficheiro de entrada, uma fonte de regras. |
| Raiz-Teste, Protocolos, Handoffs em cada modo | Protocolos e Raiz-Teste só na raiz do Governo; Handoffs por tema dentro do Geral | Modos só isolam trabalho. Protocolos são um só conjunto. Raiz-Teste é laboratório da raiz. |
| Handoff por tema, «já se explica» | `TEMAS.md` (quadro) + `TEMA.md` por tema (mandato · estado · por fazer) + handoffs numerados, tipo autocontido ou enquadrado | O Geral tem de saber sempre o que há e para que serve. |
| Inbox: uma, «a que o David indicar» | Uma por modo; entrada é semente de tema: abrir, passar, ou decidir | — |
| Âncora: Rascunhos.md | Quatro instrumentos com função própria: Árvore (onde estou), bloco Propósito/Resultado/Estado (o que entrego), Rascunhos (onde estaciono), pergunta-âncora (serve ou hiperespaço?) | A sessão derivou sem que ninguém registasse. |
| Fecho: handoff + commit | + texto de arranque da sessão seguinte, no chat | Poupa perguntas ao abrir. |

## 2. Princípios que continuam por discutir (não canónicos)

- Arquiteto: mapa permanente objectivo → cortes MECE → frentes; artefacto HTML com estado e aba de alertas; activado
  quando uma thread regista algo. Tema Governo-do-Projeto.
- Threads: isolamento real mais via expedita para sobreposições. Tema Governo-do-Projeto.
- Governo: artefacto HTML com o diagrama de todas as peças. Tema Meta-Governo.
- Wayfinder para cortar o objectivo do projecto em frentes: depois de Governo-do-Projeto aberto.

## 3. Onde está cada coisa

| O quê | Onde |
|---|---|
| Diagramas detalhados do fluxo | `Governo/fluxo-governo.md` (V2.1) |
| Como funciona o governo, em cinco linhas | `Governo/README.md` |
| Entrada | `CLAUDE.md` raiz → `Governo/CLAUDE.md` |
| Regras, âncora, handoff, inbox | `Governo/Protocolos/Governo-Enquadramento.md` |
| Templates | `Governo/Protocolos/` (Árvore, Handoff, Tema) e `Active-Session/Sessao-Template/` |
| Quadro de temas | `Governo/Modos-Governo/Geral/TEMAS.md` |
| O que o David disse, por ordem | `Registos-david.md` (Registos 1–8) |
| Decisões | `Decisoes.md` (D1–D19) |
