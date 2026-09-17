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
> ### A auditoria tem duas partes
>
> | | |
> |---|---|
> | **1 · Protocolo** | A thread cumpre as regras? Mandato, território, canal de mensagens, entrega |
> | **2 · Arrumação e conteúdo** | **Sabendo tudo o que lá está:** o que melhorar na estrutura do relatório final, que ficheiros renomear para ganhar clareza, o que consolidar, o que arquivar, o que eliminar |
>
> **A parte 2 é a que produz trabalho.** Está na secção **ARRUMAÇÃO** no fim deste documento,
> com propostas concretas thread a thread.
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

---

# ARRUMAÇÃO — propostas concretas

> **Esta secção é a parte 2 da auditoria.** Não é verificação: são **propostas de trabalho**,
> levantadas a partir do que está efectivamente nas pastas a 2026-09-17.
>
> **Nada aqui está decidido.** Cada proposta diz o problema, a proposta e o que custa.

---

## A · PROBLEMAS FACTUAIS ENCONTRADOS

### A1 · Oito imagens da T002 estão fora do índice

`David-Docs/INDICE.md` é a ficha de cada imagem — o que é, serve, mostra, **não é**, liga a.
**Oito das 20 imagens não têm ficha:**

| Imagem | O que é |
|---|---|
| `PLANTA-ARVORES-POSICAO.jpg` | **A planta de referência das árvores** |
| `PLANTA-ARVORES-POSICAO-COPAS.jpg` | **A planta das copas — base do cálculo das duas estações** |
| `JARDIM-LODAO1-A.jpg` · `-B.jpg` · `JARDIM-LODAO1E2.jpg` | **A prova de que são dois lodões** |
| `DEPOIS-VISTA -PALMEIRA.jpg` | Render de intenção |
| `DEPOIS-VISTA PARA FRACAO.jpg` · `(2).jpg` | Renders de intenção |

**Gravidade: alta para as cinco primeiras** — são as que suportam factos usados na T004.
**Proposta:** fichar as oito. Meia hora.

### A2 · O índice tem entrada para um ficheiro que não existe

`INDICE.md` descreve `Plano-Original-V2.jfif`. **O ficheiro não está na pasta.**

**Proposta:** recuperar o ficheiro, ou remover a entrada e dizer porquê.

### A3 · Nomes inconsistentes — três convenções na mesma pasta

| Convenção | Exemplos |
|---|---|
| MAIÚSCULAS-COM-HÍFENS | `PALMEIRA-ICONE-NOITE.jpg` · `ZONAMENTO-PLANTA-ZONAS.jpg` |
| Capitalizado | `Situacao-Atual.jpg` · `Plano-Original-V1.jpg` |
| minúsculas | `palmeira-icone.jpeg` |
| **Com espaços e parênteses** | `DEPOIS-VISTA -PALMEIRA.jpg` · `DEPOIS-VISTA PARA FRACAO (2).jpg` |

**Os nomes com espaços já obrigaram a aspas em comandos e são os que quebram ligações relativas.**

**Proposta de convenção:** `TEMA-SUBTEMA-QUALIFICADOR.ext`, MAIÚSCULAS, hífens, **sem espaços,
sem parênteses, sem acentos**.

**Custo:** renomear obriga a corrigir as referências em `INDICE.md`, nos `.md` de `research/` e
**dentro dos HTML** (que embebem as imagens em base64 — esses não partem, mas as legendas citam nomes).

### A4 · Um PDF de 17 MB em `T001/research/`

`Jardim_Relva_Natural_Viabilidade_slides.pdf` — **17 MB, 25% do peso da T001.**
É um deck gerado a partir de um `.md` que está ao lado.

**Proposta:** arquivar em `90-ARQUEOLOGIA/` ou eliminar. **O conteúdo está no markdown.**

### A5 · A T001 pesa 67 MB — 87% do repositório

| Thread | Tamanho |
|---|---|
| **T001** | **67 MB** |
| T002 | 6,3 MB |
| T004 | 2,4 MB |
| T003 | 264 KB |

`Docs-David-Local/` tem **52 ficheiros**, incluindo subpastas `arqueologia/` e `Claude outputs/`.

**Proposta:** inventariar o que ainda serve. **Não mexer sem o David decidir** — o dossier é canónico
e as ligações relativas são frágeis (foi por isso que se decidiu não o migrar).

---

## B · ESTRUTURA DO RELATÓRIO FINAL — T004

### B1 · Os sete documentos numerados sobrepõem-se

| Ficheiro | Problema |
|---|---|
| `01-O-DESNIVEL-ENUNCIADO.md` | Os dados do jacuzzi repetem-se em 03, 04 e 07 |
| `03-SOLUCAO-TRANSICAO.md` | **Superado por 04** — a geometria mudou com o maciço |
| `04-TRANSICAO-FIXADA.md` | Repete partes de 01 e 03 |
| `06-O-PROBLEMA-DAS-COPAS.md` | **Superado por 07** — os valores do David substituíram os cálculos |

**Proposta:** consolidar em **três documentos**:

| Novo | Absorve |
|---|---|
| `01-A-TRANSICAO.md` | 01 + 03 + 04 |
| `02-AS-ARVORES.md` | 06 + 07 |
| `03-PESQUISAS.md` *(ou sai da thread — ver C1)* | 02 + 05 |

**O que se ganha:** quem chegar de novo lê três documentos em vez de sete, sem repetições.
**O que se perde:** o rasto de como se lá chegou. **É aceitável** — o David pediu factos actuais,
não histórico.

### B2 · Três HTML, dois deles superados

| Ficheiro | Estado |
|---|---|
| `PLANTA-TRANSICAO.html` | **Superado** — geometria anterior ao maciço |
| `DUAS-TRANSICOES.html` | **Superado** — as variantes A e B foram postas de lado |
| `VARIANTE-C-MACICO.html` | **Actual** |

**Proposta:** **um HTML só, completo**, com a geometria final, as árvores e as duas estações.
Os dois superados vão para `research/historico/` ou saem.

> ⚠ **O degrau-banco não está desenhado em peça nenhuma.** Foi decidido depois do
> `VARIANTE-C-MACICO.html`. **A peça final tem de o incluir.**

### B3 · Três scripts `_planta*.py` em `research/`

`_planta.py` · `_planta2.py` · `_plantaC.py` — geram as peças. **Os dois primeiros geram HTML
superados.**

**Proposta:** manter só o que gera a peça final, renomeado `gerar-pecas.py`. Os outros saem.

---

## C · ÂMBITO — o que está na thread errada

### C1 · A pesquisa de vegetação — fica na thread

`T004/research/05-PESQUISA-VEGETACAO.md` — paleta para seis zonas, relva, iluminação.
**Excede o mandato de geometria da T004**, e está assinalado no próprio ficheiro.

> **Regra de governo, fixada pelo David em 2026-09-17:**
>
> **Cada thread guarda as suas pesquisas em `research/` da própria thread.**
> **Só o Arquitecto decide** se uma pesquisa sobe a `40-PESQUISAS/` por ser de interesse geral.

**Consequência:** a pesquisa **fica onde está**. A thread não a move — nem pode (T3), nem lhe cabe
julgar se é de interesse geral.

**O que a thread deve fazer:** sinalizar ao Arquitecto, pelo canal de mensagens, que produziu uma
pesquisa que excede o seu mandato e que **pode ser de interesse transversal**. A decisão é dele.

**O mesmo se aplica** às pesquisas da T001 (catálogo vegetal, viabilidade de relva, software de
modelação): **ficam na T001** até o Arquitecto decidir o contrário — mesmo sendo material que a T004
consultou e que outras threads vão consultar.

### C2 · A pesquisa de transições é de geometria

`02-PESQUISA-TRANSICOES.md` — tipologias com fontes. **Está dentro do mandato da T004.**
Fica, sem reservas.

### C3 · As imagens da T002 são usadas pela T004

A T004 cita `David-Docs/` da T002 em vários documentos. **Está correcto** (T4: pode ler tudo), mas
**cria dependência entre threads**: se a T002 for arquivada, a T004 perde as imagens.

**Proposta:** decidir se `David-Docs/` sobe a **`20-VISUAL/`** — material do David, não de uma thread.

---

## D · O QUE O DOSSIER PRECISA DE RECEBER

Já listado na secção T001. **Resumo do trabalho:**

| # | Facto | Onde toca |
|---|---|---|
| 1 | **São dois lodões** | §8 vegetação · §5.6 limitações do modelo |
| 2 | Relva artificial ainda existe | §7.1 superfícies |
| 3 | Muros podem não ter altura uniforme | §2.2 dimensões · **§5.4 toda a tabela de sol** |
| 4 | **Valores de copa do David** | §8 — substituem o que lá está |
| 5 | Padrão de fissuração diverge | §7.2 patologias |

**O #3 é o que dá mais trabalho:** se os muros forem 2,25 m, **a tabela de sol do §5.4 muda toda.**

---

---

## F · REGRAS NOVAS — T18–T22 (NotebookLM e registo de documentos)

**As quatro threads receberam regras novas** sobre NotebookLM e `REGISTO-DOCUMENTOS.md`, que
existe na raiz. **Confirmado presente nos quatro `CLAUDE.md`.**

### O que as regras obrigam

| Regra | O quê |
|---|---|
| **T18** | Ao produzir **research** ou **report**, perguntar ao David em tabela numerada quais enviar para o NotebookLM. Em lote, se vários ficarem prontos juntos |
| **T19** | Upload com nome `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>` + slide deck `detailed` em português |
| **T20** | No fim da sessão: verificar decks, descarregar PDF para junto do documento, **registar TODOS os documentos produzidos** em `REGISTO-DOCUMENTOS.md` — os que foram e os que não foram |
| **T21** | `REGISTO-DOCUMENTOS.md` é **append only**, leitura on demand |
| **T22** | Pode perguntar ao notebook em vez de ler. **Uma resposta do NotebookLM não é decisão** |

### ⚠ Dívida desta sessão

**A sessão de 2026-09-17 produziu documentos sob estas regras e não cumpriu T18 nem T20.**

**Documentos produzidos e não registados:**

| Thread | Documentos | Tipo |
|---|---|---|
| **T002** | `05-LUZ-COTA-ESTIMATIVA-T002.md` · `06-PROJECTO-REFORMULADO-VISTA.md` · `07-ZONAMENTO-DAVID.md` · `08-EXPLICACAO-DO-LOCAL.md` + HTML | RESEARCH / REPORT |
| **T004** | `01` a `07` + 3 HTML | RESEARCH / REPORT |

**Proposta:** a sessão 2 da T004 aplica T18 e T20 **retroactivamente** — apresenta a tabela numerada
ao David com todos os documentos das duas threads, e regista o que ele decidir.

**Nota de método:** as regras entraram durante a sessão; **não é incumprimento retroactivo, é dívida
a saldar.** Mas a partir de agora aplicam-se a todas as sessões.

## E · PROPOSTA DE SEQUÊNCIA

| Ordem | O quê | Onde |
|---|---|---|
| **1** | **Fichar as 8 imagens órfãs** e resolver a entrada fantasma | T002 — **rápido e desbloqueia o resto** |
| **2** | **Consolidar os 7 documentos em 3** | T004 sessão 2 |
| **3** | **Uma peça HTML final**, com o degrau-banco | T004 sessão 2 |
| **4** | **Sinalizar ao Arquitecto** as pesquisas que excedem o mandato da thread | T004 → canal de mensagens |
| **5** | **Convenção de nomes** e renomeação | Depois de 1–3, para não renomear duas vezes |
| **6** | **Incorporar os 5 factos no dossier** | T001 |
| **7** | **Arrumar o peso da T001** — PDF de 17 MB, 52 ficheiros | T001, sem pressa |
| **8** | **Saldar a dívida T18/T20** — tabela ao David, registar em `REGISTO-DOCUMENTOS.md` | T004 sessão 2 |

> **A ordem importa:** renomear antes de consolidar obriga a corrigir referências duas vezes.

