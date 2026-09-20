---
title: "Criticas a definicao de arvore no protocolo"
date: 2026-09-20
type: audit
case: protocolo
tags: [MECE, arvore, audit]
sobre:
  - "[[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]]"
  - "[[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]]"
---

# Criticas a definicao de arvore no protocolo

## 0 · Sumário executivo

- **Dez críticas de precisão, não de concepção.** A concepção aguenta; seis elementos do protocolo são melhores do que qualquer prática documentada na literatura.
- **C1 — ME e CE estão fixados ao nível errado.** Não variam com o propósito, variam com o nível. Consequência: uma árvore de caracterização bem construída será sinalizada como defeituosa pelo auditor.
- **C2 — não há notação para o factor transversal**, e é a falha que o detector não apanha. O sistema classificará uma falha estrutural como falha declarativa.
- **C3 — a poda está registada onde o enviesamento não opera.** Protege contra reabertura, não contra o encolhimento silencioso do âmbito.
- **C4 — a triagem está aplicada a árvores onde a decisão ainda não existe.**
- **C8 — a árvore de caracterização não tem condição de morte escrevível**, e a condição de morte é o travão único declarado do sistema.
- **Correcção estrutural:** duas das correcções **retiram** regras em vez de acrescentar; três acrescentam objectos pequenos; nenhuma toca na arquitectura.
- **Aviso de âmbito:** o articulado normativo não está na pasta.

---

## 1 · Mandato

Abrir a pasta `naoabrirsemordem`, ler cada documento para perceber o contexto em que a árvore é ferramenta, e produzir dois relatórios. Este é o primeiro:

**Críticas à forma como os agentes definiram a árvore** nos dois documentos — §2.2 de `arquitectura-governo.md` (quatro propósitos, MECE, critério de corte, triagem, estados de ramo, protocolo `P1.1`–`P1.7`) e §7 de `R3-genese-mandato-global-arvore.md` (o que é, o que não é, como se desenvolve, três tempos).

O segundo relatório — definição e instruções de uso — está em documento próprio.

---

## 2 · Método

**Confronto de cada regra contra a base de evidência** das duas sínteses. Para cada crítica: a regra ou frase citada, o que está errado ou em falta, a evidência, e a correcção concreta.

**Justiça como critério de credibilidade.** O relatório abre pelo que está certo e é melhor do que a prática documentada — seis elementos que não existem em nenhuma tradição investigada. Uma crítica que não reconhece o mérito do objecto não é usável por quem o escreveu.

**Ordenação por gravidade**, com tabela final que declara o custo de corrigir e a consequência de não corrigir.

**Verificação de identificadores** entre os dois documentos, que revelou o desencontro registado no aviso de âmbito.

**Limite assumido:** critica-se a definição tal como está nestes dois documentos. Onde o articulado ausente já resolva algum ponto, a crítica cai.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

**Alvo:** `naoabrirsemordem/arquitectura-governo.md` §2.2 e `naoabrirsemordem/R3-genese-mandato-global-arvore.md` §7
**Base:** as seis investigações em `01`–`06` e as sínteses `00` e `00b`
Data: 20 de Setembro de 2026

---

### Aviso de âmbito

**O protocolo normativo não está na pasta.** O `R3` cita `P0.10`, `P0.14`–`P0.21`, `P1.9`, `P1.11`–`P1.13`, `P2.8`, `P2.11`–`P2.18`, `P4`–`P10` e `C.4`. O `arquitectura-governo.md` contém apenas `P0.1`–`P0.8`, `P1.1`–`P1.7` e `P2.1`–`P2.6`. Existe um terceiro documento — o articulado — que não foi lido.

Há ainda um desencontro de identificadores entre os dois documentos presentes: o `R3` §3 mapeia *"tecto numérico de árvores e de frentes"* para `P0.5` e `P0.6`, mas em `arquitectura-governo.md` essas duas regras são sobre **quem redige o mandato**. Uma das duas numerações está errada, e como o tecto de árvores é o travão único declarado em `T5`, vale a pena resolver.

Tudo o que se segue critica a definição **tal como está nestes dois documentos**. Onde o articulado já resolva algum destes pontos, a crítica cai.

---

### O que está certo, e é melhor do que a prática documentada

Isto precisa de ser dito primeiro, porque dá medida ao resto. Seis coisas neste protocolo **não existem na literatura** que investiguei, e resolvem problemas que ela deixa em aberto:

| Elemento do protocolo | Problema que resolve |
|---|---|
| **Condição de morte declarada ao nascer** (`P1.1`) | Rittel: os problemas perversos *"do not have a stopping rule"*. Nenhuma fonte lida propõe declarar a paragem no acto de abertura. É uma resposta original. |
| **Razão de poda registada** (`P1.6`) | A literatura regista que becos reabrem; nenhuma fonte prescreve o registo como obrigação. |
| **Proibição de fundir árvores de propósito diferente** (`P1.7`) | Chevallier proíbe misturar "porquê" e "como" **dentro** de uma árvore; ninguém proíbe a fusão **entre** árvores. A justificação dada — a decisão nunca fecha porque há sempre mais para caracterizar — é exacta. |
| **Dependências declaradas no acto de desenhar o ramo** (`P1.4`) | Ataca no sítio certo o custo de declaração que o `T1` identifica. |
| **Duas existências: mecânica completa, projecção sem razões** | Reinvenção independente de uma decisão de desenho que a McKinsey toma por outros motivos. Aqui é melhor fundamentada: retira o material com que se reabriria um ramo. |
| **"Uma árvore madura é maioritariamente morta"** | Correcto e raramente enunciado. O valor concentra-se nos ramos mortos. |

As dez críticas abaixo são de **precisão**, não de concepção. A concepção aguenta.

---

# As críticas

### C1 · ME e CE estão fixados ao nível errado

**O que o documento diz.** *"Mutuamente exclusivo aplica-se sempre"* — sobreposição é erro em qualquer árvore. E `P1.3`: *"Ramos irmãos não podem sobrepor-se."* A exaustividade é que varia com o propósito.

**O problema.** ME e CE **não variam com o propósito. Variam com o nível.** Dentro de um eixo, aplicam-se ambos — as posições de um eixo devem cobrir o seu espectro e não se sobrepor. **Entre eixos, não se aplica nenhum dos dois** — eixos não se excluem, cruzam-se.

A árvore de caracterização, tal como o documento a descreve — forma **aberta**, *"ramos nascem da investigação"* — é uma estrutura de facetas. E numa estrutura de facetas, perguntar se os ramos de topo são mutuamente exclusivos não tem resposta: "solo" e "luz" não se sobrepõem nem deixam de se sobrepor, porque um jardim tem simultaneamente uma posição em cada.

**Porque é que isto morde neste sistema em particular.** `P1.3` não é decorativa — é uma das falhas que o auditor procura (§3.1: *"árvore única, ou ramos sobrepostos"*). Ou seja: **uma árvore de caracterização bem construída será sinalizada como defeituosa**, e a correcção que o agente fará é a errada — fundir facetas que deviam ficar separadas, ou inventar exclusividade onde não é devida.

**Correcção proposta.**

> ME e CE aplicam-se **dentro de um eixo**, em qualquer propósito.
> Entre eixos, não se aplica nenhum dos dois.
> `P1.3` passa a: *ramos irmãos sob o mesmo eixo não podem sobrepor-se.*

Com esta redacção, `P1.3` deixa de ser uma regra separada e passa a ser o corolário de `P1.2` (um eixo por nó) — o que é bom sinal: reduz o corpo de regras em vez de o aumentar, que é o critério do próprio protocolo.

---

### C2 · A árvore não tem notação para o factor transversal — e é isso que falha primeiro

**O que o documento diz.** As arestas são o mecanismo de detecção; a passagem de dependência é *"a mais valiosa e a mais barata"*; e quando o detector semântico apanha algo que a árvore não previa, *"falta uma aresta"*.

**O problema.** Nem tudo o que escapa é uma aresta em falta. O modo de falha mais comum de uma árvore real é o **factor que atravessa todos os ramos** — não vive em nenhum, condiciona todos. No caso canónico do método de que este protocolo deriva, a política pública aparecia como ramo próprio quando na verdade condicionava todos os outros, e os autores admitem que a árvore *"isn't MECE"*. Nota-se bem: **a falha foi de exclusividade mútua, não de exaustividade** — exactamente o eixo que o protocolo declarou invariante em C1.

Um factor transversal não tem representação possível numa árvore:

- pô-lo num ramo → destrói a exaustividade dos outros;
- duplicá-lo em todos → destrói a exclusividade mútua;
- ligá-lo por arestas a todos → satura o detector, e a passagem que o protocolo chama "facto" passa a ruído.

**Consequência.** O sistema classificará uma falha **estrutural** como falha **declarativa**. E a instrução que daí sai — "declarar mais arestas" — não a corrige. Isto realiza `T2` por um caminho que `T2` não prevê: o conflito caro não é o que não se viu, é o que não é representável.

**Correcção proposta.** Um objecto novo, ao nível da árvore e não da aresta:

> **`transversal`** — factor declarado ao nível da árvore, com slug, que condiciona todos os ramos.
> Não é ramo e não é aresta. Quando muda de estado, o cone afectado é **a árvore inteira**.
> Regra de higiene: se um factor transversal for descoberto **depois** de a árvore estar desenhada, a árvore é redesenhada, não remendada.

É barato, usa a maquinaria de slugs que já existe, e dá ao detector semântico uma segunda saída além de "falta uma aresta".

---

### C3 · A poda está registada exactamente onde o enviesamento não opera

**O que o documento diz.** `P1.6` obriga a registar a razão da poda. E `R3` §7.1 diz que a projecção epistémica tem *"nós, estados e arestas, sem razões"*, porque a omissão *"retira o material com que se reabriria um ramo fechado"*.

**O desenho está certo quanto ao objectivo que declara.** Protege contra a reabertura. Mas há um segundo efeito da poda que nenhum mecanismo do protocolo cobre, e está medido.

**A evidência.** Fischhoff, Slovic e Lichtenstein deram a sujeitos árvores de falhas com ramos inteiros removidos **sem aviso**. A categoria residual devia ter absorvido os ramos removidos — subir de `.078` para `.468`, um factor de seis. Subiu para `.140`. **Acertou 1 em 55.** O efeito manteve-se com mecânicos de automóveis experientes, e a auto-avaliação de perícia não previa melhor desempenho.

**Porque é que este protocolo é mais exposto do que a média.** Um agente *"não vê nenhuma das duas [existências]. Vê o seu próprio ramo e as fronteiras negativas dos ramos vizinhos."* Ou seja, vê **menos** do que os sujeitos da experiência — que pelo menos viam a árvore podada inteira. O protocolo protege o ramo morto contra ressurreição e não protege o âmbito contra encolhimento silencioso.

**Correcção proposta.** Preserva integralmente a intenção de desenho:

> A projecção mostra a **massa podada**: quantos ramos irmãos foram podados e **sob que eixo**.
> Nunca a razão, nunca o conteúdo, nunca a alternativa.

O agente recebe "sob o eixo *X* havia 4 ramos, 3 estão podados" — material para saber que o espaço é maior do que o que vê, e nenhum material para formar opinião sobre o que lá estava. É a mesma lógica de `P6.10`/`P6.11` (devolver o identificador, nunca a razão), aplicada à poda em vez da decisão.

E uma linha nova na tabela de garantias §3.1, porque não existe:

| Garantia | Como se obtém | Como se detecta a falha |
|---|---|---|
| **O âmbito não encolhe em silêncio** | massa podada visível na projecção | ramo reaberto por "não sabia que existia", e não por discordar |

---

### C4 · A triagem está aplicada a árvores onde a pergunta que ela faz ainda não existe

**O que o documento diz.** `P1.5`: nenhum ramo passa a trabalho sem triagem de ordem de grandeza. O teste: *"se este ramo variasse dez vezes, mudava a decisão final?"* E a triagem é descrita como *"gratuita"* e *"a única operação que impede a árvore de gerar frentes em excesso"*.

**O problema.** O teste pressupõe **uma decisão final já conhecida**. Isso é verdade numa árvore de problema e numa de decisão. Não é verdade nas outras duas:

- **Árvore de mandato** — a decisão final é precisamente o que está a ser descoberto. Aplicar-lhe o teste dos dez é erro de categoria: poda-se o que o humano ainda não aprendeu a querer.
- **Árvore de caracterização** — o documento diz que a exaustividade é *"verificada no fim"*. Se a verificação é no fim, a decisão contra a qual se triaria ainda não está formada no início.

**E há um segundo problema, mais fino.** O teste dos dez mede **impacto na decisão**. Não tem canal para o caso em que um ramo é tecnicamente irrelevante e é aquele que interessa ao humano. Um sítio com sombra densa e solo pobre é um ramo de baixo impacto por qualquer métrica agronómica, e pode ser o único sítio que a pessoa quer usar. A valência não é propriedade do ramo — é uma relação entre o ramo e quem decide. Com `P1.5` como está, esse ramo é podado por um agente, de graça, e com razão registada.

**Correcção proposta.**

| Propósito | Regra de triagem |
|---|---|
| Problema, Decisão | `P1.5` como está — teste dos dez |
| Caracterização | substituir por: *este eixo discrimina entre as opções ainda vivas?* Se não discrimina, não se poda — **suspende-se** |
| Mandato | **sem triagem.** É generativa. A disciplina é saturação, não poda |

---

### C5 · "Assimetria" é apresentada como filtro pré-dados e não pode sê-lo

**O que o documento diz.** Dois filtros, *"ambos aplicáveis antes de haver dados"*. E o exemplo: *"Se a produtividade caiu 10% em todo o lado, cortar por geografia não serve. Serve se revelar que uma região caiu 40%."*

**O problema.** O exemplo é **posterior ao corte**. Só se sabe que uma região caiu 40% depois de cortar por geografia e olhar. Como está redigido, o filtro pede ao agente que saiba o resultado antes de fazer a operação que o produz. Um agente cumpridor congela; um agente pragmático inventa a assimetria e segue.

**Correcção proposta.** Não é mudar o filtro — é reconhecer que já existe o teste dele:

> **Assimetria esperada** é uma *hipótese sobre o corte*, formulada antes dos dados.
> **A triagem de ordem de grandeza é o teste barato dessa hipótese.**
> **Assimetria verificada** é o resultado.

Isto arruma a sequência correctamente e explica melhor porque é que a triagem é gratuita: ela não testa o ramo, testa **o corte**. E é a mesma regra que o método de origem exprime como validar o corte com contas de guardanapo antes de construir a árvore.

---

### C6 · Falta o critério de escolha entre árvores concorrentes que mais importa a este sistema

**O que o documento diz.** Árvores concorrentes são obrigatórias — *"uma árvore só é o mesmo erro que um caminho só: não é escolha, é inércia"* — e *"vivem em simultâneo até a triagem preliminar matar as estéreis"*.

**O problema.** "Estéril" não está definido. Os dois critérios fornecidos — assimetria e accionabilidade — aplicam-se a **cortes**, não a **árvores inteiras**. Falta o critério que decide entre duas árvores igualmente assimétricas e accionáveis.

**E falta precisamente aquele de que este sistema depende mais do que qualquer outro:**

> **Integridade do driver** — prefere-se o corte que mantém o driver provável **inteiro dentro de um ramo**, em vez de o repartir por vários.

**Porquê aqui mais do que em qualquer outro sítio.** Toda a camada de detecção deste protocolo é travessia de arestas entre ramos. Um driver repartido por três ramos produz uma árvore cujas arestas **não conseguem exprimir o acoplamento real**. O detector não falha com ruído — falha com silêncio. É o pior modo de falha possível para um sistema cujo caso normal é *"o ficheiro de alertas vazio"*: fica indistinguível do funcionamento correcto.

**Correcção proposta.** Acrescentar aos critérios de corte, e usá-lo como desempate entre árvores concorrentes. Sinal verificável pelo auditor: um ramo com arestas para todos os irmãos é quase sempre um driver mal alojado — ou um transversal por declarar (C2).

---

### C7 · Não há regra de consistência de pergunta

**O que falta.** `P1.2` governa o eixo por nó. Nada governa o **tipo de pergunta** ao longo de um caminho da raiz à folha.

**O problema.** Uma árvore que nasce em *"porque é que isto falha"* e ao terceiro nível passa a ramificar em *"como corrigimos"* tornou-se duas árvores dentro de uma. Isto viola `P1.7` — proibição de fundir árvores de propósito diferente — mas viola-a de um modo que **nenhuma regra actual detecta**, porque a fusão não aconteceu entre dois ficheiros, aconteceu dentro de um.

**Correcção proposta.** Uma linha:

> Uma árvore mantém o mesmo tipo de pergunta da raiz à folha. Não se misturam "porquê" e "como".

Torna `P1.7` verificável por inspecção de um único ficheiro, em vez de depender de alguém notar que duas árvores foram fundidas.

---

### C8 · A árvore de caracterização não tem condição de morte escrevível — e é o travão único

**O que o documento diz.** `P1.1` exige condição de morte ao nascer. E `T5` declara que a multiplicação de árvores é *"o ponto onde o sistema pode crescer sem limite"*, com `P1.1` como ***travão único***.

**O problema.** Para três dos quatro propósitos a condição de morte é fácil de escrever (causa encontrada; opção escolhida; mandato produzido). Para a árvore de caracterização — aberta, ramos a nascer da investigação, exaustividade verificada só no fim — **não há condição de morte honestamente escrevível ao nascer**, porque ela é função de um espaço que ainda não se conhece. Na prática escrever-se-á uma data, que não é condição de morte, é prazo.

Ou seja: o travão único do sistema é mais fraco exactamente no propósito que mais cresce.

**Correcção proposta.** A condição existe e tem três literaturas independentes a convergir nela:

> **Saturação.** A árvore de caracterização morre quando dois ciclos consecutivos de investigação não produzem **nenhum eixo novo** — apenas posições novas em eixos existentes.

É escrevível ao nascer, é verificável pelo auditor a partir do histórico de ramos, e não depende de conhecer o espaço total. É o critério de saturação teórica da investigação qualitativa, é o critério que as National Academies propõem para elicitação de objectivos admitindo que *"there are no exact rules"*, e é o análogo do critério de coerência de Conklin. Três origens sem contacto entre si, mesmo resultado.

---

### C9 · A quarta árvore é a terceira com outro nome

**O que o documento diz.**

| Propósito | Pergunta |
|---|---|
| Decisão | *o que é que eu quero* |
| Mandato | *o que é que eu quero, afinal* |

**O problema.** São a mesma pergunta. "Afinal" não é uma diferença de propósito — é ênfase. Um agente que tenha de escolher entre as duas não tem critério.

**A diferença real não está na pergunta — está no estatuto do espaço de opções:**

| | Decisão | Mandato |
|---|---|---|
| As opções | **existem** e estão sobre a mesa | **não existem ainda** |
| A operação | seleccionar | **gerar** |
| Triagem | sim | **não** (C4) |
| Morte | opção escolhida | mandato produzido |
| Profundidade desigual | é alocação de esforço | é enviesamento — nesta fase todos os ramos valem o mesmo |

Escrita assim, a distinção fica utilizável e as regras diferentes deixam de parecer arbitrárias.

**Nota conexa.** Não existe árvore de **solução** ("como fazemos isto"). Pela arquitectura, o "como" é do **caminho**, não da árvore — e isso está certo. Mas não está escrito em lado nenhum, e é o erro que um agente cometerá naturalmente. Vale uma linha explícita: *o "como" vive no caminho; uma árvore de "como" é sinal de que o caminho não foi escrito.*

---

### C10 · Duas inconsistências entre os documentos

**(a) A árvore precede ou deriva?** `R3` §7.2: *"a árvore precede o que existe e determina o que virá a existir"*, como argumento para dizer que não é um índice. Mas §2.2 descreve a árvore de caracterização como aberta, com *"ramos [que] nascem da investigação"* — isto é, derivada do que existe. Para esse propósito, a frase do `R3` é falsa. A formulação correcta é mais estreita: *as árvores de problema, decisão e mandato precedem; a de caracterização acompanha.*

**(b) A hierarquia de importância é afirmada sem critério.** `R3` §7.2 diz que a decomposição do entregável é uma árvore de caracterização — *"uma das quatro, e não a mais importante"*. Não há critério que sustente o ranking, e num projecto cujo L1 é dominado por terreno desconhecido, a caracterização é a que desbloqueia as outras: é ela que dá significado às opções antes de a decisão poder fechar — o que o próprio §2.2 diz, no caso típico do acoplamento. Sugiro retirar o ranking em vez de o justificar. Os propósitos não competem; encadeiam-se.

**(c) Numeração.** Ver o aviso de âmbito. `R3` §3 atribui o tecto numérico a `P0.5`/`P0.6`, que em `arquitectura-governo.md` são outra coisa.

---

### Síntese: o que muda, por ordem de urgência

| # | Crítica | Custo de corrigir | Consequência de não corrigir |
|---|---|---|---|
| **C1** | ME/CE ao nível errado | uma linha; **reduz** o corpo de regras | o auditor sinaliza como defeito toda a árvore de caracterização correcta |
| **C2** | sem notação para factor transversal | objecto novo, usa slugs existentes | o detector falha **em silêncio**, indistinguível de funcionar |
| **C4** | triagem aplicada onde não há decisão | tabela por propósito | poda-se o que o humano ainda não aprendeu a querer |
| **C8** | caracterização sem condição de morte | uma definição | o travão único é mais fraco onde mais cresce |
| **C3** | massa podada invisível | um campo na projecção | âmbito encolhe em silêncio; efeito medido, factor de seis |
| **C6** | falta integridade do driver | um critério | árvores cujas arestas não exprimem o acoplamento real |
| **C9** | mandato ≡ decisão | reescrever duas linhas da tabela | agentes sem critério para escolher o propósito |
| **C7** | sem consistência de pergunta | uma linha | `P1.7` inverificável dentro de um ficheiro |
| **C5** | assimetria como filtro pré-dados | reordenar a sequência | instrução impossível: congela ou finge |
| **C10** | inconsistências entre documentos | edição | numeração não resolve |

As correcções `C1` e `C7` **retiram** regras em vez de acrescentar. `C2`, `C3` e `C8` acrescentam três objectos pequenos. Nenhuma toca na arquitectura.

O resultado prático está em [`2026-09-20-sintese-protocolo-arvore-definicao-e-uso.md`](2026-09-20-sintese-protocolo-arvore-definicao-e-uso.md), já escrito no formato de roteamento, para ser lido por agentes dentro do protocolo.

---

## 4 · Fontes

*Sem secção de fontes no relatório original.*
