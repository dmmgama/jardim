---
created: 2026-09-17
project: Jardim
tipo: governo
modo: append-only
leitura: on-demand
summary: |
  Registo de todos os documentos produzidos por qualquer sessão — Arquitecto ou thread —
  tenham ido ou não para o NotebookLM. Organizado por secção temática, para que quem
  chega saiba o que existe. Append only.
---

# REGISTO DE DOCUMENTOS

> **Regra G23:** todas as sessões registam aqui os documentos que produziram, **tenham ido ou
> não para o NotebookLM**.
> **Regra G24:** **append only.** Não se reescreve nem se reordena — corrige-se acrescentando.
> **Regra G25:** as threads **podem** escrever aqui. Terceira e última excepção à regra territorial.
> **Regra G26:** **leitura *on demand*.** Não se lê por rotina ao arrancar sessão.

**Notebook do projecto:** ver `Notebook-LM` no front matter do `CLAUDE.md`.

---

## Como se lê este ficheiro

Está organizado por **secção temática**, não por ordem cronológica — para que quem chega saiba
**o que há**, não apenas o que se fez ontem. Dentro de cada secção, as entradas acumulam-se por
ordem de sessão.

**Colunas:**

| Coluna | O que é |
|---|---|
| **Documento** | Wikilink para o ficheiro original |
| **Sumário** | Uma a três linhas: o que é e o que conclui |
| **NotebookLM** | ✅ com wikilink para o PDF do deck · ❌ se não foi · ⏳ se está pendente |

**Nomenclatura da source no NotebookLM:** `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>`, onde `CARGO`
é `TNN` (thread), `ARQ` (Arquitecto) ou `DVD` (material do próprio David, de origem externa
ao repositório — **não tem wikilink, e não se elimina sem perguntar**). **TIPODOC:** `RESEARCH` ·
`REPORT` · `SINTESE` · `DOSSIER` · `NOTA` · `OUTROS`.

---

# 📚 PESQUISA

## 2026-09-17 · Thread T005 · «2026.09.17 - Arquiteto - Pesquisa de Catalogacao»

Fase 1 da T005 — quatro pesquisas de estado da arte lançadas em paralelo, com enunciados
separados e sem conhecimento umas das outras.

| # | Documento | Sumário | NotebookLM |
|---|---|---|---|
| 1 | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES]] | **16 disciplinas** que intervêm na caracterização deste espaço, com métodos, normas, fase de intervenção e decisões bloqueadas. Abriu por iniciativa própria a secção «impermeabilização de coberturas ajardinadas — a disciplina que faltava nomear» e classificou-a em **#1 das cinco que mais valem**. Matriz de conflitos entre disciplinas. | ⏳ por decidir |
| 2 | [[30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE]] | Nove eixos de software para modelar o jardim **e fazer experiências**. Conclui que **não existe plataforma única de «digital twin» a esta escala** — é uma arquitectura de ficheiros e scripts que se monta. Recomenda Rhino + Grasshopper + Ladybug/Honeybee. Identifica a **vegetação como «o eixo mais subestimado»**. | ⏳ por decidir |
| 3 | [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO]] | Do sensor ao actuador. **A humidade do substrato é o parâmetro mestre** — o único cuja falha mata plantas em dias. Achado mais valioso: **detecção acústica precoce do escaravelho da palmeira, >90% de sucesso** em ensaios publicados. Corta fertirrega, LoRaWAN, CO2 e sensores de vegetação. | ⏳ por decidir |
| 4 | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS]] | Levantamento com equipamento profissional (TLS, SLAM). **Veredicto dividido:** vale para a copa da palmeira, não justifica sozinha para os muros. **Inversão de intuição:** o reboco liso é o pior caso para fotogrametria e um dos melhores para TLS. Cadeia de tratamento gratuita em Windows. | ⏳ por decidir |
| 5 | [[30-THREADS/T005-caracterizacao/research/00-PONTO-DE-PARTIDA]] | Análise própria, escrita **antes** de as pesquisas chegarem. Diagnostica que o dossier está organizado por objecto físico e não sabe dizer quando pode parar. Fixou o teste de falsificação da thread. | ⏳ por decidir |

---

# 🧩 SÍNTESES

## 2026-09-17 · Thread T005 · «2026.09.17 - Arquiteto - Pesquisa de Catalogacao»

| # | Documento | Sumário | NotebookLM |
|---|---|---|---|
| 1 | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1]] | Cruzamento das quatro pesquisas. **Três convergiram, sem combinação, na mesma reclassificação: o jardim sobre laje é tecnicamente uma cobertura ajardinada.** Identifica o conflito retenção-vs-drenagem como o compromisso não resolvido mais valioso, e a tripla razão do bloqueio da palmeira. Propõe dois campos novos para a grelha da fase 2. | ⏳ por decidir |

---

# 📋 REPORTS

## 2026-09-17 · Thread T005 · «2026.09.17 - Arquiteto - Pesquisa de Catalogacao»

| # | Documento | Sumário | NotebookLM |
|---|---|---|---|
| 1 | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA]] | Report da fase 1: objectivos, sumário executivo, tabela das pesquisas com prompts, report próprio com **grau de certeza por bloco** (nulo para espessuras de camadas, baixo para preços), quatro tensões por resolver, conclusão e próximos passos. | ⏳ por decidir |

---

# 📐 DOSSIERS

*(sem entradas)*

---

# 📝 NOTAS

*(sem entradas)*

---

# 📦 OUTROS

## 2026-09-17 · Arquitecto · «2026.09.17 - Arquiteto - Pesquisa de Catalogacao»

| # | Documento | Sumário | NotebookLM |
|---|---|---|---|
| 1 | [[CONSOLIDACAO-NOTEBOOKLM-2026-09-17]] | **Primeira consolidação de documentação (G32–G35).** Auditoria às 9 sources e 11 artefactos do notebook. Propõe eliminar 4 sources e 3 artefactos, renomear 7. Achado grave: a `Analise_Decisao_Betonilha` está **revogada** — foi escrita para decidir a demolição, e o `ESTADO.md` decidiu a 2026-09-17 que a betonilha não se demole. **Proposta: nada executado sem aprovação.** | ❌ não enviado — é documento de governo, não material de estudo |

### Material do David já no notebook  (`DVD`)

Registado aqui para constar. **Não saiu de sessão nenhuma e não tem ficheiro no repositório** —
por isso não tem wikilink. Identificado pelo David a 2026-09-17.

| Source no notebook | Origem | Estado |
|---|---|---|
| «Relatório Técnico: Projeto de Reabilitação Paisag…» | **Pesquisa autónoma do David**, carregada por ele | 🔵 Vigente. **Não é do Agente propor eliminá-lo.** |

---

## Nota sobre esta primeira entrada

**Os cinco documentos de pesquisa, a síntese e o report foram produzidos *antes* de o
protocolo NotebookLM existir** — que foi escrito no fim desta mesma sessão. Por isso ficam
marcados `⏳ por decidir` em vez de `❌`: **a pergunta do G27 ainda não foi feita ao David.**

A partir da próxima sessão o fluxo é o normal: pergunta em lote logo após a produção, upload e
deck dos assinalados, e verificação com download no fim.
