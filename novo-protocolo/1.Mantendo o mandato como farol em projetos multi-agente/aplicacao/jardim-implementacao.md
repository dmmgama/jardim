---
created: 2026-09-19 21:05
project: Jardim
chat: Implementação da arquitectura de governo no Jardim
summary: >
  Proposta de implementação faseada da arquitectura de governo no projecto Jardim,
  com o que não implementar, particularidades do domínio físico e exemplos preenchidos.
---

# Implementação no Jardim — proposta

## 1 · Recomendação

**Implementar quatro peças das dez, em cerca de oito horas, por esta ordem: mandato, árvores, caminho, registo de decisões.** Deixar de fora tudo o que existe para gerir paralelismo entre agentes — o Jardim tem uma pessoa, um empreiteiro e sessões sequenciais.

A razão para implementar não é o governo. É que o Jardim tem três decisões em aberto há meses — betonilha, pavimento, estilo — e um roadmap com fases datadas que a realidade já ultrapassou. As peças propostas são exactamente as que atacam isso.

## 2 · Diagnóstico

### O que já existe e funciona

| Peça da arquitectura | No Jardim |
|---|---|
| Fonte única | repositório local, desde Set 2026 |
| Estado curado | `ESTADO.md` por tema |
| Registo negativo | `REJEICOES.md` com o porquê |
| Separação caos/entrega | `research/` e `entregue/` com nota |
| Travão intra-sessão | `Rascunhos.md`, que acaba em branco |
| Re-ancoragem | `Arvore.md` |
| Canónico vs histórico | `90-ARQUEOLOGIA`, consulta mas não obedece |
| Isolamento por escrita | `T00X/CLAUDE.md` governa a pasta |
| Caracterização canónica | `Planta_e_Espaco_Fisico.md`, ficheiros de imagem canónicos |

### O que falta

| Lacuna | Consequência observável |
|---|---|
| Não há mandato | não existe critério para recusar uma ideia |
| Não há não-objectivos | tudo o que é bonito cabe no projecto |
| Não há árvore de decisão | pavimento e estilo em aberto sem espaço de opções mapeado |
| Não há caminho com pressupostos | o roadmap é sequência de entregáveis, não de coisas a descobrir |
| Janelas irreversíveis não são tratadas como tal | a barreira de rizomas só é económica durante a escavação da Fase 1 |
| Decisões sem slug | o que foi decidido reabre sob outro nome |
| Nada reavalia quando algo derrapa | as fases têm datas que já passaram e nada disparou |

## 3 · O que não implementar

Esta secção vale mais do que a seguinte.

| Peça | Porquê não |
|---|---|
| **Worktrees** | um repositório de documentos, um autor, sessões sequenciais. O isolamento resolve um problema que não existe |
| **Hooks de confinamento** | sem múltiplas frentes simultâneas não há zona alheia para invadir |
| **Passagem de colisão do watcher** | duas frentes a tocar no mesmo ficheiro é caso raro aqui |
| **Proveniência selada** | o repositório com histórico já dá rastreabilidade suficiente para um projecto pessoal |
| **HALT** | nada corre sem o David presente |
| **Quota de escrita por sessão** | o volume não justifica árbitro automático |
| **Gate de fecho automatizado** | a verificação manual no fecho chega a este ritmo |

Implementar estas sete transformaria o Jardim num exercício de governo. O sinal de que a decisão está certa: cada uma resolve um sintoma que o Jardim não tem.

## 4 · O que implementar

### J1 · Mandato — 1 hora

O ficheiro que falta e que torna tudo o resto possível. Uma página, com três a cinco objectivos e dois a três não-objectivos por objectivo.

O agente redige por reformulação; a validação é tua, por dois testes — reformulação e discriminação.

**Clarificação de uma ambiguidade do protocolo.** P0.6 proíbe o agente de acrescentar objectivos ou não-objectivos que o humano não enunciou; o teste de reformulação pede-lhe que derive não-objectivos não enunciados e acerte. Não se contradizem, mas a ordem importa: o agente **propõe** como demonstração de compreensão, e só entram no ficheiro depois de confirmados. Proposta não é acrescento.

**Critério de desbloqueio.** Três ideias plausíveis para o jardim — duas dentro, uma fora mas parecida. Três sessões limpas. Classificam igual → J1 fechada.

### J2 · Duas árvores acopladas — 2 horas

É o caso que motivou os quatro propósitos. Duas árvores, nunca fundidas.

**Árvore de caracterização** — o que é este objecto. Aberta: ramos nascem da investigação. Muito dela já existe dispersa: cardinalidade, exposição solar, espécies, cotas, estado da betonilha. Passa a ter forma de árvore e estados de ramo.

**Árvore de decisão** — o que quero. Ramos: estilo, pavimento, betonilha, água, luz, arte. Profundidade deliberadamente desigual.

**As arestas são o ponto.** Cada ramo de decisão declara de que ramo de caracterização depende, no momento em que é desenhado. Exemplos directos:

```
decisao/pavimento/relva-natural  →  depende de  caracterizacao/sol/verao
decisao/pavimento                →  depende de  caracterizacao/betonilha/estado
decisao/agua/lago-em-u           →  depende de  caracterizacao/palmeira/rizomas
```

Quando o ramo de caracterização fecha, o de decisão reavalia: aprofundar ou podar. É exactamente o que descreveste — o estudo não decide por ti, muda o significado das opções.

### J3 · Caminho — 2 horas

Converter o roadmap de sequência de entregáveis em sequência de pressupostos.

O roadmap actual diz o que fica pronto e quando. O caminho diz o que tem de ser verdade para que valha a pena, e o que se faz se não for.

Pressupostos candidatos, a validar e ordenar por ti:

| Pressuposto | Regra de paragem | Janela |
|---|---|---|
| A barreira de rizomas é a acção de maior alavancagem | se a escavação revelar outro constrangimento maior, reordenar | **só durante a Fase 1** |
| Relva natural é viável com a sombra existente | se a caracterização der menos de X horas de sol directo no Verão, muda para o ramo alternativo | antes de fechar o pavimento |
| O empreiteiro executa dentro do protocolo de três tranches | se falhar um marco visível sem explicação, rever o âmbito antes de pagar | contínua |
| O artista visita o jardim nocturno antes de pintar | se não visitar, a Fase 6 não arranca | Jan–Fev 2027 |

**Pressupostos com janela são a particularidade deste projecto.** Um pressuposto que só pode ser testado durante uma obra que acontece uma vez tem custo de descobrir tarde praticamente infinito. Na ordenação de M5, sobe sempre ao topo.

**Primeiro uso real do caminho:** reconciliar com o que derrapou. O roadmap tem fases com datas que já passaram. Isso não é falha do roadmap — é o que acontece a qualquer plano. Mas é a reavaliação que nunca foi disparada, e é o melhor primeiro exercício possível para o mecanismo.

### J4 · Registo de decisões com slugs — 3 horas

Slugs em decisões e ramos. Índice gerado por inversão. Um ficheiro por decisão, com alternativa rejeitada e razão.

Duas coisas concretas que isto resolve no Jardim:

A **identificação da árvore** — uma hipótese foi confirmada e outra descartada. Com slug e decisão registada, a hipótese descartada fica morta e não volta a aparecer num documento novo.

A **reabertura de decisões fechadas.** É o padrão típico de um projecto que vive meses com decisões de gosto: fecha-se, esquece-se a razão, reabre-se com outro nome. O slug morto bloqueia a recriação.

Não é preciso hook automático nesta fase — basta o índice e a disciplina de o consultar antes de reabrir. Automatiza-se quando doer.

## 5 · O que a arquitectura genérica não cobre

Quatro particularidades deste domínio, que valem como extensão local e podem valer como emenda ao documento geral.

### 5.1 Actor humano externo

O empreiteiro está fora de todas as zonas, não lê nenhum ficheiro, e executa a partir de conversa e visita. O protocolo que o governa já existe e é sólido: telefonar em vez de escrever, fechar âmbito no local, confirmar por escrito curto, pagar por marcos visíveis, dizer o quê e onde e nunca o como.

**Consequência para a arquitectura:** existe uma fronteira onde o sistema termina e começa relação humana. O que atravessa essa fronteira não são ficheiros — são decisões já fechadas. Uma decisão que chega ao empreiteiro ainda em aberto vira improviso no terreno.

### 5.2 Irreversibilidade física

Nenhum gate protege contra betão já vazado. É a diferença de fundo entre este projecto e um de software.

**Extensão proposta:** um ramo ou pressuposto marcado `irreversivel` exige confirmação humana antes de passar a trabalho, e é o único caso em que o `Rascunhos.md` é lido antes do fecho — para verificar se alguma tensão registada e não resolvida toca naquela decisão. Esse mecanismo já existe no teu fluxo; falta apenas a marca que o dispara.

### 5.3 Dinheiro em tranches

As tranches estão atadas a marcos físicos visíveis. Isso é, na linguagem da arquitectura, exactamente uma regra de paragem — só que com consequência financeira.

**Consequência:** as tranches entram no caminho como regras de paragem, não no roadmap como calendário. Nunca pagar à frente do trabalho feito é a regra de paragem mais bem escrita de todo o projecto.

### 5.4 Atenção dispersa

O Jardim é o maior multiplicador pessoal e o mais em risco de atenção dispersa. A arquitectura não tem mecanismo para isto, e não deve ter — é gestão de prioridades, não de projecto.

O que ela dá é indirecto: uma frente com pressuposto e regra de paragem torna visível quando parou. Um roadmap com datas não.

## 6 · Exemplo preenchido

Esboço para reagires, não para aceitares. É reformulação da tua intenção a partir do que está registado, sujeita aos dois testes.

```markdown
# Mandato — Jardim
v1 · 2026-09-19

## Objectivos
G1. Jardim mediterrânico de dia e instalação de arte UV à noite, nos 75 m².
G2. Espaço utilizável todos os dias por uma família, não um jardim de exposição.
G3. Intervenção faseada e reversível, excepto onde a física obriga.

## Não-objectivos
NG1. Não é um jardim de manutenção intensiva.
NG2. Não é uma colecção botânica — as espécies servem a composição.
NG3. Não é uma obra única: nenhuma fase depende de todas as outras acontecerem.
NG4. Não se compra solução definitiva para decisão ainda em aberto.

## Critério de aceitação
Termina quando as seis fases estiverem executadas e o jardim for usado de noite
sem nada por acabar à vista.

## Casos decididos
C1. Comentários de exposição solar em fonte textual → não são facto. Só imagens e
    observação no local. Exclui: inferir orientação a partir de descrições.
```

E um ramo, com a forma que passam a ter:

```yaml
slug: decisao/pavimento/relva-natural
arvore: decisao
estado: suspenso
depende_de: [caracterizacao/sol/verao, caracterizacao/betonilha/estado]
serve: G2
triagem: passou          # se a relva falhar, muda a utilização diária — discrimina
irreversivel: false
```

## 7 · Critério de sucesso e plano de falha

A implementação resulta se, dentro de um mês:

| Critério | Verificação |
|---|---|
| As três decisões em aberto fecharam ou têm dependência declarada | `arvores/decisao` |
| A reconciliação do roadmap produziu uma reavaliação registada | `CAMINHO` |
| Nenhuma ideia nova entrou sem passar pelo mandato | `REJEICOES` tem entradas |
| O pressuposto da barreira de rizomas está no topo da ordem | `CAMINHO` |

**Se ao fim de um mês nada disto for verdade**, a conclusão não é que faltam mecanismos. É que o sistema não está a ser usado, e a resposta certa é reduzi-lo a J1 e J2 — mandato e árvores — que são as duas peças que funcionam sem disciplina nenhuma.

## 8 · Riscos

| Risco | Sinal | Mitigação |
|---|---|---|
| Implementar governo em vez de fazer o jardim | J1 a J4 demoram mais de duas sessões | tecto duro: oito horas, e nenhuma peça extra |
| Árvore de caracterização eterna | ramos novos a nascer sem nenhum a fechar | condição de morte declarada: fecha quando as decisões que dela dependem estiverem tomadas |
| Mandato a papaguear o que já está escrito | passa o teste de discriminação e falha o de reformulação | rejeitar e discutir, não reescrever |
| Janela da Fase 1 perdida enquanto se desenha o sistema | a escavação acontece antes de J3 estar feito | se a Fase 1 estiver iminente, J3 vem antes de J2 |

O último é o único risco com data. Se a escavação estiver perto, inverte a ordem e trata primeiro do caminho — o resto espera, a barreira de rizomas não.
