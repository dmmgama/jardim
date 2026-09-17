---
created: 2026-09-17
project: Jardim
thread: T004
tipo: TEMPORÁRIO — instruções de sessão
estado: por executar
---

# ⚠ FICHEIRO TEMPORÁRIO — APAGAR NO FIM

> **Este ficheiro existe só para esta sessão.**
>
> **A última acção da sessão é apagar este ficheiro.** Se ele ainda cá estiver, a sessão não acabou.
>
> Escrito pela sessão `2026.09.16 - T002 S2 e T004 S1`, a pedido do David.

---

## O QUE ESTA SESSÃO É

**Sessão 2 da T004 — arrumação e fecho. É a última.**

**Antes de mexer em nada:** dá o estado ao David e **valida com ele o mandato desta sessão**.

**Ler primeiro:** `AUDITORIA-2026-09-17.md` na raiz — secção **T004** e secção **ARRUMAÇÃO**
(partes **B**, **C** e **F**).

> **Fazer a T002 primeiro, se ainda não foi feita.** As imagens que ela fica com ficha são as que a
> peça final desta thread vai citar — renomear depois parte as referências.

---

## AS SETE TAREFAS

### 1 · Consolidar os sete documentos em três

**Os numerados sobrepõem-se, e dois estão superados:**

| Ficheiro | Estado |
|---|---|
| `01-O-DESNIVEL-ENUNCIADO.md` | Os dados do jacuzzi repetem-se em 03, 04 e 07 |
| `02-PESQUISA-TRANSICOES.md` | Válido — pesquisa com fontes |
| `03-SOLUCAO-TRANSICAO.md` | **Superado por 04** — a geometria mudou com o maciço |
| `04-TRANSICAO-FIXADA.md` | Válido, mas repete partes de 01 e 03 |
| `05-PESQUISA-VEGETACAO.md` | Válido — **excede o mandato, ver tarefa 4** |
| `06-O-PROBLEMA-DAS-COPAS.md` | **Superado por 07** — os valores do David substituíram os cálculos |
| `07-ARVORES-POSICAO-E-COPAS.md` | Válido |

**Proposta:**

| Novo | Absorve |
|---|---|
| `01-A-TRANSICAO.md` | 01 + 03 + 04 |
| `02-AS-ARVORES.md` | 06 + 07 |
| `03-PESQUISAS.md` | 02 + 05 |

**O que se ganha:** três documentos em vez de sete, sem repetições.
**O que se perde:** o rasto de como se lá chegou. **É aceitável** — o David pediu factos actuais.

### 2 · Uma peça HTML final

**Três HTML, dois superados:**

| Ficheiro | Estado |
|---|---|
| `PLANTA-TRANSICAO.html` | **Superado** — geometria anterior ao maciço |
| `DUAS-TRANSICOES.html` | **Superado** — as variantes A e B foram postas de lado |
| `VARIANTE-C-MACICO.html` | **Actual, mas incompleto** |

> ### ⚠ O degrau-banco não está desenhado em peça nenhuma
>
> Foi a **última decisão da sessão 1**, tomada depois do `VARIANTE-C-MACICO.html`:
>
> | | |
> |---|---|
> | Assento | **+0,925** — 42,5 cm acima do jardim |
> | Profundidade | 0,45 m |
> | Desenvolvimento | 3,10 m, ao longo do maciço |
> | Custa ao jardim | 1,4 m² → **≈55,0 m²** |
>
> **A peça final tem de o incluir, em planta e em corte.**

**Fazer:** **um HTML só**, com a geometria actual, as árvores e as duas estações.
Os dois superados vão para `research/historico/` ou saem.

### 3 · Arrumar os scripts

`_planta.py` · `_planta2.py` · `_plantaC.py` — **os dois primeiros geram HTML superados.**

**Proposta:** manter só o que gera a peça final, renomeado `gerar-pecas.py`. Os outros saem.

### 4 · Sinalizar ao Arquitecto as pesquisas que excedem o mandato

> **Regra fixada pelo David em 2026-09-17:**
> **Cada thread guarda as suas pesquisas em `research/` da própria thread.**
> **Só o Arquitecto decide** se uma pesquisa sobe a `40-PESQUISAS/`.

`05-PESQUISA-VEGETACAO.md` — paleta para seis zonas, relva, iluminação — **excede o mandato de
geometria**. **Não a mover.** A thread não pode escrever fora da sua pasta (T3), nem lhe cabe julgar
o que é de interesse geral.

**Fazer:** escrever em `mensagens.md` que a thread produziu material transversal, e acrescentar a
linha a `THREAD-MENSAGENS.md`. **A decisão é do Arquitecto.**

*(`02-PESQUISA-TRANSICOES.md` é de geometria — está dentro do mandato, fica sem reservas.)*

### 5 · `entregue/` com `NOTA.md`

**Regra T10:** o produto final em `entregue/`, mais nota que diga **o que é · como se usa · que
decisões pede ao Arquitecto · o que ficou por fazer**.

**Tem de incluir a lista de medições, por ordem de valor** — é o produto lateral mais útil da thread
e **alimenta a thread seguinte**:

| # | O quê | Decide |
|---|---|---|
| **M1a** | Ø de copa do **lodão 2** | 35% da área de Verão. **O mais valioso** |
| **M1b** | Ø de copa da **palmeira** + altura do estipe | 31% da área e o pé-direito sob copa |
| **M5** | Posição dos quatro troncos — 8 medidas | Fecha a planta |
| **M2** | Altura dos muros, troço a troço | 2,25 ou 2,50 m — **35% na luz de Dezembro** |
| **M3** | Cotas: soleira, patim, jardim | Confirma a transição |
| **M4** | O vão do jacuzzi e o que está por baixo | Antes de lá pôr ≈2,6 t |
| **M1c** | Ø de copa do **lodão 1** | Só 6% do jardim — **interessa para a fachada** |

**E as reservas que não podem cair na entrega:**

1. **A escada toca o muro SE**, com patologia de origem desconhecida 🔴 — **não pode ser a primeira
   coisa da obra. A plataforma pode.**
2. **A carga mudou de natureza** — ≈2,6 t sobre uma caixa oca, não no chão.
3. **As copas são valores inferidos, não medidos.** Banda de incerteza quase dupla: céu aberto de
   Verão entre ≈16,5 e ≈29 m². **Chega para saber que o Verão é sombrio; não chega para dimensionar
   plantação.**

### 6 · Saldar a dívida T18/T20

As regras **T18–T22** entraram durante a sessão 1, que produziu documentos sem as cumprir.
**É dívida, não incumprimento retroactivo.**

**Documentos da T004 por registar:** os sete numerados (ou os três consolidados) + os HTML +
`entregue/NOTA.md`.

**Fazer:** tabela numerada ao David (T18), em lote · o que ele assinalar vai para o NotebookLM (T19)
· registar **todos** em `REGISTO-DOCUMENTOS.md` (T20).

### 7 · Propor o fecho

**T10.3** — pelo canal de mensagens. **T11: a thread não se declara fechada.**

---

## O QUE NÃO SE FAZ NESTA SESSÃO

| | Porquê |
|---|---|
| **Desenhar o resto do jardim** | Depende das medições que não existem |
| **Escolher espécies** | É matéria de projecto, não de geometria |
| **Mover a pesquisa de vegetação** | Só o Arquitecto a faz subir |
| **Reabrir a transição** | Está fixada |

---

## REGRAS DE ESCRITA

1. **Só factos actuais.** Nada de «pensava-se que era X, afinal é Y».
2. **Onde há dúvida:** grau de confiança declarado, e **se afecta ou não alguma decisão**.
3. **Os valores das árvores são do David, inferidos de fotografias** — referência de trabalho,
   **não medições**. Dizê-lo sempre.
4. **Os números de sol correm sem árvores.** Para as zonas sob copa descrevem uma situação que não
   existe.

---

## A ÚLTIMA ACÇÃO

**Apagar este ficheiro.**

Antes disso: `thread.md` actualizado, `entregue/` com a nota, fecho proposto em `mensagens.md`,
e a linha em `THREAD-MENSAGENS.md`.
