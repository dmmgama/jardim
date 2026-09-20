---
title: "Arvore: definicao e uso no protocolo"
date: 2026-09-20
type: sintese
case: protocolo
tags: [MECE, arvore, protocolo, instrucao-operacional]
sobre:
  - "[[2026-09-20-audit-protocolo-criticas-definicao-de-arvore]]"
  - "[[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]]"
---

# Arvore: definicao e uso no protocolo

## 0 · Sumário executivo

- **Documento operacional**, para ser lido por agentes dentro de protocolos: roteamento primeiro, depois só o cartão do caso.
- Porta de entrada com cinco sinais de que **não se deve abrir árvore nenhuma**.
- Roteamento de quatro perguntas que **podem devolver mais do que um cartão** — é isso que responde a "de quantas árvores preciso".
- Tabela de combinações com ordem e acoplamento, incluindo a regra de que os ramos dependentes ficam `suspenso` em vez de esperar.
- **Concorrência de árvores só em problema e decisão.** Em caracterização e mandato acrescenta-se eixo, não se compete por ele.
- **Desempate entre concorrentes pela integridade do driver**, que é o critério de que este sistema mais depende, por toda a detecção ser travessia de arestas.
- Quatro cartões auto-suficientes, mais oito regras comuns.

---

## 1 · Mandato

Segundo dos dois relatórios pedidos após a leitura da pasta do protocolo:

> *"Cria uma definição de árvore e instruções de uso: tipificando casos e ajustando a estratégia de desenvolvimento de árvores e de utilização no contexto em que se inserem — o contexto do protocolo. Não sejas muito extenso: é para ser lido por agentes em protocolos, não pode carregar demasiado contexto. Tem de ser quase como um diagrama de fluxo, para que agentes não vejam os casos que não interessam: devem seguir o fluxo em que percebem o caso que têm pela frente e os tipos de árvore que precisam — uma ou mais."*

---

## 2 · Método

**Restrições de forma tratadas como requisitos duros**, não como preferências: economia de contexto, roteamento antes de conteúdo, e isolamento dos cartões.

**Vocabulário do protocolo** — ramo, aresta, poda, fecho, condição de morte, triagem, caminho, pressuposto, frente, slug, cone — com referência às regras `P1.x` onde relevantes, para que o documento seja invocável de dentro do sistema.

**Cada regra acrescentada é rastreável a uma crítica da auditoria**, e as correcções que retiram regras foram preferidas às que acrescentam, seguindo o critério do próprio protocolo de que o corpo de regras não deve crescer sem um modo de falha observado.

---

## 3 · Corpo do relatório

*A numeração abaixo é a do relatório original.*

> **Como ler.** Lê §0 e §1. Percorre §2 e anota os cartões que te saírem. Lê §3. Lê **só os cartões que te saíram** em §4 — não leias os outros. Lê §5. Ignora o resto.

---

### 0 · Definição

Uma árvore é uma **partição de um espaço por eixos**.
**Ramo** = unidade de trabalho. **Aresta** = dependência declarada. **Eixo** = critério de divisão.

Não é um plano — o plano é o **caminho**.
Não é um índice — o índice deriva do que existe.
Não é o entregável decomposto.

A árvore gera os cortes. O caminho testa-os.

---

### 1 · Porta de entrada: precisas de árvore?

Se **qualquer** destes for verdade, **não abras árvore**:

| Sinal | Para onde vai |
|---|---|
| A definição do problema muda a cada interlocutor | ainda é mandato ou rumo — não é árvore |
| Não consegues escrever a condição de morte | `P1.1` impede. Não abras |
| O que interessa só existe no todo (coerência, confiança, cultura) | não tem ramo possível |
| A causalidade tem retorno: X afecta Y que afecta X | cortar o ciclo **é** decidir. Outra representação |
| Decisão pequena e reversível | o custo de estruturar excede o valor. Decide |

Caso contrário, continua.

---

### 2 · Roteamento

Responde às quatro. **Podem sair-te várias.** É normal e é a resposta à pergunta "quantas árvores".

```
G1  Há um estado indesejado cuja causa se procura?
      sim ─────────────────────────────────────────► CARTÃO A · PROBLEMA

G2  O humano não consegue enunciar o que quer?
      sim ─────────────────────────────────────────► CARTÃO D · MANDATO
                                                      (abre antes de tudo; morre antes de tudo)

G3  Falta conhecer o objecto ou o terreno antes de se poder escolher?
      sim ─────────────────────────────────────────► CARTÃO B · CARACTERIZAÇÃO

G4  Há opções sobre a mesa entre as quais escolher?
      sim ─────────────────────────────────────────► CARTÃO C · DECISÃO
```

---

### 3 · Quantas, por que ordem, como acoplam

| Saiu | Árvores | Ordem | Acoplamento |
|---|---|---|---|
| só A | 1 propósito, **≥2 concorrentes** | — | — |
| só C | 1 propósito, **≥2 concorrentes** | — | — |
| B + C | 2 propósitos | **B primeiro**; C abre em paralelo com ramos suspensos | ramos de C ficam `suspenso: <ramo de B>`. Ao devolver resultado, C reavalia com **duas saídas apenas: aprofundar ou podar** |
| A + B | 2 propósitos | **B primeiro** quando a causa depende de terreno desconhecido | igual |
| D + qualquer | D isolada | **D morre primeiro**, produz o `MANDATO`, e **volta-se a §2** | nenhum — D não acopla |

**Concorrência.** Em **A** e em **C** abrem-se sempre duas ou mais árvores com eixos conceptuais distintos: uma árvore só é inércia, não é escolha. A triagem mata as estéreis.
Em **B** e em **D** **não há concorrência** — nestas acrescenta-se eixo, não se compete por ele. Duas árvores de caracterização sobre o mesmo objecto são redundância, não alternativa.

**Desempate entre concorrentes**, por ordem: (1) **integridade do driver** — vence o corte que mantém o driver provável inteiro dentro de um ramo, em vez de o repartir; (2) assimetria esperada; (3) accionabilidade.
*Um ramo com arestas para todos os irmãos é driver mal alojado, ou transversal por declarar (R5).*

**Nunca se fundem** (`P1.7`). Acoplam-se por dependência declarada (`P1.4`).

---

### 4 · Cartões — lê só o teu

#### CARTÃO A · PROBLEMA — *porque é que isto acontece*

**Antes de ramificar:** escreve o contraste. Onde o problema **está** e onde **podia estar e não está**; quando sim e quando não. Esgotar o contraste é mais barato do que qualquer ramo e elimina metade deles.

| | |
|---|---|
| **Raiz** | pergunta fechada: *porque é que `<estado indesejado>`* |
| **Eixo** | um por nó (`P1.2`). Escolhe o que mantém o driver inteiro num ramo |
| **ME / CE** | ambos, **estritos, dentro do eixo** |
| **Triagem** | **sim** (`P1.5`): se este ramo variasse dez vezes, mudava a decisão? Não → poda |
| **Ordem de ataque** | primeiro as análises que eliminam ramos inteiros, depois as que refinam |
| **Folha** | hipótese falsificável por **uma** análise discreta. Se não é, ramifica mais |
| **Profundidade** | desigual é priorização, não defeito |
| **Poda** | `P1.6`, com razão |
| **Morte** | causa identificada e confirmada; **ou** cone prioritário esgotado sem causa → escala |
| **Entrega ao caminho** | a causa, como pressuposto testável |

---

#### CARTÃO B · CARACTERIZAÇÃO — *o que é este objecto*

**Os ramos de primeiro nível não são partes. São eixos.** Partes somam-se; eixos cruzam-se — o objecto tem simultaneamente uma posição em cada.

**Declara dois registos, separados e nunca misturados no mesmo nível:**

| | **eixos do real** | **eixos de preferência** |
|---|---|---|
| Vêm de | domínios de conhecimento | da pessoa |
| Pode-se estar errado? | **sim** | **não** |
| Fecham-se por | investigação, medição | conversa |
| Falta um porque | ainda não se investigou | ainda não se descobriu que se queria |

| | |
|---|---|
| **Raiz** | o objecto, não uma pergunta |
| **ME / CE** | **dentro de cada eixo: ambos.** Entre eixos: **nenhum dos dois**. É assim que se lê `P1.3` aqui |
| **Forma** | aberta. Eixo novo é resultado, não defeito |
| **Triagem** | **não se aplica** — não há ainda decisão contra a qual triar. Substitui por: *este eixo discrimina entre as opções vivas?* |
| **Poda** | **proibida enquanto a árvore está aberta.** Ramo que não discrimina fica `suspenso`, nunca `podado` |
| **Morte** | **saturação**: dois ciclos consecutivos de investigação sem **nenhum eixo novo** — posições novas em eixos existentes não contam. Declara isto ao nascer (`P1.1`) |
| **Ao fechar** | verifica-se a exaustividade **dentro de cada eixo**, não entre eixos |
| **Entrega ao caminho** | **não entrega decisão.** Entrega significado: o que as opções passam a querer dizer neste contexto concreto |

**Teste de suficiência**, antes de declarar saturação: *consigo, só com estes eixos, descrever um objecto que seria claramente mau aqui, e distingui-lo do bom?* Se os dois recebem a mesma descrição, falta um eixo.

**Não atribuas pesos que somem 100%.** Somar a 1 é afirmar exaustividade que esta árvore não tem.

---

#### CARTÃO C · DECISÃO — *qual destas*

| | |
|---|---|
| **Raiz** | a escolha, com o **espaço de opções declarado** |
| **Eixo** | um por nó (`P1.2`) |
| **ME** | estrita entre opções irmãs |
| **CE** | sobre o **espaço declarado** ("dentro destas N opções"), nunca absoluta. Escreve o espaço |
| **Triagem** | **sim** (`P1.5`) |
| **Profundidade** | desigual é alocação de esforço. O ramo raso **fica registado** como não aprofundado — não desaparece |
| **Pesos** | **não normalizes.** Somar a 100% afirma exaustividade que não tens, e subdividir um ramo aumenta-lhe o peso independentemente do mérito. Decide por eliminação e dominância |
| **Se depende de B** | ramos ficam `suspenso: <ramo de B>`. Ao devolver: **aprofundar ou podar**, nada mais |
| **Morte** | opção escolhida, registada **com a alternativa rejeitada** |
| **Entrega ao caminho** | a opção, como caminho a executar ou como pressuposto a testar |

---

#### CARTÃO D · MANDATO — *o que é que eu quero, afinal*

**Diferença face a C: em C as opções existem e seleccionam-se. Aqui não existem — geram-se.**

| | |
|---|---|
| **Raiz** | o humano responsável |
| **Como se obtêm os eixos** | por **contraste entre exemplos concretos**, nomeados com as palavras do humano. Nunca por questionário. Pergunta *"o que é que este tem que aquele não tem?"* |
| **ME / CE** | dentro do eixo. Conjunto de eixos **aberto** |
| **Triagem** | **não.** É generativa. Podar aqui é podar o que o humano ainda não aprendeu a querer |
| **Profundidade** | desigual **é defeito** nesta árvore — nesta fase todos os ramos valem o mesmo |
| **Poda** | não se poda |
| **Morte** | **produz o `MANDATO` e morre.** Não sobrevive ao desbloqueio de `P0.7` |
| **Entrega** | o `MANDATO`. Depois **volta a §2** |

---

### 5 · Regras comuns

| | |
|---|---|
| **R1** | Um eixo por nó (`P1.2`). Compõem-se por níveis, nunca no mesmo nível |
| **R2** | ME e CE aplicam-se **dentro do eixo**. Entre eixos, nenhum dos dois |
| **R3** | A mesma pergunta da raiz à folha. Não se mistura "porquê" com "como". **O "como" é do caminho** — uma árvore de "como" é sinal de que o caminho não foi escrito |
| **R4** | Arestas declaradas **no acto de desenhar o ramo** (`P1.4`), nunca depois |
| **R5** | **Factor transversal:** se condiciona todos os ramos, não é ramo nem aresta. Declara-se `transversal` ao nível da árvore, com slug. Cone afectado = a árvore inteira. Se aparecer depois de a árvore estar desenhada, **redesenha-se, não se remenda** |
| **R6** | Condição de morte declarada ao nascer (`P1.1`). Sem ela, não abras |
| **R7** | Poda com razão registada (`P1.6`). A projecção mostra **quantos ramos foram podados e sob que eixo** — nunca a razão. O que se corta sem deixar rasto desaparece do âmbito sem ninguém decidir |
| **R8** | Árvores de propósito diferente não se fundem (`P1.7`). Acoplam por dependência declarada |

---

### 6 · Fecho

Um ramo que fecha devolve resultado ao caminho e o cone a jusante é recalculado por travessia das arestas.

**Uma árvore madura é maioritariamente morta.** O ramo aberto diz o que se está a fazer; o ramo morto diz o que não se voltará a fazer. É a segunda informação que impede a repetição de trabalho meses depois.

---

## 4 · Fontes

*Sem secção de fontes no relatório original.*
