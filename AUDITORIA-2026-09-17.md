---
created: 2026-09-17
project: Jardim
tipo: governo — folha de auditoria
sessao: "2026.09.16 - T002 S2 e T004 S1"
---

# AUDITORIA — estado das quatro threads

> **Para o David auditar antes de prosseguir.** Uma folha por thread: o que lá está, o que está
> fixado, o que está por resolver, e **o que verificar**.
>
> **Regra de leitura:** só factos actuais. Onde há dúvida, o grau de confiança está declarado e diz
> se afecta ou não alguma decisão.

**Estado global a 2026-09-17:**

| Thread | Estado | Sessões | O que é |
|---|---|---|---|
| **T001 — Local** | `ONGOING` | 1 | Consulta e alimentação. Dossier canónico entregue |
| **T002 — Jardim V2** | **`FECHADA`** | 2 | Entrega absorvida em 2026-09-17 |
| **T003 — Modelo solar** | `ACTIVA`, **parada** | **0** | Nunca arrancou. **Ver divergência de mandato** |
| **T004 — Geometria** | `ACTIVA` ⚠ **urgente** | 1 | Caminho crítico da obra |

---

# T001 — LOCAL

**Pasta:** `30-THREADS/T001-local/` · **Estado:** `ONGOING` · **Sessões:** 1 (2026-09-15)

## O que lá está

| | |
|---|---|
| **Entrega** | `Docs-David-Local/DOSSIER-LOCAL.md` — **827 linhas, declarado canónico em `ESTADO.md` §01.** Versão HTML autónoma ao lado |
| `research/` | 9 ficheiros — catálogo vegetal (104 KB), viabilidade de relva (123 KB), software de modelação solar, estado da arte |
| `entregue/` | `NOTA-entregue-etapa1.md` |

## Papel actual

**Não é thread de trabalho activo.** É **consulta e alimentação**: responde a factos quando as outras
precisam, e recebe medições à medida que forem feitas.

## ⚠ O que tem de ser corrigido — três factos novos

| # | Facto | Onde está no dossier | Confiança | Afecta |
|---|---|---|---|---|
| **1** | **São DOIS lodões, não um.** O dossier §8 regista um *Celtis australis* (X≈2,6 · Y≈0,4) | §8 | **Alta** — fotografado em `JARDIM-LODAO1E2.jpg` | **Sim.** Muda o cálculo de sombra e de área |
| **2** | **A relva artificial existe e ainda lá está**, em placas descoladas sobre a betonilha | §7.1 descreve betonilha à vista | **Alta** — `ANTES-vista-esmagada-altura-NE.jpeg` | Não muda decisões. **O Local está desactualizado** |
| **3** | **Os muros podem não ter todos a mesma altura.** O David referiu 2,25 m; o dossier diz ≤2,50 m `[observado]` | §2.2 | **Média** — leitura fotográfica | **Sim, e muito.** A 1,75 m relativos Dezembro dá ≈2,3 h em vez de 1,7 h — **35% na variável mais crítica** |

**Também por registar:** o padrão de fissuração da betonilha diverge entre duas imagens (rede fina
em Out 2025; placas com juntas abertas em 2026). Comunicado em 2026-09-16.

## O que auditar

- [ ] O dossier continua a ser a fonte canónica? Nada o contradiz sem estar assinalado?
- [ ] Os três factos acima estão por incorporar — **confirmar que a T001 os recebe**
- [ ] `research/` tem material que nunca foi usado (catálogo vegetal, relva). **Ainda serve?**
- [ ] A etapa 2 tem 12 secções por instruir e 4 itens bloqueantes. **Continua a fazer sentido assim?**

---

# T002 — JARDIM V2

**Pasta:** `30-THREADS/T002-jardim-v2/` · **Estado:** **`FECHADA`** 2026-09-17 · **Sessões:** 2

## O que lá está

| | |
|---|---|
| **Peça principal** | `research/EXPLICACAO-DO-LOCAL.html` — 9 secções, 8 imagens embebidas, autónomo |
| `research/` | 13 ficheiros, incluindo o **modelo solar re-executável** (`solar.py`, `run.py`, `curva.py`, `sens.py`) |
| `David-Docs/` | **20 imagens** + `INDICE.md` com ficha de cada uma |
| `entregue/` | `NOTA.md` (nota de entrega) · `PROPOSTA-T004.md` (mandato da sucessora) |

## O que ficou fixado, e está em `ESTADO.md`

| # | Decisão |
|---|---|
| 1 | **O projecto é fazer o jardim entrar na sala.** Marquise sai, envidraçado total |
| 2 | **A palmeira é inegociável.** Dado fixo |
| 3 | **Seis zonas** — o zonamento do David |
| 4 | **A laranjeira sai.** ⚠ Janela Fev–início Mar 2027 |
| 5 | **A betonilha não se demole.** Cota +0,50 m por cima |
| 6 | **Quatro planos de cota** |
| 7 | **Princípios V1 #2 e #5 confirmados** — estão executados e fotografados |
| 8 | **Objectivo:** *«bonito de dia e cénico de noite»* |

## O desvio ao mandato, ratificado

O mandato pedia **2 a 4 opções viáveis**. **Não foram entregues.** O David trouxe uma base de
projecto completa, e produzir alternativas para as rejeitar seria teatro. **O Arquitecto ratificou**
— está em `THREADS.md` e em `entregue/NOTA.md`.

## O que ficou por fazer

| Matéria | Estado |
|---|---|
| **Custo a fazer e a manter** — o filtro 4 do mandato | **Nunca aplicado.** Não há orçamento de V2 |
| **Faseamento completo** | Parcial |
| **Cinco dos oito princípios de V1** (#3, #4, #6, #7, #8) | Por rever |

## Os números que a T002 produziu — e o seu estatuto

> **Todos os valores de sol são `[estimado pela T002, a confirmar pela T003]`**, de **modelo sem
> árvores**. Validados contra a tabela §5.4 do dossier: concordam dentro de 0,3 h em todas as zonas,
> sempre pelo lado conservador.
>
> **Confiança: média.** Servem para comparar cenários (os deltas são fiáveis); **não servem para
> dimensionar** (os absolutos são aproximados).

| | Dez | Eq. | Jun |
|---|---|---|---|
| Média hoje | 0,9 h | 4,2 h | 5,6 h |
| Média +0,50 m | **1,7 h** (×1,8) | 4,8 h | 6,0 h |
| **Área ≥3 h em Dezembro** | 12 → **23 m²** | — | — |
| Zona 6 (NW) | **4,9 h** | 6,0 h | 4,7 h |
| Zona 2 (SE) | **0,0 h** | 1,4 h | 5,0 h |

## O que auditar

- [ ] A entrega está completa e legível? O HTML abre e faz sentido sozinho?
- [ ] `David-Docs/INDICE.md` cobre as 20 imagens?
- [ ] **A thread está fechada mas os ficheiros continuam em `research/`** — é assim que se quer, ou
      devia haver limpeza?
- [ ] O `TICKETS.md` tem **duas propostas de thread por criar** (impermeabilização, peso por zona).
      **Ainda se querem?**

---

# T003 — MODELO SOLAR

**Pasta:** `30-THREADS/T003-modelo-solar/` · **Estado:** `ACTIVA` · **Sessões: 0 — nunca arrancou**

## O que lá está

| | |
|---|---|
| `modelo/` | `contrato-de-dados.yaml` · `parametros-activos.yaml` · `PONTE-DADOS.md` |
| `research/` | 3 ficheiros — pacote de arranque, plano de sessão |
| `mockups/` | `layouts-jardim.html` |
| `entregue/` | **vazio** |
| `mensagens.md` | **vazio — nunca recebeu o pedido da T002** |

## ⚠ DIVERGÊNCIA DE MANDATO — a resolver antes de arrancar

**O mandato escrito em `thread.md` diz:**

> «Construir e manter um **modelo digital paramétrico** do quintal» — geometria por variáveis,
> cálculo solar, mover árvores e testar posições, sensibilidade a parâmetros incertos.
>
> **E declara explicitamente:** *«Medição no terreno — T003 consome medições, não as produz.
> As medições são de T001.»*

**O David descreveu a T003 em 2026-09-17 como:**

> *«T003: levantamento preciso e plano para recolher toda a informação que falta.»*

> ### São duas coisas diferentes
>
> **Modelo paramétrico** ≠ **levantamento e plano de recolha**. O mandato actual exclui
> explicitamente a medição.
>
> **Isto é decisão do Arquitecto:** ou se reescreve o mandato da T003, ou se cria uma thread nova
> para o levantamento e a T003 mantém-se como modelo. **Não avançar sem resolver.**

## O pedido que a T003 nunca recebeu

`../T002-jardim-v2/research/03-PEDIDO-T003-COTA.md` — cinco pedidos de quantificação solar.
**Duas alterações desde que foi escrito:**

1. **O pedido 5 (palmeira modelada) subiu a DECISIVO** — decide quanto da zona 4 é utilizável.
2. **Acrescentar: a forma da mancha dos 23 m²**, não só a área.

**Nota:** a T002 acabou por fazer a estimativa por geometria própria, porque o pedido nunca chegou.
**O modelo da T002 existe e é re-executável** — a T003 pode partir dele em vez de começar do zero.

## O que auditar

- [ ] **Resolver a divergência de mandato.** É a decisão mais importante desta auditoria
- [ ] O `contrato-de-dados.yaml` e o `PONTE-DADOS.md` continuam válidos?
- [ ] **Faz sentido a T003 recomeçar do zero**, tendo a T002 produzido um modelo que funciona?

---

# T004 — GEOMETRIA ⚠ URGENTE

**Pasta:** `30-THREADS/T004-geometria/` · **Estado:** `ACTIVA` · **Sessões:** 1 (2026-09-17)

**Porquê urgente:** *«há URGÊNCIA pq essa parte da plataforma e construção civil é o que vai ocorrer
já agora»* `[David, 2026-09-17]`

## O que lá está

| | |
|---|---|
| `research/` | **13 ficheiros** — 7 documentos numerados, 3 HTML com peças cotadas, 3 scripts de desenho |
| `David-Docs/` | 2 modelos 3D do David |
| `entregue/` | **vazio** — a thread ainda não entregou |

**Peças desenhadas:** `PLANTA-TRANSICAO.html` · `DUAS-TRANSICOES.html` · `VARIANTE-C-MACICO.html`

## O que está FIXADO — a transição

| Cota | O quê |
|---|---|
| **+1,350** | Sala · plataforma · **superfície da água** — os três ao mesmo nível |
| **+0,925** | **Degrau-banco** — assento a 42,5 cm do jardim, 0,45 m fundo, 3,10 m |
| **+0,650** | Base do jacuzzi (1,75 × 1,75 × 0,70) |
| **+0,500** | Jardim, sobre a betonilha mantida |

| | |
|---|---|
| **Escada** | 6 degraus de 0,1417 m · cobertor 0,35 · Blondel 0,633 — **dentro do DL 163/2006** |
| **Maciço** | 1,75 m de profundidade · **1,60 m³ de vazio técnico contínuo** entre jacuzzi e escada |
| **Jardim que sobra** | **≈55,0 m²** |

**Confiança: alta.** É geometria calculada sobre cotas do dossier. **Não depende das medições em
falta.**

## O que está como REFERÊNCIA — as árvores

**Valores do David, inferidos de fotografias, fixados em 2026-09-17.** Substituem os do dossier.

| Árvore | Ø copa | Base da copa | Confiança |
|---|---|---|---|
| Palmeira | 5,0 m (4,5–6,0) | estipe 1,0–1,8 m | ±20% |
| Lodão 2 | 7,5 m nominal | 1ª ramificação 2,5–3,5 m | ±15% copa · ±25% altura |
| Lodão 1 | 8–10 m | 3,0–4,0 m | ±30% |

### O resultado principal

| | Sob copa | **A céu aberto** |
|---|---|---|
| **Verão** | 66% | **19,0 m²** |
| **Inverno** | 31% | **38,8 m²** |

> **O jardim troca de natureza duas vezes por ano.** Não é sombrio — dá sombra no calor e sol no
> frio. **As bases de copa (1,5–3,5 m) determinam que se passa por baixo das três:** sob-copa é
> sombra com pé-direito, não obstáculo.

**⚠ Confiança: média-baixa, e a banda é larga.** Com os mínimos das bandas, o céu aberto de Verão vai
a ≈29 m²; com os máximos, a ≈16,5 m². **Quase o dobro.**
**Afecta:** chega para saber que o Verão é sombrio; **não chega para dimensionar plantação.**

## O que NÃO está feito

| | |
|---|---|
| **Geometria do jardim zona a zona** | **Não feito.** Depende das medições |
| **Escolha de espécies** | Recolha com fontes em `05-PESQUISA-VEGETACAO.md`. **Não decidido** — é matéria de projecto, não de geometria |
| **Entrega** | `entregue/` vazio. É o trabalho da sessão 2 |

## Reservas registadas

| # | Reserva | Afecta |
|---|---|---|
| **1** | **A escada encosta ao muro SE**, cuja patologia tem origem desconhecida 🔴 | **A ordem da obra.** A escada não pode ser a primeira coisa; a plataforma pode |
| **2** | **A carga mudou de natureza** — ≈2,6 t apoiam-se sobre uma caixa oca, não no chão | Dimensionamento (do David) |
| **3** | **O lodão 1 está na faixa da plataforma** | Resolve-se com recorte. **Vale 6% do jardim** — a decisão é da caixa de esgotos, não do jardim |
| **4** | **Ventilação do vazio técnico** obrigatória | Detalhe construtivo |

## O que auditar

- [ ] As peças HTML abrem e as cotas fazem sentido?
- [ ] **`research/` tem 3 scripts `_planta*.py`** — ficam ou saem na arrumação?
- [ ] Os ficheiros numerados 01–07 têm sobreposição entre si (04 repete partes de 01 e 03).
      **Consolidar na sessão 2?**
- [ ] A pesquisa de vegetação (05) **excede o mandato de geometria**. Fica aqui, vai para
      `40-PESQUISAS/`, ou para outra thread?

---

# O QUE ATRAVESSA TODAS

## As medições — o produto lateral mais útil, por ordem de valor

| # | O quê | Decide | Custo |
|---|---|---|---|
| **M1a** | **Ø de copa do lodão 2** | 35% da área de Verão. **O número mais valioso** | fita |
| **M1b** | **Ø de copa da palmeira** + altura do estipe | 31% da área e o pé-direito sob copa | fita |
| **M5** | **Posição dos quatro troncos** — 8 medidas | Fecha a planta | fita |
| **M2** | **Altura dos muros**, troço a troço | 2,25 ou 2,50 m — **35% na luz de Dezembro** | fita |
| **M3** | Cotas: soleira, patim, jardim | Confirma a transição | fita/nível |
| **M4** | O vão do jacuzzi e o que está por baixo | Antes de lá pôr ≈2,6 t | fita |
| **M1c** | Ø de copa do lodão 1 | Só 6% do jardim — **interessa para a fachada** | fita |
| — | **Traçador no dreno** | **Acção n.º 1 do projecto** | <10 € |

**Todas numa ida.** O dossier estima as copas em 1 hora (item P2.2 🔴).

## Os prazos

| | Quando | Depende de |
|---|---|---|
| **Abertura junto à caixa de esgotos** — decide o lodão 1 | **Semana de 21/09** | Só do David |
| **Transplante da laranjeira** | **Fev–início Mar 2027.** Se passar, é 2028 | Só do David |
| **Construção civil** | **«já agora»** — por confirmar | Terceiro |

## Os pressupostos que continuam pressupostos

**T1 drenagem · T2 impermeabilização · T3 redução de peso** — assumidos por instrução do David para
o debate avançar. **Não verificados.** `T002/TICKETS.md`

## Pendentes de governo

- [ ] **Duas threads propostas e nunca criadas:** impermeabilização sobre betonilha; redução de peso por zona
- [ ] **O pedido à T003 nunca foi encaminhado**
- [ ] **`Jardim.html`** — território do Arquitecto, **desactualizado** face às decisões de 2026-09-17
- [ ] **Orçamento de V2** — o filtro 4 nunca foi aplicado
