---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Plano de implementação do protocolo no projecto Jardim: decisão de runner em duas vias,
  procedimento de arranque, esqueleto de árvores, ordem de montagem e critério de sucesso.
---

# R4 · Implementação no projecto Jardim

## Conclusão

**Adaptar, não recomeçar.** O que existe no Jardim é matéria de trabalho, não governo; nada nele colide com o protocolo. O arranque consiste em instalar o governo por cima do que já foi produzido e reclassificar esse material como ramos.

**A decisão bloqueante é o runner, não o conteúdo.** Sem hooks bloqueantes, o protocolo degrada-se em sugestão e perde a sua tese. A escolha entre as duas vias abaixo determina tudo o resto e deve ser tomada antes de qualquer escrita.

**O valor do Jardim não é o Jardim.** É o banco de ensaio: um projecto de consequência baixa onde a maquinaria falha barato antes de carregar trabalho que importa.

---

## 1 · A decisão de runner

### Via 1 — repositório com imposição

O Jardim passa a repositório. Frentes em árvores de trabalho separadas. Hooks bloqueantes no runner que escreve. Substrato de arestas em base de ficheiro único fora das zonas.

| | |
|---|---|
| Satisfaz | P3.2, P4.1, P4.7, P5.3, P6.7 a P6.9, P9.1 a P9.3 |
| Exige | repositório, runner de agente com ganchos, cerca de um dia de montagem |
| Custo corrente | o trabalho do Jardim passa a fazer-se em ambiente de código |
| Efeito colateral | a montagem fica feita e transferível para os projectos seguintes |

### Via 2 — projecto em interface de conversa

O Jardim permanece onde está. Os documentos de governo são conhecimento do projecto. As frentes são conversas separadas arrancadas com o mandato de frente.

| | |
|---|---|
| Satisfaz | P0, P1, P2, P3.1, P3.3 a P3.10, P4.3 a P4.6, P8 |
| Não satisfaz | P5.3, P6.7 a P6.9, P7.1, P7.2, P7.12, P9.1 |
| Exige | nada |
| Custo corrente | nenhum |
| Limite | nada recusa. Uma frente que escreva fora da sua zona não é bloqueada, é apenas incorrecta |

### Posição

**Via 1.** A Via 2 preserva a camada que organiza o pensamento e perde inteiramente a camada que a torna executável — que é a metade que não existe em mais lado nenhum e a única razão para construir isto. Um ensaio da Via 2 não ensaia nada: valida um método que já se sabe correcto e não testa o mecanismo que ainda não se sabe se funciona.

**Se a Via 1 for recusada,** o Jardim não serve de piloto e o piloto deve ser outro projecto que já viva em repositório.

---

## 2 · Arranque · P0

O mandato não pode ser escrito por mim. P0.8 proíbe inscrever objectivo ou não-objectivo que não tenhas enunciado. O que segue é o procedimento, não o conteúdo.

**Passo 1.** Enuncias, sem estrutura, o que queres do Jardim e o que recusas.

**Passo 2.** Reformulo em mandato com slugs, entre um e cinco objectivos, dois a três não-objectivos por objectivo, critério de fim, tectos e canal de alerta.

**Passo 3.** Teste de reformulação, P0.14 a P0.18. Derivo um não-objectivo que não enunciaste, classifico uma tarefa-fronteira construída no momento, enuncio o que o mandato exclui, nomeio a tensão entre dois objectivos e digo qual cede. Confirmas ou rejeitas cada um.

**Passo 4.** Teste de discriminação, P0.19 a P0.21. Três tarefas, três sessões limpas.

**Passo 5.** Só depois abre a primeira frente.

**Campos que o mandato do Jardim tem de fixar e que não dependem de mim:**

| Campo | Regra |
|---|---|
| Critério de fim — o que existe quando o Jardim está feito | P0.4 |
| Tecto de árvores simultaneamente abertas | P0.5 |
| Tecto de frentes simultaneamente abertas | P0.6 |
| Canal para onde o alerta é empurrado | P7.12 |
| Cadência da auditoria, não mais frequente que mensal | P10.2, P10.3 |

**Sugestão de tectos para escala de projecto doméstico:** duas árvores, duas frentes. Fica à tua decisão; o valor é normativo depois de inscrito.

---

## 3 · Esqueleto de árvores

Proposta para validação. Nenhum ramo passa a frente antes de P1.5.

**Árvore de caracterização — `arv/sitio`.** Propósito: o que é este objecto. Exaustividade verificada ao fechar, P1.12. Condição de morte: quando todos os ramos vivos estiverem fechados ou podados e nenhum ramo novo tiver nascido durante um ciclo de auditoria.

Eixo do primeiro nível: domínio físico. Ramos candidatos — solo, água, luz e sombra, estrutura existente, acessos.

**Árvore de decisão — `arv/programa`.** Propósito: o que queres. Profundidade deliberadamente desigual, permitida. Condição de morte: quando o caminho for declarado escolhido.

Eixo do primeiro nível: função do espaço. Ramos candidatos conforme o mandato.

**Acoplamento.** `arv/programa` declara arestas para os ramos de `arv/sitio` de que depende, no acto em que é desenhada, P1.4. As duas árvores não se fundem, P1.8.

**O ramo que altera os outros.** A questão de que especialidades devem compor a análise não é um ramo: é um eixo de corte. Deve ser resolvida antes de `arv/programa` ramificar, sob pena de a árvore ser redesenhada depois de ter gerado frentes.

---

## 4 · Ordem de montagem no Jardim

| Ordem | Peça | Via | Esforço |
|---|---|---|---|
| 1 | Repositório e árvores de trabalho | A4 | 1 h |
| 2 | Hook de zona | A2 via 1 | 2 h |
| 3 | Esquema dos ficheiros de troca | A3 | 1 h |
| 4 | Substrato de arestas e cone afectado | A1 via 2 | 3 h |
| 5 | Slugs e índice de decisões | — | 1 h |
| 6 | Gate de fecho | A2 via 1 | 2 h |
| 7 | Watcher, passagens de colisão e dependência | A4 | 2 h |
| 8 | Alerta empurrado e invocação da triagem | A8 via 2 | 2 h |
| 9 | Cold-read | A6 via 2 | 1 h |
| 10 | Proveniência selada | A5 via 2 | 1 h |
| 11 | Auditoria por cadência | A9 via 1 | 1 h |

Os passos 1 a 6 impõem e são condição de P0.11 na Via 1. Os passos 7 a 8 são o que transforma o sistema em automático. Os passos 9 a 11 verificam.

**A passagem de equivalência, A7 via 2, fica de fora do arranque.** A extensão está em fase anterior à versão 1 e a via 1 por slug cobre o caso comum. Entra quando houver incidente que a justifique, P10.1.

**Geração de mandatos de frente, A11.** Via 1 no arranque. A via 2 entra se o número de frentes crescer para além do que compensa escrever à mão.

---

## 5 · Regras sem objecto nesta escala

Nenhuma regra é dispensada. As seguintes não terão disparo previsível no Jardim e permanecem em vigor:

| Regra | Razão de não disparar |
|---|---|
| P2.12 | com tecto de duas frentes, raramente se atinge |
| P7.6 | colisão de ficheiros exige paralelismo que o tecto limita |
| P10.11 | volume insuficiente para gerar slugs equivalentes |
| P9.6 | um único runner previsto |

Uma regra que não dispara não é uma regra a remover. É a condição em que P10.1 opera: só se remove o que produziu falso positivo registado.

---

## 6 · Critério de sucesso do piloto

O Jardim não valida o protocolo por produzir um jardim. Valida-o por produzir sinais.

| Sinal | Leitura |
|---|---|
| O alerta chega sem ser pedido | P7.12 funciona |
| O alerta vazio é o caso normal | a detecção está calibrada |
| Uma escrita fora de zona é recusada, ao menos uma vez | P3.2 é imposição e não convenção |
| Um ramo fechado gera cone afectado correcto | P5.7 funciona |
| Nenhuma sessão é convocada para verificar alinhamento | o mandato global cumpre-se |
| Uma tentativa de reabrir ramo podado é sinalizada | P6.9 funciona |

**Contra-sinal.** Se ao fim de três ciclos de auditoria o alerta disparar sempre, a detecção está mal calibrada. Se nunca disparar e houver colisões reais, as arestas estão mal declaradas. Ambos são falhas do sistema, não do Jardim.

---

## 7 · Sequência imediata

1. Decides a via de runner.
2. Enuncias a intenção do Jardim, sem estrutura.
3. Redijo o mandato e corro P0.14 a P0.21.
4. Desenhamos `arv/sitio` e `arv/programa` com as arestas declaradas.
5. Monto os passos 1 a 6.
6. Abre a primeira frente sobre o discriminante do topo.

O passo 1 bloqueia todos os restantes.
