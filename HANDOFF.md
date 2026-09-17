---
created: 2026-09-14
updated: 2026-09-17
project: Jardim
tipo: governo
summary: |
  Continuidade entre sessões de Arquitecto. Onde ficou a sessão anterior e qual é o próximo passo.
---

# HANDOFF

> **Regra A4:** o Agente regista aqui, no fim da sessão, o estado e o próximo passo.

**Última sessão:** `2026.09.15 - Arquiteto` — sessão de Arquitecto puro, aberta a 2026-09-15 e
fechada a 2026-09-17. Commits `48d9d37`, `8029b2a`, `127e9f7`.

> ⚠ **AVISO SOBRE ESTE HANDOFF.** A sessão que o escreve esteve aberta dois dias e **ficou
> desactualizada a meio**. Entre o seu penúltimo commit e o fecho, cinco commits de outras sessões
> alteraram o projecto: abriu a T005, a T004 posicionou as árvores e fechou a sessão 1, e entraram
> **dois pedidos pendentes** no canal. **Este handoff regista o estado verificado no momento do
> fecho, não o que a sessão julgava saber.** O que ela própria fez está na secção 2; o resto foi
> lido do repositório, não da sua memória.

---

## 1. Estado no momento do fecho — verificado

| Thread | Estado | Situação |
|---|---|---|
| **T001 — Local** | `ONGOING` | Consulta e alimentação. Etapa 2 por instruir — quatro bloqueantes, todos < 10 € e uma tarde. **Dois factos novos por lhe passar** (ver §4). |
| **T004 — Geometria** | `ACTIVA` ⚠ **caminho crítico** | **Sessão 1 fechada.** Transição resolvida em geometria completa. Sessão 2 é a última e vai propor o fecho. |
| **T005 — Caracterização** | `ACTIVA` · `ONGOING` | **Fase 1 entregue.** Aberta depois desta sessão começar. |
| **T003 — Modelo solar** | `ACTIVA` | **Arrancada por esta sessão.** Pedido em mão, zero sessões próprias ainda. |
| **T002 — Jardim V2** | `FECHADA` | Entrega absorvida 2026-09-17. |

**Pedidos pendentes: dois. Ambos da T005, ambos de 2026-09-17.** Nenhum é desta sessão.

---

## 2. O que esta sessão fez

Três actos de governo, nenhum de projecto.

### 2.1 Absorveu a etapa 1 da T001 — `48d9d37`

O repositório tinha um dossier canónico de 827 linhas e o `ESTADO.md` continuava a dizer
«Local: em aberto, tudo». **A entrega não era decisão vigente.**

Três decisões de fundo:

| Decisão | Porquê |
|---|---|
| **O dossier fica onde está** — canon em `Docs-David-Local/`, não migra para `10-LOCAL/` | **Absorver ≠ mover.** Partir 25 ligações a ~50 imagens não compra nada. Passa a canon por estar declarado no `ESTADO.md`. |
| **Muro SW não se decide por despacho** — foi a debate na T002 | Era a primeira ideia genuinamente nova do projecto. Decidida isolada, produzia o quinto plano. |
| **Rejeições vegetais ficam no inbox** | São conclusões de projecto, não factos do Local. Registá-las era fechar por escrito o que não fora debatido. |

Criou `ESTADO.md` §11 e `REJEICOES.md` §11 (Modelo e simulação), em espelho.

### 2.2 Arrancou a T003 — `8029b2a`

**Descoberta ao abrir:** o `mensagens.md` da T003 estava **vazio**. O pedido de quantificação que a
T002 lhe escreveu a 2026-09-16 nunca foi encaminhado. A T002 acabou por construir um modelo solar
próprio em Python porque a T003 nunca respondeu.

Encaminhado, com duas alterações:
- **Pedido 5 (palmeira modelada) sobe a decisivo.** Sem a copa, o cenário do muro SW responde à
  pergunta errada — dá *quanto sol entraria* quando a pergunta é *quanto chega ao chão depois de
  atravessar a copa*.
- **Pedido 1 ganha forma e posição** da mancha de sol, não só área.

Âmbito alargado à **captura 3D com telemóvel**, por instrução do David.

### 2.3 A pesquisa de captura 3D contrariou o próprio pedido — `127e9f7`

| Alvo | Ferramenta | Erro |
|---|---|---|
| **Altura dos muros, troço a troço** | **Telémetro laser, 20–40 €** | **±1,5 mm** |
| **Copas** | LiDAR de iPhone Pro | dezenas de cm |

**O limiar crítico do projecto é 0,5 m.** Três ordens de grandeza de margem. Registado em
`ESTADO.md` §11 e `REJEICOES.md` §11.

> **A T005 refinou isto depois, e o refinamento manda.** Ver §3.

---

## 3. O que mudou depois, e que esta sessão não fez

Cinco commits de outras sessões. **Ler antes de agir.**

### 3.1 A T005 abriu e entregou a fase 1 — `fb07883`, `e8e8d2a`, `9645572`

**Achado central, e é grande:** três pesquisas lançadas em paralelo, com enunciados separados e sem
conhecimento umas das outras, **convergiram na mesma reclassificação do projecto** — o jardim sobre
laje é **tecnicamente uma cobertura ajardinada**.

Isso activa um corpo normativo (**FLL**), um modo de falha próprio (**substrato fino seca em dias**,
e a literatura é explícita sobre falhar cedo e mal em clima mediterrânico) e uma ferramenta gratuita
(**SWMM, módulo Green Roof**). **Nada disto está no dossier** — e não por descuito: quando o dossier
foi escrito, o jardim ainda era de chão.

**Correcção ao que esta sessão registou sobre nuvem de pontos:** a T005 apurou uma inversão que a
pesquisa desta sessão não viu — **o reboco liso é o pior caso para fotogrametria e um dos melhores
para TLS** (laser scanning profissional). **Não contradiz `REJEICOES.md` §11**, que rejeitou captura
*por telemóvel*. Custo de aluguer em Portugal por apurar.

### 3.2 A T004 posicionou as árvores e fechou a sessão 1 — `c69183c`, `da55638`

- **Transição resolvida em geometria completa.** Quatro cotas, maciço de 1,75 m, escada de 6 degraus
  dentro da norma, 1,60 m³ de vazio técnico. **Jardim resultante ≈55,0 m².**
- **São quatro árvores, não três.** O dossier regista **um** *Celtis australis*; **são dois**,
  confirmado em fotografia.
- **O jardim tem duas estações:** céu aberto **34% no Verão · 69% no Inverno**, porque os lodões são
  caducos. **Não é um jardim sombrio** — dá sombra no calor e sol no frio.
- **A palmeira desperdiça 11% da copa fora do recinto, contra 74% do lodão 1.** É a árvore que mais
  rende por metro de copa — argumento aritmético a somar ao estatuto de ícone.
- **Reserva de sequência:** a escada encosta ao muro SE, cuja patologia tem origem desconhecida 🔴.
  **A escada não pode ser a primeira coisa da obra; a plataforma pode.**

---

## 4. O próximo passo

### Primeiro — despachar os dois pedidos da T005 (regra A3)

1. **As camadas dos +0,50 m.** ⚠ **Urgente para a T004.** A cota está fixada mas **não decomposta em
   camadas** (drenante / filtrante / substrato) — e **a decomposição é geometria, não acabamento**.
   A T004 está a desenhar sem ela.
2. **Instruir ou adiar a fase 2 da T005.**
3. **Decidir sobre o TLS** — custo de aluguer em PT não apurado.

### Depois

- **As cinco medições.** Continuam por fazer. **M1 — copa da palmeira — é a mais importante e nunca
  foi feita.** Custa uma hora, está 🔴 desde sempre, e bloqueia o pedido 5 à T003 **e** a entrega da
  T004.
- **Comprar o telémetro laser (20–40 €).** Resolve M2, M3, M4 e a cota de retenção do muro SW.
  **É a compra de melhor retorno do projecto.**
- **Perguntar ao David que telemóvel tem** — decide o método para M1.
- **Passar três factos à T001:** (1) a relva artificial existe e ainda lá está; (2) os muros podem
  não ter todos a mesma altura; (3) **são dois lodões, não um** — corrige o dossier.
- **Criar as threads de impermeabilização e de redução de peso** — propostas em
  `T002-jardim-v2/TICKETS.md`, ainda por criar. **A reclassificação como cobertura ajardinada
  aumenta muito o valor da primeira.**
- **A sessão 2 da T004 vai propor o fecho.** Estar pronto para absorver.
- **Rever os cinco princípios de V1 que sobram** (#3, #4, #6, #7, #8).
- **`Jardim.html`** — desactualizado. Território exclusivo do Arquitecto.

### Com prazo próprio

- **Laranjeira: Fev–início Mar 2027.** Não depende de ninguém. Faltam ~5 meses.
- **Calendário da construção civil** — manda em tudo o resto, e continua por confirmar.

---

## 5. Cuidados

1. **Este handoff foi escrito por uma sessão que ficou desactualizada.** Se alguma coisa aqui não
   bater com o repositório, **o repositório ganha.** `ESTADO.md`, `THREADS.md` e
   `THREAD-MENSAGENS.md` são a verdade; isto é um mapa.

2. **A reclassificação como cobertura ajardinada ainda não está em `ESTADO.md`.** A T005 entregou-a,
   o Arquitecto não a absorveu. **Enquanto não estiver lá, não é decisão vigente** (G1) — e é
   provavelmente o achado mais consequente das últimas 48 horas.

3. **A urgência não dispensa medir.** M1 custa uma hora; a plataforma, se ficar mal, custa a obra
   toda. É o único ponto em que o Arquitecto insistiria contra a pressa.

4. **Os números de sol em uso são estimativa da T002, não da T003.** A T003 nunca correu. Entram
   sempre com etiqueta, e está-lhe dado por escrito que **se o modelo não os reproduzir, deve
   dizê-lo em vez de se ajustar ao que já está escrito.**

5. **O muro SW já está rejeitado como argumento solar** (`REJEICOES.md` §06) — o sol que entraria
   atravessa a copa da palmeira. **Mantém-se em aberto por vista, proporção e sensação de recinto.**
   Não reabrir o argumento da luz sem facto novo.

6. **O erro caro do projecto continua a ser a drenagem.** O quintal escoa há décadas por uma descarga
   que ninguém localizou, e a piscina põe ≈1,1 t naquele canto. **Abrir o orifício + traçador de
   corante é a acção n.º 1**, sinalizada desde 2026-09-16 e ainda por fazer.
