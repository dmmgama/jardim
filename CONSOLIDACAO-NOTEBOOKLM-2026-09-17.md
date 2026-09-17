---
created: 2026-09-17
project: Jardim
tipo: consolidacao
cargo: ARQ
estado: PROPOSTA — aguarda decisão do David
summary: |
  Primeira consolidação de documentação do NotebookLM (G32-G35). Auditoria às 9 sources e
  11 artefactos existentes, classificados em VIGENTE / SUPERADO / REVOGADO / DUPLICADO.
  Achado principal: há 3 duplicados exactos, 1 source revogada por decisão de 2026-09-17
  (a betonilha não se demole), 1 source órfã (superada), e 11 artefactos com títulos
  gerados automaticamente em inglês, nenhum a seguir a convenção de nomes. Expôs também
  uma lacuna do protocolo escrito no mesmo dia: faltava o cargo DVD, para material que o
  próprio David carrega e que não tem ficheiro no repositório — sem ele, "não tem ficheiro"
  levaria mecanicamente a "eliminar". Nada é eliminado sem aprovação explícita (G34).
---

# Consolidação NotebookLM — 2026-09-17

> **Regra G34: nada se elimina sem aprovação explícita do David.** Isto é uma proposta.

**Notebook:** «David - PES - Jardim» · 9 sources · 11 artefactos
**Estado do repositório à data:** `ESTADO.md` actualizado a 2026-09-17 (base de projecto fixada)

---

## 1. O problema, em duas linhas

O notebook foi carregado a **15 de Setembro**. **A base de projecto mudou a 17** — a betonilha
deixou de se demolir, o jardim passou a subir +0,50 m por cima dela, e o projecto foi
reformulado. **Há material lá dentro que responde a perguntas que já não se fazem.**

Um notebook que responde com base em documentação revogada **é pior que um notebook vazio**: dá
respostas erradas com a autoridade de quem cita uma fonte.

---

## 2. Sources — diagnóstico

| # | Source | Estado | Porquê | Proposta |
|---|---|---|---|---|
| 1 | `DOSSIER-LOCAL.md` | 🟢 **VIGENTE** | Documento canónico do Local (`ESTADO.md` §01). A referência factual do projecto. | **Manter** |
| 2 | `Jardim_Analise_Decisao_Betonilha.md` | 🔴 **REVOGADO** | Foi escrito para decidir **se se demolia a betonilha**. `ESTADO.md` decidiu a 2026-09-17: **«A betonilha NÃO se demole.»** O documento responde a uma pergunta encerrada. | **Eliminar ambas as cópias** |
| 3 | `Jardim_Analise_Decisao_Betonilha.md` *(2.ª cópia)* | 🟠 **DUPLICADO** + revogado | Cópia exacta da #2. | **Eliminar** |
| 4 | `Jardim_Catalogo_Vegetal.md` | 🟡 **VIGENTE com reserva** | Continua útil (espécies por zona), mas foi escrito **antes** da reclassificação como cobertura ajardinada e **antes** da correcção da drenagem. As conclusões por luz mantêm-se; as de encharcamento estão atenuadas (ver `INBOX.md`). | **Manter, com nota** |
| 5 | `Jardim_Relva_Natural_Viabilidade.md` | 🟡 **VIGENTE com reserva** | Conclusão principal (relva de gramíneas inviável) mantém-se e é robusta — assenta em luz, não em água. Mas contém secções de **sequência de demolição** que estão revogadas. | **Manter, com nota** |
| 6 | `Jardim_Relva_Natural_Viabilidade.md` *(2.ª cópia)* | 🟠 **DUPLICADO** | Cópia exacta da #5. | **Eliminar** |
| 7 | `Jardim_Research_Relva_Natural_vs_Artificial.md` | 🟠 **SUPERADO** | **Correcção 2026-09-17:** o ficheiro **existe** em `40-PESQUISAS/David/` — não o tinha encontrado porque procurei só em `30-THREADS/`. É de **2026-09-14**, anterior à T001, e assume premissas hoje corrigidas: muros a **3 m** (são 2,50) e cota **1,60 m**. Superado por #5. | **Eliminar do notebook** — o ficheiro fica no repositório |
| 8 | `Jardim_Software_Modelacao_Solar.md` | 🟡 **PARCIALMENTE SUPERADO** | Foi o relatório que fechou a via Google 3D (`REJEICOES.md` §11) — **essa parte mantém-se**. Mas a matéria de captura 3D foi **superada duas vezes**: pela pesquisa da T003 e pela `04-NUVEM-DE-PONTOS` da T005. | **Decisão tua** — ver §4 |
| 9 | «Relatório Técnico: Projeto de Reabilitação Paisag…» | 🔵 **MATERIAL DO DAVID** (`DVD`) · 🟢 **VIGENTE E CRÍTICO** | **Identificado 2026-09-17:** pesquisa autónoma do David, em `40-PESQUISAS/David/Sem título.md`. **É a peça mais actual do notebook** — trata **espessuras de substrato FLL, substratos leves com peso saturado e carga sobre o muro SW**. Responde ao conflito que a T005 identificou como o mais valioso por arbitrar. | **Manter e renomear.** Ver §4-bis. |

**Balanço:** 1 vigente sem reserva · 3 vigentes com reserva · **4 propostos para eliminação** ·
1 material do David (mantém-se).

---

## 3. Artefactos (decks e infográficos) — diagnóstico

**Problema transversal: nenhum segue convenção de nomes, e 8 em 11 têm título em inglês** —
gerados automaticamente pelo NotebookLM, não nomeados por ninguém.

| # | Artefacto | Tipo | Estado | Proposta |
|---|---|---|---|---|
| 1 | *Geotechnical Landscape Engineering* | deck | ❓ origem não identificada | Identificar |
| 2 | *Boa Hora 15 Technical Diagnostic* | deck | 🟠 provável duplicado de #3 | Eliminar um |
| 3 | *Alcântara Garden Technical Diagnostic* | deck | 🟢 vigente (dossier) | **Renomear** |
| 4 | *Jardim de Alcântara Site Analysis* | infográfico | 🟢 vigente (dossier) | **Renomear** |
| 5 | *Alcântara Botanical Feasibility* | deck | 🟡 catálogo vegetal | **Renomear** |
| 6 | *Jardim_Software_Modelacao_Solar* | deck | 🟡 parcialmente superado | Ver §4 |
| 7 | *Jardim_Analise Decisao_Betonilha* | deck | 🔴 **REVOGADO** | **Eliminar** |
| 8 | *Jardim_Analise_Decisao_Betonilha* | deck | 🔴 **REVOGADO** + duplicado | **Eliminar** |
| 9 | *Garden Sunlight Modeling Blueprint* | infográfico | 🟡 solar | Ver §4 |
| 10 | *Jardim Alcântara Structural Diagnosis* | deck | ❓ origem não identificada | Identificar |
| 11 | *Relvado Alcântara Feasibility* | deck | 🟡 relva | **Renomear** |

**Balanço:** **3 propostos para eliminação** · 4 a renomear · 2 por identificar · 2 dependentes
da decisão §4.

---

## 4. A única decisão que não é óbvia

**`Jardim_Software_Modelacao_Solar` e os seus dois artefactos.**

O documento tem duas partes com destinos diferentes:

- **A rejeição da via Google 3D** — continua **vigente**, está em `REJEICOES.md` §11 e a
  `04-NUVEM-DE-PONTOS` **confirmou-a por via independente** (a fotogrametria falha por física da
  superfície, não por qualidade da ferramenta).
- **A matéria de captura 3D e escolha de software** — **superada duas vezes**, pela T003 e pela
  T005.

**Três opções:**

| | Opção | Consequência |
|---|---|---|
| **A** | **Manter** como está | O notebook pode responder com recomendações de software que já foram substituídas. |
| **B** | **Eliminar** | Perde-se a fundamentação original da rejeição da via Google 3D — que está registada em `REJEICOES.md`, mas sem o detalhe. |
| **C** | **Substituir** pelas pesquisas novas da T005 | Mantém-se a conclusão vigente e actualiza-se a fundamentação. **É a que recomendo**, se decidires enviar a `04-NUVEM-DE-PONTOS`. |

---

## 4-bis. A descoberta que muda a prioridade desta consolidação

**O documento do David responde à pergunta que a T005 deixou em aberto.**

A síntese da fase 1 identificou como *«o compromisso técnico não resolvido mais valioso do
projecto»* o conflito **retenção de água para a planta vs. drenagem rápida para proteger a
impermeabilização** — e concluiu que a espessura de cada camada *«é uma decisão de compromisso,
não uma optimização única, e ainda não foi tomada neste projecto»*.

**Já tinha sido trabalhada.** O «Relatório Técnico: Projeto de Reabilitação Paisagística e
Geotécnica com Sistema de Cobertura Ajardinada» traz, com fontes FLL / ZinCo / Optigreen:

- **Espessuras mínimas e recomendadas de substrato por tipologia de plantação** — e a
  classificação extensiva / semi-intensiva / intensiva que decorre delas.
- **Substratos técnicos leves com densidade seca *e saturada***, que é o parâmetro certo: em
  geotecnia de coberturas o que dimensiona não é o peso seco, é o peso saturado.
- **Mitigação da sobrecarga sobre o muro de suporte SW** — explicitamente, pelo nome.

**O que isto significa, por ordem de importância:**

1. **O sinal urgente que a T005 mandou à T004 — «os +0,50 m estão fixados como cota mas não
   decompostos em camadas» — tem agora com que ser respondido.** O documento não decide por
   ninguém, mas dá as ordens de grandeza que faltavam.
2. **Confirma a reclassificação por via totalmente independente.** Três pesquisas da T005
   convergiram em que isto é uma cobertura ajardinada; **este documento já o tratava como tal,
   e o David encomendou-o antes.**
3. **É o argumento mais forte a favor de o notebook ser usado para perguntar (G30).** Esta
   informação estava disponível durante toda a fase 1 e **não foi consultada** — porque o
   protocolo que manda consultar só foi escrito hoje, depois das pesquisas.

> **Recomendação do Arquitecto:** este documento deve ser **o primeiro a ser lido** por quem
> pegar na questão das camadas, e **deve ser passado à T004** com o sinal já enviado. Fica em
> `INBOX.md`.

---

## 5. Nomenclatura proposta para o que fica

Aplicando a convenção `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>` (G28), com a data **do documento
original**, não a do upload:

| Actual | Proposto |
|---|---|
| `DOSSIER-LOCAL.md` | `T001-26-09-15-DOSSIER-LOCAL` |
| `Jardim_Catalogo_Vegetal.md` | `T001-26-09-15-RESEARCH-CATALOGO-VEGETAL` |
| `Jardim_Relva_Natural_Viabilidade.md` | `T001-26-09-15-RESEARCH-RELVA-VIABILIDADE` |
| *Alcântara Garden Technical Diagnostic* | `T001-26-09-15-DOSSIER-LOCAL` *(igual à source)* |
| *Alcântara Botanical Feasibility* | `T001-26-09-15-RESEARCH-CATALOGO-VEGETAL` |
| *Relvado Alcântara Feasibility* | `T001-26-09-15-RESEARCH-RELVA-VIABILIDADE` |
| «Relatório Técnico: Projeto de Reabilitação Paisag…» | `DVD-26-09-17-RESEARCH-COBERTURA-AJARDINADA-FLL` |

> **Nota:** as sources antigas foram carregadas antes de a convenção existir. **Renomear sources
> pode não ser possível via API** — confirmo antes de prometer. Os artefactos têm acção de
> `rename` disponível.

---

## 6. Uma lacuna de protocolo que esta consolidação expôs

O protocolo escrito hoje previa dois cargos: `TNN` (thread) e `ARQ` (Arquitecto). **Faltava
o terceiro: o próprio David.**

Nem tudo o que está no notebook sai de uma sessão. O David carrega material próprio — pesquisa
autónoma, documento de terceiro, relatório encomendado. Esse material **não tem ficheiro no
repositório e, por isso, não tem wikilink.**

**O risco concreto, que quase se materializou nesta consolidação:** eu classifiquei a source #9
como «por identificar» porque não encontrava ficheiro correspondente. **Num critério puramente
mecânico, "não tem ficheiro" teria levado a "eliminar"** — e teria proposto apagar trabalho do
David por não o reconhecer.

**Correcção aplicada ao protocolo (G28):** cargo `DVD` criado, com regra explícita — *o Agente
NÃO PODE propor eliminar material do David por não reconhecer a origem: pergunta primeiro.*
Propagada aos seis `CLAUDE.md` de thread.

---

## 7. Resumo da proposta

| Acção | Sources | Artefactos |
|---|---|---|
| **Eliminar** | 4 | 3 |
| **Renomear** | 3 *(a confirmar se é possível)* | 4 |
| **Identificar primeiro** | — | 2 |
| **Manter sem tocar** | 2 *(dossier + material do David)* | — |

**Nada é executado sem a tua aprovação, item a item.**
