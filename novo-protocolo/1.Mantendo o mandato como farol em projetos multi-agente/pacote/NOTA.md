---
created: 2026-09-19 20:40
chat: Arquitectura de governo de projectos com agentes
summary: >
  Nota de entrega do pacote da sessão: o que foi produzido, o que está decidido,
  o que está em aberto e qual o próximo passo.
---

# Nota de entrega

**A sessão produziu uma arquitectura de governo para projectos multi-frente conduzidos por agentes, completa ao nível do desenho e por validar na prática.** Quinze decisões fechadas com alternativa registada, cinco tensões em aberto, nenhum mecanismo testado.

## O que está no pacote

| Ficheiro | O que é |
|---|---|
| `NOTA.md` | este ficheiro |
| `REPORT.md` | avaliação da sessão contra o seu mandato, com as lacunas |
| `handoff.json` | como retomar sem ler nada do que passou |
| `debates/D-arquitectura-governo.json` | as quinze decisões, com alternativas rejeitadas |
| `INBOX/schema-debates.json` | o único item por processar |

A arquitectura está em `arquitectura-governo.md` e na página publicada. Não é duplicada aqui.

## O que está decidido

A arquitectura assenta em cinco camadas — mandato, caminho, estado, frente, sessão — com três instrumentos transversais: a árvore como partição do espaço, os hooks como enforcement determinístico, e o registo de decisões como protecção do que foi debatido.

Três decisões carregam o resto. **O controlo é da escrita, não da leitura** — vedar ficheiros reduz ruído, não produz alinhamento. **Cada nível classifica contra o nível imediatamente acima, nunca contra o topo** — o que torna o escopo de contexto seguro. E **mudar de caminho não é mudar de rumo** — o que impede que cada surpresa técnica se transforme numa revisão do projecto.

## O que está em aberto

Um item por processar: o schema canónico do registo de debates, com quatro pontos por definir.

Cinco tensões, todas na §4 da arquitectura. A mais provável de morder é T1 — se declarar dependências não for barato no momento em que o ramo nasce, o detector mais valioso do sistema cala-se sem dar sinal.

## Próximo passo

Escrever `PROTOCOLO-GOVERNO.md` e `ANEXO-GOVERNO.md` a partir de P0, P1 e P2.

Feito quando os dois ficheiros existem, a lei não contém nenhuma frase que justifique uma regra, e o anexo não contém nenhuma regra nova.

## O que este pacote não resolve

Nada foi aplicado. A arquitectura descreve mecanismos que nunca correram, com tectos, quotas e cadências por calibrar. O primeiro projecto real que a usar vai encontrar coisas que este desenho não previu — e o sinal de que o sistema funciona será ele próprio absorver isso sem crescer.
