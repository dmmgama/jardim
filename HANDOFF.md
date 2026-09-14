---
created: 2026-09-14
project: Jardim
tipo: governo
summary: |
  Continuidade entre sessões de Arquitecto. Reescrito no fim de cada sessão.
---

# HANDOFF — Arquitecto

> **Regra A4:** o Arquitecto regista aqui, no fim da sessão, o estado e o próximo passo.
> Reescrito, não acumulado. O histórico vive em `ESTADO.md` e `REJEICOES.md`.

---

## Sessão 1 — 2026-09-14

**Nome da sessão:** `2026.09.14 - Jardim Arquiteto - S1`

### O que se fez

Montou-se o regime de governo V2 de raiz.

- Levantamento do estado real: leitura do Canon V1, worklog, dossier Adriano, e das duas páginas Notion (via subagentes).
- Diagnóstico: quatro planos paralelos, nenhum executado, zero obra no terreno.
- Desenho e implementação do governo: modos Arquitecto/Thread, estado e rejeições em espelho, threads estanques com canal de mensagens duplo.
- Reestruturação do repositório. `00-CANON/` extinto; V1 e DIY para arqueologia.
- Criadas T001 (Local, ongoing) e T002 (Jardim V2).
- `FLUXO-DE-PROJECTO.md` e `Fluxo-de-Projecto.html` a documentar o regime.
- Repositório posto sob git, com commit inicial.

### O que se decidiu

Registado em `ESTADO.md` §00. Descartes registados em `REJEICOES.md`.

### Estado no fim da sessão

| | |
|---|---|
| **Threads activas** | T001 (etapa 1, por arrancar — **prioridade máxima**) · T002 (à espera, bloqueada por T001) |
| **Pedidos pendentes** | nenhum |
| **Obra no terreno** | nenhuma |
| **Inbox** | 15 entradas por processar |

### Por fazer, decidido nesta sessão

- **Notion** — está no inbox. A estrutura do Jardim Hub (subpáginas V1, DIY, V2) e o protocolo de sincronização repo→Notion ficaram por definir. O David já criou a página raiz.
- **`Jardim.html`** — por criar. Próxima sessão.
- **Fichas de actor** — `10-EQUIPA/<actor>/ficha.md` criadas com o essencial; falta aprofundar.

---

## Próximo passo

**Sessão seguinte: T001, etapa 1 — o cenário completo do jardim.** Definido pelo David no fim desta sessão:

> "garantir que os agentes têm entendimento certo do cenário do jardim todo. sem isso não há nada que se possa debater."

Isto inverte a ordem que o Arquitecto tinha sugerido, e com razão: debater V2 sobre uma base factual contaminada reproduziria o erro que gerou quatro planos com cotas diferentes.

Depois disso:
1. **T002** — o David explica a oportunidade vantajosa. Desbloqueia com a entrega da etapa 1 de T001.
2. Tickets.
3. Processar o inbox — Notion Hub, PDFs, contradições.

---

## Cuidado com

**O padrão a não repetir.** V1 parou por depender de três terceiros e de um encadeamento rígido. O DIY foi o recuo perante isso e **também não arrancou — zero execução, confirmado pelo David em 2026-09-14**. Logo, baixar a ambição já foi tentado e não resolveu. V2 tem de resolver dependência e sequência, não apenas tamanho. Se a sessão de V2 produzir um quinto plano sem tocar nisto, o Arquitecto deve dizê-lo.

**Não há custo afundado nem obra a demolir.** O quintal está exactamente como em Fevereiro de 2026: betonilha degradada, quatro canteiros, hot tub sobre paletes. V2 arranca de folha limpa — é a única vantagem herdada dos seis meses parados.

**A palmeira.** É o princípio 1 do projecto e o elemento de maior risco do quintal. O único material sobre a manter viva — risco *Rhynchophorus ferrugineus*, protocolo 50–400 €/ano — está no Notion e nunca entrou no repositório.
