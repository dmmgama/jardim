---
title: "Transferencia da decomposicao MECE para fora da estrategia empresarial"
date: 2026-09-20
type: research
case: dominios
tags: [MECE, arvore, research]
---

# Transferencia da decomposicao MECE para fora da estrategia empresarial

## 0 · Sumário executivo

- **Texto integral de *Bulletproof Problem Solving* obtido e lido**, o que permite citar os casos reais e desmentir atribuições correntes.
- **Não existe no livro** nenhum caso de "comprar vs. arrendar" nem de direitos indígenas / *native title*. Ambos circulam atribuídos.
- O caso do salmão mostra **a árvore errada primeiro**: a política governamental atravessava todos os ramos — falha de exclusividade mútua, não de exaustividade.
- O caso da sobrepesca é **o mais honesto do livro e o menos favorável ao método**: as três opções da árvore falharam e a solução veio de fora dela, por analogia.
- **Onze métodos cognatos** inventados independentemente; só FTA e WBS exigem exaustividade formal.
- Cinco condições em que a transferência se parte, sendo a mais citável de Gasper: *"To date, LFA has predominantly been a tool of the powerful."*
- O que viaja melhor do que a regra MECE é o **catálogo de cortes** (*cleaving frames*).

---

## 1 · Mandato

**Prompt dado ao analista.** Investigar como a decomposição MECE tem sido efectivamente aplicada fora da estratégia empresarial, e o que muda na transferência:

1. Aplicações não-empresariais documentadas, com a estrutura real das árvores e não apenas a anedota.
2. Métodos cognatos estruturalmente equivalentes, inventados independentemente: Fault Tree Analysis, Ishikawa, 5 Porquês, FMEA, Problem Tree do logframe e ZOPP, Kepner-Tregoe, A3 Toyota, diagnóstico diferencial, taxonomia lineana e cladística, WBS, mind maps. Para cada um: quem o inventou, qual a regra de ramificação, se exige exaustividade, e em que difere de uma issue tree.
3. O que se parte ou tem de ser adaptado na transferência.
4. Ensino e difusão fora da consultoria.

---

## 2 · Método

Leitura do texto integral do livro a partir de PDF público, com extracção por `pdftotext`. Isto permite reportar **texto real** em vez de paráfrases de resumos — e permite desmentir atribuições.

**Limitação declarada:** as árvores propriamente ditas estão em imagens (*exhibits*); os rótulos de ramo reportados são reconstruções a partir da prosa que descreve cada uma, e isso está assinalado caso a caso.

**Regra de refutação:** onde o livro **não** confirma um caso alegado, isso é dito explicitamente e a atribuição é marcada como folclore até prova em contrário.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

> Memo de analista A (#4 de 6). Investigação autónoma, base documental própria.
> Segunda investigação. Ver também: `2026-09-20-research-dominios-caracterizacao-e-me-sem-ce.md`, `2026-09-20-research-dominios-limites-e-contra-indicacoes.md`, os exercícios em `2026-09-20-sintese-jardim-exercicios-aplicados.md`, e a síntese `2026-09-20-sintese-dominios-aplicacao-a-outros-dominios.md`.

---

### 1. Nota metodológica prévia

Foi obtido e extraído o **texto integral de *Bulletproof Problem Solving*** (Conn & McLean, Wiley, 2019) a partir de um PDF público. Isto permite reportar o **texto real** dos casos, não paráfrases de resumos — e permite **desmentir** várias atribuições correntes (ver §5).

Limitação importante: as árvores propriamente ditas estão em **exhibits (imagens)** — os rótulos dos ramos abaixo são reconstruções a partir da prosa que descreve cada exhibit, e isso está assinalado. Onde o livro não confirma um caso alegado, diz-se explicitamente.

---

### 2. Aplicações não-empresariais documentadas

#### 2.1 Salmão do Pacífico (Gordon & Betty Moore Foundation, ~15 anos, 275 M USD)

O caso mais valioso porque o livro mostra **a árvore errada primeiro**. A "árvore de componentes" inicial (Exhibit 3.3) era, pela descrição textual:

```
Preservar o salmão selvagem do Pacífico
├── Qualidade das bacias hidrográficas de água doce
├── Condições ambientais oceânicas
├── Pesca comercial e outras pescas
├── Incubadoras (hatcheries) e aquacultura
├── Comportamento do consumidor
└── Política governamental          ← ramo que quebra o MECE
```

Conn admite o defeito: o ramo de política pública **afecta cada alavanca**, das bacias às pescas, em vez de ser um tópico separado. A árvore *"isn't MECE"* — e note-se bem: **falha de exclusividade mútua, não de exaustividade**.

Após revisão (Exhibit 8.15), a estrutura tornou-se uma *theory of change* com quatro estratégias:

```
Função do ecossistema do salmão no Pacífico Norte
├── (1) Preservar a integridade do habitat
├── (2) Neutralizar a ameaça da aquacultura em jaula aberta
├── (3) Mitigar o impacto da propagação em incubadoras
└── (4) Assegurar gestão sustentável das pescas
```

Nota crítica de transferência: a **definição do problema mudou porque a medição falhou**. A fundação exigia resultados mensuráveis, mas a Oscilação Decadal do Pacífico torna impossível separar variação interanual natural de efeito de política. A solução não foi analítica mas conceptual: substituir "contar peixes" por *populações suficientes para usar a capacidade de carga oceânica disponível*. Este é o padrão genérico — **quando os dados não permitem dimensionar ramos, redefine-se o nó-raiz**.

#### 2.2 Asma em Western Sydney (The Nature Conservancy Australia, Rob McLean)

O *cleave* foi **incidência vs. severidade**, escolhido — e isto é revelador — por familiaridade, não por teoria: McLean usara-o em relatórios de acidentes noutros conselhos de administração.

```
Carga da asma em Sydney
├── Incidência  → +10% em Western vs. Northern Sydney
└── Severidade
    ├── Taxa de hospitalização  → +65%
    └── Taxa de mortalidade     → +54%
         └── Driver hipotético: ausência de espaço verde urbano
             ├── Cobertura arbórea 15-20% vs. 30-40%
             └── PM2.5 máximo +54%
```

O insight só aparece porque incidência e severidade **divergem por uma ordem de grandeza**. Um *cleave* por grupo etário ou por medicação não teria produzido nada.

#### 2.3 Obesidade (McKinsey Global Institute, Reino Unido)

Cleave **procura/oferta**, operacionalizado como *cost curve* (analogia directa da curva de abatimento de CO₂). Não é uma árvore mas uma ordenação: 18 grupos de intervenção → 74 intervenções avaliadas → 44 seleccionadas por custo-eficácia em USD/DALY, meta de 20% em 5 anos, custo 40 mil M USD. Conn & McLean registam alternativas **rejeitadas** de *cleave*: incidência/severidade, clínico/comportamental, financeiro/não-financeiro. Citam o MGI: *"Obesity is a complex, systemic issue with no single or simple solution."*

Crítica dos próprios autores: faltam intervenções de **custo negativo** na curva, porque num SNS universal os incentivos individuais estão embotados — ou seja, **a escolha de decisor (governo do RU) determinou a forma da árvore**.

#### 2.4 Sobrepesca — *"the quintessential wicked problem"*

A estrutura real aqui é de **opções convencionais esgotadas** (Exhibit 9.2), não árvore causal:

```
Reduzir o impacto do arrasto de fundo (US West Coast Groundfish)
├── Zonas de interdição de arrasto             → sucesso limitado
├── Redução de esforço via recompra de licenças → sucesso limitado
└── Modificação de artes de pesca               → sucesso limitado
   ⇒ solução FORA da árvore: compra de direitos por ONG (TNC),
     servidão marinha de 3,8 M acres, quota comunitária (Morro Bay)
```

**É o caso mais honesto do livro sobre os limites do método:** a solução veio de **analogia** (servidões de conservação terrestres aplicadas ao mar) e de Ostrom, não de decomposição.

#### 2.5 Casos pessoais e sociais menores, com estrutura

- **Painéis solares (Rob):** árvore dedutiva de critérios — payback < 10 anos; declínio do custo dos painéis a abrandar (não vale esperar); redução da pegada de CO₂ ≥ 10%.
- **Joelho (artroscopia, Rob):** "regra de três perguntas" — grau de desconforto / natureza degenerativa vs. traumática / horizonte da tecnologia alternativa. Quatro opções: cirurgia APM; recolher mais dados e decidir go/no-go; esperar por nova tecnologia com fisioterapia; fisioterapia e reabilitação. **Decisão: esperar.**
- **Enfermagem, Bay Area (12 anos):** árvore dedutiva com dois troncos — aumentar o número de diplomados qualificados / melhorar competências e práticas das enfermeiras existentes. Resultado reportado: +4.500 enfermeiras, ~1.000 vidas/ano poupadas de sépsis.
- **Escolha de carreira:** matriz (previsão económica do sector × capacidade × interesse × tolerância ao risco) → três estratégias: *big bet*, *no regrets*, *hedge*.
- **Enfartes (triagem hospitalar):** árvore de decisão indutiva com três testes — TA sistólica mínima em 24 h > 91; idade > 62,5; presença de taquicardia sinusal.
- **Taxa escolar local (Charles):** financiamento por aluno / demografia dos alunos / qualidade dos professores e do ambiente escolar; conclusão de que o problema dos EUA está *"mostly with teachers and schools"*, pelo que votou contra a emissão obrigacionista focada em instalações.

#### 2.6 O verdadeiro contributo teórico: *cleaving frames*

Conn & McLean generalizam o MECE num **catálogo de lentes**, e é isto que viaja melhor do que a regra formal:

- **Política pública:** Regular/Incentivar · Igualdade/Liberdade · Mitigar/Adaptar · Oferta/Procura
- **Pessoal:** Trabalho/Lazer · Curto/Longo prazo · Financeiro/Não-financeiro
- **Negócio:** Preço/Volume · Principal/Agente · Activos/Opções · Colaborar/Competir

Regra prática declarada: escolher um *frame* e **validá-lo com cálculos de guardanapo antes** de construir a árvore.

---

### 3. Métodos cognatos, inventados independentemente

| Método | Origem | Regra de ramificação | Exige exaustividade? | Diferença face à issue tree |
|---|---|---|---|---|
| **Fault Tree Analysis** | H. A. Watson, Bell Labs, contrato USAF Minuteman (1961 ou 1962 — ver §5); Haasl/Boeing 1965; NUREG-0492, 1981 | Dedutiva, topo→baixo, portas booleanas AND/OR/XOR | **Sim, formalmente** — via *minimal cut sets*; a álgebra de Boole impõe-no | Única variante formalmente exaustiva e **quantificável em probabilidade**. Limitação admitida: *"is not good at finding all possible initiating faults"* |
| **FMEA/FMECA** | MIL-P-1629 (1949); NASA Apollo 1966; RPN pela AIAG 1993 | **Indutiva, baixo→topo**, por componente | Exaustiva nos modos de falha de cada componente, não nas combinações | Inverte a direcção. Não capta falhas múltiplas combinadas |
| **Ishikawa / espinha de peixe** | Ishikawa, Kawasaki (1943/1960s), *Guide to Quality Control* 1968 | Categorias fixas 6M (Man, Machine, Material, Method, Measurement, Milieu) | Não — exaustividade é *presumida* pelas categorias, nunca verificada | Categorias **pré-fabricadas**, não derivadas do problema. Objectivo declaradamente democrático: usável pelo operário de linha |
| **5 Porquês** | Taiichi Ohno, Toyota | Cadeia causal única, sem ramificação | Não | Profundidade sem largura. Criticado dentro da Toyota (Teruyuki Minoura) por ser *"too basic"* |
| **Problem/Objective Tree (LFA, ZOPP)** | USAID anos 60; GTZ ZOPP c. 1980 | Causas para baixo, efeitos para cima, a partir de um *focal problem*; depois reformulado a positivo | Não formalmente; exige **problema focal único** | Construída por workshop participativo, não por analista. Ver §4 |
| **Kepner-Tregoe** | Kepner & Tregoe, RAND, firma fundada 1958; *The Rational Manager* 1965 | Matriz **IS / IS-NOT** × (Quem, Quê, Quando, Onde, Quanto) → distinções → mudanças | Exaustividade pela *fronteira*: o que o problema **não** é | Não é árvore; é **delimitação por contraste**. Provável ancestral comum com McKinsey (ambos anos 50-60) |
| **A3 / Toyota Practical Problem Solving** | Toyota anos 60-70; Shook, *Managing to Learn* 2008 | Decomposição até ao *point of cause*, depois PDCA | Não; a restrição é **física** (uma folha A3) | O limite de espaço substitui a regra de exaustividade |
| **Diagnóstico diferencial / VINDICATE** | Mnemónica clínica | Grelha 2D: eixo anatómico × mecanismo (Vascular, Infeccioso, Neoplásico, Degenerativo, Iatrogénico, Congénito, Autoimune, Traumático, Endócrino) | **Aspiracional** — a mnemónica existe precisamente para forçar exaustividade contra o *premature closure* | O produto cruzado anatomia × mecanismo é uma árvore MECE implícita; Graber recomenda compilar um diferencial completo como antídoto cognitivo |
| **Taxonomia lineana / cladística** | Lineu 1735; Hennig | Hierarquia encaixada de patentes / monofilia por sinapomorfia | Lineana: hierarquia encaixada mas admite **grupos parafiléticos** (répteis sem aves). Cladística: proíbe-os | A cladística é MECE-estrito imposto por um **critério externo** (ancestralidade), não por conveniência analítica |
| **WBS** | PERT/Polaris 1957; MIL-STD-881, 1968; PMI Practice Standard | Decomposição orientada a entregáveis | **Sim — "regra dos 100%"**: a soma dos filhos = 100% do pai, nem mais nem menos; elementos sem sobreposição | Literalmente MECE, mas sobre **âmbito de trabalho**, não sobre causas ou hipóteses |
| **Mind map (Buzan)** | Buzan, *The Mind Map Book* | Radial, associativo, **uma palavra por ramo** | **Não — e deliberadamente não** | Buzan queria a palavra isolada como "gatilho" associativo. Exaustividade mataria a divergência. Serve a fase de brainstorming; a árvore lógica serve a fase de estruturação |

---

### 4. O que se parte na transferência

**(a) Dados inexistentes para dimensionar ramos.** É o problema do salmão. Conn & McLean não resolvem por melhor análise — mudam a métrica do nó-raiz. Generalização: em domínios ecológicos e sociais a poda por magnitude de impacto (*"prune your tree savagely"*) é inaplicável, porque **as magnitudes são precisamente o que não se sabe**.

**(b) Inexistência de decisor.** No caso da obesidade o MGI **postulou** um decisor (o governo britânico) para que a árvore fechasse. Gasper aponta que o LFA foi importado *"from engineering, military and private business contexts"* para contextos onde falta uma estrutura de autoridade simples. O nó-raiz de uma issue tree é sempre *"o que deve X fazer?"* — **sem X, a árvore não tem orientação**.

**(c) Raiz politicamente contestada.** É o achado mais forte de Gasper: *"nearly every problem-'tree' is really a web, due to crosscutting and feedback effects"*. A insistência num **problema focal único** é uma escolha administrativa, não lógica. E as análises de problema ZOPP eram, na literatura revista, *"simplistic, ahistorical, and negativist"* — começar por "qual é o seu problema?" em vez de potenciais e aspirações é **desempoderador**.

**(d) Horizontes longos.** Quinze anos no salmão, doze na enfermagem. A resposta de Conn & McLean é substituir a árvore por **portfólio**: matriz Semear / Cultivar / Colher × ambição incremental vs. transformacional. Ou seja, a árvore deixa de ser o artefacto de gestão e passa a ser insumo de um mapa de carteira.

**(e) ONG/voluntariado sem capacidade analítica.** Gasper: o uso de ZOPP *"did not outlive donor funding"*, e frequentemente exigia importar um moderador especializado. E, de forma contundente: *"To date, LFA has predominantly been a tool of the powerful."* A GTZ despromoveu oficialmente o ZOPP em 1996-7, recolocando-o como um conjunto de ferramentas entre muitos. Note-se o contraste deliberado de Ishikawa, que desenhou a espinha de peixe **para ser usável sem analista**.

**(f) Patologias de uso.** *Lock-frame* (matriz congelada, impede aprendizagem), *lack-frame* (simples demais, omite o essencial), *box-filling* (preencher células com material plausível ignorando a lógica). Citação recolhida por Gasper: *"People tend to dwell on how to fill in the boxes"* (Solem, 1987). Equivalente clínico: *premature closure* — *"When the diagnosis is made, the thinking stops."*

---

### 5. Contradições e folclore — sinalizados

1. **1961 vs. 1962 para a FTA.** Múltiplas fontes secundárias dizem 1961 (Watson, Bell Labs, Minuteman); a Wikipédia diz 1962. Não resolvido; tratar como "início dos anos 60".
2. **"Direitos indígenas / native title" como caso de árvore lógica: NÃO CONFIRMADO.** Pesquisado o texto integral de *Bulletproof Problem Solving*: não existe caso de *native title*. Existem (i) direitos de propriedade das Primeiras Nações como componente da estratégia de habitat do salmão, (ii) pescas aborígenes históricas no Skeena. Em *The Imperfectionists* (2023) há um caso de **gestão indígena do fogo** no Norte da Austrália com a TNC Austrália — plausivelmente a origem da confusão. **Tratar a atribuição como folclore até prova em contrário.**
3. **"Comprar vs. arrendar": NÃO EXISTE no livro.** O que existe é "Where Should I Move?" (análise multicritério ponderada, ~20 variáveis, quatro categorias: sistema escolar, ambiente natural e recreio, características da vida urbana, capacidade de gerar rendimento — com "segurança/criminalidade" **podada por não diferenciar**) e "Will My Retirement Savings Last?".
4. **"Salmão correu 15 anos": ligeira inconsistência interna.** O livro diz *"a dozen years"* no capítulo 8 e *"15-year, $275m effort"* no capítulo 3. Ambas as formulações são dos autores.
5. **Origem do MECE.** Atribui-se rotineiramente a Barbara Minto/McKinsey; nenhuma fonte lida documenta a invenção. As convergências independentes (WBS 1957-68, FTA 1961, K-T 1958) sugerem que o MECE foi **nomeado** pela McKinsey, não inventado.
6. **Ishikawa "inventou em 1943 / popularizou em 1968".** Fontes secundárias divergem entre Kawasaki Steel 1943 e estaleiros Kawasaki anos 60. Baixa fiabilidade.

---

### 6. Ensino e difusão

- **Diagnóstico dos próprios autores:** *"It remains early days in codifying and disseminating problem solving best practices"* em instituições de ensino. E, sobre universidades: *"we have not seen a common framework or process emerge yet."*
- **OCDE/PISA:** testes de resolução individual de problemas desde 2012, colaborativa desde 2015. Schleicher, citado no livro: *"the world no longer rewards people just for what they know"*. Achado relevante: ensinar bem leitura, matemática e ciências **não basta** — criatividade, lógica e raciocínio são contributos autónomos.
- **Ensino superior:** CLA+ (Council for Aid to Education) usado em ~200 *colleges*; o WSJ (2017) reportou progresso mensurável na maioria das instituições testadas, com excepções em instituições prestigiadas.
- **Difusão académica formal:** Arnaud Chevallier (curso criado em Rice, hoje IMD, co-director do programa Complex Problem Solving) codificou as **quatro regras da issue tree** — consistência (sempre "porquê" ou sempre "como"), progressão, MECE, insight — e a distinção entre árvores **diagnósticas** ("porquê") e **de solução** ("como"). É a formulação mais próxima de um padrão académico existente.
- **Sector público / educação K-12:** Benjamin Tregoe fundou o **Tregoe Education Forum** (1993, hoje TregoED) e publicou *Analytic Processes for School Leaders* (2001) — transferência explícita do K-T para direcção escolar. **É o caso mais claro de adopção pública documentada.**
- **Canais próprios de Conn & McLean:** curso online auto-guiado de 4-6 horas, educação corporativa, apêndice de folhas de trabalho em branco e secções "Problems to Try on Your Own" em cada capítulo — o livro é construído como manual didáctico. **Não foi encontrada evidência de um "programa para escolas" formal** dos autores; tratar essa alegação como não verificada.

---

---

## 4 · Fontes

- `farasaze.co/.../Bulletproof Problem Solving (2019).pdf` — **texto integral do livro**, extraído com pdftotext. **Fiabilidade máxima** para citações e estrutura; imagens dos exhibits não recuperáveis.
- `repub.eur.nl/pub/50949/Metis_165267.pdf` — Des Gasper, "Logical Frameworks: Problems and Potentials". **Alta**: académico, revisão de literatura extensa, é a fonte central da secção 4.
- `en.wikipedia.org/wiki/Fault_tree_analysis` — **Média-alta**; boa sobre método e portas lógicas, data divergente (1962).
- `en.wikipedia.org/wiki/Work_breakdown_structure` — **Média-alta**; formula a regra dos 100% e a história PERT/MIL-STD-881.
- `en.wikipedia.org/wiki/Issue_tree` — **Média**; útil por codificar as quatro regras de Chevallier.
- `en.wikipedia.org/wiki/Benjamin_Tregoe` — **Média**; confirma RAND, 1958, *The Rational Manager*, TregoED.
- `coffeetalk101.github.io/bulletproof-problem-solving/` — resumo detalhado do livro. **Média**; usado para triangular casos, confirmado depois no texto original.
- `pdfcoffee.com/bulletproof-problem-solving-...` — excerto do livro. **Média-baixa** isolada; serviu de ponte para o PDF integral.
- `bulletproofproblemsolving.com` — site oficial. **Média**: fiável sobre oferta formativa, promocional no resto; não menciona programa escolar.
- `mckinsey.com/.../six-problem-solving-mindsets-for-very-uncertain-times` — **não acedido** (ECONNRESET); só conhecido por resultados de pesquisa. Tratar como não lido.
- `odi.org/en/publications/planning-tools-problem-tree-analysis/` — **não acedido** (HTTP 403). Conteúdo sobre problem tree obtido de resumos de pesquisa; fiabilidade reduzida.
- Resultados de pesquisa agregados para: FMEA/MIL-P-1629, Ishikawa 6M, 5 Whys e crítica de Minoura, A3/Shook, VINDICATE, Graber e *premature closure*, cladística vs. Lineu, Buzan, Chevallier/IMD, *The Imperfectionists*, PISA. **Fiabilidade média**: snippets sintetizados, não páginas completas. Os pontos sinalizados como folclore em §5 derivam precisamente desta camada.
