---
created: 2026-09-14
project: Jardim
tipo: governo
summary: |
  Explicação do fluxo de governo do projecto Jardim: modos de sessão, ciclo de decisão, threads, canais de comunicação e ficheiros. Com diagramas.
---

# Fluxo de Projecto — Jardim Alcântara

Este documento explica **como o projecto funciona**: quem faz o quê, por que ordem, e onde fica registado. Serve tanto ao David como a qualquer agente que abra o repositório sem contexto.

---

## 1. Porque existe este governo

O projecto esteve seis meses parado com **quatro planos simultâneos** — V1 completo, conceito do jardineiro, DIY temporário, dossier da palmeira — espalhados por dois sistemas (repositório e Notion), nenhum com autoridade sobre os outros. Decisões tomadas em conversa nunca chegaram ao papel. Opções rejeitadas voltavam a ser discutidas do zero porque ninguém tinha registado o motivo da rejeição.

Este governo resolve três coisas:

| Problema | Solução |
|---|---|
| Decisões perdem-se na conversa | `ESTADO.md` — o que não está escrito não existe |
| Opções mortas ressuscitam | `REJEICOES.md` — espelho do Estado, com o **porquê** de cada descarte |
| Assuntos profundos poluem a visão geral | Threads estanques, com mandato próprio |

---

## 2. Os modos de sessão

Toda a sessão começa com uma pergunta: **Geral, Governo, Arquitecto ou Thread?**

| Modo | Lê ao arrancar | Para quê |
|---|---|---|
| **Geral** | Nada | Fazer o que o David pedir, sem protocolo. Não regista decisões sem ordem — avisa quando uma decisão fica só na conversa. |
| **Governo** | `CLAUDE.md`, `FLUXO-DE-PROJECTO.md`, `BRANCHES.md` | Mexer no sistema de governo. Não toca no conteúdo de projecto. |
| **Arquitecto** | Ver diagrama | Visão geral do projecto, decisões, threads. |
| **Thread** | Ver diagrama | Um assunto isolado, com mandato. |

O diagrama mostra os dois modos de projecto (Arquitecto e Thread).

```
                    ┌─────────────────────┐
                    │  ABRIR REPOSITÓRIO  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   CLAUDE.md raiz    │
                    │  "Arquitecto ou     │
                    │      Thread?"       │
                    └──────────┬──────────┘
                    ┌──────────┴──────────┐
                    │                     │
            ARQUITECTO                 THREAD
                    │                     │
                    ▼                     ▼
    ┌───────────────────────┐   ┌────────────────────┐
    │ Lê:                   │   │ Lê THREADS.md      │
    │  1. ESTADO.md         │   │ Lista activas      │
    │  2. THREADS.md        │   │ "Qual?"            │
    │  3. THREAD-MENSAGENS  │   └─────────┬──────────┘
    │  4. HANDOFF.md        │             │
    └───────────┬───────────┘             ▼
                │              ┌──────────────────────┐
                ▼              │ 30-THREADS/T00X/     │
    ┌───────────────────────┐  │ CLAUDE.md local      │
    │ Reporta ao David:     │  │ governa a partir daí │
    │ · threads activas     │  └──────────┬───────────┘
    │ · pedidos pendentes   │             │
    │ · onde ficou          │             ▼
    └───────────┬───────────┘  ┌──────────────────────┐
                │              │ Lê:                  │
                ▼              │  1. thread.md        │
          ┌──────────┐         │  2. mensagens.md     │
          │  DEBATE  │         │  3. material         │
          └──────────┘         └──────────┬───────────┘
                                          ▼
                                    ┌──────────┐
                                    │ TRABALHA │
                                    └──────────┘
```

### Arquitecto

**Detém a visão geral.** Decide, abre e fecha threads, mantém o estado. Opera na raiz.

Não mergulha em assuntos profundos: reconhece quando um assunto precisa de investigação e isola-o numa thread. Se mergulhar, perde a visão — e o assunto fica mal tratado por ser feito de passagem.

### Thread

**Trata um assunto, isolado, com mandato escrito.** Opera só na sua pasta.

Não vê o projecto todo nem precisa. Vê o seu mandato. Toda a exploração, becos sem saída e material intermédio ficam na pasta dela; só a entrega sobe.

---

## 3. O ciclo de decisão

```
        ┌───────────────────────────────────────────────┐
        │                  INBOX.md                     │
        │   ideias · dúvidas · pendências em bruto      │
        │   (qualquer um escreve, a qualquer momento)   │
        └────────────────────┬──────────────────────────┘
                             │  processa
                             ▼
        ┌───────────────────────────────────────────────┐
        │                 ARQUITECTO                    │
        │        consulta ESTADO + REJEICOES            │
        └──┬─────────────────┬──────────────────┬───────┘
           │                 │                  │
    descarta            decide já          abre THREAD
           │                 │                  │
           │                 │       ┌──────────▼──────────┐
           │                 │       │  mandato escrito    │
           │                 │       │        ↓            │
           │                 │       │  investiga (research)│
           │                 │       │        ↓            │
           │                 │       │  entrega (entregue/) │
           │                 │       └──────────┬──────────┘
           │                 │                  │
           │                 └──────┬───────────┘
           │                        ▼
           │        ┌───────────────────────────────┐
           │        │      ARQUITECTO DECIDE        │
           │        └───────────────┬───────────────┘
           │                        │
           ▼                        ▼
    ┌─────────────┐        ┌─────────────────┐
    │ REJEICOES.md│◄───────┤    ESTADO.md    │
    │ (com porquê)│ espelho│  (por tema)     │
    └─────────────┘        └────────┬────────┘
                                    ▼
                           ┌─────────────────┐
                           │   Jardim.html   │
                           │    (refeito)    │
                           └────────┬────────┘
                                    ▼
                           ┌─────────────────┐
                           │     NOTION      │
                           │  (publicação)   │
                           └─────────────────┘
```

**Em palavras:**

1. Ideias caem no `INBOX.md` a qualquer momento — mesmo a meio de outro assunto.
2. O Arquitecto processa o inbox: descarta, decide, ou abre thread.
3. Assunto que precisa de profundidade vira thread com mandato escrito.
4. A thread trabalha isolada, comunica pelo canal, entrega em `entregue/`.
5. O Arquitecto absorve a entrega e decide.
6. Cada decisão escreve em `ESTADO.md`; cada descarte em `REJEICOES.md`, **com o motivo**.
7. `Jardim.html` é refeito.
8. O Notion recebe o resultado estruturado.

> **A regra que mantém isto vivo:** nenhuma decisão existe fora de `ESTADO.md`, nenhum descarte fora de `REJEICOES.md`. Se ficou só na conversa, não aconteceu.

---

## 4. Comunicação thread ↔ arquitecto

Há **dois canais**. A conversa vive na thread, o sinal vive na raiz.

```
   THREAD T00X                              ARQUITECTO
        │                                        │
        │ precisa de decisão                     │
        │                                        │
        ├──1──► T00X/mensagens.md                │
        │       (pedido, com contexto)           │
        │                                        │
        ├──2──► THREAD-MENSAGENS.md (raiz)       │
        │       - [ ] data | T00X | assunto ─────┼──► vê o sinal
        │                                        │    ao arrancar
        ├──3──► handoff: "à espera"              │
        │                                        │
     (sessão termina)                            │
                                                 │
                                    responde ◄───┤
                                        │        │
        T00X/mensagens.md ◄──────────────┘        │
                                                 │
                        THREAD-MENSAGENS.md ◄────┤
                        - [x] ... [RESPONDIDO]   │
                                                 │
   (próxima sessão da thread)                    │
        │                                        │
        └──► lê mensagens.md → destrava          │
```

**Porquê dois canais:** o Arquitecto não pode ter de abrir sete pastas para descobrir se alguém precisa dele. Lê uma linha na raiz e sabe. A conversa fica onde pertence; o sinal fica onde é visto.

O Arquitecto **também pode** iniciar comunicação — correcções de rumo, informação nova — pela mesma via. A thread lê sempre `mensagens.md` ao arrancar.

---

## 5. Anatomia de uma thread

```
30-THREADS/T00X-assunto/
│
├── CLAUDE.md      ← governo local. Substitui o da raiz.
│                    Regra territorial: só escreve nesta pasta.
│
├── thread.md      ← MANDATO (fixo, escrito pelo Arquitecto)
│                    ESTADO face ao mandato (reescrito a cada sessão)
│                    HANDOFF (próximo passo, bloqueios)
│
├── mensagens.md   ← canal com o Arquitecto
│
├── research/      ← pesquisas, notas, material de trabalho.
│                    Pode ser caótico. Fica aqui.
│
└── entregue/      ← produto final + NOTA.md explicativa.
                     Só quando a thread entrega.
```

**Três princípios:**

**O mandato é fixo, o estado é reescrito.** O estado não se acumula em log: responde sempre "onde estou face ao que me foi mandado". Uma thread que deriva do mandato torna-se visível imediatamente.

**A fronteira é explícita.** Arquitecto e thread não partilham contexto — falam por um canal registado. É isso que mantém a thread estanque de verdade, e não só por convenção.

**Produto separado de processo.** O `research/` pode ser caótico; o que sai é uma peça limpa com nota explicativa. O Arquitecto consome a entrega, não o processo.

### Tipos de thread

| Tipo | Comportamento |
|---|---|
| `NORMAL` | Fecha quando entrega e o Arquitecto absorve. |
| `ONGOING` | Não fecha. Entrega por partes, cada uma com a sua nota. |

### Quem pode o quê

| Acção | Arquitecto | Thread |
|---|:---:|:---:|
| Criar thread | ✓ | ✗ |
| Fechar thread | ✓ | ✗ (propõe) |
| Escrever o mandato | ✓ | ✗ |
| Escrever em `ESTADO` / `REJEICOES` | ✓ | ✗ |
| Escrever em `INBOX.md` | ✓ | ✓ |
| Escrever em `THREAD-MENSAGENS.md` | ✓ | ✓ |
| Escrever fora da sua pasta | ✓ | ✗ |
| Refazer `Jardim.html` | ✓ | ✗ |
| Ler o repositório todo | ✓ | ✓ |

---

## 6. As três camadas de informação

```
┌──────────────────────────────────────────────────────┐
│  10-LOCAL/          O EXISTENTE                      │
│  Factual. Sem versões, sem plano.                    │
│  Geometria, exposição, materiais, árvores, muros.    │
│  Base de tudo. Mantida por T001 (ongoing).           │
└──────────────────────────────────────────────────────┘
                          ▲
                          │ assenta em
┌──────────────────────────────────────────────────────┐
│  20-PLANO/          O PLANO ACTIVO (V2)              │
│  Onde se decide. Alimentado por ESTADO.md.           │
└──────────────────────────────────────────────────────┘
                          ▲
                          │ consulta, não obedece
┌──────────────────────────────────────────────────────┐
│  90-ARQUEOLOGIA/    AS VERSÕES ANTIGAS               │
│  V1 completo · DIY temporário · migração             │
│  SÓ LEITURA. Nunca é decisão vigente.                │
└──────────────────────────────────────────────────────┘
```

**Local** não tem versões: é o que o espaço é. V1, DIY e V2 assentam todos nele. Foi a sua ausência que permitiu que existissem três planos com cotas diferentes.

**Arqueologia** existe para consultar, não para competir. V1 e DIY deixam de ser alternativas vivas.

---

## 7. Claude e Notion

| | Claude (este repositório) | Notion |
|---|---|---|
| **Função** | Pensar e decidir | Estruturar e publicar |
| **Contém** | Debate, threads, estado, rejeições | Resultado organizado, por plano |
| **Autoridade** | Sim — a decisão nasce aqui | Não — recebe o que já foi decidido |
| **Também é** | — | Fonte de recolha de informação |

O Notion tem a raiz **Jardim Hub**, com uma subpágina por plano: Jardim V1, Jardim DIY, Jardim V2.

Nenhuma decisão nasce no Notion. Nenhum debate fica só no Notion. Foi exactamente assim que o dossier da palmeira e o plano DIY ficaram invisíveis ao repositório durante meses.

---

## 8. Ficheiros de governo

| Ficheiro | Função | Quem escreve |
|---|---|---|
| `CLAUDE.md` | Dispatcher de modo (Geral · Governo · Arquitecto · Thread) + governo do Arquitecto | — |
| `ESTADO.md` | O que está decidido, por tema | Arquitecto |
| `REJEICOES.md` | Espelho: o que foi rejeitado e porquê | Arquitecto |
| `INBOX.md` | Ideias e pendências em bruto | Todos |
| `THREADS.md` | Threads activas e fechadas | Arquitecto |
| `THREAD-MENSAGENS.md` | Sinalizador global de pedidos | Todos |
| `HANDOFF.md` | Continuidade entre sessões de Arquitecto | Arquitecto |
| `FLUXO-DE-PROJECTO.md` | Este documento | Arquitecto |
| `Jardim.html` | Estado visual, refeito a cada decisão | Arquitecto |

---

## 9. Ciclo de vida de uma decisão

```
  IDEIA ──► INBOX ──► ARQUITECTO ──┬──► DESCARTE ──► REJEICOES.md (+ porquê)
                                   │
                                   ├──► DECISÃO ───► ESTADO.md
                                   │                      │
                                   └──► THREAD            │
                                          │               │
                                    mandato               │
                                          │               │
                                    research/             │
                                          │               │
                                    entregue/             │
                                          │               │
                                          └──► ARQUITECTO ┘
                                                          │
                                                          ▼
                                                  Jardim.html
                                                          │
                                                          ▼
                                                      NOTION
```

Uma decisão só está completa quando está em `ESTADO.md`. Uma rejeição só está completa quando tem motivo escrito em `REJEICOES.md`.

Uma rejeição **não é irreversível** — é memória. Se o contexto mudar, reabre-se; mas conscientemente, e a reabertura fica registada.
