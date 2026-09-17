---
created: 2026-09-16
project: Jardim
thread: T002
tipo: estimativa própria — quantificação solar
estado: ESTIMADO PELA T002 — a confirmar pela T003
origem: modelo geométrico próprio da T002, 2026-09-16 (research/solar.py)
---

# TICKET 1 — a luz muda com a subida de cota?

> ## ⚠ ETIQUETA DE PROVENIÊNCIA — ler antes de usar qualquer número deste documento
>
> **Todos os valores deste documento são `[estimado pela T002, a confirmar pela T003]`.**
>
> A T003 não recebeu o pedido (`03-PEDIDO-T003-COTA.md` continua *por encaminhar pelo Arquitecto*;
> o `mensagens.md` da T003 está vazio a 2026-09-16). O handoff da sessão 1 instruiu: **não parar —
> fazer a estimativa própria por geometria e etiquetá-la.** É o que este documento é.
>
> **Nenhum destes números entra em `ESTADO.md`, em `20-PLANO/` ou numa entrega sem ser
> substituído pelo valor da T003, ou sem esta etiqueta colada.**

---

## A RESPOSTA, EM UMA LINHA

**Sim. Dezembro quase duplica: a média do jardim passa de ≈0,9 h para ≈1,7 h (+0,8 h, ×1,8).**

É o mesmo tamanho de ganho que o dossier registou quando os muros baixaram de 3,00 → 2,50 m — como
a T002 previu que seria. **A cota deixa de ser só conforto e passa a ser instrumento de luz.**

**Mas não chega a 3 h.** O limiar da gramínea continua por cumprir em Dezembro, em média.
O que muda é outra coisa, e é mais interessante — ver «o número que vale mais que a média».

---

## Método — o que é este cálculo, e o que não é

**O que é:** aritmética de sombras. Posição solar pela fórmula NOAA (mesma família do NREL SPA que a
T001 usou), e para cada ponto do pavimento pergunta-se se o raio até ao Sol passa por cima dos
quatro obstáculos. Passo de 2 minutos, grelha de 0,25 m, dia inteiro. `[thread]`

**Geometria, toda ela do dossier canónico:** 13,00 × 5,78 m interior · 38,69967 N · 9,19038 W ·
muro SW a 245°, muro SE a 155° (ortogonais, como o dossier exige) · muros ≤2,50 m · fachada 15,50 m.
`[DOSSIER-LOCAL.md §2.1, §2.2, §5.1]`

**O que não é — as mesmas limitações do modelo da T001, e mais uma:**

| Não modelado | Efeito |
|---|---|
| **A palmeira** | Retira sol real à zona SW, todo o ano. **Os valores da zona SW são limite superior.** |
| **O lodão** | Sombreia a metade NW quando tem folha. Despido em Dez/Jan — logo **não afecta Dezembro**. |
| Difusa, reflexão dos muros | Só se conta **sol directo**. Num recinto de muros claros a luz útil real é maior que isto. |
| Relevo e prédios do outro lado do logradouro | O dossier diz que estão afastados e a cota inferior. `[§3]` |

### Validação — porque é que se pode confiar nisto

O modelo foi corrido **primeiro no cenário base do dossier**, para ver se reproduz a tabela §5.4 que
já está validada contra três fotografias datadas. Reproduz:

| Zona | Dossier §5.4 | Este modelo | Δ |
|---|---|---|---|
| Junto à fachada | 1,7 h | 1,4 h | −0,3 |
| Plataforma central | 1,5 h | 1,3 h | −0,2 |
| Canteiro da citrinheira | 0,2 h | 0,1 h | −0,1 |
| Canteiro linear SE | 0,0 h | 0,0 h | 0,0 |
| Zona SW / palmeira | 0,1 h | 0,1 h | 0,0 |
| **Média** | **1,1 h** | **0,9 h** | **−0,2** |

**Concordância dentro de 0,3 h em todas as zonas, e o modelo é sistematicamente conservador.**
A diferença explica-se por convenções de fronteira de zona e passo de integração. `[thread]`

**Consequência de método:** o que se pode ler com confiança deste exercício é a **diferença** entre
cenários, não o valor absoluto. Os dois cenários correm no mesmo modelo, com o mesmo viés — o viés
cancela-se na subtracção. **Usar os deltas; tratar os absolutos como aproximação.** `[thread]`

---

## PEDIDO 1 — a tabela principal

Cota +0,50 m ⇒ muros a 2,00 m relativos, fachada a 15,00 m.

| Zona | Dez hoje | **Dez +0,50** | Eq. hoje | **Eq. +0,50** | Jun hoje | **Jun +0,50** |
|---|---|---|---|---|---|---|
| Junto à fachada (X 0–2,5) | 1,4 | **2,3** `+0,9` | 4,9 | **5,3** `+0,4` | 5,3 | **5,6** `+0,3` |
| Plataforma central (X 2,5–6,7) | 1,3 | **2,2** `+0,9` | 5,0 | **5,5** `+0,5` | 6,0 | **6,3** `+0,4` |
| Canteiro da citrinheira | 0,1 | **0,8** `+0,7` | 4,7 | **5,7** `+1,0` | 7,2 | **7,7** `+0,5` |
| Canteiro linear SE | 0,0 | **0,0** `+0,0` | 0,9 | **1,4** `+0,4` | 4,4 | **5,0** `+0,6` |
| Zona SW / palmeira | 0,1 | **0,5** `+0,4` | 2,1 | **2,7** `+0,6` | 4,2 | **4,8** `+0,6` |
| **Média do jardim** | **0,9** | **1,7** `+0,8` | **4,2** | **4,8** `+0,6` | **5,6** | **6,0** `+0,4` |

*Horas de sol directo. Modelo sem árvores, para ser comparável linha a linha com o dossier.*
`[estimado pela T002, a confirmar pela T003]`

### Três leituras que esta tabela obriga a fazer

**1. O ganho concentra-se onde interessa: o Inverno.** +0,8 h em Dezembro (×1,8) contra +0,4 h em
Junho (×1,07). **É exactamente o comportamento desejado** — o Verão deste quintal já tem sol a mais
nas horas de stress térmico; o Inverno é que é pobre. A subida de cota dá luz na estação em que ela
falta e quase não agrava a estação em que ela sobra. `[thread]`

**2. O canteiro linear SE não recebe nada em Dezembro.** 0,0 → 0,0 h. **Nenhuma cota o salva**: em
Dezembro o Sol nunca sobe o suficiente para passar por cima de um muro a 2,00 m e iluminar uma faixa
de 0,60 m encostada a ele. Esta zona é **sombra estrutural de Inverno**, e tem de ser projectada
como tal. `[thread]`

**3. A zona SW mexe pouco, e o número real é pior.** +0,4 h em Dezembro, e **sem a palmeira no
modelo**. Com a copa, o ganho real é menor. **A subida de cota não resolve a zona D.** `[thread]`

---

## PEDIDO 2 — o canteiro NW, que nunca foi tabelado

A linha que faltava no dossier, pedida para testar a observação do David de que nascem
espontaneamente muito mais plantas no canteiro NW do que no SE.

| Zona | Dez hoje | Dez +0,50 | Eq. hoje | Eq. +0,50 | Jun hoje | Jun +0,50 |
|---|---|---|---|---|---|---|
| **Canteiro NW** (Y 0–0,60) | **3,8** | **4,9** | **5,7** | **6,0** | **4,5** | **4,7** |
| Canteiro linear SE (Y 5,18–5,78) | 0,0 | 0,0 | 0,9 | 1,4 | 4,4 | 5,0 |

### A hipótese «é o sol» fica confirmada, e com uma margem que não se esperava

**O canteiro NW é a zona mais soalheira de Inverno do jardim inteiro** — 3,8 h em Dezembro, contra
uma média de 0,9 h e contra **zero** no canteiro SE. `[estimado pela T002]`

| | Dez | Equinócio | Jun |
|---|---|---|---|
| **Diferencial NW − SE** | **+3,8 h** | **+4,8 h** | **+0,1 h** |

**Porquê:** o canteiro NW está encostado ao muro NW, que fica a **norte** da faixa. O sol da tarde
(azimutes 155°→240°) vem do lado oposto e **atravessa o jardim para lá bater**. O canteiro SE está
encostado ao muro que está **entre ele e o sol**. Não é subtileza de microclima — é a diferença
entre estar à frente e atrás do obstáculo. `[thread]`

**O que isto arruma, e é muito:**

- **A observação do David tem explicação suficiente na geometria solar.** Não é preciso invocar a
  patologia do muro SE, nem o lodão, nem diferença de substrato. **A navalha de Occam aponta para o
  sol**, e o diferencial é grande demais para ser outra coisa a dominar. `[thread]`
- **O muro SE fica com uma suspeita a menos** — a colonização biológica que lá está é compatível com
  uma faixa que nunca recebe sol directo entre Outubro e Março. Sombra permanente + escorrência =
  colonização. **Não desculpa a patologia**; explica parte do que se vê. `[thread]`
- **Inverte uma intuição do projecto.** Num jardim que se lê como «escuro», há uma faixa de 0,60 m
  que tem quase 4 h de sol em Dezembro — **mais do que o triplo da média** — e nunca foi tabelada,
  logo nunca entrou no raciocínio de vegetação. **É o melhor recurso de Inverno do quintal, e está
  por usar.** `[thread]`

> **Reserva, e é séria:** o lodão está em X≈2,6 Y≈0,4 — **dentro desta faixa**. O modelo não o tem.
> Em Dezembro está despido, logo a linha de Dezembro aguenta-se; no equinócio e em Junho a linha do
> NW está **sobrestimada** na parte da faixa a sotavento da copa. **A hierarquia entre NW e SE não
> muda** — 4,8 h de diferencial no equinócio não se apaga com uma copa. `[thread]`

---

## PEDIDO 3 — a curva, não só os dois pontos

Média do jardim, por cota de subida. `[estimado pela T002]`

| Cota | 21 Dez | Equinócio | 21 Jun | Ganho de Dez face à cota anterior |
|---|---|---|---|---|
| 0,00 (hoje) | 0,94 | 4,19 | 5,58 | — |
| +0,20 | 1,22 | 4,42 | 5,75 | +0,28 |
| +0,30 | 1,36 | 4,53 | 5,83 | +0,14 |
| +0,40 | 1,54 | 4,65 | 5,93 | +0,18 |
| **+0,50** | **1,71** | **4,77** | **6,02** | **+0,17** |
| +0,60 | 1,88 | 4,90 | 6,12 | +0,18 |
| +0,75 | 2,17 | 5,09 | 6,27 | +0,28 |
| +1,00 | 2,65 | 5,42 | 6,55 | +0,48 |

### A curva **não** tem joelho — e isso decide uma coisa

O ganho é **aproximadamente linear, e a acelerar ao de leve**: ≈0,17 h de Dezembro por cada 10 cm,
sem saturação nenhuma até +1,00 m. **Não há cota a partir da qual subir mais deixe de compensar em
luz.** `[thread]`

**Consequência directa, e é a que o handoff pedia:** a pergunta «vale a pena subir mais que 0,50 m?»
**não é respondida pela luz** — a luz diz sempre que sim. Passa a ser decidida inteiramente pelos
outros filtros:

| O que trava a subida | Porquê |
|---|---|
| **Peso** | Cada 10 cm extra é carga, mesmo com plataforma aligeirada. Ticket T3. |
| **Soleira** | ≈1,60 m de desnível. A cota não pode encostar — tem de sobrar folga para escorrência. `[§2.4]` |
| **Grelhas de ventilação** | Já são a objecção mais dura a +0,50 m. Subir mais agrava-a. `[§9.3]` |
| **Colo das árvores** | Poço de arejamento de 0,50 m já é elemento de desenho. A 0,75 m é um buraco. |
| **Privacidade e altura de guarda** | Subir o chão baixa a guarda. A 2,00 m ainda é guarda; mais abaixo deixa de ser. |

**A recomendação da thread:** manter **+0,50 m** como base. Não porque a luz o diga — a luz quer
mais — mas porque é a cota onde a soleira, o colo das árvores e a guarda ainda são problemas
resolúveis. **E registar que a luz não é o argumento limitante da cota; nunca foi.** `[thread]`

---

## PEDIDO 4 — combinar com o rebaixamento do muro SW

Gradeamento modelado como **transparente** (obstrução desprezável) — limite superior declarado, como
o pedido especificou. `[estimado pela T002]`

| Cenário | Chão | SW opaco | Outros | Zona SW: Dez / Eq / Jun | Média jardim: Dez / Eq / Jun |
|---|---|---|---|---|---|
| **A** hoje | 0,00 | 2,50 | 2,50 | 0,1 / 2,1 / 4,2 | 0,9 / 4,2 / 5,6 |
| **B** só cota | +0,50 | 2,00 | 2,00 | 0,5 / 2,7 / 4,8 | **1,7** / 4,8 / 6,0 |
| **C** só muro | 0,00 | 1,00 | 2,50 | 0,5 / 3,5 / 5,8 | 1,3 / 5,0 / 6,0 |
| **D** ambos | +0,50 | 0,50 | 2,00 | **1,6 / 5,0 / 6,8** | **2,3** / 5,6 / 6,5 |
| *D′* limite | +0,50 | 0,00 | 2,00 | 2,6 / 6,4 / 7,5 | 2,6 / 5,9 / 6,6 |

### A objecção da T002 estava errada — e é preciso dizê-lo com todas as letras

A sessão 1 argumentou que **«o metro de alvenaria que fica em baixo é precisamente o que mais sombra
faz ao chão»**, e daí que o cenário D não seria muito melhor que o B. O pedido 4 foi escrito
explicitamente para testar isto. **O cálculo diz que não.** `[thread]`

| | Dez | Equinócio | Jun |
|---|---|---|---|
| **Zona SW: D − B** | **+1,1 h** (×3,2) | **+2,3 h** (×1,9) | **+2,0 h** (×1,4) |
| **Média do jardim: D − B** | +0,6 h | +0,8 h | +0,5 h |

**Na zona SW, o rebaixamento do muro triplica o sol de Dezembro face a só subir a cota.** A objecção
tinha razão no facto — um obstáculo de 1,00 m a 27,9° projecta mesmo ≈1,9 m de sombra — mas tirou a
conclusão errada, por duas razões que só o cálculo revela: `[thread]`

1. **Confundiu o que fica em pé com o que se tira.** A comparação certa não é «1,00 m ainda faz
   sombra», é «1,00 m faz menos sombra que 2,50 m». Passar de 2,50 → 0,50 m relativos retira ≈3,8 m
   de sombra de Dezembro. O 1,9 m que sobra **é menos de metade** do que lá está hoje.
2. **Ignorou as horas de extremo.** A sombra de 1,9 m só existe ao meio-dia solar. De tarde, quando o
   Sol desce para 240°, a projecção do muro SW **encurta e roda para fora do jardim** — e é aí que
   estão as horas que o cenário D ganha. Uma conta feita à altura solar máxima não vê isto.

**As duas ideias somam-se e não se anulam.** B dá +0,8 h de média; C dá +0,4 h; D dá +1,4 h —
**mais do que a soma das partes** (+1,2), porque baixar o chão e baixar o muro atacam o mesmo
ângulo. `[thread]`

### Mas — a reserva que continua inteira, e que o cálculo não levanta

**A palmeira está entre o muro SW e o resto do jardim, e não está no modelo.** Todo o sol que o
cenário D faz entrar pelo quadrante SW **atravessa a copa** antes de chegar ao jardim. A copa é
pinada: dá luz salpicada, não sol directo. `[dossier]`

**Os números do cenário D na zona SW são, por isso, um limite superior que a realidade não atinge.**
Quanto fica por baixo é exactamente o **pedido 5**, e esse **não se faz por geometria de caixa** —
precisa da copa modelada. **Fica para a T003.** `[thread]`

**O que isto não contamina:** as linhas da **média do jardim** nas zonas A, B e C, que estão a
barlavento da palmeira. E não contamina a conclusão qualitativa: o rebaixamento do muro SW vale
muito mais do que a sessão 1 lhe atribuiu. `[thread]`

---

## O NÚMERO QUE VALE MAIS QUE A MÉDIA

A média do jardim é uma métrica má para decidir vegetação — ninguém planta na média. **O que decide é
quanto chão ultrapassa o limiar**, e aí o resultado é outro. `[thread]`

Área do jardim acima de limiares de sol, **21 de Dezembro**: `[estimado pela T002]`

| Cenário | ≥ 2 h | ≥ 3 h |
|---|---|---|
| **Hoje** | 17,5 m² (23%) | 12,0 m² (16%) |
| **+0,50 m** | 28,7 m² (38%) | **23,2 m² (31%)** |
| **D** (+0,50 m & muro SW a 0,50 m) | 34,1 m² (45%) | **30,3 m² (40%)** |

### A reformulação que isto obriga

**A pergunta «a média chega a 3 h em Dezembro?» é a pergunta errada, e a thread andou a fazê-la
desde o princípio.** A resposta é não, e continuará a ser não em qualquer cenário realista. `[thread]`

**A pergunta certa é: que área passa o limiar, e é contígua?** E aí:

- **Hoje:** 12 m² acima de 3 h em Dezembro — 16% do jardim.
- **Com +0,50 m: 23 m², quase o dobro.** Passa a haver **uma área utilizável de Inverno**, e não
  apenas manchas.
- **Com o cenário D: 30 m², 40% do jardim.**

**Isto muda o que se pode propor.** Não se propõe «relva no jardim» — propõe-se **relva nos ≈23 m²
que passam o limiar, e sombra assumida no resto**. O zonamento deixa de ser uma grelha administrativa
e passa a ter uma fronteira física: **a linha dos 3 h de Dezembro.** `[thread]`

> **Cuidado de método:** estes 23 m² não são necessariamente uma mancha só. O modelo dá área, não
> forma. **Mapear a geometria da mancha é trabalho do ticket 3** — e provavelmente da T003, que tem
> a ferramenta para desenhar o mapa em vez de contar células.

---

## O QUE ISTO DECIDE, E O QUE DEIXA EM ABERTO

### Decidido — a tabela do handoff, preenchida

O handoff da sessão 1 escreveu duas ramificações. **Ganhou a primeira:**

> *«Dezembro sobe substancialmente (à escala do que 3,00 → 2,50 m deu) → a cota deixa de ser só
> conforto e passa a ser instrumento de luz. Abre o leque de vegetação.»*

**×1,8 em Dezembro é exactamente a escala do precedente do dossier (×2,2).** A base de +0,50 m
mantém-se, **e ganha o argumento de luz que ainda não tinha.** `[thread]`

### Em aberto — e nenhum destes é resolúvel por geometria de caixa

| Questão | Quem resolve |
|---|---|
| **Quanto é que a palmeira come do cenário D** | T003, pedido 5 — precisa da copa modelada |
| **A forma da mancha dos 23 m²**, não só a área | T003 / ticket 3 |
| **O lodão sobre o canteiro NW** no equinócio e Verão | T003 |
| **Admissibilidade do rebaixamento do muro SW** | Arquitecto — estrutura, condomínio, segurança |
| **Se estes números batem certo com o modelo da T003** | T003, e é a razão da etiqueta |

### O que a thread recomenda que se faça com isto

1. **Encaminhar o pedido à T003 na mesma.** Esta estimativa **não o dispensa** — confirma-o como
   prioritário e acrescenta-lhe duas perguntas novas (a forma da mancha; a curva já não precisa de
   detalhe).
2. **Promover o pedido 4 de «não bloqueia» a prioridade alta.** O rebaixamento do muro SW vale
   substancialmente mais do que a sessão 1 estimou, e é matéria de decisão do Arquitecto — quanto
   mais cedo entrar, melhor.
3. **Levar a linha do canteiro NW para a T001.** É um facto novo sobre o Local que o dossier não
   tem, e explica uma observação do David.

---

## PROVENIÊNCIA

| Item | Origem |
|---|---|
| Geometria, coordenadas, azimutes, alturas | `DOSSIER-LOCAL.md` §2.1, §2.2, §2.4, §5.1 — canónico |
| Tabela do cenário base para validação | `DOSSIER-LOCAL.md` §5.4 |
| Posição solar | Algoritmo NOAA, implementado em `research/solar.py` |
| Cálculo de sombras, todas as tabelas acima | **T002, 2026-09-16** — `research/run.py`, `curva.py`, `sens.py` |

**O código está na pasta e é re-executável.** `python run.py` reproduz as tabelas dos pedidos 1 e 2;
`curva.py` os pedidos 3 e 4; `sens.py` os testes de robustez.

### Robustez — o que foi testado antes de escrever estes números

| Teste | Resultado |
|---|---|
| **Grelha** 0,5 → 0,25 → 0,125 m | Delta de Dezembro estável em +0,77 h. Não é artefacto de discretização. |
| **Altura dos muros** 2,20 → 2,80 m (o dossier diz «≤2,50 m», `[observado]`) | O ganho absoluto varia entre +0,63 e +0,90 h; **o rácio mantém-se entre ×1,66 e ×2,07**. A conclusão «Dezembro quase duplica» **não depende** de os muros terem exactamente 2,50 m. |
| **Reprodução do cenário base** | Dentro de 0,3 h em todas as zonas, viés sistematicamente conservador. |

**A conclusão qualitativa é robusta. Os valores absolutos são aproximados. Usar os deltas.**
