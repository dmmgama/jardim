---
created: 2026-09-18
thread: T005
tipo: pesquisa
summary: |
  Levantamento de agentes de IA, skills, MCP servers e projectos open source adoptáveis
  para as áreas identificadas na fase 1 da T005. Três eixos: agentes especializados,
  open source para análise e estudo, e instrumentação/dados/automatização.

  O achado central é negativo e é o mais valioso: **não existe um único agente de IA
  especializado em jardim, arboricultura ou cobertura ajardinada que valha a pena adoptar.**
  O espaço «AI agent for agriculture» tem 504 repositórios no GitHub e o mais estrelado tem
  8 estrelas — é integralmente demo de hackathon. A `human-avatar/skills-for-agriculture`
  (9★, parada desde Junho de 2026) é a melhor coisa que existe e não cobre nada do que este
  projecto precisa: não tem arboricultura de obra, não tem cobertura ajardinada, não tem FLL.

  O que vale a pena não são agentes de domínio — são **MCP servers que dão ao agente acesso
  às ferramentas que a pesquisa 02 já tinha escolhido**. Dois achados fortes e verificados:
  `nkarasiak/qgis-mcp` (310★, commit de ontem, 118 ferramentas, Windows) põe o agente a correr
  SOLWEIG/UMEP directamente — confirmado que o UMEP regista provider `umep:` de Processing;
  `homeassistant-ai/ha-mcp` (4766★, MIT, modo só-leitura) põe o agente a ler o histórico dos
  sensores. Um terceiro candidato, o `agentic-swmm-workflow`, foi **elogiado e depois
  descartado dentro da própria pesquisa**: tem paper revisto por pares, mas os casos de
  validação são de **~1 km² e 40 sub-bacias** — é a «ferramenta da escala acima» outra vez,
  desta vez bem disfarçada.

  Armadilha documentada com prova: `jjsantos01/qgis_mcp` tem 1096 estrelas — **mais do triplo
  do vivo — e está parado desde Outubro de 2025.** Neste espaço a contagem de estrelas mede
  atenção passada, não vida.

  No eixo 2 aparece uma peça que faltava ao projecto: **pyfao56** (97★, USDA-ARS, activo),
  implementação de referência do FAO-56 com balanço hídrico diário de solo — é a ferramenta
  que fecha o lado «quanto retém o substrato» do conflito retenção-vs-drenagem, e nenhuma
  pesquisa anterior a tinha.

  Achado lateral com consequência imediata: o `Olen/homeassistant-plant` (868★, activo)
  **calcula DLI a partir de um sensor de iluminância, com factor lux→PPFD configurável** —
  é onde vive, em código já escrito, a calibração que a pesquisa 03 propôs para substituir a
  compra do Apogee DLI-500 (≈460 €, pendente no `INBOX.md` desde 2026-09-15).

  No eixo 3, a pergunta expressa do enunciado — **há código aberto para detecção acústica do
  escaravelho-da-palmeira?** — tem resposta apurada e é **quase não**. Nenhum dos trabalhos de
  >90% citados na pesquisa 03 publicou código. O que existe é `potamitis123/TreeVibe.v3`
  (0★, sem licença, Maio 2024) e o dataset Zenodo 10820310 (CC-BY 4.0, 6.434 gravações,
  aberto) — mas de **amoreira, não de palmeira**, e o hardware é uma sonda de 35 cm enfiada
  no tronco. É matéria-prima de investigação, não solução adoptável.
---

# Agentes de IA e open source adoptáveis para as áreas da T005

> Pesquisa da T005, fase 1, frente 5. **Encomendada depois** das quatro primeiras e da
> síntese, para responder a uma pergunta que nenhuma delas tinha: *o que é que já existe,
> feito por outros, que possamos simplesmente adoptar?*

---

## Prompt de pesquisa

```
# QUEM ÉS NESTA TAREFA

És uma sessão de pesquisa da **thread T005** do projecto Jardim. Operas dentro de
`30-THREADS/T005-caracterizacao/`. **Não escrevas fora dessa pasta**, excepto nos dois
ficheiros da raiz que este prompt te manda tocar explicitamente (`INBOX.md` e
`REGISTO-DOCUMENTOS.md`).

---

# FASE 1 — LER, ANTES DE PESQUISAR

**Lê, por esta ordem, e regista no report quais leste:**

1. `30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md` — 16 disciplinas envolvidas
2. `30-THREADS/T005-caracterizacao/research/02-DIGITAL-TWIN-SOFTWARE.md` — software de modelação
3. `30-THREADS/T005-caracterizacao/research/03-MONITORIZACAO-ACTUACAO.md` — sensores e actuadores
4. `30-THREADS/T005-caracterizacao/research/04-NUVEM-DE-PONTOS.md` — levantamento 3D
5. `30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md` — **a síntese; lê esta com atenção**
6. `CLAUDE.md` da raiz, secção 5.7 (regras G23–G36) — o protocolo de registo e NotebookLM
7. `REGISTO-DOCUMENTOS-INSTRUCOES.md` da raiz — as regras de registo **novas**

**Por que importa ler primeiro:** a tua pesquisa é sobre **que agentes e projectos open source
existem para as áreas que essas pesquisas identificaram**. Sem as ler, não sabes quais são as
áreas.

---

# FASE 2 — A PESQUISA

## A pergunta

**Que agentes de IA, skills e projectos open source existem que possamos adoptar para as áreas
identificadas na fase 1 da T005 — tanto para análise e estudo, como para instrumentação,
tratamento de dados e automatização de processos?**

## Contexto mínimo do projecto

Quintal urbano de ~75 m² em Alcântara, Lisboa. Recinto estreito e fundo (13,00 × 5,78 m) entre
muros de 2,50 m. O jardim vai subir +0,50 m sobre a betonilha existente — **tecnicamente uma
cobertura ajardinada sobre laje**, o que activa normativo próprio (FLL). Há uma palmeira que é
o ícone do projecto e cuja copa nunca foi medida. Utilizador em **Windows 10**, tecnicamente
competente, não é programador profissional. **Histórico do projecto: quatro planos morreram por
dependerem de coisas que não aconteciam** — o que sobrevive ao abandono vale mais que o que é
tecnicamente superior.

## Os três eixos

### Eixo 1 — Agentes de IA especializados

Procura **agentes, sub-agentes, skills, prompts estruturados e frameworks de agentes** para:
arboricultura e sanidade vegetal · agronomia e solos · hidrologia e drenagem urbana ·
geotecnia · climatologia e microclima · paisagismo · luminotecnia · IoT agrícola.

Cobre: **Claude Skills e sub-agentes publicados** (GitHub, awesome-lists, directórios de
skills) · **MCP servers** relevantes (dados meteorológicos, GIS, sensores, bases de dados de
plantas) · agentes em LangChain / CrewAI / AutoGen para domínios agronómicos ou ambientais ·
projectos académicos com código publicado.

**Sê céptico e diz-o:** muito «AI agent for agriculture» é demo abandonada ou wrapper de LLM
sem valor. **Distingue o que está vivo e usável do que é papel.** Verifica a data do último
commit.

### Eixo 2 — Open source para análise e estudo

Bibliotecas e ferramentas que **complementem ou substituam** o que a `02-DIGITAL-TWIN-SOFTWARE`
já identificou. Não repitas o que lá está — **procura o que falta ou o que é melhor**:
modelação de crescimento vegetal · balanço hídrico de substrato · análise de copa a partir de
nuvem de pontos · cálculo de carga estrutural · modelos de cobertura verde · bases de dados
abertas de espécies com requisitos de luz e água.

### Eixo 3 — Instrumentação, dados e automatização

Firmware, bibliotecas e integrações que **complementem** a `03-MONITORIZACAO-ACTUACAO`:
componentes ESPHome e integrações Home Assistant específicas de jardim · bibliotecas de
calibração de sensores de humidade de substrato · pipelines de séries temporais para dados
ambientais · **detecção acústica de pragas com código publicado** — a pesquisa 03 identificou
trabalho sobre o escaravelho-vermelho-da-palmeira com >90% de detecção, **procura se há código
aberto** · automatização de rega por ETo com código.

## Critérios de avaliação — aplica-os a tudo

| Critério | Pergunta |
|---|---|
| **Vivo?** | Último commit. Abandonware com site vivo é armadilha. |
| **Windows 10?** | O que for Linux-only está eliminado, não penalizado. |
| **Escala?** | Serve 75 m² ou é para hectares/cidades? |
| **Sobrevive ao abandono?** | Precisa de manutenção semanal? Então morre. |
| **Substitui ou complementa?** | O que já está identificado nas pesquisas 02 e 03? |

## Regras de método — não negociáveis

- **Facto e fonte.** WebSearch e WebFetch a fundo. Links concretos para repositórios.
- **«Não apurado» em vez de estimativa.** NUNCA inventes nomes de repositórios, estrelas,
  licenças ou datas.
- **Distingue facto de interpretação.**
- **Secção obrigatória «o que NÃO vale a pena»**, com conteúdo real.
- **Contraria o enunciado se a evidência o exigir.** Se a conclusão for «não há nada que valha a
  pena adoptar nesta área», diz — com prova. Já aconteceu neste projecto e foi valorizado.

---

# FASE 3 — ESCREVER O REPORT

Ficheiro: `30-THREADS/T005-caracterizacao/research/06-AGENTES-E-OPENSOURCE.md`

**Estrutura obrigatória:**

1. **Front matter YAML** — `created: 2026-09-18`, `thread: T005`, `tipo: pesquisa`, `summary` de várias linhas
2. **`## Prompt de pesquisa`** — **este prompt, integral**, num bloco de código. É regra do projecto: o prompt fica com o documento, senão o relatório não é auditável.
3. **`## Documentos lidos antes da pesquisa`** — a lista da fase 1, com o que cada um te deu
4. **O corpo** — os três eixos, com tabelas comparativas
5. **`## O que NÃO vale a pena`**
6. **`## Recomendação`** — se tivesses de adoptar **três coisas**, quais e porquê
7. **`## Buracos`** — o que não apuraste

Densidade alta, tabelas onde ajudarem, sem enchimento.

---

# FASE 4 — REGISTAR

**a) `REGISTO-DOCUMENTOS.md` da raiz.** Acrescenta a entrada na secção de Pesquisa, seguindo o
formato que lá está hoje. **Não reorganizes o ficheiro** — está a ser migrado por outro processo
em paralelo. Só acrescentas a tua linha.

**b) `INBOX.md` da raiz.** Acrescenta **uma entrada** antes da secção `### Higiene do repositório`,
no formato das que lá estão: `- [ ] 2026-09-18 | T005 | **<achado principal>** …`. Escreve o que
**muda alguma coisa**, não um resumo do que fizeste.

---

# FASE 5 — NOTEBOOKLM

Notebook: `8e3c8f38-0f8c-494d-aae5-fc24e9be17d2`

1. **Upload** do teu report com `mcp__notebooklm-mcp__source_add` (`source_type: file`, `wait: true`)
2. **Renomeia a source** com `source_rename` para `T005-26-09-18-RESEARCH-AGENTES-E-OPENSOURCE`
3. **Cria um slide deck** com `studio_create`: `artifact_type: slide_deck`, `slide_format: detailed_deck`, `language: pt-PT`, **`source_ids` restrito à TUA source** — um deck sobre o teu documento, não sobre o notebook todo
4. **Espera** — os decks levam ~10 minutos e o status fica em `unknown`, não em `in_progress`
5. **Descarrega o PDF** com `download_artifact` (`slide_deck_format: pdf`, `wait: true`) para
   `30-THREADS/T005-caracterizacao/research/T005-26-09-18-RESEARCH-AGENTES-E-OPENSOURCE.pdf`
6. **Renomeia o artefacto** com `studio_status` (`action: rename`) para o mesmo nome — **atenção: o
   `title` passado na criação NÃO pega, o artefacto nasce com o nome do notebook. Renomear é
   obrigatório, não é verificação.**

---

# NO FIM

**Devolve um resumo de 5 a 10 linhas, não mais.** O agente que te lançou tem o contexto
esticado e **não vai ler o teu report**. Diz apenas: que ficheiros escreveste, se o NotebookLM
correu até ao fim, e **uma linha** com o achado mais importante.
```

> **Correcção de instrução recebida a meio da execução** (Arquitecto, por ordem do David):
> a alínea **(b) da Fase 4 foi cancelada** — não se escreve no `INBOX.md` da raiz; o registo
> deste trabalho entra no handoff da T005. A alínea (a) mantém-se. **O `INBOX.md` não foi
> tocado em momento algum.**

---

## Documentos lidos antes da pesquisa

| # | Documento | O que me deu, concretamente |
|---|---|---|
| 1 | `01-ESPECIALIDADES.md` | A lista de disciplinas por onde procurar agentes: arboricultura (§3), agronomia/substrato (§4), estruturas sobre laje (§6), **impermeabilização de cobertura ajardinada (§6-bis)**, hidrologia urbana (§7), microclimatologia (§9), luminotecnia (§11), fitopatologia (§12). E as duas restrições normativas concretas — **FLL** e **EN 13948** — que usei como termo de pesquisa e que **não devolveram uma única ferramenta open source**. |
| 2 | `02-DIGITAL-TWIN-SOFTWARE.md` | A linha de base que não podia repetir: Rhino/Grasshopper, Ladybug/Honeybee, **SWMM com módulo Green Roof**, **SOLWEIG/UMEP**, DIALux evo, e a cola Python (pvlib, trimesh, shapely, pyvista). Foi esta lista que reorientou o eixo 1: **as ferramentas já estão escolhidas — o que falta é o agente lhes chegar.** Deu-me também a queixa operacional que o eixo 1 resolve: «*a ligação a SOLWEIG continua a exigir exportação manual*». |
| 3 | `03-MONITORIZACAO-ACTUACAO.md` | A base de instrumentação: Home Assistant + ESPHome como núcleo local, Wi-Fi em vez de LoRaWAN, humidade de substrato como parâmetro mestre, **BH1750 calibrado contra PAR de referência**, e a encomenda explícita desta pesquisa — *«detecção acústica >90%, procura se há código aberto»*. Deu-me também a lista de rejeições a não reabrir (ML para rega, fertirrega, NDVI, EC/pH contínuo). |
| 4 | `04-NUVEM-DE-PONTOS.md` | A cadeia de tratamento já decidida — **CloudCompare + Open3D, gratuita e em Windows 10** — e o alvo declarado: alpha shape/concave hull por fatias para a copa da palmeira. Foi contra isto que testei se há algo melhor no eixo 2 (há: `lidR`, `TreeQSM`, `pointcloudlabeler` — e **nenhum deles serve**, ver §2.3). |
| 5 | `05-SINTESE-FASE-1.md` | As prioridades que ordenaram a pesquisa toda: (a) **o projecto é uma cobertura ajardinada**; (b) **o conflito retenção-vs-drenagem é o compromisso não resolvido mais valioso** — foi isto que me fez procurar balanço hídrico de substrato e encontrar o pyfao56; (c) **a copa da palmeira bloqueia por três razões**; (d) o critério «o que sobrevive ao abandono», que virou o critério de corte do documento. |
| 6 | `CLAUDE.md` raiz §5.7 (G23–G36) | Protocolo de registo e NotebookLM. **Nota factual: o `CLAUDE.md` da raiz tem a §5.7 e as regras G23–G36 — confirmado por leitura directa das linhas 171–260.** A versão do documento injectada no meu contexto de arranque terminava em G22; a do disco não. Usei a do disco. |
| 7 | `REGISTO-DOCUMENTOS-INSTRUCOES.md` | As regras novas: oito colunas, quatro níveis de Dono, tags hierárquicas. **Não as apliquei** — o enunciado manda seguir «o formato que lá está hoje» e não reorganizar, e o `REGISTO-DOCUMENTOS.md` ainda está no formato antigo de três colunas. Ver §Buracos. |

**O que a leitura mudou na pesquisa.** Ia procurar «agentes de IA para jardins». As pesquisas
02 e 03 mostram que **as ferramentas técnicas já estão escolhidas e são boas** — o que não
existe é o agente a manejá-las. Reorientei o eixo 1 de *agentes de domínio* para **MCP servers
sobre as ferramentas já decididas**, e é daí que vem tudo o que este documento recomenda.

---

# EIXO 1 — Agentes de IA especializados

## 1.1 A resposta curta, e é negativa

**Não existe um agente de IA especializado em arboricultura, cobertura ajardinada, hidrologia
urbana à escala doméstica ou luminotecnia de jardim que valha a pena adoptar.** Procurei em
todas as oito disciplinas do enunciado. Não é «não encontrei» — é que o espaço está medido e
está vazio.

**A prova, por contagem do GitHub Search API (18-09-2026):**

| Consulta | Total de repos | Repo mais estrelado | Data do último push |
|---|---|---|---|
| `agriculture ai agent in:name,description` | **504** | `Dharaneesh20/Agro-Mandi-FrontEnd` — **8★** | 2026-01-11 |
| `agronomy agent llm` | **9** | `khawtech/nalog-agent` — **1★** | 2026-07-20 |
| `garden mcp server in:name,description` | **22** | `avlihachev/mcp-garden` — **2★** | 2026-03-29 |
| `plant growth model simulation` (Python) | **4** | `mzschwartz5/PlantGrowthModeling` — **1★** | 2021-06-22 |
| `capacitive soil moisture calibration` | **6** | `makerportal/soil-moisture-cal` — **11★** | 2026-09-17 |
| `green roof model in:name,description` | **18** | `wangzhi123321/GR-Net` — **9★** | 2025-12-31 |

**Interpretação (minha, não das fontes):** 504 repositórios cujo topo tem 8 estrelas não é um
ecossistema imaturo — é um **cemitério de projectos de fim de curso e hackathon**. Quando um
domínio tem procura real, produz vencedores: a mesma consulta para `irrigation` devolve um
repo com 778★ e dois com 460–550★, todos vivos. A diferença entre os dois padrões é o teste.

**Os repositórios do topo da lista de «agriculture ai agent», lidos pelas descrições:**
`Agro-Mandi` (preços de mercado indiano), `AgriAid` (Bangladesh, parado desde 2023),
`KisaanMitr`, `dzuka-agri`, `TerraGuard` — todos aconselhamento a pequenos agricultores em
economias agrícolas, quase todos multi-agente-com-Gemini, nenhum com licença na maioria dos
casos. **Nada disto tem relação com um quintal de 75 m² em Lisboa.**

## 1.2 Claude Skills publicadas — o que existe e porque não chega

| Recurso | Estrelas | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`human-avatar/skills-for-agriculture`](https://github.com/human-avatar/skills-for-agriculture) | **9** | **2026-06-12** | MIT | **A melhor coisa que existe no domínio — e não serve.** 50+ skills em 9 categorias. Cobre `/s4ag-orchards`, `/s4ag-soil`, `/s4ag-water`, `/s4ag-pests`, `/s4ag-agroforestry`. **O que falta:** arboricultura de obra (RPA, colo soterrado), cobertura ajardinada, FLL, estruturas, drenagem urbana, luminotecnia. O enquadramento é **agricultura regenerativa e permacultura** (Yeomans, Savory, biodinâmica, agricultura natural coreana) — quadro filosófico, não normativo. **Parado há 3 meses, 8 commits no total.** |
| [`aegro/skills`](https://awesomeclaudeplugins.com/aegro/skills) | não apurado | não apurado | não apurado | Plugin Claude Code com 12 skills de gestão agrícola. **Não verifiquei o repositório directamente** — só o directório de plugins o lista. Pelo nome (Aegro é ERP agrícola brasileiro), é gestão de explorações, não técnica de jardim. |
| [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | **75 240** | 2026-08-10 | — | Directório geral com 1000+ skills. **Consultado como índice; nada de jardim, arboricultura ou construção paisagística.** |
| [`travisvn/awesome-claude-skills`](https://github.com/travisvn/awesome-claude-skills) | **15 101** | 2026-04-28 | — | Idem. Útil como mapa do que existe; **inútil para este domínio.** |

**A conclusão que isto obriga, e é a mais importante do eixo 1:** as skills de valor para este
projecto **têm de ser escritas, não descarregadas**. E o projecto já está a fazê-lo sem lhe
chamar isso: `CLAUDE.md` da raiz, os `CLAUDE.md` de thread, o `DOSSIER-LOCAL.md`. **A pesquisa
01 é mais densa em conteúdo técnico accionável do que qualquer skill de agricultura publicada
que encontrei.**

## 1.3 MCP servers — é aqui que está o valor real

Este é o achado do eixo 1. **Não são agentes de domínio; são pontes entre o agente e as
ferramentas que a pesquisa 02 já escolheu.**

| MCP server | ★ | Último push | Licença | Windows | O que faz, e porque importa aqui |
|---|---|---|---|---|---|
| [`nkarasiak/qgis-mcp`](https://github.com/nkarasiak/qgis-mcp) | **310** | **2026-09-17** | GPL-2.0 (plugin) + MIT (servidor) | **Sim** (inclui MSIX/Microsoft Store) | **O mais valioso.** 118 ferramentas: gestão de camadas, edição de features, `execute_processing`, `execute_processing_batch`, `list_processing_algorithms`, SQL, render, layouts. QGIS 3.28–4.x. **Porque é que isto é grande:** o SOLWEIG/UMEP corre como *Processing provider* do QGIS (`processing_umep`), e a pesquisa 02 escolheu SOLWEIG como «a ferramenta certa» para microclima. Este MCP permite ao agente **correr SOLWEIG por chamada de algoritmo**, em vez de o David clicar numa interface que só usaria três vezes por ano. |
| [`Zhonghao1995/agentic-swmm-workflow`](https://github.com/Zhonghao1995/agentic-swmm-workflow) | **29** | **2026-09-06** | **MIT** | **Sim** — one-liner PowerShell ou Docker | **Agente que conduz o EPA SWMM**, com paper revisto por pares e reprodutibilidade byte-a-byte verificada. **Tecnicamente impressionante e — apurado depois — à escala errada.** Ver §1.3-bis. |
| [`homeassistant-ai/ha-mcp`](https://github.com/homeassistant-ai/ha-mcp) | **4 766** | **2026-09-17** | **MIT** | **Sim** — script de instalação dedicado | 87+ ferramentas sobre uma instância Home Assistant: **ler histórico de sensores**, estados, traces de automações, logs; criar automações, scripts, dashboards. **Tem `Read Only Mode` e endpoint `/readonly`, com backups automáticos antes de qualquer edição.** É o que transforma o histórico de sensores da configuração (b) da pesquisa 03 numa coisa que se **pergunta**, em vez de um dashboard que se olha. |
| [`sparkgeo/geo-mcp-servers`](https://github.com/sparkgeo/geo-mcp-servers) | **104** | **2026-09-11** | MIT | n/a (é uma lista) | Lista curada e **com estado monitorizado** de MCP servers geoespaciais. Vale como índice para não repetir esta pesquisa daqui a seis meses. |
| [`voska/hass-mcp`](https://github.com/voska/hass-mcp) | **342** | 2026-08-06 | MIT | Sim | Alternativa mais magra ao `ha-mcp`. Sem razão forte para preferir, dado que o `ha-mcp` tem 14× as estrelas e commit de ontem. |

### 1.3-bis. O `agentic-swmm-workflow`, e porque é que o descarto depois de o ter elogiado

**Correcção a mim próprio, feita durante a redacção.** Classifiquei-o como achado forte com base
na página do projecto. Ao fechar o buraco «suporta LID/Green Roof?», li o README completo — e a
resposta muda a conclusão.

**O que a leitura do README estabelece (factos, com citação):**

- A tabela de validação tem **seis linhas de evidência e nenhuma menciona LID ou Green Roof.**
- Os casos são: **Greenwich Peninsula e NYC Midtown, «~1 km² cada»**; «**modelo Tecnopolo externo
  de 40 sub-bacias**»; camadas GeoPackage públicas do TUFLOW.
- O trabalho de síntese de rede é do [SWMManywhere](https://github.com/ImperialCollegeLondon/SWMManywhere)
  (Imperial College London) e parte de uma **bounding box WGS84**.
- O próprio repositório declara os limites: «***not** a calibrated or validated network*»,
  «*GIS preprocessing concept, not a calibrated SWMM performance claim*», «*Structured raw GIS
  path, not arbitrary CAD/GIS recognition*».
- Convite a contribuições em «*DEM / land-use / soil / drainage-asset workflows*» — o vocabulário
  é de bacia hidrográfica urbana.

**Veredicto revisto: não adoptar.** Este agente resolve *«sintetizar a rede de drenagem de um
quilómetro quadrado de cidade a partir de dados escassos»*. O problema deste projecto é
*«uma cobertura ajardinada de 75 m² com uma saída de drenagem»* — **quatro ordens de grandeza
abaixo, e sem rede nenhuma para sintetizar.** É o padrão que as pesquisas 02 e 03 já tinham
nomeado (§4.1 da síntese): **a tentação de comprar a ferramenta da escala acima.** Desta vez
vinha embrulhada num paper revisto por pares, que é o disfarce mais convincente que o padrão já
usou neste projecto.

**O que se mantém:** o **EPA SWMM** e o seu módulo Green Roof continuam a ser a resposta certa —
directamente, pela interface, como a pesquisa 02 disse. **O agente por cima é que não.**

### A armadilha, documentada com prova

| Repositório | ★ | Último push | Estado |
|---|---|---|---|
| [`jjsantos01/qgis_mcp`](https://github.com/jjsantos01/qgis_mcp) | **1 096** | **2025-10-01** | **Parado há ~1 ano. Sem licença.** |
| [`nkarasiak/qgis-mcp`](https://github.com/nkarasiak/qgis-mcp) | 310 | **2026-09-17** | Vivo, 213 commits, GPL-2.0+MIT |

**O repositório com 3,5× mais estrelas está morto e o vivo é o segundo da lista.** É a
demonstração exacta do critério «Vivo?» do enunciado: **neste espaço a contagem de estrelas
mede atenção passada, não vida.** Quem pesquisar «qgis mcp» e ordenar por estrelas — o que
qualquer pessoa faz — instala o morto. Fica registado porque **este erro é gratuito de cometer
e caro de descobrir.**

## 1.4 Dados meteorológicos e de plantas por MCP

| Recurso | ★ | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`etudelab/agri-weather-mcp`](https://github.com/etudelab/agri-weather-mcp) | **0** | **2025-07-23** | MIT | 6 ferramentas sobre a Open-Meteo, incluindo `get_evapotranspiration_data` (ET e **ET₀** de referência) e `get_soil_conditions`. **Funcionalmente é exactamente o que se quereria.** Mas: 0 estrelas, parado há 14 meses, Python 3.11+. **Não adoptar como dependência — ler como exemplo.** É ~200 linhas de wrapper sobre uma API pública gratuita; copiar a ideia custa menos que herdar o abandono. |
| Outros MCP Open-Meteo (`cmer81`, `IBM/chuk-mcp-open-meteo`, `isdaniel`, `gbrigandi`, `JeremyMorgan`) | não apurados individualmente | — | vários | **Existem pelo menos seis.** Todos wrappers da mesma API gratuita e sem chave. A escolha entre eles é indiferente; **a Open-Meteo é que é o activo**, não o wrapper. |
| [`Olen/home-assistant-openplantbook`](https://github.com/Olen/home-assistant-openplantbook) | **563** | **2026-08-11** | GPL-3.0 | **Base de dados aberta de requisitos por espécie** (open.plantbook.io): humidade de solo min/max, temperatura min/max, rega, luz solar, solo, poda, fertilização. **Conta gratuita com `client_id`/`secret` obrigatória.** **Ressalva verificada: a documentação não confirma DLI nem condutividade** — e o DLI é, pela pesquisa 03, «o número que decide a espécie». |
| [`Olen/homeassistant-plant`](https://github.com/Olen/homeassistant-plant) | **868** | **2026-09-04** | GPL-3.0 | O componente que **compara os sensores reais contra os limiares do OpenPlantbook** e gera alerta por espécie. É o par funcional do anterior e o mais estrelado dos dois. **Vivo, 14 dias.** |
| [`treflehq/trefle-api`](https://github.com/treflehq/trefle-api) | **586** | 2026-09-16 | AGPL-3.0 | ~400 000 espécies. **Facto verificado: `GET https://trefle.io/api/v1/plants` devolve HTTP 401** — exige token. O repositório tem commits recentes mas **não confirmei que o serviço público aceita registos novos**; o Trefle teve histórico de indisponibilidade. **Não apurado** — ver Buracos. |
| [`avlihachev/mcp-garden`](https://github.com/avlihachev/mcp-garden) | **2** | 2026-03-29 | MIT | «MCP server for gardening intelligence — weather, frost alerts, soil data». 2 estrelas, parado há 6 meses. **Ignorar.** |

## 1.5 LangChain / CrewAI / AutoGen para domínios agronómicos

**Nada apurado que valha a pena.** As buscas dedicadas devolveram só os frameworks genéricos e
artigos comparativos. Os agentes agronómicos concretos que encontrei (`agrosage`,
`AgriSense-Agent`, `AgriCoreAI`, `geoharvestai`, `agribot`) têm **todos 0 ou 1 estrela** e são
orquestrações de prompts sobre uma API de tempo e uma API de preços.

**Interpretação minha:** um LLM moderno com acesso a web e a uma boa base documental — que é o
que esta thread é — **já supera qualquer um destes.** Adoptar um deles seria trocar um modelo
actual por um modelo antigo embrulhado num prompt de terceiro.

---

# EIXO 2 — Open source para análise e estudo

Regra do enunciado: **não repetir o que a 02 já tem.** Tudo aqui é acrescento ou correcção.

## 2.1 Balanço hídrico de substrato — a peça que faltava

**Este é o achado do eixo 2, e liga-se directamente ao conflito central da síntese.**

| Ferramenta | ★ | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`kthorp/pyfao56`](https://github.com/kthorp/pyfao56) | **97** | **2026-02-12** | **CC0 1.0 / domínio público** | **Adoptar.** Implementação Python do **FAO-56, método dos coeficientes culturais duplo e simples**, com **balanço hídrico diário do solo**. Classes `SoilWaterProfile` (depleção da zona radicular, SWD em mm) e `Visualization` (séries temporais de depleção, ET e Kc). Publicado em *SoftwareX* e mantido por **investigador do USDA-ARS**. Existe cópia editorial em `ElsevierSoftwareX/SOFTX-D-23-00060`. |
| [`soilwater/fieldcaster`](https://github.com/soilwater/fieldcaster) | **0** | **2020-11-04** | nenhuma | **Abandonware.** Parado há quase 6 anos. Nomeado só para o descartar. |
| `WaterpyBal` | não apurado no GitHub | — | — | Biblioteca de recarga de aquíferos publicada em *Environmental Modelling & Software*. **Escala errada** — modelação espácio-temporal de recarga difusa. Não é para 75 m². |

**Porque é que o pyfao56 importa a este projecto, dito com precisão.** A síntese identifica o
conflito **retenção-para-a-planta vs. drenagem-para-a-laje** como «o compromisso técnico não
resolvido mais valioso», e diz que «a espessura de cada camada é uma decisão de compromisso».
A pesquisa 03 acrescenta que num substrato fino sobre laje impermeável **não há reserva
lateral nem drenagem profunda** — o erro de rega mata em dias.

**O pyfao56 é a ferramenta que põe um número nessa frase.** Dá capacidade de campo, ponto de
emurchecimento, depleção diária e ET cultural — ou seja, permite responder *«com X cm de
substrato de retenção Y, quantos dias aguenta sem rega em Agosto?»* **Nenhuma das quatro
pesquisas anteriores identificou uma ferramenta para esta pergunta.** A 03 recomenda ETo como
refinamento, não como base, «porque o Kc não existe para este substrato» — verdade, mas o
pyfao56 serve na mesma para **dimensionar as camadas**, que é uma pergunta de projecto, não de
rega diária. **Correcção honesta a mim próprio:** isto não é rega automatizada por ML, que a 03
rejeitou com razão — é uma folha de cálculo hidrológica a correr uma vez.

> **Licença verificada durante esta pesquisa, e é o melhor caso possível.** O GitHub API
> devolve `NOASSERTION`, mas o ficheiro `LICENSE.md` diz: «*As a work of the United States
> Government, this package is in the public domain within the United States. Additionally, we
> waive copyright and related rights in the work worldwide through the **CC0 1.0 Universal**
> public domain dedication.*» **Sem obrigações de atribuição, sem contaminação copyleft, uso
> comercial livre.** Buraco fechado.

## 2.2 Modelação de crescimento vegetal

**Veredicto: não há nada. O espaço está vazio e a pesquisa 02 já tinha a melhor resposta.**

A consulta `plant growth model simulation` em Python devolve **4 repositórios**, topo com 1
estrela, o mais recente de Maio de 2025. A 02 já tinha identificado a resposta certa — **The
Grove 3D** (comercial, crescimento procedural com simulação de competição por luz) e Sapling
(gratuito, no Blender). **Nada no open source se aproxima.** Não reabrir.

## 2.3 Análise de copa a partir de nuvem de pontos

A 04 recomendou CloudCompare + Open3D (alpha shape/concave hull por fatias). **Testei se há
melhor. Há ferramentas mais sofisticadas — e nenhuma serve.**

| Ferramenta | ★ | Último push | Licença | Porque NÃO serve aqui |
|---|---|---|---|---|
| [`r-lidar/lidR`](https://github.com/r-lidar/lidR) | **710** | **2026-09-04** | GPL-3.0 | Madura e viva, mas é **R, não Python**, e é para **inventário florestal por ALS** — detecção de topos de árvore e segmentação em povoamentos. Para **uma** árvore já segmentada à mão, a segmentação individual (o valor principal do lidR) é trabalho a zero. |
| [`InverseTampere/TreeQSM`](https://github.com/InverseTampere/TreeQSM) | **231** | **2023-05-11** | NOASSERTION | Referência para modelação quantitativa de estrutura. **MATLAB** (licença comercial cara) e **parado há mais de 3 anos.** Modela ramificação cilíndrica — a arquitectura de **uma palmeira não é ramificada**: é um estipe e uma coroa de folhas. O modelo é errado para a espécie. |
| `PyTLidar` | não encontrado no GitHub Search | — | — | Port Python do TreeQSM, descrito em preprint no EcoEvoRxiv. **Não localizei o repositório** — ver Buracos. Mesma objecção de arquitectura: QSM é para árvores ramificadas. |
| [`honkaepp/pointcloudlabeler`](https://github.com/honkaepp/pointcloudlabeler) | **0** | **2026-09-17** | GPL-3.0 | Vivo (commit de ontem) e faz o que se quer — altura, DAP, métricas de copa, a partir de TLS/MLS. **Mas: 0 estrelas, escrito em Rust, e é inventário florestal.** Zero utilizadores é zero suporte. |

**Veredicto: a pesquisa 04 estava certa e mantém-se.** CloudCompare (4 750★, commit de ontem)
+ Open3D (13 973★, commit de 2 dias) para o alpha shape. **A literatura confirma o método:**
o volume de copa calcula-se agrupando os pontos da árvore, filtrando protuberâncias isoladas
por *clustering*, e computando o **invólucro convexo 3D** como aproximação do volume. É
exactamente o que a 04 propõe. **Não trocar.**

## 2.4 Cálculo de carga estrutural

*(Nota de conformidade O7/T17: descrevem-se ferramentas de cálculo; não se recomenda consulta a
profissional.)*

| Ferramenta | ★ | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`pcachim/eurocodepy`](https://github.com/pcachim/eurocodepy) | **53** | **2026-08-29** | LGPL-3.0 | O melhor do lote, e **insuficiente para o que aqui importa.** Cobre EN 1990/1991 (tipos de carga, combinações ULS/SLS/ALS), EN 1992, 1993, 1995, 1997, 1998, com base de dados de valores característicos. **Ressalva verificada: não está confirmado que implemente o âmbito completo da EN 1991-1-1** — pesos próprios, sobrecargas e **densidades de materiais**, que é o único capítulo que este projecto precisa. Exige Python ≥3.12. **O próprio README declara: «educational and research purposes only… must not be used for final structural designs».** |
| [`kunle009/FoundationDesign`](https://github.com/kunle009/FoundationDesign) | **89** | 2025-07-23 | GPL-3.0 | Sapatas isoladas e combinadas. **Objecto errado** — aqui não há fundação nova; há carga sobre laje existente. Parado há 14 meses. |
| [`domthom21/eurocodedesign`](https://github.com/domthom21/eurocodedesign) | **8** | **2026-09-01** | MPL-2.0 | Vivo, tipado, mas muito pequeno. Sem massa crítica. |

**Veredicto, e é para dizer com clareza:** o cálculo que este projecto precisa —
*espessura × peso volúmico saturado de cada camada, somado, em kg/m²* — **é aritmética, não é
software.** A pesquisa do David (`2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md`)
já traz densidades secas **e saturadas** por substrato e secções-tipo com peso por m². **Uma
folha de cálculo com esses números resolve mais do que qualquer destas bibliotecas**, e nenhuma
delas traz uma base de dados de substratos FLL. **Não adoptar nenhuma.**

## 2.5 Modelos de cobertura verde

**Veredicto: não existe open source de cobertura verde utilizável. 18 repositórios no mundo.**

O topo é `wangzhi123321/GR-Net` (9★) e é **segmentação semântica de imagem** — identificar
telhados verdes em fotografia aérea, problema oposto ao deste projecto. Os restantes são
código MATLAB de tese (`Peter-Gunn/Green-Roof`, 3★, 2022, rede térmica RC) ou repositórios
vazios. `CITY-at-UMD/GreenRoofModel` está parado desde **2014**.

**A resposta continua a ser a que a 02 deu: o módulo Green Roof do EPA SWMM** — [`USEPA/Stormwater-Management-Model`](https://github.com/USEPA/Stormwater-Management-Model), 361★, push 2025-05-01, domínio público, Windows nativo. É código da EPA, validado, e o facto de o push ser de há 16 meses **não é abandono** — é software governamental maduro com ciclo de release lento. **Distinção importante:** abandono num projecto de uma pessoa lê-se pela data; num organismo público, não.

## 2.6 Bases de dados abertas de espécies

Ver §1.4 — **OpenPlantbook + `homeassistant-plant`** é a combinação viva e utilizável.
`OpenFarm` ([`openfarmcc/OpenFarm`](https://github.com/openfarmcc/OpenFarm), 1 733★) é
**arquivado** — confirmado pelo campo `archived: true` do API. Não usar.

---

# EIXO 3 — Instrumentação, dados e automatização

## 3.1 Rega por ETo com código — existe, é maduro, e resolve

| Recurso | ★ | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`altmenorg/HAsmartirrigation`](https://github.com/altmenorg/HAsmartirrigation) (Smart Irrigation, de jeroenterheerdt) | **550** | **2026-09-13** | **MIT** | **Adoptar quando houver rega.** Componente HACS que **calcula o tempo de rega para compensar a perda por evapotranspiração**, descontando a precipitação ocorrida e prevista. É a automação por ETo que a pesquisa 03 descreveu como «refinamento» — já escrita, testada e mantida. Vivo há 5 dias. |
| [`rgc99/irrigation_unlimited`](https://github.com/rgc99/irrigation_unlimited) | **460** | **2026-06-22** | **MIT** | Controlador de rega para HA: zonas, sequências, calendários. **Encaixa com o anterior** — o Smart Irrigation calcula o tempo, o Irrigation Unlimited executa-o. Documentado pela comunidade como par. |
| `Dan-in-CA/SIP` | 420★ | 2026-07-27 | — | Controlador sobre Raspberry Pi, **independente do Home Assistant**. Bom projecto, mas **duplica o núcleo** que a 03 já escolheu. Não adoptar. |

**Ressalva importante, e é do enunciado:** isto é automação por ETo, **não é ML**. A pesquisa 03
rejeitou ML para rega com um argumento que se mantém intacto. O Smart Irrigation é uma
fórmula FAO com dados de tempo — determinística, auditável e depurável.

## 3.2 ESPHome e calibração de humidade de substrato

**Veredicto: não há biblioteca. Há receitas, e o valor está na receita, não no código.**

| Recurso | ★ | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`esphome/esphome`](https://github.com/esphome/esphome) | **11 700** | **2026-09-17** | — | A base. Viva ao dia. Já era a escolha da 03. |
| [`stratogk/Ultimate-ESPHome-Soil-Moisture-Node`](https://github.com/stratogk/Ultimate-ESPHome-Soil-Moisture-Node) | **3** | **2026-04-17** | MIT | **Copiar o padrão, não instalar o projecto.** Traz uma ideia que vale: **sequência de calibração interactiva disparada por botão no dashboard do Home Assistant**, com sensor de texto a guiar o processo em tempo real. Isto responde ao problema que a 03 deixou em aberto — recalibração anual de ~2 h. **Mas 3 estrelas é uma pessoa.** É um ficheiro YAML: lê-se, entende-se, reescreve-se. |
| [`makerportal/soil-moisture-cal`](https://github.com/makerportal/soil-moisture-cal) | **11** | **2026-09-17** | GPL-3.0 | Calibração de sensor capacitivo com Arduino + Python. **É o mais estrelado do mundo nesta consulta, com 11 estrelas.** Vivo ao dia. Serve como referência de método (curva tensão→VWC), não como dependência. |
| Consulta completa `capacitive soil moisture calibration` | **6 repositórios no total** | — | — | **É a medida da maturidade do espaço.** Não existe biblioteca de calibração de sensores de humidade de substrato. Cada pessoa faz a sua curva de dois pontos (seco/saturado). **A 03 estava certa em tratar isto como procedimento manual.** |

## 3.3 Detecção acústica de pragas — a pergunta expressa do enunciado

**A resposta é: quase não. E o «quase» é matéria-prima de investigação, não solução.**

O enunciado pediu explicitamente para procurar código aberto para o trabalho de >90% de
detecção do *Rhynchophorus ferrugineus* que a pesquisa 03 identificou. **Procurei e apurei:**

| Trabalho | Código publicado? | Facto verificado |
|---|---|---|
| *On the Design of a Bioacoustic Sensor for the Early Detection of the Red Palm Weevil* (Sensors 13(2):1706, 2013) | **Não** | O artigo de 2013 descreve hardware, não software distribuído. |
| *Early Detection of RPW Infestations using Deep Learning Classification of Acoustic Signals* ([arXiv 2308.15829](https://arxiv.org/html/2308.15829)) | **Não** | **Verificado por leitura directa: não há declaração de disponibilidade de código nem de dados, nem link GitHub ou Zenodo.** Dataset proprietário de Al-Ahssa (531 infestados / 575 sãos), cedido por terceiro. Reporta **100% de exactidão** com features CQCC-MFCC-BFCC combinadas — e é justamente um número que, sem código nem dados, não é reprodutível. **Hardware descrito: sonda (guia de onda) de 35 cm inserida dentro da árvore, furo de 8 mm a 30°, gravações de 20 s com período de repetição de 5 min.** |
| *Machine learning-enabled acoustic sensing for RPW infestation detection* (Sci. Rep. 2025/26, PMC12583683) | Não apurado | Não abri o artigo completo. Ver Buracos. |
| *Towards Detecting RPW Using ML and Fiber Optic Distributed Acoustic Sensing* (Sensors 21(5):1592) | **Irrelevante para adopção** | DAS por fibra óptica é tecnologia para **explorações vastas**, não para uma árvore. Além disso, há **pedido de patente norte-americana** sobre o método (USPTO 12259272) — sinal claro de que a linha não vai para o open source. |

### O que existe realmente, e é de outra espécie

| Recurso | Estado verificado | Veredicto |
|---|---|---|
| [`potamitis123/TreeVibe.v3`](https://github.com/potamitis123/TreeVibe.v3) | **0★ · último push 2024-05-12 · sem ficheiro de licença · Python** | Contém **três ficheiros**: `README.md`, `mullbery_7_days.py`, `vibro_scan_paper.py`. **É código de demonstração do paper, não uma biblioteca.** Sem modelo treinado, sem script de treino, sem inferência empacotada. |
| [Zenodo 10820310](https://doi.org/10.5281/zenodo.10820310) — *Automated Vibroacoustic Monitoring of Trees for Borer Infestation* | **Aberto · CC-BY 4.0 · 6 434 gravações** (4 747 infestado / 1 091 não infestado, mais conjunto de teste em 5 árvores e 596 gravações de 7 dias) · 16 kHz, mp3 e wav | **É o único activo aberto real de todo este eixo.** Publicado com o paper *Automated Vibroacoustic Monitoring of Trees for Borer Infestation* (Sensors 24(10):3074). |
| Dataset TreeVibes no Kaggle (`kaggle.com/datasets/potamitis/treevibes`) | ~1 000 gravações «limpas» e >50 000 «infestadas» segundo a literatura. **Termos de licença não apurados** — a página bloqueia por reCAPTCHA. | Complementar ao Zenodo. |

**O problema que mata a adopção directa, e é de espécie, não de código:** o TreeVibes é de
**amoreira** — o próprio ficheiro se chama `mullbery_7_days.py`. A assinatura acústica de uma
larva de broca a roer madeira de amoreira **não é a de uma larva de *R. ferrugineus* a
alimentar-se do tecido fibroso do estipe de uma *Phoenix***. A literatura de 2013 aponta a
intensidade em torno dos **2250 Hz** como marcador do escaravelho; nada garante que um
classificador treinado em amoreira transfira.

**E o problema físico é maior que o de software.** O hardware da literatura de RPW é uma
**sonda de 35 cm inserida por furo de 8 mm no tronco**. Aplicar isto ao activo que o projecto
declara «protagonista absoluta» e «inegociável» é **furar a palmeira** — e num contexto em que
a mesma pesquisa 01 identifica o soterramento do colo como causa de declínio lento, abrir uma
via de entrada para patogénios não é decisão trivial.

**Conclusão do eixo, dita como o enunciado pediu — contrariando a expectativa:** a pesquisa 03
classificou a detecção acústica como «o achado mais valioso». **Mantém-se valiosa como
conhecimento e mantém-se sem caminho open source.** O que está disponível para adopção
imediata continua a ser o que a 03 já recomendou: **armadilha de feromona de agregação
convencional (dezenas de euros) e inspecção visual regular.** Um DIY acústico a partir do
TreeVibes é **um projecto de investigação de meses** — exactamente o tipo de coisa que, pelo
histórico deste projecto, não acontece.

## 3.4 Séries temporais de dados ambientais

**Veredicto: não acrescentar nada. A 03 já decidiu bem.**

A consulta `influxdb grafana sensor garden` devolve **1 repositório, com 0 estrelas**. A 03 já
tinha classificado ThingsBoard/InfluxDB+Grafana como «excesso para 75 m²… brinquedo técnico sem
retorno». **Confirma-se, e por via independente:** o Home Assistant tem *recorder* e
estatísticas de longo prazo nativas, e o **`ha-mcp` (§1.3) permite consultar esse histórico por
pergunta**. Montar infra-estrutura de séries temporais por baixo é acrescentar um serviço para
manter — o oposto do critério «sobrevive ao abandono».

## 3.5 Integrações Home Assistant específicas de jardim

| Recurso | ★ | Último push | Licença | Veredicto |
|---|---|---|---|---|
| [`Olen/homeassistant-plant`](https://github.com/Olen/homeassistant-plant) | **868** | **2026-09-04** | GPL-3.0 | **Adoptar quando houver sensores — e é mais valioso do que parecia.** Ver §3.6. Limiares min/max para **temperatura · humidade de solo · condutividade · iluminância · humidade do ar · CO2 · temperatura de solo**, e **calcula DLI e VPD por derivação**. Cada limiar é uma entidade editável pela interface. **É o que transforma «tenho um número» em «esta planta está fora do intervalo dela».** |
| [`Olen/home-assistant-openplantbook`](https://github.com/Olen/home-assistant-openplantbook) | **563** | **2026-08-11** | GPL-3.0 | O backend de dados do anterior. Conta gratuita necessária. |
| `PatrickHallek/automated-irrigation-system` | 778★ | **2024-02-18** | nenhuma | O mais estrelado do espaço de rega — **e parado há 19 meses, sem licença.** Segunda instância do padrão «estrelas ≠ vida». Não adoptar. |

## 3.6 O DLI já está resolvido em código — e isso toca numa compra pendente de 460 €

**Este achado apareceu ao fechar um buraco e é o mais accionável do eixo 3.**

**Facto verificado** no README do `Olen/homeassistant-plant`: a integração **cria
automaticamente um sensor de DLI para cada planta**, descrito como «*a luz total
fotossinteticamente activa recebida por dia*», **calculado a partir de um sensor de
iluminância através de um factor de conversão lux→PPFD configurável, com valor por omissão
0,0185**. Cria também VPD a partir de temperatura e humidade (limiares por omissão 0,4 e
1,6 kPa).

**Porque é que isto importa, e liga-se a `INBOX.md`.** A síntese §4.3 documenta a compra
pendente do **Apogee DLI-500 (≈460 €)** e a resposta da pesquisa 03: *um BH1750 de 5–8 € por
zona, calibrado uma vez contra um PAR de referência, dá 80% do valor a 5% do custo*. **O que
faltava era onde vive essa calibração.** Vive aqui: **é o factor lux→PPFD, um campo
configurável.**

A cadeia fica fechada e sem escrever código: **BH1750 por zona (ESPHome) → `homeassistant-plant`
converte para DLI com o factor → compara contra o limiar da espécie vindo do OpenPlantbook.**
O Apogee emprestado serve para **afinar um número**, não para equipar o jardim.

⚠ **Ressalva de método, e é importante:** 0,0185 é um factor **genérico**. A pesquisa 03 dizia
que a incerteza espectral (factor PAR, ±14%) é precisamente o que nenhuma simulação resolve.
**O factor por omissão não resolve nada — resolve o facto de ser editável.** Isto reforça o
argumento da 03, não o dispensa: continua a ser preciso **um** acesso a um sensor PAR de
referência, uma vez, para saber que número pôr no campo.

---

## O que NÃO vale a pena

1. **Agentes de IA «para agricultura».** 504 repositórios, topo com 8 estrelas, quase nenhum
   com licença, quase todos aconselhamento a pequenos agricultores em economias agrícolas.
   **Nenhum tem relação com um quintal urbano sobre laje.** Não é um espaço imaturo — é um
   espaço sem procura real, cheio de projectos de portefólio.

2. **`jjsantos01/qgis_mcp` (1 096★).** Parado desde **Outubro de 2025**, sem licença. É o
   resultado que aparece primeiro em qualquer pesquisa e é o errado. **Usar
   `nkarasiak/qgis-mcp`.**

3. **`PatrickHallek/automated-irrigation-system` (778★).** Parado desde Fevereiro de 2024, sem
   licença. Mesmo padrão.

4. **`openfarmcc/OpenFarm` (1 733★).** **Arquivado** — confirmado pelo API. Aparece citado como
   fonte de dados agregada pelo Trefle, o que é motivo adicional de cautela sobre a frescura
   dos dados a jusante.

5. **Escrever um detector acústico de RPW a partir do TreeVibes.** Dataset de amoreira, 0
   estrelas no repo de código, sem licença, sem modelo treinado, e o hardware da literatura
   exige **furar o estipe da palmeira com broca de 8 mm a 35 cm de profundidade**. É um
   projecto de investigação de meses com resultado incerto, sobre o activo insubstituível do
   projecto. **Pelo critério «quatro planos morreram por depender de coisas que não
   aconteciam», isto é o arquétipo do quinto.**

6. **Bibliotecas de Eurocódigo em Python para calcular a carga do pacote.** `eurocodepy` é o
   melhor e **o próprio README declara ser só para fins educativos e de investigação**. O
   cálculo aqui é uma soma de `espessura × peso volúmico saturado`; o que falta são os
   **números dos substratos**, e esses já estão na pesquisa do David — não numa biblioteca.

7. **Infra-estrutura de séries temporais (InfluxDB + Grafana + ThingsBoard).** Confirmada a
   conclusão da 03 por via independente: 1 repositório no mundo para esta combinação em
   contexto de jardim, com 0 estrelas. O HA já grava e o `ha-mcp` já responde.

8. **`lidR`, `TreeQSM` e `pointcloudlabeler` para a copa da palmeira.** São ferramentas de
   inventário florestal: resolvem **segmentar muitas árvores**, que aqui não é problema. O
   TreeQSM modela **ramificação cilíndrica**, e uma *Phoenix* não é uma árvore ramificada —
   é o modelo errado para a espécie, além de estar em MATLAB e parado desde 2023.

9. **`etudelab/agri-weather-mcp` como dependência.** Funcionalmente ideal (tem ET₀), mas **0
   estrelas e parado há 14 meses**. Ler o código e reimplementar custa menos que herdar o
   abandono de um wrapper de ~200 linhas sobre uma API pública.

10. **Modelos open source de cobertura verde.** 18 repositórios, topo de 9★ que faz segmentação
    de imagem aérea — problema inverso. **O módulo Green Roof do SWMM continua a ser a única
    resposta séria**, e já estava identificado.

11. **`Zhonghao1995/agentic-swmm-workflow`, apesar de tudo o que tem a favor.** MIT, vivo, paper
    revisto por pares, reprodutibilidade byte-a-byte, instalação por PowerShell. **E os casos de
    validação são de ~1 km² e 40 sub-bacias, sem uma única menção a LID ou Green Roof.** É a
    ferramenta da escala acima com o melhor disfarce que este projecto já encontrou. **Correr o
    SWMM directamente**, como a pesquisa 02 disse.

---

## Recomendação — as três coisas a adoptar

**Critério aplicado: só entra o que está vivo, corre em Windows 10, serve 75 m² e não exige
manutenção para continuar a valer.**

### 1. [`nkarasiak/qgis-mcp`](https://github.com/nkarasiak/qgis-mcp) — 310★ · commit de 2026-09-17 · GPL-2.0 + MIT

**Porquê esta em primeiro lugar.** A pesquisa 02 escolheu **SOLWEIG/UMEP** como «a ferramenta
certa» para microclima e apontou o ponto fraco: *«a ligação a SOLWEIG continua a exigir
exportação manual — não há plugin directo»*. O SOLWEIG corre como Processing provider do QGIS;
este MCP expõe `execute_processing` e `list_processing_algorithms` ao agente. **Resolve
exactamente a fricção declarada.**

E resolve um problema maior que o técnico: **o QGIS é uma ferramenta que o David usaria três
vezes no projecto inteiro** — precisamente a condição em que a curva de aprendizagem nunca se
amortiza e o plano morre. Com o MCP, o agente maneja a ferramenta e o David lê o resultado.

**Riscos, ditos:** GPL-2.0 no plugin; exige o gestor `uv`; QGIS 3.28+. **É software de uma
pessoa** — mas com 213 commits, 77 forks e commit de ontem, está na categoria certa.

> **Verificação feita durante esta pesquisa, e fecha o principal risco da recomendação.** A
> documentação oficial do UMEP confirma que o UMEP for Processing **regista um provider
> normal do QGIS Processing com o prefixo `umep:`**, invocável por `processing.run()`:
>
> ```python
> processing.run("umep:Urban Geometry: Wall Height and Aspect", {...})
> ```
>
> Ou seja, os algoritmos do UMEP são algoritmos de Processing como quaisquer outros — e o
> `execute_processing` / `list_processing_algorithms` do MCP alcança-os **sem integração
> especial**. **Ressalva que fica:** a documentação marca o SOLWEIG como migrado e «READY»
> mas **não mostra o identificador exacto do algoritmo SOLWEIG** no excerto consultado.
> Obtém-se em 2 minutos por `list_processing_algorithms` ou pelo log do Processing.

### 2. [`kthorp/pyfao56`](https://github.com/kthorp/pyfao56) — 97★ · commit de 2026-02-12 · **CC0 / domínio público** · USDA-ARS · publicado em *SoftwareX*

**Porquê.** É a única ferramenta desta pesquisa que ataca **o compromisso que a síntese
classificou como o mais valioso por resolver**: retenção-para-a-planta vs.
drenagem-para-a-laje. Dá balanço hídrico diário com capacidade de campo, ponto de
emurchecimento e depleção da zona radicular — ou seja, converte «quanto retém o substrato» de
adjectivo em número de dias.

**E chega no momento certo.** A síntese marca a decomposição dos +0,50 m em camadas como
**urgente para a T004, porque a obra arranca**. A pesquisa do David já traz espessuras e
densidades saturadas; **o pyfao56 é o que testa essas secções-tipo contra um Agosto de Lisboa
antes de serem construídas.** Custo: zero. Corre em Python, que o David já usa com modelo
validado — o indicador de sucesso que a 02 destacou.

**Riscos:** nenhum de licença — **verificado: CC0 1.0 / domínio público dos EUA**. O Kc para este
substrato não existe, como a 03 avisou; para dimensionar camadas, uma gama de Kc plausível
chega, e a sensibilidade do resultado a esse intervalo é ela própria informação útil.

### 3. [`homeassistant-ai/ha-mcp`](https://github.com/homeassistant-ai/ha-mcp) — 4 766★ · commit de 2026-09-17 · MIT

**Porquê, e é a mais alinhada com o histórico do projecto.** A configuração (b) da pesquisa 03
produz dados que alguém tem de olhar. **O modo de falha deste projecto não é técnico — é o
abandono:** o dashboard que ninguém abre passado o segundo mês. Este MCP permite **perguntar ao
histórico em vez de o vigiar** — «a zona 3 secou mais depressa que a 1 este Verão?» — e isso
sobrevive ao desinteresse de uma forma que nenhum painel sobrevive.

**Adoptar em `Read Only Mode`, e isso é parte da recomendação, não uma ressalva.** O servidor
tem endpoint `/readonly` e activação por ferramenta. **Um agente com poder de escrita sobre as
válvulas de rega é o modo de falha «sensor preso a seco» da pesquisa 03, com um LLM no lugar do
sensor.** Leitura resolve o problema real; escrita cria um novo.

**Ordem de execução:** o **pyfao56 é o único dos três que é útil hoje** — os outros dois
esperam pelo QGIS montado e pelos sensores instalados. Se só uma coisa for feita, é essa.

---

## Buracos

Declarados com o que faltaria para fechar cada um.

> **Cinco foram fechados durante a própria redacção, e um deles inverteu uma recomendação.**
> Ficam registados como fechados em vez de apagados, porque o percurso é a prova: (1) o UMEP
> regista provider `umep:` de Processing — a recomendação nº 1 fica de pé; (2) o
> `agentic-swmm-workflow` valida a ~1 km² e **passou de recomendado a rejeitado**; (3) o Trefle
> está de pé e o 401 é normal; (4) o `homeassistant-plant` **deriva DLI de iluminância com
> factor configurável**, o que gerou o §3.6 e toca numa compra de 460 €; (5) o `pyfao56` é
> **CC0 / domínio público**, não `NOASSERTION`.

1. **~~Não confirmei que o `nkarasiak/qgis-mcp` expõe o `processing_umep`/SOLWEIG.~~
   FECHADO durante esta pesquisa, quase por inteiro.** A documentação oficial do UMEP confirma
   que o plugin regista um **provider de Processing normal com prefixo `umep:`**, invocável por
   `processing.run("umep:...", {...})` — logo alcançável pelo `execute_processing` do MCP sem
   integração dedicada. **O que resta:** o **identificador exacto do algoritmo SOLWEIG** não
   consta do excerto consultado. Obtém-se por `list_processing_algorithms` ou pelo log do
   Processing. Minutos, não horas.

2. **~~O `agentic-swmm-workflow` não documenta suporte a LID / Green Roof.~~ FECHADO, e mudou a
   conclusão** — ver §1.3-bis. A leitura do README completo confirma que nenhuma das seis linhas
   de evidência de validação menciona LID ou Green Roof, e que os casos são de ~1 km² e de um
   modelo externo de 40 sub-bacias. **Passou de recomendado a rejeitado.** O paper em si
   (DOI 10.3390/aieng1010005) **não foi lido** — a MDPI devolve HTTP 403 a este agente — mas o
   README é do mesmo autor e é explícito sobre os limites de evidência.

3. **Estado do serviço público do Trefle — parcialmente fechado.** Verificado: `trefle.io`
   responde **HTTP 200**, a página de registo `/users/sign_up` responde **HTTP 200**, e
   `GET /api/v1/plants` devolve **401 com `{"code":"unauthorized"}`** e remete para obter token
   — ou seja, **o serviço está de pé e o 401 é comportamento normal, não avaria.** **Por
   apurar:** se o registo conclui e se o token é gratuito. **Baixa prioridade** — o
   OpenPlantbook cobre a necessidade e integra-se directamente no Home Assistant, o que o
   Trefle não faz.

4. **~~O OpenPlantbook tem DLI e condutividade?~~ FECHADO pelo lado do consumidor, não do
   fornecedor.** O `homeassistant-plant` trata limiares de **condutividade, iluminância,
   humidade do ar, CO2 e temperatura de solo**, e **deriva DLI e VPD** (ver §3.6). Logo o par
   serve. **O que fica por apurar** é se os **valores por espécie** do OpenPlantbook cobrem
   todos esses campos ou se alguns ficam por preencher à mão — e, em particular, se traz
   valores para ***Phoenix canariensis*, *Celtis australis*** e citrinos. **Para fechar:**
   consultar essas quatro espécies na API. Tentei aceder à documentação da API e a
   `open.plantbook.io/docs.html` devolve apenas a página de login; a documentação real está em
   `/api/docs/` (Swagger), que **não consultei**.

5. **~~Licença do `pyfao56`.~~ FECHADO.** `LICENSE.md` declara **domínio público dos EUA +
   CC0 1.0 Universal**. O `NOASSERTION` do API era falta de classificação automática, não
   ausência de licença.

6. **`aegro/skills` não verificado no repositório de origem.** Só apareceu num directório de
   plugins. Baixa prioridade — pelo perfil (ERP agrícola brasileiro) é gestão, não técnica.

7. **`PyTLidar` não localizado no GitHub.** Descrito num preprint do EcoEvoRxiv como port Python
   do TreeQSM. A busca por `PyTLidar QSM` não devolveu repositórios. **Para fechar:** ler o
   preprint. **Baixa prioridade** — a objecção de arquitectura (QSM é para árvores ramificadas,
   a palmeira não é) invalida-o independentemente de existir.

8. **`PMC12583683` (Sci. Rep. 2025/26) não lido integralmente.** É o trabalho de ML acústico
   mais recente de RPW. Não verifiquei a declaração de disponibilidade de código. **Para
   fechar:** abrir o artigo e procurar *Data availability*. **É o único buraco que poderia
   alterar a conclusão do §3.3.**

9. **Termos de licença do dataset TreeVibes no Kaggle.** A página bloqueia por reCAPTCHA. O
   Zenodo equivalente é **CC-BY 4.0 confirmado**, o que torna isto pouco relevante.

10. **Nenhuma ferramenta open source encontrada para FLL ou EN 13948.** Procurei. Não apurei
    nada — nem calculadora de camadas, nem base de dados de substratos conformes, nem
    verificador. **Interpretação minha:** é matéria de catálogo de fabricante (ZinCo,
    Optigreen, Sika), não de software livre, e a pesquisa do David já cobre o essencial.

11. **Formato do `REGISTO-DOCUMENTOS.md`.** O `REGISTO-DOCUMENTOS-INSTRUCOES.md` (2026-09-18)
    define oito colunas e quatro níveis de Dono; o `REGISTO-DOCUMENTOS.md` ainda está no formato
    antigo de três. **Segui o formato antigo**, por instrução expressa do enunciado de não
    reorganizar. **Fica assinalado para quem fizer a migração.**

---

## Nota final de método

Toda a verificação de vida dos repositórios foi feita contra a **API pública do GitHub**
(`pushed_at`, `stargazers_count`, `license.spdx_id`, `archived`) a **2026-09-18**, não por
leitura de páginas web — as páginas de projecto mentem por omissão, o campo `pushed_at` não.
Onde uma afirmação vem da documentação do projecto e não de verificação independente, está
escrito. **Nenhum nome de repositório, contagem de estrelas, licença ou data foi estimado:**
onde não apurei, escrevi «não apurado» e disse o que faltaria.

**A conclusão mais importante é negativa**, e é registada como tal por ser útil: **não há
agentes de domínio para adoptar.** O que há são **pontes para as ferramentas que já estavam
escolhidas** — e é aí, e só aí, que esta pesquisa acrescenta alguma coisa.
