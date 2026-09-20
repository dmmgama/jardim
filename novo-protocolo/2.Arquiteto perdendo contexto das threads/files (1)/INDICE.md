---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Índice do conjunto documental da sessão: identificação, mandato, documento recebido
  e oito documentos produzidos, com nome, slug e resumo.
---

# Índice de documentos

## 1 · Identificação da sessão

| Campo | Valor |
|---|---|
| Slug | `sessao/encontrar-existente` |
| Data | 2026-09-19 |
| Tema | Governo de projectos multi-frente conduzidos por sessões de agentes |
| Nível | L1 — camada de caminho |
| Projecto de destino | Jardim como piloto; SSOT e MQT-AI como destino |

## 2 · Mandato da sessão

**Objectivo.** `mandato/encontrar-existente` — Localizar frameworks, sistemas de governo ou repositórios existentes que endereçassem a perda de enquadramento do arquitecto perante outputs de threads isoladas.

**Não-objectivos.**

| Slug | Conteúdo |
|---|---|
| `nobj/construir-governo` | construir um sistema de governo de raiz |
| `nobj/versao-degradada` | produzir versão reduzida por razões de custo |
| `nobj/disciplina-humana` | propor mecanismos dependentes de sessões de controlo |

**Critério de fim.** Lista de mecanismos necessários, cada um classificado como montável a partir de ferramenta existente ou como autoral.

**Pressuposto testado.** As arestas entre unidades de trabalho são recuperáveis a partir dos artefactos produzidos.

**Estado do pressuposto.** Invalidado fora de software.

**Emenda ao mandato.** Registada no turno 6, não declarada no momento: extensão do objectivo à redacção de protocolo. Classificada como deriva em R3.

## 3 · Documento recebido

| Nome | Slug | Origem | Resumo |
|---|---|---|---|
| `arquitectura-governo.md` | `doc/arquitectura-recebida` | sessão externa, 2026-09-19 20:05 | Arquitectura de governo em quatro partes — mandato, arquitectura, garantias permanentes, tensões em aberto. Cinco níveis hierárquicos, protocolos P0 a P2, seis actores, dezasseis garantias, cinco tensões declaradas. |

## 4 · Documentos produzidos

### Relatórios

| Nome | Slug | Resumo |
|---|---|---|
| `R1-mandato-e-exploracao.md` | `doc/r1-exploracao` | Mandato da sessão, sete ramificações com razões de poda, discriminante testado, treze ferramentas descobertas com aplicação, cinco objectos propostos e as suas substituições, dez mecanismos de imposição, quatro projecções do mapa, juízo de viabilidade. |
| `R2-leitura-da-proposta.md` | `doc/r2-leitura` | Leitura factual do documento recebido: conteúdo, seis elementos identificados como superiores, cinco críticas F1 a F5, sete alternativas A-1 a A-7 com estado, oito complementos, duas retractações, uma lacuna por aplicação do critério do próprio documento. |
| `R3-genese-mandato-global-arvore.md` / `.html` | `doc/r3-genese` | Génese do protocolo em três fontes e quatro operações, catorze elementos adoptados sem alteração, treze alterações, três não adoptados, formulação do mandato global e cinco consequências, tese sobre a natureza da árvore em seis secções. |
| `R4-implementacao-jardim.md` | `doc/r4-jardim` | Plano de implementação no Jardim: decisão de runner em duas vias com posição tomada, procedimento de arranque P0 em cinco passos, esqueleto de duas árvores, ordem de montagem em onze passos com esforço, regras sem objecto nesta escala, seis sinais de sucesso do piloto. |

### Protocolo

| Nome | Slug | Resumo |
|---|---|---|
| `PROTOCOLO-LEI.md` | `doc/protocolo-lei` | Lei. Vocabulário modal de três termos, cinquenta e três definições em ordem de dependência, onze conjuntos de regras P0 a P10 com identificador individual, secção de conformidade com quatro cláusulas. Sem justificação e sem comentário. |
| `PROTOCOLO-ANEXO.md` | `doc/protocolo-anexo` | Anexo de implementação. Quinze secções A1 a A15. Cada função com uma ou duas vias, o que cada via exige, o que custa e que regra serve. Tabela de ficheiros, ordem de montagem, correspondência regra-via, duas funções sem ferramenta. |
| `protocolo.html` | `doc/protocolo-html` | Lei e anexo num documento navegável, com alternância de tema. |

### Índice

| Nome | Slug | Resumo |
|---|---|---|
| `INDICE.md` | `doc/indice` | Este documento. |

## 5 · Dependências entre documentos

```
doc/arquitectura-recebida
        │
        ├──> doc/r2-leitura ──────┐
        │                         │
doc/r1-exploracao ────────────────┼──> doc/protocolo-lei ──> doc/protocolo-anexo
        │                         │              │
        └─────────────────────────┘              ├──> doc/protocolo-html
                                                 │
                                                 ├──> doc/r3-genese
                                                 │
                                                 └──> doc/r4-jardim
```

## 6 · Estado no fecho

| Item | Estado |
|---|---|
| Pressuposto `existe-ferramenta-completa` | invalidado |
| Decisão de via de runner para o Jardim | por tomar — bloqueia a sequência |
| Mandato do Jardim | por enunciar pelo humano responsável |
| Testes P0.14 a P0.21 sobre o Jardim | por correr |
| Montagem dos passos 1 a 6 | por iniciar |
| Passagem de equivalência A7 via 2 | adiada até incidente registado |
