---
created: 2026-09-15
project: Jardim
thread: T001
tipo: pesquisa
summary: >
  Estado da arte sobre caracterização e levantamento de espaço exterior privado:
  paisagismo, solo, luz, vegetação, geometria, infra-estrutura, ferramentas abertas
  e permacultura. Com ficha-modelo de campos e sequência de levantamento.
nota_de_producao: >
  Investigação por subagente research-analyst. O subagente não dispunha de ferramenta
  de escrita; o texto foi redigido a partir do relatório devolvido, sem acrescentar
  factos nem fontes que ele não tenha reportado.
---

# Estado da arte — caracterização de espaço exterior privado

Pesquisa motivada pelo quintal de 75 m² da Calçada da Boa Hora 15, Alcântara. O objecto da pesquisa é o **método**, não o quintal.

---

## Sumário executivo

**Não existe norma obrigatória para caracterizar um jardim doméstico.** Nem em Portugal, nem na Europa, nem globalmente. O que existe é convergência de prática entre escolas — não uma ISO, nem um equivalente europeu ao ANSI A300 americano.

Cinco achados que alteram o modo de trabalhar:

1. **A distinção facto ≠ decisão é a base metodológica da disciplina**, não uma invenção deste projecto. A NYBG separa explicitamente *inventory* (factos brutos) de *analysis* (interpretação para projecto).
2. **Percolação é o teste mais barato e mais decisivo que existe.** Custo zero, meio-dia de trabalho, e condiciona toda a escolha de vegetação. Vem antes de qualquer demolição.
3. **DLI não tem atalho.** Ou ≈460 € e duas semanas de medição real, ou 15–30 h de simulação Radiance com incerteza maior. **Lux não serve** para decisão hortícola — as fontes são unânimes.
4. **Não existe ferramenta open source pronta** para caracterizar um jardim doméstico. Os schemas existentes são municipais e grandes demais; os projectos de permacultura no GitHub são caso a caso.
5. **A palmeira inspecciona-se pela coroa, não pelo tronco**, para sinais de *Rhynchophorus ferrugineus*. Detalhe operacional que inverte o instinto.

---

## 1. Paisagismo e arquitectura paisagista

Não há norma única. Há **convergência de conteúdo** entre escolas anglo-saxónicas.

A referência mais estruturada e citável encontrada é o guia da **New York Botanical Garden**, que distingue:

| Fase | Natureza |
|---|---|
| **Inventory** | Factos brutos sobre o sítio |
| **Analysis** | Interpretação desses factos para o projecto |

Campos-tipo do inventário: elementos construídos (caminhos, vedações, infra-estrutura); elementos naturais (árvores, afloramentos, vistas); factores climáticos (vento, sol/sombra, topografia, tipo de solo); vegetação (árvores acima de 4" DAP, arbustos, herbáceas).

**Em Portugal:** a APAP **não publica checklist técnico**. O documento *Caracterização da Arquitectura Paisagista em Portugal* (2010) é sobre a profissão, não um manual de método. O curso de Arquitectura Paisagista do ISA tem unidades curriculares de projecto, mas não expõe publicamente sílabos com checklist de levantamento.

> **Achado.** O método existe como **prática de ensino tácita**, não como documento público. Não é anomalia — é o estado da disciplina na Europa.

**Fontes:** [NYBG Site Inventory](https://libguides.nybg.org/siteinventory) · [APAP — Caracterização (PDF)](https://apap.pt/wp-content/uploads/2017/08/CARACTERIZAcaO-DA-ARQUITECTURA-PAISAGISTA-EM-PORTUGAL-Outubro-2010.pdf) · [ISA/ULisboa](https://fenix.isa.ulisboa.pt)

---

## 2. Solo

Hierarquia clara de esforço contra custo.

| Ensaio | Custo | Tempo | O que dá |
|---|---|---|---|
| **Teste do frasco** (jar test) | 0 € | 24–48 h de sedimentação | Textura aproximada, qualitativo |
| **Teste de percolação** | 0 € | Meio-dia + 1 noite | Drenagem em cm/h. **Decisivo.** |
| **pH caseiro** (tiras/kit) | 5–20 € | Minutos | Indicativo, não substitui laboratório |
| **Laboratório — básica** | 10–30 € | < 1 semana | pH, matéria orgânica, macronutrientes |
| **Laboratório — completa** | 30–50 € | < 1 semana | + textura |
| **Laboratório — avançada** | 50–70 € | < 1 semana | + micronutrientes |

### Protocolo de percolação

Furo de 30 × 30 cm. Saturar sem tempo de espera. Medir a descida de água em cm/h no dia seguinte, após saturação durante a noite.

| Resultado | Leitura |
|---|---|
| 1–2 "/h | Bom |
| > 3 "/h | Drenagem excessiva |
| < 0,5 "/h | Drenagem má |

### Laboratórios em Portugal

- **AGQ Labs Portugal** — [agqlabs.pt](https://agqlabs.pt/analise-do-solo/)
- **Laboratório de Solos e Fertilidade, ESA-IPCB** — [labsolos.esa.ipcb.pt](https://labsolos.esa.ipcb.pt/analises/)
- **Eurofins Portugal** — [eurofins.pt](https://www.eurofins.pt/agricultura/an%C3%A1lises-de-solos/)
- **UÉvora / MED** — [tabela de preços (PDF)](https://www.med.uevora.pt/wp-content/uploads/2022/09/tabela-de-precos-prestacao-de-servicos-Set2020.pdf)

Guia em português: [acientistaagricola.pt](https://acientistaagricola.pt/testes-ao-solo-o-que-sao-quanto-custam-e-como-e-onde-fazer/)

> **Ordem correcta: percolação antes de laboratório.** Se a drenagem for inviável, muda toda a estratégia — e a análise química passa a ser irrelevante.

**Fontes:** [Percolation test — Wikipedia](https://en.wikipedia.org/wiki/Percolation_test) · [Iowa State Extension](https://yardandgarden.extension.iastate.edu/how-to/testing-and-improving-soil-drainage)

---

## 3. Luz e microclima

### As três unidades, e porque não se confundem

| Unidade | O que mede | Serve para decisão de plantas? |
|---|---|---|
| **DLI** (mol/m²/dia) | Total diário de fotões úteis | **Sim.** É a unidade correcta. |
| **PAR / PPFD** (µmol/m²/s) | Instantânea | Sim, mas é fotografia, não filme |
| **Lux** | Ponderado à visão humana | **Não.** A relação lux→PAR varia com o espectro |

### Equipamento

**Apogee DLI-500** — ≈460 €. PAR, DLI e fotoperíodo; 99 dias de registo automático; incerteza ±5% NIST. [apogeeinstruments.com](https://www.apogeeinstruments.com/dli-500-par-daily-light-integral-and-photoperiod-meter-full-spectrum-400-700-nm/)

Apps de telemóvel são indicativas. Não substituem sensor calibrado.

### Simulação como alternativa

**Radiance** via `honeybee-radiance` (Python, sem Rhino) é o padrão-ouro open source. **Nenhum software dá DLI directamente** — é sempre irradiância (W/m²) convertida por factor PAR (≈2,0–2,3 µmol/J), com incerteza própria de ±10–15%.

> **Não há atalho.** DLI fiável exige 460 € + duas semanas de medição, ou 15–30 h de simulação com incerteza maior. Não existe app grátis que resolva.

---

## 4. Vegetação existente

### Avaliação de árvores

| Método | Origem | Natureza |
|---|---|---|
| **VTA** — Visual Tree Assessment | Mattheck/Breloer, Alemanha | Referência europeia de facto. Três fases: visual → confirmação instrumental se há suspeita → critério de falha. Revisão tipicamente bienal. |
| **QTRA** — Quantified Tree Risk Assessment | Reino Unido | Complemento quantitativo: risco = alvo × dimensão × probabilidade de falha |
| **ANSI A300** | EUA (ISA) | 10 standards. **Sem equivalente europeu único.** |

A Europa opera por VTA mais normas nacionais de poda fragmentadas (ex.: ZTV alemãs).

**Campos-padrão de inventário arbóreo:** espécie · DAP (medido a 1,30 m) · altura · projecção de copa · estado fitossanitário · estrutura · idade estimada · riscos observados.

### *Phoenix canariensis* e o escaravelho-vermelho

Praga em Portugal desde 2007 (Algarve). Plano de acção da **DGAV** (2013), sob regime de controlo obrigatório da UE.

**Sinais de infestação:** folhas com marcas de rasgão na inserção no tronco · murchidão da coroa · serrim ou exsudado na base das folhas.

> **A vigilância faz-se pela coroa, não pelo tronco** — ao contrário do que o instinto sugere e do que é hábito noutras pragas.

Em zonas afectadas: inspecção visual regular mais armadilhas de feromona.

**Fontes:** [VTA — Wikipedia (IT)](https://it.wikipedia.org/wiki/Visual_Tree_Assessment) · [QTRA](https://qtra.co.uk/about-qtra/) · [CM Tomar — ficha técnica (PDF)](https://www.cm-tomar.pt/images/CMT/municipio/documentos/espacos_verdes/RhynchophorusferrugineusAspetosGerais.pdf) · [CM Lamego (PDF)](https://www.cm-lamego.pt/cmlamego/uploads/writer_file/document/280/ficha_de_divulgacao_palmeiras.pdf) · [Naturdata](https://naturdata.com/especie/Rhynchophorus-ferrugineus/39274/0/)

---

## 5. Levantamento geométrico

| Método | Precisão | Custo | Nota |
|---|---|---|---|
| **Fita + triangulação** | ±1–2 cm | 0 € | Suficiente para espaço pequeno e regular |
| **Distanciómetro laser** | ±1–3 mm | 30–80 € | Rápido. Base para as cotas que importam. |
| **Fotogrametria LiDAR** (Polycam, iPhone/iPad Pro) | Centimétrica | Freemium | Boa para volumetria, **não** para cotas finas. Exporta .obj/.ply/.dxf/.las |
| **Fotogrametria por fotos** (Meshroom, RealityCapture) | Depende de sobreposição e qualidade | 0 € (Meshroom) | Mais lenta; melhor para detalhe de superfície e patologias |

> **Não existe convenção formal de coordenadas locais para jardins pequenos.** A prática é sempre *ad hoc*: origem arbitrária num canto, eixos alinhados aos muros, cotas relativas à soleira.

**Fonte:** [Polycam](https://apps.apple.com/br/app/polycam-lidar-3d-scanner/id1532482376)

---

## 6. Infra-estrutura enterrada

### Detecção não destrutiva

| Meio | Custo | Para quê |
|---|---|---|
| **Corante traçador** | Poucos euros | Confirmar destino de um ralo. **O mais barato e directo.** |
| **Detector de metais/cabos** | 30–150 € | Localizar metal e cabos activos |
| **Câmara endoscópica** | 50–300 € (compra) ou aluguer | Inspeccionar tubagem |

Fornecedor especializado identificado em Lisboa: **J. Roma, Lda.**, Rua Robalo Gouveia 5B.

### Arquivo Municipal de Lisboa

Consulta de processos de obra por marcação prévia, via Loja Lisboa. **Consulta gratuita.** Certidões e cópias certificadas têm custo e prazo até **10 dias úteis**. Processos antigos estão a ser digitalizados, mas a cobertura não é total.

> **Sequência correcta** para um ponto de drenagem de destino desconhecido: (1) processo de obra no Arquivo, se existir planta original; (2) **corante traçador**; (3) câmara endoscópica, só se os dois anteriores não resolverem.

**Fontes:** [Arquivo Municipal](https://arquivomunicipal.lisboa.pt/servicos/consulta-e-reproducao-de-documentos) · [Certidões](https://informacoeseservicos.lisboa.pt/servicos/detalhe/certidao-copia-certificada) · [SciELO — digitalização](https://scielo.pt/scielo.php?script=sci_arttext&pid=S2183-31762015000100013)

---

## 7. Ferramentas e repositórios open source

Existem schemas — **fragmentados e sem adopção**.

| Recurso | O que é | Utilidade aqui |
|---|---|---|
| [**FIWARE ParksAndGardens**](https://github.com/smart-data-models/dataModel.ParksAndGardens) | Schema JSON para parques urbanos, nível municipal | Referência de campos. Grande demais para uso directo. |
| [**Open-Plant-Schema**](https://github.com/JakeHartnell/Open-Plant-Schema) | schema.org para plantas | Projecto pequeno, pouco activo |
| [**permaculture-site-plan**](https://github.com/keser/permaculture-site-plan) | Site plan pessoal real (0,43 acres, Connecticut) | Template inspirador, não reutilizável |
| [**Site-and-Pattern**](https://github.com/yarrowyarrowyarrow/Site-and-Pattern) | App com 433 plantas nativas do Alberta | Flora errada; **o modelo de dados é reutilizável** |
| [**Pl@ntNet API**](https://my.plantnet.org/) | Identificação por imagem + taxonomia, 54 línguas | Útil para identificação de espécies |
| [**iNaturalist API**](https://www.inaturalist.org/api) | Dados de observação | Complementar ao Pl@ntNet |
| [**Ladybug Tools**](https://github.com/ladybug-tools/ladybug) | Simulação ambiental; usa `pvlib` internamente | Padrão-ouro para sol |
| **pvlib-python** | Cálculo de posição solar (BSD) | Já em uso neste projecto |
| **SunCalc** | Posição solar e sombras, web | Simples; não produz DLI |
| **QGIS** · **FreeCAD** | SIG · CAD paramétrico (GPL/LGPL) | Genéricos |

> **Achado central.** Não existe nenhum schema ou ferramenta open source pronta para caracterizar um jardim doméstico de 75 m². O que há é: (a) schemas municipais, grandes demais; (b) projectos pessoais de permacultura, não generalizáveis; (c) bases de dados de plantas com API decente, sem componente de sítio.
>
> **Uma ficha-modelo para este caso preenche um vazio real — não reinventa uma roda existente.**

---

## 8. Permacultura

**Sector analysis** e **zone planning** são metodologia consolidada na tradição Mollison/Holmgren: sobrepõem em planta as energias do sítio — sol de Verão e de Inverno, vento dominante, ruído, água.

Duas críticas, assinaladas pelo investigador como opinião fundamentada e não como fonte:

**«Observar um ano antes de intervir» é parcialmente folclore.** O princípio de observar antes de agir é sólido e coincide com o paisagismo (eixo 1). A prescrição literal de um ano completo **não tem base empírica citável** — é tradição oral do movimento. Para 75 m² com histórico fotográfico disponível, um ciclo anual de observação é desproporcionado face ao que se obtém por medição direccionada mais modelação.

**O zoneamento em 5 zonas concêntricas perde sentido a esta escala.** É ferramenta de propriedade rural. A distinção zona 1 / zona 2 não significa nada num quintal fechado de 75 m².

> **O que a permacultura contribui:** o vocabulário de *sector* — sobreposição de vento, sol, ruído e água em planta — como ferramenta de síntese visual. Nenhuma técnica de medição que os eixos 2–3 não cubram já.

**Fontes:** [Santa Cruz Permaculture](https://santacruzpermaculture.com/2021/02/zone-and-sector-analysis/) · [permaculturepractice.com](https://permaculturepractice.com/permaculture-site-analysis/)

---

## 9. Ficha-modelo de caracterização

Campos por domínio, com método, custo e precisão. **É o produto principal desta pesquisa.**

### Geometria

| Campo | Método | Custo | Tempo | Precisão |
|---|---|---|---|---|
| Dimensões em planta | Fita + triangulação, ou laser | 0–80 € | 1–2 h | ±1–2 cm / ±3 mm |
| Altura de muros | Laser ou fita | 0–80 € | 30 min | ±1–3 cm |
| Cotas verticais e desníveis | Laser ou nível | 0–80 € | 1 h | ±1 cm |
| Volumetria e copas | Fotogrametria LiDAR | Freemium | 1 h campo + 2 h proc. | Centimétrica |
| Orientação e azimute | Planta + verificação solar | 0 € | — | < 1° |

### Solo

| Campo | Método | Custo | Tempo |
|---|---|---|---|
| **Drenagem / percolação** | Furo 30×30, protocolo padrão | 0 € | Meio-dia + 1 noite |
| Textura | Jar test, ou laboratório | 0–50 € | 48 h |
| pH | Tiras, ou laboratório | 5–30 € | Minutos / 1 semana |
| Matéria orgânica | Laboratório | 10–30 € | < 1 semana |
| Macro e micronutrientes | Laboratório | 30–70 € | < 1 semana |
| Profundidade útil | Sondagem manual | 0 € | 1 h |
| Compactação | Penetrómetro, ou vareta | 0–150 € | 1 h |

### Luz e microclima

| Campo | Método | Custo | Tempo |
|---|---|---|---|
| Geometria solar | `pvlib` / NREL SPA | 0 € | Horas |
| Sombreamento por zona | Radiance / honeybee | 0 € | 15–30 h |
| **DLI real** | Apogee DLI-500 | ≈460 € | 7–14 dias por ponto |
| Validação | Fotos datadas com EXIF | 0 € | — |
| Vento dominante | Observação + estação local | 0 € | Meses |
| Temperatura e humidade | Datalogger | 30–100 € | Contínuo |

### Vegetação existente

| Campo | Método | Custo |
|---|---|---|
| Espécie | Pl@ntNet, ou identificação presencial | 0 € |
| DAP | Fita, a 1,30 m | 0 € |
| Altura e projecção de copa | Laser, ou fotogrametria | 0–80 € |
| Estado fitossanitário | VTA (visual) | 0 € |
| Risco | QTRA, se houver alvo | — |
| **Vigilância *Rhynchophorus*** | **Inspecção da coroa**, feromona | 0–100 €/ano |

### Infra-estrutura

| Campo | Método | Custo |
|---|---|---|
| Destino da drenagem | **Corante traçador** | < 10 € |
| Traçado de tubagem | Câmara endoscópica | 50–300 € |
| Cabos e metal enterrado | Detector | 30–150 € |
| Planta original | Arquivo Municipal | 0 € consulta · 10 dias certidão |
| Pontos de água e electricidade | Inspecção visual | 0 € |

### Envolvente

| Campo | Método | Custo |
|---|---|---|
| O que confina | Observação + aérea | 0 € |
| Quem vê / privacidade | Observação nas quatro direcções | 0 € |
| Ruído | Medição por app, ou sonómetro | 0–100 € |
| Acessos para materiais | Observação e medição de vãos | 0 € |

---

## 10. Sequência recomendada

A ordem importa: cada passo condiciona os seguintes.

| # | Passo | Porquê agora |
|---|---|---|
| **1** | **Geometria básica** — fita e laser | Condiciona tudo o resto |
| **2** | **Percolação e ponto de drenagem** | **Eliminatório.** Decide a viabilidade de vegetação de solo. Antes de qualquer demolição. |
| **2b** | Infra-estrutura enterrada | Em paralelo com 2 — mesma escavação |
| **3** | Inventário de vegetação — espécie, DAP, estado; VTA da palmeira | Independente dos anteriores |
| **4** | Luz — medição **ou** simulação | Não ambas em simultâneo à partida |
| **5** | Solo laboratorial | **Só depois** de confirmada a drenagem |
| **6** | Fotogrametria e documentação fina | Quando o resto estabilizar |

---

## 11. Conclusão metodológica

O maior achado é negativo: **não há metodologia única, oficial e citável a seguir cegamente.**

Três consequências práticas:

1. A regra **facto e fonte**, com o desconhecido escrito como desconhecido, é mais rigorosa do que a média do que se encontra publicado.
2. A separação **inventário / análise** — factos numa thread, decisão noutra — coincide com a base metodológica da disciplina.
3. Uma ficha-modelo própria não é improviso por falta de alternativa: **é o que preenche um vazio real** entre schemas municipais e projectos pessoais.

---

## Bibliografia

**Paisagismo** — [NYBG Site Inventory](https://libguides.nybg.org/siteinventory) · [APAP (PDF)](https://apap.pt/wp-content/uploads/2017/08/CARACTERIZAcaO-DA-ARQUITECTURA-PAISAGISTA-EM-PORTUGAL-Outubro-2010.pdf) · [ISA/ULisboa](https://fenix.isa.ulisboa.pt)

**Solo** — [Percolation test](https://en.wikipedia.org/wiki/Percolation_test) · [Iowa State Extension](https://yardandgarden.extension.iastate.edu/how-to/testing-and-improving-soil-drainage) · [AGQ Labs](https://agqlabs.pt/analise-do-solo/) · [ESA-IPCB](https://labsolos.esa.ipcb.pt/analises/) · [Eurofins](https://www.eurofins.pt/agricultura/an%C3%A1lises-de-solos/) · [UÉvora (PDF)](https://www.med.uevora.pt/wp-content/uploads/2022/09/tabela-de-precos-prestacao-de-servicos-Set2020.pdf) · [A Cientista Agrícola](https://acientistaagricola.pt/testes-ao-solo-o-que-sao-quanto-custam-e-como-e-onde-fazer/)

**Luz** — [Apogee DLI-500](https://www.apogeeinstruments.com/dli-500-par-daily-light-integral-and-photoperiod-meter-full-spectrum-400-700-nm/) · [Ladybug Tools](https://github.com/ladybug-tools/ladybug)

**Vegetação** — [VTA](https://it.wikipedia.org/wiki/Visual_Tree_Assessment) · [QTRA](https://qtra.co.uk/about-qtra/) · [CM Tomar (PDF)](https://www.cm-tomar.pt/images/CMT/municipio/documentos/espacos_verdes/RhynchophorusferrugineusAspetosGerais.pdf) · [CM Lamego (PDF)](https://www.cm-lamego.pt/cmlamego/uploads/writer_file/document/280/ficha_de_divulgacao_palmeiras.pdf) · [Naturdata](https://naturdata.com/especie/Rhynchophorus-ferrugineus/39274/0/)

**Geometria** — [Polycam](https://apps.apple.com/br/app/polycam-lidar-3d-scanner/id1532482376)

**Infra-estrutura** — [Arquivo Municipal de Lisboa](https://arquivomunicipal.lisboa.pt/servicos/consulta-e-reproducao-de-documentos) · [Certidões](https://informacoeseservicos.lisboa.pt/servicos/detalhe/certidao-copia-certificada) · [SciELO](https://scielo.pt/scielo.php?script=sci_arttext&pid=S2183-31762015000100013)

**Open source** — [FIWARE ParksAndGardens](https://github.com/smart-data-models/dataModel.ParksAndGardens) · [Open-Plant-Schema](https://github.com/JakeHartnell/Open-Plant-Schema) · [permaculture-site-plan](https://github.com/keser/permaculture-site-plan) · [Site-and-Pattern](https://github.com/yarrowyarrowyarrow/Site-and-Pattern) · [Pl@ntNet API](https://my.plantnet.org/) · [iNaturalist API](https://www.inaturalist.org/api)

**Permacultura** — [Santa Cruz Permaculture](https://santacruzpermaculture.com/2021/02/zone-and-sector-analysis/) · [permaculturepractice.com](https://permaculturepractice.com/permaculture-site-analysis/)
