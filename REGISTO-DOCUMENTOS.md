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

### Pesquisa autónoma do David  (`DVD`) — `40-PESQUISAS/David/`

**Não saiu de sessão nenhuma.** Identificada e arrumada pelo David a 2026-09-17, em pasta
própria. **Tem ficheiro no repositório e, por isso, tem wikilink.**

| # | Documento | Sumário | NotebookLM |
|---|---|---|---|
| 1 | [[40-PESQUISAS/David/2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA]] | **Sistemas de cobertura ajardinada**, com fontes FLL / ZinCo / Optigreen. **Inclui o prompt de pesquisa integral** (acrescentado pelo David a 2026-09-17), com as **8 perguntas** que o originaram. Cobre: espessuras de substrato por tipologia · substratos leves com densidade seca **e saturada** · camadas drenantes comparadas por peso · **cálculo de sobrecarga em kPa com Rankine/Coulomb e Eurocódigo 7** · **consequências de enterrar o colo de *Phoenix canariensis* e *Celtis australis*** · impermeabilização sobre betonilha fissurada e barreira anti-raízes FLL · saída de drenagem e modo de falha · **2-3 secções-tipo completas, camada a camada, com peso e custo por m²**. **Responde à questão da decomposição dos +0,50 m em camadas** que a T005 sinalizou à T004 como urgente. | ✅ está no notebook como «Relatório Técnico: Projeto de Reabilitação Paisag…» — **a renomear** para `DVD-26-09-17-RESEARCH-COBERTURA-AJARDINADA-FLL` |
| 2 | [[40-PESQUISAS/David/2026-09-14-Research-Relva_Natural_vs_Artificial]] | Relva natural vs. artificial — espécies, sombra, execução, manutenção, custos. **De 2026-09-14, anterior à T001.** Assume **muros a 3 m** (são 2,50) e **cota 1,60 m**: premissas hoje corrigidas. Superado por `Jardim_Relva_Natural_Viabilidade.md`, que é o relatório completo com fontes. | ✅ está no notebook — **proposto para eliminação** (superado) |

> **Os prompts ficam com os documentos.** O David guardou o prompt de pesquisa **dentro** do
> ficheiro #1, antes do relatório. **É a prática certa e adopta-se:** um relatório sem o prompt
> que o gerou não é auditável — não se sabe o que foi perguntado, o que ficou de fora, nem que
> premissas foram dadas ao modelo. Vale para pesquisa do David e para pesquisa de sessão.
>
> **Um detalhe que o prompt revela e importa:** foi escrito com **cota 1,60 m** e **muros de
> 2,0–2,5 m** — e descreve a betonilha como **«EMPOÇA água»**. Esta última premissa **está
> corrigida** desde 2026-09-16 (o quintal escoa; ver `ESTADO.md` §01). **Não invalida o
> relatório** — as espessuras e pesos FLL não dependem disso — mas quem o ler deve saber.

> **Nota de método, registada para constar.** Na primeira consolidação classifiquei o #1 como
> «por identificar» e o #2 como «órfão», por ter procurado os ficheiros apenas em
> `30-THREADS/`. **Ambos existiam.** Foi o que levou à criação do cargo `DVD` e à regra de
> perguntar antes de propor eliminar — ver `CLAUDE.md` §5.7.

---

## Nota sobre esta primeira entrada

**Os cinco documentos de pesquisa, a síntese e o report foram produzidos *antes* de o
protocolo NotebookLM existir** — que foi escrito no fim desta mesma sessão. Por isso ficam
marcados `⏳ por decidir` em vez de `❌`: **a pergunta do G27 ainda não foi feita ao David.**

A partir da próxima sessão o fluxo é o normal: pergunta em lote logo após a produção, upload e
deck dos assinalados, e verificação com download no fim.
