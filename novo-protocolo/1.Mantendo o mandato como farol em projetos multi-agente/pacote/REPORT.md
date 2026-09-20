---
created: 2026-09-19 20:40
chat: Arquitectura de governo de projectos com agentes
summary: >
  Avaliação da sessão contra o seu mandato: o que era pedido, como cada entregue
  contribui, e as lacunas que ficaram por fechar.
---

# Report de sessão

## 1 · O mandato

**O mandato desta sessão não foi declarado no início.** Emergiu ao longo do trabalho e foi sendo corrigido cinco vezes. Isto é facto, não estilo: a sessão que desenhou um sistema para impedir deriva de objectivo correu ela própria sem objectivo declarado, e mudou de âmbito várias vezes sem o registar no momento.

Reconstruído a partir do que foi pedido:

> Determinar que instrumentos existem para manter o objectivo geral operante num projecto multi-frente conduzido por agentes, e produzir uma arquitectura que o garanta — aplicável a qualquer projecto, não a um em concreto.

**Não-objectivos, também reconstruídos:**

- Não produzir plano de aplicação a um projecto específico.
- Não escrever os protocolos finais.
- Não construir o que já existe em pacotes disponíveis.

**Mudanças de âmbito ao longo da sessão**, todas por pedido explícito e todas aceites:

| Momento | Alteração |
|---|---|
| 1 | de levantamento de instrumentos para desenho de arquitectura |
| 2 | de arquitectura nova para delta sobre sistema existente |
| 3 | de delta para arquitectura genérica outra vez |
| 4 | acrescento da camada de caminho e da autoria do mandato |
| 5 | acrescento da árvore, do escopo por nível, dos slugs e da escolha de runner |

A quantidade de correcções não é sinal de falha: cada uma fechou uma lacuna real. É sinal de que um mandato declarado à cabeça teria poupado trabalho — que é exactamente a tese do documento produzido.

## 2 · Como os entregues contribuem

| Entregue | Contribuição | Objectivo que serve |
|---|---|---|
| `arquitectura-governo.md` e página | o artefacto central: cinco camadas, três instrumentos transversais, quinze garantias | o mandato inteiro |
| Página do fluxo | especificação binária das sete fases; fonte para os protocolos | tornar a arquitectura executável |
| `debates/D-arquitectura-governo.json` | quinze decisões com alternativa rejeitada e razão | permitir reverter sem reconstituir a sessão |
| `handoff.json` | retoma a frio, validada pelo critério cold-read | continuidade |
| `INBOX/schema-debates.json` | o único item por processar, sem o abrir | evitar deriva de conversa |
| `NOTA.md` | resposta primeiro, uma página | regra de saída |

**O que cada um não faz.** A arquitectura não é protocolo — descreve e justifica, e por isso não pode ser aplicada directamente por um agente. A página do fluxo é a única peça já despida de justificação, mas cobre a execução, não o nascimento nem o caminho. Nenhum dos dois é executável sem o par lei/anexo que fica por escrever.

## 3 · Ficou completo?

**Completo ao nível do desenho.** As três perguntas do mandato têm resposta: existem instrumentos, estão inventariados com fontes; a arquitectura cobre nascimento, estratégia, execução, evolução e garantias; e é genérica.

**Incompleto em tudo o resto.** Sete lacunas, por ordem de custo.

### L1 · Nada foi testado

Nenhum mecanismo correu. O sistema inteiro é desenho. A probabilidade de o primeiro uso real revelar um modo de falha não previsto é alta, e o desenho não tem como saber qual.

### L2 · A arquitectura não passou pelos seus próprios testes

O documento exige de qualquer projecto um teste de discriminação e um teste de reformulação. Não foi submetido a nenhum dos dois. Não sabemos se três sessões limpas, lendo só este documento, classificariam o mesmo caso da mesma maneira — que é precisamente a garantia que ele promete.

### L3 · Calibração ausente

Tectos de frentes, quota por sessão, cadência de auditoria, limiar do detector semântico: todos referidos, nenhum com valor. Sem números, os mecanismos de contenção não contêm nada.

### L4 · Protocolos por escrever

A lei e o anexo não existem. É o próximo passo declarado, mas significa que hoje nenhum agente pode aplicar isto — só lê-lo.

### L5 · Mecanismos novos nunca exercitados

Escopo por nível, slugs com índice invertido, detecção por dependência e escolha de runner entraram nas últimas trocas. São os mais recentes e os menos discutidos. Os quatro parecem sólidos e nenhum foi contestado — o que também quer dizer que nenhum foi testado contra objecção.

### L6 · Custo de operação não estimado

Quanto custa, em tempo e em chamadas, correr o gate de fecho, o watcher com três passagens e a auditoria periódica. Se o custo por sessão for alto, o sistema é abandonado em silêncio — o modo de falha mais comum em governo, e o único que não deixa rasto.

### L7 · Alocação concreta de runners por preencher

A §2.4.10 define requisitos; a coluna de ferramentas fica por atribuir por falta de informação sobre as capacidades de cada runner disponível.

## 4 · Observação sobre a sessão

Foram várias horas de governo sobre governo, sem trabalho real por baixo. O documento produzido avisa contra isto em três sítios distintos — tecto do mandato, condição de morte das árvores, regra de que nenhuma regra nasce sem falha observada.

Isso não invalida o trabalho: a arquitectura é sólida e as correcções foram todas substantivas. Mas o teste dela não é a coerência interna, que está assegurada. É sobreviver ao primeiro projecto que a usar — e até lá nada aqui está provado.
