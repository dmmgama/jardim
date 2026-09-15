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

**Última actualização:** 2026-09-16

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

### T002 — Jardim V2

| | |
|---|---|
| **Pasta** | `30-THREADS/T002-jardim-v2/` |
| **Estado** | `ACTIVA` — **em curso.** Bloqueio levantado em 2026-09-16. |
| **Aberta** | 2026-09-14 |
| **Mandato** | **Debater soluções possíveis para o jardim e chegar a opções viáveis**, testadas contra as condicionantes reais do local — drenagem, sol, clima, custo — e contra o gosto do David. Mandato reescrito em 2026-09-16. |
| **Entrega** | Conjunto de opções viáveis em `entregue/`, cada uma com o que implica e porque sobrevive às condicionantes. Para consolidar em `ESTADO.md` e `20-PLANO/`. |
| **Sessões** | 0 |
| **Desbloqueio** | A etapa 1 da T001 entregou. Existe base factual partilhada: o dossier canónico do Local. |
| **Nota** | **É agora a thread de trabalho activo do projecto.** Consulta o dossier da T001 em permanência e pede à T003 a quantificação de sombra quando precisar. |

---

### T003 — Modelo solar

| | |
|---|---|
| **Pasta** | `30-THREADS/T003-modelo-solar/` |
| **Estado** | `ACTIVA` · pacote de arranque pronto, por montar |
| **Aberta** | 2026-09-15 |
| **Mandato** | Construir e manter um modelo digital paramétrico do quintal que permita testar posições de árvores e ver o efeito no sombreamento. |
| **Entrega** | Modelo funcional em `modelo/` + tabelas de exposição por cenário em `entregue/`. `ONGOING`. |
| **Sessões** | 0 |
| **Nota** | Criada pela sessão T001 de 2026-09-15 com autorização expressa do David para derrogar G9. **Ratificada pelo Arquitecto em 2026-09-16, mandato confirmado sem alteração** — ver `ESTADO.md` §11. |

---

## Fechadas

*(nenhuma)*

---

## Numeração

As threads numeram-se sequencialmente a partir de T001, sem reutilização. Uma thread fechada mantém o seu número para sempre.

Nome da pasta: `T<NNN>-<assunto-em-kebab-case>`.
