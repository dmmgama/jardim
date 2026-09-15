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

**Última actualização:** 2026-09-15

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
| **Estado** | `ONGOING` · **etapa 1 em curso** |
| **Aberta** | 2026-09-14 |
| **Mandato** | Produzir e manter a descrição factual inequívoca do espaço existente. |
| **Entrega** | **Etapa 1:** cenário completo do jardim (bloqueante). **Etapa 2:** aprofundamento por tema, ongoing. |
| **Sessões** | 0 |
| **Prioridade** | **Máxima.** T002 está bloqueada até a etapa 1 entregar. |

---

### T002 — Jardim V2

| | |
|---|---|
| **Pasta** | `30-THREADS/T002-jardim-v2/` |
| **Estado** | `À ESPERA` — bloqueada por T001 |
| **Aberta** | 2026-09-14 |
| **Mandato** | Debater e definir o que é o Jardim V2: âmbito, ambição, princípios, orçamento, faseamento. |
| **Entrega** | Definição de V2 em `entregue/`, para consolidar em `ESTADO.md` e `20-PLANO/`. |
| **Sessões** | 0 |
| **Bloqueio** | Aguarda a etapa 1 de T001. Sem base factual partilhada não há debate possível — foi assim que nasceram quatro planos com cotas diferentes. |
| **Nota** | Motivada por uma oportunidade vantajosa, ainda por explicar. Se tiver janela temporal curta, o David pode levantar o bloqueio. |

---

### T003 — Modelo solar

| | |
|---|---|
| **Pasta** | `30-THREADS/T003-modelo-solar/` |
| **Estado** | `ACTIVA` · pacote de arranque pronto, por montar |
| **Aberta** | 2026-09-15 |
| **Mandato** | Construir e manter um modelo digital paramétrico do quintal que permita testar posições de árvores e ver o efeito no sombreamento. |
| **Entrega** | Modelo funcional em `modelo/` + tabelas de exposição por cenário em `entregue/`. `ONGOING`. |
| **Sessões** | 0 |
| **Nota** | **Criada pela sessão T001 de 2026-09-15, com autorização expressa do David para derrogar G9.** A ratificar pelo Arquitecto — ver `INBOX.md`. |

---

## Fechadas

*(nenhuma)*

---

## Numeração

As threads numeram-se sequencialmente a partir de T001, sem reutilização. Uma thread fechada mantém o seu número para sempre.

Nome da pasta: `T<NNN>-<assunto-em-kebab-case>`.
