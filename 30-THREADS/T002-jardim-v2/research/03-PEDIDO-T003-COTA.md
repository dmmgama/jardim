---
created: 2026-09-16
project: Jardim
thread: T002
tipo: pedido de quantificação à T003
estado: por encaminhar pelo Arquitecto
---

# PEDIDO À T003 — o que muda na luz quando o jardim sobe 0,50 m

> **Via:** a T002 não escreve na pasta da T003 (T3). Este pedido vai ao Arquitecto em
> `mensagens.md`, para ele o encaminhar. Este documento é o enunciado técnico completo.
>
> **É o ticket n.º 1 da sessão 2 da T002.** Sem ele, o debate de vegetação é cego.

---

## A pergunta, em uma linha

**Subir o pavimento 0,50 m baixa todos os muros em 0,50 m relativos. Quanto sol é que isso dá?**

---

## Porque é que esta pergunta vale mais do que parece

O dossier da T001 já registou a sensibilidade: **baixar os muros de 3,00 → 2,50 m duplicou a média
de sol de Dezembro** (0,5 → 1,1 h), e quase não mexeu no Verão. `[dossier §5.4]`

A subida de cota é **um passo do mesmo tamanho, na mesma direcção** — 2,50 → 2,00 m relativos.

Se a relação se mantiver, Dezembro voltaria a subir substancialmente. **Se subir o suficiente, muda
o que é plantável.** Se não subir, a base de +0,50 m continua a valer pelo desnível da escada e pela
facilidade de obra, mas deixa de ser argumento de luz — e isso muda o que se pode propor.

**Não se pode escolher vegetação antes de saber isto.**

---

## Parâmetros

### O que muda

| Parâmetro | Cenário base (hoje) | Cenário +0,50 |
|---|---|---|
| Cota do pavimento | 0,00 (referência actual) | **+0,50 m** |
| Altura relativa do muro NW | 2,50 m | **2,00 m** |
| Altura relativa do muro SE | 2,50 m | **2,00 m** |
| Altura relativa do muro SW | 2,50 m | **2,00 m** |
| Altura relativa da fachada NE | 15,50 m | **15,00 m** |

### O que **não** muda

Geometria em planta (13,00 × 5,78 m interior) · coordenadas (38,69967 N · 9,19038 W) · azimute do
eixo longo (65°/245°) · plano da fachada a 155°.

### Cuidado a ter — a fachada também baixa

A fachada NE passa de 15,50 para 15,00 m relativos. **É irrelevante para o resultado** (uma fachada
de 15 m tapa a manhã exactamente como uma de 15,5 m), mas se o modelo for paramétrico convém que
seja coerente, não que fique com o pavimento subido e a fachada à cota antiga.

---

## O que se pede

### Pedido 1 — a tabela principal

A mesma tabela do dossier §5.4, para o cenário +0,50 m, com o cenário actual ao lado:

| Zona | Dez hoje | **Dez +0,50** | Eq. hoje | **Eq. +0,50** | Jun hoje | **Jun +0,50** |
|---|---|---|---|---|---|---|
| Junto à fachada (X 0–2,5) | 1,7 h | ? | 5,0 h | ? | 5,2 h | ? |
| Plataforma central (X 2,5–6,7) | 1,5 h | ? | 5,2 h | ? | 5,9 h | ? |
| Canteiro da citrinheira | 0,2 h | ? | 4,8 h | ? | 7,3 h | ? |
| Canteiro linear SE | 0,0 h | ? | 1,3 h | ? | 4,6 h | ? |
| Zona SW / palmeira | 0,1 h | ? | 2,1 h | ? | 4,2 h | ? |
| **Média do jardim** | **1,1 h** | **?** | **4,3 h** | **?** | **5,6 h** | **?** |

**Mesmas condições do modelo original: sem árvores.** Para ser comparável linha a linha.

### Pedido 2 — o canteiro NW, que nunca foi tabelado

**O dossier tabela o canteiro linear SE mas não tem linha equivalente para o NW.** `[dossier §5.4]`

Isto passou a importar por causa de uma **observação nova do David**: nascem espontaneamente **muito
mais plantas no canteiro NW do que no SE**. Uma das cinco hipóteses para o diferencial é
simplesmente **o sol** — e não se pode testar sem o número.

**Pede-se a linha do canteiro NW** (faixa junto ao muro NW, Y ≈ 0–0,60) nos dois cenários e nas três
datas.

**O que a resposta decide:** se o NW tiver sol claramente superior ao SE, a hipótese «é o sol»
explica a observação e o muro SE fica com uma suspeita a menos. Se tiverem sol semelhante, **a causa
é outra** — e as candidatas passam a ser a patologia do muro SE, o lodão, ou o substrato.

### Pedido 3 — a curva, não só os dois pontos

**+0,50 m é base de trabalho, não decisão final.** Para a thread de afinação da cota decidir bem,
é preciso saber onde está o joelho da curva.

**Média do jardim, por cota:** 0,00 · +0,20 · +0,30 · +0,40 · **+0,50** · +0,60 · +0,75

Nas três datas. **Uma linha por cota, sem detalhe por zona** — chega para ver a forma da curva.

**O que isto responde:** se o ganho for aproximadamente linear, cada centímetro conta e vale
discutir subir mais. Se saturar acima de certa cota, os 0,50 m podem ser mais do que o necessário —
e aí a cota decide-se pelo desnível da escada, não pelo sol.

### Pedido 4 — combinar com o rebaixamento do muro SW

A outra ideia em cima da mesa é **substituir a guarda opaca do muro SW por ≈1,00 m de alvenaria +
gradeamento**. As duas ideias somam-se: com o chão a +0,50 m, uma alvenaria de 1,00 m fica a
**0,50 m relativos**.

**Pede-se, para a zona SW e para a média do jardim, nas três datas:**

| Cenário | Chão | Muro SW opaco | Outros muros |
|---|---|---|---|
| A | 0,00 | 2,50 | 2,50 |
| B | +0,50 | 2,00 | 2,00 |
| C | 0,00 | 1,00 (+ grade) | 2,50 |
| **D** | **+0,50** | **0,50 (+ grade)** | **2,00** |

**Nota importante sobre o gradeamento:** modelar como **transparente** (obstrução desprezável) e
declarar esse pressuposto. Um gradeamento real com barrotes densos não é transparente, mas para
decidir se vale a pena vale como limite superior.

**A objecção que este pedido testa:** a thread T002 argumentou que **o metro de alvenaria que fica em
baixo é precisamente o que mais sombra faz ao chão** — a 27,9° de altura solar, um obstáculo de
1,00 m projecta ≈1,9 m de sombra. Se isto estiver certo, o cenário D não é muito melhor que o B, e o
rebaixamento do muro perde grande parte do seu argumento. **É um cálculo, não uma opinião — a T003
é que o resolve.**

### Pedido 5 — a palmeira, se o modelo já a tiver

**Só se já estiver modelada. Não atrasar os pedidos 1–4 por causa deste.**

A palmeira está **entre o muro SW e o resto do jardim**. Todo o sol que entre por um muro SW
rebaixado **atravessa a copa** antes de chegar ao jardim. Se o modelo já tiver a copa, pede-se o
cenário D **com e sem** palmeira — é a diferença entre «o rebaixamento dá sol» e «o rebaixamento dá
luz salpicada».

---

## Prioridade

| # | Pedido | Porquê |
|---|---|---|
| **1** | Tabela +0,50 m | **Bloqueia a sessão 2 da T002.** Sem isto não se define o que vai em cada zona. |
| **2** | Canteiro NW | Testa uma observação nova do David. Barato — é mais uma linha na mesma corrida. |
| **3** | Curva por cota | Alimenta a thread de afinação da cota. Não bloqueia. |
| **4** | Combinação com muro SW | Decide se o rebaixamento vale a pena. Não bloqueia, mas decide muito. |
| **5** | Palmeira | Só se já existir no modelo. |

**Os pedidos 1 e 2 são a mesma corrida do modelo com um parâmetro mudado.** Se o modelo estiver
montado, é trabalho de minutos, não de sessão.

---

## Uma nota sobre proveniência

A regra em vigor: **valores não se copiam entre threads sem `origem:` declarada.**
`[REJEICOES.md §11]`

A T002 **não copiou** nenhum valor da T003. Os números do cenário base citados aqui vêm todos do
`DOSSIER-LOCAL.md` §5.4, que é canónico. Os valores que a T003 devolver entram na T002 **com origem
declarada** — `origem: T003, modelo <versão>, data`.
