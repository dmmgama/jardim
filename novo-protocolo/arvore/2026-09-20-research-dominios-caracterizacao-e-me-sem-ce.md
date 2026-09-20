---
title: "Arvores que caracterizam em vez de resolver: a legitimidade de ME sem CE"
date: 2026-09-20
type: research
case: dominios
tags: [MECE, arvore, research]
---

# Arvores que caracterizam em vez de resolver: a legitimidade de ME sem CE

## 0 · Sumário executivo

- **Resposta curta: é legítimo.** Uma árvore ME-sem-CE não é uma árvore MECE defeituosa — é uma **cobertura parcial disjunta** em vez de uma partição, com tradições próprias e maduras.
- O que muda não é o rigor: muda **qual é o critério de rigor**.
- ME e CE são **logicamente independentes**. MECE é a conjunção das duas.
- **Nas facetas, a exclusividade é da característica de divisão**, e a hospitalidade — acomodar algo novo sem refazer a estrutura — é virtude, não defeito.
- **Contradição registada:** fontes enciclopédicas exigem "ME e CE" às facetas. Aplicam o critério ao nível errado.
- **Tensão na ciência da decisão:** a norma manda completar a árvore; o resultado empírico (*splitting bias*) mostra que completar por subdivisão distorce os pesos.
- **Convergência mais valiosa:** três literaturas independentes chegam ao mesmo critério de paragem — **saturação**.
- **A objecção mais séria:** Alexander escreveu o tratado canónico sobre decomposição de design e repudiou-o no ano seguinte — o domínio é semi-reticulado, não árvore.

---

## 1 · Mandato

**Prompt dado ao analista.** O caso motivador: alguém quer fazer um jardim, e quer-se construir uma árvore não para chegar a uma solução mas para **caracterizar** a situação e as preferências — com ramos a emergir organicamente, gostos a mudar a meio, sem resposta certa e sem necessidade de cobrir o universo. É um uso legítimo da forma de árvore? Qual é a literatura rigorosa?

Investigar: o estatuto formal de ME e CE como requisitos separáveis; análise por facetas (Ranganathan, Vickery, Spiteri); tipologia vs. taxonomia (Bailey; Collier et al.); Análise Morfológica Geral (Zwicky, Ritchey); pensamento focado em valores e hierarquias de objectivos (Keeney, Keeney & Raiffa); elicitação de preferências como árvore (Kelly, laddering, QOC, KJ, Alexander); estrutura emergente e grounded theory; instabilidade de preferências (Slovic; Payne, Bettman & Johnson).

O memo tem de poder responder, com citações: *é legítimo construir uma árvore ME-mas-não-CE, e sob que disciplina?*

---

## 2 · Método

Pesquisa académica e de referência, com distinção explícita entre fontes lidas integralmente, fontes consultadas apenas por excerto de motor de busca, e fontes tentadas e inacessíveis.

**Critério de arbitragem entre literaturas:** onde tradições diferentes usam o mesmo termo com regras diferentes, procurou-se o **nível** a que cada regra se aplica, em vez de escolher entre elas. Foi isso que resolveu a aparente contradição sobre facetas.

**Teste de suficiência do próprio memo:** a síntese operacional final tem de ser accionável — dez regras que substituem a exaustividade —, e não apenas descritiva.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

**A legitimidade da Exclusividade Mútua sem Exaustividade Colectiva**

> Memo de analista B (#5 de 6). Investigação autónoma, base documental própria.
> Segunda investigação. Ver também: `2026-09-20-research-dominios-transferencia-do-metodo.md`, `2026-09-20-research-dominios-limites-e-contra-indicacoes.md`, os exercícios em `2026-09-20-sintese-jardim-exercicios-aplicados.md`, e a síntese `2026-09-20-sintese-dominios-aplicacao-a-outros-dominios.md`.

---

### 0. Resposta curta

Sim, é legítimo. Uma árvore ME-mas-não-CE não é uma árvore MECE defeituosa: é uma **família formal distinta** — uma *cobertura parcial disjunta* em vez de uma *partição* — e tem tradições metodológicas próprias, maduras e com regras próprias (análise por facetas, tipologia conceptual, Análise Morfológica Geral, hierarquias de objectivos fundamentais, *pattern languages*). O que muda não é o rigor: muda **qual é o critério de rigor**. A exaustividade deixa de ser a disciplina e é substituída por exclusividade *local*, hospitalidade declarada, não-redundância, consistência cruzada e saturação. O erro grave não é omitir ramos — é omitir ramos **sem declarar o âmbito** dentro do qual a árvore pretende ser completa.

---

### 1. Estatuto formal: ME e CE são requisitos separáveis

Em teoria de conjuntos a distinção é limpa. Uma **partição** exige três coisas: blocos não vazios, disjuntos, e cuja união devolve o conjunto original. Uma família apenas **disjunta** satisfaz ME e admite lacunas; uma **cobertura** satisfaz CE e admite sobreposições. ME e CE são, portanto, condições logicamente independentes — MECE é a conjunção das duas, não uma propriedade unitária.

O princípio MECE (Barbara Minto, McKinsey, finais dos anos 60) é explicitamente o análogo prático da partição, e a própria literatura reconhece limites: MECE *"does not exclude superfluous/extraneous items"*, forçar respostas a este molde pode ser desnecessariamente limitativo, e a exclusão de redundâncias é por vezes indesejável. O exemplo canónico de falhanço — classificar pessoas por nacionalidade — falha *nas duas* dimensões em simultâneo (dupla nacionalidade viola ME; apátridas violam CE), o que ilustra bem que são eixos distintos.

**Quando CE é genuinamente obrigatória** (a lista é curta e reconhecível):

```
CE OBRIGATÓRIA
├── partições de probabilidade      → lei da probabilidade total; somas = 1
├── contabilidade / auditoria       → asserção de completude; nada fora do balanço
├── orçamento / alocação            → percentagens têm de fechar a 100%
├── estatística oficial (ex. ICD)   → todo o caso tem de ser codificável
├── inquéritos fechados             → opções têm de ser exaustivas e exclusivas
└── pesos em MAVT/AHP               → normalizar pesos a 1 ASSUME o conjunto exaustivo
```

```
CE DISPENSÁVEL (ou nociva)
├── caracterização exploratória     → facetas, tipologias conceptuais
├── espaços de design               → QOC, pattern languages
├── estruturação de problemas "wicked" → AMG
├── elicitação de gosto/valores     → laddering, repertory grid
└── teoria emergente                → grounded theory
```

O último item da primeira lista é o mais subtil e o mais relevante para o caso do jardim: **no momento em que se atribuem pesos que somam 1, está-se tacitamente a declarar que a árvore é exaustiva**. Uma árvore puramente caracterizadora, sem pesos normalizados, não faz essa afirmação e não precisa de a honrar.

**Mundo aberto vs. mundo fechado.** A mesma distinção reaparece na representação de conhecimento. Sob *closed-world assumption* (CWA), o que não é demonstrável é falso — a base é assumida completa (bases de dados relacionais). Sob *open-world assumption* (OWA), a ausência de informação significa "desconhecido", não "falso"; ontologias OWL adoptam-na precisamente porque é inviável representar explicitamente toda a informação negativa. Uma árvore ME-sem-CE é simplesmente uma **árvore em mundo aberto**. É incoerente exigir-lhe uma garantia de cobertura que ela nunca prometeu — e é igualmente incoerente usá-la depois como se fosse CWA (p. ex. concluir "o cliente não quer X porque X não está na árvore").

**A convenção "e outros" e as suas patologias.** O remendo habitual para fabricar CE artificial é a categoria residual: em inquéritos, "outro, por favor especifique" é recomendado sempre que não se possa garantir opções exaustivas. Mas o remendo tem custo documentado: os inquiridos tendem a escolher as opções apresentadas em vez de escreverem a sua própria, ou seja, o residual **absorve mal** o que devia capturar. Star e Bowker vão mais longe: categorias residuais são as que *"cannot be formally represented within a given classification system"*, e a sua gestão é um problema ético e político, não apenas técnico — na ICD, a regra prática é *distribuir* os "not elsewhere classified" por toda a estrutura e nunca os colocar ao nível de topo. Conclusão operativa: **"Outros" não converte uma cobertura parcial numa partição; apenas esconde a incompletude atrás de uma etiqueta**. Mais vale declarar o âmbito.

---

### 2. Análise por facetas: o caso-modelo de ME sem CE global

Ranganathan (Colon Classification, PMEST: *Personality, Matter, Energy, Space, Time*) rompe com a classificação enumerativa: em vez de um lugar pré-definido para cada assunto, analisa-se o assunto em facetas e sintetiza-se a notação. As consequências: múltiplos caminhos de acesso, filtragem dinâmica, e — a palavra-chave — **hospitalidade** para assuntos novos.

As regras, na reformulação simplificada de **Louise Spiteri (1998)** tal como exposta por William Denton, são explícitas quanto ao que tem de ser exclusivo:

```
PLANO DAS IDEIAS — escolha de facetas
├── Diferenciação     distinguir claramente entre as partes componentes
├── Relevância        facetas reflectem propósito, assunto e âmbito do sistema
├── Averiguabilidade  facetas definidas e verificáveis
├── Permanência       qualidades duradouras, não atributos transitórios
├── Homogeneidade     "facets must be homogeneous"
└── Exclusividade     "each facet must represent only one characteristic of division"

PLANO DAS IDEIAS — ordem de citação
├── Sucessão relevante   (cronológica, espacial, de complexidade…)
└── Sucessão consistente (estável, salvo mudança de propósito)
```

**Contradição a assinalar, porque é central.** A entrada da Wikipédia sobre *faceted classification* afirma que as facetas devem ser *"clearly defined, mutually exclusive, and collectively exhaustive"* — aparentemente contradizendo a tese de que o conjunto de facetas é aberto. A leitura correcta, sustentada por Denton/Spiteri e pelo cânone da hospitalidade, é que **a exaustividade se aplica ao *array* dentro de uma faceta, não ao conjunto de facetas**: dentro da faceta "exposição solar" as condições devem esgotar o espectro relevante e não se sobrepor; mas nada obriga a que "exposição solar + solo + manutenção + estilo" esgotem a essência de um jardim. Denton é claro ao dizer que sistemas facetados são hospitaleiros a novas entidades, mantendo cada faceta internamente exclusiva. **Quem cita a fórmula "ME+CE" para facetas está a aplicar o critério ao nível errado.**

Aplicação directa ao jardim:

```
JARDIM (faceta = eixo de caracterização; conjunto aberto)
├── Luz          : pleno sol | meia-sombra | sombra
├── Água         : rega automática | manual | seco/mediterrânico
├── Manutenção   : alta | média | negligência deliberada
├── Uso          : contemplativo | produtivo | infantil | recepção
├── Estação-alvo : primavera | verão | inverno estrutural
└── [faceta nova a acrescentar quando emergir na conversa]
```

Cada linha é ME internamente. O conjunto de linhas **não pretende ser CE** — e é por isso que aguenta o momento em que a pessoa diz, a meio, "afinal o que me interessa é o cheiro à noite": acrescenta-se a faceta "Aroma/nocturnidade" sem refazer a árvore. É exactamente esta propriedade — **extensão sem reconstrução** — que uma árvore MECE não tem.

Na arquitectura de informação, o corolário prático é a **polihierarquia**: a Nielsen Norman Group nota que *"some things don't fit cleanly in just one category"* e recomenda polihierarquia com contenção, ou navegação facetada em alternativa à referência cruzada exaustiva.

---

### 3. Tipologia vs. taxonomia vs. classificação

Bailey (*Typologies and Taxonomies*, 1994) fixa a distinção que resolve metade da questão: **tipologia classifica conceitos; taxonomia classifica entidades empíricas**. E acrescenta o par monotético/politético: em classes monotéticas todos os casos partilham características idênticas sem excepção; em classes politéticas agrupa-se por semelhança global, sem identidade em todas as variáveis. Tipos heurísticos tendem a ser monotéticos e conceptuais; tipos empíricos, politéticos e quantitativos.

A implicação: uma **tipologia conceptual** construída por cruzamento de dimensões é automaticamente ME e CE *no espaço de propriedades* — mas a prática consiste em reduzir esse espaço, eliminando células vazias ou absurdas, o que **destrói a CE e preserva a ME**. (Redução do espaço de propriedades, tradição Lazarsfeld–Barton retomada por Bailey; assinalo-a como conhecimento estabelecido que *não* foi confirmado numa fonte lida integralmente nesta pesquisa.)

Collier, LaPorte e Seawright (*Putting Typologies to Work*, PRQ 2012) dão o padrão de rigor: conceito abrangente explícito no título, variáveis de linha e de coluna que desagregam esse conceito, matriz, e tipos-célula com significado conceptual próprio. Notavelmente, **não impõem ME+CE de forma uniforme**: aceitam ordens parciais e tipos-célula ambíguos que continuam analiticamente úteis. Exigem sim critérios consistentes de formação dos tipos e que não se misturem tipologias conceptuais com tipologias explicativas. O contraste com o MECE consultivo é instrutivo: **a exigência deslocou-se de *cobertura* para *consistência do critério de divisão***.

---

### 4. Análise Morfológica Geral (Zwicky, Ritchey): caracterização explícita

A AMG é a formalização mais pura de "árvore que caracteriza". Ritchey define-a como *"a method for structuring and investigating the total set of relationships"* em complexos de problemas multidimensionais e não quantificáveis. Foi concebida por Fritz Zwicky para problemas onde, nas palavras do material de Ritchey, *"quantitative methods, causal modeling and simulation are relatively useless"*, porque os factores têm forte dimensão social e política.

Método:

```
1. Parâmetros    (dimensões do problema)
2. Condições     (estados possíveis de cada parâmetro — ME dentro do parâmetro)
3. Campo morfológico (caixa de Zwicky = produto cartesiano das condições)
4. CCA — Cross-Consistency Assessment (comparação par-a-par de condições)
      ├── contradições lógicas
      ├── restrições empíricas
      └── restrições normativas
5. Espaço-solução (subconjunto internamente consistente)
```

Dois pontos decisivos. Primeiro, o produto não é uma solução mas *"a smaller set of internally consistent configurations"* representando um espaço-solução, funcionando como *"inference model or virtual laboratory"* — a caixa **caracteriza** e o utilizador navega-a. Segundo, a AMG substitui a exaustividade por outra disciplina: a CCA fornece *"in-built garbage detection"*, porque parâmetros mal definidos e gamas de condições incompletas tornam-se imediatamente visíveis quando se tenta avaliar a consistência cruzada. **A coerência interna faz o trabalho que a exaustividade faria.**

Para o jardim, isto é directamente utilizável: incompatibilidades como "sombra profunda × horta produtiva" ou "manutenção nula × sebes topiadas" são eliminadas por CCA, e o que resta é o espaço de jardins coerentes com a pessoa — **sem jamais ter de enumerar o universo dos jardins possíveis**.

---

### 5. Pensamento focado em valores: a resposta rigorosa da ciência da decisão

Keeney e Raiffa (1976) fixam as propriedades desejáveis de um conjunto de atributos: **completude, operacionalidade, decomponibilidade, não-redundância e dimensão mínima**. Keeney (*Value-Focused Thinking*, 1992) acrescenta a distinção estruturalmente mais importante para o nosso problema:

```
HIERARQUIA DE OBJECTIVOS FUNDAMENTAIS   — árvore de fins (o que se valoriza em si)
        vs.
REDE DE OBJECTIVOS MEIOS-FINS           — rede causal (o que serve para atingir fins)
```

O teste separador é o **WITI** (*"Why Is This Important?"*): se a resposta remete para outro objectivo, é um meio; se é intrinsecamente valioso, é um fim. Os meios formam uma **rede**, não uma árvore — um meio alimenta vários fins. Já a hierarquia de fundamentais é uma árvore e é aí, e só aí, que a completude é exigida (e que os pesos somam 1).

E é aqui que a literatura contém uma **tensão interna explícita**: completude e dimensão mínima são requisitos antagónicos. A prática de MCDA assume-o abertamente — o objectivo é um bom equilíbrio entre completude e simplicidade, para que o esforço de elicitação não seja excessivo. As National Academies admitem que se deve evitar *"too few or too many objectives"* mas que *"there are no exact rules for doing so"*, e propõem um critério pragmático de paragem: se, ao comparar alternativas, nenhum interessado levanta novos objectivos, a lista é adequada. **Isto é saturação, não exaustividade.**

Pior (ou melhor, consoante o ponto de vista): a completude obtida por subdivisão é activamente enviesante. Weber, Eisenführ e von Winterfeldt (*Management Science*, 1988) mostraram que partes mais detalhadas da árvore de valor recebem pesos significativamente mais elevados — o **splitting bias** —, efeito atribuído à maior saliência dos atributos explicitados em detalhe, e confirmado depois em vários métodos e populações (Jacobi & Hobbs, *Decision Analysis*, 2007).

> **Contradição a assinalar:** a norma prescritiva manda completar a árvore; o resultado empírico mostra que completar por subdivisão **distorce os pesos**. Em contexto de gosto pessoal — onde não há verdade externa a proteger — isto é um argumento forte a favor de árvores pequenas, assumidamente parciais, e sem pesos normalizados.

---

### 6. Elicitar preferências como árvore: o repertório de técnicas

- **Kelly, Teoria dos Construtos Pessoais / repertory grid.** Cada pessoa constrói o seu próprio enquadramento conceptual; os construtos são **bipolares** (elicitados pelo método da tríade: como é que dois são semelhantes e diferentes de um terceiro), e organizam-se hierarquicamente. Note-se: **um construto bipolar é ME por construção e nunca CE** — "formal/informal" não esgota o mundo, apenas o discrimina utilmente.
- **Laddering (Reynolds & Gutman) e means-end chain (Gutman, 1982).** Repetir "porque é que isso é importante para si?" para subir de **atributos → consequências → valores**, e codificar em *Hierarchical Value Maps*. É o WITI de Keeney com outro nome e outra disciplina — e produz um mapa das cadeias mais frequentes, não uma cobertura.
- **QOC (MacLean, Young, Bellotti & Moran, 1991).** *Questions, Options, Criteria*: notação semiformal para representar o **espaço de design** em torno de um artefacto. As Questões identificam pontos de decisão, as Opções são respostas possíveis, os Critérios avaliam-nas. O objecto explícito é o espaço, não a solução — e o valor está na rastreabilidade do raciocínio.
- **KJ / diagramas de afinidade (Kawakita, anos 60) e card sorting.** Aqui a estrutura **emerge**: agrupam-se cartões por relação percebida, permitindo a emergência de categorias em vez de as impor por um esquema de codificação pré-definido; os títulos de categoria escrevem-se **depois** do agrupamento.
- **Christopher Alexander.** *Notes on the Synthesis of Form* (1964) é decomposição hierárquica pura — o algoritmo HIDECS 2 parte o conjunto de variáveis nos dois subconjuntos com transferência mínima de informação. Mas **Alexander repudiou o método** quase de imediato em *"A City is Not a Tree"* (1965) e repetiu a repudiação no prefácio de 1971: os subsistemas sobrepõem-se, a estrutura certa é o **semi-reticulado**, em que *"each node has relationships with many nodes"*. *A Pattern Language* é a consequência: uma rede de padrões com ligações a montante e a jusante. O padrão 172, *Garden Growing Wild* — *"A garden which grows true to its own laws"* — liga-se a *Terraced Slope* (169) e *Fruit Trees* (170) a montante, a *Greenhouse* (175), *Garden Seat* (176) e *Still Water* (71) a jusante, e é referenciado por *Half-Hidden Garden* (111) e *Site Repair* (104).

> **Contradição a assinalar, e é a mais séria deste memorando:** a autoridade mais óbvia para "árvore de design de jardim" argumentou explicitamente que **o domínio não é uma árvore**. Quem usa a forma de árvore para um jardim deve saber que está a projectar um semi-reticulado numa árvore, e que essa projecção perde as sobreposições — a faceta é uma forma de recuperar parte do que se perde.

---

### 7. Estrutura emergente: que disciplina substitui o MECE

Na grounded theory a sequência é **codificação aberta → axial → selectiva**: fragmentar e etiquetar, relacionar fragmentos com categorias mais amplas, e integrar numa categoria central. Os dispositivos de rigor que substituem a exaustividade são dois:

1. **Comparação constante** — cada novo dado é comparado com as categorias existentes, refinando-as;
2. **Saturação teórica** — pára-se quando novos dados deixam de contribuir para o desenvolvimento da teoria.

Traduzido para a árvore do jardim: a árvore está "pronta" não quando cobre todos os jardins possíveis, mas quando **uma nova pergunta deixa de produzir um ramo novo**.

Esta é, note-se, literalmente a mesma regra de paragem que as National Academies propõem para hierarquias de objectivos. **É a convergência mais útil de toda esta pesquisa:** duas literaturas independentes — qualitativa-indutiva e decisória-prescritiva — chegam ao mesmo critério de suficiência quando abandonam a exaustividade.

---

### 8. Instabilidade das preferências: a árvore que se mexe não está avariada

Slovic (1995) e a colecção de Lichtenstein & Slovic (2006) estabelecem que as preferências são frequentemente **construídas durante a elicitação**, não lidas de uma lista pré-existente — *"preferences are not simply read off some master list"*. A prova dura são as **inversões de preferência**: métodos normativamente equivalentes (escolha vs. fixação de preço) produzem respostas sistematicamente diferentes, violando a invariância procedimental que funda todas as teorias da escolha racional. Payne, Bettman e Johnson acrescentam o mecanismo: a decisão é processamento de informação altamente contingente, sensível à complexidade da tarefa, pressão temporal, modo de resposta, enquadramento e pontos de referência.

Consequências para a árvore de gosto, directas:

- **Uma árvore que se altera a meio da conversa não é sinal de falhanço de elicitação — é o comportamento esperado.** A alternativa (uma árvore que não se mexe) é mais provavelmente sinal de ancoragem na primeira estrutura proposta do que de estabilidade genuína das preferências.
- **A forma da pergunta determina o que se encontra.** Isto agrava o *splitting bias*: a estrutura da árvore não é um instrumento neutro de medição do gosto, **é parte da causa do gosto expresso**.
- **Mas** — e aqui há tensão na literatura, que deve ser assinalada — a corrente construtiva em apoio à decisão (Gregory, Slovic) não conclui que "tudo é arbitrário"; conclui que a elicitação deve ser *estruturada e explícita* precisamente porque constrói. A construção disciplinada é preferível à construção acidental. Em vez de tentar capturar preferências estáveis, a árvore torna-se **o próprio instrumento de construção**, e a sua qualidade mede-se pela qualidade do pensamento que provoca, não pela fidelidade a um original que não existe.

---

### 9. Síntese operacional

Uma árvore ME-mas-não-CE é legítima sob esta disciplina composta:

```
 1. Declarar o âmbito       → CE relativa a um universo explicitado, não absoluta
 2. ME apenas localmente    → exclusiva dentro de cada faceta/array (Spiteri)
 3. Hospitalidade explícita → prever o acrescento de facetas sem refazer a árvore
 4. Um só critério de divisão por nível (Collier et al.; Ranganathan)
 5. Separar fins de meios   → teste WITI; meios formam rede, não árvore (Keeney)
 6. Não-redundância         → evitar dupla contagem (Keeney & Raiffa)
 7. Consistência cruzada    → eliminar combinações incompatíveis (CCA, Ritchey)
 8. Saturação               → parar quando novas perguntas não geram ramos novos
 9. Não normalizar pesos    → somar a 1 é afirmar exaustividade que não se tem
10. Registar o raciocínio   → Questões/Opções/Critérios (QOC), incluindo ramos abandonados
```

O ponto 9 é o guarda-costas de toda a construção:

> **É lícito não ser exaustivo desde que não se faça nenhuma operação que pressuponha exaustividade.**
>
> Caracterizar, comparar, gerar, dar a ver — lícito.
> Ponderar, somar a 100%, afirmar "não existe mais nada" — ilícito.

---

---

## 4 · Fontes

**Lidas integralmente**

- `en.wikipedia.org/wiki/MECE_principle` — enciclopédico; bom para definição e origem (Minto), inclui secção de críticas; verificar contra fonte primária para citações de Minto.
- `en.wikipedia.org/wiki/Faceted_classification` — enciclopédico; útil para PMEST, mas contém a formulação "mutually exclusive and collectively exhaustive" aplicada ao nível errado (ver §2) — usar com cautela.
- `miskatonic.org/library/facet-web-howto.html` — William Denton, bibliotecário; exposição fiel e citável do modelo de Spiteri; **a melhor fonte lida sobre as regras de facetação**.
- `swemorph.com/ma.html` — sítio oficial de Tom Ritchey; fonte primária da AMG moderna; parcial por ser autoral, mas autoritativa quanto ao método.
- `en.wikipedia.org/wiki/Morphological_analysis_(problem-solving)` — enciclopédico; confirma Zwicky, CCA e a aplicação a problemas "wicked".
- `cambridge.org/core/books/working-with-concepts/putting-typologies-to-work/...` — Cambridge UP, capítulo de Collier/LaPorte/Seawright; académico de topo; apenas metadados e sumário acessíveis sem subscrição.
- `lesswrong.com/posts/.../value-focused-thinking-a-chapter-by-chapter-summary` — resumo secundário de Keeney (1992), não revisto por pares; fiável na estrutura (WITI, fundamentais vs. meios), a confirmar no original para citações literais.
- `nationalacademies.org/read/24874/chapter/9` — National Academies Press; institucional e revisto; **excelente para o critério prático de paragem** na elicitação de objectivos.
- `jonkolko.com/phd/writing/25-06-27-construction-of-preference` — nota de leitura pessoal sobre Slovic; útil para citações curtas, mas é fonte terciária — confirmar no original.
- `nngroup.com/articles/polyhierarchy/` — Nielsen Norman Group; profissional, bem fundamentado empiricamente; **melhor fonte lida sobre falhanço prático da exclusividade mútua** em arquitectura de informação.
- `patternlanguage.cc/Patterns/Garden-Growing-Wild-(172)` — transcrição não oficial de Alexander et al.; conteúdo do padrão fiável, numeração a confirmar (fontes divergem entre 172 e 173).
- `en.wikipedia.org/wiki/A_City_Is_Not_a_Tree` — enciclopédico e muito sumário; confirma a tese árvore/semi-reticulado, mas sem citações extensas do ensaio original.

**Consultadas apenas por excerto de motor de busca (não lidas na íntegra)**

- `pubsonline.informs.org/doi/10.1287/deca.1070.0100` — *Decision Analysis* (INFORMS), revisto por pares; splitting bias quantificado e mitigado.
- `ideas.repec.org/a/inm/ormnsc/v34y1988i4p431-445.html` — registo de Weber, Eisenführ & von Winterfeldt (1988), *Management Science*; **fonte primária do splitting bias**.
- `sciencedirect.com/science/article/abs/pii/S0377221719301870` — *EJOR*, revisto por pares; hierarquias de objectivos concisas, compromisso completude/simplicidade.
- `link.springer.com/article/10.1007/s10676-007-9141-7` — Star & Bowker, *Ethics and Information Technology*; fonte primária sobre categorias residuais; acesso bloqueado por autenticação.
- `en.wikipedia.org/wiki/Open-world_assumption` — enciclopédico; definições OWA/CWA suficientemente padronizadas.
- `en.wikipedia.org/wiki/Ladder_interview` e `en.wikipedia.org/wiki/Personal_construct_theory` — enciclopédicos; adequados para o esqueleto de laddering e repertory grid.
- `dl.acm.org/doi/10.1207/s15327051hci0603%264_2` — MacLean et al. (1991), *Human–Computer Interaction*; fonte primária do QOC.
- `en.wikipedia.org/wiki/Affinity_diagram` e `pmc.ncbi.nlm.nih.gov/articles/PMC13526983/` — o segundo é artigo revisto por pares e é a melhor base para a afirmação de que as categorias no método KJ **emergem** em vez de serem impostas.
- `delvetool.com/blog/openaxialselective` — fonte comercial/divulgativa; correcta mas superficial sobre grounded theory; confirmar em Strauss & Corbin.
- `polisci.berkeley.edu/.../PuttingTypologiesAppendixandArticle_0.pdf` e o PDF de Bailey em ResearchGate — fontes primárias em PDF; não extraíveis nesta sessão.

**Tentadas e não lidas** (PDF binário ou bloqueio): `swemorph.com/pdf/gma.pdf`; `swemorph.com/pdf/it-webart.pdf`; `bear.warrington.ufl.edu/brenner/mar7588/Papers/slovic-ampsy1995.pdf` (Slovic 1995 no original — **a lacuna mais significativa deste memorando**); `archive.iainstitute.org/.../a_simplified_model_for_facet_analysis.php` (certificado inválido); `conbio.onlinelibrary.wiley.com/doi/full/10.1111/csp2.13155` (403).
