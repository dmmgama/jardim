---
created: 2026-09-14
project: Jardim
tipo: governo
summary: |
  Registo de todas as threads do projecto: activas, em espera e fechadas.
---

# THREADS

> **Regra G9:** só o Arquitecto cria uma thread.
> **Regra G10:** só o Arquitecto fecha uma thread. A thread propõe o fecho pelo canal de mensagens.
> **Regra G11:** o mandato é escrito em `thread.md` no momento da criação.

**Última actualização:** 2026-09-17

---

## Estados possíveis

| Estado | Significado |
|---|---|
| `ACTIVA` | Em trabalho. |
| `ONGOING` | Activa e sem data de fecho prevista — alimenta-se por partes. |
| `À ESPERA` | Bloqueada à espera de resposta do Arquitecto ou de input externo. |
| `PROPOSTA DE FECHO` | A thread entregou e propôs fechar. Aguarda o Arquitecto. |
| `FECHADA` | Entrega absorvida. Só de leitura. |

---

## Activas

### T001 — Local

| | |
|---|---|
| **Pasta** | `30-THREADS/T001-local/` |
| **Estado** | `ONGOING` · **etapa 1 entregue e absorvida (2026-09-16)** · etapa 2 por instruir |
| **Aberta** | 2026-09-14 |
| **Mandato** | Produzir e manter a descrição factual inequívoca do espaço existente. |
| **Entrega** | **Etapa 1: ✅ entregue.** Dossier canónico do Local — `T001-local/Docs-David-Local/DOSSIER-LOCAL.md`, declarado canónico em `ESTADO.md` §01. **Etapa 2:** aprofundamento por tema, por partes. |
| **Sessões** | 1 (2026-09-15) |
| **Prioridade** | **Não é a thread de trabalho activo.** Passa a thread de **consulta e alimentação**: responde a factos quando a T002 ou a T003 precisarem, e recebe as medições à medida que forem feitas. Não se abre sessão própria sem um motivo dos que estão abaixo. |

**Nota de estado:** não está em pausa nem fechada. `ONGOING` é o estado correcto — a etapa 2 é alimentação por partes, sem data de fecho, e o dossier é o documento que a T002 vai consultar em permanência.

#### O que falta na etapa 2

**Bloqueantes — os três primeiros custam menos de 10 € e uma tarde:**

| # | O que | Custo | Tempo | Porque importa |
|---|---|---|---|---|
| 1 | **Para onde descarrega o dreno** (X ≈ 11,7 · Y ≈ 3,5). Corante traçador. | < 10 € | 1 tarde | O erro caro do projecto é entupir uma descarga que funciona há décadas. |
| 2 | **Teste de percolação.** | 0 € | Meio-dia + 1 noite | Eliminatório para qualquer vegetação de solo. |
| 3 | **Processo de obra no Arquivo Municipal.** Tipo construtivo e fundação do muro SW. | 0 € | Até 10 dias | **Condiciona a T002 directamente** — sem isto o rebaixamento do muro SW não é decidível. |
| 4 | **Cota até onde o muro SW retém terras** — fronteira suporte/guarda. | 0 € | Mesma ida ao terreno | Define quanto se pode rebaixar sem tocar em estrutura. |

**Prioridade 2:** altura real do desnível exterior · espessura da betonilha e sub-base · copa da palmeira e do lodão · origem da humidade no muro SE · análise de solo em laboratório (10–70 €, **só depois da percolação**).

**Doze secções por instruir:** solo e substrato · DLI medido · microclima · vento · cargas · acessos para materiais · privacidade · ruído · condomínio · coroa dos muros · muro NW de frente · fotografia do orifício de drenagem.

**Uma contradição aberta:** C5 — as duas cadeias de cotas da `Planta Fracao.png` não fecham (4,84 m de diferença). **Sem consequência para o quintal**, os 13,00 m estão confirmados por duas fontes independentes. Fica por higiene.

**Uma verificação legal pendente:** DL 92/2019 Anexo II (espécies invasoras). O PDF oficial não se deixou processar e as transcrições secundárias divergem nos asteriscos que distinguem "invasora na Madeira/Açores" de "invasora no continente". Critério conservador adoptado. **Tem de ser confirmado contra o original.**

---

### T004 — Geometria do jardim  ⚠ URGENTE

| | |
|---|---|
| **Pasta** | `30-THREADS/T004-geometria/` |
| **Estado** | `ACTIVA` · **caminho crítico da obra** |
| **Aberta** | 2026-09-17 |
| **Mandato** | **Fixar a geometria do jardim:** onde acaba a casa, onde começa o jardim, e o que sobra para ser jardim. A pergunta central: *o jardim útil é o que fica entre o fim da transição e o início da copa da palmeira — quanto é, onde é, que forma tem?* |
| **Entrega** | Planta cotada · corte longitudinal · quadro de áreas · cargas declaradas · nota do que ficou por medir. **A transição pode entregar-se em separado e primeiro, se a obra o exigir — autorizado à cabeça.** |
| **Sessões** | 0 |
| **Porquê urgente** | O David declarou em 2026-09-17: *«há URGÊNCIA pq essa parte da plataforma e construção civil é o que vai ocorrer já agora.»* **A ajuda de construção civil está disponível agora** — foi o que destravou o projecto ao fim de quatro planos parados. |
| **Bloqueante interno** | **Quatro medições, uma tarde.** M1 copa da palmeira (🔴 P2.2, nunca feita) · M2 altura dos muros · M3 cotas · M4 o vão da piscina. A thread ensaia com a copa parametrizada para não parar, **mas não entrega sem M1.** |
| **Criada por** | Autorização expressa do David, 2026-09-17. Mandato redigido pela T002 a pedido dele, **ratificado sem alterações**. |
| **Absorve** | O âmbito de **geometria** do ticket T4 da T002 (afinação da cota). |

---

### T003 — Modelo solar

| | |
|---|---|
| **Pasta** | `30-THREADS/T003-modelo-solar/` |
| **Estado** | `ACTIVA` · **arrancada 2026-09-17, a correr em paralelo** |
| **Aberta** | 2026-09-15 |
| **Mandato** | Construir e manter um modelo digital paramétrico do quintal que permita testar posições de árvores e ver o efeito no sombreamento. **Alargado em 2026-09-17:** avaliar e recomendar uma ferramenta de **captura 3D operável com telemóvel** que alimente o modelo. |
| **Entrega** | Modelo funcional em `modelo/` + tabelas de exposição por cenário em `entregue/`. **Mais:** recomendação de ferramenta de captura + procedimento de campo executável pelo David numa tarde. `ONGOING`. |
| **Sessões** | 0 |
| **Pedido em mão** | **Encaminhado 2026-09-17.** `T002-jardim-v2/research/03-PEDIDO-T003-COTA.md` — cinco pedidos, com duas alterações do Arquitecto: pedido 5 (palmeira) sobe a **decisivo**; pedido 1 ganha **forma e posição** da mancha de sol, não só área. |
| **Nota** | Criada pela sessão T001 de 2026-09-15 com autorização expressa do David para derrogar G9. **Ratificada em 2026-09-16, mandato confirmado sem alteração** — ver `ESTADO.md` §11. |

**Porque foi alargada.** A T003 precisa de geometria que não existe: a copa da palmeira nunca foi
medida (🔴 P2.2) e **bloqueia a T004**, que está no caminho crítico da obra. Os muros estão a 2,50 m
`[observado]` sem detalhe por troço, e há suspeita nova de que não têm todos a mesma altura. A
captura 3D entra no âmbito da T003 porque **é ela que sabe de que geometria precisa e com que
tolerância** — não é decisão de ferramenta, é decisão de requisito.

**Cautela registada à cabeça:** os muros são o pior caso para fotogrametria — reboco liso, sem
textura, em sombra permanente. A via Google 3D já foi rejeitada por não os resolver
(`REJEICOES.md` §11). A T003 está instruída a dizer **onde a fita métrica ganha à app**, em vez de
recomendar tecnologia por defeito.

---

## Fechadas

### T002 — Jardim V2

| | |
|---|---|
| **Pasta** | `30-THREADS/T002-jardim-v2/` |
| **Estado** | `FECHADA` — **entrega absorvida em 2026-09-17** |
| **Aberta / fechada** | 2026-09-14 → 2026-09-17 |
| **Sessões** | 2 (2026-09-16, 2026-09-17) |
| **Mandato que tinha** | Debater soluções possíveis e chegar a **duas a quatro opções viáveis**, testadas contra drenagem, sol, clima, custo e gosto do David. |
| **O que entregou** | **A lógica do jardim, não um leque de opções.** `research/EXPLICACAO-DO-LOCAL.html` (peça principal, autónoma) · `07-ZONAMENTO-DAVID.md` (as seis zonas) · `05-LUZ-COTA-ESTIMATIVA-T002.md` (quantificação solar própria) · modelo solar re-executável em Python · `David-Docs/INDICE.md` (13 imagens fichadas) · `entregue/NOTA.md`. |
| **Porque fechou assim** | **Desvio ao mandato literal, aceite pelo Arquitecto.** Na sessão 2 o David trouxe uma base de projecto completa — não uma preferência entre opções, mas o projecto. Produzir «duas a quatro opções distintas» sobre uma base já escolhida pelo decisor seria fabricar alternativas para as rejeitar. A thread registou-o, levantou a questão de mandato em 2026-09-16, e o Arquitecto **ratifica a interpretação**: a base do David substituiu a necessidade de leque. |
| **O que não fez** | Custo a fazer e a manter (filtro 4) · faseamento completo · cinco dos oito princípios de V1. **Passa à T004 e ao Arquitecto.** |
| **Sucessora** | **T004 — Geometria do jardim.** |

---

---

## Numeração

As threads numeram-se sequencialmente a partir de T001, sem reutilização. Uma thread fechada mantém o seu número para sempre.

Nome da pasta: `T<NNN>-<assunto-em-kebab-case>`.
