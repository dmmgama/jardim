---
created: AAAA-MM-DD
updated: AAAA-MM-DD
project: Jardim
tipo: governo
modo: append-only
leitura: on-demand
lingua: pt-PT
instrucoes: REGISTO-DOCUMENTOS-INSTRUCOES.md
summary: |
  Catálogo único de todos os documentos produzidos no projecto — por Arquitecto, por
  threads e pelo David — tenham ido ou não para o NotebookLM. Organizado por Dono e,
  dentro de cada dono, por sessão. Append only, excepto a secção de dependências.
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (a) · DESCRIÇÃO — escrita uma vez, não se toca.                       -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# REGISTO DE DOCUMENTOS

Catálogo de **tudo o que este projecto produziu em forma de documento** — de sessões de
Arquitecto, de threads, e do próprio David — tenha ido ou não para o NotebookLM.
Existe para que ninguém volte a fazer trabalho que já estava feito.

> **Append only (G24).** Não se reescreve nem se reordena. Corrige-se acrescentando.
> **Única excepção:** a secção [[#Dependências entre documentos]], no fim deste ficheiro.
>
> **Leitura *on demand* (G26 · T21).** Não se lê por rotina ao arrancar sessão.
>
> **As threads podem escrever aqui (G25 · T2).** Terceira e última excepção à regra territorial.
>
> **Como se preenche:** ver `REGISTO-DOCUMENTOS-INSTRUCOES.md`. **Não se improvisa.**

**Notebook do projecto:** ver `Notebook-LM` no front matter do `CLAUDE.md`.
**Nomenclatura da source:** `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>` · `CARGO` = `TNN` · `ARQ` · `DVD`.

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (b) · ÍNDICE GERAL — estático. Só muda se nascer secção nova.         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Índice geral

- [[#Índice de Donos]]
- [[#Índice por Tipo]]
- [[#1 · ARQUITECTO]]
- [[#2 · THREADS]]
- [[#3 · DAVID]]
- [[#4 · OUTROS]]
- [[#Dependências entre documentos]]

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (c) · ÍNDICE DE DONOS — MANUAL.                                       -->
<!-- Quem abre uma thread nova (= Arquitecto, G9) acrescenta aqui uma linha.    -->
<!-- Uma thread NÃO edita esta zona: cria o heading no corpo e avisa por INBOX. -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Índice de Donos

| Dono | Tag | Secção |
|---|---|---|
| Arquitecto | `#dono/arquitecto` | [[#1 · ARQUITECTO]] |
| T001 · local | `#dono/t001` | [[#T001 · local]] |
| T002 · jardim-v2 | `#dono/t002` | [[#T002 · jardim-v2]] |
| T003 · modelo-solar | `#dono/t003` | [[#T003 · modelo-solar]] |
| T004 · geometria | `#dono/t004` | [[#T004 · geometria]] |
| T005 · caracterizacao | `#dono/t005` | [[#T005 · caracterizacao]] |
| David | `#dono/david` | [[#3 · DAVID]] |
| Outros | `#dono/outros` | [[#4 · OUTROS]] |

<!-- Thread nova → acrescentar linha acima E criar o heading H3 na secção 2. -->

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ZONA (d) · ÍNDICE POR TIPO — automático pela TAG. Não se mexe.             -->
<!-- Clicar na tag lista as ocorrências. Os blocos Dataview estão COMENTADOS:   -->
<!-- com tudo num só ficheiro, `FROM #tag` devolve o ficheiro, não as linhas.   -->
<!-- Só se activam se o registo passar a uma nota por documento. Ver §5.2.      -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Índice por Tipo

Vocabulário **fechado**. Se o tipo não for evidente, **pergunta-se ao David** — não se
classifica ao calha (G28 · T19). `Outros` é para quando não há certeza.

### Sínteses · #tipo/sintese
Cruza e conclui sobre vários documentos anteriores.
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/sintese SORT Data DESC
```
-->

### Reports · #tipo/report
Relato de trabalho feito: objectivos, método, achados, próximos passos.
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/report SORT Data DESC
```
-->

### Research · #tipo/research
Estado da arte ou investigação externa. **Leva sempre o prompt dentro do ficheiro.**
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/research SORT Data DESC
```
-->

### Dossiers · #tipo/dossier
Compilação de referência sobre um objecto ou tema, para consulta.
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/dossier SORT Data DESC
```
-->

### Notas · #tipo/nota
Registo curto, pontual, sem pretensão de completude.
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/nota SORT Data DESC
```
-->

### Outros · #tipo/outros
Governo, auditoria, consolidação — **ou** quando não há certeza.
<!--
```dataview
TABLE WITHOUT ID Título, Dono, Data FROM #tipo/outros SORT Data DESC
```
-->

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 1 DE 4 — ARQUITECTO                                          -->
<!-- Blocos de sessão por ordem cronológica. O mais recente vai para o FIM.     -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 1 · ARQUITECTO

*(sem entradas)*

<!-- FORMA DE UM BLOCO DE SESSÃO — copiar daqui para baixo:

## AAAA-MM-DD · «nome exacto da sessão Claude»
#dono/arquitecto

Sumário de sessão em 1 a 3 linhas: o que se fez COM DOCUMENTAÇÃO nesta sessão.
Não é o resumo da sessão — é o resumo do trabalho documental.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/xxx | AAAA-MM-DD | Arquitecto | «...» | [[caminho/ficheiro\|Título]] | [[caminho/ficheiro.md\|ficheiro.md]] · — sem PDF | Duas linhas. O que **conclui**, não de que trata. | — |

-->

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 2 DE 4 — THREADS                                             -->
<!-- Um H2 por thread. Dentro de cada thread, blocos de sessão H3.              -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 2 · THREADS

## T001 · local

*(sem entradas)*

## T002 · jardim-v2

*(sem entradas)*

## T003 · modelo-solar

*(sem entradas)*

## T004 · geometria

*(sem entradas)*

## T005 · caracterizacao

<!-- ───────────────────────────────────────────────────────────────────────── -->
<!-- EXEMPLO PREENCHIDO COM DADOS FICTÍCIOS ÓBVIOS (T999 · 2026-01-01).        -->
<!-- Serve só para se ver a forma. APAGAR ao instanciar o registo real.        -->
<!-- ───────────────────────────────────────────────────────────────────────── -->

### 2026-01-01 · «2026.01.01 - EXEMPLO - Sessao Ficticia»
#dono/t999

Exemplo fictício. Fase 1 da T999: duas pesquisas em paralelo e uma síntese que as cruza.
Duas subiram ao notebook; a terceira ficou de fora por ser método interno.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/research | 2026-01-01 | T999 | «2026.01.01 - EXEMPLO - Sessao Ficticia» | [[30-THREADS/T999-exemplo/research/01-EXEMPLO-ALFA\|Exemplo Alfa]] | [[30-THREADS/T999-exemplo/research/01-EXEMPLO-ALFA.md\|01-EXEMPLO-ALFA.md]] · [[30-THREADS/T999-exemplo/research/T999-26-01-01-RESEARCH-EXEMPLO-ALFA.pdf\|T999-26-01-01-RESEARCH-EXEMPLO-ALFA.pdf]] | Pesquisa fictícia de demonstração. **Conclui que o campo Sumário diz o que o documento conclui**, não de que trata. | — |
| #tipo/research | 2026-01-01 | T999 | «2026.01.01 - EXEMPLO - Sessao Ficticia» | [[30-THREADS/T999-exemplo/research/02-EXEMPLO-BETA\|Exemplo Beta]] | [[30-THREADS/T999-exemplo/research/02-EXEMPLO-BETA.md\|02-EXEMPLO-BETA.md]] · — sem PDF | Segunda pesquisa fictícia. **Não foi ao notebook** — material de decisão de compra, para consultar quando for altura. | — |
| #tipo/sintese | 2026-01-01 | T999 | «2026.01.01 - EXEMPLO - Sessao Ficticia» | [[30-THREADS/T999-exemplo/research/03-SINTESE-EXEMPLO\|Síntese de exemplo]] | [[30-THREADS/T999-exemplo/research/03-SINTESE-EXEMPLO.md\|03-SINTESE-EXEMPLO.md]] · [[30-THREADS/T999-exemplo/research/T999-26-01-01-SINTESE-EXEMPLO.pdf\|T999-26-01-01-SINTESE-EXEMPLO.pdf]] | Cruza Alfa e Beta. **As dependências vão à secção do fim, não a esta coluna** — ver §6 das instruções. | — |

<!-- NOTAS SOBRE O EXEMPLO ACIMA:
     · Título  → wikilink SEM extensão, com alias legível.
     · Ficheiros → wikilink COM extensão, alias = só o nome. Sem PDF ⇒ "— sem PDF".
     · O `|` do alias dentro da tabela vai SEMPRE escapado: \|
     · Supported nasce a "—" e NUNCA MAIS se toca. Ver secção de dependências.
     · #dono/t999 vai no heading, nunca na tabela.
-->

<!-- ───────── FIM DO EXEMPLO — apagar tudo o que está entre as duas barras ─── -->

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 3 DE 4 — DAVID                                               -->
<!-- Material do cargo DVD. Heading = data de CATALOGAÇÃO, não de produção.     -->
<!-- Obrigações prévias: G36 (ler · front matter · prompt · confrontar · G27).  -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 3 · DAVID

*(sem entradas)*

<!-- FORMA:

## AAAA-MM-DD · Catalogação — (sem sessão)
#dono/david

Sumário de 1 a 3 linhas: o que foi catalogado e a que questão em aberto responde.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/research | AAAA-MM-DD | David | — (sem sessão) | [[40-PESQUISAS/David/ficheiro\|Título]] | [[40-PESQUISAS/David/ficheiro.md\|ficheiro.md]] · — sem PDF | O que responde. Declarar se assenta em premissas entretanto corrigidas. | — |

MATERIAL SÓ NO NOTEBOOK (sem ficheiro no repositório):
| #tipo/outros | AAAA-MM-DD | David | — (sem sessão) | Título em texto simples *(só no notebook)* | — sem ficheiro | Origem declarada: quem o trouxe e de onde. **Não se propõe eliminar sem perguntar.** | — |

-->

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CORPO · NÍVEL 4 DE 4 — OUTROS                                              -->
<!-- O que não cabe acima: terceiros, documentos herdados, arqueologia.         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# 4 · OUTROS

*(sem entradas)*

<!-- FORMA:

## AAAA-MM-DD · «nome da sessão» (ou "— (sem sessão)")
#dono/outros

Sumário de 1 a 3 linhas.

| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
| #tipo/outros | s/d | Outros | — (sem sessão) | [[caminho/ficheiro\|Título]] | [[caminho/ficheiro.md\|ficheiro.md]] · — sem PDF | Origem e motivo de estar aqui. Data desconhecida ⇒ "s/d" e explicar. | — |

-->

---
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ÚNICA SECÇÃO EDITÁVEL DESTE FICHEIRO — excepção declarada ao G24.          -->
<!-- Fora daqui, o append-only é absoluto.                                      -->
<!-- Lê-se: FONTE → foi usada por → CONSUMIDOR.                                 -->
<!-- Natureza (fechado): Síntese · Fonte externa citada · Substituição ·        -->
<!--                     Refutação · Deck NotebookLM                            -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Dependências entre documentos

> **Esta secção — e só esta — é editável.** Toda a dependência descoberta *depois* de a
> linha do documento ter sido escrita regista-se aqui, não na coluna `Supported`.
> Razão da regra: `REGISTO-DOCUMENTOS-INSTRUCOES.md` §6.

| Data do registo | Fonte | Usada por | Natureza |
|---|---|---|---|
| 2026-01-01 | [[30-THREADS/T999-exemplo/research/01-EXEMPLO-ALFA.md\|01-EXEMPLO-ALFA.md]] | [[30-THREADS/T999-exemplo/research/03-SINTESE-EXEMPLO.md\|03-SINTESE-EXEMPLO.md]] | Síntese |
| 2026-01-01 | [[30-THREADS/T999-exemplo/research/02-EXEMPLO-BETA.md\|02-EXEMPLO-BETA.md]] | [[30-THREADS/T999-exemplo/research/03-SINTESE-EXEMPLO.md\|03-SINTESE-EXEMPLO.md]] | Síntese |

<!-- Linhas acima são do exemplo fictício T999. Apagar ao instanciar. -->

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- RODAPÉ — checklist de fim de sessão. Não se apaga.                         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Checklist de fim de sessão

```
[ ] Todos os documentos produzidos estão na tabela? (os que foram E os que não foram ao notebook)
[ ] As 8 colunas preenchidas, nenhuma vazia?
[ ] Tipo com tag #tipo/<valor> — e perguntado ao David se não era evidente?
[ ] Wikilinks com o `|` do alias escapado como `\|`?
[ ] PDF dos decks na pasta do documento de origem, com o nome certo? (G29)
[ ] Sumário de sessão, 1-3 linhas, antes da tabela?
[ ] Dependências novas na secção do fim?
[ ] Nada editado fora da secção de dependências?
```
