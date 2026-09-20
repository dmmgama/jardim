---
created: 2026-09-19 21:25
chat: Arquitectura de governo de projectos com agentes
summary: >
  Índice do pacote da sessão de 19 de Setembro de 2026: identificação, mandato,
  o que foi produzido e o que é cada ficheiro.
---

# Índice — sessão 2026-09-19

## Identificação

| | |
|---|---|
| **Sessão** | `2026-09-19-arquitectura-governo` |
| **Data** | 19 de Setembro de 2026 |
| **Modo** | rumo |
| **Estado** | fechada |

## Mandato

O mandato não foi declarado no início da sessão: emergiu ao longo do trabalho e foi corrigido cinco vezes. Reconstruído a partir do que foi pedido:

> Determinar que instrumentos existem para manter o objectivo geral operante num projecto multi-frente conduzido por agentes, e produzir uma arquitectura que o garanta — aplicável a qualquer projecto, não a um em concreto.

**Não-objectivos**, também reconstruídos: não produzir plano de aplicação a um projecto específico; não escrever os protocolos finais; não construir o que já existe em pacotes disponíveis.

O primeiro não-objectivo foi levantado por decisão no fim da sessão, com a proposta de aplicação ao Jardim.

## O que foi produzido

Uma arquitectura de governo em cinco camadas, com três instrumentos transversais, quinze garantias e cinco tensões em aberto. A especificação binária do fluxo de sessão em sete fases. Uma proposta de aplicação ao Jardim. E o pacote de entrega da própria sessão.

Quinze decisões fechadas, cada uma com alternativa rejeitada e razão. Um item por processar. Nenhum mecanismo testado.

## Ficheiros

### `arquitectura/`

| Ficheiro | O que é | Quando se lê |
|---|---|---|
| `arquitectura-governo.md` | **A fonte.** Mandato do sistema, árvore, caminho, desenvolvimento por níveis, evolução, garantias e tensões | para perceber o sistema inteiro, ou para escrever os protocolos a partir dele |
| `arquitectura-governo.html` | O mesmo conteúdo, navegável | para ler |
| `fluxo.html` | Especificação binária das sete fases de uma sessão, com o capítulo de handoff e o seu critério de validade | para implementar hooks e gates, ou para escrever a lei |

O `.md` e o `.html` da arquitectura têm o mesmo conteúdo. O `.md` é a fonte a editar.

### `aplicacao/`

| Ficheiro | O que é | Quando se lê |
|---|---|---|
| `jardim-implementacao.md` | Proposta de implementação no Jardim: quatro peças das dez, o que não implementar e porquê, particularidades do domínio físico, mandato-esboço | antes de decidir se se aplica, e ao aplicar |

### `pacote/`

| Ficheiro | O que é | Quando se lê |
|---|---|---|
| `NOTA.md` | Uma página, resposta primeiro: o que a sessão produziu, o que está decidido, o que está em aberto | **primeiro** |
| `REPORT.md` | Avaliação da sessão contra o seu mandato, com as sete lacunas por ordem de custo | para saber o que não está resolvido |
| `handoff.json` | Como retomar sem ler nada do que passou: pressupostos, por decidir, próximo passo, critério de conclusão | ao abrir a sessão seguinte |
| `debates/D-arquitectura-governo.json` | As quinze decisões, com alternativa rejeitada, razão e secções afectadas | quando algo falhar e for preciso saber que alternativa havia |
| `INBOX/schema-debates.json` | O único item por processar: schema canónico do registo de debates | na próxima triagem |

## Próximo passo

Escrever `PROTOCOLO-GOVERNO.md` e `ANEXO-GOVERNO.md` a partir de P0, P1 e P2 da arquitectura e das fases F1–F7 do fluxo.

**Feito quando** os dois ficheiros existem, a lei não contém nenhuma frase que justifique uma regra, o anexo não contém nenhuma regra nova, e cada regra da lei tem slug.

## Aviso

Nada foi testado. A arquitectura descreve mecanismos que nunca correram, com tectos, quotas e cadências por calibrar, e não passou pelos seus próprios testes de discriminação e reformulação. As sete lacunas estão no `REPORT.md`.
