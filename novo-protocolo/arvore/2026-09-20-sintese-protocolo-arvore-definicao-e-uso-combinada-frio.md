---
title: Árvore — definição e uso (versão combinada)
date: 2026-09-20
type: sintese
case: protocolo
tags: [MECE, arvore, protocolo]
sobre: ["[[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-frio]]", "[[2026-09-20-sintese-protocolo-arvore-definicao-e-uso]]", "[[2026-09-20-audit-protocolo-criticas-definicao-de-arvore-frio]]"]
---

# Árvore — definição e uso (versão combinada)

## 0 · Sumário executivo

Duas versões independentes do documento operacional da árvore foram produzidas sobre o mesmo mandato. Esta é a versão combinada.

A estrutura resultante tem **três portas em série**: um filtro de admissão que recusa os casos em que nenhuma árvore serve; um roteamento de **saída múltipla**, que devolve um ou mais cartões e é, ele próprio, a resposta à pergunta "de quantas árvores preciso"; e um conjunto de cartões de que o agente lê apenas os seus.

Cinco divergências foram resolvidas pelo mérito. **Três a favor da outra versão** — roteamento multi-saída, poda visível apenas como massa e nunca como rótulo, e ausência de concorrência entre árvores de caracterização e de mandato. **Duas a favor desta** — o filtro de admissão passa a incluir os dois testes anteriores a tudo (a frase de fecho assinável; conheço melhor as partes do que o alvo), e o acoplamento tem quatro saídas, não duas.

Uma divergência foi resolvida por **composição em vez de escolha**: o factor transversal tem agora duas notações com fronteira declarada — aresta para travessia parcial, objecto `transversal` para travessia total. A justificação é que uma aresta para cada irmão satura a passagem de dependência, que o protocolo trata como facto e não como sugestão, e um canal de confiança alta transformado em ruído é pior do que não existir.

O corpo operacional (§3) é curto por obrigação: é lido por agentes dentro de protocolos.

---

## 1 · Mandato

Produzir a versão combinada do documento de instruções de árvore, juntando duas versões escritas em paralelo sobre o mesmo mandato original — definição de árvore e instruções de uso no contexto deste protocolo, tipificando os casos e ajustando a estratégia a cada um, em formato curto e quase de fluxograma, com o agente a ver apenas o caso que lhe interessa, respondendo a "de quantas árvores preciso, quais, em que ordem e como se acoplam", e usando o vocabulário do protocolo com referência às regras `P1.x`.

Julgar cada divergência pelo mérito, não por autoria, e justificar em uma linha cada opção mantida contra a outra versão. Cinco divergências a resolver explicitamente:

1. **Roteamento** — saída única com tabela de "quantas árvores" lida por todos, contra saída múltipla com o número a sair do próprio roteamento. Os dois testes de admissão de uma das versões (frase de fecho assinável; conheço melhor as partes do que o alvo) são superiores à porta de entrada da outra.
2. **Factor transversal** — aresta `P1.4` contra objecto `transversal` ao nível da árvore com cone igual à árvore inteira. Avaliar complementaridade.
3. **Visibilidade da poda** — rótulo do ramo podado visível, contra apenas contagem e eixo, por o rótulo ser material de reabertura.
4. **Concorrência de árvores** — se há ou não árvores concorrentes em caracterização e em mandato.
5. **Integração cruzada** — trazer de uma das versões `escapar` como quarta saída de acoplamento, a ausência de identificador em "árvores concorrentes", a declaração do formalismo que sustenta a exaustividade com residual nomeado, `suspenso: por dimensionar` com gatilho de reformulação da raiz, e os campos em falta a `P1.1`; e da outra, a consistência de tipo de pergunta da raiz à folha e a integridade do driver como desempate entre concorrentes.

---

## 2 · Método

Cada divergência foi julgada por quatro critérios, aplicados nesta ordem.

**1 · Mecanismo do protocolo antes de doutrina.** Uma solução que preserva a qualidade de um canal existente vence uma que a degrada. É este critério que decide o factor transversal: a passagem de dependência é a única das três passagens de detecção classificada como **facto**, e a solução que a satura converte-a em sugestão. Nenhum ganho de simplicidade compensa isso.

**2 · Efeito declarado antes de efeito desejado.** Onde as duas versões perseguem o mesmo efeito, vence a que o obtém com menos fuga de informação. É o critério que decide a visibilidade da poda: o enviesamento medido é **quantitativo** — o residual não incha para absorver o que foi removido — e a contagem por eixo corrige-o inteiro, sem entregar o material com que se reabriria um ramo. O rótulo entrega mais do que o necessário para o mesmo efeito.

**3 · Regra que decorre da forma antes de regra imposta à forma.** Onde uma exigência não decorre da natureza da estrutura, cai. É o critério que decide a concorrência: competem-se cortes quando é preciso escolher **uma** partição; numa estrutura de eixos não se escolhe, acrescenta-se — logo duas caracterizações do mesmo objecto são redundância, não alternativa.

**4 · Contradição interna antes de conformidade textual.** Onde o protocolo se contradiz, vence a leitura que salva a prosa fundamentadora contra a regra mal escrita. É o critério que decide o acoplamento com quatro saídas: a arquitectura escreve "duas saídas apenas — aprofundar ou podar" e, dois parágrafos abaixo, dá como razão de ser do acoplamento que "a evidência não decidiu — mudou o significado das opções". Mudar o significado não é aprofundar nem podar.

Critério de forma, transversal: **uma correcção que retira uma regra vence uma que acrescenta**, a efeito igual. É o critério declarado pelo próprio protocolo ("o governo não incha") e é por ele que `P1.3` passa a corolário de `P1.2` em vez de regra autónoma.

---

## 3 · Corpo do relatório

> **Como ler.** §3.1 a §3.5 são para todos. De §3.6 lê **apenas os cartões que o roteamento te devolveu** — ler os outros carrega eixos que não são teus e contamina o corte. §3.7 é registo, não instrução.

### 3.1 · Definição

Uma árvore é uma **partição de um espaço por eixos**.
**Ramo** = unidade de trabalho · **eixo** = critério de divisão · **aresta** = dependência declarada · **cone** = tudo a jusante por travessia das arestas.

Não é um plano — o plano é o **caminho**. Não é um índice — o índice deriva do que existe. Não é o entregável decomposto.
**A árvore gera os cortes; o caminho testa-os.** A triagem mata ramos antes de haver dados; o caminho gasta dados no que sobrou.
A árvore mais as arestas é um semi-reticulado: o que atravessa vários ramos vive na aresta ou no `transversal`, nunca no ramo.

### 3.2 · Porta de entrada — precisas mesmo de árvore?

Se **qualquer** destes for verdade, não abras árvore. Vai a **CARTÃO E**.

| Sinal | Porquê |
|---|---|
| Não consegues escrever a frase que, daqui a 6 meses, dirá que isto está resolvido — e que os outros assinariam | o trabalho ainda é sobre a formulação |
| Não conheces melhor as **partes** do que o **alvo** | decompor só empurra a incerteza para baixo |
| A definição do problema muda a cada interlocutor | ainda é mandato ou rumo |
| Não consegues escrever a condição de morte | `P1.1` impede |
| O que interessa só existe no todo (coerência, confiança, cultura) | não tem ramo possível |
| A causalidade tem retorno: X afecta Y que afecta X | cortar o ciclo **é** decidir |
| O objecto é gosto, luto ou identidade | articular altera o que se queria descobrir |
| Decisão pequena e reversível | o custo de estruturar excede o valor |

### 3.3 · Roteamento

Responde às quatro. **Podem sair-te várias. É normal, e é a resposta a "quantas árvores".**

```
G0  O humano não consegue enunciar o que quer? ........ CARTÃO D · MANDATO
      (abre antes de tudo, morre antes de tudo; ao morrer, volta a G1)

G1  Há um estado indesejado cuja causa se procura? .... CARTÃO A · PROBLEMA

G2  Falta conhecer o objecto ou o terreno antes de
    se poder escolher? ............................... CARTÃO B · CARACTERIZAÇÃO

G3  Há opções sobre a mesa entre as quais escolher? ... CARTÃO C · DECISÃO
```

### 3.4 · Quantas, por que ordem, como acoplam

| Saiu | Quantas | Ordem | Acoplamento |
|---|---|---|---|
| **D** | 1, isolada | morre primeiro, produz o `MANDATO`, **volta a G1** | nenhum — D não acopla |
| só **A** | **≥2 concorrentes** | simultâneas até a triagem matar as estéreis | — |
| só **C** | **≥2 concorrentes** | idem | — |
| **B** | **1, nunca concorrente** | — | — |
| **B + C** | 2 propósitos | **B primeiro**; C abre em paralelo com ramos `suspenso: <ramo de B>` | ao devolver, C aplica as quatro saídas (R10) |
| **A + B** | 2 propósitos | **B primeiro** quando a causa depende de terreno desconhecido | idem |
| **A → C** | 2 propósitos | A fecha, C abre | o fecho de A recalcula o cone de C |

**Concorrência.** Obrigatória em **A** e **C**: uma árvore só não é escolha, é inércia. Proibida em **B** e **D**: aí acrescenta-se eixo, não se compete por ele — duas caracterizações do mesmo objecto são redundância, não alternativa.

**Desempate entre concorrentes**, por ordem: **(1) integridade do driver** — vence o corte que mantém o driver provável inteiro dentro de um ramo em vez de o repartir; (2) assimetria esperada; (3) accionabilidade.
*Um ramo com arestas para todos os irmãos é driver mal alojado, ou `transversal` por declarar (R6).*

**Nunca se fundem** (`P1.7`). Acoplam por dependência declarada (`P1.4`).

### 3.5 · Regras comuns

| | |
|---|---|
| **R1** | Um eixo por nó (`P1.2`). Eixos compõem-se por níveis, nunca no mesmo nível |
| **R2** | ME e CE aplicam-se **dentro do eixo**, em qualquer propósito. Entre eixos, nenhum dos dois. `P1.3` lê-se: *ramos irmãos sob o mesmo eixo não podem sobrepor-se* |
| **R3** | A mesma pergunta da raiz à folha. Não se mistura "porquê" com "como". **O "como" é do caminho** — uma árvore de "como" é sinal de que o caminho não foi escrito |
| **R4** | `P1.1` nasce com cinco campos: *propósito · raiz · decisor · precisão exigida e horizonte · condição de morte*. Raiz em forma de pergunta cuja resposta é a solução, nunca tópico (excepto cartões B e D) |
| **R5** | Arestas declaradas **no acto de desenhar o ramo** (`P1.4`), nunca depois. Podar **não** apaga a aresta: marca-a `podada`, e o cone a jusante continua a existir |
| **R6** | **Factor transversal, duas notações.** Atravessa *alguns* irmãos → arestas (`P1.4`). Atravessa *todos* → objecto **`transversal`** ao nível da árvore, com slug; não é ramo nem aresta; cone afectado = a árvore inteira. Descoberto depois de a árvore estar desenhada → **redesenha-se, não se remenda** |
| **R7** | Poda com razão registada (`P1.6`). A projecção mostra a **massa podada** — quantos ramos irmãos foram podados e **sob que eixo**. Nunca o rótulo, nunca a razão, nunca a alternativa |
| **R8** | **Assimetria esperada** é hipótese *sobre o corte*, formulada antes dos dados; a **triagem** (`P1.5`) é o teste barato dessa hipótese; **assimetria verificada** é resultado. Valida o corte com contas de guardanapo antes de ramificar |
| **R9** | Não normalizes pesos — somar a 1 afirma exaustividade que não tens. Compara ramos só entre irmãos com a **mesma granularidade**: subdividir um ramo aumenta-lhe o peso percebido, sem mérito |
| **R10** | Árvores de propósito diferente não se fundem (`P1.7`). **Quatro saídas de acoplamento:** `aprofundar` · `podar` · `recortar` (o resultado mudou o significado: o eixo do nó é refeito) · `escapar` (o resultado cai fora da árvore → sobe ao caminho como pressuposto, não como ramo) |

**Estados de ramo:** `por abrir` · `em desenvolvimento` · `fechado` · `podado` · `suspenso: <dependência>` · `suspenso: por dimensionar`.

**Nota de numeração:** os `P1.x` desta página são os de `arquitectura-governo.md` (`P1.1`–`P1.7`). O documento `R3` usa `P1.x` com outro referente. Confirma a família antes de invocar. `P1.8` (concorrência obrigatória em A e C) é proposta — hoje só existe em prosa.

### 3.6 · Cartões — lê só o teu

---

#### ▸ CARTÃO A · PROBLEMA — *porque é que isto acontece*

**Ramos são partes; partes somam-se.**
**Antes de ramificar:** escreve o contraste. Onde o problema **está** e onde **podia estar e não está**; quando sim e quando não. Esgotar o contraste é mais barato do que qualquer ramo e elimina metade deles.

| | |
|---|---|
| **Raiz** | pergunta fechada: *porque é que `<estado indesejado>`* |
| **Concorrência** | **≥2 árvores**, eixos conceptuais distintos. Desempate: integridade do driver |
| **Driver** | nomeia o mais provável. Fica inteiro num ramo? Não → muda o corte, ou declara `transversal`/aresta (R6). Ignorá-lo é proibido |
| **ME / CE** | ambos, estritos, **dentro do eixo** |
| **Exaustividade** | declara o **formalismo** que a sustenta: algébrico · booleano · regra-100% · `A / não-A` → sem residual. **Nenhum** (categorias presumidas, o caso normal) → **residual nomeado obrigatório**, que diz o que ficou de fora. Nunca "Outros" |
| **Triagem** | `P1.5`: variação de 10× muda a decisão final? **não** → poda (R7) · **não sei** → `suspenso: por dimensionar`, **não podes podar** · **>½ dos irmãos suspensos** → a raiz está errada: reformula a raiz, não recolhas mais dados |
| **Ordem de ataque** | primeiro as análises que eliminam ramos inteiros, depois as que refinam |
| **Folha** | hipótese falsificável por **uma** análise discreta. Se não é, ramifica mais |
| **Profundidade** | desigual é priorização, não defeito |
| **Morte** | causa identificada e confirmada; **ou** cone prioritário esgotado sem causa → escala |
| **Entrega** | a causa, ao caminho, como pressuposto testável |

**Armadilha:** declarar exaustividade porque a regra a exige. A sensação de completude não correlaciona com completude.

---

#### ▸ CARTÃO B · CARACTERIZAÇÃO — *o que é este objecto*

**Os ramos de primeiro nível não são partes. São eixos.** Partes somam-se; eixos cruzam-se — o objecto tem simultaneamente uma posição em cada.

**Declara dois registos, separados e nunca misturados no mesmo nível:**

| | **eixos do real** | **eixos de preferência** |
|---|---|---|
| Vêm de | domínios de conhecimento | da pessoa |
| Pode-se estar errado? | **sim** | **não** |
| Fecham-se por | investigação, medição | conversa |
| Falta um porque | ainda não se investigou | ainda não se descobriu que se queria |

A valência não é propriedade do facto: é relação entre um facto e uma pessoa.

| | |
|---|---|
| **Raiz** | o objecto, não uma pergunta |
| **Concorrência** | **não há**. Acrescenta-se eixo, não se compete por ele |
| **ME / CE** | dentro de cada eixo, **ambos**. Entre eixos, **nenhum dos dois**. É assim que se lê `P1.3` aqui |
| **Forma** | aberta. Eixo novo é resultado, não defeito. Um eixo derivável de outro sai |
| **Triagem** | **não se aplica** — não há ainda decisão contra a qual triar. Substitui por: *este eixo discrimina entre as opções vivas?* |
| **Poda** | **proibida enquanto a árvore está aberta.** Ramo que não discrimina fica `suspenso`, nunca `podado` |
| **Pesos** | não atribuas pesos que somem 100% (R9) |
| **Em vez de exaustividade** | **consistência cruzada**: cruza posições par a par, elimina as combinações incompatíveis, fica com o resto |
| **Morte** | **saturação**: dois ciclos consecutivos de investigação sem **nenhum eixo novo** — posições novas em eixos existentes não contam. Declara isto ao nascer (`P1.1`) |
| **Ao fechar** | verifica-se a exaustividade **dentro de cada eixo**, nunca entre eixos |
| **Entrega** | **não entrega decisão. Entrega significado** — o que as opções passam a querer dizer neste contexto concreto |

**Teste de suficiência**, antes de declarar saturação: *consigo, só com estes eixos, descrever um objecto que seria claramente mau aqui, e distingui-lo do bom?* Se os dois recebem a mesma descrição, falta um eixo.
**Output:** um **espaço de configurações consistentes**, não uma resposta. A pluralidade é o produto declarado, não uma falha.
**Armadilha:** ser tratada como decomposição do entregável. Essa é outra coisa — partes, com regra dos 100% — e pertence ao cartão A.

---

#### ▸ CARTÃO C · DECISÃO — *qual destas*

**Ramos são alternativas; alternativas excluem-se.**

| | |
|---|---|
| **Raiz** | a escolha, com o **espaço de opções declarado** |
| **Concorrência** | **≥2 árvores**, eixos distintos sobre o espaço de opções. Desempate: integridade do driver |
| **Eixo** | um por nó (`P1.2`). Cada ramo recai sobre variável que **este** decisor mexe — alavanca enorme e imóvel elimina-se, não se estuda |
| **ME** | estrita entre opções irmãs |
| **CE** | sobre o **espaço declarado** ("dentro destas N opções"), nunca absoluta. Escreve o espaço |
| **Triagem** | `P1.5`, com as três saídas do cartão A |
| **Profundidade** | desigual é alocação de esforço. O ramo raso **fica registado** como não aprofundado — não desaparece |
| **Pesos** | não normalizes (R9). Decide por eliminação e dominância |
| **Se depende de B** | ramos ficam `suspenso: <ramo de B>`. Ao devolver, aplica as **quatro saídas** de R10 — a saída provável de uma caracterização é `recortar`, não `aprofundar` |
| **Morte** | opção escolhida, registada **com a alternativa rejeitada** |
| **Entrega** | a opção, ao caminho, como caminho a executar ou pressuposto a testar |

**Armadilha:** a solução vem de fora da árvore mais vezes do que parece. Se o resultado não cabe em nenhum ramo, usa `escapar` — não o forces para dentro.
**Bloqueio:** nenhum ramo é declarado escolhido com discriminante por testar (`P2.4`).

---

#### ▸ CARTÃO D · MANDATO — *o que é que eu quero, afinal*

**Diferença face a C: em C as opções existem e seleccionam-se. Aqui não existem — geram-se.**
A estrutura não mede a preferência: constrói-a. Trata-a como instrumento, não como espelho.

| | |
|---|---|
| **Raiz** | o humano responsável |
| **Concorrência** | **não há** |
| **Como se obtêm os eixos** | por **contraste entre exemplos concretos**, nomeados com as palavras do humano. Nunca por questionário. Pergunta *"o que é que este tem que aquele não tem?"* |
| **Teste a cada nó** | *"porque é que isto é importante?"* — se remete para outro objectivo, é **meio**, não fim: é rede, não árvore. Tira-o daqui |
| **ME / CE** | dentro do eixo. Conjunto de eixos **aberto** |
| **Triagem** | **não.** É generativa. Podar aqui é podar o que o humano ainda não aprendeu a querer |
| **Profundidade** | desigual **é defeito** nesta árvore — nesta fase todos os ramos valem o mesmo |
| **Poda / pesos** | não se poda, não se pondera |
| **Mudar a meio** | é funcionamento, não avaria. Uma estrutura que não se mexe é mais provavelmente ancoragem do que estabilidade |
| **Morte** | saturação **e** discriminação: sem eixos novos, **e** a estrutura já separa as opções em cima da mesa. Produz o `MANDATO` e morre — não sobrevive ao desbloqueio de `P0.7` |
| **Entrega** | 1–5 objectivos com slug e 2–3 não-objectivos por objectivo (`P0.1`, `P0.2`). Depois **volta a G1** |

**Armadilha:** entregar um mandato cujos objectivos são meios uns dos outros. Quebra `P0.1`–`P0.2` a jusante e só aparece semanas depois.

---

#### ▸ CARTÃO E · NÃO USES ÁRVORE

**O trabalho ainda é sobre a FORMULAÇÃO.** Uma árvore construída agora é uma resposta à pergunta errada com aparência de rigor.

```
Faz:
  · IS / IS-NOT sobre a fronteira do fenómeno
  · eixos abertos (cartão B), sem fechar nada
  · morfologia: parâmetros × posições, consistência cruzada par a par
  · sondas: intervenções pequenas e reversíveis, para ver o que responde
  · decompõe o espaço de ACÇÃO (intervenções candidatas), nunca o espaço CAUSAL

Não faças:
  · não podes podar — a poda é o erro caro aqui
  · não feches a definição do problema
  · não reduzas a duas opções
  · não trates isto como igual a um caso anterior já resolvido
  · não meças um substituto por o original não se deixar medir
```

**Saída:** um **pressuposto** para o caminho (`P2.2`), com regra de paragem escrita antes de a frente abrir (`P2.3`). Não um ramo.
**Reentrada:** volta a §3.2 quando a frase de fecho passar a ser escrevível. Só então.

---

### 3.7 · Registo das cinco divergências

| # | Divergência | Resolução | Razão, em uma linha |
|---|---|---|---|
| 1 | roteamento de saída única vs. múltipla | **saída múltipla** (versão do outro agente), com os dois testes de admissão desta versão promovidos a filtro anterior (§3.2) | o mandato exige responder a "uma ou mais"; um roteamento que pára na primeira saída não consegue devolver "duas" e obriga a uma tabela lida por todos — a saída múltipla é a própria resposta, e a tabela de §3.4 encolhe para ordem e acoplamento |
| 2 | aresta `P1.4` vs. objecto `transversal` | **as duas, com fronteira declarada** (R6): travessia parcial → aresta; travessia total → `transversal`, cone = árvore inteira | não são alternativas mas regimes diferentes do mesmo fenómeno; uma aresta para cada irmão satura a única passagem de detecção classificada como *facto* e converte-a em ruído, que é pior do que silêncio num sistema cujo caso normal é o alerta vazio |
| 3 | rótulo do ramo podado vs. massa podada | **massa podada** (versão do outro agente): quantos ramos e sob que eixo, nunca o rótulo | o enviesamento medido é quantitativo — o residual não incha para absorver o removido — e a contagem por eixo corrige-o inteiro sem entregar material de reabertura; é a mesma lógica de devolver o identificador e nunca a razão, aplicada à poda |
| 4 | concorrência em caracterização e mandato | **proibida** nas duas (versão do outro agente), obrigatória em problema e decisão | competem-se cortes quando é preciso escolher uma partição; numa estrutura de eixos acrescenta-se em vez de escolher, logo duas caracterizações do mesmo objecto são redundância e não alternativa |
| 5 | integração cruzada | **tudo integrado**, com uma excepção: o acoplamento mantém **quatro** saídas e não duas | *(opção mantida contra a outra versão)* a arquitectura escreve "duas saídas apenas" e justifica o acoplamento dizendo que a evidência "mudou o significado das opções" — que não é aprofundar nem podar; o cartão B da outra versão diz, correctamente, que a caracterização "entrega significado", o que contradiz a sua própria regra de duas saídas |

Integrado desta versão: `escapar`; `P1.8` proposta com identificador para a concorrência; formalismo de exaustividade declarado com residual nomeado; `suspenso: por dimensionar` com gatilho de reformulação da raiz; cinco campos em `P1.1`; granularidade comparável entre irmãos; cartão E operacional; nota de numeração.
Integrado da outra versão: consistência de tipo de pergunta da raiz à folha (R3), que torna `P1.7` verificável dentro de um ficheiro; integridade do driver como desempate entre concorrentes; `P1.3` reduzida a corolário de `P1.2` (R2); assimetria esperada vs. verificada (R8); contraste antes de ramificar; saturação operacionalizada em dois ciclos sem eixo novo; teste de suficiência antes de declarar saturação; distinção mandato/decisão por estatuto do espaço de opções; profundidade desigual como defeito em D.

---

## 4 · Fontes

Documentos de partida, lidos na íntegra:

- [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-frio]] — versão desta linha de trabalho
- [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso]] — versão produzida em paralelo
- [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore-frio]] — racional crítico desta linha
- [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore]] — racional crítico da outra linha

Alvo criticado, e origem do vocabulário `P0.x`/`P1.x`/`P2.x`, `cone`, `frente`, `slug`, `triagem`, `caminho`, `pressuposto`:

- [[arquitectura-governo]] §2.2 — a árvore como instrumento de partição
- [[R3-genese-mandato-global-arvore]] §7 — natureza da árvore, três tempos

Base de evidência invocada nos dois racionais críticos:

- [[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]] — ciclo de vida da árvore, da pergunta-raiz ao arquivo
- [[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]] — três modos de árvore, ME sem CE, limites e evidência experimental

**Advertência de estatuto.** Vários resultados citados nos racionais são declarados pelas próprias sínteses como lidos em paráfrase e não no original — entre eles a redução de erro por decomposição, o efeito de analisar razões sobre a satisfação pós-escolha, e a literatura sobre ruminação. O estudo de árvores de falhas que sustenta R7 e a proibição de poda nos cartões B, D e E é, esse, relatório original com dados. Nenhum número deve ser usado citacionalmente sem confirmação contra a fonte primária.
