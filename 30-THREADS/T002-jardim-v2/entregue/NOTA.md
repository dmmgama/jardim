---
created: 2026-09-17
project: Jardim
thread: T002
tipo: nota de entrega
estado: ENTREGUE — propõe fecho
sessoes: 2
---

# NOTA DE ENTREGA — T002 · Jardim V2

> **Regra T10.** Esta nota diz: o que é · como se usa · que decisões pede ao Arquitecto · o que
> ficou por fazer. **A thread não se declara fechada (T11)** — propõe o fecho.

---

## 1. O QUE É

O mandato pedia **duas a quatro opções viáveis**, atravessadas por cinco filtros.
**A thread não entrega opções. Entrega o que tornou as opções desnecessárias nesta forma.**

**Isto tem de ser dito com clareza, porque é um desvio ao mandato literal:** `[thread]`

Durante a sessão 2 o David trouxe uma **base de projecto completa** — não uma preferência entre
opções, mas o projecto ele próprio: a marquise sai, o envidraçado entra, a plataforma dá
continuidade à sala, a cota sobe 0,50 m, a palmeira é inegociável, e o zonamento é este. Produzir
«duas a quatro opções distintas» sobre uma base já escolhida pelo decisor seria **fabricar
alternativas para as rejeitar**.

**O que a thread fez em vez disso:** registou a base, testou-a contra os cinco filtros, calculou o
que estava por calcular, e **encontrou três erros — dois deles da própria thread**.

Esta questão de mandato foi levantada ao Arquitecto em `mensagens.md` em 2026-09-16 e **continua sem
resposta**. A entrega faz-se na interpretação declarada ali: *o leque mantém-se enquanto não houver
instrução*, mas o trabalho mostrou que **a base do David substituiu a necessidade de leque**.
`[thread]`

### O produto

| # | Ficheiro | O que é |
|---|---|---|
| **1** | `EXPLICACAO-DO-LOCAL.html` | **A peça principal.** 9 secções, 8 imagens embebidas, autónomo (2,1 MB). Cada afirmação etiquetada `David` / `foto` / `thread` / `dossier`. |
| **2** | `08-EXPLICACAO-DO-LOCAL.md` | O mesmo, em markdown. |
| **3** | `07-ZONAMENTO-DAVID.md` | **As seis zonas.** Grelha oficial, do David. |
| **4** | `05-LUZ-COTA-ESTIMATIVA-T002.md` | **A quantificação solar** da subida de cota. Estimativa própria, etiquetada. |
| **5** | `06-PROJECTO-REFORMULADO-VISTA.md` | Versão longa do enquadramento. |
| **6** | `TICKETS.md` | Pressupostos T1–T4 e três propostas de thread. |
| **7** | `solar.py` · `run.py` · `curva.py` · `sens.py` | **O modelo solar, re-executável.** Sem dependências externas. |
| **8** | `../David-Docs/INDICE.md` | Ficha das 13 imagens: o que é · serve · mostra · **não é** · liga a. |

**Nota de localização:** os ficheiros vivem em `research/`, não em `entregue/`. São documentos
vivos, com imagens ligadas por caminho relativo a `David-Docs/`; copiá-los partia as ligações e
criava duas versões a divergir. **`entregue/` contém esta nota, que é o índice da entrega.**
`[thread]`

---

## 2. COMO SE USA

**Para ler e perceber o projecto:** abrir `research/EXPLICACAO-DO-LOCAL.html` no browser. É
autónomo — não precisa das imagens ao lado.

**Para o Arquitecto absorver:** ver secção 3 desta nota.

**Para a thread seguinte:** ler o HTML, depois `07-ZONAMENTO-DAVID.md`. **Não é preciso reler o
dossier do Local** — o que interessa está destilado.

**Para refazer os números de sol:** `cd research && python run.py` (tabelas dos pedidos 1 e 2),
`python curva.py` (pedidos 3 e 4), `python sens.py` (robustez).

> ### ⚠ A etiqueta que não pode cair
>
> **Todos os valores de sol são `[estimado pela T002, a confirmar pela T003]`.** A T003 nunca
> recebeu o pedido — o `mensagens.md` dela está vazio. A thread fez a estimativa por geometria
> própria, como o handoff da sessão 1 instruía.
>
> **Nenhum destes números entra em `ESTADO.md` ou em `20-PLANO/` sem ser substituído pelo valor da
> T003, ou sem esta etiqueta colada.** `[REJEICOES.md §11]`

---

## 3. O QUE PEDE AO ARQUITECTO

### 3.1 Para absorver em `ESTADO.md`

| # | Matéria | Estatuto |
|---|---|---|
| **1** | **O projecto é fazer o jardim entrar na sala.** Marquise sai, envidraçado total recolhível, plataforma de continuidade a +1,35 m, gradiente de descida, jardim a +0,50 m. | Decisão do David, 2026-09-17 |
| **2** | **A palmeira é inegociável.** Dado fixo, não variável de projecto. | Decisão do David, 2026-09-17 |
| **3** | **O zonamento são seis zonas** — `07-ZONAMENTO-DAVID.md`. | Decisão do David, 2026-09-17 |
| **4** | **A laranjeira sai da posição actual.** Destino em aberto. **Janela Fev–início Mar 2027.** | Decisão do David, 2026-09-17 |
| **5** | **Princípios de V1 #2 e #5 estão provados em fotografia**, não são hipóteses. | Proposta da thread |
| **6** | **Objectivo declarado:** *«um jardim muito bonito de dia e cénico de noite»*. | Palavras do David |

### 3.2 Para registar em `REJEICOES.md`

| Matéria | Motivo |
|---|---|
| **Muro SW rebaixado como instrumento de luz** | O quadrante que ilumina é o da palmeira, que é inegociável. **Mantém-se em aberto** por vista e proporção — **cai** como argumento de sol. |
| **Piscina deslocada para SE** *(proposta da thread)* | Ignora que a descida se faz pela porta da sala, a única entrada do jardim. Retirada pela thread. |
| **Zonamento em quatro faixas + três camadas** *(proposta da thread)* | Substituído pelo do David. Histórico em `04-ZONAMENTO-PRESSUPOSTO.md`. |

### 3.3 Três decisões que só o Arquitecto pode tomar

| # | Pedido | Estado |
|---|---|---|
| **1** | **Criar a T004 — Geometria do Jardim.** Mandato redigido, a ratificar. Ver `PROPOSTA-T004.md`. | **Pedido do David, 2026-09-17** |
| **2** | **As três threads de `TICKETS.md`** — impermeabilização, peso por zona, afinação da cota. | Pedido em 2026-09-16, **sem resposta** |
| **3** | **Encaminhar o pedido à T003.** Ver 3.4. | Pedido em 2026-09-16, **sem resposta** |

### 3.4 Para passar à T003 — com uma prioridade alterada

O pedido está escrito em `03-PEDIDO-T003-COTA.md`. **Duas alterações que esta sessão obriga:**

| # | Alteração |
|---|---|
| **1** | **O pedido 5 (palmeira modelada) sobe de «só se já existir» a DECISIVO.** É ele que diz se o muro SW ainda vale alguma coisa, e quanto da zona 4 é utilizável. |
| **2** | **Acrescentar: a forma da mancha, não só a área.** A thread apurou que ≈23 m² passam as 3 h em Dezembro, mas dá área, não geometria. **A forma decide onde vai a relva.** |

### 3.5 Dois factos para a T001

Detalhe em `08-EXPLICACAO-DO-LOCAL.md` §5.

1. **A relva artificial existe e ainda lá está**, em placas descoladas sobre a betonilha. O dossier
   descreve betonilha à vista. **O Local está desactualizado.**
2. **Os muros podem não ter todos a mesma altura.** O David referiu 2,25 m; o dossier diz ≤2,50 m
   `[observado]`. **A 1,75 m relativos, Dezembro dá ≈2,3 h em vez de 1,7 h — 35% na variável mais
   crítica do projecto, resolvido com uma fita métrica.**

Fica também registado que o **padrão de fissuração diverge** entre duas imagens (rede fina em Out
2025, placas com juntas abertas em 2026) — já comunicado em 2026-09-16.

---

## 4. O QUE A THREAD APUROU — o essencial em cinco pontos

### 4.1 A luz muda com a subida de cota. Quase duplica em Dezembro

**Média do jardim: 0,9 h → 1,7 h (×1,8).** Mesma escala do precedente do dossier (3,00→2,50 m deu
×2,2). O ganho concentra-se no Inverno (+0,8 h) e mal toca em Junho (+0,4 h) — **a forma certa**,
porque o Verão já tem sol a mais nas horas de calor. `[estimado T002]`

**Robusto:** estável ao refinar a grelha; o rácio mantém-se entre ×1,66 e ×2,07 mesmo variando a
altura dos muros entre 2,20 e 2,80 m. Validado contra a tabela §5.4 do dossier — concorda dentro de
0,3 h em todas as zonas, sempre pelo lado conservador.

### 4.2 A pergunta certa não é a média — é a área que passa o limiar

**Ninguém planta na média.** `[thread]`

| 21 Dez | ≥3 h |
|---|---|
| Hoje | 12,0 m² (16%) |
| **+0,50 m** | **23,2 m² (31%)** |
| +0,50 m & muro SW a 0,50 m | 30,3 m² (40%) |

A média nunca chega a 3 h em cenário nenhum realista — **mas a área acima de 3 h quase duplica.**
A proposta deixa de ser «relva no jardim» e passa a «relva nos ≈23 m² que passam o limiar».
**O zonamento ganha uma fronteira física: a linha das 3 h de Dezembro.**

### 4.3 O canteiro NW nunca foi tabelado, e é a melhor luz de Inverno do quintal

**3,8 h em Dezembro (4,9 h com a cota), contra 0,0 h no canteiro SE.** Duas faixas que a planta
desenha iguais, em lados opostos, com **4,9 h de diferencial**. `[estimado T002]`

Explica a observação do David de que ali nascem plantas espontaneamente — **e ele já lhe chamava
«o canteiro onde crescem plantas» antes de haver número.** O muro SE fica com uma suspeita a menos:
sombra permanente + escorrência = colonização. **O musgo é sintoma, não causa.**

**É o recurso desperdiçado do projecto:** nunca entrou no raciocínio de vegetação de nenhum dos
quatro planos, e na planta tem sebe por cima.

### 4.4 Três erros corrigidos — dois da própria thread

| Erro | Quem | Correcção |
|---|---|---|
| **«O metro de alvenaria que fica em baixo é o que mais sombra faz — o cenário D não é muito melhor que o B»** | **thread** | **Falso.** Na zona SW, D **triplica** o sol de Dezembro face a B. A sombra de 1,9 m é real mas é menos de metade da actual, e só existe ao meio-dia solar. |
| **«A piscina devia ir para SE»** | **thread** | **Retirada.** Ignora o gradiente e a única descida. |
| **Medir a distância à palmeira pelo tronco** | **thread** | **Corrigido pelo David.** A copa é enorme e transborda sobre o canteiro da citrinheira — raio ≥3,1 m, **não cabe na largura do quintal**. Ver 5.1. |

### 4.5 Porque morreram quatro planos — a explicação que faltava

A leitura do Arquitecto era: V1 parou porque dependia de terceiros. **Verdade, e insuficiente.**
`[thread]`

> **Nenhum dos quatro planos tinha urgência, porque o jardim era invisível.**
>
> Um plano que depende de terceiros e que **ninguém vê falta** não é adiado — é abandonado sem
> decisão. A dependência explica **por que parou**; a invisibilidade explica **por que ninguém o
> retomou**.

**E é por isso que esta base é diferente:** a primeira coisa que faz é **tornar o jardim visível da
sala**. A partir daí o David passa a ser a pressão que nenhum plano anterior teve.

---

## 5. O QUE FICOU POR FAZER

### 5.1 O que interrompeu a sessão — e é o mandato da T004

A última pergunta da sessão foi do David: **a transição de cota não pode ser tão grande que fique
sem jardim, e entre ela e a palmeira tem de haver espaço.**

A thread fez a conta em X e concluiu que havia folga. **O David corrigiu: «a palmeira não se mede
até ao tronco, a copa é enorme.»** `[David, 2026-09-17]`

**A correcção é dupla, e a segunda parte é mais grave que a primeira:** `[thread]`

1. O raio usado (2,5 m) está errado — o dossier regista que a copa **transborda sobre o canteiro da
   citrinheira**, logo alcança X≈8,5: **raio ≥3,1 m**.
2. **Medir em X é o erro de método.** Uma copa de 6–7 m de diâmetro **não cabe nos 5,78 m de largura
   do recinto** — atravessa-o de muro a muro. **A palmeira não ocupa uma zona: ocupa uma secção.**

> **A reformulação do problema, que é o que a T004 herda:**
>
> **O jardim útil é o que fica entre o fim da transição e o início da copa. Essa faixa pode ser
> muito mais estreita do que qualquer planta em X sugere.**

**E o número que decide isto não existe:** o diâmetro de copa da palmeira está **🔴 por
inspeccionar** — item **P2.2** do dossier, estimado em **1 hora** de trabalho.

### 5.2 Por resolver, por ordem de urgência

| # | Questão | Porquê urge |
|---|---|---|
| **1** | **Medir a copa da palmeira** (diâmetro, altura da base das palmas) | **Bloqueia a T004.** Item P2.2, 1 hora. |
| **2** | **Laranjeira: para onde?** | **Janela Fev–Mar 2027.** Se passar, é 2028. Não depende de ninguém. |
| **3** | **Abrir o dreno + traçador** | Acção n.º 1 desde 2026-09-16. Agravada: a piscina põe ≈1,1 t sobre aquele canto. |
| **4** | **Fita métrica aos muros** | 35% na variável mais crítica. 20 min, mesma ida. |
| **5** | **A palmeira no modelo (T003)** | Decide o muro SW e a zona 4. |
| **6** | **Origem da água no muro SE** | 🔴. **Bloqueia a zona 2.** |

### 5.3 Do mandato original, o que não foi feito

| Item do mandato | Estado |
|---|---|
| Duas a quatro opções viáveis | **Não entregue.** Ver secção 1 — a base do David substituiu-as. **Questão de mandato sem resposta do Arquitecto.** |
| Rever os 8 princípios de V1 | **Parcial.** #2 e #5 resolvidos; #1 confirmado (palmeira). Os outros cinco por rever. |
| Custo a fazer e a manter | **Não feito.** Filtro 4 por aplicar. |
| Faseamento | **Parcial.** Identificadas as acções que não dependem de terceiros; sequência completa por fazer. |
| Identificar decisões que precisam de thread | **Feito.** Quatro propostas: T004 + as três de `TICKETS.md`. |

### 5.4 Os pressupostos que continuam pressupostos

**T1** drenagem · **T2** impermeabilização · **T3** redução de peso — assumidos por instrução do
David para o debate avançar. **Não verificados.** Se um cair, cai o que se construiu em cima.
`TICKETS.md`

---

## 6. PROPOSTA DE FECHO

A thread **propõe o fecho** (T10.3). O mandato foi exercido em duas sessões; o que dele resta —
opções, custo, faseamento — **depende da geometria que a T004 vai fixar**, e não se faz antes.

**Sugestão de sequência:** absorver esta entrega → ratificar a T004 → responder às três propostas de
thread de `TICKETS.md` → encaminhar o pedido à T003.

**Se o Arquitecto entender que o mandato exige as duas a quatro opções antes de fechar**, a thread
reabre e produz — mas regista que seria **construir alternativas a uma base já escolhida pelo
decisor**, e que o filtro 5 as rejeitaria todas. `[thread]`
