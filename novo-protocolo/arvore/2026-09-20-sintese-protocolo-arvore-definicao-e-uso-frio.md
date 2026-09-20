---
title: "Arvore: definicao e uso no protocolo (agente frio, controlo independente)"
date: 2026-09-20
type: sintese
case: protocolo
tags: [MECE, arvore, protocolo, instrucao-operacional, controlo-independente]
sobre:
  - "[[2026-09-20-audit-protocolo-criticas-definicao-de-arvore-frio]]"
  - "[[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]]"
---

# Arvore: definicao e uso no protocolo (agente frio, controlo independente)

## 0 · Sumário executivo

- **Controlo independente** do documento operacional, produzido sobre o mesmo mandato sem contacto com a versão paralela.
- **Roteamento por portas binárias:** a frase de fecho assinável e o teste "conheço melhor as partes do que o alvo" — as duas melhores perguntas de entrada produzidas em qualquer das versões.
- **Cinco cartões**, com o quinto — "não uses árvore" — como **destino com instruções próprias**, e não como saída sem rumo.
- **Cartão de caracterização declarado explicitamente como não-árvore:** eixos lado a lado, nunca compostos por níveis.
- **Quatro saídas de acoplamento**, incluindo `escapar`, que fecha o caso do resultado que não cabe em nenhum ramo.
- **`P1.1`+ com cinco campos**, incluindo decisor, precisão e horizonte.
- A aresta **sobrevive à poda**, marcada `podada`.

---

## 1 · Mandato

**Prompt dado ao agente, em sessão fria** — idêntico ao da versão paralela, na mesma tarefa de controlo que produziu a auditoria independente:

> *"Uma definição de árvore e instruções de uso no contexto deste protocolo, que tipifique os casos e ajuste a estratégia de desenvolvimento e utilização das árvores a cada caso. Curto, porque é lido por agentes dentro de protocolos. Quase um diagrama de fluxo. O agente não deve ver os casos que não lhe interessam. Tem de responder a de quantas árvores preciso — uma ou mais — e quais, e em que ordem, e como se acoplam. Usa o vocabulário do protocolo e refere as regras `P1.x`."*

---

## 2 · Método

**Desenho de controlo**, com leitura restrita às duas sínteses e aos dois documentos do protocolo, e interdição de abrir o trabalho paralelo.

As decisões de desenho são do próprio agente. As que divergem da versão paralela — roteamento para um só cartão com tabela de contagem lida por todos, factor transversal resolvido na aresta, rótulo do ramo podado visível — foram depois arbitradas no documento combinado.

**Uso previsto:** comparação e alimentação da versão combinada.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

### 1 · O que é, em quatro linhas

Uma **árvore** parte um espaço em ramos, para que cada ramo possa virar trabalho ou morrer barato.
Não é um plano (a ordem vem do caminho), não é um índice (precede o que existe), não é a decomposição do entregável.
**A árvore gera os cortes; o caminho testa-os.** A triagem mata ramos antes de haver dados; o caminho gasta dados no que sobrou.
A árvore mais as **arestas** de `P1.4` é um semi-reticulado: o que atravessa vários ramos vive na aresta, não no ramo.

---

### 2 · Roteamento

Responde por ordem. Pára na primeira que te encaminhar.

```
R0  Consegues escrever agora a frase que, daqui a 6 meses, dirá que isto
    está resolvido — e os outros assinavam-na?
      NÃO e não há mandato ............................ CARTÃO D
      NÃO e o mandato existe mas a raiz foge ......... CARTÃO E
      SIM ............................................. R1

R1  Conheces melhor as PARTES do que o ALVO?
      NÃO ............................................. CARTÃO E
      SIM ............................................. R2

R2  Qual é a pergunta-raiz?
      «porque é que isto acontece»  .................. CARTÃO A
      «qual destas»                 .................. CARTÃO B
      «que espécie de coisa é esta» .................. CARTÃO C
      «o que é que eu quero, afinal» ................. CARTÃO D

R3  Antes de abrir o cartão, verifica os dois sinais de paragem:
      · a definição do problema muda a cada interlocutor  → CARTÃO E
      · as ligações entre elementos pesam mais que os
        elementos, ou o objecto é gosto, luto ou identidade → CARTÃO E
```

---

### 3 · De quantas árvores preciso

| Situação | Quantas | Quais, e por que ordem | Acoplamento |
|---|---|---|---|
| Mandato por enunciar | **1** | D. Morre ao saturar. Nada mais abre antes. | nenhum — precede tudo |
| Diagnóstico puro | **≥2** | A e A′, eixos conceptuais distintos, em simultâneo | triagem mata as estéreis |
| Decisão pura | **≥2** | B e B′, eixos distintos | idem |
| Decisão que depende do que as opções significam | **3 = C + B + B′** | C primeiro (abre), B/B′ em paralelo (fecham) | aresta `P1.4`: ramo de B declara que depende de ramo de C |
| Diagnóstico que vai dar em acção | **A, depois B** | nunca a mesma árvore (`P1.7`) | o fecho de A recalcula o cone de B |

**Regra dura.** Uma árvore só, num caso que pede duas, não é escolha — é inércia. Se abrires só uma, regista em `REJEICOES` o eixo alternativo que não desenhaste e porquê.

**Regra dura.** Árvores de propósito diferente **não se fundem** (`P1.7`). Se a decisão nunca fecha, foi fundida com uma caracterização.

---

### 4 · Vale em todos os cartões

- **`P1.1`+** — ao nascer, declara cinco campos: *propósito · raiz (pergunta cuja resposta é a solução) · decisor · precisão exigida e horizonte · condição de morte*. Raiz em forma de pergunta, nunca tópico.
- **`P1.2`** — um eixo por nó. Eixos compõem-se por níveis, nunca por mistura no mesmo nível.
- **`P1.4`** — as arestas declaram-se no acto de desenhar o ramo, não depois. O que atravessa vários ramos é aresta, não ramo. Um ramo podado **mantém** a aresta, marcada `podada`.
- **`P1.6`** — poda regista razão. Poda por triagem é **visível**: o rótulo do ramo fica na projecção dos irmãos. Só o fecho com resultado pode tornar um ramo invisível.
- Estados: `por abrir` · `em desenvolvimento` · `fechado` · `podado` · `suspenso: <dependência>` · `suspenso: por dimensionar`.
- **Saídas de acoplamento**, quatro: `aprofundar` · `podar` · `recortar` (o resultado mudou o significado: o eixo do nó é refeito) · `escapar` (o resultado cai fora da árvore → sobe ao caminho como pressuposto, não como ramo).
- **Nota de numeração:** os identificadores `P1.x` desta página são os de `arquitectura-governo.md`. O documento R3 usa `P1.x` com outro referente. Confirma a família antes de invocar.

---

### 5 · Cartões

> **Lê apenas o teu.** Ler os outros carrega eixos que não são teus e contamina o corte.

---

#### ▸ CARTÃO A — PROBLEMA · «porque é que isto acontece»

**Ramos são partes; partes somam-se.**

```
1  Duas árvores, eixos distintos. Valida cada eixo com conta de guardanapo
   ANTES de ramificar.
2  Nomeia o driver mais provável. Fica inteiro num ramo?
      sim  → o corte serve
      não  → muda o corte, OU declara-o aresta P1.4 visível a todos
             os ramos que atravessa. Ignorá-lo é proibido.
3  Declara o formalismo que sustenta a exaustividade do nó:
      algébrico · booleano · regra-100% · A/não-A  → sem residual
      nenhum (categorias presumidas)               → RESIDUAL NOMEADO,
                                                     obrigatório, nunca «Outros»
4  Triagem (P1.5): variação de 10× muda a decisão final?
      não           → poda visível, razão registada (P1.6)
      não sei       → `suspenso: por dimensionar`. NÃO podes podar.
      >½ dos irmãos suspensos → a raiz está errada. Reformula a raiz,
                                não recolhas mais dados.
5  Compara ramos só entre irmãos com a mesma granularidade.
   Subdividir um ramo aumenta-lhe o peso percebido, sem mérito.
```

**Condição de morte:** a folha é uma hipótese falsificável com **uma** análise discreta, ou a causa foi localizada.
**Armadilha:** declarar exaustividade porque a regra a exige. A sensação de completude não correlaciona com completude.

---

#### ▸ CARTÃO B — DECISÃO · «qual destas»

**Ramos são alternativas; alternativas excluem-se.**

```
1  Duas árvores, eixos distintos sobre o espaço de opções.
2  Cada ramo recai sobre variável que ESTE decisor mexe.
   Alavanca enorme e imóvel elimina-se — não se estuda.
3  Profundidade desigual é alocação de esforço, não defeito.
   O defeito é o ramo raso desaparecer sem ficar registado que se
   decidiu não o aprofundar.
4  Triagem (P1.5) como no cartão A, com as mesmas três saídas.
5  Se a árvore depende do significado das opções → abre C primeiro e
   acopla por aresta. Não fundas (P1.7).
6  Nenhum ramo é declarado escolhido com discriminante por testar (P2.4).
```

**Condição de morte:** opção escolhida, com os ramos não escolhidos `podado` e razão registada.
**Armadilha:** a solução vem de fora da árvore mais vezes do que parece. Se o resultado não cabe em nenhum ramo, usa `escapar` — não o forces para dentro.

---

#### ▸ CARTÃO C — CARACTERIZAÇÃO · «que espécie de coisa é esta»

**Isto não é uma árvore. São eixos, e os eixos cruzam-se.**
Um objecto não se reparte pelos eixos: tem simultaneamente uma posição em cada.

```
1  Não compões eixos por níveis. Listas eixos, lado a lado.
2  DENTRO de cada eixo: ME e CE. As posições cobrem o espectro
   e não se sobrepõem.
3  ENTRE eixos: nenhuma exaustividade a exigir. O conjunto é aberto
   por desenho — acrescenta-se um eixo sem refazer nada.
4  Separa os dois registos de eixo:
      do real       → pode estar errado; corrige-se investigando
      da preferência → não pode estar errado; abre-se conversando
   A valência não é propriedade do facto: é relação entre facto e pessoa.
5  Em vez de exaustividade, CONSISTÊNCIA CRUZADA: cruza posições par
   a par, elimina as combinações incompatíveis, fica com o resto.
6  NÃO PODAR. NÃO PONDERAR. Não normalizar pesos — somar a 1 é afirmar
   uma exaustividade que não tens.
7  Um eixo derivável de outro sai (não-redundância).
```

**Condição de morte:** **saturação** — novas perguntas deixam de gerar eixos novos. Não é verificação de exaustividade; essa não é possível aqui.
**Output:** um **espaço de configurações consistentes**, não uma resposta. A pluralidade é o produto declarado, não uma falha.
**Acoplamento:** quando entregas a uma árvore de decisão, a saída provável é `recortar`, não `aprofundar` — mudaste o significado das opções.
**Armadilha:** ser tratada como decomposição do entregável. Essa é outra coisa (partes, com regra dos 100%) e pertence ao cartão A.

---

#### ▸ CARTÃO D — MANDATO · «o que é que eu quero, afinal»

**A estrutura não mede a preferência: constrói-a.** Trata-a como instrumento, não como espelho.

```
1  Raiz curta. Ancora em EXEMPLOS CONCRETOS, nunca em categorias
   abstractas. Analisar razões abstractas torna as opções mais
   parecidas entre si e privilegia o que se consegue dizer por palavras.
2  Teste WITI a cada nó: «porque é que isto é importante?»
      remete para outro objectivo → é MEIO, não fim → é REDE, não árvore.
        Tira-o daqui.
      não remete → é fim → fica.
3  NÃO PODAR. NÃO PONDERAR.
4  Mudar a meio da conversa é funcionamento, não avaria. Uma estrutura
   que não se mexe é mais provavelmente ancoragem do que estabilidade.
5  Esta é a única árvore cujo output alimenta P0. Sai dela com
   1–5 objectivos com slug e 2–3 não-objectivos por objectivo (P0.1, P0.2).
```

**Condição de morte:** saturação **e** discriminação — novas perguntas não geram eixos novos, **e** a estrutura já separa as opções em cima da mesa. «Morre ao produzir o mandato» não é verificável; isto é.
**Bloqueio:** nenhuma frente abre antes de `P0.7` devolver verdadeiro (`P0.8`).
**Armadilha:** entregar um mandato cujos objectivos são meios uns dos outros. Quebra `P0.1`–`P0.2` a jusante e só aparece semanas depois.

---

#### ▸ CARTÃO E — NÃO USES ÁRVORE

Chegaste aqui por um destes: não há frase de fecho assinável; não conheces melhor as partes do que o alvo; a definição do problema muda a cada interlocutor; as ligações pesam mais que os elementos; o objecto é gosto, luto ou identidade.

**O trabalho ainda é sobre a FORMULAÇÃO.** Uma árvore construída agora é uma resposta à pergunta errada com aparência de rigor. Decompor aqui só empurra a incerteza para baixo.

```
Faz:
  · IS / IS-NOT sobre a fronteira do fenómeno
  · eixos abertos (cartão C), sem fechar nada
  · morfologia: parâmetros × posições, consistência cruzada par a par
  · sondas: intervenções pequenas e reversíveis, para ver o que responde
  · decompõe o espaço de ACÇÃO (intervenções candidatas), nunca o
    espaço CAUSAL

Não faças:
  · não podes podar — a poda é o erro caro aqui
  · não feches a definição do problema
  · não reduzas a duas opções
  · não trates isto como igual a um caso anterior já resolvido
  · não meças um substituto por o original não se deixar medir
```

**Saída deste cartão:** um **pressuposto** para o caminho (`P2.2`), com regra de paragem escrita antes de a frente abrir (`P2.3`). Não um ramo.
**Reentrada:** volta ao roteamento quando R0 passar a SIM. Só então.

---

### 6 · Se ficaste sem cartão

Estás em `Confused`. Decompor é aqui uma operação de **triagem** legítima e de **modelação** ilegítima: usa a decomposição só para descobrir em que caso estás, e não a guardes como árvore.

---

## 4 · Fontes

*Sem secção de fontes no relatório original.*
