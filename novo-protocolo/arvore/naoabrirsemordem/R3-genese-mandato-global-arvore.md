---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Génese do protocolo produzido, inventário do que foi adoptado e do que foi alterado,
  formulação do mandato global do conjunto e tese sobre a natureza da árvore.
---

# R3 · Génese, mandato global e árvore

## 1 · Como o protocolo foi gerado

**Três fontes.**

| Fonte | Contributo |
|---|---|
| Proposta de arquitectura recebida | camadas, actores, protocolos P0 a P2, mecanismos, garantias |
| Exploração de ferramentas | vias de implementação e identificação do que não existe |
| Método de decomposição | critérios de corte, exaustividade por propósito, triagem antes de dados |

**Quatro operações.**

1. Separação de géneros: a lei recebeu apenas regras; a implementação passou a anexo.
2. Atribuição de identificador a toda a norma que existia em prosa.
3. Fecho das lacunas identificadas por simetria com regras já existentes.
4. Conversão de cada mecanismo em vias, preservando a via original onde ela satisfaz a regra.

## 2 · Adoptado sem alteração

| Elemento | Onde ficou |
|---|---|
| Camada de caminho com pressuposto e regra de paragem | P2 |
| Escopo por nível e não-escrita ascendente | P4.4, P4.5 |
| Teste de reformulação e teste de discriminação de tarefa | P0.14 a P0.21 |
| Gate de fecho em dois graus | P4.9 a P4.13 |
| Detecção em três passagens | P7.5 a P7.9 |
| Quatro níveis de protecção por slug | P6.7 a P6.12 |
| Bloqueio que devolve identificador e nunca razão | P6.10, P6.11 |
| Alerta com estado e hash | P7.10, P7.11 |
| Watcher sem modelo | P7.4 |
| Regra de saída com conclusão à cabeça | P8.1, P8.2 |
| Cold-read sobre a acção seguinte | P8.3, P8.4 |
| Estado por substituição, evidência por acrescento | P8.5 a P8.7 |
| Recusa por indisponibilidade de hook | P9.3 |
| Quatro saídas de reavaliação | P2.8 |

## 3 · Alterado

| Alteração | Regra | Natureza |
|---|---|---|
| Teste de discriminação aplicado ao caminho | P2.11, P2.15 a P2.18 | simetria com P0.10 |
| Tecto numérico de árvores e de frentes | P0.5, P0.6, P1.9, P2.12 | limite que faltava ao risco declarado |
| Exaustividade por propósito convertida em regra | P1.11, P1.12 | prosa com identificador |
| Accionabilidade do corte convertida em regra | P1.13 | prosa com identificador |
| Substrato de arestas com invisibilidade ao agente | P5.1 a P5.3 | condição de execução tornada normativa |
| Cone afectado por travessia transitiva | P5.4 a P5.8 | mecanismo tornado obrigação |
| Alerta empurrado | P7.12 | remoção da dependência de consulta |
| Triagem invocada por máquina | P7.13 | remoção da dependência de convocação |
| Confronto de pesquisa contra ramos fechados | P6.14 a P6.16 | extensão da protecção do decidido |
| Projecção legível sem razão de fecho | P6.13 | omissão por desenho |
| Regra nova exige incidente registado | P10.1 | prosa com identificador |
| Auditoria com listagem fixa | P10.5 a P10.11 | prosa com identificador |
| Consequência de violação grave | C.4 | conformidade tornada operante |

## 4 · Não adoptado

| Elemento | Fundamento |
|---|---|
| Perfil reduzido sem repositório nem hooks | uma regra que não pode ser recusada é sugestão |
| Disciplina de leitura do arquitecto na ingestão | depende de convocação humana |
| Exclusão de projectos de frente única | o confinamento e a protecção do decidido operam sem paralelismo |

## 5 · O mandato global

O mandato de cada sessão foi encontrar ferramentas. O mandato do conjunto é outro.

**Formulação.** Libertar o humano responsável para o trabalho do projecto, transferindo integralmente para máquina a vigilância do alinhamento.

**Critério de fim.** Ausência de sessões cuja única função seja verificar se o trabalho continua alinhado.

**Não-objectivo central.** Produzir um sistema que funcione desde que alguém se lembre de o consultar.

**Consequências que decorrem da formulação.**

| Consequência | Manifestação no protocolo |
|---|---|
| A vigilância é executada, não convocada | P7.1, P7.2, P7.13 |
| A regra que não pode ser recusada não é regra | P9.1, P9.3 |
| O que se lê não é o que se guarda | P6.11, P6.13 |
| Nenhum nível precisa do quadro global | P4.4, P4.5 |
| O que foi fechado defende-se sozinho | P6.9, P6.14 |

**A quarta consequência é a que resolve o problema de origem.** O esquecimento do quadro global deixa de ser um risco quando nenhum nível o utiliza. A frente classifica contra o seu pressuposto; a triagem classifica contra os ramos que o alerta toca; o caminho classifica contra o mandato. O quadro global não é lembrado porque não é lido.

## 6 · Como este trabalho se aplica ao mandato global

| Contributo | Efeito |
|---|---|
| Inventário de vias | oito das dez funções deixam de ser construção |
| Identificação do que não existe | a escrita própria fica confinada à camada de caminho e ao escopo por nível |
| Duas lacunas de imposição | o caminho ganha teste; a ingestão perde a dependência de consulta |
| Separação de géneros | a lei passa a ser aplicável por máquina, não por leitura |
| Identificadores | toda a norma passa a ser invocável, auditável e testável |

O contributo é de montagem e de fecho, não de concepção. A concepção estava feita.

## 7 · A árvore

### 7.1 O que é

A árvore é a única estrutura do sistema que é simultaneamente objecto de trabalho e instrumento de controlo. Os ramos são unidades de trabalho. As arestas são o mecanismo de detecção. A mesma estrutura que organiza o pensamento é a que sinaliza a colisão.

Daqui decorre a sua propriedade mais estranha: **a árvore tem duas existências e nunca é lida por inteiro.**

A existência mecânica é completa — nós, arestas, estados, razões de fecho, níveis de protecção — e reside fora de todas as zonas de leitura. É consultada por travessia, nunca por leitura.

A existência epistémica é uma projecção filtrada — nós, estados e arestas, sem razões. É o que o humano vê. A omissão não protege segredos: retira o material com que se reabriria um ramo fechado.

Um agente não vê nenhuma das duas. Vê o seu próprio ramo e as fronteiras negativas dos ramos vizinhos.

### 7.2 O que a árvore não é

Não é um plano. Um plano ordena trabalho no tempo; a árvore parte um espaço. A ordem de execução vem do caminho, não da árvore.

Não é um índice. Um índice é derivado do que existe; a árvore precede o que existe e determina o que virá a existir.

Não é uma decomposição do entregável. A decomposição do entregável é uma árvore de caracterização — uma das quatro, e não a mais importante.

### 7.3 Como se desenvolve

Quatro operações, e só quatro.

**Nascer.** Com propósito e condição de morte declarados. Uma árvore sem condição de morte não morre, e uma árvore que não morre converte-se numa lista de tarefas com genealogia — mais difícil de encerrar do que uma lista sem genealogia, porque cada item aparenta justificação.

**Ramificar.** Um eixo por nó. Eixos compõem-se por níveis, nunca por mistura no mesmo nível. A ramificação cessa quando o corte deixa de produzir assimetria ou deixa de recair sobre variável controlável.

**Podar.** Com razão registada. A poda não é rejeição: é decisão de não aprofundar. O registo da razão é o que impede a reabertura.

**Fechar.** Com resultado registado. O fecho devolve ao caminho, e o cone a jusante é recalculado.

### 7.4 Três tempos

**Divergente.** Árvores concorrentes sobre o mesmo objecto, com eixos conceptuais distintos. A exaustividade é estrita numa árvore de problema e aspiracional numa de caracterização. Uma árvore única não é escolha: é inércia.

**Triagem.** Estimativa de ordem de grandeza e cenário extremo, antes de qualquer recolha de evidência. Um ramo cuja variação por um factor de dez não alteraria a decisão final é podado sem ser testado. Esta operação é gratuita e é a única que impede a árvore de gerar frentes em excesso.

**Convergente.** O caminho testa com dados caros o que a triagem deixou vivo. Cada pressuposto invalidado poda um subcone inteiro.

### 7.5 A propriedade que emerge

**Uma árvore madura é maioritariamente morta.**

Um sistema saudável acumula mais ramos podados e fechados do que abertos, e o valor concentra-se nos mortos. O ramo aberto diz o que se está a fazer; o ramo morto diz o que não se voltará a fazer, e é essa segunda informação que impede a repetição de trabalho meses depois.

A consequência prática inverte a leitura habitual: a árvore não é um mapa do que se vai fazer. É o registo do que se deixou de fazer, com uma franja viva na periferia.

### 7.6 Porque a árvore substitui o arquitecto

A pergunta de origem — como é que o arquitecto olha para os outputs sem perder o quadro — pressupõe que exista alguém a segurar o quadro.

Na árvore completa, o quadro não é segurado: é percorrido. Quando um ramo fecha, a travessia das arestas determina quem ficava à espera daquele resultado. A determinação é exacta, é instantânea e não depende de ninguém se lembrar da razão por que o ramo foi aberto.

O arquitecto deixa de ser o detentor do quadro e passa a ser o destinatário do alerta. É a única transformação que o mandato global exige, e a árvore é a estrutura que a torna possível.
