---
created: 2026-09-14
project: Jardim
tipo: governo
summary: |
  Registo de todas as threads do projecto: activas, em espera e fechadas.
---

# THREADS

> **Regra G9:** só o Arquitecto cria uma thread.
> **Regra G10:** só o Arquitecto fecha uma thread. A thread propõe o fecho pelo canal de mensagens.
> **Regra G11:** o mandato é escrito em `thread.md` no momento da criação.

**Última actualização:** 2026-09-14

---

## Estados possíveis

| Estado | Significado |
|---|---|
| `ACTIVA` | Em trabalho. |
| `ONGOING` | Activa e sem data de fecho prevista — alimenta-se por partes. |
| `À ESPERA` | Bloqueada à espera de resposta do Arquitecto ou de input externo. |
| `PROPOSTA DE FECHO` | A thread entregou e propôs fechar. Aguarda o Arquitecto. |
| `FECHADA` | Entrega absorvida. Só de leitura. |

---

## Activas

### T001 — Local

| | |
|---|---|
| **Pasta** | `30-THREADS/T001-local/` |
| **Estado** | `ONGOING` |
| **Aberta** | 2026-09-14 |
| **Mandato** | Produzir e manter a descrição factual inequívoca do espaço existente. |
| **Entrega** | Incremental, por tema, para `10-LOCAL/`. Não fecha. |
| **Sessões** | 0 |

---

### T002 — Jardim V2

| | |
|---|---|
| **Pasta** | `30-THREADS/T002-jardim-v2/` |
| **Estado** | `ACTIVA` |
| **Aberta** | 2026-09-14 |
| **Mandato** | Debater e definir o que é o Jardim V2: âmbito, ambição, princípios, orçamento, faseamento. |
| **Entrega** | Definição de V2 em `entregue/`, para consolidar em `ESTADO.md` e `20-PLANO/`. |
| **Sessões** | 0 |

---

## Fechadas

*(nenhuma)*

---

## Numeração

As threads numeram-se sequencialmente a partir de T001, sem reutilização. Uma thread fechada mantém o seu número para sempre.

Nome da pasta: `T<NNN>-<assunto-em-kebab-case>`.
