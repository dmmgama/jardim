---
title: "Arvores MECE fora da consultoria: transferencia, caracterizacao, ME sem CE, e limites"
date: 2026-09-20
type: sintese
case: dominios
tags: [MECE, arvore, sintese]
sobre:
  - "[[2026-09-20-research-dominios-transferencia-do-metodo]]"
  - "[[2026-09-20-research-dominios-caracterizacao-e-me-sem-ce]]"
  - "[[2026-09-20-research-dominios-limites-e-contra-indicacoes]]"
  - "[[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]]"
---

# Arvores MECE fora da consultoria: transferencia, caracterizacao, ME sem CE, e limites

## 0 · Sumário executivo

- **O MECE foi nomeado, não inventado.** Convergem independentemente Lineu (1735), Ranganathan (1937), WBS/PERT (1957-68), Kepner-Tregoe (1958), Fault Tree Analysis (1961), Ishikawa. A reinvenção repetida valoriza o método.
- **Só duas tradições são formalmente exaustivas** — FTA (álgebra de Boole) e WBS (regra dos 100%). Nas restantes, incluindo a McKinsey, a exaustividade é presumida, nunca verificada.
- **Existem três modos de árvore, não um:** diagnóstico, decisão, caracterização. Requisitos de ME e CE diferentes, critérios de paragem diferentes, modos de falha diferentes.
- **ME sem CE é uma família formal legítima** — cobertura parcial disjunta, não partição defeituosa.
- **Regra de ouro:** é lícito não ser exaustivo desde que não se faça nenhuma operação que pressuponha exaustividade.
- **Nas facetas, a exaustividade aplica-se para dentro, não para fora.**
- **Numa caracterização há dois registos de faceta** — as que vêm de domínios de conhecimento e as que vêm da pessoa. E a valência não é propriedade do facto: é relação entre facto e pessoa.
- **Podar corrompe o julgamento — está medido.** Fischhoff: subestimação do residual por um factor de seis; 1 em 55 acertou, incluindo peritos.
- **E decompor reduz o erro em ~42%.** A contradição resolve-se: ajuda quando a partição é conhecida; prejudica quando a partição é a incógnita.
- **O caso canónico do método falha o próprio método** — a árvore do salmão falhou por exclusividade mútua.

---

## 1 · Mandato

Investigar a aplicação da metodologia a outros domínios, em três frentes, e sintetizar:

1. **Desmontar um problema com o método**, seja ele qual for.
2. **Usos distintos:** em vez de partir um problema, caracterizar uma situação — com ramos a surgir organicamente, sem solução única, e com gostos que variam durante o processo. Avaliar se faz sentido ser mutuamente exclusivo mas não necessariamente colectivamente exaustivo.
3. **Casos em que se aplica e casos em que não é mesmo boa ideia.**

Os exercícios aplicados foram produzidos em documento à parte, por decisão do mandante.

---

## 2 · Método

Três investigações independentes em paralelo, com bases documentais próprias e sem contacto entre si, seguidas de síntese integradora.

**Ganho documental face à investigação anterior:** dois documentos que faltavam foram obtidos e lidos na íntegra — o texto integral de *Bulletproof Problem Solving*, que permite desmentir atribuições que só circulam por resumos, e o relatório original de Fischhoff, Slovic & Lichtenstein (1978), que é a evidência experimental mais forte de toda a investigação e é desfavorável ao método.

**Critério de arbitragem:** onde a evidência empírica contradiz a doutrina prescritiva, a contradição é enunciada e reconciliada por condição de aplicabilidade, nunca resolvida por autoridade.

**Mitos:** cada afirmação corrente que não se confirmou fica na tabela da Parte V com o seu estatuto.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

**Transferência para outros domínios · árvores que caracterizam em vez de resolver · ME sem CE · onde aplicar e onde não**
Data: 20 de Setembro de 2026

---

### Como ler este relatório

Segunda investigação. A primeira — [`2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey.md`](2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey.md) — estabeleceu como a McKinsey usa árvores MECE. Esta pergunta o que acontece quando se tira o método do sítio onde nasceu.

Sintetiza três investigações independentes, conduzidas em paralelo, cujos memos ficam intactos no repositório:

| Ficheiro | Cobertura |
|---|---|
| [`2026-09-20-research-dominios-transferencia-do-metodo.md`](2026-09-20-research-dominios-transferencia-do-metodo.md) | Casos não-empresariais documentados; métodos cognatos (FTA, Ishikawa, logframe, WBS, diagnóstico diferencial…); o que se parte na transferência |
| [`2026-09-20-research-dominios-caracterizacao-e-me-sem-ce.md`](2026-09-20-research-dominios-caracterizacao-e-me-sem-ce.md) | Estatuto formal de ME e CE; análise por facetas; tipologias; morfologia geral; hierarquias de objectivos; elicitação de preferências |
| [`2026-09-20-research-dominios-limites-e-contra-indicacoes.md`](2026-09-20-research-dominios-limites-e-contra-indicacoes.md) | Problemas perversos; Ackoff e sistemas; Cynefin; limites formais; a evidência experimental contra a poda; domínios proibidos |

Os **exercícios aplicados** estão em documento à parte, como pedido: [`2026-09-20-sintese-jardim-exercicios-aplicados.md`](2026-09-20-sintese-jardim-exercicios-aplicados.md).

#### Ganho documental face à primeira investigação

Dois documentos que faltavam foram obtidos e lidos na íntegra:

- **O texto integral de *Bulletproof Problem Solving*** (Conn & McLean, 2019) — o que permite citar os casos reais e **desmentir** atribuições que só circulam por resumos.
- **Fischhoff, Slovic & Lichtenstein (1978), *Fault Trees: Sensitivity of Estimated Failure Probabilities to Problem Representation*** — relatório original com dados. É a evidência experimental mais forte de toda a investigação, e é desfavorável ao método.

---

### Sumário executivo

1. **O MECE foi nomeado, não inventado.** Convergem independentemente: Ranganathan (1937), Lineu (1735), WBS/PERT (1957-68), Kepner-Tregoe (1958), Fault Tree Analysis (1961), Ishikawa (anos 40-60). A McKinsey deu-lhe sigla e doutrina. Isto não desvaloriza o método — **valoriza-o**: a reinvenção repetida é indício de utilidade real, não de marketing.
2. **Quase nenhuma destas tradições exige exaustividade a sério.** Só duas são formalmente exaustivas — Fault Tree Analysis (a álgebra de Boole obriga) e a WBS (a "regra dos 100%"). Nas restantes, incluindo a McKinsey, a exaustividade é **presumida, nunca verificada**. A CE da consultoria está mais próxima do Ishikawa (categorias pré-fabricadas que se *assume* cobrirem tudo) do que da FTA.
3. **Existem três modos de árvore, não um.** Diagnóstico ("porquê"), decisão ("qual"), caracterização ("que espécie de coisa é esta"). Têm requisitos diferentes de ME e CE, critérios de paragem diferentes, e modos de falha diferentes. Confundi-los é a origem da maior parte dos maus usos.
4. **ME sem CE é uma família formal legítima** — uma *cobertura parcial disjunta*, não uma partição defeituosa. Tem tradições próprias e maduras: análise por facetas, tipologia conceptual, análise morfológica geral, redes de meios-fins.
5. **A regra que governa tudo:** *é lícito não ser exaustivo desde que não se faça nenhuma operação que pressuponha exaustividade*. Caracterizar, comparar, gerar, dar a ver — lícito. Ponderar, somar a 100%, afirmar "não há mais nada" — ilícito.
6. **Nas facetas, a exaustividade aplica-se para dentro, não para fora.** Dentro de cada eixo, as posições devem cobrir o espectro relevante e não se sobrepor. O *conjunto* de eixos é deliberadamente aberto. Quem exige "ME+CE às facetas" está a aplicar o critério ao nível errado.
7. **Numa caracterização há dois registos de faceta, não um** — as que vêm de domínios de conhecimento (onde se pode estar errado) e as que vêm da pessoa (onde não se pode). E a consequência que reorganiza tudo: **a valência não é propriedade do facto, é uma relação entre um facto e uma pessoa**. O que torna formal a ausência de solução única — o cruzamento dos dois registos produz um *espaço* de configurações consistentes, não uma resposta.
8. **Podar uma árvore corrompe o julgamento — está medido.** No estudo de Fischhoff, remover ramos inteiros de uma árvore de falhas sem avisar fez com que os sujeitos subestimassem a categoria "outros" por um factor de **seis**. Apenas **1 em 55** acertou. O efeito manteve-se em mecânicos experientes. **O que sai da árvore sai da cabeça.**
9. **E, simultaneamente, decompor reduz o erro em ~42% sob alta incerteza** (MacGregor). A contradição é real e resolve-se assim: a decomposição **ajuda quando a partição é conhecida e se conhece melhor as partes do que o todo; prejudica quando a partição é ela própria a incógnita.** É o melhor teste único que a literatura oferece.
10. **O caso canónico do método falha o próprio método.** No salmão do Pacífico, Conn admite que a árvore inicial *"isn't MECE"* — e a falha é de **exclusividade mútua**, não de exaustividade. Um driver que atravessa todos os ramos não tem notação possível numa árvore.
11. **Há domínios onde a árvore faz mal, com evidência e não com intuição:** luto e trauma (a análise de causa-raiz do próprio estado afectivo é formalmente ruminação, que degrada a resolução de problemas), e preferências estéticas (analisar razões piora a escolha e reduz a satisfação — Wilson & Schooler).

---

# PARTE I — O que viaja e o que não viaja

### 1.1 A família a que o método pertence

O achado mais desarmante da investigação sobre transferência é que **não houve transferência nenhuma**: a mesma ideia foi inventada repetidamente, em domínios sem contacto entre si, antes e depois da McKinsey.

| Método | Data | O que ramifica | Exaustividade | Quem o pode usar |
|---|---|---|---|---|
| Classificação lineana | 1735 | hierarquia encaixada de patentes | admite grupos parafiléticos | taxonomistas |
| Facetas (Ranganathan) | 1937 | dimensões independentes | **dentro** da faceta | bibliotecários |
| WBS / PERT | 1957-68 | âmbito de trabalho | **sim — regra dos 100%** | gestores de projecto |
| Kepner-Tregoe | 1958 | não ramifica: IS / IS-NOT | pela fronteira | gestores |
| Fault Tree Analysis | ~1961 | portas booleanas AND/OR | **sim — minimal cut sets** | engenheiros |
| MECE / issue tree | anos 60 | questões ou hipóteses | presumida | consultores |
| Ishikawa | 1943/60s | categorias fixas 6M | presumida pelas categorias | **o operário de linha** |
| 5 Porquês | anos 50-70 | cadeia única, sem largura | não | qualquer pessoa |
| Problem tree (LFA/ZOPP) | anos 60-80 | causas ↓ efeitos ↑ | não | workshop participativo |
| Mind map (Buzan) | anos 70 | associação radial | **deliberadamente não** | qualquer pessoa |
| Morfologia geral (Zwicky) | anos 40-60 | parâmetros × condições | não — consistência cruzada | analistas |

Três leituras desta tabela:

**(a) A exaustividade real é rara e sempre imposta de fora.** A FTA é exaustiva porque a álgebra de Boole a obriga; a WBS porque a regra dos 100% a define; a cladística porque um critério externo (ancestralidade comum) decide. Onde não há formalismo externo, a CE é aspiração. A honestidade obriga a dizer que **a CE da issue tree é do tipo "Ishikawa" — presumida — e não do tipo "FTA" — demonstrada**.

**(b) A direcção varia.** FTA é dedutiva (topo → baixo); FMEA é indutiva (componente → sistema); o problem tree do logframe cresce nos dois sentidos (causas para baixo, efeitos para cima). A issue tree é dedutiva e esquece que a alternativa existe.

**(c) Quem pode usar cada uma é uma escolha de desenho, não um acidente.** Ishikawa desenhou a espinha de peixe com categorias pré-fabricadas **precisamente para dispensar o analista**. A issue tree exige alguém capaz de inventar o corte. Isto reaparece como problema real na secção 1.3.

### 1.2 Os casos não-empresariais que existem mesmo

Do texto integral do livro, não de resumos:

- **Salmão do Pacífico** (Moore Foundation, ~275 M USD). Valioso porque o livro **mostra a árvore errada primeiro**.
- **Asma em Western Sydney.** O corte incidência vs. severidade — escolhido, reveladoramente, **por familiaridade**: McLean já o usara em relatórios de acidentes noutros conselhos de administração. O insight só aparece porque os dois divergem por uma ordem de grandeza: incidência +10%, mortalidade +54%, hospitalização +65%.
- **Obesidade no Reino Unido** (MGI). Corte procura/oferta operacionalizado como curva de custo, por analogia directa com a curva de abatimento de CO₂. 18 grupos → 74 intervenções → 44 seleccionadas por USD/DALY.
- **Sobrepesca.** Ver 1.4 — é o caso mais instrutivo e o menos favorável ao método.
- **Pessoais:** painéis solares; artroscopia ao joelho (decisão: esperar); onde morar (~20 variáveis, quatro categorias — com "criminalidade" **podada por não discriminar entre as opções**); poupança para a reforma; escolha de carreira; um voto sobre uma emissão obrigacionista escolar.
- **Enfermagem na Bay Area**, 12 anos, +4.500 enfermeiras.

> **Correcções ao folclore.** Não existe no livro nenhum caso de "comprar vs. arrendar" nem de direitos indígenas / *native title* — ambos circulam atribuídos e nenhum está no texto. E o próprio livro é inconsistente sobre o salmão: *"a dozen years"* no capítulo 8, *"15-year effort"* no capítulo 3.

### 1.3 O que se parte na transferência — cinco condições

**(a) Não há dados para dimensionar ramos.** É o problema do salmão: a abundância oscila com a Oscilação Decadal do Pacífico, e é impossível separar variação natural de efeito de política. A resposta dos autores **não foi analítica — foi conceptual**: substituíram "contar peixes" por *populações suficientes para usar a capacidade de carga oceânica disponível*. Padrão genérico: **quando os dados não permitem dimensionar os ramos, muda-se o nó-raiz.** E isto arrasta uma consequência incómoda: a poda por magnitude de impacto, que é o coração do método, torna-se inaplicável em domínios ecológicos e sociais — porque as magnitudes são exactamente o que não se sabe.

**(b) Não há decisor.** No caso da obesidade, o MGI teve de **postular** um decisor (o governo britânico) para a árvore fechar — e essa escolha determinou a forma da árvore, ao ponto de faltarem as intervenções de custo negativo, porque num SNS universal os incentivos individuais estão embotados. O nó-raiz de uma issue tree é sempre *"o que deve X fazer?"*. **Sem X, a árvore não tem orientação.**

**(c) A raiz é politicamente contestada.** Achado mais forte de Gasper sobre o logframe: *"nearly every problem-'tree' is really a web, due to crosscutting and feedback effects"*. A exigência de um **problema focal único** é uma escolha administrativa, não lógica. E as análises ZOPP eram, na literatura revista, *"simplistic, ahistorical, and negativist"* — começar por "qual é o seu problema?" em vez de por potenciais e aspirações é **desempoderador**.

**(d) O horizonte é longo demais.** Quinze anos no salmão, doze na enfermagem. A resposta dos autores é abandonar a árvore como artefacto de gestão e passar a **portfólio** (Semear / Cultivar / Colher × incremental vs. transformacional).

**(e) Não há capacidade analítica.** Gasper: o uso do ZOPP *"did not outlive donor funding"*, e exigia frequentemente importar um moderador. E a frase que devia acompanhar qualquer transferência deste método para contextos sem poder: *"To date, LFA has predominantly been a tool of the powerful."* A GTZ despromoveu oficialmente o ZOPP em 1996-7.

As patologias nomeadas na literatura do logframe descrevem exactamente o que se vê no mau uso da issue tree: ***lock-frame*** (estrutura congelada que impede aprendizagem), ***lack-frame*** (simples demais, omite o essencial), ***box-filling*** (preencher células com material plausível ignorando a lógica). O equivalente clínico chama-se ***premature closure***: *"When the diagnosis is made, the thinking stops."*

### 1.4 O caso que o método não resolveu

Na sobrepesca — que o livro chama *"the quintessential wicked problem"* — as três opções da árvore falharam todas:

```
Reduzir o impacto do arrasto de fundo
├── Zonas de interdição              → sucesso limitado
├── Recompra de licenças             → sucesso limitado
└── Modificação de artes de pesca    → sucesso limitado
   ⇒ a solução veio DE FORA da árvore:
     compra de direitos de pesca por uma ONG, servidão marinha,
     quota comunitária — por ANALOGIA com servidões de conservação terrestres
```

É o caso mais honesto do livro e o mais importante para quem quer transferir o método: **a árvore delimita o espaço de busca e, ao fazê-lo, também o fecha.** A solução veio de analogia e de Ostrom, não de decomposição.

### 1.5 O que viaja melhor do que o MECE

Não é a regra formal — é o **catálogo de cortes** (*cleaving frames*):

- **Política pública:** Regular/Incentivar · Igualdade/Liberdade · Mitigar/Adaptar · Oferta/Procura
- **Pessoal:** Trabalho/Lazer · Curto/Longo prazo · Financeiro/Não-financeiro
- **Negócio:** Preço/Volume · Principal/Agente · Activos/Opções · Colaborar/Competir

Com uma regra prática associada que vale mais do que qualquer teoria: **escolher um corte e validá-lo com cálculos de guardanapo *antes* de construir a árvore.**

---

# PARTE II — Os três modos de árvore

Esta é a tipologia que organiza o resto do relatório, e a sua ausência explica a maior parte dos maus usos que se vêem.

| | **DIAGNÓSTICO** | **DECISÃO** | **CARACTERIZAÇÃO** |
|---|---|---|---|
| **Pergunta-raiz** | porque é que isto acontece? | qual destas opções? | que espécie de coisa é esta? |
| **Os ramos são** | partes de um todo | alternativas | dimensões |
| **Relação entre ramos** | somam-se | excluem-se | cruzam-se |
| **ME** | obrigatória | obrigatória | **dentro de cada eixo** |
| **CE** | **obrigatória** — a causa pode estar no que falta | obrigatória no conjunto considerado | **não se aplica entre eixos** |
| **Paragem** | folha testável com uma análise discreta | opção escolhida | **saturação** |
| **Output** | uma causa | uma decisão | um espaço descrito |
| **Falha** | a causa estava fora da árvore | faltava uma opção | a estrutura não discrimina |
| **A árvore mudar é** | aprendizagem | reenquadramento | **o resultado** |
| **Tradição** | FTA, Ishikawa, issue tree | decision tree, MAUT | facetas, morfologia, tipologia |

A distinção decisiva está na terceira linha. **Partes somam-se; dimensões cruzam-se.** Um jardim não se reparte entre "uso" e "manutenção" — tem simultaneamente uma posição em cada. É por isso que a exigência de exaustividade, que é uma condição de validade no primeiro caso, deixa de fazer sentido no terceiro.

Chevallier, que é a codificação académica mais próxima de um padrão, chega perto disto ao separar árvores de "porquê" de árvores de "como", com a interdição explícita de as misturar. O que falta na sua formulação é o terceiro modo — que não é nem "porquê" nem "como", mas **"que espécie de coisa"**.

---

# PARTE III — ME sem CE: a resposta

### 3.1 O estatuto formal

Em teoria de conjuntos, a distinção é limpa e resolve a questão:

- **Partição** — blocos disjuntos cuja união devolve o conjunto original. É o MECE.
- **Cobertura** — a união devolve o conjunto, mas admite sobreposição. É CE sem ME.
- **Família disjunta** — blocos sem sobreposição, admitindo lacunas. **É ME sem CE.**

ME e CE são **condições logicamente independentes**. MECE é a conjunção das duas, não uma propriedade unitária. Uma árvore ME-sem-CE não é uma árvore MECE defeituosa: é outra coisa, com nome próprio.

A mesma distinção reaparece em representação de conhecimento como **mundo fechado vs. mundo aberto**. Sob mundo fechado, o que não está representado é falso; sob mundo aberto, é desconhecido. **Uma árvore ME-sem-CE é uma árvore em mundo aberto.** É incoerente exigir-lhe uma garantia que ela nunca deu — e é igualmente incoerente usá-la depois como se fosse fechada, concluindo "isto não interessa à pessoa porque não está na árvore".

### 3.2 Quando a exaustividade é mesmo obrigatória

A lista é curta e reconhecível:

```
CE OBRIGATÓRIA                          CE DISPENSÁVEL (ou nociva)
├── partições de probabilidade          ├── caracterização exploratória
├── contabilidade e auditoria           ├── espaços de design
├── orçamento e alocação                ├── estruturação de problemas perversos
├── estatística oficial (ICD)           ├── elicitação de gosto e valores
├── inquéritos fechados                 └── teoria emergente
└── pesos normalizados em MAUT/AHP
```

O último item da coluna esquerda é o mais subtil e o mais importante: **no momento em que se atribuem pesos que somam 1, está-se tacitamente a declarar que a árvore é exaustiva.** Uma árvore que apenas caracteriza não faz essa afirmação e não tem de a honrar.

### 3.3 A regra de ouro

> **É lícito não ser exaustivo desde que não se faça nenhuma operação que pressuponha exaustividade.**
>
> **Lícito:** caracterizar · comparar · gerar opções · discriminar · dar a ver · organizar conversa.
> **Ilícito:** ponderar · somar a 100% · calcular probabilidades · afirmar "não existe mais nada" · concluir por ausência.

Toda a disciplina do modo de caracterização decorre desta linha.

E daqui sai também o veredicto sobre o remendo habitual. A categoria **"Outros"** não converte uma cobertura parcial numa partição — **esconde a incompletude atrás de uma etiqueta**. Há prova disto: em inquéritos, os inquiridos tendem a escolher as opções apresentadas em vez de escreverem a sua, ou seja, o residual absorve mal aquilo que devia capturar. Star e Bowker acrescentam que as categorias residuais são as que *"cannot be formally represented"*, e que a sua gestão é um problema ético, não técnico. Mais vale **declarar o âmbito** do que fabricar cobertura.

### 3.4 Onde a exaustividade continua a valer — para dentro

Esta é a correcção mais importante à formulação intuitiva, e vale a pena ser exacto.

As regras da análise por facetas (Ranganathan, via Spiteri e Denton) exigem que cada faceta represente **uma só característica de divisão** e seja homogénea. Ou seja:

> **Dentro de cada eixo**, as posições devem cobrir o espectro relevante e não se sobrepor — aí vale **ME e CE**.
> **Entre eixos**, não há exaustividade nenhuma a exigir — o conjunto é aberto por desenho.

A palavra técnica para essa abertura é **hospitalidade**: a capacidade de acomodar algo novo sem refazer a estrutura. É precisamente a propriedade que uma árvore MECE não tem, e é a razão pela qual uma estrutura facetada aguenta que alguém diga, a meio da conversa, "afinal o que me interessa é o cheiro ao fim da tarde".

> **Contradição registada:** fontes enciclopédicas afirmam que as facetas devem ser "mutually exclusive and collectively exhaustive". Aplicam o critério ao nível errado. A literatura especializada é clara: a exclusividade é **da característica de divisão**, e a hospitalidade é uma virtude do sistema, não um defeito.

### 3.5 A disciplina que substitui a exaustividade

Dez regras, destiladas das cinco tradições:

```
 1. Declarar o âmbito       → completude relativa a um universo explicitado
 2. ME localmente           → exclusiva dentro de cada eixo
 3. CE localmente           → as posições de um eixo cobrem o seu espectro
 4. Hospitalidade           → acrescentar eixos sem refazer a estrutura
 5. Um critério de divisão por nível
 6. Separar fins de meios   → teste WITI: "porque é que isto é importante?"
                              se remete para outro objectivo, é meio → REDE, não árvore
 7. Não-redundância         → nenhum eixo derivável dos outros
 8. Consistência cruzada    → eliminar combinações incompatíveis, par a par
 9. Saturação               → parar quando novas perguntas não geram eixos novos
10. Não normalizar pesos    → somar a 1 é afirmar exaustividade que não se tem
```

Quatro notas:

**Sobre o ponto 6.** É a distinção de Keeney entre uma *hierarquia de objectivos fundamentais* (árvore de fins, onde a completude é exigida) e uma *rede de meios-fins* (onde um meio alimenta vários fins, e portanto **não é árvore**). No jardim, "ter sombra" pode ser fim (quer-se a sensação) ou meio (para poder almoçar lá fora em Agosto). Se for meio, está no sítio errado numa árvore.

**Sobre o ponto 8.** Vem da Análise Morfológica Geral de Zwicky e Ritchey, concebida para problemas onde *"quantitative methods, causal modeling and simulation are relatively useless"*. Em vez de exaustividade, a AMG avalia par a par que combinações de posições são compatíveis, e o que resta é o espaço coerente. Ritchey chama-lhe *"in-built garbage detection"* — parâmetros mal definidos tornam-se visíveis quando se tenta avaliar consistência. **Para o jardim, isto é directamente utilizável:** "sombra profunda × horta produtiva" e "manutenção nula × sebes topiadas" eliminam-se por inconsistência, sem nunca enumerar o universo dos jardins.

**Sobre o ponto 9.** É a convergência mais valiosa de toda a investigação: **três literaturas independentes chegam ao mesmo critério de paragem quando abandonam a exaustividade.** A grounded theory chama-lhe saturação teórica (parar quando novos dados não desenvolvem a teoria). As National Academies, sobre elicitação de objectivos, admitem que *"there are no exact rules"* e propõem parar quando, ao comparar alternativas, nenhum interessado levanta novos objectivos. Conklin, sobre problemas perversos, substitui exaustividade por **coerência** — entendimento partilhado. É o mesmo critério três vezes: **pára-se quando a estrutura pára de crescer, não quando o mundo acaba.**

**Sobre o ponto 10.** Tem apoio empírico independente e forte — ver 4.3.

### 3.6 Nem todas as facetas são da mesma espécie — e a valência é uma relação

A literatura trata "faceta" como categoria única. Na prática de caracterização, há pelo menos **dois registos de faceta com estatuto epistemológico diferente**, e confundi-los produz erros em ambos os sentidos.

| | **Facetas do real** | **Facetas da preferência** |
|---|---|---|
| Origem | **domínios de conhecimento** (disciplinas) | a pessoa, por contraste entre exemplos |
| Pode-se estar errado? | **sim** | **não** |
| Dependem de quem pergunta? | não | inteiramente |
| Estáveis? | sim, na escala do trabalho | não — mudam durante a elicitação |
| Verificação | medição, ensaio, observação | saturação e discriminação |
| ME e CE **dentro** da faceta | alcançáveis | alcançáveis (eixos bipolares) |
| CE **entre** facetas | não — e a falta é **ignorância**, corrigível investigando | não — e a falta é **abertura**, não defeito |

A última linha é a que importa. Nos dois registos o conjunto de facetas é aberto, **mas por razões opostas**: falta uma faceta ao real porque ainda não se investigou; falta uma faceta à preferência porque a pessoa ainda não descobriu que queria aquilo. A primeira lacuna fecha-se com uma sondagem, a segunda só com conversa.

**E daqui decorre a consequência que reorganiza tudo:**

> **A valência não é propriedade do facto. É uma relação entre um facto e uma pessoa.**

Um facto do real — "esta zona tem sombra densa", "esta cota encharca no Inverno", "este acesso só dá para carrinho de mão" — **não é bom nem mau em si**. Torna-se um ou outro apenas ao cruzar com o registo da preferência. O conhecimento técnico tem autoridade sobre **o que é possível**; não tem nenhuma sobre **o que é desejável**. Confundir as duas é o erro mais destrutivo do lado técnico, e o simétrico do erro de analisar o gosto até o estragar.

Cruzando os dois registos, cada facto cai numa de quatro caixas:

|  | **a pessoa quer** | **a pessoa não quer / indiferente** |
|---|---|---|
| **o real favorece** | recurso — usar | recurso por aproveitar — mostrar antes de descartar |
| **o real dificulta** | **a caixa que interessa** | problema — e é o **único** quadrante que pertence ao modo diagnóstico |

A caixa inferior esquerda — o que a disciplina manda corrigir e a pessoa quer manter — é onde as decisões de desenho realmente se tomam, e é invisível para qualquer estrutura que trate o real como "constrangimento".

**Isto explica formalmente porque não há solução única.** A operação de cruzamento é a **avaliação de consistência cruzada** da Análise Morfológica Geral: cruzar posições par a par, eliminar as combinações internamente inconsistentes, e ficar com o resto. O produto de uma AMG **não é uma solução — é um espaço de configurações consistentes**. A pluralidade não é falha da análise: é o output declarado do método. A estrutura reduz o infinito ao coerente e devolve a escolha a quem ela pertence.

Nota operacional: o cruzamento **não cabe dentro de nenhuma das duas árvores**, porque é uma operação *entre* elas — o que é mais um indício de que a forma de árvore está a ser esticada, e liga directamente à objecção seguinte.

### 3.7 A objecção mais séria ao exemplo do jardim

Tem de ficar registada, porque vem da autoridade mais óbvia e é contra nós.

**Christopher Alexander** escreveu em *Notes on the Synthesis of Form* (1964) o tratado canónico sobre decomposição hierárquica de problemas de design — um algoritmo que parte o conjunto de variáveis nos dois subconjuntos com transferência mínima de informação. E **repudiou-o no ano seguinte**, em *A City is Not a Tree* (1965), repetindo a repudiação no prefácio de 1971. O argumento: em domínios de design os subsistemas **sobrepõem-se**, e a estrutura correcta é o **semi-reticulado**, em que cada nó tem relações com muitos nós. *A Pattern Language* é a consequência — uma rede de padrões com ligações a montante e a jusante, e que contém, literalmente, padrões de jardim (*Garden Growing Wild*, *Half-Hidden Garden*, *Terraced Slope*, *Fruit Trees*, *Garden Seat*).

**A resposta honesta não é refutar — é aceitar e limitar.** Quem usa a forma de árvore para um jardim está a projectar um semi-reticulado numa árvore, e essa projecção **perde as sobreposições**. As facetas recuperam parte do que se perde, porque permitem que o mesmo objecto viva em vários eixos ao mesmo tempo — que é exactamente a propriedade que Alexander exigia e que a árvore nega. Mas só parte. Se as ligações entre elementos do jardim forem mais importantes do que os elementos, nenhuma estrutura facetada salva a situação e a ferramenta certa é o padrão em rede, não a árvore.

### 3.8 A instabilidade dos gostos: não é ruído, é o fenómeno

A literatura sobre **preferências construídas** (Slovic; Payne, Bettman & Johnson) estabelece que as pessoas frequentemente **não têm** preferências estáveis à espera de serem lidas — constroem-nas durante a elicitação. A prova dura são as **inversões de preferência**: métodos normativamente equivalentes (escolher vs. fixar preço) produzem respostas sistematicamente diferentes, violando a invariância procedimental que funda toda a teoria da escolha racional.

Três consequências para uma árvore de gosto:

1. **Uma árvore que se altera a meio da conversa não está avariada — está a funcionar.** A alternativa, uma árvore que não se mexe, é mais provavelmente sinal de ancoragem na primeira estrutura proposta do que de estabilidade genuína.
2. **A estrutura da árvore não é instrumento neutro de medição — é parte da causa** do gosto expresso. A forma da pergunta determina o que se encontra.
3. **Mas isso não torna tudo arbitrário.** A corrente construtiva em apoio à decisão conclui o contrário do relativismo: como a elicitação constrói, deve ser **estruturada e explícita**, porque construção disciplinada é melhor do que construção acidental. A árvore deixa de ser um espelho e passa a ser um instrumento — e a sua qualidade mede-se pela qualidade do pensamento que provoca, não pela fidelidade a um original que não existe.

---

# PARTE IV — Quando aplicar e quando não

### 4.1 A contradição central da evidência

É preciso enunciá-la antes de qualquer recomendação, porque tudo o resto depende de como se resolve.

**A favor da decomposição:** MacGregor, sintetizando três estudos com 15 testes, reporta **redução de erro de ~42%** por decomposição judicativa sob elevada incerteza. Armstrong, Collopy e Yokum reportam redução de **dois terços** na decomposição de séries por forças causais. Kahneman e Lovallo recomendam desempacotar como antídoto à vista interna.

**Contra:** Fischhoff mostra que a estrutura da árvore determina o julgamento independentemente dos factos (4.3). Tversky e Koehler mostram que desempacotar **inflaciona** a probabilidade julgada: cancro (18%) + enfarte (22%) + outras causas naturais (33%) = **73%**, contra **58%** quando se pergunta por "morte por causa natural" como um todo. A mesma realidade, particionada de duas maneiras, dá dois números — e **MECE não protege disto, MECE é a operação que o produz**.

**A reconciliação, que é o teste mais útil de toda a investigação:**

> A decomposição **ajuda** quando a partição é conhecida e se conhece melhor as **componentes** do que o **alvo**.
> A decomposição **prejudica** quando a partição é ela própria a incógnita.

Isto não é só um critério de uso — é também o critério que distingue os três modos da Parte II. No modo diagnóstico a partição é conhecida (a fisiologia da planta, a contabilidade da empresa) e a incógnita está dentro dela. No modo de caracterização **a partição é a coisa que se está a descobrir** — e é por isso que ali a poda é proibida e a saturação substitui a exaustividade.

### 4.2 O domínio certo

O Cynefin dá a triagem mais utilizável:

| Domínio | Relação causa-efeito | Acção | Árvore? |
|---|---|---|---|
| **Clear** | óbvia a todos | sentir–categorizar–responder | desnecessária |
| **Complicated** | discernível **por peritos**, com análise | sentir–**analisar**–responder | **sim — é o seu domínio** |
| **Complex** | só visível em retrospectiva | **sondar**–sentir–responder | **não — experimentar** |
| **Chaotic** | inexistente | agir–sentir–responder | não |
| **Confused** | não se sabe em que domínio se está | decompor e atribuir | só para triagem |

O perigo próprio do domínio Complicated é nomeado: **paralisia analítica e excesso de confiança nos peritos**. E o domínio Confused é descrito como o estado por defeito e o mais perigoso, porque cada um resolve segundo a sua preferência habitual — quem gosta de árvores faz uma árvore.

> **Tensão registada:** Snowden proíbe a decomposição dentro do Complexo mas prescreve-a para sair do Confused. Não é incoerência fatal — é a pista de que **a decomposição é uma operação de *triagem* legítima e uma operação de *modelação* ilegítima**.

### 4.3 O custo da poda — está medido

O achado mais desconfortável da investigação, e o que mais directamente ataca o método da primeira parte deste dossier.

Fischhoff, Slovic e Lichtenstein deram a sujeitos uma árvore de falhas para "o carro não arranca" — bateria, sistema de combustível, e "todos os outros problemas". Um grupo recebeu a árvore completa. Outros receberam árvores **podadas**, com ramos inteiros removidos **sem aviso**.

Se as pessoas fossem sensíveis ao que falta, a fatia "outros" devia inchar para absorver os ramos removidos — de **.078** para **.468**, um factor de seis. Subiu para **.140**. Apenas **1 em 55** sujeitos dos grupos podados atribuiu a "outros" a proporção correcta ou superior. **O efeito manteve-se com mecânicos de automóveis experientes**, e a auto-avaliação de perícia não previa melhor desempenho.

E o efeito simétrico: **a importância percebida de um ramo aumenta se ele for apresentado partido em dois sub-ramos** — o que confirma, por outra via, o *splitting bias* medido por Weber, Eisenführ e von Winterfeldt em árvores de valor, onde as partes mais detalhadas recebem pesos significativamente mais elevados.

Três consequências práticas, todas contra a intuição:

1. **"Podar a árvore agressivamente" é o passo mais perigoso do método, não o mais inócuo.** O que sai da árvore sai da cabeça, e não volta.
2. **A sensação de completude não correlaciona com completude.** Uma árvore bem desenhada *sente-se* rigorosa independentemente de ser verdadeira.
3. **Subdividir um ramo aumenta-lhe o peso, independentemente do seu mérito.** Logo, numa árvore de gosto, a regra 10 (não normalizar pesos) não é preciosismo — é protecção contra um enviesamento medido.

### 4.4 Onde é mesmo má ideia

Com argumento e evidência, não com intuição:

**Luto, trauma, estados afectivos.** Duas linhas convergentes. A "hipótese do trabalho de luto" — a ideia de que é preciso confrontar e processar analiticamente a perda — tem definição imprecisa e evidência equívoca; o que funciona é **oscilação** entre orientação para a perda e orientação para a restauração, em doses geríveis (Stroebe & Schut). E a investigação sobre ruminação (Nolen-Hoeksema) mostra que o pensamento repetitivo sobre causas e consequências do humor negativo **agrava e prolonga** a depressão e, crucialmente, **prejudica a resolução de problemas**. **Uma análise de causa-raiz aplicada ao próprio estado afectivo é formalmente indistinguível de ruminação.**

**Preferências estéticas e escolhas sentidas.** Wilson & Schooler, *Thinking Too Much* (1991): quem analisou as razões da sua preferência por compotas concordou **menos** com os peritos do que os controlos; o mesmo aconteceu na escolha de cadeiras universitárias, tanto pela análise de razões como pela avaliação exaustiva de atributos. O mecanismo: analisar razões desloca a atenção para critérios **verbalizáveis mas não-óptimos**, e avaliar muitos atributos *modera* as avaliações, fazendo as opções parecerem mais equivalentes do que são. Há também redução medida da satisfação pós-escolha.

> Traduzido para o jardim: **uma árvore de gosto torna as opções mais parecidas entre si e privilegia o que se consegue dizer por palavras.** Não é um risco vago — é um efeito medido, e é o argumento mais forte para manter a árvore pequena e ancorada em exemplos concretos em vez de em categorias abstractas.

**Decisões pequenas e reversíveis.** O custo de estruturar excede o valor. Gigerenzer e o grupo ABC documentam o efeito *less-is-more*: heurísticas rápidas e frugais igualam ou batem estratégias que usam toda a informação, e uma lista de três passos supera uma análise de 19 pontos na triagem de enfarte. O conceito operativo é **racionalidade ecológica** — nenhuma heurística é boa em abstracto, é boa em relação a um ambiente, e ambientes de incerteza genuína com amostras pequenas favorecem o simples.

**Problemas genuinamente novos.** Sem classe de referência não há vista externa, e uma árvore construída por analogia é uma das manobras de "amansamento" de Conklin: tratar o problema como igual a um anterior já resolvido.

**Identidade e relações.** O caso mais puro de sistema não-estacionário sob observação: o acto de articular os ramos altera a preferência que se pretendia descobrir.

### 4.5 O teste único

> **Consigo escrever agora a frase que, daqui a seis meses, me dirá que isto está resolvido — e as outras pessoas envolvidas assinariam essa frase?**
>
> **Se sim** → decomponha. Está num problema com fronteira, com regra de paragem, e provavelmente no domínio Complicated.
> **Se não** → o trabalho ainda é sobre a **formulação**, e qualquer árvore construída agora será uma resposta à pergunta errada com aparência de rigor.

E o sinal de alarme mais fiável, suficiente sozinho: **a definição do problema muda sempre que se fala com um stakeholder diferente.**

Complemento útil, de Conklin: se se der por si a fechar a definição do problema, a declará-lo resolvido, a medir um substituto, a tratá-lo como igual a um caso anterior, a desistir, ou a reduzi-lo a duas opções — **está a tratar um problema perverso como se fosse dócil**. Note-se que a penúltima e a última dessas manobras são, respectivamente, a definição de um nó-raiz e a definição de um nível MECE.

### 4.6 O steelman

Justiça para o método, que a Parte IV maltratou:

1. **Auditabilidade.** Uma árvore torna o raciocínio inspeccionável linha a linha. Um diagrama de ciclo causal ou um mapa de diálogo não produzem um artefacto que um terceiro possa verificar. Se a decisão tem de ser defendida perante um conselho, um regulador ou um tribunal, a árvore vale independentemente da sua verdade ontológica.
2. **Localização do desacordo.** O argumento mais forte. Numa árvore, duas pessoas que discordam conseguem apontar **qual nó** é a origem da divergência. É o que Conklin quer do IBIS — entendimento partilhado sem acordo — e a árvore fá-lo também, de forma mais tosca e muito mais barata.
3. **Redução de erro medida** — os 42% de MacGregor, nas condições certas.
4. **Decompor as alavancas, não o sistema.** Mesmo não se conseguindo modelar um sistema complexo, pode-se enumerar e priorizar intervenções candidatas. Repare-se que **Meadows entrega uma hierarquia ordenada de doze pontos de alavanca como resposta à impossibilidade de modelação hierárquica** — estrutura aplicada ao espaço de acção, não ao espaço causal.
5. **A perversidade é um contínuo, não um binário.** Alford & Head formalizam nove graus. O argumento correcto nunca é "não usar árvores" — é **"não usar árvores no sub-espaço perverso de um problema misto"**.

---

# PARTE V — Correcções e mitos

| Afirmação corrente | Estatuto |
|---|---|
| A McKinsey inventou o MECE | **Nomeou-o.** Convergências independentes: Lineu 1735, Ranganathan 1937, WBS 1957-68, K-T 1958, FTA 1961. Nenhuma fonte documenta a invenção. |
| As árvores de consultoria são exaustivas | **Presumidamente, não demonstradamente.** Só a FTA e a WBS têm exaustividade formal, ambas impostas por formalismo externo. |
| *Bulletproof Problem Solving* tem um caso de "comprar vs. arrendar" | **Não existe.** Existe "Where Should I Move?" e "Will My Retirement Savings Last?". |
| ...e um caso de direitos indígenas / *native title* | **Não existe** nesse livro. Provável confusão com um caso de gestão indígena do fogo em *The Imperfectionists* (2023). |
| O caso do salmão correu 15 anos | **O livro diz as duas coisas** — "a dozen years" no cap. 8, "15-year effort" no cap. 3. |
| A árvore do salmão falhou por não ser exaustiva | **Falhou por não ser mutuamente exclusiva.** A política pública atravessava todos os ramos. |
| Facetas devem ser ME e CE | **Nível errado.** ME e CE aplicam-se dentro de cada faceta; o conjunto de facetas é aberto por desenho. |
| "Outros" resolve a falta de exaustividade | **Não.** Esconde-a, e está medido que os inquiridos não a usam correctamente. |
| Desempacotar é sempre desenviesante | **Contraditado.** É desenviesante quando a partição é conhecida; é enviesante quando não é (Fischhoff, Tversky & Koehler). |
| Uma árvore que muda a meio é sinal de má elicitação | **Ao contrário**, em modo de caracterização. Uma árvore que não muda é mais provavelmente sinal de ancoragem. |
| Analisar as razões do gosto melhora a escolha | **Falso e medido.** Piora a concordância com peritos e reduz a satisfação (Wilson & Schooler). |

---

# PARTE VI — Protocolo de decisão

```
                    ┌─────────────────────────────────────────┐
                    │ Consigo escrever a frase que, daqui a   │
                    │ 6 meses, dirá que isto está resolvido?  │
                    │ E os outros assinavam-na?               │
                    └───────────────┬─────────────────────────┘
                     NÃO ───────────┴────────── SIM
                      │                          │
        ┌─────────────▼──────────┐    ┌──────────▼───────────────┐
        │ O trabalho é sobre a   │    │ Conheço melhor as PARTES │
        │ FORMULAÇÃO.            │    │ do que o ALVO?           │
        │                        │    └──────────┬───────────────┘
        │ Ferramentas:           │      NÃO ─────┴───── SIM
        │ · IS / IS-NOT (K-T)    │       │              │
        │ · mapa de diálogo      │  ┌────▼──────┐  ┌────▼─────────────┐
        │ · facetas              │  │ Decompor  │  │ MODO DIAGNÓSTICO │
        │ · morfologia (Zwicky)  │  │ só empurra│  │ ou DECISÃO       │
        │ · sondas               │  │ a incerteza│ │                  │
        │                        │  │ para baixo│  │ MECE a sério     │
        │ Não podar. Gerar.      │  └───────────┘  │ folhas testáveis │
        └────────────────────────┘                 │ podar com receio │
                                                   └──────────────────┘

  E em qualquer ponto, se a pergunta for "que espécie de coisa é esta?"
  em vez de "porquê" ou "qual":

        ┌──────────────────────────────────────────────┐
        │ MODO CARACTERIZAÇÃO                          │
        │ eixos, não partes · ME e CE dentro do eixo   │
        │ conjunto aberto · saturação · sem pesos      │
        │ NUNCA podar — a poda é o erro caro aqui      │
        └──────────────────────────────────────────────┘
```

---

### Lacunas

- **O capítulo 9 de *Bulletproof Problem Solving* ("Wicked Problems") não foi lido** — 403. A avaliação de que Conn & McLean respondem só a metade de Rittel assenta em sumários e no índice do método; é de confiança média e deve ser confirmada contra o livro.
- **Rittel & Webber (1973) no original** está atrás de paywall; as dez características vêm de fonte universitária secundária fiel.
- **Snowden & Boone (HBR 2007)** em paywall; o material sobre os domínios vem de fontes secundárias.
- **Slovic (1995) no original** não foi lido — é a lacuna mais significativa da parte sobre preferências construídas.
- **Wilson & Schooler, Stroebe & Schut, Nolen-Hoeksema, MacGregor** foram usados em paráfrase a partir de registos e resumos, não do texto integral. São todos revistos por pares, mas os números citados devem ser verificados antes de uso citacional.
- **Bailey (1994) e Collier et al. (2012)** apenas em sumário e metadados.
- Nenhuma fonte quantifica **quantos eixos tem tipicamente uma estrutura facetada saturada** — a regra de saturação é qualitativa em todas as literaturas que a usam.

### Mapa de fontes

Listagens completas, com notas de fiabilidade, em cada memo:
[`04`](2026-09-20-research-dominios-transferencia-do-metodo.md) · [`05`](2026-09-20-research-dominios-caracterizacao-e-me-sem-ce.md) · [`06`](2026-09-20-research-dominios-limites-e-contra-indicacoes.md)

**As cinco fontes que mais sustentam este relatório:**

1. **Conn & McLean, *Bulletproof Problem Solving* (Wiley, 2019)** — texto integral, excepto cap. 9
2. **Fischhoff, Slovic & Lichtenstein (1978), *Fault Trees: Sensitivity of Estimated Failure Probabilities to Problem Representation*** — relatório original com dados
3. **Conklin, "Wicked Problems and Social Complexity"**, cap. 1 de *Dialogue Mapping* — texto primário integral
4. **Denton, exposição do modelo de facetação de Spiteri (1998)**, a partir de Ranganathan
5. **Ritchey, *General Morphological Analysis*** (swemorph.com) — fonte primária do método

---

## 4 · Fontes

*Sem secção de fontes no relatório original.*
