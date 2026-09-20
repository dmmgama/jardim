---
title: "Árvore — definição e uso (versão combinada)"
date: 2026-09-20
type: sintese
case: protocolo
tags: [MECE, arvore, protocolo, instrucao-operacional]
sobre:
  - "[[2026-09-20-sintese-protocolo-arvore-definicao-e-uso]]"
  - "[[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-frio]]"
  - "[[2026-09-20-audit-protocolo-criticas-definicao-de-arvore]]"
  - "[[2026-09-20-audit-protocolo-criticas-definicao-de-arvore-frio]]"
---

# Árvore — definição e uso · versão combinada

## 0 · Sumário executivo

Junta as duas versões independentes do documento operacional numa só, resolvendo seis divergências pelo mérito.

**O que se adoptou de cada lado.** Da versão fria: as duas perguntas de porta (`R0` frase de fecho assinável, `R1` partes vs. alvo), o cartão **E** como destino com instruções próprias em vez de saída sem rumo, a quarta saída de acoplamento `escapar`, a declaração obrigatória do **formalismo que sustenta a exaustividade** com residual nomeado, o estado `suspenso: por dimensionar` com gatilho de reformulação da raiz, os campos em falta em `P1.1`, o teste WITI no mandato, e a condição de morte verificável do mandato. Da outra versão: o roteamento **multi-cartão** (é ele que responde a "uma ou mais"), a **consistência de tipo de pergunta** da raiz à folha, a **integridade do driver** como desempate entre árvores concorrentes, a exclusão de concorrência em caracterização e mandato, e a projecção da **massa podada sem rótulo**.

**As duas divergências resolvidas por síntese e não por escolha:** o factor transversal fica com **duas notações** — aresta para travessia parcial, objecto `transversal` para travessia total; e a poda passa a ter **contagem visível sem rótulo**, mais a aresta que sobrevive marcada `podada`.

**Uma coisa não se resolveu:** os identificadores `P1.x` divergem entre os dois documentos de origem. O documento assinala-o e não escolhe.

---

## 1 · Mandato

Produzir uma versão combinada dos dois documentos de instruções produzidos independentemente sobre o mesmo mandato — definir a árvore e as instruções de uso no contexto do protocolo, tipificando casos e ajustando a estratégia a cada um — que fique melhor do que qualquer uma das duas.

Requisitos herdados do mandato original, que se mantêm:

- curto, porque é lido por agentes dentro de protocolos e não pode carregar contexto a mais;
- quase um diagrama de fluxo: o agente entra, percebe o caso e é encaminhado;
- o agente não vê os casos que não lhe interessam;
- responde a **de quantas árvores preciso**, quais, por que ordem e como acoplam;
- vocabulário do protocolo, com referência às regras `P1.x`.

---

## 2 · Método

**Critério de arbitragem.** Cada divergência foi julgada por mérito e não por autoria, contra três testes, por esta ordem:

1. **Custo em contexto.** Entre duas formulações correctas, vence a que ocupa menos espaço na janela do agente que a vai ler.
2. **Fidelidade ao desenho declarado do protocolo.** Uma proposta que informa mais mas contraria uma intenção de desenho explícita (por exemplo, a omissão de razões na projecção) perde, salvo se a intenção estiver errada — e nesse caso a crítica vai para o documento de auditoria, não para aqui.
3. **Verificabilidade.** Vence a regra que o auditor consegue confirmar por inspecção, contra a que depende de julgamento.

**Regra de composição.** Onde as duas propostas resolviam casos diferentes do mesmo problema, adoptaram-se ambas em vez de se escolher uma. Aconteceu duas vezes: factor transversal e visibilidade da poda.

**Limite assumido.** O articulado normativo não foi lido — não está na pasta. Os identificadores `P1.x` usados são os de `arquitectura-governo.md`.

---

## 3 · Corpo do relatório

### 3.1 · Registo das divergências e como se resolveram

| # | Divergência | Resolução | Porquê |
|---|---|---|---|
| 1 | Roteamento: um cartão vs. vários | **Híbrido.** `R0` e `R1` como **portas** (falham → cartão E); `R2` como roteamento **multi-cartão** | As portas da versão fria são melhores e são binárias, portanto baratas. Mas "uma ou mais" tem de sair do roteamento, não de uma tabela lida à parte — senão a pergunta central fica respondida fora do fluxo |
| 2 | Factor transversal: aresta vs. objecto | **Ambos.** Aresta para travessia parcial; objecto `transversal` ao nível da árvore para travessia total | Resolvem casos diferentes. Um factor que atravessa *todos* os ramos, posto em arestas, satura a passagem de dependência — que o protocolo trata como **facto** e não como sugestão. Degradá-la custa mais do que informa |
| 3 | Poda: rótulo visível vs. só contagem | **Contagem e eixo, sem rótulo**, e a **aresta sobrevive** marcada `podada` | O rótulo é material de reabertura, e a projecção omite esse material por desenho declarado (critério 2). A aresta sobrevivente dá o efeito estrutural que o rótulo dava, sem o custo |
| 4 | Concorrência de árvores em todos os propósitos | **Só em problema e decisão** | Em caracterização e mandato acrescenta-se eixo; não se compete por ele. Duas árvores sobre o mesmo objecto são aí redundância, não alternativa |
| 5 | Saídas de acoplamento | **Quatro**: `aprofundar` · `podar` · `recortar` · `escapar` | `escapar` é o achado da versão fria e fecha um caso real: a solução que cai fora da árvore. Com duas saídas, o resultado é forçado para dentro de um ramo |
| 6 | Identificadores `P1.x` | **Não resolvido**, assinalado | Divergem entre os dois documentos de origem e o articulado não está disponível |

---

### 3.2 · O documento operacional

> **Como ler.** §A e §B. Depois §C. Depois **só os cartões que §B te devolveu** — não leias os outros. Depois §E. Ignora o resto.

---

#### A · Definição

Uma árvore é uma **partição de um espaço por eixos**.
**Ramo** = unidade de trabalho · **Aresta** = dependência declarada · **Eixo** = critério de divisão.

Não é um plano — a ordem vem do **caminho**. Não é um índice — o índice deriva do que existe. Não é o entregável decomposto.

**A árvore gera os cortes; o caminho testa-os.** A triagem mata ramos antes de haver dados, de graça; o caminho gasta dados no que sobrou.

Árvore mais arestas é um semi-reticulado: o que atravessa **alguns** ramos vive na aresta; o que atravessa **todos** é `transversal` (R5).

---

#### B · Roteamento

```
PORTA 1 · Consegues escrever agora a frase que, daqui a seis meses, dirá
          que isto está resolvido — e os outros assinavam-na?
            NÃO, e não há mandato ....................... CARTÃO D, e só D
            NÃO, há mandato mas a raiz foge ............. CARTÃO E
            SIM ......................................... segue

PORTA 2 · Conheces melhor as PARTES do que o ALVO?
            NÃO ......................................... CARTÃO E
            SIM ......................................... segue

PORTA 3 · Algum destes é verdade?
            · a definição muda a cada interlocutor
            · a causalidade tem retorno: X afecta Y afecta X
            · o que interessa só existe no todo
            · as ligações pesam mais do que os elementos
            · decisão pequena e reversível
            · o objecto é gosto, luto ou identidade
            qualquer um ................................. CARTÃO E
            nenhum ...................................... segue

ROTEAMENTO · responde às quatro. PODEM SAIR-TE VÁRIAS.
             É isto que responde a "de quantas árvores preciso".

  G1  Há um estado indesejado cuja causa se procura? ..... + CARTÃO A
  G2  Falta conhecer o objecto ou o terreno
      antes de se poder escolher? ....................... + CARTÃO B
  G3  Há opções sobre a mesa entre as quais escolher? .... + CARTÃO C
  G4  O humano não consegue enunciar o que quer? ........ + CARTÃO D
                                                           (abre e morre antes de tudo)
```

---

#### C · Quantas, por que ordem, como acoplam

| Saiu | Quantas | Ordem | Acoplamento |
|---|---|---|---|
| só **A** | 1 propósito, **≥2 concorrentes** | — | — |
| só **C** | 1 propósito, **≥2 concorrentes** | — | — |
| **B + C** | 2 propósitos | **B abre primeiro**; C abre em paralelo com ramos suspensos | ramos de C ficam `suspenso: <ramo de B>` |
| **A + B** | 2 propósitos | **B primeiro** se a causa depende de terreno desconhecido | idem |
| **A → C** | 2 propósitos, **nunca a mesma árvore** (`P1.7`) | A fecha, C abre | o fecho de A recalcula o cone de C |
| **D** | 1, isolada | **morre primeiro**, produz o `MANDATO`, **volta ao roteamento** | não acopla |

**Quatro saídas de acoplamento**, e só quatro:

| Saída | Quando |
|---|---|
| `aprofundar` | o resultado confirma que o ramo vale trabalho |
| `podar` | o resultado mata o ramo |
| `recortar` | o resultado mudou o **significado** das opções → o eixo do nó é refeito |
| `escapar` | o resultado **não cabe em nenhum ramo** → sobe ao caminho como pressuposto, não como ramo |

*`escapar` não é falha da árvore. A solução vem de fora dela mais vezes do que parece; forçá-la para dentro de um ramo é que é falha.*

**Concorrência.** Em **A** e em **C**, sempre ≥2 árvores com eixos conceptuais distintos — uma árvore só é inércia, não é escolha. Em **B** e em **D**, **não há concorrência**: acrescenta-se eixo, não se compete por ele.
*Se abrires só uma onde se pedem duas, regista em `REJEICOES` o eixo que não desenhaste e porquê.*

**Desempate entre concorrentes**, por ordem: **(1) integridade do driver** — vence o corte que mantém o driver provável inteiro dentro de um ramo; (2) assimetria esperada; (3) accionabilidade.
*Um ramo com arestas para todos os irmãos é driver mal alojado, ou `transversal` por declarar.*

---

#### D · Cartões — lê só o teu

> Ler os outros carrega eixos que não são teus e contamina o corte.

---

##### ▸ CARTÃO A · PROBLEMA — «porque é que isto acontece»

**Ramos são partes. Partes somam-se.**

**Antes de ramificar:** escreve o contraste — onde o problema **está** e onde **podia estar e não está**; quando sim e quando não. Esgotar o contraste é mais barato do que qualquer ramo e elimina metade deles.

```
1  Duas árvores, eixos distintos. Valida cada eixo com conta de
   guardanapo ANTES de ramificar.

2  Nomeia o driver mais provável. Fica inteiro num ramo?
     sim              → o corte serve
     atravessa alguns → declara-o aresta P1.4, visível a todos os
                        ramos que atravessa
     atravessa todos  → não é ramo nem aresta: é `transversal` (R5)
   Ignorá-lo é proibido.

3  Declara o formalismo que sustenta a exaustividade do nó:
     algébrico · booleano · regra-100% · A/não-A → sem residual
     nenhum (categorias presumidas)             → RESIDUAL NOMEADO,
                                                  obrigatório, nunca «Outros»

4  Triagem (P1.5): variação de 10× muda a decisão final?
     não      → poda, razão registada (P1.6)
     não sei  → `suspenso: por dimensionar`. NÃO PODES PODAR.
     mais de metade dos irmãos suspensos → a raiz está errada.
       Reformula a raiz. Não recolhas mais dados.

5  Ordem de ataque: primeiro as análises que eliminam ramos inteiros,
   depois as que refinam.

6  Compara ramos só entre irmãos com a mesma granularidade.
   Subdividir um ramo aumenta-lhe o peso percebido, sem mérito.
```

**Folha:** hipótese falsificável por **uma** análise discreta. Se não é, ramifica mais.
**Profundidade desigual:** é priorização, não defeito.
**Morte:** causa localizada e confirmada; **ou** cone prioritário esgotado sem causa → escala.
**Entrega ao caminho:** a causa, como pressuposto testável.
**Armadilha:** declarar exaustividade porque a regra a exige. A sensação de completude não correlaciona com completude.

---

##### ▸ CARTÃO B · CARACTERIZAÇÃO — «que espécie de coisa é esta»

**Isto não se comporta como árvore. São eixos, e os eixos cruzam-se.**
Um objecto não se reparte pelos eixos: tem simultaneamente uma posição em cada.

```
1  NÃO compões eixos por níveis. Listas eixos, lado a lado.

2  DENTRO de cada eixo: ME e CE. As posições cobrem o espectro e não
   se sobrepõem. É assim que se lê P1.3 aqui.

3  ENTRE eixos: nenhuma exaustividade a exigir. O conjunto é aberto
   por desenho — acrescenta-se um eixo sem refazer nada.

4  Separa os dois registos de eixo, e nunca os mistures no mesmo nível:
     do real        → pode estar errado; fecha-se investigando
     da preferência → não pode estar errado; abre-se conversando
   A valência não é propriedade do facto: é relação entre facto e pessoa.

5  Em vez de exaustividade: CONSISTÊNCIA CRUZADA. Cruza posições par a
   par, elimina as combinações incompatíveis, fica com o resto.

6  NÃO PODAR enquanto a árvore está aberta. Ramo que não discrimina
   fica `suspenso`, nunca `podado`.

7  NÃO PONDERAR. Somar a 1 é afirmar exaustividade que não tens.

8  Um eixo derivável de outro sai (não-redundância).
```

**Teste de suficiência:** *consigo, só com estes eixos, descrever um objecto que seria claramente mau aqui, e distingui-lo do bom?* Se os dois recebem a mesma descrição, falta um eixo.
**Morte: saturação** — dois ciclos consecutivos de investigação sem **nenhum eixo novo**; posições novas em eixos existentes não contam. Declara isto ao nascer (`P1.1`).
**Ao fechar:** verifica-se exaustividade **dentro de cada eixo**, nunca entre eixos.
**Output:** um **espaço de configurações consistentes**, não uma resposta. A pluralidade é o produto declarado.
**Entrega:** não entrega decisão — entrega **significado**. Ao acoplar a uma árvore de decisão, a saída provável é `recortar`.
**Armadilha:** ser tratada como decomposição do entregável. Essa é outra coisa — partes, com regra dos 100% — e pertence ao cartão A.

---

##### ▸ CARTÃO C · DECISÃO — «qual destas»

**Ramos são alternativas. Alternativas excluem-se.**

```
1  Duas árvores, eixos distintos sobre o espaço de opções.

2  Escreve o espaço de opções. CE é sobre o espaço DECLARADO
   («dentro destas N»), nunca absoluta.

3  Cada ramo recai sobre variável que ESTE decisor mexe. Alavanca
   enorme e imóvel elimina-se — não se estuda.

4  Triagem (P1.5), com as mesmas três saídas do cartão A.

5  Profundidade desigual é alocação de esforço. O defeito é o ramo
   raso desaparecer sem ficar registado que se decidiu não o aprofundar.

6  NÃO NORMALIZES PESOS. Somar a 100% afirma exaustividade que não
   tens, e subdividir um ramo aumenta-lhe o peso sem mérito.
   Decide por eliminação e dominância.

7  Se depende do significado das opções → abre B primeiro e acopla
   por aresta. NÃO FUNDAS (P1.7).

8  Nenhum ramo é declarado escolhido com discriminante por testar (P2.4).
```

**Morte:** opção escolhida, registada **com a alternativa rejeitada**; ramos não escolhidos ficam `podado` com razão.
**Entrega ao caminho:** a opção, como caminho a executar ou como pressuposto a testar.
**Armadilha:** o resultado que não cabe em nenhum ramo. Usa `escapar` — não o forces para dentro.

---

##### ▸ CARTÃO D · MANDATO — «o que é que eu quero, afinal»

**Em C as opções existem e seleccionam-se. Aqui não existem — geram-se.**
**A estrutura não mede a preferência: constrói-a.** Trata-a como instrumento, não como espelho.

```
1  Raiz curta. Ancora em EXEMPLOS CONCRETOS, nunca em categorias
   abstractas. Pergunta «o que é que este tem que aquele não tem?».
   Os eixos saem nomeados pelas palavras do humano.
   Analisar razões abstractas torna as opções mais parecidas entre si
   e privilegia o que se consegue dizer por palavras.

2  Teste WITI a cada nó — «porque é que isto é importante?»:
     remete para outro objectivo → é MEIO, não fim → é REDE, não
       árvore. Tira-o daqui.
     não remete → é fim → fica.

3  NÃO PODAR. NÃO PONDERAR. NÃO TRIAR.
   Podar aqui é podar o que o humano ainda não aprendeu a querer.

4  Profundidade desigual é DEFEITO nesta árvore. Nesta fase todos os
   ramos valem o mesmo.

5  Mudar a meio da conversa é funcionamento, não avaria. Uma estrutura
   que não se mexe é mais provavelmente ancoragem do que estabilidade.
```

**Morte:** **saturação e discriminação** — novas perguntas não geram eixos novos, **e** a estrutura já separa as opções em cima da mesa. *"Morre ao produzir o mandato" não é verificável; isto é.*
**Entrega:** 1–5 objectivos com slug e 2–3 não-objectivos por objectivo (`P0.1`, `P0.2`). Depois **volta ao roteamento**.
**Bloqueio:** nenhuma frente abre antes de `P0.7` devolver verdadeiro (`P0.8`).
**Armadilha:** entregar um mandato cujos objectivos são meios uns dos outros. Quebra `P0.1`–`P0.2` a jusante e só aparece semanas depois.

---

##### ▸ CARTÃO E · NÃO USES ÁRVORE

Chegaste aqui por uma das portas. **O trabalho ainda é sobre a FORMULAÇÃO.** Uma árvore construída agora é uma resposta à pergunta errada com aparência de rigor — e decompor só empurra a incerteza para baixo.

```
FAZ
  · IS / IS-NOT sobre a fronteira do fenómeno
  · eixos abertos (cartão B), sem fechar nada
  · morfologia: parâmetros × posições, consistência cruzada par a par
  · sondas: intervenções pequenas e reversíveis, para ver o que responde
  · decompõe o espaço de ACÇÃO — intervenções candidatas — nunca o
    espaço CAUSAL

NÃO FAÇAS
  · não podes podar: a poda é o erro caro aqui
  · não feches a definição do problema
  · não reduzas a duas opções
  · não trates isto como igual a um caso anterior já resolvido
  · não meças um substituto por o original não se deixar medir
```

**Saída:** um **pressuposto** para o caminho (`P2.2`), com regra de paragem escrita antes de a frente abrir (`P2.3`). Não um ramo.
**Reentrada:** volta ao roteamento quando a Porta 1 passar a SIM. Só então.

---

#### E · Regras comuns

| | |
|---|---|
| **R1** | **`P1.1`+** — ao nascer, declara cinco campos: *propósito · raiz (pergunta cuja resposta é a solução) · decisor · precisão exigida e horizonte · condição de morte*. Raiz em forma de pergunta, nunca tópico. Sem condição de morte, **não abras** |
| **R2** | **`P1.2`** — um eixo por nó. Eixos compõem-se por níveis, nunca por mistura no mesmo nível |
| **R3** | **ME e CE aplicam-se dentro do eixo.** Entre eixos, nenhum dos dois. É assim que se lê `P1.3` |
| **R4** | **Mesma pergunta da raiz à folha.** Não se mistura "porquê" com "como". **O "como" é do caminho** — uma árvore de "como" é sinal de que o caminho não foi escrito. É isto que torna `P1.7` verificável dentro de um único ficheiro |
| **R5** | **`P1.4`** — arestas declaradas **no acto de desenhar o ramo**, nunca depois. O que atravessa **alguns** ramos é aresta. O que condiciona **todos** é `transversal`: objecto ao nível da árvore, com slug, cone afectado = a árvore inteira. Transversal descoberto depois de a árvore estar desenhada → **redesenha-se, não se remenda** |
| **R6** | **`P1.6`** — poda regista razão. Na projecção aparecem **quantos ramos foram podados e sob que eixo** — nunca o rótulo, nunca a razão. **A aresta de um ramo podado sobrevive**, marcada `podada` |
| **R7** | **`P1.7`** — árvores de propósito diferente não se fundem. Acoplam por dependência declarada, com as quatro saídas de §C |
| **R8** | Estados de ramo: `por abrir` · `em desenvolvimento` · `fechado` · `podado` · `suspenso: <dependência>` · `suspenso: por dimensionar` |
| **R9** | **Nota de numeração.** Os `P1.x` desta página são os de `arquitectura-governo.md`. O `R3` usa `P1.x` com outro referente. Confirma a família antes de invocar |

---

#### F · Fecho

Um ramo que fecha devolve resultado ao caminho, e o cone a jusante é recalculado por travessia das arestas.

**Uma árvore madura é maioritariamente morta.** O ramo aberto diz o que se está a fazer; o ramo morto diz o que não se voltará a fazer. É a segunda informação que impede a repetição de trabalho meses depois.

**Se ficaste sem cartão,** estás em `Confused`. Aí a decomposição é operação de **triagem** legítima e de **modelação** ilegítima: usa-a para descobrir em que caso estás, e não a guardes como árvore.

---

## 4 · Fontes

Documentos de origem, ambos produzidos independentemente sobre o mesmo mandato:

- [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso]]
- [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-frio]]

Auditorias que fundamentam as regras acrescentadas:

- [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore]]
- [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore-frio]]

Base de evidência:

- [[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]]
- [[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]]

Objecto auditado (fora desta pasta, em `naoabrirsemordem/`):

- `arquitectura-governo.md` §2.2 e protocolo `P0`–`P2`
- `R3-genese-mandato-global-arvore.md` §7
