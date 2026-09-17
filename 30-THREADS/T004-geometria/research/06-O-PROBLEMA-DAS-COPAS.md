---
created: 2026-09-17
project: Jardim
thread: T004
tipo: problema de geometria — as copas
estado: ABERTO · bloqueia o desenho do jardim
origem: cálculo T004 sobre posições do dossier
---

# AS COPAS — metade do jardim está por baixo delas

> **Dois achados desta sessão, e o primeiro é urgente porque toca na obra que vai arrancar já.**

---

## 1. ⚠ O LODÃO ESTÁ ONDE O MACIÇO VAI SER CONSTRUÍDO

### O facto

| | |
|---|---|
| **Lodão** *(Celtis australis)* | **X ≈ 2,6 · Y ≈ 0,4** — encostado ao muro NW `[dossier §2.3, §8]` 🟡 |
| **Maciço** (plataforma + jacuzzi + escada) | **X de 1,50 a 3,25** |

```
   X=1,50        X=2,6         X=3,25
     │             │             │
 ────┼─────────────┼─────────────┼────  Y=0   MURO NW
     │ PLATAFORMA  │   MACIÇO    │
     │             │  ♣ LODÃO    │      ← o tronco está aqui dentro
     │             │             │
```

**O tronco do lodão fica dentro da faixa que vai ser construída.** `[T004]`

### Porque é que nenhum desenho o apanhou

**Nem os modelos 3D do David nem as plantas da T004 representam o lodão nessa faixa.** As plantas da
T004 desenham-no; mas a faixa do maciço foi definida em X, e a verificação de colisão com as árvores
não foi feita até agora. **É um falhanço de método desta thread, e assume-se.** `[T004]`

### As três saídas

| | O que implica | Custo |
|---|---|---|
| **A · A plataforma contorna-o** | O maciço recorta em Y ≈ 0–1,2. Perde-se área de plataforma junto ao muro NW | Área e complexidade de construção |
| **B · O lodão sai** | **É a árvore que dá sombra de Verão à metade NW — e sendo caduca, não tira sol no Inverno.** Perde-se um regime raro e valioso | Perde-se a zona 6 como a conhecemos |
| **C · Fica num vazio na plataforma** | Poço de arejamento. **Mas a plataforma está a +1,35 m** — seria um buraco de 0,85 m em volta do tronco | Detalhe construtivo difícil; risco para a árvore |

> **Não é decisão da thread. Mas condiciona a plataforma — que é a parte que o David quer construir
> já.** `[T004]`

### Porque é que o lodão vale a pena defender

A pesquisa de vegetação confirmou duas coisas: `[05-PESQUISA-VEGETACAO.md]`

- ***Celtis australis* tem raiz não invasiva** e é adequado a pátios urbanos — boa notícia para uma
  faixa de 1,00 m encostada a muro.
- **Sendo caduco, cria um regime raro:** sol no Inverno, sombra no Verão. É o padrão inverso do
  habitual, e é o que torna a zona 6 a candidata a **zona de floração de Inverno** — com
  *Iris unguicularis* e *Viburnum tinus*, que querem exactamente isso.

**Tirá-lo não é só perder uma árvore. É perder o que torna a zona 6 especial.** `[T004]`

---

## 2. AS COPAS COMEM METADE DO JARDIM

### O cálculo

Jardim livre do maciço: **56,4 m²** (X de 3,25 a 13,00 × 5,78).

| Cenário | Área sob copa | % | Jardim a céu aberto |
|---|---|---|---|
| Palmeira r≈3,1 + lodão r≈2,6 | **26,9 m²** | **48 %** | **29,4 m²** |
| Palmeira r≈3,5 + lodão r≈3,0 | 31,6 m² | 56 % | 24,7 m² |

*Áreas calculadas por integração sobre a planta, contando só a parte da copa que cai dentro do
jardim livre.* `[T004]`

### O que isto muda

**Metade do jardim não é «zona com x horas de sol» — é sob-copa**, com três condições diferentes:

| | |
|---|---|
| **Luz salpicada**, não sol directo | As tabelas de horas não a descrevem |
| **Competição radicular** | A palmeira compete por água em todo o raio `[dossier]` |
| **Folhada sazonal** | O lodão é caduco — cai tudo no Outono |

> ### O aviso de método que isto obriga
>
> **As tabelas de sol que esta thread tem usado correm SEM ÁRVORES.** `[estimado T002]`
>
> Para metade do jardim, **estão a descrever uma situação que não existe.** As zonas 4 e 6 são as
> mais afectadas — e a zona 6 é precisamente aquela a que a thread atribuiu **4,9 h em Dezembro, a
> melhor luz do quintal.**
>
> **Se o lodão for do tamanho que os modelos 3D sugerem, esse número está optimista.** Em Dezembro o
> lodão está despido, o que salva parcialmente a linha de Dezembro — **mas não as do equinócio e do
> Verão.** `[T004]`

---

## 3. O QUE ISTO FAZ ÀS MEDIÇÕES

**M1 e M1b deixam de ser detalhe e passam a ser o que decide o jardim.** `[T004]`

| # | O quê | Porquê agora |
|---|---|---|
| **M1** | **Copa da palmeira** — diâmetro e altura da base das palmas | Decide se o jardim a céu aberto tem 29 m² ou 25 m² |
| **M1b** | **Copa do lodão** — diâmetro, altura, e **distância exacta do tronco ao muro NW** | Decide as três saídas da §1 **e** se as 4,9 h da zona 6 se aguentam |

**Ambas são o item P2.2 do dossier, marcado 🔴, estimado em 1 hora.** `[dossier §12]`

### E há uma medição nova

| # | O quê | Porquê |
|---|---|---|
| **M5** | **Posição exacta do tronco do lodão em X e Y** | O dossier dá X≈2,6 · Y≈0,4 `[desenho]` 🟡 — **não medido**. Se estiver 40 cm mais para lá, o conflito com o maciço desaparece ou agrava-se |

---

## 4. A DUAS ALTURAS — a nota que falta

**A copa tem duas geometrias, e decidem coisas diferentes:** `[T004]`

| Geometria | O que decide |
|---|---|
| **Projecção no chão** | Área que compete por luz e por água |
| **Altura da base das palmas / dos ramos** | **Se por baixo se pode circular e estar** |

**Uma copa alta que cubra 20 m² não é a mesma coisa que uma copa baixa que cubra 20 m².** A primeira
dá espaço utilizável em sombra; a segunda é um obstáculo. **M1 e M1b têm de medir as duas.**

---

## PROVENIÊNCIA

| Item | Origem |
|---|---|
| Posição do lodão X≈2,6 · Y≈0,4 · raiz não invasiva · caduco | `DOSSIER-LOCAL.md` §2.3, §8 — 🟡 `[desenho]`, **não medido** |
| Posição da palmeira X≈11,6 · Y≈3,0 | `DOSSIER-LOCAL.md` §8 |
| Copa da palmeira transborda sobre o canteiro da citrinheira | `DOSSIER-LOCAL.md` §8 — base do raio ≥3,1 m estimado |
| **Colisão lodão × maciço · áreas sob copa · as três saídas** | **T004**, 2026-09-17 |
| Copas maiores do que o assumido | Modelos 3D do David, 2026-09-17 — leitura visual |
| Diâmetros de copa | 🔴 **P2.2 — nunca medidos** |
