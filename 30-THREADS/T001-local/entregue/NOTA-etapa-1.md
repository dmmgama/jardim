---
created: 2026-09-15
project: Jardim
thread: T001
tipo: nota de entrega
etapa: 1 — cenário completo do jardim
estado: ENTREGUE · aguarda absorção pelo Arquitecto
---

# T001 · Entrega da etapa 1

**Etapa 1 do mandato cumprida.** O cenário completo do jardim está produzido, com cobertura de todo o
quintal e declaração explícita do que não se sabe.

> **T002 estava bloqueada por esta entrega.** O Arquitecto pode levantar o bloqueio.

## PRODUTO — onde está

> **O produto desta entrega NÃO vive nesta pasta.** Vive em `../Docs-David-Local/`, junto às ~50
> imagens que referencia. Os caminhos das imagens são relativos e simples; separá-los partiria 25
> ligações. Ver **T10-bis** do `CLAUDE.md` da thread.

| Produto | Caminho |
|---|---|
| **Dossier do Local** (canónico) | `../Docs-David-Local/DOSSIER-LOCAL.md` |
| Dossier, versão autónoma | `../Docs-David-Local/DOSSIER-LOCAL.html` |
| Material de origem | `../Docs-David-Local/` — ~50 imagens |

---

---

## 1. O produto

| Ficheiro | O que é |
|---|---|
| **`Docs-David-Local/DOSSIER-LOCAL.md`** | **O documento canónico. Único.** 827 linhas, 14 secções, 6 diagramas ASCII, índice de 49 imagens, semáforo de fiabilidade por secção. |
| **`Docs-David-Local/DOSSIER-LOCAL.html`** | O mesmo, autónomo (9,2 MB), com imagens embebidas. Para leitura e circulação. |
| `research/AUDITORIA-COERENCIA-T001.md` | Auditoria de coerência da pasta contra o protocolo. Origem das correcções de arrumação desta sessão. |

Tudo vive em `Docs-David-Local/`, junto às imagens que referencia. **Nada foi movido para fora da
pasta** — a arrumação final é decisão do proprietário.

### Material de apoio, em `research/`

| Ficheiro | O que é |
|---|---|
| `INVENTARIO-DOCS-DAVID-LOCAL.md` | Inventário dos 57 ficheiros: o que cada imagem mostra, órfãos, contradições, duplicados, lacunas. |
| `Estado_Arte_Caracterizacao_Espaco_Exterior.md` | Estado da arte sobre como se caracteriza um espaço exterior. Inclui **ficha-modelo de campos** e sequência de levantamento. |

---

## 2. Como se lê o dossier

**Ordem das secções: por estabilidade.** O que não muda vem antes do que muda — geometria antes de
exposição solar, exposição solar antes de vegetação.

**Semáforo, em cada secção:**

| | Significado | Que decisão suporta |
|---|---|---|
| 🟢 | Desenho cotado, medição, ou observação directa confirmada | Decisão **irreversível** |
| 🟡 | Fonte única, ou inferência de fotografia. Coerente, não verificado | Decisão **reversível**. Nunca dimensionamento. |
| 🔴 | Desconhecido, ou fontes em conflito | **Bloqueia** ou obriga a plano B declarado |

**Contagem:** 🟢 38 · 🟡 26 · 🔴 34.

**Etiquetas de proveniência:** `[desenho]` `[foto]` `[observado]` `[medido]` `[estimado]`.
A etiqueta `[observado]` foi criada nesta sessão — sobre *comportamento* prevalece sobre fotografia;
sobre *dimensão* cede ao desenho.

**Os diagramas lêem-se sem abrir uma única imagem.** Planta cotada, corte, escoamento, nomenclatura
e percurso solar estão em ASCII dentro do Markdown.

---

## 3. O que se estabeleceu nesta sessão

### Três conflitos fechados

| Tema | Resolução |
|---|---|
| **Altura dos muros** | **2,50 m** `[observado]`, confirmado pelo proprietário. Era o item 1 de «por confirmar» e a maior fonte de erro do modelo solar — 3,00 → 2,50 m **duplica** a média de sol de Dezembro. |
| **Corte de arquitectura** | Era um corte de **proposta de ampliação**, usado como levantamento. Anotado pelo proprietário: passou a 2,5 m + 5 m de muro, 1,35 m de escada. Concorda agora com a observação. |
| **Drenagem** | **Existe drenagem construída e funciona.** Estabelecido por observação: caudal forte, nunca satura. Exclui a hipótese de absorção pela palmeira. |

### Dois erros de facto corrigidos

**«Água estagnada, sem escoamento aparente»** — afirmação retirada. Era conclusão tirada de uma
fotografia: não se via para onde a água ia, e isso foi lido como não ir a lado nenhum. O quintal
escoa.

**Cinco fotografias descritas erradamente no índice** — `Foto2b` (que é a **única fonte sobre
electricidade** de todo o acervo), `Foto3` (fachada com cotas manuscritas, não escada), `Foto4`
(marquise, não zona SW), `Foto-Aerea` (janela de piso superior, não aérea), `Foto1b`.

### Oito contradições, sete resolvidas

| | |
|---|---|
| **Resolvidas** (5) | C1 altura do edifício · C2 terras retidas · **C3 azimute** · C7 largura da escada |
| **Anuladas** (2) | C4 comparava grandezas diferentes · C6 descrevia ficheiro já substituído |
| **Aberta** (1) | C5 cotas da planta da fracção — **sem consequência para o quintal** |

**C3 — azimute do eixo longo — resolvida e aplicada.** Adoptado **65°/245°**, do diagrama declarado
normativo e que é a única fonte a declarar «medido»; os 60°/240° eram aproximações com «≈». O plano
da fachada passa de 150° para **155°**, e as horas de entrada do sol foram recalculadas por posição
solar: **+22 min** em Dezembro, +15 em Março, +13 em Setembro, +8 em Maio, +7 em Junho. Maior no
Inverno, porque o Sol percorre o azimute mais devagar quando está baixo.

**Erro de cálculo detectado ao aplicar (F7).** O valor de 21 Mar (11:28) não correspondia a nenhum
plano de fachada plausível — a essa hora o azimute solar é 133°. As outras quatro datas reproduziam-se
a ±4 min. Corrigido para **12:40**.

### Geometria solar adoptada

Valores NREL SPA: altura solar máxima **27,9°** no Inverno, **74,7°** no Verão. É o número que explica
o jardim: a 27,9° num corredor de 5,78 m entre muros de 2,50 m, a sombra é de ≈4,7 m — quase a largura
inteira. O Inverno não é escuro por orientação, é por **proporção**.

---

## 4. O que o Arquitecto tem de decidir

### 4.1 Absorver ou não o dossier

O dossier é candidato a `10-LOCAL/`. **A T001 não pode escrevê-lo lá** (regra T3). A migração implica
decidir o que fazer aos caminhos das imagens, que hoje são relativos e simples.

### 4.2 Hipótese registada, por avaliar — rebaixamento do muro SW

Levantada pelo proprietário. **Está registada como hipótese, sem avaliação** — a T001 não avalia
propostas de transformação.

Os factos que a decisão terá de considerar estão na secção 6.3 do dossier. Um deles não tinha sido
ligado antes: **a intervenção proposta e o ponto de drenagem estão no mesmo sítio.**

### 4.3 Levantar o bloqueio da T002

A etapa 1 está entregue. A condição do bloqueio deixou de se verificar.

---

## 5. O que fica por fazer — etapa 2

### Prioridade 1 — bloqueantes

| # | O que | Custo | Tempo |
|---|---|---|---|
| 1 | **Identificar para onde descarrega o dreno** (X ≈ 11,7 · Y ≈ 3,5). Corante traçador é o teste mais barato e responde à mesma pergunta que escavar. | < 10 € | 1 tarde |
| 2 | **Teste de percolação.** Eliminatório: decide a viabilidade de qualquer vegetação de solo. | 0 € | Meio-dia + 1 noite |
| 3 | **Processo de obra no Arquivo Municipal.** Tipo construtivo e fundação do muro SW. | 0 € consulta | Até 10 dias |

### Prioridade 2

Altura real do desnível exterior · espessura da betonilha e sub-base · copa da palmeira e do lodão ·
origem da humidade no muro SE · análise de solo em laboratório (10–70 €, < 1 semana, **só depois da
percolação**).

### Doze secções por instruir

Solo e substrato · DLI medido · microclima · vento · cargas · acessos para materiais · privacidade ·
ruído · condomínio · coroa dos muros · muro NW de frente · fotografia do orifício de drenagem.

Cada uma está no dossier com o que falta, como se obtém, custo e tempo.

### Uma contradição em aberto

**C5** — as duas cadeias de cotas da `Planta Fracao.png` não fecham (diferença de 4,84 m). **Não
afecta o quintal:** os 13,00 m estão confirmados por duas fontes independentes. Fica registada por
higiene, não por consequência.

---

## 6. Achado operacional que não cabe no dossier

Do estado da arte, dois pontos com consequência imediata:

**A palmeira inspecciona-se pela coroa, não pelo tronco**, para sinais de *Rhynchophorus ferrugineus*
— folhas rasgadas na inserção, murchidão da coroa, serrim na base das folhas. Contraria o instinto, e
a palmeira é o elemento de maior valor do quintal.

**Não existe protocolo estabelecido** para caracterizar um jardim doméstico — nem em Portugal, nem na
Europa. A regra «facto e fonte, buraco declarado» que esta thread aplica é, por comparação, mais
rigorosa do que o que está publicado.

---


## 8. Estado da thread

**`ONGOING`.** A etapa 1 fecha; a etapa 2 é alimentação por partes, conforme o projecto pedir
profundidade. Não há proposta de fecho.
