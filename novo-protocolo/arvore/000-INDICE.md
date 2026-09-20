---
title: "Índice — árvores MECE"
date: 2026-09-20
type: indice
tags: [MECE, arvore, indice]
---

# Índice — árvores MECE

Quinze documentos, quatro casos, três tipos. Produzidos em 20 de Setembro de 2026.

---

## Convenção de nomes

```
YYYY-MM-DD-TYPE-CASE-TITLE.md
```

| Elemento | Valores |
|---|---|
| **TYPE** | `research` · `audit` · `sintese` |
| **CASE** | `mckinsey` · `dominios` · `jardim` · `protocolo` |

**`research`** — investigação com base documental própria; a secção *Mandato* reproduz o prompt dado ao analista.
**`audit`** — confronto de um objecto existente contra uma base de evidência.
**`sintese`** — trabalho derivado: integra, aplica ou combina o que já existe.

Todo o documento tem a mesma espinha: `0 · Sumário executivo` · `1 · Mandato` · `2 · Método` · `3 · Corpo do relatório` · `4 · Fontes`.
Os documentos `audit` e `sintese` declaram no frontmatter o campo **`sobre:`**, com wikilinks para aquilo de que dependem.

*Este índice não é nenhum dos três tipos, e por isso leva `type: indice`.*

---

## Por onde começar

| Se queres… | Lê |
|---|---|
| Perceber o método como ele é praticado | [[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]] |
| Usá-lo fora da consultoria, ou caracterizar em vez de resolver | [[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]] |
| **Operar dentro do protocolo — és um agente** | [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-combinada]] |
| Auditar a definição de árvore actualmente em vigor | [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore]] |
| Ver o método aplicado a um caso concreto | [[2026-09-20-sintese-jardim-exercicios-aplicados]] |

---

## CASO `mckinsey` — como o método é praticado

Investigação 1. Três analistas em paralelo, bases documentais independentes, seguidos de síntese.

| Tipo | Documento | O que traz |
|---|---|---|
| `sintese` | [[2026-09-20-sintese-mckinsey-arvores-mece-na-mckinsey]] | **O relatório principal.** Ciclo completo: pergunta-raiz, cortes, pluralidade de cortes, teste, mutação, conclusão, destino da árvore |
| `research` | [[2026-09-20-research-mckinsey-front-end-e-definicao-do-problema]] | Origens do MECE em Minto; o worksheet de oito campos; SCQA; a *one-day answer*; tipologias de árvore |
| `research` | [[2026-09-20-research-mckinsey-construcao-dos-cortes-mece]] | Seis famílias de corte; as 13 estruturas válidas para o mesmo caso; critérios de escolha; poda |
| `research` | [[2026-09-20-research-mckinsey-vida-teste-e-fim-da-arvore]] | **Traz o Staff Paper No. 66**, documento interno da firma, lido na íntegra. Testes, mutação, conclusão, storyline |

---

## CASO `dominios` — o método fora da consultoria

Investigação 2. Mesmo desenho: três analistas em paralelo, depois síntese.

| Tipo | Documento | O que traz |
|---|---|---|
| `sintese` | [[2026-09-20-sintese-dominios-aplicacao-a-outros-dominios]] | **O relatório principal.** Os três modos de árvore; ME sem CE; a regra de ouro; onde aplicar e onde não |
| `research` | [[2026-09-20-research-dominios-transferencia-do-metodo]] | **Traz o texto integral de *Bulletproof Problem Solving***. Onze métodos cognatos; o que se parte na transferência |
| `research` | [[2026-09-20-research-dominios-caracterizacao-e-me-sem-ce]] | Facetas, tipologias, morfologia, hierarquias de objectivos; a resposta formal a ME-sem-CE |
| `research` | [[2026-09-20-research-dominios-limites-e-contra-indicacoes]] | **Traz o relatório original de Fischhoff.** Problemas perversos, Ackoff, Cynefin, domínios proibidos |

---

## CASO `jardim` — o método aplicado

| Tipo | Documento | O que traz |
|---|---|---|
| `sintese` | [[2026-09-20-sintese-jardim-exercicios-aplicados]] | Dois exercícios no mesmo domínio: diagnóstico e caracterização. Os dois registos de faceta e o cruzamento; a valência como relação |

---

## CASO `protocolo` — a árvore como ferramenta de governo

Auditoria da definição de árvore em `naoabrirsemordem/`, e o documento operacional que dela resulta.
**Desenho de controlo:** todo o trabalho foi feito **duas vezes**, por dois agentes sem contacto entre si e com leitura restrita. Os documentos marcados *(frio)* são o controlo independente.

### Auditorias

| Tipo | Documento | O que traz |
|---|---|---|
| `audit` | [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore]] | Dez críticas. ME/CE ao nível errado; sem notação para o factor transversal; a poda registada onde o enviesamento não opera |
| `audit` | [[2026-09-20-audit-protocolo-criticas-definicao-de-arvore-frio]] | *(controlo)* Convergiu em quatro pontos, independentemente. Achados próprios: `escapar`, a regra sem identificador, o formalismo da exaustividade, `suspenso: por dimensionar` |

### Documento operacional

| Tipo | Documento | Estatuto |
|---|---|---|
| `sintese` | [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-combinada]] | **Candidato a canónico.** Combina as duas versões, com registo de como cada divergência foi arbitrada |
| `sintese` | [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-combinada-frio]] | *(controlo)* Combinação independente. **Convergiu em quatro das cinco divergências** |
| `sintese` | [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso]] | Versão de origem |
| `sintese` | [[2026-09-20-sintese-protocolo-arvore-definicao-e-uso-frio]] | *(controlo)* Versão de origem independente |

---

## Como foi feito

```
INVESTIGAÇÃO 1 ─── 3 analistas paralelos ──► síntese mckinsey
INVESTIGAÇÃO 2 ─── 3 analistas paralelos ──► síntese dominios
                             │
                             ├──► exercícios aplicados (jardim)
                             │
                             └──► leitura do protocolo
                                      │
                    ┌─────────────────┴─────────────────┐
              agente principal                    agente frio
                    │                                   │
              auditoria                            auditoria
                    │                                   │
              doc. operacional                   doc. operacional
                    │                                   │
                    └────────► combinação ◄─────────────┘
                              (duas, independentes)
```

**Princípio de método, transversal a tudo:** hierarquia de provas declarada, contradições entre fontes registadas em vez de resolvidas por autoridade, e uma tabela de folclore em cada documento — para que o que não se confirmou não volte por outra via.

---

## Em aberto

| # | Questão |
|---|---|
| 1 | **O articulado normativo não está na pasta.** O `R3` cita `P0.10`, `P0.14`–`P0.21`, `P1.9`–`P1.13`, `P2.8`–`P2.18`, `P4`–`P10` e `C.4`; `arquitectura-governo.md` só tem `P0.1`–`P0.8`, `P1.1`–`P1.7`, `P2.1`–`P2.6`. As auditorias **não cobrem** o articulado ausente |
| 2 | **Desencontro de identificadores.** O `R3` §3 atribui o tecto numérico de árvores a `P0.5`/`P0.6`; na arquitectura essas regras são sobre quem redige o mandato. O tecto é o travão único declarado em `T5` |
| 3 | **Escolher qual das duas combinadas é canónica.** Convergiram em quatro das cinco divergências; a quinta — ordenação e âmbito dos cartões — é escolha de desenho, não de mérito |
| 4 | **Decidir se as correcções propostas entram no protocolo**, e por que via. Duas delas **retiram** regras; três acrescentam objectos pequenos; nenhuma toca na arquitectura |
