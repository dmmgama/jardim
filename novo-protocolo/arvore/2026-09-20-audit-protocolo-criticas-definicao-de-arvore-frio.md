---
title: "Criticas a definicao de arvore no protocolo (agente frio, controlo independente)"
date: 2026-09-20
type: audit
case: protocolo
tags: [MECE, arvore, audit, controlo-independente]
sobre:
  - "[[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]]"
  - "[[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]]"
---

# Criticas a definicao de arvore no protocolo (agente frio, controlo independente)

## 0 · Sumário executivo

- **Controlo independente.** Mesmo mandato, agente sem contacto com o trabalho anterior, leitura restrita às duas sínteses e aos dois documentos do protocolo.
- **Convergiu** com a auditoria paralela em quatro pontos, obtidos independentemente: o erro de nível no ME/CE, a poda e o estudo de Fischhoff, a triagem aplicada onde a magnitude é a incógnita, e os desencontros de identificadores.
- **Quatro achados próprios**, que a outra auditoria não tinha: a quarta saída de acoplamento `escapar`; a ausência de identificador na regra das árvores concorrentes; a obrigação de **declarar o formalismo que sustenta a exaustividade**, com residual nomeado; e o estado `suspenso: por dimensionar` com gatilho de reformulação da raiz.
- Identificou também que `P1.1` não exige raiz escrita, decisor, precisão nem horizonte — os campos que a síntese aponta como sistematicamente omitidos.
- Reportou sete inconsistências entre os dois documentos do protocolo.

---

## 1 · Mandato

**Prompt dado ao agente, em sessão fria.** Leitura restrita a quatro ficheiros — as duas sínteses de investigação e os dois documentos do protocolo — com interdição explícita de abrir qualquer outro ficheiro da pasta, incluindo os exercícios aplicados e o trabalho paralelo sobre o mesmo mandato:

> *"Existem outros trabalhos sobre o mesmo tema nesta pasta e o objectivo deste exercício é obter um julgamento independente. Se abrires, destróis o valor do que te é pedido."*

Tarefa: críticas à forma como os agentes definiram a árvore nos documentos do protocolo, confrontando com a evidência das sínteses; específico quanto à regra criticada, ao que está errado, à evidência e à correcção; incluindo o que está certo e é melhor do que a prática documentada; ordenado por gravidade.

---

## 2 · Método

**Desenho de controlo.** O mandato é idêntico ao da auditoria paralela e a leitura é restringida para impedir contaminação. A convergência entre as duas auditorias em pontos obtidos independentemente é o sinal com valor — não a concordância obtida por leitura mútua.

O método interno é do próprio agente e está declarado na secção 0 do corpo do relatório.

**Uso previsto:** comparação com a auditoria paralela, e alimentação do documento operacional combinado.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

### 0 · Método e limites desta crítica

Li quatro documentos e só quatro: as duas sínteses de investigação e os dois documentos de protocolo (arquitectura §2.2, R3 §7). Não li nenhum outro ficheiro do repositório, nem o documento de protocolo com as famílias P4–P10 que o R3 cita e que não está entre os quatro. Nada aqui foi verificado contra trabalho paralelo sobre o mesmo tema.

**Estatuto da evidência invocada.** As sínteses declaram o que leram na origem e o que leram em paráfrase. Marco-o sempre que é material:

- **Primário, lido na origem:** McKinsey Staff Paper No. 66 (2007); Fischhoff, Slovic & Lichtenstein (1978); Conn & McLean, *Bulletproof Problem Solving* (2019, excepto cap. 9); Conklin cap. 1; Ritchey.
- **Segunda mão declarada pelas próprias sínteses:** MacGregor (redução de erro ~42%), Wilson & Schooler, Nolen-Hoeksema, Stroebe & Schut, Rittel & Webber, Snowden & Boone, Slovic (1995), Rasiel. Os números destes devem ser confirmados antes de uso citacional — a síntese 00b di-lo explicitamente na secção *Lacunas*.
- **Camada de preparação para entrevista, marcada [prep] na origem:** largura 3–5 ramos por nó; as 13 estruturas da Nespresso; as seis desagregações do lucro.

Não cito nada que não esteja numa das duas sínteses.

---

### 1 · Inconsistências de identificadores entre os dois documentos

Isto vem primeiro porque não é uma questão de julgamento: é verificável por leitura e afecta toda a capacidade de invocar regras.

**Os identificadores `P1.x` têm dois referentes incompatíveis.**

A arquitectura define exactamente três famílias: `P0.1`–`P0.8`, `P1.1`–`P1.7`, `P2.1`–`P2.6`. O R3 cita, como se existissem, `P0.10`, `P0.14`–`P0.21`, `P1.9`, `P1.11`, `P1.12`, `P1.13`, `P2.8`, `P2.11`, `P2.12`, `P2.15`–`P2.18`, e famílias inteiras `P4`–`P10` mais uma cláusula `C.4`. Nenhum destes existe na arquitectura.

**Há colisão directa, não apenas ausência.** O R3 §3 atribui a `P0.5` e `P0.6` o "tecto numérico de árvores e de frentes". Na arquitectura, `P0.5` é "o mandato deve ser redigido por agente, por reformulação" e `P0.6` é "o agente não pode acrescentar objectivo ou não-objectivo que o humano não tenha enunciado". Um agente que receba os dois documentos e invoque `P0.6` não tem maneira de saber qual das duas normas está a invocar.

**Duas normas que o R3 declara terem ganho identificador não têm identificador.** R3 §3 regista "Exaustividade por propósito convertida em regra → `P1.11`, `P1.12`" e "Accionabilidade do corte convertida em regra → `P1.13`". Na arquitectura, ambas continuam em prosa: a exaustividade por propósito vive na tabela dos quatro propósitos e no parágrafo "Colectivamente exaustivo varia com o propósito"; a accionabilidade vive sob "Critério de corte". `P1` pára em `P1.7` e nenhuma das duas lá está. Como a operação 2 do R3 §1 é precisamente "atribuição de identificador a toda a norma que existia em prosa", o R3 declara cumprida uma operação que o documento que temos não mostra cumprida.

**Leitura mais provável, e o que falta para a confirmar.** R3 §1 diz que a "proposta de arquitectura recebida" contribuiu com "protocolos P0 a P2". Isto sugere que `arquitectura-governo.md` é a *proposta*, e que o R3 comenta um *terceiro* documento — o protocolo consolidado, com P0–P10 e cláusulas C. Se for esse o caso, a incoerência não é erro de citação mas ausência de aviso: nenhum dos dois documentos diz ao leitor que os `P1.x` de um não são os `P1.x` do outro. **Correcção mínima: prefixar as famílias por documento (`A-P1.4` vs `L-P1.4`) ou renumerar o protocolo consolidado fora do espaço P0–P2.** Enquanto isso não existir, qualquer regra citada por identificador é ambígua.

**Vocabulário sem definição.** `cone` e `subcone` são usados no R3 (§7.3 "o cone a jusante é recalculado"; §7.4 "cada pressuposto invalidado poda um subcone inteiro") e são operacionalmente centrais. A arquitectura nunca usa a palavra. A definição — presumivelmente o fecho transitivo a jusante pelas arestas de `P1.4` — só existe por inferência.

**Contradição substantiva entre os dois documentos.** Arquitectura §1.3: o sistema "não se aplica a projectos de frente única". R3 §4: a "exclusão de projectos de frente única" foi **não adoptada**, com fundamento. O R3 revoga a arquitectura sem o assinalar como revogação.

**Contradição interna na arquitectura.** §2.4.1 estabelece que "um nível nunca escreve no nível acima"; as árvores são L1; os estados de ramo (`fechado`, `podado`) mudam por acção de frentes, que são L3, e R3 §7.3 confirma-o ("Fechar. Com resultado registado. O fecho devolve ao caminho"). Ou o estado de ramo não é L1, ou a regra tem uma excepção não declarada.

**Travão declarado e travão real.** Arquitectura T5: "Travão único: P1.1 — condição de morte declarada ao nascer". R3 §3 diz que foi acrescentado um tecto numérico de árvores. O "único" deixou de ser único e a tensão T5 ficou por actualizar.

---

### 2 · Críticas, por gravidade

#### G1 · A poda é declarada gratuita. É a operação mais cara que existe, e está medido.

**O que está escrito.** Arquitectura §2.2: *"Esta triagem é gratuita e é o que impede a árvore de gerar frentes a mais."* R3 §7.4: *"Esta operação é gratuita e é a única que impede a árvore de gerar frentes em excesso."* A palavra é a mesma nos dois documentos e não é retórica: é o fundamento de `P1.5`.

**A evidência.** Fischhoff, Slovic & Lichtenstein (1978) — relatório original, lido na íntegra pela síntese 00b, que é a fonte experimental mais forte de todo o dossier. Deram a sujeitos uma árvore de falhas para "o carro não arranca". Uns receberam a árvore completa; outros, árvores com ramos inteiros removidos **sem aviso**. Se as pessoas fossem sensíveis ao que falta, a fatia "outros" deveria ter subido de `.078` para `.468` — um factor de seis. Subiu para `.140`. **Apenas 1 em 55** sujeitos dos grupos podados atribuiu ao residual a proporção correcta ou superior. O efeito manteve-se em mecânicos de automóveis experientes, e a auto-avaliação de perícia não previa melhor desempenho. A síntese 00b §4.3 conclui: *"'Podar a árvore agressivamente' é o passo mais perigoso do método, não o mais inócuo. O que sai da árvore sai da cabeça, e não volta."*

**Porque é que o protocolo é especialmente exposto a isto.** A condição experimental de Fischhoff — ramos removidos **sem aviso** — não é um acidente que o protocolo evite: é o seu desenho declarado. R3 §7.1: *"Um agente não vê nenhuma das duas [existências]. Vê o seu próprio ramo e as fronteiras negativas dos ramos vizinhos."* Um agente que triar, dimensionar ou estimar dentro do seu ramo está exactamente na posição do sujeito de 1978. O protocolo produz a podagem silenciosa como serviço.

**O que o protocolo já faz bem aqui, e é preciso dizê-lo.** `P1.6` obriga a registar a razão da poda; `REJEICOES` acumula; o slug morto bloqueia a recriação. A síntese 00 regista, como achado negativo, que **não existe na prática de referência nenhuma prática de guardar a árvore original para auditoria** — "nada no Staff Paper, nada nos relatos", sendo a descrição dominante a de reescrita contínua sem versionamento. O protocolo resolve uma lacuna real. Mas resolve o problema errado: o registo da razão protege contra **reabertura**, não contra **subestimação do residual**. São dois riscos distintos e só o primeiro está coberto.

**Correcção concreta.** Três regras, e a terceira é a que importa:

- **`P1.5-a`** — A poda é de dois graus. *Poda visível*: o nó desaparece do trabalho mas **o seu rótulo e o seu estado permanecem na projecção de todos os ramos irmãos**. *Poda invisível*: o nó sai da projecção. A poda invisível **não pode** ser aplicada por triagem de ordem de grandeza — só por fecho com resultado (`P1.5` e `P1.6` passam a distinguir-se).
- **`P1.5-b`** — Todo o nó de árvore de problema **deve** ter um ramo residual nomeado e visível, que não é "Outros". A síntese 00b §3.3 é explícita a este respeito: *"a categoria 'Outros' não converte uma cobertura parcial numa partição — esconde a incompletude atrás de uma etiqueta"*, e há medida de que os inquiridos não a usam correctamente. O residual tem de dizer **o que foi retirado**, não que algo foi retirado.
- **`P1.5-c`** — Quando um ramo é podado por triagem, a aresta de `P1.4` que dele partia **não** é eliminada: fica marcada `podada`. O cone a jusante continua a existir. Sem isto, podar amputa silenciosamente o mecanismo de detecção, que é a coisa mais valiosa do sistema.

---

#### G2 · "Mutuamente exclusivo aplica-se sempre" é falso no modo de caracterização, e o erro propaga-se por todo o protocolo.

**O que está escrito.** Arquitectura §2.2, a negrito: *"**Mutuamente exclusivo aplica-se sempre.** Sobreposição entre ramos é erro em qualquer árvore: produz dupla contagem e duplica esforço."* E logo abaixo: *"**Um eixo por nó.** [...] Iterar níveis é permitido e é como se compõem eixos."*

**O que a evidência diz.** A síntese 00b Parte II estabelece três modos, com a linha decisiva na terceira posição da tabela: os ramos de um diagnóstico **somam-se**, os de uma decisão **excluem-se**, e os de uma caracterização **cruzam-se**. Daí: *"Partes somam-se; dimensões cruzam-se. Um jardim não se reparte entre 'uso' e 'manutenção' — tem simultaneamente uma posição em cada."* E §3.4: *"Dentro de cada eixo, as posições devem cobrir o espectro relevante e não se sobrepor — aí vale ME e CE. Entre eixos, não há exaustividade nenhuma a exigir — o conjunto é aberto por desenho."* A síntese regista até, como contradição resolvida, que fontes enciclopédicas exigem ME+CE às facetas e **aplicam o critério ao nível errado**.

**Onde exactamente o protocolo erra.** A construção "um eixo por nó, eixos compõem-se por níveis" é uma maneira de simular facetas dentro de uma hierarquia. Funciona formalmente e falha em três pontos práticos, todos nomeados na evidência:

1. **Destrói a hospitalidade.** A síntese 00b §3.4 chama *hospitalidade* à capacidade de acomodar algo novo sem refazer a estrutura, e identifica-a como *"precisamente a propriedade que uma árvore MECE não tem"*. Numa composição por níveis, acrescentar um eixo a meio obriga a refazer todos os níveis abaixo. Numa estrutura facetada acrescenta-se um eixo e nada mais muda. O protocolo declara a árvore de caracterização "aberta — ramos nascem da investigação" (tabela dos quatro propósitos) e depois dá-lhe a única forma que não suporta abertura.
2. **Multiplica folhas em vez de as acrescentar.** Três eixos com quatro posições cada dão doze posições numa estrutura facetada e sessenta e quatro folhas numa composição por níveis. Como cada folha é candidata a frente (`P1.5`), este é o gerador de inchaço real — mais do que a multiplicação de árvores que T5 identifica.
3. **Impõe uma ordem de eixos que é arbitrária e determinante.** Numa composição por níveis, o eixo de nível 1 estrutura tudo o que está abaixo. A síntese 00b §3.8 estabelece que *"a estrutura da árvore não é instrumento neutro de medição — é parte da causa"* do que se encontra. Escolher qual eixo vai primeiro é uma decisão de conteúdo disfarçada de decisão de arrumação, e o protocolo não a regula.

**Correcção concreta.** Retirar a caracterização da lista de propósitos de árvore e dar-lhe estrutura própria:

- O modo de caracterização **não produz uma árvore**. Produz um conjunto aberto de **eixos**, com `ME` e `CE` **dentro** de cada eixo e nenhuma exigência entre eixos.
- A sua condição de morte (`P1.1`) é **saturação**, não verificação: parar quando novas perguntas deixam de gerar eixos novos. A síntese 00b §3.5 nota que três literaturas independentes — grounded theory, elicitação de objectivos nas National Academies, e Conklin sobre problemas perversos — convergem neste critério exacto quando abandonam a exaustividade. É a convergência mais forte de toda a investigação.
- A operação que substitui a exaustividade é a **consistência cruzada** de Zwicky/Ritchey: avaliar par a par que posições são compatíveis e ficar com o espaço coerente. Ritchey chama-lhe *"in-built garbage detection"*. O produto **não é uma solução — é um espaço de configurações consistentes**.
- **Nunca podar** no modo de caracterização (consequência directa de G1 mais §4.3 da síntese).
- **Nunca normalizar pesos.** A síntese 00b §3.2 e §4.3: no momento em que se atribuem pesos que somam 1 está-se tacitamente a declarar exaustividade; e o *splitting bias* está medido — subdividir um ramo aumenta-lhe o peso independentemente do mérito.

---

#### G3 · A exclusividade mútua está definida entre irmãos. O modo de falha canónico não é entre irmãos.

**O que está escrito.** `P1.3` — *"Ramos irmãos **não podem** sobrepor-se."*

**A evidência.** A síntese 00b, ponto 10 do sumário executivo: *"O caso canónico do método falha o próprio método. No salmão do Pacífico, Conn admite que a árvore inicial 'isn't MECE' — e a falha é de **exclusividade mútua**, não de exaustividade. Um driver que atravessa todos os ramos não tem notação possível numa árvore."* A síntese 00 desenvolve-o como o critério mais subtil e o que mais estraga árvores — **integridade do driver**: na primeira árvore, "política governamental" aparecia como ramo próprio quando na verdade atravessava todos os outros, e *"enquanto a árvore esteve assim, nenhuma análise dentro dela podia ser conclusiva"*.

`P1.3` não apanha isto. Nenhum par de irmãos se sobrepõe numa árvore com um driver transversal; o driver está correctamente dentro de um ramo e incorrectamente ausente dos outros. A violação é de outra espécie e o protocolo não a nomeia.

**O que salva o protocolo, e que ele não aproveita.** `P1.4` obriga a declarar as arestas de dependência no acto de desenhar o ramo, e o cone é percorrido transitivamente. **Uma árvore mais um conjunto de arestas transversais é exactamente um semi-reticulado** — a estrutura que Christopher Alexander exigiu em *A City is Not a Tree* (1965) depois de ter repudiado a sua própria decomposição hierárquica de 1964 (síntese 00b §3.7, que apresenta esta objecção como a mais séria e vinda "da autoridade mais óbvia"). O protocolo já construiu a resposta a Alexander e continua a falar como se não a tivesse.

**Correcção concreta.**

- **`P1.3-a`** — Antes de fixar um corte, nomear o driver mais provável e verificar se fica **inteiro num ramo**. Se atravessar mais do que um, ou o corte muda, ou o driver é declarado como **aresta transversal** ao abrigo de `P1.4`, visível a todos os ramos que atravessa. A terceira saída — ignorá-lo — é proibida.
- Reescrever `P1.4` como o que ele de facto é: **o mecanismo que converte a árvore em semi-reticulado**, e não apenas um substrato de detecção de colisões. Isto muda a forma como um agente o preenche: passa de "de que ramos dependo" para "que factos atravessam este corte".
- O detector semântico já tem esta função atribuída na arquitectura §2.4.8 — *"quando apanha um conflito que a árvore não previa, falta uma aresta"*. Acrescentar-lhe a leitura simétrica: **um driver que reaparece em vários alertas do mesmo nível é um corte errado, não uma aresta em falta.**

---

#### G4 · A triagem de `P1.5` exige uma magnitude que, nos casos em que é invocada, não se conhece.

**O que está escrito.** Arquitectura §2.2: *"Antes de recolher evidência, estimativa de ordem de grandeza e cenário extremo: se este ramo variasse dez vezes, mudava a decisão final? Se não, descarta-se o ramo sem o testar empiricamente."* `P1.5` torna-o eliminatório.

**A evidência contra, em três camadas.**

1. **Onde as magnitudes são a incógnita, a operação é inaplicável.** Síntese 00b §1.3(a), sobre o salmão do Pacífico: a abundância oscila com a Oscilação Decadal do Pacífico e é impossível separar variação natural de efeito de política. E a conclusão, que é geral: *"a poda por magnitude de impacto, que é o coração do método, torna-se inaplicável em domínios ecológicos e sociais — porque as magnitudes são exactamente o que não se sabe."* A resposta dos autores não foi analítica: **mudaram o nó-raiz**. Padrão genérico registado na síntese: *"quando os dados não permitem dimensionar os ramos, muda-se o nó-raiz."* `P1.5` não tem esta saída.
2. **A estimativa é contaminada pela forma da árvore que a produz.** Fischhoff: a importância percebida de um ramo **aumenta se ele for apresentado partido em dois sub-ramos**. Weber, Eisenführ e von Winterfeldt medem o mesmo em árvores de valor. Logo, dois ramos irmãos com granularidades diferentes não são comparáveis por estimativa, e `P1.5` compara-os.
3. **O teste único da literatura é anterior e o protocolo não o tem.** Síntese 00b §4.1: *"A decomposição ajuda quando a partição é conhecida e se conhece melhor as componentes do que o alvo. A decomposição prejudica quando a partição é ela própria a incógnita."* A síntese apresenta-o como "o melhor teste único que a literatura oferece". Note-se que resolve uma contradição real — MacGregor reporta ~42% de redução de erro por decomposição sob alta incerteza (segunda mão), e Tversky & Koehler mostram que desempacotar inflaciona a probabilidade julgada: 18% + 22% + 33% = **73%**, contra **58%** para "morte por causa natural" como um todo. A síntese acrescenta a frase que devia estar no protocolo: *"MECE não protege disto, MECE é a operação que o produz."*

**Correcção concreta.**

- **`P1.5-d`** — Se o agente não conseguir dar um intervalo de ordem de grandeza **com fundamento declarado**, o ramo **não** é podado. Fica `suspenso: por dimensionar`. Ausência de estimativa não é estimativa de zero.
- **`P1.5-e`** — Se mais de metade dos ramos irmãos ficarem `suspenso: por dimensionar`, não é a árvore que está incompleta: é o nó-raiz que está errado. Dispara reformulação da raiz, não recolha de dados.
- **`P1.0`** (novo, anterior a tudo) — Uma árvore **não pode** nascer sem que esteja escrito que se conhece melhor as partes do que o alvo. Se não se conhece, decompor só empurra a incerteza para baixo e produz, nas palavras da síntese, *"uma resposta à pergunta errada com aparência de rigor"*.
- Comparar ramos por estimativa só entre irmãos com **a mesma granularidade**, explicitamente verificada.

---

#### G5 · Nenhuma regra obriga a árvore a ter raiz escrita, decisor, horizonte e precisão.

**O que está escrito.** `P1.1` obriga cada árvore a declarar propósito e condição de morte. É tudo. A raiz aparece uma única vez, na camada do caminho, em `M1` ("enunciar o mandato como pergunta de decisão") — e o caminho é posterior às árvores em `M2`.

**A evidência.** É o achado mais insistente da síntese 00, que lhe dedica a Fase 0 inteira. O modo de falha tem nome formal — **erro de Tipo III**, de Kimball (1957): *"the error committed by giving the right answer to the wrong problem"*. Sarrazin: *"At McKinsey, we spend an enormous amount of time in writing that little statement."* O *Problem Statement Worksheet* tem oito campos, e a síntese destaca que **os campos 6–8 são precisamente os que as versões vulgarizadas do método omitem**: decisor e stakeholders (com bloqueadores), fontes-chave de insight, e horizonte temporal com grau de precisão exigido. Conn: *"What are the forces acting upon your decision maker? How quickly is the answer needed?"*

E a síntese 00b §1.3(b) mostra o que acontece à árvore sem decisor. No caso da obesidade no Reino Unido, o MGI teve de **postular** um decisor para a árvore fechar, *"e essa escolha determinou a forma da árvore, ao ponto de faltarem as intervenções de custo negativo"*. Conclusão: *"O nó-raiz de uma issue tree é sempre 'o que deve X fazer?'. Sem X, a árvore não tem orientação."*

O protocolo tem um `MANDATO` com decisor implícito (o humano responsável) e um critério de fim. Mas uma árvore não é o projecto, e uma árvore de caracterização acoplada a uma decisão pode ter um destinatário diferente do mandato. Sem raiz escrita, o critério de corte de §2.2 — assimetria e accionabilidade — fica sem referente: **assimetria em relação a quê, accionável por quem.**

**Correcção concreta.** `P1.1` passa a exigir cinco campos, não dois:

```
propósito · raiz (pergunta cuja resposta é a solução) · decisor
precisão exigida e horizonte · condição de morte
```

A raiz não pode ser um tópico. A síntese 00 dá a regra gramatical directamente: *"'How can the client minimize its tax burden?' is more useful than 'Tax.'"*

---

#### G6 · O acoplamento entre árvores tem duas saídas. A prosa do próprio documento descreve uma terceira.

**O que está escrito.** Arquitectura §2.2: *"Quando o segundo devolve resultado, o primeiro reavalia, com duas saídas apenas — aprofundar ou podar."* E, dois parágrafos abaixo, no mesmo documento: *"A evidência não decidiu — mudou o significado das opções, que é o que a torna útil."*

**A contradição é interna e é material.** "Mudar o significado das opções" não é aprofundar nem podar: é **redesenhar o eixo do nó**. A regra proíbe a operação que a prosa acabou de declarar ser a razão de ser do acoplamento.

**A evidência.** A síntese 00b §3.6 identifica esta operação como estando fora de ambas as árvores: *"o cruzamento não cabe dentro de nenhuma das duas árvores, porque é uma operação entre elas — o que é mais um indício de que a forma de árvore está a ser esticada."* E dá-lhe conteúdo: a valência não é propriedade do facto, é uma relação entre um facto e uma pessoa. O quadro de quatro caixas que daí sai — real favorece/dificulta × a pessoa quer/não quer — tem uma caixa que a síntese chama "a que interessa" (o real dificulta, a pessoa quer), e nota que **só um dos quatro quadrantes pertence ao modo diagnóstico**. Um acoplamento com duas saídas colapsa quatro estados em dois.

Corolário: também o caso mais instrutivo da síntese aponta para fora. Na sobrepesca — que o livro chama *"the quintessential wicked problem"* — os três ramos da árvore falharam todos e **a solução veio de fora da árvore**, por analogia com servidões de conservação terrestres e por Ostrom. A síntese: *"a árvore delimita o espaço de busca e, ao fazê-lo, também o fecha."* Um acoplamento cujas únicas saídas são internas à árvore não tem como registar isto.

**Correcção concreta.** Quatro saídas de acoplamento, mutuamente exclusivas, por simetria com as quatro saídas da reavaliação do caminho (§2.3):

```
aprofundar   o resultado confirma o ramo         → vira frente
podar        o resultado esvazia o ramo          → P1.6, razão registada
recortar     o resultado muda o significado      → o eixo do nó é refeito
                                                   (nova árvore, P1.7 mantém-se)
escapar      o resultado cai fora da árvore      → sobe ao caminho como
                                                   pressuposto novo, não como ramo
```

`escapar` é o que falta a todos os protocolos de árvore inventariados nas sínteses e é o que a sobrepesca exige.

---

#### G7 · "Exaustividade estrita desde o início" é uma garantia que nenhuma tradição consegue dar.

**O que está escrito.** Tabela dos quatro propósitos: árvore de problema, exaustividade *"estrita, desde o início"*, forma *"fechada"*. E: *"Numa árvore de problema é estrito desde o início — a soma das partes é o problema todo, e uma lacuna esconde a causa."*

**A evidência.** Síntese 00b, ponto 2 do sumário: *"Quase nenhuma destas tradições exige exaustividade a sério. Só duas são formalmente exaustivas — Fault Tree Analysis (a álgebra de Boole obriga) e a WBS (a 'regra dos 100%'). Nas restantes, incluindo a McKinsey, a exaustividade é presumida, nunca verificada."* E o veredicto directo: *"a CE da issue tree é do tipo 'Ishikawa' — presumida — e não do tipo 'FTA' — demonstrada."* A exaustividade real é sempre imposta por formalismo externo. A síntese 00 acrescenta que a própria árvore de lucro canónica não é MECE em sentido estrito, porque preço e quantidade estão correlacionados, e conclui que MECE é *"an ideal, not a law"*.

O custo de declarar o que não se pode honrar não é retórico. Síntese 00b §4.3: *"A sensação de completude não correlaciona com completude. Uma árvore bem desenhada sente-se rigorosa independentemente de ser verdadeira."* Uma regra que diz "estrito desde o início" produz agentes que declaram exaustividade porque a regra a exige.

**Correcção concreta.** Substituir o adjectivo por uma declaração verificável. O nó declara o **formalismo que sustenta a sua exaustividade**:

| Formalismo declarado | Exaustividade | Consequência |
|---|---|---|
| algébrico (a fórmula devolve a métrica) | demonstrada | sem residual |
| booleano (portas AND/OR, minimal cut sets) | demonstrada | sem residual |
| regra dos 100% (âmbito de trabalho) | demonstrada | sem residual |
| lógico `A / não-A` | demonstrada | sem residual |
| nenhum — categorias presumidas | **presumida** | residual nomeado obrigatório (`P1.5-b`) |

A última linha é o caso normal e deve ser declarada como tal. Note-se a correcção que a síntese 00 faz ao folclore: o corte binário só é MECE por definição na forma *A / não-A*; "oferta vs. procura" é dicotomia substantiva, não lógica.

---

#### G8 · "Árvores concorrentes" é a regra mais importante do arranque e é a única que não tem identificador.

**O que está escrito.** Arquitectura §2.2: *"No arranque desenham-se árvores concorrentes com eixos conceptuais distintos sobre o mesmo problema. [...] Uma árvore só é o mesmo erro que um caminho só: não é escolha, é inércia."* R3 §7.4 repete-o. A garantia de §3.1 lista a falha detectável — "árvore única, ou ramos sobrepostos". **E `P1.1`–`P1.7` não contêm nenhuma regra que o imponha.** Em contraste, `P2.1` impõe explicitamente dois ou mais caminhos.

Isto é tanto mais notável quanto R3 §1 declara, como operação 2 da génese, "atribuição de identificador a toda a norma que existia em prosa". A norma mais consequente de §2.2 ficou em prosa.

**A evidência de que a norma é correcta.** É o ponto central da síntese 00, Fase 2. Conn: *"I love to do two or three different cuts at it"*. O livro dá-a como regra anti-enviesamento — *"Always try multiple trees / cleaves"*. E o caso da asma em Western Sydney prova-o: pelo corte da **incidência** não aparecia nada (~10% acima do resto da cidade); pelo corte da **severidade** o problema abriu-se — mortes e hospitalizações 54–65% superiores, correlacionadas com metade da cobertura arbórea e PM2,5 50% mais alto. A intervenção que daí saiu — plantar árvores — era **literalmente invisível** no primeiro corte. A síntese: *"Não foi a análise que produziu o insight. Foi a escolha do corte."*

Um detalhe que o protocolo devia absorver: a síntese 00b §1.2 nota que o corte vencedor foi escolhido **por familiaridade** — McLean já o usara em relatórios de acidentes noutros conselhos. O acerto foi acidental. Isso reforça a regra em vez de a enfraquecer: precisamente porque a origem do bom corte é arbitrária, é preciso gerar vários.

**Correcção concreta.** `P1.8` — No arranque de uma árvore de problema ou de decisão, **devem** existir duas ou mais árvores com eixos conceptuais distintos antes de qualquer ramo passar a trabalho. Uma árvore única só é admissível com registo em `REJEICOES` da alternativa que não se desenhou e porquê.

E acrescentar a regra prática que a síntese 00b §1.5 destaca como valendo mais do que qualquer teoria: **escolher um corte e validá-lo com cálculos de guardanapo *antes* de construir a árvore.**

---

#### G9 · A árvore de mandato é o caso mais perigoso e é o único sem disciplina própria.

**O que está escrito.** Arquitectura §2.1: *"Se o humano não conseguir enunciar o que quer, o mandato não se força: desenha-se uma árvore de mandato (§2.2) e o mandato sai dela."* Na tabela dos quatro propósitos: pergunta *"o que é que eu quero, afinal"*, exaustividade *"emergente"*, forma *"morre ao produzir o mandato"*. Mais nada.

**Porque é o caso mais perigoso.** É elicitação de preferências, e é o terreno onde a evidência é mais desfavorável à decomposição.

- **Wilson & Schooler, *Thinking Too Much* (1991)** — usado em paráfrase pela síntese, não no original: quem analisou as razões da sua preferência concordou **menos** com os peritos do que os controlos, tanto por análise de razões como por avaliação exaustiva de atributos, com redução medida da satisfação pós-escolha. Mecanismo: analisar razões desloca a atenção para critérios **verbalizáveis mas não-óptimos**, e avaliar muitos atributos *modera* as avaliações, fazendo as opções parecerem mais equivalentes do que são. A síntese traduz: *"uma árvore de gosto torna as opções mais parecidas entre si e privilegia o que se consegue dizer por palavras."*
- **Preferências construídas** (Slovic; Payne, Bettman & Johnson — Slovic 1995 não foi lido no original, é a lacuna que a síntese declara maior nesta parte): as pessoas frequentemente não têm preferências estáveis à espera de serem lidas; constroem-nas durante a elicitação. As inversões de preferência são a prova dura.
- **Consequência que o protocolo inverte.** Síntese 00b §3.8: *"Uma árvore que se altera a meio da conversa não está avariada — está a funcionar. A alternativa, uma árvore que não se mexe, é mais provavelmente sinal de ancoragem na primeira estrutura proposta do que de estabilidade genuína."* O protocolo trata a mudança como carga (reavaliação, emenda, registo) em todos os níveis. Aqui, mudança é o produto.

**E falta um teste formal que é barato.** O **teste WITI** de Keeney (síntese 00b §3.5, regra 6): perguntar a cada nó "porque é que isto é importante?". Se a resposta remeter para outro objectivo, o nó é um **meio**, não um fim — e meios alimentam vários fins, logo a estrutura é **rede, não árvore**. Sem este teste, uma árvore de mandato mistura fins e meios e produz um mandato cujos objectivos não são independentes, o que quebra `P0.1` e `P0.2` a montante.

**Correcção concreta.** Cartão próprio para o propósito mandato, com cinco regras: raiz curta; **ancorar em exemplos concretos, não em categorias abstractas** (é a recomendação directa da síntese 00b §4.4); teste WITI a cada nó, com saída para rede; **proibição absoluta de poda e de pesos**; condição de morte por **saturação e discriminação** (parar quando novas perguntas não geram eixos novos e a estrutura já distingue as opções em cima da mesa), não por "produzir o mandato" — que não é verificável.

---

#### G10 · A regra de saída resolve o destino do documento. Não resolve o destino da árvore.

**O que está escrito.** Arquitectura §2.4.9: *"A árvore é lógica de partição do problema; esta é lógica de comunicação do resultado. Confundi-las produz documentos que expõem a análise em vez de a concluir."*

**Isto está certo e é bem visto.** Corresponde exactamente à Fase 8 da síntese 00: o Staff Paper reconhece que a pirâmide *"can be laid out as a tree – just as with issue and hypothesis trees"*, **mas** *"the best problem solvers capture it by creating dot-dash storylines"*, com lógica horizontal SCR. A síntese resume: *"A árvore é o andaime. O deck é o edifício. O andaime sai."* A arquitectura tem a distinção e tem o verificador mecânico (cold-read). É melhor do que a maioria das formulações.

**O que falta.** A síntese 00 Fase 8 descreve dois destinos para a árvore, e o segundo é o que o protocolo devia querer: do lado da firma, a árvore *"morre como entregável e renasce como template"*, alimentando o primeiro rascunho do projecto seguinte — *"a first draft may already exist"*. E a síntese regista a tensão sem a resolver: **o mesmo mecanismo que garante exaustividade é o que produz ancoragem institucional**, e o Staff Paper recomenda o primeiro e avisa contra a segunda *"sem notar que são a mesma coisa"*.

O protocolo, com árvores mortas guardadas, slugs mortos e `REJEICOES`, constrói uma biblioteca. Não declara o que faz com ela, nem o risco. R3 §7.5 — *"uma árvore madura é maioritariamente morta [...] o valor concentra-se nos mortos"* — é uma formulação que nenhuma das duas sínteses tem e que me parece certa, mas é precisamente a condição de ancoragem máxima.

**Correcção concreta.** Declarar o arquivo como o que é — acelerador e âncora — e dar-lhe uma regra: uma árvore arquivada **pode** ser consultada depois de os cortes alternativos estarem desenhados (`P1.8`), nunca antes. E acrescentar à listagem da auditoria de §3.2 o sinal correspondente: cortes que se repetem entre projectos sem que nenhum tenha sido gerado de novo.

---

### 3 · O que está certo, e é melhor do que a prática documentada

A crítica acima não se sustenta se esta secção não for genuína. Seis pontos, e três deles não existem em nenhuma das tradições inventariadas nas sínteses.

**A1 · Condição de morte declarada ao nascer (`P1.1`). Não existe em lado nenhum, e ataca um modo de falha medido.** A síntese 00 Fase 8 documenta o destino real da árvore do lado do cliente: *"becomes a static artefact. It is not updated"*, com o diagnóstico estrutural — *"The value of the driver tree was always in the ongoing use, not the initial construction. But the delivery model optimised for the construction."* A síntese 00b §1.3 dá-lhe o nome que a literatura do logframe usa: ***lock-frame***, estrutura congelada que impede aprendizagem, ao lado de *lack-frame* e *box-filling*. Todas as tradições descrevem a patologia; nenhuma prescreve o antídoto. `P1.1` prescreve-o, e a formulação da arquitectura — *"uma árvore eterna transforma-se na lista de tarefas que geram tarefas — com melhor genealogia, o que a torna mais difícil de matar"* — é uma observação que eu não encontro em nenhuma das sínteses e que é exacta.

**A2 · Razão de poda registada (`P1.6`), com slug morto a bloquear a recriação. Preenche uma lacuna que a síntese regista explicitamente como vazia.** Síntese 00 Fase 5: *"**Não encontrado:** qualquer prática de guardar a árvore original para auditoria. Nada no Staff Paper, nada nos relatos. A descrição dominante é de reescrita contínua sem versionamento."* O protocolo é, neste ponto, mais rigoroso do que a sua fonte de referência. O quarto nível de protecção — slug morto que impede ressurreição silenciosa — é a resposta ao *premature closure* clínico que a síntese 00b cita (*"When the diagnosis is made, the thinking stops"*) aplicada ao inverso: impede que o que foi fechado volte sem decisão.

**A3 · `P1.7` — árvores de propósito diferente não podem ser fundidas — é a regra mais bem fundamentada do conjunto.** Coincide com Chevallier, que a síntese 00 apresenta como *"a codificação académica mais próxima de um padrão"*: árvores de diagnóstico vs. de solução, com interdição explícita de as misturar — *"You can't mix 'why' and 'how' questions in one same tree"*. E o protocolo vai mais longe do que a fonte em dois aspectos: dá a **razão mecânica** (*"Fundidas, a decisão nunca fecha, porque há sempre mais para caracterizar"*), e torna a interdição **executável** em vez de conselho. A síntese 00b diz que a ausência desta tipologia *"explica a maior parte dos maus usos que se vêem"*. O protocolo tem-na.

**A4 · `P1.4` — arestas declaradas no acto de desenhar o ramo, percorridas por travessia. É a contribuição genuinamente nova.** Nenhuma das onze tradições da tabela de 00b §1.1 tem isto. Resolve, por via lateral, o problema que a síntese declara insolúvel dentro de uma árvore: *"Um driver que atravessa todos os ramos não tem notação possível numa árvore."* O protocolo dá-lhe notação — fora da árvore, como aresta. E a tensão T1 identifica correctamente a condição de que tudo depende (se declarar não for barato no momento do nascimento, as arestas ficam vazias e o detector cala-se, *"pior do que não existir, porque parece estar a vigiar"*), com um sinal de verificação gratuito. Isto é melhor engenharia do que qualquer coisa nas sínteses.

**A5 · A separação entre teste gratuito e teste caro é mais limpa do que a matriz de referência.** A arquitectura §2.3: *"a árvore gera os cortes, o caminho testa-os [...] Juntar os dois testes faz desaparecer a triagem e transforma todos os cortes em frentes."* A prática documentada na síntese 00 Fase 4 usa uma matriz 2×2 (importância × capacidade de mover) e reconhece abertamente que ela não serve para descobrir prioridades mas para *"forçar o cliente a escolher em frente aos pares"* — *"all the Post-it notes start off in the top right-hand corner"*. O protocolo substitui um ritual social por dois testes com custos declarados e momentos distintos. Mantém, correctamente, o critério de accionabilidade, que é o que elimina o caso das **condições oceânicas** no salmão: a maior alavanca de todas, e completamente imóvel.

**A6 · R3 §7.6 — o quadro percorrido em vez de segurado — é uma reformulação correcta do problema.** A síntese 00 Fase 3 diz que não há algoritmo para verificar exaustividade, e que os dois mecanismos reais são disciplina de camada e memória institucional — *"na McKinsey, o perito é o arquivo"*. O protocolo substitui o perito humano por travessia de arestas, o que é a única forma de a propriedade não depender de quem estava presente. E a formulação de R3 §7.5 — a árvore como **registo do que se deixou de fazer, com uma franja viva na periferia** — é, tanto quanto vejo, original e correcta. É também, note-se, a razão pela qual G1 importa tanto: se o valor está nos mortos, a invisibilidade dos mortos é a falha cara.

---

### 4 · Resumo das correcções propostas

| # | Alvo | Correcção | Gravidade |
|---|---|---|---|
| G1 | `P1.5`, `P1.6` | poda visível vs. invisível; residual nomeado; aresta sobrevive à poda | **alta** |
| G2 | §2.2 "ME aplica-se sempre" | caracterização sai da família árvore: eixos abertos, ME/CE dentro do eixo, saturação, consistência cruzada, sem poda, sem pesos | **alta** |
| G3 | `P1.3` | integridade do driver; `P1.4` reconhecido como conversão em semi-reticulado | **alta** |
| G4 | `P1.5` | `suspenso: por dimensionar`; reformulação da raiz; `P1.0` partes-vs-alvo; granularidade comparável | **alta** |
| G5 | `P1.1` | raiz escrita, decisor, precisão e horizonte | alta |
| G6 | acoplamento | quatro saídas: aprofundar · podar · recortar · escapar | alta |
| G7 | tabela dos propósitos | formalismo de exaustividade declarado, em vez de "estrita" | média |
| G8 | `P1.x` | `P1.8` — duas ou mais árvores concorrentes, com identificador | média |
| G9 | propósito mandato | cartão próprio: exemplos concretos, teste WITI, sem poda nem pesos, saturação | média |
| G10 | §2.4.9 / §3.2 | arquivo declarado como acelerador e âncora; consulta só após `P1.8` | baixa |
| §1 | identificadores | desambiguar `P0.x`/`P1.x`/`P2.x` entre os dois documentos; definir `cone`; resolver frente-única e T5 | **bloqueante** |

---

## 4 · Fontes

*Sem secção de fontes no relatório original.*
