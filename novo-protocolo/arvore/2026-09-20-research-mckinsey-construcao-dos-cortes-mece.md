---
title: "A construcao da arvore MECE: tipologia de cortes e pluralidade de cortes validos"
date: 2026-09-20
type: research
case: mckinsey
tags: [MECE, arvore, research]
---

# A construcao da arvore MECE: tipologia de cortes e pluralidade de cortes validos

## 0 · Sumário executivo

- Seis famílias de corte, por robustez lógica decrescente: algébrico, processual, segmentação, binário, frameworks de prateleira, dedutivo/indutivo.
- **Há sempre mais do que um corte válido.** A CraftingCases demonstra-o com **13 estruturas MECE distintas** para o mesmo caso; a MConsultingPrep documenta seis para "o lucro está a cair".
- Seis critérios de escolha entre cortes concorrentes, sendo o mais subtil a **integridade do driver** — não partir a causa provável por vários ramos.
- O caso do salmão do Pacífico é o exemplo canónico de corte mal escolhido: a política pública atravessava todos os ramos.
- **Uma fonte de prep admite que a árvore de lucro canónica não é estritamente MECE**, porque preço e quantidade estão correlacionados.
- Vários enunciados correntes são folclore: o corte binário como "único MECE", o desenho "da direita para a esquerda", o termo *tree-off*.

---

## 1 · Mandato

**Prompt dado ao analista.** Investigar a construção da árvore — os tipos de corte, como se escolhe um, e o facto de existirem sempre múltiplos cortes válidos para o mesmo problema:

1. Taxonomia dos cortes MECE, com exemplos: algébrico/value driver, processual/cadeia de valor, segmentação, binário, frameworks de prateleira, dedutivo vs. indutivo em Minto.
2. **A questão central:** há sempre mais do que um corte válido. Como se escolhe? Critérios de selecção. A prática de desenhar 2-3 árvores alternativas antes de comprometer.
3. Regras de profundidade e forma: níveis, quando parar, folhas testáveis, número de ramos, simetria, mesmo nível de abstracção.
4. Poda e priorização: 80/20, matriz impacto × facilidade, derivação do plano de trabalho.
5. O artesanato físico: quadro, Post-its, ferramentas actuais.
6. Exemplos reais do mesmo problema cortado de duas ou mais maneiras MECE.

---

## 2 · Método

Três camadas de autoridade declaradas e sinalizadas ao longo do texto: **(a)** fonte-firma ou autor primário; **(b)** prática de ex-consultor; **(c)** sites de preparação de entrevista, marcados `[prep]`.

A camada (c) é a mais detalhada sobre tipologia de cortes e simultaneamente a menos autoritativa — é codificação pedagógica para entrevistas, não documentação interna. Essa tensão é declarada em vez de resolvida.

**Tabela final de folclore:** cada afirmação corrente que não se confirmou fica registada com o seu estatuto, para não voltar por outra via.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

**Tipologia de cortes, escolha do corte e a pluralidade de cortes válidos**

> Memo de analista #2 de 3. Investigação autónoma, base documental própria.
> Ver também: `2026-09-20-research-mckinsey-front-end-e-definicao-do-problema.md`, `2026-09-20-research-mckinsey-vida-teste-e-fim-da-arvore.md`, e a síntese `2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey.md`.

**Âmbito:** Foca-se na *engenharia* da árvore (issue tree / logic tree), não na definição de MECE nem na comunicação dos resultados.

**Nota de método e fiabilidade:** as fontes dividem-se em três camadas de autoridade, sinalizadas ao longo do texto. (a) **Fonte-firma/autor primário** — McKinsey.com (podcast dos sete passos), Conn & McLean, Minto, Chevallier (académico, IMD/Oxford UP). (b) **Prática ex-consultor** — StrategyU (Paul Millerd, ex-McKinsey/BCG), Stratechi (ex-McKinsey), Umbrex. (c) **Sites de preparação de entrevista** — CraftingCases, MConsultingPrep, HackingTheCaseInterview, Analyst Academy. A camada (c) é a **mais detalhada e explícita** sobre tipologia de cortes — mas é uma codificação *pedagógica* feita para entrevistas, não documentação interna de firmas. Onde uma afirmação existe apenas em (c), assinalo com **[prep]**.

---

### 1. Taxonomia dos cortes (lógicas de ramificação)

A codificação mais completa e citada é a das **"5 formas de ser MECE"** da CraftingCases **[prep]**, que organiza os cortes em três técnicas centrais e duas auxiliares. Cruzei-a com a lista de cinco decomposições da MConsultingPrep (matemática, segmentos, etapas, lados opostos, *stakeholders*) e com as quatro "lentes" da Analyst Academy (*stakeholder, process, segment, math*) — as três listas convergem substancialmente.

#### 1.1 Corte algébrico / equação (*equation trees*, *value driver trees*, *lever trees*)

Decompõe uma métrica pela sua própria fórmula. É o corte com garantia estrutural mais forte: *"Algebraic structures guarantee MECEness because a formula has to yield the target metric"* (CraftingCases).

```
Lucro
├── Receita
│   ├── Preço médio
│   └── Volume
│       ├── N.º de clientes
│       └── Frequência de compra
└── Custo
    ├── Variável
    └── Fixo
```

Variantes documentadas: *Lucro = Receita × % Margem*; *Margem de contribuição − Custos fixos*; custo de contratação = *n.º contratados × custo por contratação*. A Stratechi (ex-McKinsey) e a McKinsey Value-Based Management estendem isto a **value driver trees** com nós de crescimento de receita, margem operacional, rotação do fundo de maneio e intensidade de capital. Limites registados: não serve problemas qualitativos (risco, preferências), é fraco em questões estratégicas de longo prazo e "achata" a realidade em números.

#### 1.2 Corte processual / sequencial / cadeia de valor

Trata o problema como um processo com início, meio e fim: funil de vendas, jornada do cliente, linha de produção, ciclo de cobrança, desenvolvimento de produto. Em Minto isto corresponde à **"time order"** (ordem temporal), uma das três ordens lógicas admissíveis.

```
Porque caem as vendas online?
├── Tráfego (visitas)
├── Conversão em carrinho
├── Conclusão de checkout
└── Retenção / recompra
```

Ponto forte citado: *"You can't miss a thing because you're covering the whole process"* (CraftingCases). Fraqueza: falhar ou trocar a ordem de uma etapa; e nem todos os problemas *têm* um processo subjacente.

#### 1.3 Corte por segmentação

Fatiar por cliente, geografia, produto, canal, tempo. Corresponde à **"structural order"** de Minto (dividir um todo em partes, exigindo-se aí MECE). Serve sobretudo para revelar **efeitos de mix** — quando a média não se move mas o peso dos segmentos sim (o exemplo das fraldas que "baratearam" apenas porque os clientes migraram para o canal online).

Aviso explícito: a segmentação é MECE por construção mas *"will only generate insight if you have chosen the right segmentation criterion"* (CraftingCases). Daí a recomendação de a usar como **tempero e não como prato principal** — camada complementar, raramente primeira camada.

#### 1.4 Corte binário / dicotómico ("opposite words")

Interno vs. externo, oferta vs. procura, financeiro vs. não financeiro, curto vs. longo prazo, estratégico vs. operacional, controlável vs. não controlável.

**Flag de contradição.** O enunciado corrente de que o corte binário é *"o único garantidamente MECE"* não é o que as fontes dizem. A CraftingCases atribui a garantia de MECE tanto ao corte binário como ao algébrico; e um resumo de prep encontrado avisa o contrário — *"two branches are not automatically MECE"* — porque "interno vs. externo" só é exaustivo se o universo estiver bem definido. **Tecnicamente**, só o par lógico *A / não-A* é MECE por definição; "oferta vs. procura" é uma dicotomia substantiva, não lógica. Trato a afirmação forte como **folclore de prep**.

O custo do corte binário é reputacional, não lógico: *"Any parrot can say 'external vs. internal'"* (CraftingCases) — estrutura sem insight, e reconhecível à distância.

#### 1.5 Cortes de prateleira (frameworks conceptuais)

3Cs, 4Ps, Porter, 7S, *business system*, e o trio "People / Process / Systems" (descrito como de uso corrente na McKinsey para temas organizacionais) **[prep]**.

Os avisos contra forçar são consistentes e vêm de várias camadas:

- Rasiel (*The McKinsey Way*), via resumos secundários: não enfiar os factos no *framework* *"like square pegs into round holes"*. **Flag:** citação verificada apenas em resumos/reviews, não no texto original — tratar como paráfrase fiável, não como citação exacta.
- CraftingCases: melhor dominar poucos e *"adapt the hell out of them"*, porque *"every case is unique"*.
- MConsultingPrep é o mais frontal: *"there is no truly 'good' framework"* — escolhe-se o mais simples e utilizável.

#### 1.6 Dedutivo vs. indutivo (Minto) e o que a firma prefere

Minto separa dois modos de agrupar ideias sob um ponto-mãe:

- **Dedutivo** — cadeia premissa maior → premissa menor → conclusão. Cada passo depende do anterior; se um cai, cai tudo.
- **Indutivo** — ideias do mesmo tipo que, somadas, sustentam a ideia-mãe. Resistente: se um ponto é rebatido, os restantes seguram a conclusão.

A preferência consultiva documentada é **indutiva**, por robustez perante contestação em sala e por ser mais rápida de absorver (StrategyU). Minto acrescenta três regras de agrupamento — ideias do mesmo tipo, a ideia superior resume as inferiores, e ordem lógica obrigatória (temporal, estrutural ou de grau).

Conn & McLean transpõem a distinção para a árvore: **árvores indutivas** sobem da observação para a generalização e exibem relações *probabilísticas, não causais*; **árvores dedutivas** descem do princípio para o caso. A sua tipologia completa: *component/factor trees*, *lever trees*, *inductive*, *deductive*, *hypothesis trees*, *decision trees*. A regra prática: **component/factor trees no início** (quando se sabe pouco, listam-se factores sem assumir relações), **hypothesis trees depois** da primeira volta de dados.

Chevallier propõe simplificar toda esta babel terminológica por **função**: árvores de diagnóstico ("porquê") vs. árvores de solução ("como"), com a interdição explícita *"You can't mix 'why' and 'how' questions in one same tree"*.

---

### 2. A questão central: há **sempre** mais do que um corte válido

Esta é a parte mais bem documentada e a mais sistematicamente omitida pelos tratamentos superficiais de MECE.

**Evidência primária (McKinsey).** No podcast McKinsey sobre os sete passos, Charles Conn identifica a desagregação como o seu passo preferido e descreve a prática: *"I love to do two or three different cuts at it"*, cada um dando um insight diferente. A mesma peça afirma que a **forma como se desagrega já dá, muitas vezes, a resposta**.

**Evidência do livro.** Resumo de *Bulletproof Problem Solving* regista a instrução como regra anti-enviesamento: *"Always try multiple trees / cleaves"* — desenhar a mesma questão sob lógicas diferentes é o antídoto contra o enquadramento único. A metáfora recorrente do livro é a do **corte do diamante**: a árvore certa "abre" o problema ao longo das suas linhas naturais e torna a solução óbvia. **Flag:** cito via resumos (O'Reilly bloqueou a leitura integral do Capítulo 3); o teor é confirmado por três resumos independentes.

**Evidência de prep.** A CraftingCases é a mais explícita: *"There are many MECE ways to break down any problem"*, e demonstra-o construindo **13 estruturas MECE distintas** para o mesmo caso (quota de mercado da Nespresso). Quando há dúvida entre duas, a instrução é literal: *"build an issue tree for each and later compare"* — o equivalente artesanal de um confronto entre árvores.

**Flag terminológico:** o termo "*tree-off*" **não aparece em nenhuma fonte lida**. A *prática* está bem documentada; o nome parece ser folclore ou jargão oral. Os termos que aparecem são "different cuts", "multiple cleaves", "alternative disaggregations".

#### Critérios de escolha entre cortes concorrentes

Sintetizando as fontes, seis critérios recorrentes:

1. **Poder de insight** — *"Insight means you're showing fundamental characteristics of the problem"*; o corte deve gerar uma hipótese, *"otherwise it is just random"* (CraftingCases).
2. **Eficiência / capacidade de eliminar** — *"Efficient means you can prioritize or eliminate whole parts"* com pouca informação. É o critério de **falsificabilidade**: um bom corte permite matar ramos cedo.
3. **Quantificabilidade e disponibilidade de dados** — escolher o corte para o qual os dados existem e permitem dimensionar cada ramo.
4. **Alinhamento com a operação e as alavancas reais do cliente** — a Stratechi insiste em construir a árvore *na linguagem e nos elementos da organização*; a CraftingCases mostra porquê: para um supermercado, "n.º de transações × valor médio" bate "preço × quantidade", que obscurece como o retalho realmente gera lucro.
5. **Não partir o driver da resposta entre ramos** — o caso do salmão do Pacífico em *Bulletproof* é o exemplo canónico: a "política governamental" aparecia como ramo próprio quando na verdade **atravessava todos os outros ramos**; só após reestruturar a árvore surgiu clareza.
6. **Accionabilidade** — o corte deve terminar em coisas que alguém pode mover.

---

### 3. Profundidade e forma

- **Número de ramos:** regra dos 3–5. A MConsultingPrep defende três como *"the most intuitive number to the human mind"*; 2 ou 4 aceitáveis; acima de 5, evitar **[prep]**.
- **Profundidade:** CraftingCases — *"no less than 2 layers and no more than 5"*. Conn & McLean trabalham a 3–4 níveis (*trunks → branches → twigs → leaves*). Consenso prático: 3 níveis para problemas estratégicos, 4–5 para análise operacional de causa-raiz.
- **Critério de paragem:** parar quando os baldes *explicam razoavelmente* o problema, ou quando a folha é uma **hipótese testável com uma análise discreta**. O plano de trabalho McKinsey materializa isto: cada folha vira hipótese com análise, produto final, fonte e prazo.
- **Mesmo nível de abstracção:** todos os ramos de um nível devem ser do mesmo tipo lógico (Minto: *same kind rule*). Erro clássico citado: pôr "América do Norte" ao lado de "Índia".
- **Assimetria:** nenhuma fonte exige simetria. Pelo contrário, a Analyst Academy avisa que *"going very deep in low-leverage branches wastes time"* — a assimetria de profundidade é sinal de priorização, não de falha.
- **Não interligar ramos:** ramos devem permanecer independentes, sob pena de a mesma causa-raiz aparecer em dois sítios.

---

### 4. Poda, priorização e derivação do plano de trabalho

A matriz de priorização de Conn & McLean é um **2×2 impacto × capacidade de mover a alavanca**. O critério, no podcast McKinsey: *"How important is this lever?"* e *"How much can I move that lever?"*. O salmão outra vez: as condições oceânicas eram importantes mas imóveis → recursos redireccionados para habitat e práticas de pesca.

Regra de poda, na formulação do livro: não reter elementos da desagregação com pouca influência **ou** impossíveis de afectar. Sobrepõe-se o 80/20 — concentrar nos 20% do problema que dão 80% do benefício; o objectivo é o **caminho crítico**.

Do que sobrevive nasce o plano de trabalho. Componentes documentados (Umbrex, convergente com Conn & McLean):

| Elemento | Conteúdo |
|---|---|
| Hipótese | a folha, formulada como afirmação falsificável |
| Análises | actividade concreta a executar |
| *End product* | o output esperado — **esboçar o gráfico antes de o fazer** |
| Fontes | onde estão os dados/peritos |
| Responsável e prazo | *"We are very specific about who is doing what by when"* |

Duas regras de sequenciamento: *"Do knock-out analyses first"* (as que eliminam decisões) e manter o plano detalhado só a **2–3 semanas**, revendo continuamente. Liga-se à *one-day answer* / *Day One Hypothesis*: uma resposta provisória desde o primeiro dia, que a árvore serve para testar.

---

### 5. O artesanato físico

Esta secção é a **mais fracamente documentada** — muito do que circula é folclore.

Confirmado: as árvores desenham-se **da esquerda para a direita**, com a raiz à esquerda, virando a folha ao alto — justificação explícita nas fontes de prep: os quadros brancos são mais largos do que altos. Também se aceita a orientação vertical.

**Flag:** a afirmação de que os consultores desenham "da direita para a esquerda" **não foi encontrada em nenhuma fonte**. É plausível que confunda duas coisas distintas: (i) o desenho *left-to-right* da árvore, e (ii) o raciocínio *top-down* da Pirâmide de Minto, que parte da resposta. Trato "right-to-left" como **folclore**.

Igualmente **não confirmado por fonte**: a regra de que "a árvore vive em papel e não em PowerPoint na fase inicial" e o uso ritual de Post-its. É consistente com a prática descrita (processo iterativo, revisto continuamente, plano a 2–3 semanas), mas nenhuma das fontes lidas o afirma.

Ferramentas actuais confirmadas: **Miro** (tem template "Building a Driver Tree" e "Problem Tree"; descrito como orientado a facilitação e síntese com equipas remotas), **Lucidchart** (edição em tempo real, templates de árvore) e folhas de cálculo para *driver trees* quantificados.

---

### 6. Exemplos trabalhados: o mesmo problema, cortes diferentes

#### 6.1 "O lucro está a cair" — seis variantes documentadas

A MConsultingPrep documenta **seis estruturas alternativas válidas** para o mesmo problema **[prep]**, com condições de uso:

```
CORTE A — unitário          CORTE B — por cliente        CORTE C — por segmento
Lucro                        Lucro                        Lucro
├─ Receita                   ├─ Receita                   ├─ Linha de negócio 1
│  ├─ Preço unitário         │  ├─ N.º clientes           ├─ Linha de negócio 2
│  └─ Quantidade             │  └─ Receita/cliente        └─ Linha de negócio 3
└─ Custo                     └─ Custo                        (cada uma → Rec./Custo)
   ├─ Custo unitário            ├─ N.º clientes
   └─ Quantidade                └─ Custo/cliente
```

As outras três: operacional vs. não operacional (lado da receita); por função/departamento (lado do custo, útil quando se suspeita de uma função específica); fixo vs. variável (*"fundamentally MECE and applicable for every business"*).

Observação crítica registada pela própria fonte: o Corte A *"is not strictly MECE"*, porque preço e quantidade estão correlacionados. **É um caso raro em que uma fonte de prep admite que a árvore canónica do sector viola tecnicamente a exclusividade mútua.**

#### 6.2 Rentabilidade de companhia aérea — "porquê" vs. "onde"

```
CORTE 1 (identidade contabilística)      CORTE 2 (segmentação)
Lucro                                     Lucro
├─ Receita                                ├─ Doméstico / Internacional
│  ├─ Yield por lugar                     ├─ Curto / longo curso
│  └─ Load factor × capacidade            └─ Por rota
└─ Custo                                     (cada um → Receita/Custo)
   ├─ Fixo (frota, tripulação)
   └─ Variável (combustível, taxas)
```

A diferença é de pergunta, não de correcção: o Corte 1 diagnostica **porquê** caiu a rentabilidade; o Corte 2 diagnostica **onde**. Na prática constrói-se um e usa-se o outro como segunda camada — nunca misturados no mesmo nível (misturar rota com categoria financeira viola a exclusividade mútua).

#### 6.3 Custos — comportamento vs. função

Exemplo curto e limpo da CraftingCases: reduzir custos admite **Fixo vs. Variável** (quando a pergunta é sobre alavancagem face ao volume) ou **COGS / SG&A / I&D / Outros** (quando o CEO quer saber *que departamento cortar*). Ambos MECE; a regra é **não misturar na mesma árvore**.

#### 6.4 "Como salvar o salmão do Pacífico?" (problema público, *Bulletproof*)

Caso não-lucrativo usado pela McKinsey. Lições registadas: (i) a primeira árvore falhou por sobreposição — a política pública atravessava todos os ramos; (ii) após reestruturação, a priorização por *importância × capacidade de mover* eliminou "condições oceânicas" (importante, imóvel) e concentrou o esforço em habitat e práticas de captura; (iii) a desagregação organizou um esforço de **15 anos**.

---

### 7. Contradições e folclore — síntese dos flags

| Afirmação | Estatuto |
|---|---|
| Corte binário é o **único** garantidamente MECE | **Folclore.** Fontes atribuem a garantia também ao corte algébrico; e avisam que duas ramificações não são automaticamente MECE. Só *A/não-A* é MECE por definição lógica. |
| Prática do "*tree-off*" | **Prática confirmada, nome não confirmado.** Fontes dizem "two or three different cuts", "multiple cleaves". |
| Desenhar a árvore "da direita para a esquerda" | **Não confirmado.** Fontes dizem esquerda→direita. Provável confusão com o *top-down* de Minto. |
| "A árvore vive em papel, não em PowerPoint" / Post-its | **Não confirmado por nenhuma fonte lida.** Plausível, mas folclore até prova em contrário. |
| MECE é condição suficiente de boa estrutura | **Contradito.** van Gelder: MECE *"does not exclude superfluous/extraneous items"*. Chevallier: há casos em que *"redundancies are desirable or even necessary"*. StrategyU: MECE é *"an ideal, not a law"*, e admite sobre a sua própria árvore: *"This tree is not perfect"*. |
| McKinsey "prefere" lógica indutiva | **Sustentado mas indirecto.** A preferência vem de Minto e de intérpretes (StrategyU, prep), não de documento da firma. |
| Regra "3 ramos" | **[prep] apenas.** Conn & McLean não a enunciam; falam de 3–4 níveis, não de largura. |

---

---

## 4 · Fontes

**Camada firma / autor primário**

- `mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-master-the-seven-step-problem-solving-process` — podcast McKinsey com Charles Conn e Hugo Sarrazin. **A fonte primária mais forte** para "two or three different cuts", priorização por alavanca e caso do salmão. *Acesso directo bloqueado (timeout/ECONNRESET); conteúdo obtido via snippets de pesquisa e via espelho.*
- `pdfcoffee.com/how-to-master-the-seven-step-problem-solving-process-pdf-free.html` — espelho não oficial do transcript acima. Fiável quanto ao conteúdo, não quanto à integridade; usado apenas para confirmação cruzada.
- `oreilly.com/library/view/bulletproof-problem-solving/9781119553021/c03.xhtml` — Capítulo 3 ("Problem Disaggregation and Prioritization"). **Fonte ideal, inacessível** (403/paywall). Conteúdo reconstruído por triangulação de três resumos.
- `en.wikipedia.org/wiki/MECE_principle` — origem (Minto, anos 60) e secção de críticas com atribuições verificáveis (van Gelder 2010; Chevallier 2016). Fiável para *quem* criticou e *o quê*.
- `powerful-problem-solving.com/dont-get-lost-in-the-terminology` — Arnaud Chevallier (IMD; Oxford University Press). **Académico/prático de alta qualidade**; melhor fonte para a arrumação diagnóstico vs. solução.
- `global.oup.com/academic/product/strategic-thinking-in-complex-problem-solving-9780190463908` — ficha do livro de Chevallier (17 frameworks conceptuais, pp. 72-74). Apenas metadados; texto não lido.

**Camada ex-consultor / prática**

- `strategyu.co/wtf-is-mece-mutually-exclusive-collectively-exhaustive/` — Paul Millerd (ex-McKinsey/BCG). Bom para história de Minto e para o enquadramento "MECE é ideal, não lei". Leve, sem tipologia de cortes.
- `strategyu.co/issue-tree/` — mesma casa. Valioso pela **honestidade** ("esta árvore não é perfeita"). Pouca tipologia.
- `strategyu.co/pyramid-principle-partone/` — melhor fonte lida para dedutivo vs. indutivo e "same level of abstraction".
- `stratechi.com/profit-trees/` — Joe Newsum, ex-McKinsey. **Excelente** para árvores de lucro à medida e para o princípio de as construir na linguagem da organização.
- `umbrex.com/resources/mckinsey-problem-solving/` — rede de ex-McKinsey. Melhor fonte lida para os **componentes do plano de trabalho** (análises, end products, fontes, timing, responsabilidade).

**Camada preparação de entrevista [prep] — detalhada mas pedagógica**

- `craftingcases.com/the-5-ways-to-be-mece-part-2/` a `part-9/` (8 páginas lidas: geral, algébrico, processo, frameworks conceptuais, segmentações, palavras opostas, construção de árvores, mestria). **A fonte mais rica e explícita sobre tipologia de cortes e sobre a pluralidade de cortes válidos** (13 estruturas para a Nespresso). Enviesada para contexto de entrevista.
- `craftingcases.com/issue-tree-guide/` — regras de profundidade (2–5 camadas), diagnóstico vs. solução, critérios de escolha.
- `craftingcases.com/profitability-tree-guide/` — cinco decomposições alternativas do lucro e critérios de personalização. Muito bom no argumento "alinhar com a mecânica real do negócio".
- `mconsultingprep.com/issue-tree` — cinco tipos de decomposição, regra dos três, mesmo nível de abstracção, "no truly good framework".
- `mconsultingprep.com/profitability-case-framework` — **as seis variantes do mesmo problema**; notável por admitir que a variante canónica não é estritamente MECE.
- `theanalystacademy.com/issue-tree-and-logic-tree-framework/` — quatro lentes (stakeholder/process/segment/math), aviso contra profundidade em ramos de baixa alavanca. Sólido mas genérico.
- `readinggraphics.com/book-summary-bulletproof-problem-solving/` — resumo do livro; fonte para a lista dos cinco/seis tipos de árvore. Secundário.
- `sellingsherpa.com/.../bulletproof-problem-solving-book-summary/` — resumo com **citações curtas do livro**. Secundário mas o mais citacional dos resumos.
- `github.com/chefjefff/mckinsey-problem-solving/.../SKILL.md` — destilação de terceiros do método (testar 2-3 desagregações alternativas, 2×2 impacto/capacidade, regras do workplan). **Não autoritativo**; usado só como confirmação cruzada.
- `miro.com/templates/building-a-driver-tree/` e `miro.com/templates/problem-tree/` — confirmação factual das ferramentas actuais.

**Fontes tentadas e inacessíveis:** `hackingthecaseinterview.com/pages/issue-trees` (403), `igotanoffer.com/.../issue-tree` (403), `qz.com/work/1682272` (403), `catalogimages.wiley.com/.../9781119553021.excerpt.pdf` (PDF binário não extraível), texto integral de Rasiel em `ndl.ethernet.edu.et` (socket hang up). As afirmações que dependiam delas estão sinalizadas como não confirmadas ou citadas via secundários.
