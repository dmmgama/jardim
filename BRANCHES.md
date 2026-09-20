---
created: 2026-09-18
project: Jardim
tipo: governo
branch: master
summary: |
  Índice de todas as branches do repositório: número, nome, mandato, datas e estado. Vive em master e está sempre actual.
---

# BRANCHES — índice

**Para que serve.** Saber a qualquer momento que branches existem, para quê, e em que estado estão. O número `Bn` entra no nome das sessões (`YYYY-MM-DD-Bn-…`) para as identificar.

**Regras.**
- Quem abre uma branch acrescenta aqui uma linha **em `master`**, no mesmo acto, com o número seguinte. Nunca se reutiliza um número.
- Toda a branch tem `MANDATO-DA-BRANCH.md` na sua raiz (regra G46 do `CLAUDE.md` da branch).
- Estados: `ativa` · `pausada` · `anulada` · `fechada` · `reaberta`.
- Ao fechar (fusão em `master`) ou anular, actualiza-se a data de fecho e o estado. Uma branch `reaberta` mantém o número.
- `master` é a linha principal e não tem número.

| N.º | Branch | Abertura | Fecho | Mandato | Estado |
|---|---|---|---|---|---|
| B0 | `Codex` | 2026-09-14 | 2026-09-14 | Sessão inicial de arranque do repositório (T001 etapa 1, T002 à espera). Sem mandato escrito; anterior a este índice. Já fundida em `master`. | `fechada` |
| B1 | `Governo-correcao-v1` | 2026-09-18 | — | Corrigir a falta de governo e a falta de instrumentos de visão do estado geral: registos e handoffs do Arquitecto por tema, mandato de branch, arranque por comando, estruturação top-down do projecto com o skill wayfinder. Ver `MANDATO-DA-BRANCH.md` na branch. | `ativa` |
| B2 | `Beads-Test` | 2026-09-19 | — | Avaliar se o Beads serve de mapa e fila de trabalho do Jardim (objectivo → peças → threads → lacunas), na sequência do diagnóstico «Arquitecto sem mapa» da B1. Veredicto binário no fecho: adoptar ou rejeitar. Worktree própria em `../Jardim-Beads-Test`. Ver `MANDATO-DA-BRANCH.md` na branch. | `ativa` |
