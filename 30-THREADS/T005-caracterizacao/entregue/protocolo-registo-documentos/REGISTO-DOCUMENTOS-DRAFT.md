---
created: 2026-09-18
updated: 2026-09-18
project: Jardim
tipo: governo
modo: append-only
leitura: on-demand
lingua: pt-PT
instrucoes: REGISTO-DOCUMENTOS-INSTRUCOES.md
estado: DRAFT — para avaliação do David antes de substituir REGISTO-DOCUMENTOS.md
summary: |
  Catálogo único de todos os documentos produzidos no projecto — por Arquitecto, por
  threads e pelo David — tenham ido ou não para o NotebookLM. Organizado por Dono e,
  dentro de cada dono, por sessão. Append only, excepto a secção de dependências.
  Draft: migração integral do registo antigo para a estrutura nova, com inventário
  completo do repositório.
---

> ## ⚠ ESTE FICHEIRO É UM DRAFT
>
> Aplica as regras de `REGISTO-DOCUMENTOS-INSTRUCOES.md` a **tudo** o que já existe no
> repositório. **Não substitui `REGISTO-DOCUMENTOS.md` sem decisão do David.**
> As reservas estão na secção [[#Notas do draft]], no fim.

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (a) · DESCRIÇÃO — escrita uma vez, não se toca.                       -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# REGISTO DE DOCUMENTOS

Catálogo de **tudo o que este projecto produziu em forma de documento** — de sessões de
Arquitecto, de threads, e do próprio David — tenha ido ou não para o NotebookLM.
Existe para que ninguém volte a fazer trabalho que já estava feito.

> **Append only (G24).** Não se reescreve nem se reordena. Corrige-se acrescentando.
> **Única excepção:** a secção [[#Dependências entre documentos]], no fim deste ficheiro.
>
> **Leitura *on demand* (G26 · T21).** Não se lê por rotina ao arrancar sessão.
>
> **As threads podem escrever aqui (G25 · T2).** Terceira e última excepção à regra territorial.
>
> **Como se preenche:** ver `REGISTO-DOCUMENTOS-INSTRUCOES.md`. **Não se improvisa.**

**Notebook do projecto:** ver `Notebook-LM` no front matter do `CLAUDE.md`.
**Nomenclatura da source:** `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>` · `CARGO` = `TNN` · `ARQ` · `DVD`.

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (b) · ÍNDICE GERAL — estático. Só muda se nascer secção nova.         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Índice geral

- [[#Índice de Donos]]
- [[#Índice por Tipo]]
- [[#1 · ARQUITECTO]]
- [[#2 · THREADS]]
- [[#3 · DAVID]]
- [[#4 · OUTROS]]
- [[#Dependências entre documentos]]

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (c) · ÍNDICE DE DONOS — MANUAL.                                       -->
<!-- Quem abre uma thread nova (= Arquitecto, G9) acrescenta aqui uma linha.    -->
<!-- Uma thread NÃO edita esta zona: cria o heading no corpo e avisa por INBOX. -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Índice de Donos

| Dono | Tag | Secção |
|---|---|---|
| Arquitecto | `#dono/arquitecto` | [[#1 · ARQUITECTO]] |
| T001 · local | `#dono/t001` | [[#T001 · local]] |
| T002 · jardim-v2 | `#dono/t002` | [[#T002 · jardim-v2]] |
| T003 · modelo-solar | `#dono/t003` | [[#T003 · modelo-solar]] |
| T004 · geometria | `#dono/t004` | [[#T004 · geometria]] |
| T005 · caracterizacao | `#dono/t005` | [[#T005 · caracterizacao]] |
| David | `#dono/david` | [[#3 · DAVID]] |
| Outros | `#dono/outros` | [[#4 · OUTROS]] |

<!-- Thread nova → acrescentar linha acima E criar o heading H3 na secção 2. -->

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (d) · ÍNDICE POR TIPO — automático pela TAG. Não se mexe.             -->
<!-- Clicar na tag lista as ocorrências. Os blocos Dataview estão COMENTADOS:   -->
<!-- com tudo num só ficheiro, `FROM #tag` devolve o ficheiro, não as linhas.   -->
<!-- Só se activam se o registo passar a uma nota por documento. Ver §5.2.      -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Índice por Tipo

Vocabulário **fechado**. Se o tipo não for evidente, **pergunta-se ao David** — não se
classifica ao calha (G28 · T19). `Outros` é para quando não há certeza.

**Agrega os 58 documentos do corpo, um por tipo, cada um uma só vez.** Dentro de cada
tipo, por data decrescente. A tag continua a ser o mecanismo real de agregação em
Obsidian (§5.2); a tabela abaixo é o que torna o índice legível **sem plugins**.

### Sínteses · #tipo/sintese
Cruza e conclui sobre vários documentos anteriores.

**1 documento.**

| Documento | Dono | Data |
|---|---|---|
| [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1\|Síntese da fase 1]] | T005 | 2026-09-17 |
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/sintese SORT Data DESC
```
-->

### Reports · #tipo/report
Relato de trabalho feito: objectivos, método, achados, próximos passos.

**1 documento.**

| Documento | Dono | Data |
|---|---|---|
| [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA\|Report da fase 1 da T005]] | T005 | 2026-09-17 |
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/report SORT Data DESC
```
-->

### Research · #tipo/research
Estado da arte ou investigação externa. **Leva sempre o prompt dentro do ficheiro.**

**14 documentos.**

| Documento | Dono | Data |
|---|---|---|
| [[30-THREADS/T003-modelo-solar/research/02-CAPTURA-3D-ESTADO-DA-ARTE\|Captura 3D com telemóvel — estado da arte]] | Arquitecto (para T003) | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/02-PESQUISA-TRANSICOES\|Pesquisa — tipologias de transição de cota]] | T004 | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/05-PESQUISA-VEGETACAO\|Pesquisa — o que plantar em cada zona]] | T004 | 2026-09-17 |
| [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES\|Especialidades técnicas na caracterização]] | T005 | 2026-09-17 |
| [[30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE\|Software para digital twin do jardim]] | T005 | 2026-09-17 |
| [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO\|Monitorização e actuação em contínuo]] | T005 | 2026-09-17 |
| [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS\|Nuvem de pontos com equipamento profissional]] | T005 | 2026-09-17 |
| [[40-PESQUISAS/David/2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA\|Sistemas de cobertura ajardinada]] | David | 2026-09-17 |
| [[30-THREADS/T001-local/research/Estado_Arte_Caracterizacao_Espaco_Exterior\|Estado da arte — caracterização de espaço exterior privado]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/research/Jardim_Catalogo_Vegetal\|Catálogo de espécies vegetais viáveis]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade\|Relva natural — relatório de investigação]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/research/Jardim_Software_Modelacao_Solar\|Software para modelar exposição solar]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/research/Jardim_Analise_Decisao_Betonilha\|Análise — demolir ou manter a betonilha]] | T001 | 2026-09-14 |
| [[40-PESQUISAS/David/2026-09-14-Research-Relva_Natural_vs_Artificial\|Relva natural vs. artificial]] | David | 2026-09-14 |
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/research SORT Data DESC
```
-->

### Dossiers · #tipo/dossier
Compilação de referência sobre um objecto ou tema, para consulta.

**4 documentos.**

| Documento | Dono | Data |
|---|---|---|
| [[30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL\|Dossier técnico do Local]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico\|Planta e Espaço Físico — rev. 16:30]] | Outros | 2026-09-15 |
| [[30-THREADS/T001-local/Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico.BACKUP-20260915\|Planta e Espaço Físico — backup]] | Outros | 2026-09-15 |
| [[30-THREADS/T001-local/research/Planta_e_Espaco_Fisico\|Planta e Espaço Físico — documento-mestre]] | T001 | 2026-09-14 |
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/dossier SORT Data DESC
```
-->

### Notas · #tipo/nota
Registo curto, pontual, sem pretensão de completude.

**22 documentos.**

| Documento | Dono | Data |
|---|---|---|
| [[30-THREADS/T002-jardim-v2/research/06-PROJECTO-REFORMULADO-VISTA\|O projecto reformulado — um problema de vista]] | T002 | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/research/07-ZONAMENTO-DAVID\|Zonamento — seis zonas, do David]] | T002 | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/research/08-EXPLICACAO-DO-LOCAL\|A explicação do local]] | T002 | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/entregue/NOTA\|Nota de entrega — T002 · Jardim V2]] | T002 | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/entregue/PROPOSTA-T004\|Proposta — T004 · A Geometria do Jardim]] | T002 | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/01-O-DESNIVEL-ENUNCIADO\|O desnível — enunciado do problema]] | T004 | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/03-SOLUCAO-TRANSICAO\|A transição — degrau-banco com escada no muro SE]] | T004 | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/04-TRANSICAO-FIXADA\|A transição — geometria fixada]] | T004 | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/06-O-PROBLEMA-DAS-COPAS\|As copas — metade do jardim está por baixo delas]] | T004 | 2026-09-17 |
| [[30-THREADS/T004-geometria/research/07-ARVORES-POSICAO-E-COPAS\|As árvores — posição, copas e consequências]] | T004 | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/research/01-HIPOTESES-NA-MESA\|Hipóteses na mesa — T002 sessão 1]] | T002 | 2026-09-16 |
| [[30-THREADS/T002-jardim-v2/research/02-IDEIAS-DAVID-SESSAO1\|Ideias do David — sessão 1]] | T002 | 2026-09-16 |
| [[30-THREADS/T002-jardim-v2/research/03-PEDIDO-T003-COTA\|Pedido à T003 — a luz e a subida de cota]] | T002 | 2026-09-16 |
| [[30-THREADS/T002-jardim-v2/research/04-ZONAMENTO-PRESSUPOSTO\|Zonamento de intervenção — pressuposto de trabalho]] | T002 | 2026-09-16 |
| [[30-THREADS/T002-jardim-v2/research/05-LUZ-COTA-ESTIMATIVA-T002\|Ticket 1 — a luz muda com a subida de cota?]] | T002 | 2026-09-16 |
| [[30-THREADS/T002-jardim-v2/David-Docs/INDICE\|Índice de David-Docs · T002]] | T002 | 2026-09-16 |
| [[30-THREADS/T003-modelo-solar/research/00-PACOTE-ARRANQUE\|Pacote de arranque da T003]] | Arquitecto (para T003) | 2026-09-15 |
| [[30-THREADS/T003-modelo-solar/research/01-PLANO-DE-SESSAO\|Plano da primeira sessão da T003]] | Arquitecto (para T003) | 2026-09-15 |
| [[30-THREADS/T003-modelo-solar/modelo/PONTE-DADOS\|Ponte de dados T001 → T003]] | Arquitecto (para T003) | 2026-09-15 |
| [[30-THREADS/T003-modelo-solar/LEIA-ME-DAVID\|T003 — o que isto é, e o que vai acontecer]] | Arquitecto | 2026-09-15 |
| [[30-THREADS/T001-local/entregue/NOTA-entregue-etapa1\|Nota de entrega da etapa 1]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/Docs-David-Local/arqueologia/NOTA\|Nota de arqueologia — Docs-David-Local]] | T001 | 2026-09-15 |
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/nota SORT Data DESC
```
-->

### Outros · #tipo/outros
Governo, auditoria, consolidação — **ou** quando não há certeza.

**16 documentos.**

| Documento | Dono | Data |
|---|---|---|
| [[AUDITORIA-2026-09-17\|Auditoria — estado das quatro threads]] | Arquitecto | 2026-09-17 |
| [[CONSOLIDACAO-NOTEBOOKLM-2026-09-17\|Consolidação NotebookLM 2026-09-17]] | Arquitecto | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/ARRUMACAO\|Arrumação — instruções de sessão T002]] | T002 | 2026-09-17 |
| [[30-THREADS/T004-geometria/ARRUMACAO\|Arrumação — instruções de sessão T004]] | T004 | 2026-09-17 |
| [[30-THREADS/T005-caracterizacao/research/00-PONTO-DE-PARTIDA\|Ponto de partida — o que o projecto já tem]] | T005 | 2026-09-17 |
| [[30-THREADS/T002-jardim-v2/TICKETS\|Tickets — T002]] | T002 | 2026-09-16 |
| [[30-THREADS/T001-local/research/INVENTARIO-DOCS-DAVID-LOCAL\|Inventário exaustivo de Docs-David-Local]] | T001 | 2026-09-15 |
| [[30-THREADS/T001-local/research/AUDITORIA-COERENCIA-T001\|Auditoria de coerência da T001]] | T001 | 2026-09-15 |
| [[90-ARQUEOLOGIA/migracao-2026-09-14/MIGRACAO_2026-09-14\|Migração 2026-09-14]] | Outros | 2026-09-14 |
| [[90-ARQUEOLOGIA/migracao-2026-09-14/worklog\|Worklog da migração]] | Outros | 2026-09-14 |
| [[10-EQUIPA/adriano/proposta_adriano_Fev2026\|Proposta do Adriano — Fev 2026]] | Outros | 2026-02 `[dia não apurado]` |
| [[10-EQUIPA/adriano/resposta_david_pedido_proposta\|Resposta do David ao pedido de proposta]] | Outros | s/d |
| [[90-ARQUEOLOGIA/V1-completo/Jardim_Alcantara_Knowledge_Base\|Knowledge Base do Jardim V1]] | Outros | s/d |
| [[90-ARQUEOLOGIA/V1-completo/Jardim_Alcantara_Anexos\|Anexos do Jardim V1]] | Outros | s/d |
| [[90-ARQUEOLOGIA/V1-completo/resumo-notion-jardim\|Resumo Notion — Jardim V1]] | Outros | s/d |
| [[90-ARQUEOLOGIA/DIY/resumo-notion-jardimtemporario\|Resumo Notion — jardim temporário DIY]] | Outros | s/d |
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/outros SORT Data DESC
```
-->

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 1 DE 4 — ARQUITECTO                                          -->
<!-- Blocos de sessão por ordem cronológica. O mais recente vai para o FIM.     -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 1 · ARQUITECTO

## 2026-09-15 · `[não apurado]`
#dono/arquitecto

Abertura da T003 pelo Arquitecto: pacote de arranque, plano da primeira sessão e ponte de
dados escritos **antes** de a thread ter sessão própria — são material do Arquitecto
depositado em território da T003. Nenhum foi ao notebook.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/nota | 2026-09-15 | Arquitecto (para T003) | `[não apurado]` | [[30-THREADS/T003-modelo-solar/research/00-PACOTE-ARRANQUE\|Pacote de arranque da T003]] | [[30-THREADS/T003-modelo-solar/research/00-PACOTE-ARRANQUE.md\|00-PACOTE-ARRANQUE.md]] · — sem PDF | Fixa o que a T003 tem de produzir: **DLI por zona e por estação**, e não um modelo genérico. **Não foi ao notebook** — material de arranque interno de thread. | — |
| #tipo/nota | 2026-09-15 | Arquitecto (para T003) | `[não apurado]` | [[30-THREADS/T003-modelo-solar/research/01-PLANO-DE-SESSAO\|Plano da primeira sessão da T003]] | [[30-THREADS/T003-modelo-solar/research/01-PLANO-DE-SESSAO.md\|01-PLANO-DE-SESSAO.md]] · — sem PDF | Sequência de execução da primeira sessão da T003, por fases, a começar em «antes de pedir nada». **Não foi ao notebook** — método interno. | — |
| #tipo/nota | 2026-09-15 | Arquitecto (para T003) | `[não apurado]` | [[30-THREADS/T003-modelo-solar/modelo/PONTE-DADOS\|Ponte de dados T001 → T003]] | [[30-THREADS/T003-modelo-solar/modelo/PONTE-DADOS.md\|PONTE-DADOS.md]] · — sem PDF | Define **como o pacote de dados da T001 chega à T003** sem violar a regra territorial. **Não foi ao notebook** — mecânica interna de projecto. | — |
| #tipo/nota | 2026-09-15 | Arquitecto | `[não apurado]` | [[30-THREADS/T003-modelo-solar/LEIA-ME-DAVID\|T003 — o que isto é, e o que vai acontecer]] | [[30-THREADS/T003-modelo-solar/LEIA-ME-DAVID.md\|LEIA-ME-DAVID.md]] · — sem PDF | Explicação da T003 **escrita para o David, não para o agente**: a thread constrói um modelo onde se move uma árvore e a sombra muda, e **está desenhada para arrancar sem dados nenhuns**. Sem front matter — data lida do corpo. | — |

## 2026-09-17 · «2026.09.16 - T002 S2 e T004 S1»
#dono/arquitecto

Auditoria às quatro threads, para o David auditar antes de prosseguir, e encomenda de uma
pesquisa de estado da arte à T003 para a thread não ter de a repetir. Nenhum foi ao notebook.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/outros | 2026-09-17 | Arquitecto | «2026.09.16 - T002 S2 e T004 S1» | [[AUDITORIA-2026-09-17\|Auditoria — estado das quatro threads]] | [[AUDITORIA-2026-09-17.md\|AUDITORIA-2026-09-17.md]] · — sem PDF | Folha de auditoria por thread, em duas partes: cumprimento de protocolo e **arrumação de conteúdo**. Conclui que **a parte que produz trabalho é a segunda** — renomear, consolidar, arquivar. **Não foi ao notebook** — documento de governo. | — |
| #tipo/research | 2026-09-17 | Arquitecto (para T003) | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T003-modelo-solar/research/02-CAPTURA-3D-ESTADO-DA-ARTE\|Captura 3D com telemóvel — estado da arte]] | [[30-THREADS/T003-modelo-solar/research/02-CAPTURA-3D-ESTADO-DA-ARTE.md\|02-CAPTURA-3D-ESTADO-DA-ARTE.md]] · — sem PDF | **Contraria o enunciado do próprio pedido:** para a altura dos muros a captura 3D é a ferramenta errada e **um telémetro laser de 20–40 € é objectivamente superior** (±1,5 mm). A captura 3D só ganha nas copas. **Não foi ao notebook** — `[não apurado]` se chegou a ser proposta. | — |

## 2026-09-17 · «2026.09.17 - Arquiteto - Pesquisa de Catalogacao»
#dono/arquitecto

Primeira consolidação de documentação do notebook (G32–G35), executada no mesmo dia.
Documento de governo — não subiu ao notebook por não ser matéria de estudo.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/outros | 2026-09-17 | Arquitecto | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[CONSOLIDACAO-NOTEBOOKLM-2026-09-17\|Consolidação NotebookLM 2026-09-17]] | [[CONSOLIDACAO-NOTEBOOKLM-2026-09-17.md\|CONSOLIDACAO-NOTEBOOKLM-2026-09-17.md]] · — sem PDF | Auditoria às 9 sources e 11 artefactos. **Executada:** 4 sources e 3 decks eliminados, 11 objectos renomeados. Achado grave: a `Analise_Decisao_Betonilha` está **revogada** — a betonilha não se demole. Expôs a lacuna que criou o cargo `DVD`. **Não foi ao notebook** — documento de governo. | — |

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 2 DE 4 — THREADS                                             -->
<!-- Um H2 por thread. Dentro de cada thread, blocos de sessão H3.              -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 2 · THREADS

## T001 · local

### 2026-09-14 · `[não apurado]`
#dono/t001

Documentos herdados da migração, depositados em `T001-local/research/` antes de a thread ter
sessão própria. Datas do front matter; nome da sessão não registado em lado nenhum.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/dossier | 2026-09-14 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/Planta_e_Espaco_Fisico\|Planta e Espaço Físico — documento-mestre]] | [[30-THREADS/T001-local/research/Planta_e_Espaco_Fisico.md\|Planta_e_Espaco_Fisico.md]] · — sem PDF | Documento-mestre do espaço físico: geometria, cotas, **nomenclatura oficial dos muros**, árvores e zona hot tub. Declarado `canon: true`, `precedencia: 1`. **Superado pelo DOSSIER-LOCAL** como peça de consulta. | — |
| #tipo/research | 2026-09-14 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/Jardim_Analise_Decisao_Betonilha\|Análise — demolir ou manter a betonilha]] | [[30-THREADS/T001-local/research/Jardim_Analise_Decisao_Betonilha.md\|Jardim_Analise_Decisao_Betonilha.md]] · — sem PDF | Reenquadra demolir-vs-manter como **questão hidráulica sobre o muro de suporte sul**, com 4 opções e recomendação faseada. **Revogado:** o `ESTADO.md` decidiu a 2026-09-17 que a betonilha não se demole. Source eliminada do notebook a 2026-09-17. | — |

### 2026-09-15 · `[não apurado]`
#dono/t001

Sessão 1 da T001, etapa 1 do mandato: três pesquisas de fundo, um inventário, uma auditoria de
coerência e o dossier canónico que ficou como produto. Quatro subiram ao notebook, em datas
posteriores.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/dossier | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL\|Dossier técnico do Local]] | [[30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL.md\|DOSSIER-LOCAL.md]] · — sem PDF | **O documento canónico do Local**, declarado em `ESTADO.md` §01: 14 secções, semáforo de fiabilidade por secção, índice de 49 imagens, e secções 12–13 com o que falta e o que está em contradição. **Nenhum valor é novo** — deriva do `Planta_e_Espaco_Fisico.md`. | — |
| #tipo/research | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/Estado_Arte_Caracterizacao_Espaco_Exterior\|Estado da arte — caracterização de espaço exterior privado]] | [[30-THREADS/T001-local/research/Estado_Arte_Caracterizacao_Espaco_Exterior.md\|Estado_Arte_Caracterizacao_Espaco_Exterior.md]] · — sem PDF | Estado da arte em levantamento de espaço exterior privado, com **ficha-modelo de campos e sequência de levantamento**. Produzido por subagente sem ferramenta de escrita — o texto foi redigido do relatório devolvido, sem acrescentar fontes. | — |
| #tipo/research | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/Jardim_Catalogo_Vegetal\|Catálogo de espécies vegetais viáveis]] | [[30-THREADS/T001-local/research/Jardim_Catalogo_Vegetal.md\|Jardim_Catalogo_Vegetal.md]] · — sem PDF | Que espécies **podem** lá viver — sem recomendação de escolha nem composição. Conclui que o filtro decisivo é **só haver sol de tarde**, o que elimina toda a paleta construída sobre *«morning sun, afternoon shade»*. No notebook como `T001-26-09-15-RESEARCH-CATALOGO-VEGETAL`; **PDF de deck não descarregado**. | — |
| #tipo/research | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade\|Relva natural — relatório de investigação]] | [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade.md\|Jardim_Relva_Natural_Viabilidade.md]] · [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade_slides.pdf\|Jardim_Relva_Natural_Viabilidade_slides.pdf]] | Viabilidade de relva natural em 75,1 m² fechados, com veredicto de abertura e convenção `[F]`/`[M]`/`[E]` em cada número. **É o relatório completo com fontes que supera a pesquisa de 2026-09-14 do David.** No notebook como `T001-26-09-15-RESEARCH-RELVA-VIABILIDADE`. | — |
| #tipo/research | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/Jardim_Software_Modelacao_Solar\|Software para modelar exposição solar]] | [[30-THREADS/T001-local/research/Jardim_Software_Modelacao_Solar.md\|Jardim_Software_Modelacao_Solar.md]] · — sem PDF | Como obter **DLI por zona e por estação** num quintal fechado por fachada de 15,50 m a NE. Fundamentou a rejeição da via Google 3D. No notebook como `T001-26-09-15-RESEARCH-SOFTWARE-MODELACAO-SOLAR`; **PDF de deck não descarregado**. | — |
| #tipo/outros | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/INVENTARIO-DOCS-DAVID-LOCAL\|Inventário exaustivo de Docs-David-Local]] | [[30-THREADS/T001-local/research/INVENTARIO-DOCS-DAVID-LOCAL.md\|INVENTARIO-DOCS-DAVID-LOCAL.md]] · — sem PDF | Inventário do material bruto do David na pasta do Local, confrontado com o que o documento canónico referencia. **Uma das duas fontes do DOSSIER-LOCAL.** Não foi ao notebook — material de arrumação. | — |
| #tipo/outros | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/research/AUDITORIA-COERENCIA-T001\|Auditoria de coerência da T001]] | [[30-THREADS/T001-local/research/AUDITORIA-COERENCIA-T001.md\|AUDITORIA-COERENCIA-T001.md]] · — sem PDF | Auditoria da pasta inteira contra o protocolo. **Diagnóstico e proposta — não executa nada.** Origem das correcções de arrumação da sessão. Não foi ao notebook — documento de método. | — |
| #tipo/nota | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/entregue/NOTA-entregue-etapa1\|Nota de entrega da etapa 1]] | [[30-THREADS/T001-local/entregue/NOTA-entregue-etapa1.md\|NOTA-entregue-etapa1.md]] · — sem PDF | Declara a etapa 1 cumprida e **levanta o bloqueio da T002**. Regista que o produto **não vive em `entregue/`** mas em `Docs-David-Local/`, junto às ~50 imagens que referencia, para não partir 25 ligações. | — |
| #tipo/nota | 2026-09-15 | T001 | `[não apurado]` | [[30-THREADS/T001-local/Docs-David-Local/arqueologia/NOTA\|Nota de arqueologia — Docs-David-Local]] | [[30-THREADS/T001-local/Docs-David-Local/arqueologia/NOTA.md\|NOTA.md]] · — sem PDF | Regista o que foi movido para arqueologia dentro da pasta do Local e com que regra: **nada foi apagado, nada saiu de `Docs-David-Local/`**. Acompanha duas versões antigas do `Planta_e_Espaco_Fisico`. | — |

## T002 · jardim-v2

### 2026-09-16 · `[não apurado]`
#dono/t002

Sessão 1 da T002: registo das hipóteses e das ideias do David antes de qualquer análise, pedido
de quantificação à T003, zonamento de trabalho e estimativa solar própria. Nenhum ao notebook.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/nota | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/research/01-HIPOTESES-NA-MESA\|Hipóteses na mesa — T002 sessão 1]] | [[30-THREADS/T002-jardim-v2/research/01-HIPOTESES-NA-MESA.md\|01-HIPOTESES-NA-MESA.md]] · — sem PDF | Regista o que o David pôs na mesa **antes** de análise, com etiqueta de proveniência por afirmação. Conclui o essencial: **três momentos de decisão, execução no terreno zero**. Hipótese H3 ficou por enunciar. | — |
| #tipo/nota | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/research/02-IDEIAS-DAVID-SESSAO1\|Ideias do David — sessão 1]] | [[30-THREADS/T002-jardim-v2/research/02-IDEIAS-DAVID-SESSAO1.md\|02-IDEIAS-DAVID-SESSAO1.md]] · — sem PDF | Registo em bruto das ideias do David, por analisar. Traz uma **observação nova do local**: o canteiro NW produz e o canteiro SE não. | — |
| #tipo/nota | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/research/03-PEDIDO-T003-COTA\|Pedido à T003 — a luz e a subida de cota]] | [[30-THREADS/T002-jardim-v2/research/03-PEDIDO-T003-COTA.md\|03-PEDIDO-T003-COTA.md]] · — sem PDF | Pedido formal de quantificação à T003: **o que muda na luz quando o jardim sobe 0,50 m**. Ficou `por encaminhar pelo Arquitecto` — é a razão de existir a estimativa própria da T002. | — |
| #tipo/nota | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/research/04-ZONAMENTO-PRESSUPOSTO\|Zonamento de intervenção — pressuposto de trabalho]] | [[30-THREADS/T002-jardim-v2/research/04-ZONAMENTO-PRESSUPOSTO.md\|04-ZONAMENTO-PRESSUPOSTO.md]] · — sem PDF | Zonamento provisório da thread, com argumento de porque **não se usam as zonas Z1–Z5 herdadas**. **Substituído a 2026-09-17** pelo zonamento do David; mantido como histórico. | — |
| #tipo/nota | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/research/05-LUZ-COTA-ESTIMATIVA-T002\|Ticket 1 — a luz muda com a subida de cota?]] | [[30-THREADS/T002-jardim-v2/research/05-LUZ-COTA-ESTIMATIVA-T002.md\|05-LUZ-COTA-ESTIMATIVA-T002.md]] · — sem PDF | Quantificação solar por modelo geométrico próprio, feita porque o pedido à T003 não foi encaminhado. **Todos os valores são `[estimado pela T002, a confirmar pela T003]`** e nenhum entra em `ESTADO.md` sem substituição ou sem a etiqueta colada. | — |
| #tipo/nota | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/David-Docs/INDICE\|Índice de David-Docs · T002]] | [[30-THREADS/T002-jardim-v2/David-Docs/INDICE.md\|INDICE.md]] · — sem PDF | Índice do material entregue pelo David à T002 na sessão 1 — imagens e plantas anotadas que servem de fonte gráfica aos documentos da thread. | — |
| #tipo/outros | 2026-09-16 | T002 | `[não apurado]` | [[30-THREADS/T002-jardim-v2/TICKETS\|Tickets — T002]] | [[30-THREADS/T002-jardim-v2/TICKETS.md\|TICKETS.md]] · — sem PDF | Quadro de tickets operacionais e de propostas de thread da T002. Instrumento de gestão interna da thread, mantido aberto. | — |

### 2026-09-17 · «2026.09.16 - T002 S2 e T004 S1»
#dono/t002

Sessão 2 e última da T002: o David traz uma base de projecto completa, a thread reformula o
problema, fixa o zonamento dele, escreve a explicação do local, propõe a T004 e entrega.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/nota | 2026-09-17 | T002 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T002-jardim-v2/research/06-PROJECTO-REFORMULADO-VISTA\|O projecto reformulado — um problema de vista]] | [[30-THREADS/T002-jardim-v2/research/06-PROJECTO-REFORMULADO-VISTA.md\|06-PROJECTO-REFORMULADO-VISTA.md]] · — sem PDF | **Reenquadra o projecto: não é um problema de jardim, é um problema de vista.** Fixado pelo David — a marquise sai, o envidraçado entra, e o jardim deixa de estar 1,35 m abaixo e atrás de barreira opaca. | — |
| #tipo/nota | 2026-09-17 | T002 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T002-jardim-v2/research/07-ZONAMENTO-DAVID\|Zonamento — seis zonas, do David]] | [[30-THREADS/T002-jardim-v2/research/07-ZONAMENTO-DAVID.md\|07-ZONAMENTO-DAVID.md]] · — sem PDF | **Zonamento oficial da thread, fixado pelo David** a partir de planta anotada: seis zonas. Substitui o pressuposto de trabalho da sessão 1. | — |
| #tipo/nota | 2026-09-17 | T002 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T002-jardim-v2/research/08-EXPLICACAO-DO-LOCAL\|A explicação do local]] | [[30-THREADS/T002-jardim-v2/research/08-EXPLICACAO-DO-LOCAL.md\|08-EXPLICACAO-DO-LOCAL.md]] · — sem PDF | **A T001 diz o que o local é; este diz o que o local significa** — porque é que quatro planos tecnicamente viáveis morreram. Explicitamente **não é caracterização**: onde divergir do dossier, o dossier ganha. | — |
| #tipo/nota | 2026-09-17 | T002 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T002-jardim-v2/entregue/NOTA\|Nota de entrega — T002 · Jardim V2]] | [[30-THREADS/T002-jardim-v2/entregue/NOTA.md\|NOTA.md]] · — sem PDF | **Declara um desvio ao mandato literal:** a thread não entrega duas a quatro opções, entrega o que as tornou desnecessárias — a base de projecto do David. Encontrou três erros, **dois da própria thread**. Entrega absorvida; thread fechada. | — |
| #tipo/nota | 2026-09-17 | T002 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T002-jardim-v2/entregue/PROPOSTA-T004\|Proposta — T004 · A Geometria do Jardim]] | [[30-THREADS/T002-jardim-v2/entregue/PROPOSTA-T004.md\|PROPOSTA-T004.md]] · — sem PDF | Mandato da T004 redigido pela T002 a pedido do David. **Ratificado pelo Arquitecto sem alterações** — é o mandato vigente da thread do caminho crítico. | — |
| #tipo/outros | 2026-09-17 | T002 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T002-jardim-v2/ARRUMACAO\|Arrumação — instruções de sessão T002]] | [[30-THREADS/T002-jardim-v2/ARRUMACAO.md\|ARRUMACAO.md]] · — sem PDF | Ficheiro **declaradamente temporário** com as instruções de arrumação da sessão, estado `por executar`. Registado por estar em disco (§7.7 das instruções), não por ser matéria de projecto. | — |

## T003 · modelo-solar

*(sem entradas próprias — a thread tem `sessoes: 0`. Os documentos da sua pasta foram produzidos pelo Arquitecto e estão em [[#1 · ARQUITECTO]].)*

## T004 · geometria

### 2026-09-17 · «2026.09.16 - T002 S2 e T004 S1»
#dono/t004

Sessão 1 da T004: enunciado do desnível, duas pesquisas com fontes, a transição fixada em
geometria, e dois achados sobre as copas — um deles a bloquear a obra. Nenhum ao notebook.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/nota | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/01-O-DESNIVEL-ENUNCIADO\|O desnível — enunciado do problema]] | [[30-THREADS/T004-geometria/research/01-O-DESNIVEL-ENUNCIADO.md\|01-O-DESNIVEL-ENUNCIADO.md]] · — sem PDF | Enuncia o primeiro grande desafio da thread a partir do que o David fixou e dos dados do jacuzzi: **vencer o desnível sem cortar o jardim em dois**. | — |
| #tipo/research | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/02-PESQUISA-TRANSICOES\|Pesquisa — tipologias de transição de cota]] | [[30-THREADS/T004-geometria/research/02-PESQUISA-TRANSICOES.md\|02-PESQUISA-TRANSICOES.md]] · — sem PDF | Tipologias para vencer 0,85 m em 5,78 m de largura, cada uma com fonte. Achado de método: **não existe precedente publicado para este caso — é um vazio de documentação pública**, e a solução tem de ser composta de princípios, não copiada. | — |
| #tipo/nota | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/03-SOLUCAO-TRANSICAO\|A transição — degrau-banco com escada no muro SE]] | [[30-THREADS/T004-geometria/research/03-SOLUCAO-TRANSICAO.md\|03-SOLUCAO-TRANSICAO.md]] · — sem PDF | Primeira geometria da transição, a partir da restrição posta pelo David. Tipologia decidida por ele, cálculo da thread. **Superada na mesma sessão** pela versão fixada. | — |
| #tipo/nota | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/04-TRANSICAO-FIXADA\|A transição — geometria fixada]] | [[30-THREADS/T004-geometria/research/04-TRANSICAO-FIXADA.md\|04-TRANSICAO-FIXADA.md]] · — sem PDF | **Fecha metade do mandato da T004.** De três iterações do David ganha a C — jacuzzi em maciço, topo ao nível da plataforma — **e a razão é estrutural, não estética**: o maciço que eleva a água aloja o equipamento e suporta a escada. | — |
| #tipo/research | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/05-PESQUISA-VEGETACAO\|Pesquisa — o que plantar em cada zona]] | [[30-THREADS/T004-geometria/research/05-PESQUISA-VEGETACAO.md\|05-PESQUISA-VEGETACAO.md]] · — sem PDF | Vegetação zona a zona, relva e iluminação, com cinco conclusões que mudam decisões. Declara o limite: **para a zona sob a palmeira não existe literatura publicada, só evidência de fórum**. Fora do mandato estrito — fica como matéria-prima. | — |
| #tipo/nota | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/06-O-PROBLEMA-DAS-COPAS\|As copas — metade do jardim está por baixo delas]] | [[30-THREADS/T004-geometria/research/06-O-PROBLEMA-DAS-COPAS.md\|06-O-PROBLEMA-DAS-COPAS.md]] · — sem PDF | **Achado urgente: o tronco do lodão fica dentro da faixa onde o maciço vai ser construído.** Nenhum desenho o apanhou porque a faixa foi definida em X sem verificação de colisão — **falhanço de método assumido pela thread**. | — |
| #tipo/nota | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/research/07-ARVORES-POSICAO-E-COPAS\|As árvores — posição, copas e consequências]] | [[30-THREADS/T004-geometria/research/07-ARVORES-POSICAO-E-COPAS.md\|07-ARVORES-POSICAO-E-COPAS.md]] · — sem PDF | **São quatro árvores**, não as que se supunha. Valores de referência fixados pelo David — **inferidos de fotografias, não medidos** — que substituem os do dossier onde divergirem, por serem mais recentes e virem com planta anotada. | — |
| #tipo/outros | 2026-09-17 | T004 | «2026.09.16 - T002 S2 e T004 S1» | [[30-THREADS/T004-geometria/ARRUMACAO\|Arrumação — instruções de sessão T004]] | [[30-THREADS/T004-geometria/ARRUMACAO.md\|ARRUMACAO.md]] · — sem PDF | Ficheiro **declaradamente temporário** com as instruções de arrumação da sessão, estado `por executar`. Registado por estar em disco, não por ser matéria de projecto. | — |

## T005 · caracterizacao

### 2026-09-17 · «2026.09.17 - Arquiteto - Pesquisa de Catalogacao»
#dono/t005

Fase 1 da T005: uma análise prévia, quatro pesquisas em paralelo sem conhecimento umas das
outras, uma síntese que as cruza e um report. **Quatro subiram ao notebook** — três pesquisas
e a síntese — com PDF de deck descarregado para junto do original.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/outros | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/research/00-PONTO-DE-PARTIDA\|Ponto de partida — o que o projecto já tem]] | [[30-THREADS/T005-caracterizacao/research/00-PONTO-DE-PARTIDA.md\|00-PONTO-DE-PARTIDA.md]] · — sem PDF | Escrito **antes** de as pesquisas chegarem. Diagnostica que **o dossier está organizado por objecto físico e não por disciplina**, e por isso não sabe responder a «isto está caracterizado?». Fixou o teste de falsificação da thread. **Não foi ao notebook** — método interno. | — |
| #tipo/research | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES\|Especialidades técnicas na caracterização]] | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md\|01-ESPECIALIDADES.md]] · [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf\|T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf]] | **16 disciplinas** com método, norma, fase e decisões bloqueadas. Achado central: **isto é tecnicamente uma cobertura ajardinada intensiva (FLL)**, o que activa um corpo normativo ausente do vocabulário do projecto. A matriz final isola a tensão retenção-vs-drenagem. | — |
| #tipo/research | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE\|Software para digital twin do jardim]] | [[30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE.md\|02-DIGITAL-TWIN-SOFTWARE.md]] · — sem PDF | Nove eixos de software. Conclui que **não existe plataforma única de «digital twin» a esta escala** — é uma combinação de 3-5 ferramentas ligadas por Python. Recomenda Rhino + Grasshopper + Ladybug/Honeybee. **Não foi ao notebook** — material de decisão de compra, para consultar quando for altura. | — |
| #tipo/research | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO\|Monitorização e actuação em contínuo]] | [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO.md\|03-MONITORIZACAO-ACTUACAO.md]] · [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-MONITORIZACAO-ACTUACAO.pdf\|T005-26-09-17-RESEARCH-MONITORIZACAO-ACTUACAO.pdf]] | **A humidade do substrato é o parâmetro mestre** — o único cuja falha mata plantas em dias. Achado de maior valor: **detecção acústica precoce do escaravelho da palmeira, >90%** em ensaios publicados, mas sem produto comercial confirmado em Portugal. Recomenda sistema mínimo local, sem cloud. | — |
| #tipo/research | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS\|Nuvem de pontos com equipamento profissional]] | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS.md\|04-NUVEM-DE-PONTOS.md]] · [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-NUVEM-DE-PONTOS.pdf\|T005-26-09-17-RESEARCH-NUVEM-DE-PONTOS.pdf]] | **Veredicto dividido:** vale para a copa da palmeira, não se justifica para a cota dos muros — que um telémetro de 30 € resolve a ±1,5 mm. **Inversão de intuição:** o reboco liso é o pior caso para fotogrametria e um dos melhores para TLS. Cadeia open source completa em CloudCompare. | — |
| #tipo/sintese | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1\|Síntese da fase 1]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] · [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-SINTESE-FASE-1.pdf\|T005-26-09-17-SINTESE-FASE-1.pdf]] | **Três pesquisas convergiram, sem combinação, na mesma reclassificação: o jardim sobre laje é uma cobertura ajardinada.** Isola o conflito retenção-vs-drenagem como o compromisso não resolvido mais valioso, e a tripla razão do bloqueio da palmeira. Sinalizou à T004 a decomposição dos +0,50 m como urgente. | — |
| #tipo/report | 2026-09-17 | T005 | «2026.09.17 - Arquiteto - Pesquisa de Catalogacao» | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA\|Report da fase 1 da T005]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] · — sem PDF | Report com prompts, **grau de certeza declarado por bloco** — nulo para espessuras de camadas, baixo para preços — quatro tensões por resolver e próximos passos. **Não foi ao notebook** — sobrepõe-se à síntese, que foi. | — |

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 3 DE 4 — DAVID                                               -->
<!-- Material do cargo DVD. Heading = data de CATALOGAÇÃO, não de produção.     -->
<!-- Obrigações prévias: G36 (ler · front matter · prompt · confrontar · G27).  -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 3 · DAVID

## 2026-09-17 · Catalogação — (sem sessão)
#dono/david

Pesquisa autónoma do David, feita fora de qualquer sessão e arrumada por ele em
`40-PESQUISAS/David/`. **Tem ficheiro no repositório, logo tem wikilink.** A primeira
responde a uma questão que a T005 tinha acabado de sinalizar como urgente.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/research | 2026-09-17 | David | — (sem sessão) | [[40-PESQUISAS/David/2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA\|Sistemas de cobertura ajardinada]] | [[40-PESQUISAS/David/2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md\|2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md]] · — sem PDF | **Responde à decomposição dos +0,50 m em camadas** que a T005 sinalizou à T004 como urgente: espessuras FLL/ZinCo/Optigreen, substratos leves com densidade seca **e saturada**, sobrecarga em kPa, e 2-3 secções-tipo com peso e custo por m². **Inclui o prompt integral.** No notebook como `DVD-26-09-17-RESEARCH-COBERTURA-AJARDINADA-FLL`. | — |
| #tipo/research | 2026-09-14 | David | — (sem sessão) | [[40-PESQUISAS/David/2026-09-14-Research-Relva_Natural_vs_Artificial\|Relva natural vs. artificial]] | [[40-PESQUISAS/David/2026-09-14-Research-Relva_Natural_vs_Artificial.md\|2026-09-14-Research-Relva_Natural_vs_Artificial.md]] · — sem PDF | Espécies, sombra, execução, manutenção e custos. **Assenta em premissas hoje corrigidas** — muros a 3 m (são 2,50) e cota 1,60 m. **Superado** pelo relatório completo da T001. Source eliminada do notebook a 2026-09-17 por estar superada. | — |

> **Os prompts ficam com os documentos.** O David guardou o prompt **dentro** do primeiro
> ficheiro, antes do relatório. **É a prática certa e adopta-se:** um relatório sem o prompt
> que o gerou não é auditável.
>
> **Premissa a conhecer:** o prompt do primeiro documento descreve a betonilha como
> «EMPOÇA água» — **corrigido desde 2026-09-16** (o quintal escoa; `ESTADO.md` §01).
> **Não invalida o relatório** — as espessuras e pesos FLL não dependem disso.

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 4 DE 4 — OUTROS                                              -->
<!-- O que não cabe acima: terceiros, documentos herdados, arqueologia.         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 4 · OUTROS

## 2026-09-18 · Catalogação — (sem sessão)
#dono/outros

Material de terceiros e material herdado, catalogado na migração para a estrutura nova.
`90-ARQUEOLOGIA/` é só de leitura (G19) — regista-se para constar que existe, não como
decisão vigente (G20).

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/outros | 2026-02 `[dia não apurado]` | Outros | — (sem sessão) | [[10-EQUIPA/adriano/proposta_adriano_Fev2026\|Proposta do Adriano — Fev 2026]] | [[10-EQUIPA/adriano/proposta_adriano_Fev2026.md\|proposta_adriano_Fev2026.md]] · — sem PDF | Proposta comercial de terceiro, recebida em Fevereiro de 2026. **Documento de origem externa** — não tem front matter e a data exacta não consta do corpo. Não foi ao notebook. | — |
| #tipo/outros | s/d | Outros | — (sem sessão) | [[10-EQUIPA/adriano/resposta_david_pedido_proposta\|Resposta do David ao pedido de proposta]] | [[10-EQUIPA/adriano/resposta_david_pedido_proposta.md\|resposta_david_pedido_proposta.md]] · — sem PDF | Correspondência do David com o Adriano. **Data desconhecida** — sem front matter e sem data no corpo. Registado como artefacto de equipa; não foi ao notebook. | — |
| #tipo/outros | s/d | Outros | — (sem sessão) | [[90-ARQUEOLOGIA/V1-completo/Jardim_Alcantara_Knowledge_Base\|Knowledge Base do Jardim V1]] | [[90-ARQUEOLOGIA/V1-completo/Jardim_Alcantara_Knowledge_Base.md\|Jardim_Alcantara_Knowledge_Base.md]] · — sem PDF | Base de conhecimento do projecto V1, hoje em arqueologia. **Só leitura (G19) e não é decisão vigente (G20).** Data não apurada — material herdado da migração. | — |
| #tipo/outros | s/d | Outros | — (sem sessão) | [[90-ARQUEOLOGIA/V1-completo/Jardim_Alcantara_Anexos\|Anexos do Jardim V1]] | [[90-ARQUEOLOGIA/V1-completo/Jardim_Alcantara_Anexos.md\|Jardim_Alcantara_Anexos.md]] · — sem PDF | Anexos do V1. **Só leitura, não é decisão vigente.** Data não apurada. | — |
| #tipo/outros | s/d | Outros | — (sem sessão) | [[90-ARQUEOLOGIA/V1-completo/resumo-notion-jardim\|Resumo Notion — Jardim V1]] | [[90-ARQUEOLOGIA/V1-completo/resumo-notion-jardim.md\|resumo-notion-jardim.md]] · — sem PDF | Exportação de resumo do Notion referente ao V1. **Só leitura, não é decisão vigente.** Data não apurada. | — |
| #tipo/outros | s/d | Outros | — (sem sessão) | [[90-ARQUEOLOGIA/DIY/resumo-notion-jardimtemporario\|Resumo Notion — jardim temporário DIY]] | [[90-ARQUEOLOGIA/DIY/resumo-notion-jardimtemporario.md\|resumo-notion-jardimtemporario.md]] · — sem PDF | Exportação do Notion referente ao jardim DIY temporário. **Só leitura, não é decisão vigente.** Data não apurada. | — |
| #tipo/outros | 2026-09-14 | Outros | — (sem sessão) | [[90-ARQUEOLOGIA/migracao-2026-09-14/MIGRACAO_2026-09-14\|Migração 2026-09-14]] | [[90-ARQUEOLOGIA/migracao-2026-09-14/MIGRACAO_2026-09-14.md\|MIGRACAO_2026-09-14.md]] · — sem PDF | Registo da migração da knowledge base para o repositório local, a 2026-09-14. **Só leitura.** Acompanhado de `worklog.md` na mesma pasta. | — |
| #tipo/outros | 2026-09-14 | Outros | — (sem sessão) | [[90-ARQUEOLOGIA/migracao-2026-09-14/worklog\|Worklog da migração]] | [[90-ARQUEOLOGIA/migracao-2026-09-14/worklog.md\|worklog.md]] · — sem PDF | Diário de execução da migração de 2026-09-14. **Só leitura.** | — |
| #tipo/dossier | 2026-09-15 | Outros | — (sem sessão) | [[30-THREADS/T001-local/Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico\|Planta e Espaço Físico — rev. 16:30]] | [[30-THREADS/T001-local/Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico.md\|Planta_e_Espaco_Fisico.md]] · — sem PDF | Revisão de 2026-09-15 16:30 do documento-mestre, com drenagem acrescentada. **É a fonte declarada do DOSSIER-LOCAL.** Movida para arqueologia interna da T001; conservada, não apagada. | — |
| #tipo/dossier | 2026-09-15 | Outros | — (sem sessão) | [[30-THREADS/T001-local/Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico.BACKUP-20260915\|Planta e Espaço Físico — backup]] | [[30-THREADS/T001-local/Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico.BACKUP-20260915.md\|Planta_e_Espaco_Fisico.BACKUP-20260915.md]] · — sem PDF | Cópia de segurança anterior à revisão das 16:30, sem a secção de drenagem. **Conservada por higiene**, não por valor de consulta. | — |

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ÚNICA SECÇÃO EDITÁVEL DESTE FICHEIRO — excepção declarada ao G24.          -->
<!-- Fora daqui, o append-only é absoluto.                                      -->
<!-- Lê-se: FONTE → foi usada por → CONSUMIDOR.                                 -->
<!-- Natureza (fechado): Síntese · Fonte externa citada · Substituição ·        -->
<!--                     Refutação · Deck NotebookLM                            -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Dependências entre documentos

> **Esta secção — e só esta — é editável.** Toda a dependência descoberta *depois* de a
> linha do documento ter sido escrita regista-se aqui, não na coluna `Supported`.
> Razão da regra: `REGISTO-DOCUMENTOS-INSTRUCOES.md` §6.

| Data do registo | Fonte | Usada por | Natureza |
|---|---|---|---|
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/00-PONTO-DE-PARTIDA.md\|00-PONTO-DE-PARTIDA.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md\|01-ESPECIALIDADES.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE.md\|02-DIGITAL-TWIN-SOFTWARE.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO.md\|03-MONITORIZACAO-ACTUACAO.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS.md\|04-NUVEM-DE-PONTOS.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/00-PONTO-DE-PARTIDA.md\|00-PONTO-DE-PARTIDA.md]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md\|01-ESPECIALIDADES.md]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE.md\|02-DIGITAL-TWIN-SOFTWARE.md]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO.md\|03-MONITORIZACAO-ACTUACAO.md]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS.md\|04-NUVEM-DE-PONTOS.md]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | [[30-THREADS/T005-caracterizacao/reports/2026-09-17-T005-REPORT-FASE-1-PESQUISA.md\|2026-09-17-T005-REPORT-FASE-1-PESQUISA.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md\|01-ESPECIALIDADES.md]] | [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf\|T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf]] | Deck NotebookLM |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO.md\|03-MONITORIZACAO-ACTUACAO.md]] | [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-MONITORIZACAO-ACTUACAO.pdf\|T005-26-09-17-RESEARCH-MONITORIZACAO-ACTUACAO.pdf]] | Deck NotebookLM |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS.md\|04-NUVEM-DE-PONTOS.md]] | [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-NUVEM-DE-PONTOS.pdf\|T005-26-09-17-RESEARCH-NUVEM-DE-PONTOS.pdf]] | Deck NotebookLM |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-SINTESE-FASE-1.pdf\|T005-26-09-17-SINTESE-FASE-1.pdf]] | Deck NotebookLM |
| 2026-09-18 | [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade.md\|Jardim_Relva_Natural_Viabilidade.md]] | [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade_slides.pdf\|Jardim_Relva_Natural_Viabilidade_slides.pdf]] | Deck NotebookLM |
| 2026-09-18 | [[CONSOLIDACAO-NOTEBOOKLM-2026-09-17.md\|CONSOLIDACAO-NOTEBOOKLM-2026-09-17.md]] | — analisou o conteúdo integral do notebook, não um documento em particular | Fonte externa citada |
| 2026-09-18 | [[40-PESQUISAS/David/2026-09-14-Research-Relva_Natural_vs_Artificial.md\|2026-09-14-Research-Relva_Natural_vs_Artificial.md]] | [[30-THREADS/T001-local/research/Jardim_Relva_Natural_Viabilidade.md\|Jardim_Relva_Natural_Viabilidade.md]] | Substituição |
| 2026-09-18 | [[30-THREADS/T001-local/research/Jardim_Software_Modelacao_Solar.md\|Jardim_Software_Modelacao_Solar.md]] | [[30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS.md\|04-NUVEM-DE-PONTOS.md]] | Fonte externa citada |
| 2026-09-18 | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | [[40-PESQUISAS/David/2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md\|2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md]] | Fonte externa citada |
| 2026-09-18 | [[30-THREADS/T001-local/research/Planta_e_Espaco_Fisico.md\|Planta_e_Espaco_Fisico.md]] | [[30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL.md\|DOSSIER-LOCAL.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T001-local/research/INVENTARIO-DOCS-DAVID-LOCAL.md\|INVENTARIO-DOCS-DAVID-LOCAL.md]] | [[30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL.md\|DOSSIER-LOCAL.md]] | Síntese |
| 2026-09-18 | [[30-THREADS/T002-jardim-v2/research/04-ZONAMENTO-PRESSUPOSTO.md\|04-ZONAMENTO-PRESSUPOSTO.md]] | [[30-THREADS/T002-jardim-v2/research/07-ZONAMENTO-DAVID.md\|07-ZONAMENTO-DAVID.md]] | Substituição |
| 2026-09-18 | [[30-THREADS/T004-geometria/research/03-SOLUCAO-TRANSICAO.md\|03-SOLUCAO-TRANSICAO.md]] | [[30-THREADS/T004-geometria/research/04-TRANSICAO-FIXADA.md\|04-TRANSICAO-FIXADA.md]] | Substituição |
| 2026-09-18 | [[30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL.md\|DOSSIER-LOCAL.md]] | [[30-THREADS/T004-geometria/research/07-ARVORES-POSICAO-E-COPAS.md\|07-ARVORES-POSICAO-E-COPAS.md]] | Substituição |
| 2026-09-18 | [[30-THREADS/T002-jardim-v2/entregue/PROPOSTA-T004.md\|PROPOSTA-T004.md]] | [[30-THREADS/T004-geometria/thread.md\|thread.md]] | Fonte externa citada |
| 2026-09-18 | [[30-THREADS/T001-local/research/Jardim_Analise_Decisao_Betonilha.md\|Jardim_Analise_Decisao_Betonilha.md]] | [[CONSOLIDACAO-NOTEBOOKLM-2026-09-17.md\|CONSOLIDACAO-NOTEBOOKLM-2026-09-17.md]] | Refutação |

<!-- Notas de leitura sobre a tabela acima:
     · A linha da CONSOLIDACAO tem o campo "Usada por" em texto — a relação é
       documento → notebook inteiro, e o vocabulário fechado de Natureza não tem
       valor para isso. Assinalado nas Notas do draft.
     · A linha DOSSIER-LOCAL → 07-ARVORES é "Substituição" parcial: os valores das
       árvores do doc 07 substituem os do dossier ONDE DIVERGIREM, não o dossier todo.
-->

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- RODAPÉ — checklist de fim de sessão. Não se apaga.                         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Checklist de fim de sessão

```
[ ] Todos os documentos produzidos estão na tabela? (os que foram E os que não foram ao notebook)
[ ] As 8 colunas preenchidas, nenhuma vazia?
[ ] Tipo com tag #tipo/<valor> — e perguntado ao David se não era evidente?
[ ] Wikilinks com o `|` do alias escapado como `\|`?
[ ] PDF dos decks na pasta do documento de origem, com o nome certo? (G29)
[ ] Sumário de sessão, 1-3 linhas, antes da tabela?
[ ] Dependências novas na secção do fim?
[ ] Nada editado fora da secção de dependências?
```

---
---

## Notas do draft

> **Esta secção não pertence ao registo.** Existe só enquanto isto for draft.
> **Apagar ao instanciar `REGISTO-DOCUMENTOS.md`.**

### 1. O que não se conseguiu apurar

| # | O que falta | Porquê | Consequência |
|---|---|---|---|
| N1 | **Nomes das sessões Claude da T001 (S1, 2026-09-15), da T002 sessão 1 (2026-09-16), e da abertura da T003 (2026-09-15)** | Só duas sessões estão nomeadas em ficheiro em todo o repositório: `2026.09.16 - T002 S2 e T004 S1` (em `HANDOFF.md`, `AUDITORIA-2026-09-17.md` e nos quatro `thread.md`) e `2026.09.17 - Arquiteto - Pesquisa de Catalogacao`. As anteriores **nunca foram registadas** | 20 linhas com `[não apurado]` na coluna Sessão. **Só o David as pode recuperar**, do histórico do cliente Claude |
| N2 | **Datas dos ficheiros de `90-ARQUEOLOGIA/V1-completo/` e `DIY/`** | Nenhum tem front matter e nenhum declara data no corpo | Registados a `s/d`, conforme §4.2 |
| N3 | **Data de `resposta_david_pedido_proposta.md`** | Sem front matter, sem data no corpo | `s/d` |
| N4 | **Dia exacto de `proposta_adriano_Fev2026.md`** | O nome do ficheiro dá o mês; o corpo não dá o dia | `2026-02 [dia não apurado]` — **quebra o formato `AAAA-MM-DD` exigido pela §4.2**. Alternativa seria `s/d`, que perderia informação verdadeira. Decisão a confirmar |
| N5 | **Se a pesquisa `02-CAPTURA-3D-ESTADO-DA-ARTE` chegou a ser proposta para o notebook** | O registo antigo não a menciona de todo, e não há nota de recusa | Registada como não tendo ido, sem motivo declarado — **viola a regra 9 da §8**, que exige o motivo |
| N6 | **Porque é que os decks de `Jardim_Catalogo_Vegetal` e `Jardim_Software_Modelacao_Solar` não estão em disco** | As duas sources estão confirmadas no notebook (9 sources), mas não há PDF na pasta. Ou não foi gerado deck, ou foi gerado e não descarregado | Registado `— sem PDF` com nota no sumário. **É uma pendência de G29, não um erro de registo** |

### 2. Contradições entre as instruções e a realidade dos ficheiros

**C1 — «Um bloco de sessão» pressupõe que as sessões tenham nome; a maioria não tem.**
A §4.4 diz que o nome da sessão se escreve entre aspas angulares e que **nunca se inventa**, e
prevê `— (sem sessão)` para material do David. **Não prevê o caso maioritário deste
repositório:** sessão que existiu, produziu documentos, e cujo nome ninguém registou.
`— (sem sessão)` seria falso — houve sessão. Adoptou-se `[não apurado]`, seguindo a regra
deste pedido. **A §4.4 precisa de um terceiro valor.**

**C2 — O «Dono» da T003 é o Arquitecto, e a estrutura não tem sítio para isso.**
A T003 tem `sessoes: 0`. Os quatro documentos na sua pasta foram escritos pelo Arquitecto,
antes de a thread arrancar. Pela §7.1 — *um documento, um dono, o de quem o escreveu no fim* —
o dono é o Arquitecto, e é onde estão. Mas então **a pergunta «o que é que a T003 produziu?»,
que a §3.1(c) diz ser a razão de existir do índice de Donos, responde-se com uma remissão.**
Escreveu-se `Arquitecto (para T003)` na coluna Dono, por analogia com a notação `T004 (+T005)`
da §7.1. **É extensão de vocabulário, não está nas instruções.**

**C3 — A `Natureza` da dependência não cobre «documento que analisou o notebook inteiro».**
A dependência nº4 do pedido — *a consolidação analisou todo o conteúdo do notebook* — não tem
fonte que seja **um documento**. O vocabulário fechado da §6.3 tem cinco valores e nenhum
serve. Registou-se com o campo «Usada por» em texto simples e `Natureza: Fonte externa citada`.
**É a solução menos má, não é a certa.**

**C4 — `AUDITORIA-2026-09-17.md` não estava no registo antigo.**
Documento de governo na raiz, produzido pela sessão de 2026-09-16/17. Pela regra de ouro da §2
a sua ausência **era um bug**. Está corrigido neste draft.

### 3. Decisões de classificação duvidosas

| # | Documento | Hesitação | Decidido | Porquê |
|---|---|---|---|---|
| D1 | Os 7 documentos de `research/` da T002 e os 5 «não-pesquisa» da T004 | `#tipo/nota` vs `#tipo/outros` | **`#tipo/nota`** | São registos curtos e pontuais de estado de trabalho, sem pretensão de completude — definição literal da §4.1. Mas estão em `research/` e alguns têm 200+ linhas, o que puxa para `outros`. **Merece confirmação do David** |
| D2 | `04-TRANSICAO-FIXADA.md` e `07-ARVORES-POSICAO-E-COPAS.md` | `#tipo/nota` vs `#tipo/dossier` | **`#tipo/nota`** | São referência fixada para consulta futura — o que a §4.1 chama Dossier. Ficaram `nota` por coerência com os irmãos da mesma pasta. **A escolha é discutível nos dois sentidos** |
| D3 | `00-PONTO-DE-PARTIDA.md` | `#tipo/outros` vs `#tipo/nota` vs `#tipo/sintese` | **`#tipo/outros`** | O front matter diz `tipo: analise` — **valor que não existe no vocabulário fechado**. Cruza o material existente (puxa para síntese) mas conclui sobre método, não sobre matéria |
| D4 | `AUDITORIA-COERENCIA-T001.md` e `INVENTARIO-DOCS-DAVID-LOCAL.md` | `#tipo/outros` vs `#tipo/report` | **`#tipo/outros`** | Têm objectivo, método e achados — a definição de Report. Ficaram `outros` por serem auditoria/inventário, que a §4.1 nomeia expressamente em `Outros` |
| D5 | Os dois `ARRUMACAO.md` | Registar ou não | **Registados, `#tipo/outros`** | A §7.7 diz que é documento se ficou em disco no fim da sessão. Ficaram. Mas são **declaradamente temporários e para apagar** — registá-los enche o catálogo de lixo com data de validade. **Reversível** |
| D6 | `LEIA-ME-DAVID.md` (T003) | Dono `Arquitecto` vs `David` | **`Arquitecto`** | É escrito **para** o David, não **pelo** David. A §7.1 manda olhar para quem escreveu |
| D7 | `Planta_e_Espaco_Fisico.md` em arqueologia da T001 | Dono `T001` vs `Outros` | **`Outros`** | As duas cópias em `Docs-David-Local/arqueologia/` foram para lá **como arqueologia**, e a §3.2 diz que `4 · OUTROS` é onde vive a arqueologia. Mas a cópia de `research/` ficou em T001 — **duas cópias do mesmo documento em donos diferentes**, o que é feio e pode não ser o que o David quer |
| D8 | Ficheiros de governo de thread (`thread.md`, `CLAUDE.md`, `mensagens.md`) | Registar ou não | **Não registados** | São infra-estrutura de governo, não artefactos de projecto. **Se se registassem, o catálogo triplicava sem ganhar nada.** Vale o mesmo para os ficheiros de governo da raiz (`ESTADO.md`, `REJEICOES.md`, `INBOX.md`, `THREADS.md`, `HANDOFF.md`, `FLUXO-DE-PROJECTO.md`, `Jardim.html`) e para os três `ficha.md` de `10-EQUIPA/`. **É a decisão de maior impacto deste draft e não está nas instruções** |

### 4. O que as instruções não cobrem e apareceu na prática

**F1 — Não dizem onde param.** Não há critério escrito para distinguir **artefacto de projecto**
de **ficheiro de governo**. Aplicado ao pé da letra, «tudo o que o projecto produziu em forma
de documento» inclui o `ESTADO.md`, os cinco `CLAUDE.md` e os `mensagens.md` — 30+ linhas de
puro ruído. A decisão D8 acima é minha e **deve entrar nas instruções**, seja qual for.

**F2 — Não têm modo de migração.** Estão escritas para o fluxo *fim de sessão*: uma sessão
regista o que acabou de produzir. Não dizem como catalogar **retroactivamente** material de
sessões que já fecharam, o que é exactamente este exercício. Daí os dois buracos: nomes de
sessão e critério de tipo por documento antigo.

**F3 — Não dizem a que sessão pertence o material herdado.** A migração de 2026-09-14 trouxe
documentos para dentro de `T001-local/research/` que são anteriores à thread. Ficaram num
bloco `2026-09-14 · [não apurado]` dentro da T001, mas podiam legitimamente estar em `4 · OUTROS`.

**F4 — Não preveem o PDF que devia existir e não existe.** A §4.6 tem `— sem PDF` para «não
foi ao notebook». Não tem valor para **«foi ao notebook e o PDF não está cá»** — o caso das
duas sources da T001. Sugere-se `— PDF em falta` como sétimo valor, para a distinção não se
perder no sumário.

**F5 — A `Data` da coluna 2 e o heading do bloco de sessão divergem para material antigo.**
A §4.2 diz que a Data é a do documento e a §7.3 diz que o heading é a data de catalogação.
Para o `2026-09-14-Research-Relva_Natural_vs_Artificial.md` isso dá heading `2026-09-17` e
Data `2026-09-14` — correcto pelas regras, mas **lê-se mal** e convém um aviso nas instruções.

### 5. Contagem

| Dono | Documentos |
|---|---|
| Arquitecto | 7 |
| T001 | 11 |
| T002 | 13 |
| T003 | 0 (próprios) |
| T004 | 8 |
| T005 | 7 |
| David | 2 |
| Outros | 10 |
| **Total** | **58** |

**Registo antigo:** 9 documentos. **Este draft:** 58. A diferença não é zelo — **são 49
documentos que existiam no repositório e não estavam em catálogo nenhum.**

### Índices — correcção de 2026-09-18

Correcção isolada aos **índices do topo**. O corpo não foi tocado: verificado por `diff`, é
byte a byte idêntico ao draft anterior de `# 1 · ARQUITECTO` até ao fim do ficheiro.

**O que estava mal.** A secção **(d) Índice por Tipo** estava por preencher — era o esqueleto
do `REGISTO-DOCUMENTOS-TEMPLATE.md` copiado tal e qual: os seis headings de tipo, a linha de
descrição de cada um e o bloco Dataview comentado, **e mais nada**. Zero entradas, para 58
documentos catalogados no corpo. Era **a razão de ser da coluna `Tipo`** e não estava lá:
a pergunta que a §3.1(d) das instruções diz ser a função deste índice — *«mostra-me todas as
sínteses do projecto»* — não tinha resposta sem descer o ficheiro inteiro à mão.

**O que se fez.** Montaram-se os seis blocos com a agregação real, segundo a §5.2: mantém-se
a **tag** como primeira camada (funciona sem plugins), mantém-se o **Dataview comentado** como
andaime, e acrescenta-se a **tabela manual** — `Documento · Dono · Data` — que a §5.2 admite
como terceira camada «se o David a quiser». Justifica-se aqui porque a própria ressalva técnica
da §5.2 reconhece que, com tudo num só ficheiro, `FROM #tipo/x` devolve o ficheiro e não as
linhas: **sem a tabela manual este índice não agrega coisa nenhuma.** Ordenação por data
decrescente dentro de cada tipo, como manda o `SORT Data DESC` dos blocos Dataview.

**Contagem por tipo** — apurada por script sobre as linhas do corpo, não por leitura:

| Tipo | Documentos |
|---|---|
| Síntese | 1 |
| Report | 1 |
| Research | 14 |
| Dossier | 4 |
| Nota | 22 |
| Outros | 16 |
| **Total** | **58** |

**A soma bate certo com os 58** do corpo e com a contagem por Dono da secção 5 acima.

**Verificação feita (por script, não por inspecção visual):**

| Teste | Resultado |
|---|---|
| Linhas de documento no corpo | 58 |
| Entradas no índice por Tipo | 58 |
| Contagem por tipo, corpo vs. índice | Idêntica nos seis tipos |
| Documentos do corpo ausentes do índice | 0 |
| Entradas fantasma (no índice, não no corpo) | 0 |
| Documentos repetidos no índice | 0 |
| Wikilinks do índice que resolvem para ficheiro em disco | 58/58 |
| Wikilinks do corpo que resolvem para ficheiro em disco | 58/58 (reverificado) |
| `\|` de alias por escapar dentro de célula | 0 |
| Linhas do corpo com número de colunas ≠ 8 | 0 |

**Índice de Donos (c) — verificado, não alterado.** Os oito donos que aparecem no corpo estão
todos listados e cada link resolve para o heading correspondente: Arquitecto (3) · T001 (11) ·
T002 (13) · T004 (8) · T005 (7) · David (2) · Outros (10), mais os 4 de `Arquitecto (para T003)`,
que somam 58. **A T003 mantém-se no índice com zero documentos próprios** — os quatro que estão
na sua pasta são do Arquitecto, pela §7.1, e é exactamente a contradição **C2** já levantada
acima. Não se mexeu.

**Incoerências encontradas entre índice e corpo:** nenhuma. Os dois estão alinhados.

**O que não se resolveu, e porquê:**

- **I1 — `2026-02 [dia não apurado]` ordena mal.** A proposta do Adriano é a única entrada
  sem dia. No índice fica ordenada pelo prefixo `2026-02`, o que a coloca no sítio certo por
  acaso; se aparecer outro documento de Fevereiro, a ordem entre os dois é arbitrária. É
  consequência directa da pendência **N4** — não se decide aqui.
- **I2 — as quatro entradas `s/d` da arqueologia** ficam no fim do bloco `Outros`, que é o
  comportamento desejável, mas por convenção minha (`s/d` ordena como data mínima), não por
  regra escrita. **As instruções não dizem onde ordenar o `s/d`.**
- **I3 — o índice repete informação do corpo e pode desactualizar-se em silêncio.** É o risco
  que a §5.2 assinala para a lista manual. Mitigação possível: o script de verificação usado
  aqui pode ser guardado e corrido a cada consolidação. **Não se guardou — decisão do David.**
- **I4 — duas cópias do mesmo documento aparecem lado a lado no bloco Dossiers**
  (`Planta_e_Espaco_Fisico` em `research/` e em `arqueologia/`, com donos diferentes). O índice
  torna visível o que a decisão **D7** já tinha assinalado como feio. **Não se corrigiu** — é
  matéria do corpo.
- **I5 — erros do corpo não foram corrigidos**, por instrução expressa. Nenhum foi encontrado
  nesta passagem: colunas, escapes e links estão todos bons.
