---
created: 2026-09-19 20:05
revised: 2026-09-20 19:30
summary: >
  Arquitectura de governo para projectos multi-frente conduzidos por agentes: definições,
  mandato, árvore (definição, porta de entrada, roteamento e modos), caminho, desenvolvimento
  por níveis, alocação de papéis, evolução, regra de saída, garantias, auditoria, tensões
  e esquemas fechados dos ficheiros.
---

# Arquitectura de governo de projectos com agentes

**Convenção de leitura.** Cada §2.x tem três blocos, por esta ordem: *Conceitos* (define o que as regras usam), *Regras* (só alíneas identificadas `Pn.m`, cada uma com força, detector e consequência) e *Nota* (racional; não vincula). Uma obrigação só existe se tiver identificador; prosa a negrito não obriga.

**Vocabulário normativo.** **deve** = obrigatório; **não pode** = proibido; **pode** = permitido.

**Colunas das regras.** *Força* ∈ {mecânica, convenção}: **mecânica** quando o detector decide o caso sozinho, por esquema, contagem, comparação ou presença de campo; **convenção** quando a verificação exige julgamento. Uma regra de força `convenção` declara `alerta`, `fecha com marca` ou `relatório`, nunca `bloqueia` (P7.3). *Detector* ∈ {hook, gate, watcher, auditor, humano}. *Consequência* ∈ {bloqueia, fecha com marca, alerta, relatório}.

**Numeração aditiva.** Uma regra nova recebe o número seguinte do seu protocolo. Nunca se insere no meio, nunca se renumera. Uma regra partida em duas metades com detectores distintos mantém o identificador em ambas, qualificado. Uma regra retirada mantém o identificador com grau `morta` (P5.5).

---

## 0 · Definições

Entrada única por termo. Todos os usos posteriores remetem para aqui. Os nomes de ficheiro não são entradas do léxico: definem-se em §2.4.5 e no Anexo A.

| Termo | Definição |
|---|---|
| **Frente** | Unidade de trabalho de nível L3 que testa um pressuposto ou executa um caminho. Tem projecção, zona, toca declarada e gate de fecho. |
| **Ramo** | Nó de uma árvore. |
| **`suspenso: <ramo>`** | Ramo bloqueado por dependência declarada. Tem sempre referente. |
| **`retido`** | Ramo que não discrimina, guardado sem poda. Não tem referente. Só em modo Caracterização, e só enquanto a árvore vive (P1.14). |
| **Aresta** | Dependência declarada entre ramos, por referência qualificada `{arvore_slug, no_slug}` (P1.4). |
| **`cone_estrutural`** | Subárvore de um nó: o nó e os seus descendentes por `pai`. |
| **`cone_de_dependencia`** | Conjunto de ramos alcançáveis a jusante por travessia de arestas a partir de um ramo. |
| **Driver** | Variável cuja variação muda o resultado. Um eixo não a pode repartir por ramos irmãos (P1.2). |
| **Transversal** | Factor que condiciona todos os ramos de uma árvore. Declara-se ao nível da árvore, com slug; não é ramo nem aresta (P1.10). |
| **Modo de árvore** | Um de Problema, Caracterização, Decisão, Mandato (§2.2.1). Determina raiz, forma, crivo, poda e morte. |
| **Árvore** | Partição de um espaço por eixos. Quatro modos (§2.2.1). Detalhe operacional no canon `protocolo-arvore-definicao-e-uso` v2, com compatibilidade declarada em `canon/regras.json`. |
| **Eixo** | Critério de divisão de um nó em ramos. |
| **Caminho** | Hipótese, hoje, sobre como se chega ao mandato (§2.3). Nunca designa uma localização no sistema de ficheiros. |
| **Trajecto** | Localização no sistema de ficheiros. Cada trajecto tem nível, modo de escrita e classe de integridade, declarados em `TRAJECTOS`. O *hook de trajecto* confina leitura e escrita por perfil. |
| **Pressuposto** | Afirmação que tem de ser verdade para um caminho valer. |
| **Discriminante** | Pressuposto cuja resposta elimina caminhos. |
| **Regra de paragem** | Critério, escrito antes de a frente abrir, que dá o teste de um pressuposto por decidido. |
| **Projecção** | O objectivo de uma frente: o pressuposto que testa, mais a regra de paragem. Fronteiras negativas: os pressupostos atribuídos às outras frentes. Deriva-se do caminho; não se redige. Vive no bloco `projeccao` de `estado.json` e é selada na abertura. Único nome deste conceito. |
| **Perfil** | Papel que uma sessão declara ao arrancar (`frente`, `triagem`, `rumo`, `caminho`, `verificacao`, `auditor`). Determina o contexto montado, a zona e a classe de integridade máxima de leitura. Declarado em `PERFIS`. |
| **Zona** | Conjunto de trajectos onde um perfil pode escrever. Declarada em `PERFIS`. |
| **Toca** | Lista de slugs e trajectos que uma frente altera. Tem duas formas: `toca_declarado[]`, write-once na abertura e fora da zona da frente, e `toca_efectivo[]`, calculado do diff no fecho (P3.21). |
| **Slug** | Identificador único no espaço de nomes do projecto, para documentos, regras, decisões, ramos, pressupostos, itens e achados. Nunca reutilizado nem renumerado. O espaço de nomes liberta-se no encerramento (P5.12). |
| **Alerta** | Item produzido pelo watcher. O seu estado-do-alerta vive em `alerta-estado.log`. |
| **Aviso de protecção** | Resposta do hook a uma edição de slug com decisão registada: identificador da decisão e grau de protecção, e nada mais (P3.9). Não é alerta. |
| **Triagem** | Actor: sessão fria de agente, disparada por alerta, que escreve `ESTADO`, `REJEICOES`, `CASOS`, `ESCALADAS`, `alerta-estado.log` e o estado dos itens do `INBOX`. Designa só o actor. |
| **Crivo de ordem de grandeza** | Filtro pré-dados que descarta um ramo cuja variação por um factor de dez não alteraria a causa provável (Problema) ou a opção escolhida (Decisão). Não é a triagem. O canon operacional chama-lhe "triagem". |
| **Watcher** | Script sem modelo, disparado a cada merge, que corre as três passagens de detecção (§2.4.8), verifica a presença dos hooks e regista a corrida. |
| **Detector semântico** | Chamada única de modelo, sem estado, invocada pelo watcher, com timeout declarado. Devolve sugestão, nunca facto. Indisponível, produz item de passagem `semantico_indisponivel`. |
| **Gate** | Verificação no fecho de sessão (S6). Dois patamares: *duro* bloqueia o fecho; *brando* fecha com marca. |
| **Cold-read** | Verificação de um output por agente sem histórico, do perfil `verificacao`, com pergunta fechada sobre a acção seguinte. Valor: `passa`, `falha` ou `nao_corrido`. |
| **`carece_aprovacao`** | Marca que um fecho brando deixa em `estado.json`. Só é levantada em `APROVACOES`, por actor distinto da frente (P3.28). |
| **Modo rumo** | Sessão aberta só pelo humano para reavaliar o mandato. Produz emenda ou nada. |
| **Emenda** | Alteração datada ao `MANDATO` ou ao canon, com decisão em `debates/` que regista a alternativa rejeitada. |
| **Sonda de fronteira** | Tarefa-fronteira classificada por três sessões com dissimilaridade declarada, contra o mandato: o teste de discriminação (§2.1.1) repetido em auditoria. |
| **Dissimilaridade declarada** | Condição de um conjunto de juízes: modelos ou fornecedores distintos, ou o humano como terceiro juiz, registada com `modelo` e `versao` por veredicto. Três amostras do mesmo modelo não a cumprem. |
| **Página** | 500 palavras, contadas pelo hook sobre os valores de texto, excluindo chaves e slugs. Aplica-se a `MANDATO` e `CAMINHO`. |
| **Worktree** | Cópia de trabalho isolada de uma frente. O merge é a verificação. |
| **Merge** | Integração da worktree de uma frente no tronco. Tem dois desfechos: integrado, ou `merge_pendente` (P3.20). Dispara a regeneração do índice e a corrida do watcher. |
| **Sessão** | Unidade de nível L4: um arranque com perfil declarado, trabalho, e um fecho que passa pelo gate. Não tem estado de espera (P3.12). |
| **Handoff** | Output de fecho que permite a outra sessão retomar a frente: próximo passo, critério de conclusão, pressupostos assumidos, referências e bloqueio. Validado por cold-read. |
| **`Rascunhos`** | Travão intra-sessão para o que sai da projecção. Termina vazio; o que sobrevive converte-se em item `descoberta` (P3.26). |
| **Milestone** | Teste de um pressuposto, não entregável. A pergunta é o que fica a saber-se. |
| **Classe de integridade** | Atributo de uma fonte de leitura: `canon`, `produzido_sob_gate` ou `nao_verificado`. Conteúdo `nao_verificado` entra marcado e só como dado (P3.23). |
| **Corrida** | Execução única do watcher sobre um merge, registada em `corridas/<id>.json` com as passagens executadas e os itens emitidos. |
| **Selagem** | Escrita write-once em `sealed/` de referências ao pedido, ao output e ao contexto, com hash de conteúdo. Faz-se em duas fases: antes do merge e depois da corrida do watcher (P3.17). |
| **Modo de escrita** | Um de `substituicao`, `acrescento`, `log`, `write_once`, declarado por trajecto em `TRAJECTOS`. Não se troca (P3.4). |
| **Modo degradado** | Estado do projecto com o responsável indisponível além do prazo declarado: as frentes abertas continuam, nenhuma abre, e o facto fica registado (P0.13). |
| **Orçamento** | Tecto declarado no `MANDATO` de chamadas de modelo por merge e por fecho e de horas-humano por mês para auditoria (P0.10). |
| **Limiar** | Valor numérico declarado no `MANDATO`, com justificação e data de revalidação (P7.6). |
| **Caducidade** | Prazo ao fim do qual um estado expira sem acto: o `visto` de um alerta (P3.10) e o próprio canon (P5.10). |
| **Força** | Atributo de uma regra: `mecânica` ou `convenção`, nos termos das Colunas das regras. Registado em `canon/regras.json`. |
| **Teste negativo** | Execução que demonstra que um detector recusa o caso que a sua regra proíbe. Condição de entrada em vigor de regra mecânica (P4.7). |
| **Achado** | Item produzido pelo auditor, com slug, dono, prazo e estado-do-achado, em `ACHADOS`. |
| **Escalada** | Passagem de um item da triagem para o humano, com payload, razão, objectivo tocado, prazo e estado, em `ESCALADAS` (P3.15). |
| **Runner** | Execução concreta onde um papel corre: processo, serviço ou interface. Declarado por perfil em `PERFIS`. Muda por decisão registada (P4.4). |
| **Orquestrador** | Actor que dispara a abertura de frente. Disparo declarado, zona nula (P4.9). |
| **Nível** | Só designa L0–L4 (§2.4.1). Os patamares do gate, os graus de protecção e os graus de regra não são níveis. |
| **Grau de protecção** | Estado de um slug face ao índice de decisões: `livre`, `decidido`, `selado`, `morto` (§2.4.8). |
| **Grau de regra** | Estado de uma regra no canon: `viva`, `postulada`, `morta` (P5.9, P5.5). |
| **Incidente** | Item de `INBOX` do tipo `falha_de_sistema`. Pré-condição de regra nova (P5.4) e de confirmação de regra postulada (P5.9). |
| **estado-do-projecto** | O que é verdade agora, em `ESTADO`, por facto datado e com origem. |
| **estado-da-frente** | Um de `aberta`, `em_trabalho`, `bloqueada`, `merge_pendente`, `carece_aprovacao`, `fechada`, `abandonada`, `obsoleta`. |
| **estado-da-arvore** | Um de `aberta`, `morta`. A morte é datada e atribuída (P1.1). |
| **estado-do-ramo** | Um de `por abrir`, `em desenvolvimento`, `fechado`, `podado`, `retido`, `suspenso: <ramo>`. |
| **estado-do-pressuposto** | Um de `por testar`, `confirmado`, `invalidado`, `inconclusivo`, com data. |
| **estado-do-alerta** | Um de `novo`, `visto`, `descartado`, `resolvido`. |
| **estado-do-achado** | Um de `aberto`, `aceite`, `corrigido`. |
| **ME / CE** | Mutuamente exclusivo / colectivamente exaustivo. |

---

## 1 · Mandato deste documento

### 1.1 Porque existe

Um projecto conduzido por várias sessões de agentes perde o objectivo sem que ninguém decida perdê-lo. Não há um momento de falha: há acumulação. Ao fim de algumas semanas o projecto é uma lista de tarefas que geram tarefas, e ninguém sabe dizer para que serve nenhuma delas.

Este documento descreve o sistema que impede isso.

### 1.2 Sintomas que resolve

| Sintoma | Mecanismo subjacente |
|---|---|
| Tarefas geram tarefas sem se saber para que servem | o objectivo não chega à sessão, ou chega e é reinterpretado |
| Não se sabe porque se escolheu este caminho e não outro | as frentes derivam do mandato sem camada de estratégia |
| O problema foi atacado por um ângulo só | não se geraram alternativas antes de decidir |
| Sessões contradizem-se sobre factos do projecto | o estado acumula em vez de ser substituído |
| Ficheiros de registo que ninguém lê | escrever é grátis e não há árbitro |
| Duas frentes a mexer na mesma coisa sem saberem | nada cruza o que cada uma declara tocar |
| Uma frente conclui algo que invalida outra, e ninguém liga | as dependências entre ramos não estão declaradas |
| Decisões tomadas e nunca aplicadas | o fecho não verifica aplicação |
| Becos sem saída reabertos meses depois | o fecho de uma frente não regista a razão |
| Regras de governo alteradas sem se saber que foram debatidas | nada liga documentos a decisões |
| Governo que cresce mais depressa que o projecto | procedimentos sem teste de utilidade |
| Governo que consome o projecto sem que nada o meça | conformidade medida, fluxo e custo não |

### 1.3 O que este sistema não faz

- Não impede uma frente de fazer a coisa errada dentro da sua própria zona.
- Não substitui julgamento humano sobre o rumo.
- Não se aplica a projectos de frente única: sem paralelismo, a maior parte dos mecanismos não tem o que detectar.
- Não vê o trabalho que não passa por ficheiro. Numa frente maioritariamente fora do disco, alerta vazio significa ausência de sinal, não saúde.
- Não garante qualidade do trabalho. Garante alinhamento e rastreabilidade.

### 1.4 Critérios de sucesso

| Critério | Medição | Garantia (§3.1) |
|---|---|---|
| Retoma a frio | uma sessão sem histórico retoma qualquer frente a partir do handoff | G17 |
| Alerta silencioso | alerta vazio é o caso normal, não a excepção | G11 |
| Zero decisões órfãs | nenhuma sessão fecha com decisão registada e não aplicada | G12 |
| Caminho vivo | todo o pressuposto resolvido produziu propagação e, se invalidado, reavaliação registada | G6 |
| Árvores mortais | nenhuma árvore aberta sem condição de morte declarada | G5 |
| Rumo rastreável | toda a alteração ao mandato tem data e alternativa rejeitada registada | G14 |
| Detecção rápida | conflito entre frentes recusado na abertura ou sinalizado no fecho seguinte | G11 |
| Governo estável | o corpo de regras não cresce sem um modo de falha observado | G16 |
| Leitura íntegra | nenhuma fonte não verificada entrou no contexto como instrução | G18 |
| Governo com fim | existe acto que o renova e critério que o encerra | G19 |
| Custo declarado | o consumo é medido contra um tecto escrito | G20 |
| Achados fecham | nenhum achado de auditoria envelhece sem dono | G21 |
| Continuidade | a indisponibilidade do responsável tem regime declarado | G22 |

*Nota.* Se o alerta dispara sempre, o detector está mal calibrado. Se nunca dispara e há colisões reais, as declarações estão mal preenchidas. Ambos são falhas do sistema, não do projecto. A calibração é item da auditoria (P7.2-humana, proporção de alertas descartados).

### 1.5 Mapa do documento

| Protocolo | Secção | Regras | Garantias que sustenta |
|---|---|---|---|
| P0 · Nascimento | §2.1.2 | P0.1–P0.13 | G1, G2, G20, G22 |
| P1 · Árvore | §2.2.2 | P1.1–P1.16 | G4, G5, G11, G13 |
| P2 · Caminho | §2.3.2 | P2.1–P2.11 | G3, G6, G11 |
| P3 · Desenvolvimento | §2.4.9 | P3.1–P3.31 | G3, G7, G8, G9, G10, G11, G12, G17, G18 |
| P4 · Alocação de papéis | §2.4.10 | P4.1–P4.9 | G15, G22 |
| P5 · Evolução | §2.5.7 | P5.1–P5.12 | G8, G13, G14, G16, G19 |
| P6 · Saída | §2.6.2 | P6.1–P6.2 | G17 |
| P7 · Auditoria | §3.2 | P7.1–P7.7 | G16, G19, G20, G21 e manutenção de G2, G4, G5, G9, G12, G13, G15 |

Esquemas dos ficheiros: Anexo A.

---

## 2 · Arquitectura

### 2.1 Nascimento do projecto

Nada arranca antes desta fase estar fechada.

#### 2.1.1 Conceitos

**O que é preciso estabelecer**

| Artefacto | Conteúdo | Quem escreve |
|---|---|---|
| `MANDATO` | objectivos, não-objectivos, critério de fim, responsável e sucessor, orçamento, limiares, data de desbloqueio | agente, por reformulação; autoria do humano |
| `PERFIS` | que perfis existem, o que lêem, onde escrevem, em que runner, com que hooks | o humano responsável |
| `TRAJECTOS` | nível, modo de escrita e classe de integridade por trajecto | o humano responsável |
| `canon/regras.json` | as regras em vigor, com força, detector, consequência, grau e teste | o humano responsável |
| `CASOS` | vazio no arranque | preenchido por divergência |
| `HALT` | ausente; o trajecto existe | — |

A fase de nascimento corre fora do regime de perfis, pela mão do humano responsável: nenhum dos perfis tem zona nos ficheiros que a fase cria, e `desbloqueado` é a fronteira de entrada no regime (P0.11).

Se o humano não conseguir enunciar o que quer, o mandato não se força: desenha-se uma árvore em modo Mandato (§2.2.1) e o mandato sai dela.

**Teste de reformulação.** O agente enuncia o mandato por palavras próprias e o humano confirma ou rejeita. Reformulação não é paráfrase: um agente que devolve as mesmas palavras por outra ordem não demonstrou nada. Compreendeu se consegue:

- derivar não-objectivos que o humano não enunciou, e acertar;
- classificar um caso-fronteira inventado na hora;
- dizer o que o mandato **exclui**, não apenas o que persegue;
- nomear a tensão entre dois objectivos e dizer qual cede.

**Teste de discriminação.** Três tarefas plausíveis: duas dentro do mandato, uma fora mas superficialmente parecida. Três sessões limpas com dissimilaridade declarada, cada uma com o mandato e nada mais. As três classificam igual e correctamente: passa. Qualquer divergência: falha. Os três veredictos ficam persistidos com `modelo` e `versao`, e é deles que o hook lê o resultado (P0.7, P0.12).

**Correcção em caso de falha.** Acrescentar não-objectivos e registar em `CASOS` a tarefa que gerou a divergência, com a classificação correcta. Nunca acrescentar princípios.

**Continuidade e custo.** O mandato declara quem responde, quem sucede, e o prazo de indisponibilidade a partir do qual o projecto entra em modo degradado. Declara também o orçamento: um sistema de governo consome chamadas de modelo e horas humanas, e sem tecto escrito o consumo só é conhecido quando já é o problema.

#### 2.1.2 Regras — Protocolo P0

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P0.1** | O mandato **deve** declarar entre um e cinco objectivos, cada um com slug. | mecânica | hook (esquema, Anexo A) | bloqueia |
| **P0.2** | O mandato **deve** declarar pelo menos dois não-objectivos por objectivo, cada um com slug. | mecânica | hook (esquema) | bloqueia |
| **P0.3** | O mandato **não pode** exceder uma página, contada sobre os valores de texto, excluindo chaves e slugs. | mecânica | hook (contagem) | bloqueia |
| **P0.4** | O mandato **deve** declarar o critério pelo qual o projecto se considera terminado. | mecânica | hook (esquema) | bloqueia |
| **P0.5** | O mandato **deve** ser redigido por agente, por reformulação da intenção do humano responsável. | convenção | humano | relatório |
| **P0.6** | O agente **não pode** acrescentar objectivo ou não-objectivo que o humano não tenha enunciado. | convenção | humano (teste de reformulação) | relatório |
| **P0.7** | O mandato **deve** passar o teste de reformulação e o teste de discriminação, apurados pelos veredictos persistidos de P0.12. | mecânica | hook (veredictos em `MANDATO.veredictos[]`) | bloqueia |
| **P0.8** | Uma frente **não pode** ser aberta antes de P0.7 devolver verdadeiro. | mecânica | hook (campo `desbloqueado` do `MANDATO`) | bloqueia |
| **P0.9** | O mandato **deve** declarar `responsavel` e `sucessor`, cada um com contacto e data de validade. | mecânica | hook (esquema) | bloqueia |
| **P0.10** | O mandato **deve** declarar orçamento de chamadas de modelo por merge e por fecho e de horas-humano por mês para auditoria; excedido o orçamento, não abre frente nova. | mecânica | hook (esquema; consumo registado em `METRICAS`) | bloqueia |
| **P0.11** | A fase de nascimento **deve** ser executada pelo humano responsável fora do regime de perfis, e nenhum perfil **pode** escrever nos artefactos que ela cria antes de `desbloqueado`. | mecânica | hook (zonas de `PERFIS` contra `desbloqueado`) | bloqueia |
| **P0.12** | Os testes de reformulação e de discriminação **devem** correr em três sessões com dissimilaridade declarada, e os três veredictos **devem** ser persistidos com `modelo` e `versao`. | mecânica | hook (esquema dos veredictos) | bloqueia |
| **P0.13** | Com o responsável indisponível além do prazo declarado, o projecto **deve** entrar em modo degradado: as frentes abertas continuam, nenhuma abre, e o facto é registado em `ESTADO`. | mecânica | hook (data de validade de `responsavel` contra `prazo_indisponibilidade`) | bloqueia |

#### 2.1.3 Nota

Um projecto sem mandato produz trabalho, mas não produz alinhamento, e o custo só aparece semanas depois.

O quarto item do teste de reformulação é o mais difícil de fingir: qual objectivo cede numa colisão não está no texto, está na intenção. Falha em qualquer item devolve o mandato à discussão, não à reescrita: o que falhou foi a transmissão da intenção, não a redacção.

Um princípio novo aumenta o espaço interpretativo em vez de o reduzir. Por isso a correcção de uma falha é sempre não-objectivo ou caso, nunca princípio.

Três sessões do mesmo modelo não são três juízes: são três amostras, e erram juntas. A concordância mede consistência; o que o teste procura é correcção, e é isso que a dissimilaridade compra.

---

### 2.2 A árvore

Este documento define **o que é** uma árvore, **quando** se abre e **qual** se abre. O detalhe fino e operacional (cartões por modo, desempates entre concorrentes, regras comuns R1–R9 com acção de reparação) vive no canon `protocolo-arvore-definicao-e-uso` v2. Este §2.2 é o roteamento; aquele é o manual.

#### 2.2.1 Conceitos

Uma árvore é uma **partição de um espaço por eixos**. Não é um plano: o plano é o caminho. Não é um índice: o índice deriva do que existe. Não é o entregável decomposto. A árvore gera os cortes; o caminho testa-os.

**Porta de entrada: precisa-se de árvore?** Se qualquer sinal for verdadeiro, não se abre árvore nenhuma (P1.8).

| Sinal | Para onde vai |
|---|---|
| A definição do problema muda a cada interlocutor | ainda é mandato ou rumo; não é árvore |
| Não se consegue escrever a condição de morte | P1.1 impede |
| O que interessa só existe no todo (coerência, confiança, cultura) | não tem ramo possível |
| A causalidade tem retorno: X afecta Y que afecta X | cortar o ciclo **é** decidir; outra representação |
| Decisão pequena e reversível | o custo de estruturar excede o valor; decide-se |

**Roteamento: qual ou quais?** Quatro perguntas; podem sair várias, e é isso que responde a "de quantas árvores preciso".

```
Q1  Há um estado indesejado cuja causa se procura?
    âncora: "as entregas atrasam três semanas e não se sabe porquê"
      sim ──────────────────────────────────► modo PROBLEMA

Q2  O humano não consegue enunciar o que quer?
    âncora: "quero uma solução boa", sem dizer o que a faz boa
      sim ──────────────────────────────────► modo MANDATO (abre antes de tudo; morre antes de tudo)

Q3  Falta conhecer o objecto ou o terreno antes de se poder escolher?
    âncora: "não sabemos o que distingue uma boa proposta neste mercado"
      sim ──────────────────────────────────► modo CARACTERIZAÇÃO

Q4  Há opções nomeadas, postas na mesa por quem decide, entre as quais escolher?
    âncora: "A, B ou C: qual delas"
      sim ──────────────────────────────────► modo DECISÃO
```

Desempate: Q1 exige estado indesejado declarado; Q3 não tem estado indesejado, procura o que o objecto é. Saírem ambas é normal. Em Q4, opções implícitas, sugeridas pelo agente ou por gerar **não contam**: se ninguém as nomeou, o caso é Q2 ou Q3.

**Quantas, por que ordem, como acoplam**

| Saiu | Concorrentes | Ordem | Acoplamento |
|---|---|---|---|
| só Problema | ≥2 em Problema | — | — |
| só Caracterização | 1; não concorre | — | — |
| só Decisão | ≥2 em Decisão | — | — |
| Problema + Caracterização | ≥2 em Problema | Caracterização primeiro se a causa depende de terreno desconhecido; senão, em paralelo | ramos de Problema que dependem do terreno ficam `suspenso: <ramo>`; ao receber resultado, reavaliam com três saídas (abaixo) |
| Problema + Decisão | ≥2 em cada | Problema primeiro; Decisão abre em paralelo com ramos suspensos | ramos de Decisão ficam `suspenso: <ramo de Problema>`; mesma reavaliação |
| Caracterização + Decisão | ≥2 em Decisão | Caracterização primeiro; Decisão abre em paralelo com ramos suspensos | ramos de Decisão ficam `suspenso: <ramo de Caracterização>`; mesma reavaliação |
| As três | ≥2 em Problema e em Decisão | Caracterização, depois Problema, depois Decisão; as três abrem já, com dependências declaradas (P1.4) | Decisão suspensa em Problema; Problema suspensa em Caracterização onde depende de terreno |
| Mandato, só ou acompanhado | 1; não concorre | morre primeiro, produz o `MANDATO`, e volta-se ao roteamento | nenhum; não acopla |

**Reavaliação de ramo suspenso: três saídas, mutuamente exclusivas.** `aprofundar`, quando o referente devolveu e o ramo ganha razão de existir; `podar`, com razão própria; `referente_morto`, quando o referente foi podado, ficou `retido` ou pertence a árvore morta, e que poda o ramo com razão herdada (P1.13). O grafo de dependências é acíclico (P1.12): um ciclo tornaria a reavaliação indefinida.

**Os quatro modos, em síntese**

| | **Problema** | **Caracterização** | **Decisão** | **Mandato** |
|---|---|---|---|---|
| Pergunta | porque é que isto acontece | o que é este objecto | qual destas | o que é que eu quero, afinal |
| Quando | Q1: estado indesejado com causa por achar | Q3: falta terreno antes de escolher | Q4: opções nomeadas por quem decide | Q2: o humano não enuncia o que quer |
| Raiz | pergunta fechada: *porque é que `<estado>`* | o objecto, não uma pergunta | a escolha, com espaço de opções declarado | o humano responsável |
| Eixos | um por nó | coexistem no 1.º nível; dois registos: eixos do real, eixos de preferência | um por nó | coexistem; obtidos por contraste entre exemplos, nas palavras do humano |
| ME / CE | ambos, estritos, dentro do eixo | dentro de cada eixo ambos; entre eixos nenhum | ME estrita; CE só sobre o espaço declarado | dentro do eixo ambos; conjunto de eixos aberto |
| Forma | fechada ao desenhar o nó | aberta; eixo novo é resultado | fechada sobre o espaço; opção nova reabre a raiz | aberta |
| Crivo | sim: *variando dez vezes, muda a causa provável?* | não; substitui-se por *este eixo discrimina bom de mau?* → senão `retido` | sim: *variando dez vezes, muda a opção?* | não; é generativa |
| Concorrência | ≥2 árvores com eixos distintos | não há | ≥2 árvores com eixos distintos | não há |
| Profundidade desigual | priorização | ritmos diferentes por eixo | alocação; o ramo raso fica registado | defeito |
| Poda | com razão no ramo | não enquanto aberta; `retido`; à morte da árvore, resolve-se (P1.14) | com razão; `suspenso` não se poda antes de o referente devolver ou morrer (P1.13) | nunca |
| Morte | causa confirmada, ou `cone_estrutural` prioritário esgotado → escala ao humano | saturação: dois ciclos sem eixo novo | opção escolhida, com alternativa rejeitada | produz o `MANDATO`; não reabre |
| Entrega ao caminho | a causa, como pressuposto testável | significado: o que as opções passam a querer dizer aqui; não decide | a opção, como caminho ou pressuposto | o `MANDATO`; volta ao roteamento |

Folha, em Problema e Decisão: hipótese falsificável por **uma** análise discreta; se não é, ramifica mais. Uma árvore madura é maioritariamente morta: o ramo morto diz o que não se voltará a fazer.

A árvore é um artefacto com estado próprio: nasce `aberta`, morre datada e atribuída, e a morte é um acto verificável, não uma leitura de quem passa (P1.1). A poda de um ramo é uma decisão, com registo em `debates/`: é isso que faz o slug entrar no índice e que impede a recriação silenciosa do beco (P1.16).

#### 2.2.2 Regras — Protocolo P1

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P1.1** | Cada árvore **deve** declarar, ao nascer, o seu modo, a condição em que morre e o estado-da-arvore; a morte **deve** ser datada e atribuída. | mecânica | hook (esquema de `arvores/*`) | bloqueia |
| **P1.2** | Num nó de árvore em modo Problema ou Decisão **não pode** ser aplicado mais de um eixo de corte, e o eixo **não pode** repartir um driver por ramos irmãos. | mecânica | hook (eixos distintos entre os filhos do nó); auditor (driver repartido) | bloqueia; relatório |
| **P1.3** | Ramos irmãos dentro de um eixo **não podem** sobrepor-se. | convenção | auditor | relatório |
| **P1.4** | Um ramo **deve** declarar as suas dependências no momento em que é desenhado, por referência qualificada `{arvore_slug, no_slug}`. | mecânica | hook (campo `depende[]`); auditor (ramos não-raiz com lista vazia) | bloqueia; relatório |
| **P1.5** | Um ramo de árvore em modo Problema ou Decisão **não pode** passar a frente sem ter passado o crivo de ordem de grandeza. | mecânica | hook (campo `crivo` do ramo) | bloqueia |
| **P1.6** | Um ramo podado **deve** registar a razão. | mecânica | hook (esquema) | bloqueia |
| **P1.7** | Árvores de modo diferente **não podem** ser fundidas. | convenção | auditor | relatório |
| **P1.8** | Uma árvore **não pode** ser aberta com qualquer sinal da porta de entrada verdadeiro. | convenção | humano (abertura) | relatório |
| **P1.9** | Em modo Problema e em modo Decisão **devem** abrir-se duas ou mais árvores concorrentes com eixos distintos. | mecânica | hook (contagem de árvores do mesmo modo, na geração da primeira frente a partir de uma árvore) | bloqueia |
| **P1.10** | Um factor que condiciona todos os ramos **deve** ser declarado `transversal` ao nível da árvore, com slug, e **não pode** ser ramo nem aresta. | mecânica | hook (esquema); auditor (ramo com arestas para todos os irmãos) | bloqueia; relatório |
| **P1.11** | Uma árvore em modo Mandato **deve** morrer ao produzir o `MANDATO` e **não pode** reabrir. | mecânica | hook (estado-da-arvore) | bloqueia |
| **P1.12** | O grafo formado por `depende[]` **não pode** conter ciclos. | mecânica | hook (fecho transitivo no desenho do ramo) | bloqueia |
| **P1.13** | A poda ou a morte de um ramo **deve** libertar para reavaliação obrigatória todos os ramos do seu `cone_de_dependencia`, com as três saídas de §2.2.1; `retido` conta como resultado negativo do referente. | mecânica | hook (transição de estado-do-ramo) | bloqueia |
| **P1.14** | À morte de uma árvore, todo o ramo `retido` **deve** transitar para `podado` com razão registada, ou para `fechado` se tiver entregue significado ao caminho. | mecânica | hook (morte da árvore) | bloqueia |
| **P1.15** | Podar um ramo com frente aberta **deve** emitir item de alerta `ramo_podado_sob_frente` e fechar a frente com razão herdada. | mecânica | watcher | alerta |
| **P1.16** | A poda de um ramo **deve** produzir entrada em `debates/` de tipo `poda`. | mecânica | hook (esquema) | bloqueia |

#### 2.2.3 Nota

Uma árvore só, em Problema ou Decisão, é inércia, não escolha; o crivo mata as estéreis. Fundir Caracterização com Decisão faz com que a decisão nunca feche, porque há sempre mais para caracterizar. Sem razão de poda, o ramo volta dentro de dois meses com outro nome. Uma árvore sem condição de morte é eterna, e uma árvore eterna é a lista de tarefas que geram tarefas, com melhor genealogia.

O ramo preso é o modo de falha silencioso desta secção: o `suspenso` cujo referente morreu, o `retido` de uma árvore que já fechou. Nenhum dos dois é visível, ambos são estados absorventes, e um cone inteiro fica preso por construção num sistema cuja tese é que as árvores têm de morrer. Daí a reavaliação obrigatória à poda e a resolução obrigatória à morte.

O canon operacional usa "triagem" para o que aqui se chama crivo de ordem de grandeza; neste documento "triagem" designa só o actor (§0).

---

### 2.3 O caminho

#### 2.3.1 Conceitos

Entre o mandato e as frentes há uma camada que decide **por onde**. O caminho é a hipótese, hoje, sobre como se chega ao mandato: uma aposta entre apostas possíveis, com os pressupostos que a sustentam declarados e testáveis.

A árvore gera os cortes; o caminho testa-os. O crivo mata ramos antes de haver dados, de graça; o caminho testa com dados reais o que sobreviveu, e é caro.

**Método de procura**

```
MP1  Enunciar o mandato como pergunta de decisão
MP2  Desenhar as árvores concorrentes e passar as estéreis pelo crivo
MP3  Por árvore sobrevivente, extrair o que tem de ser verdade: os pressupostos
MP4  Marcar os discriminantes: pressupostos cuja resposta elimina caminhos
MP5  Ordenar por (incerteza × custo de descobrir tarde) ÷ custo de testar
MP6  A primeira frente testa o discriminante do topo
MP7  Aplicar P2.4
```

O discriminante de MP4 é o corte de maior assimetria da árvore que sobreviveu. As frentes derivam do caminho, não do mandato. Os três factores de MP5 são campos do pressuposto: sem eles declarados, a ordem de ataque é uma opinião sem rasto.

**`CAMINHO`**

| Campo | Conteúdo |
|---|---|
| Pergunta de decisão | o mandato reformulado como pergunta |
| Caminhos em aberto | dois ou mais, com uma linha cada |
| Caminho actual | um, ou `não escolhido` |
| Pressupostos | estado-do-pressuposto, com data, frente atribuída e os três factores de MP5 |
| Ordem de ataque | os slugs dos pressupostos por ordem de MP5 |
| Regras de paragem | por pressuposto, escritas antes de a frente abrir |
| Reavaliações | data, disparo, pressuposto, caminho antes e depois, saída |

Uma página. Muda mais que o mandato, menos que o estado.

**Como se avalia.** Um milestone não é um entregável: é um teste de pressuposto. O resultado sobe por item de `INBOX` de tipo `pressuposto_resolvido`, qualquer que seja o valor, e é a triagem que o propaga ao `CAMINHO` e reordena a ordem de ataque (P2.8). Um resultado que não sobe é um teste que não aconteceu.

| Resultado | Significado | Consequência |
|---|---|---|
| `confirmado` | o pressuposto aguenta | avança para o seguinte na ordem |
| `invalidado` | o pressuposto cai | reavaliação obrigatória (P2.5) |
| `inconclusivo` | o teste não decidiu | redesenhar o teste, não repetir; repetido além do tecto declarado, escala (P2.11) |

**Como se reavalia.** A reavaliação tem actor: o perfil `caminho`, que escreve só em `CAMINHO` (P2.9). Três disparos: pressuposto invalidado, cadência declarada, ou vontade do humano.

```
reavaliação do caminho → quatro saídas, mutuamente exclusivas

  manter             nada mudou que altere a ordem
  reordenar          mudou a ordem de ataque, não o caminho
  trocar de caminho  o caminho actual cai; outro dos abertos assume
  escalar            o mandato é que está errado → modo rumo
```

Mudar de caminho não é mudar de rumo. Só a quarta saída toca no mandato.

**Colisão antes do trabalho.** A toca declara-se na abertura e é cruzada nesse momento contra as frentes abertas (P2.10). Recusar a abertura custa uma frente por abrir; descobrir a mesma colisão no merge custa duas frentes de trabalho.

#### 2.3.2 Regras — Protocolo P2

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P2.1** | O caminho **deve** declarar dois ou mais caminhos plausíveis. | mecânica | hook (lê `CAMINHO` ao abrir frente) | bloqueia |
| **P2.2** | Cada frente **deve** declarar a sua projecção: que pressuposto testa ou que caminho executa, com regra de paragem e fronteiras negativas. | mecânica | gate; hook (bloco `projeccao` selado na abertura) | bloqueia |
| **P2.3** | Cada pressuposto **deve** ter regra de paragem escrita antes de a frente abrir. | mecânica | hook (abertura) | bloqueia |
| **P2.4** | Um caminho **não pode** ser declarado escolhido com discriminante por testar. | mecânica | hook (esquema de `CAMINHO`) | bloqueia |
| **P2.5** | Um pressuposto invalidado **deve** disparar reavaliação datada posterior à queda, antes de abrir frente nova. | mecânica | hook (abertura: `pressupostos[].estado_data` contra `reavaliacoes[].data` para o mesmo `pressuposto_slug`) | bloqueia |
| **P2.6** | O caminho **não pode** exceder uma página. | mecânica | hook (contagem) | bloqueia |
| **P2.7** | Cada frente **deve** declarar o que toca antes de abrir. | mecânica | hook (abertura: `toca_declarado[]`) | bloqueia |
| **P2.8** | O resultado de um pressuposto **deve** subir por item de `INBOX` de tipo `pressuposto_resolvido`, e a triagem **deve** propagá-lo a `CAMINHO.pressupostos[]` e reordenar `ordem_ataque[]`. | mecânica | hook (fecho de frente com pressuposto resolvido sem item; item processado sem propagação) | bloqueia |
| **P2.9** | A reavaliação do caminho **deve** ser executada pelo perfil `caminho`, disparada por pressuposto invalidado, por cadência declarada ou pelo humano, escreve só em `CAMINHO`, e a sua saída **deve** ser uma das quatro e ficar registada. | mecânica | hook (zona e esquema de `reavaliacoes[]`) | bloqueia |
| **P2.10** | A abertura de frente **deve** cruzar `toca_declarado[]` contra as frentes abertas e recusar em colisão. | mecânica | hook (abertura) | bloqueia |
| **P2.11** | `inconclusivo` repetido sobre o mesmo pressuposto acima do tecto declarado **deve** escalar ao humano por entrada em `ESCALADAS`. | mecânica | hook (contagem por `pressuposto_slug`) | bloqueia |

#### 2.3.3 Nota

Sem esta camada, cada frente deriva directamente do mandato e é uma aposta isolada que ninguém consegue avaliar. Juntar o crivo e o teste do caminho faz desaparecer o crivo e transforma todos os cortes em frentes.

O caminho não se escolhe no início. Escolhe-se depois do primeiro teste que elimina alternativas. Uma frente que não testa um pressuposto nem executa um caminho já escolhido não tem razão para existir.

A pergunta de um milestone não é *o que fica pronto* mas *o que fica a saber-se*. `inconclusivo` diz algo sobre o sistema, não sobre o projecto: a regra de paragem foi escrita sem critério verificável. Repetido, diz que o pressuposto não é testável como está enunciado, e isso é matéria do humano.

Separar mudança de caminho de mudança de rumo é o que evita que cada surpresa técnica se transforme numa discussão existencial.

---

### 2.4 Desenvolvimento

#### 2.4.1 Hierarquia

| Nível | Artefacto | Muda por | Ritmo |
|---|---|---|---|
| **L0 · Projecto** | `MANDATO`, canon | emenda datada | meses |
| **L1 · Caminho** | `CAMINHO`, árvores | reavaliação | semanas |
| **L2 · Estado** | `ESTADO`, `FRENTES` | triagem; `FRENTES` por geração | dias |
| **L3 · Frente** | `estado.json`, projecção | fecho de sessão | sessões |
| **L4 · Sessão** | worktree, `INBOX` | trabalho | horas |

Cada trajecto declara o seu nível em `TRAJECTOS`; a hierarquia não se lê da prosa. O que sobe é um pedido, não uma alteração (P3.1).

#### 2.4.2 Escopo de contexto

Corolário da hierarquia: cada nível classifica o seu trabalho contra o nível imediatamente acima, nunca contra o topo (P3.2).

| Quem | Classifica contra | Não precisa de |
|---|---|---|
| Sessão | a projecção da frente | o caminho, o mandato |
| Frente | o pressuposto que testa e a regra de paragem | o mandato |
| Triagem | os ramos que o alerta toca, e os slugs dos objectivos | o texto do mandato |
| Caminho | o mandato | a intenção por trás |
| Rumo | a intenção do humano | — |

Uma frente sem o mandato geral continua a detectar que derrapou, porque derrapar é sair do **seu pressuposto**. O item `pressuposto_caido` que emite no `INBOX` significa "o meu pressuposto caiu", não "o projecto está errado"; a tradução para eventual emenda é feita por quem tem o mandato.

**Uma excepção, com identificador.** Os objectivos são escopáveis; os não-objectivos e os casos não. P3.2 exclui-os expressamente do seu tecto e P3.3 obriga a carregá-los inteiros. Uma fronteira que não está carregada não bloqueia nada, e o erro provável não é cair fora de um objectivo específico: é cair fora do mandato todo.

#### 2.4.3 Actores

Tabela única de actores. §2.4.10 acrescenta requisitos de execução; não acrescenta actores.

| Actor | É agente | Dispara por | Escreve em |
|---|---|---|---|
| **Humano responsável** | não | vontade | tudo |
| **Sucessor** | não | indisponibilidade do responsável (P0.13) | tudo, em modo degradado |
| **Orquestrador** | não | pedido de abertura de frente | nada; zona nula (P4.9) |
| **Arquitecto · triagem** | sim | alerta | `ESTADO`, `REJEICOES`, `CASOS`, `ESCALADAS`, `APROVACOES`, `alerta-estado.log`, estado dos itens de `INBOX` |
| **Arquitecto · rumo** | sim | só o humano | emenda ao `MANDATO`, `debates/` e `canon/`, ou nada. Nunca `ESTADO` (P5.2) |
| **Arquitecto · caminho** | sim | pressuposto invalidado, cadência ou humano | `CAMINHO` (P2.9) |
| **Frente** | sim | trabalho | a sua worktree, `INBOX` |
| **Verificação** | sim | fecho de sessão | o campo `cold_read` (P3.27) |
| **Auditor** | sim | cadência (P7.1) e sinal (P7.7) | relatório e `ACHADOS`, `METRICAS` |
| **Watcher** | não | cada merge | `corridas/<id>.json`, `alerta-estado.log`, `HALT` por indisponibilidade de hook |
| **Detector semântico** | não (chamada única) | o watcher | nada; devolve sugestão ao watcher |
| **Script de indexação** | não | cada merge, antes do watcher | `indice-decisoes.json` |
| **Script de inversão** | não | cada merge | `FRENTES` |
| **Hook de trajecto** | não | arranque, leitura, escrita e fecho de sessão | `sealed/` |

O watcher não tem modelo. É um script. O processo que vigia está sempre ligado; o que julga é sempre uma sessão fria e curta (P4.1). `ALERTA` não tem escritor: é derivado do log a cada corrida.

#### 2.4.4 Ferramentas

| Ferramenta | Função | Substitui |
|---|---|---|
| **Árvore** | partição do espaço, geração de cortes | ataque por um ângulo só |
| **Worktree** | isolamento, paralelismo, merge como verificação | disciplina de não mexer na pasta alheia |
| **Manifesto de trajectos** | nível, modo de escrita e classe de integridade por localização | regras escritas em prosa |
| **Hook de trajecto** | confinamento de leitura e escrita por perfil | regras escritas em prosa |
| **Índice de decisões** | liga slugs a decisões e graus; protege o que foi debatido | memória de quem estava presente |
| **Watcher** | cruzar declarações, seguir dependências, contar e vigiar os próprios hooks | reuniões de coordenação |
| **Registo de corridas** | prova de que a detecção correu, e com que passagens | confiança no processo |
| **Cold-read** | verificar auto-suficiência de um output, por actor distinto | confiança |
| **Proveniência selada** | registo imutável, por referência com hash, fora do índice de pesquisa | memória |
| **`ACHADOS`** | dá estado, dono e prazo ao que a auditoria encontra | relatórios que ninguém lê |
| **`METRICAS`** | mede fluxo e consumo, não só conformidade | impressão de que o governo é barato |
| **`HALT`** | paragem imediata de todas as escritas, salvo drenagem | — |

#### 2.4.5 Ficheiros

Esquema de cada ficheiro: Anexo A. Modo de escrita e nível por trajecto: `TRAJECTOS`.

| Ficheiro | O que é | Escrita | Quem |
|---|---|---|---|
| `MANDATO` | a lei do projecto | emenda datada | agente redige, humano valida |
| `canon/regras.json` | as regras em vigor, com força, detector, grau e teste | substituição | rumo |
| `PERFIS` | perfis, zonas, runners, hooks exigidos | substituição | humano |
| `TRAJECTOS` | nível, modo de escrita e classe de integridade por trajecto | substituição | humano |
| `CAMINHO` | a hipótese de como se lá chega | substituição | perfil `caminho` |
| `arvores/*` | partições do espaço, por modo | substituição | humano com agente |
| `CASOS` | casos-fronteira decididos | acrescento | humano, triagem |
| `ESTADO` | o estado-do-projecto: o que é verdade agora, por facto com origem | substituição | triagem |
| `FRENTES` | índice de frentes e ramos | gerado por inversão dos `estado.json` | script |
| `REJEICOES` | o que foi descartado e porquê | acrescento | triagem |
| `tocas/<frente>.json` | a toca declarada na abertura | write-once | hook |
| `corridas/<id>.json` | o que cada corrida do watcher fez | acrescento | watcher |
| `ALERTA` | projecção do estado de alerta na última corrida | derivado | — |
| `alerta-estado.log` | transições de estado-do-alerta, última-vence | log | watcher, triagem |
| `ESCALADAS` | o que subiu ao humano, com prazo | acrescento | triagem |
| `APROVACOES` | levantamento de `carece_aprovacao` | acrescento | humano, triagem |
| `INBOX/*.json` | descobertas, pressupostos, incidentes e fechos brandos por processar | acrescento | frentes, gate |
| `debates/*.json` | decisões, com alternativa rejeitada, aplicação esperada e o que afectam | acrescento | rumo, triagem, humano |
| `indice-decisoes.json` | slug → grau e decisões | gerado | script |
| `estado.json` | estado-da-frente face ao seu pressuposto | substituição | frente |
| `handoff.json` | como retomar | substituição | frente |
| `ACHADOS` | achados de auditoria, com dono e prazo | log | auditor, humano |
| `METRICAS` | indicadores de fluxo e consumo | acrescento | auditor |
| `research/` | exploração | livre | frente |
| `entregue/` | o que sobe | acrescento | frente |
| `Rascunhos` | travão intra-sessão | termina vazio | frente |
| `sealed/` | pedido, output, referências, em duas fases | write-once | hook |
| `HALT` | interruptor, com razão e escopo | write-once | humano, watcher |

Estado substitui-se, evidência acumula-se; nunca no mesmo ficheiro (P3.4). `research/` e `Rascunhos` existem para a exploração não contaminar o estado; não se disciplinam quanto à forma, e é por isso que a sua classe de integridade é `nao_verificado` (P3.23). A proveniência guarda referências com hash, não conteúdo (P3.5).

#### 2.4.6 O que é importante e o que não é

| Importante | Não é importante |
|---|---|
| O que cada frente declara **tocar** e de que **depende** | o que cada frente fez |
| O que ficou **fechado ou podado** e porquê | o que ficou aberto na conversa |
| O **próximo passo** e o seu critério de conclusão | a narrativa do percurso |
| A **alternativa rejeitada** numa decisão | a discussão que levou à decisão |
| Que o alerta esteja **vazio** e que a corrida tenha **acontecido** | quantos alertas já foram resolvidos |
| Que o output seja **auto-suficiente** | que a sessão tenha sido produtiva |
| Pressupostos **declarados** | pressupostos correctos |
| Quanto **custou** governar | quanto se escreveu |

A coluna da direita não é proibida. É o que não entra no estado curado: vive na proveniência selada, recuperável e não lida.

#### 2.4.7 Fluxos, do geral ao átomo

**L0–L2 · Projecto**

```
MANDATO → ÁRVORES → CAMINHO → frentes → merges → índice → watcher → alerta

alerta vazio            → nada acontece
alerta com item         → triagem
INBOX acima do limiar   → alerta (P3.19) → triagem
triagem toca no mandato → escalada (P3.15) → humano → rumo → emenda → MANDATO → P5.7
```

**L3 · Frente**

```
F1  Abre com projecção derivada do caminho, toca declarada e cruzada (P2.2, P2.10)
F2  Sessões de trabalho, N ≥ 1
F3  Fecho de cada sessão: gate (P3.16)
F4  Pressuposto resolvido → item pressuposto_resolvido → frente fecha → triagem propaga (P2.8)
```

**L4 · Sessão — o átomo**

```
S1  HALT presente?                    sim → drena e termina (P3.13)
S2  Perfil declarado e hooks presentes?
      não                             → recusa (P4.2, P4.5)
S3  Porta de abertura
      achado aberto há dois ciclos    → não abre (P7.5)
      orçamento excedido              → não abre (P0.10)
      modo degradado                  → não abre frente nova (P0.13)
      colisão de toca                 → não abre (P2.10)
S4  Monta contexto por perfil e por escopo, com classe por fonte (P3.2, P3.3, P3.23)
S5  Trabalha
      escrita fora da zona            → bloqueia, devolve zona, continua
      edição de slug com decisão      → aviso de protecção conforme o grau (§2.4.8)
      índice mudou desde o arranque   → recusa a escrita (P3.24)
      ampliação de toca               → evento próprio; concedido ou colisão (P3.21)
      dúvida                          → declara pressuposto, continua (P3.12)
      tema fora da projecção          → Rascunhos, volta ao tema
S6  Fecho (P3.16)
      toca efectiva fora da declarada → não fecha
      sem projecção                   → não fecha
      Rascunhos não vazio             → converte em descoberta (P3.26); só então verifica
      pressuposto novo                → fecha com carece_aprovacao
      cold_read = falha ou nao_corrido→ fecha com carece_aprovacao
      trabalho continua               → handoff.json, validado por cold-read
S7  Sela fase 1 → merge → regenera índice → watcher → sela fase 2 (P3.17)
      merge falhado                   → merge_pendente, incidente, alerta (P3.20)
```

Não existe estado de espera (P3.12). Sob `HALT` a sessão não espera: escreve o handoff, sela o que tem e termina.

#### 2.4.8 Mecanismos

**Gate de fecho.** Dois patamares. Divergência dura, quando a toca efectiva saiu da toca declarada, ou o que a sessão produziu não serve projecção nenhuma, bloqueia o fecho. Divergência branda, quando há pressuposto novo ou o cold-read não devolve `passa`, deixa fechar com a marca `carece_aprovacao` e produz item de `INBOX` de tipo `fecho_brando`. O primeiro protege o projecto; o segundo protege o ritmo. A marca não se levanta a si própria: quem a recebe não é quem a apaga (P3.28).

**Detecção, três passagens.**

| Passagem | Base | Confiança | Apanha |
|---|---|---|---|
| Colisão | `toca_declarado[]` (P2.7) contra `toca_efectivo[]` | facto | duas frentes na mesma coisa |
| Dependência | arestas da árvore (P1.4) | facto | conclusão que muda outro ramo |
| Semântico | chamada única de modelo, com timeout | sugestão | o que ninguém declarou |

Quando uma frente fecha um ramo, o watcher segue as arestas declaradas e vê quem ficava à espera daquilo. Apanha o conflito sem colisão de ficheiros. O detector semântico é a rede de segurança: quando apanha um conflito que a árvore não previa, falta uma aresta. Indisponível ou em timeout, não desaparece em silêncio: a corrida regista a passagem como falhada e emite item de passagem `semantico_indisponivel` (P3.18).

Um merge falhado é, ele próprio, a colisão que a primeira passagem existe para apanhar. Por isso não é excepção de execução: é evento de passagem `merge`, com item de incidente e dono (P3.20).

**Alerta com estado.** O watcher inscreve `novo` no log ao emitir o item. Só a triagem transita `novo → visto | descartado | resolvido`, e `visto` caduca no prazo declarado, voltando a `novo`. `ALERTA` é a projecção do log na última corrida: derivado, nunca escrito, logo nunca substituído por uma corrida concorrente. O hash de um item é `H(passagem, par ordenado, slug_tocado)`: um descarte na passagem de colisão não silencia a de dependência, e um par que mude de conteúdo volta a emitir (P3.10, P3.11).

**Protecção do que foi decidido.** Tudo tem slug (P3.6). A decisão declara o que afecta, o que sela, o que desbloqueia e o que retira; o índice é gerado por inversão (P3.7). Ao editar, o hook extrai o slug e consulta o índice (P3.8):

| Grau de protecção | Origem | Comportamento |
|---|---|---|
| `livre` | sem decisão | edita |
| `decidido` | decisão registada | aviso de protecção; a sessão continua e fecha com `carece_aprovacao` |
| `selado` | decisão com `sela[]` | bloqueia; só decisão com `desbloqueia[]` liberta |
| `morto` | slug retirado por decisão com `retira[]` | bloqueia a recriação |

O aviso de protecção devolve o identificador da decisão e o grau, e nada mais (P3.9). O agente recebe material para parar, não para formar opinião. Assim o contexto montado para a sessão não contém uma única referência ao conteúdo de decisões e continua protegido.

Uma regra retirada sai da vista do agente e vive no canon com grau `morta` (P5.5). Limite: só apanha reintrodução pelo mesmo slug; ver T3.

**Concorrência.** Merges e corridas do watcher são serializados, e o índice é regenerado antes de a corrida começar: sem isso, a protecção avalia contra índice velho. Todo o ficheiro de substituição carrega `base_hash`, e uma escrita cuja base já não é a corrente é recusada em vez de perder a actualização alheia (P3.25). Uma sessão aberta antes de um merge revalida `indice_versao` em cada edição (P3.24).

**Integridade de leitura.** O confinamento de escrita não diz nada sobre o que se lê. Cada fonte tem classe: `canon` é o que o governo declara, `produzido_sob_gate` é o que passou por fecho verificado, `nao_verificado` é tudo o resto — `research/`, o campo `texto` de um item de `INBOX`, qualquer origem externa. O último entra marcado e só como dado: nunca como instrução (P3.23).

**Cold-read.** Um agente sem histórico, do perfil `verificacao`, lê o output ou o handoff e responde a uma pergunta fechada (P6.2). Para um handoff: *consegues enunciar o próximo passo e o critério que o dá por feito?* Devolve `passa`, `falha` ou `nao_corrido`. O campo é da zona do verificador, não da frente (P3.27): um output que se certifica a si próprio não verifica nada.

**Paragem.** A presença de `HALT` faz o hook recusar arranque e qualquer escrita, com uma excepção de drenagem: `handoff.json` e a selagem da sessão em curso (P3.13). As sessões vivas ficam inertes na operação seguinte. Não se terminam processos: matar a meio deixa ficheiros parciais, que é exactamente o que a drenagem impede. `HALT` tem razão e escopo declarados, e a sua remoção segue procedimento de saída, com inventário de worktrees não fundidas e de selagens sem merge (P3.30).

#### 2.4.9 Regras — Protocolo P3

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P3.1** | Um nível **não pode** escrever no nível acima. | mecânica | hook (nível do trajecto em `TRAJECTOS`) | bloqueia |
| **P3.2** | O contexto de uma sessão **deve** ser montado por perfil e escopo (§2.4.2) e **não pode** incluir níveis acima do imediato, salvo os não-objectivos e os casos, nos termos de P3.3. | mecânica | hook | bloqueia |
| **P3.3** | Os não-objectivos e os casos **devem** ser carregados inteiros em toda a sessão que classifique. | mecânica | hook | bloqueia |
| **P3.4** | Cada trajecto **deve** ter um só modo de escrita declarado em `TRAJECTOS` — `substituicao`, `acrescento`, `log` ou `write_once` — e a escrita **não pode** usar outro. | mecânica | hook (modo do trajecto) | bloqueia |
| **P3.5** | A selagem **não pode** guardar conteúdo: só referências dos tipos da lista branca de `TRAJECTOS`, cada uma com hash do conteúdo do referente; um referente selado **não pode** ser apagado. | mecânica | hook (selagem; apagamento de referente) | bloqueia |
| **P3.6** | Todo o artefacto **deve** ter slug; um slug **não pode** ser reutilizado nem renumerado. | mecânica | hook (esquema) | bloqueia |
| **P3.7** | `indice-decisoes.json` e `FRENTES` **não podem** ser escritos por agente. | mecânica | hook (ficheiros gerados fora das zonas) | bloqueia |
| **P3.8** | Em cada edição o hook **deve** consultar o índice e aplicar o comportamento do grau de protecção (§2.4.8). | mecânica | hook | bloqueia; alerta |
| **P3.9** | O aviso de protecção **deve** devolver o identificador da decisão e o grau, e **não pode** devolver o conteúdo do debate, a alternativa rejeitada nem a razão. | mecânica | hook (formato do aviso); auditor (amostra) | bloqueia; relatório |
| **P3.10** | O watcher **deve** inscrever `novo` em `alerta-estado.log` ao emitir um item; só a triagem **pode** transitar `novo → visto \| descartado \| resolvido`, e `visto` **deve** caducar no prazo declarado, voltando a `novo`. | mecânica | hook (autor e transição); watcher (caducidade) | bloqueia; alerta |
| **P3.11** | O watcher **não pode** reemitir um item cujo estado-do-alerta é `descartado` ou `resolvido` enquanto o par não mudar de conteúdo; a reabertura **deve** ser decisão registada do humano. | mecânica | auditor | relatório |
| **P3.12** | Uma sessão **não pode** ficar à espera de outro actor; declara o pressuposto que assumiu e prossegue. | mecânica | gate (pressuposto novo) | fecha com marca |
| **P3.13** | Com `HALT` presente, o hook **deve** recusar arranque e qualquer escrita, salvo a escrita de `handoff.json` e a selagem da sessão em curso. | mecânica | hook | bloqueia |
| **P3.14** | Os hooks, o índice de decisões, `PERFIS`, `TRAJECTOS`, `canon/` e `HALT` **devem** residir fora de todas as zonas de escrita. | mecânica | auditor | relatório |
| **P3.15** | A triagem **não pode** resolver nem descartar um item cujo par toque slug de objectivo; **deve** deixar o item `novo` e abrir entrada em `ESCALADAS` com prazo. A triagem recebe os slugs dos objectivos, não o texto. | mecânica | gate (transição em `alerta-estado.log`) | bloqueia |
| **P3.16** | O gate **deve** bloquear o fecho em divergência dura e, em divergência branda, fechar com `carece_aprovacao` e produzir item de `INBOX` de tipo `fecho_brando`. | mecânica | gate | bloqueia; fecha com marca |
| **P3.17** | Todo o fecho **deve** seguir a ordem selar fase 1, merge, regenerar índice, correr o watcher, selar fase 2, e toda a corrida **deve** ficar registada em `corridas/<id>.json`. | mecânica | hook (ordem); auditor (sessões seladas sem corrida) | bloqueia; relatório |
| **P3.18** | O watcher **deve** correr as três passagens a cada corrida, registar a passagem de origem de cada item e registar como falhada a passagem que não executou. | mecânica | watcher; auditor | alerta; relatório |
| **P3.19** | O watcher **deve** contar os itens `por_processar` do `INBOX` e emitir alerta acima do limiar declarado; todo o item `pressuposto_caido` **deve** gerar alerta imediato. | mecânica | watcher | alerta |
| **P3.20** | Um merge falhado **deve** deixar a frente em `merge_pendente`, emitir item `falha_de_sistema` e alerta de passagem `merge`, e atribuir a resolução ao humano; a selagem fase 2 **não pode** ocorrer sem merge integrado. | mecânica | hook | bloqueia |
| **P3.21** | `toca_declarado[]` é write-once na abertura e reside fora da zona da frente; o gate **deve** compará-lo com `toca_efectivo[]` calculado do diff, e a ampliação da toca **deve** ser evento próprio, cruzado pelo watcher, que devolve `concedido` ou `colisão`. | mecânica | hook (write-once); gate (comparação) | bloqueia |
| **P3.22** | Todo o item de `INBOX` **deve** ter slug e estado (`por_processar`, `processado`, `rejeitado`); a triagem escreve o estado e devolve o resultado ao autor. | mecânica | hook (esquema; autor do estado) | bloqueia |
| **P3.23** | Toda a fonte **deve** ter classe de integridade, e conteúdo `nao_verificado` **não pode** ser montado como instrução: entra marcado e só como dado. | mecânica | hook (classe do trajecto na montagem de contexto) | bloqueia |
| **P3.24** | O hook **deve** revalidar `indice_versao` em cada edição e recusar a escrita quando o índice mudou desde o arranque da sessão. | mecânica | hook | bloqueia |
| **P3.25** | Merges e corridas do watcher **devem** ser serializados, e todo o ficheiro de substituição **deve** carregar `base_hash`, com recusa da escrita em desencontro. | mecânica | hook | bloqueia |
| **P3.26** | O conteúdo de `Rascunhos` que sobreviva à sessão **deve** ser convertido em item `descoberta` no `INBOX` antes de o gate verificar o vazio. | mecânica | gate | bloqueia |
| **P3.27** | O cold-read **deve** ser executado pelo perfil `verificacao`, único com zona no campo `cold_read`, cujo domínio é `passa \| falha \| nao_corrido`; `nao_corrido` é divergência branda. | mecânica | hook (zona do campo) | bloqueia |
| **P3.28** | A marca `carece_aprovacao` **deve** ser levantada por actor distinto da frente, por entrada em `APROVACOES`; a frente **não pode** transitá-la de `true` para `false`. | mecânica | hook (autor da transição) | bloqueia |
| **P3.29** | Todo o output de agente registado **deve** carregar `modelo` e `versao`. | mecânica | hook (esquema) | bloqueia |
| **P3.30** | `HALT` **deve** declarar `data`, `quem`, `razao` e `escopo`, e a sua remoção **deve** seguir o procedimento de saída: inventário de worktrees não fundidas, inventário de selagens sem merge, decisão por item e registo de `falha_de_sistema`. | mecânica | hook (esquema; remoção sem inventário) | bloqueia |
| **P3.31** | Toda a worktree de frente fechada, abandonada ou em `merge_pendente` **deve** constar do inventário de limpeza, com actor e cadência declarados. | mecânica | auditor | relatório |

#### 2.4.10 Escolha de agente por papel

Os papéis de §2.4.3 são funções, não produtos. Cada um tem requisitos que derivam da arquitectura, e é por eles que se escolhe onde corre. A escolha fica declarada em `PERFIS`, por perfil: zona de leitura, zona de escrita, runner e hooks exigidos.

**Seis critérios**

| Critério | Pergunta |
|---|---|
| Duração | o papel vive enquanto trabalha, ou tem de estar sempre ligado? |
| Disparo | quem o invoca: humano, evento, ou calendário? |
| Filesystem | precisa de worktree, git e ficheiros locais? |
| Enforcement | precisa de hooks que bloqueiem uma operação antes de executar? |
| Escopo | o contexto tem de ser montado por perfil e cortado? |
| Julgamento | o papel decide, ou só detecta? |

O critério de enforcement é eliminatório (P4.2).

**Requisitos por papel**

| Papel | Duração | Disparo | Precisa de | Natural em |
|---|---|---|---|---|
| **Orquestrador** | por pedido | humano ou calendário | invocação; zona nula | qualquer runner invocável |
| **Frente** | efémera | orquestrador | filesystem, git, hooks bloqueantes | runner de código local |
| **Arquitecto · triagem** | efémera, curta | evento (alerta) | leitura ampla, escrita escopada, invocação por máquina | runner invocável programaticamente |
| **Arquitecto · rumo** | efémera | só o humano | conversa; escrita só validada pelo humano (§2.4.3) | interface de chat |
| **Arquitecto · caminho** | efémera | pressuposto, cadência ou humano | leitura de árvores e `INBOX`; escrita só em `CAMINHO` | runner invocável programaticamente |
| **Verificação** | efémera, curta | fecho de sessão | leitura sem histórico; modelo distinto do que produziu | chamada limpa, com timeout |
| **Auditor** | efémera | calendário e sinal | leitura total, escrita só em relatório, `ACHADOS` e `METRICAS` | infraestrutura agendada |
| **Watcher** | persistente | cada merge | nenhum modelo; processo, disco e acesso aos hooks | infraestrutura sempre ligada |
| **Detector semântico** | por chamada | o watcher | uma chamada sem estado, com timeout | API directa, sem agente |
| **Script de indexação** | por corrida | cada merge, antes do watcher | disco | o runner do watcher |
| **Script de inversão** | por corrida | cada merge | disco | o runner do watcher |
| **Hook de trajecto** | por operação | cada operação | acesso bloqueante ao runner que escreve | o runner que escreve |

**Regras — Protocolo P4**

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P4.1** | Um processo permanente **não pode** julgar. | convenção | humano (decisão de alocação) | relatório |
| **P4.2** | Um papel que escreve em zona **não pode** correr em runner sem hooks bloqueantes. | mecânica | hook (S2, contra `PERFIS`) | bloqueia |
| **P4.3** | Os hooks **devem** residir no runner que executa a escrita. | convenção | humano (decisão de alocação) | relatório |
| **P4.4** | Uma mudança de runner **deve** ser precedida de decisão registada. | mecânica | auditor (`PERFIS` contra `debates/` de tipo `runner`) | relatório |
| **P4.5** | Um hook indisponível **deve** produzir recusa da operação que dele dependia. | mecânica | watcher (confirmação da presença e integridade dos hooks a cada corrida) | bloqueia |
| **P4.6** | A indisponibilidade de hook **deve** escrever `HALT` com `razao: hook_indisponivel`. | mecânica | watcher | bloqueia |
| **P4.7** | Uma regra de força mecânica **não pode** entrar em vigor sem teste negativo que demonstre que o detector recusa o caso proibido, registado na matriz `regra → detector → teste`. | mecânica | hook (campo `teste_ref` em `canon/regras.json`) | bloqueia |
| **P4.8** | Uma mudança de modelo **deve** ser precedida de decisão registada e obriga a repetir P0.7 e as sondas de fronteira. | mecânica | auditor (`modelo` e `versao` registados contra `debates/` de tipo `modelo`) | relatório |
| **P4.9** | O orquestrador **deve** constar de `PERFIS` com disparo declarado e zona de escrita nula. | mecânica | hook (esquema de `PERFIS`) | bloqueia |

#### 2.4.11 Nota

Infraestrutura persistente serve para vigiar, disparar e agendar. Um agente permanente a julgar acumula contexto e deriva, e seria o pior sítio do sistema para isso acontecer.

Um orquestrador que valida trajectos mas delega a escrita a um processo sem hooks não protege nada. O que define a frente é a projecção, a zona e o gate de fecho, não onde corre; mudar de ferramenta é substituição de implementação. Um hook que não responde equivale a `HALT` para as operações que dependiam dele; ver T4.

Há defesa para o hook ausente e é preciso defesa para o hook errado, que é muito mais provável. Uma regra escrita em prosa não se torna um detector correcto por ser escrita: o teste negativo é o que separa uma coluna preenchida de um mecanismo. E a variável que mais muda o comportamento de todo o sistema não é o runner: é o modelo.

---

### 2.5 Evolução

Um sistema que só impede movimento é uma jaula. Este distingue três formas de mudar.

A maior parte da mudança num projecto saudável é de ramo ou de caminho, não de rumo, e resolve-se em §2.2 e §2.3 sem tocar no mandato. Só chega aqui o que elas não conseguem absorver.

#### 2.5.1 Por necessidade

```
frente marca pressuposto_caido no INBOX
  → watcher emite alerta imediato (P3.19)
  → triagem
  → toca em slug de objectivo?
      não  → triagem resolve: estado, frente nova, ou rejeição
      sim  → escalada com prazo; item fica novo (P3.15)
  → humano abre modo rumo (P5.1)
  → emenda datada (P5.3), propagada (P5.7), ou nada
```

A frente nunca pára à espera desta cadeia (P3.12).

#### 2.5.2 Por vontade

O humano decide reavaliar sem que nada tenha falhado. Abre o modo rumo, o único modo que nenhum agente pode abrir (P5.1). Produz uma emenda ou nada; "nada" é resultado frequente e legítimo. O rumo não escreve no estado (P5.2): se escrevesse, cada alerta reabriria a discussão de rumo.

Uma emenda não é um acto local. Pode invalidar a pergunta de decisão, os caminhos abertos, os pressupostos e as projecções das frentes vivas. Por isso repõe `desbloqueado: null`, dispara reavaliação do caminho e alerta cada frente aberta cuja projecção dependa de objectivo emendado (P5.7).

#### 2.5.3 Por falha do próprio sistema

Um mecanismo não funciona. Entra no `INBOX` como `falha_de_sistema`, é triado, e se alterar como o projecto se governa, é emenda ao canon. Só um incidente assim justifica regra nova (P5.4), e é também um incidente assim que confirma uma regra postulada (P5.9). O incidente dispara ainda auditoria extraordinária, limitada à listagem afectada (P7.1).

#### 2.5.4 Deriva e inflexão

| | Deriva | Inflexão |
|---|---|---|
| Alteração do objectivo | real | real |
| Declarada | não | sim |
| Datada | não | sim |
| Alternativa registada | não | sim |
| Tratamento | é o que o sistema existe para impedir | é saudável |

Abrir frentes novas não é patologia. O que mata o projecto é a frente que altera o mandato sem o dizer. O sistema não impede movimento: torna impossível alterar o mandato sem emendar o mandato.

#### 2.5.5 Registo de debates

Cada decisão produz um ficheiro em `debates/` com campos fechados (Anexo A): o tipo, a decisão, a alternativa rejeitada, a razão, os slugs que afecta, o que sela, desbloqueia ou retira, e a aplicação esperada. Não a discussão.

Serve três funções: quando um mecanismo falhar daqui a meses, diz o que havia em alternativa e porque foi posto de lado; alimenta o índice que protege o que foi decidido; e a aplicação esperada é o que torna verificável, no fecho, que a decisão foi aplicada. É rastreabilidade, não história.

Quatro actos produzem decisão: a emenda de rumo, a mudança de runner ou de modelo, a opção escolhida numa árvore de Decisão, e a poda de um ramo. Todos escrevem em `debates/`, com o tipo declarado.

#### 2.5.6 O governo é governado

O canon é artefacto do projecto como qualquer outro: tem slug, tem zona, tem grau e muda por emenda (P5.8). Uma regra do corpo inicial nasce `postulada`, porque ainda não tem o incidente que P5.4 exige de todas as outras; confirma-se com o primeiro incidente que a motive, e sem incidente ao fim do prazo declarado é candidata a remoção (P5.9). O canon declara caducidade: manter o governo exige um acto, em vez de o abandonar exigir um (P5.10).

O sistema declara também como se entra e como se sai. A adopção por um projecto em curso segue período de transição, com os detectores mecânicos primeiro em modo de aviso (P5.11). Atingido o `criterio_fim`, o encerramento é protocolo, não abandono: o watcher desliga-se, as árvores vivas fecham, o arquivo tem retenção declarada e o espaço de nomes liberta-se (P5.12). Um projecto terminado com watcher ligado consome orçamento a vigiar trabalho que ninguém faz.

#### 2.5.7 Regras — Protocolo P5

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P5.1** | Só o humano **pode** abrir o modo rumo. | mecânica | hook (perfil `rumo` exige humano) | bloqueia |
| **P5.2** | O modo rumo **não pode** escrever fora de `MANDATO`, `debates/` e `canon/`. | mecânica | hook (zona de `PERFIS`) | bloqueia |
| **P5.3** | Toda a alteração ao `MANDATO` **deve** ser emenda datada com decisão em `debates/` que registe a alternativa rejeitada. | mecânica | hook (esquema) | bloqueia |
| **P5.4** | Uma regra nova **não pode** ser acrescentada ao canon sem incidente registado no `INBOX` que a motive. | mecânica | auditor (`incidente_slug` em `canon/regras.json`) | relatório |
| **P5.5** | Uma regra retirada **deve** manter o slug com grau `morta`. | mecânica | hook (esquema de `canon/regras.json`) | bloqueia |
| **P5.6** | Cada decisão **deve** produzir ficheiro em `debates/` com os campos do Anexo A, incluindo `tipo` e `aplicacao_esperada[]`. | mecânica | hook (esquema) | bloqueia |
| **P5.7** | Toda a emenda ao `MANDATO` **deve** repor `desbloqueado: null` até novo teste, disparar reavaliação do caminho e emitir alerta a cada frente aberta cuja projecção dependa de objectivo emendado. | mecânica | hook (escrita no `MANDATO`) | bloqueia |
| **P5.8** | O canon **deve** ter slug, residir em zona exclusiva do perfil `rumo` e ser alterado por emenda datada com decisão em `debates/`. | mecânica | hook (zona e esquema) | bloqueia |
| **P5.9** | Uma regra do corpo inicial **deve** nascer com grau `postulada`, confirma-se com o primeiro incidente que a motive e, sem incidente ao fim do prazo declarado, é candidata a remoção. | mecânica | auditor (grau e `incidente_slug` contra prazo) | relatório |
| **P5.10** | O canon **deve** declarar caducidade e, sem reafirmação activa no fim de cada período declarado, entra em estado `caduco`. | mecânica | auditor (`caduca_em`) | relatório |
| **P5.11** | A adopção por um projecto em curso **deve** seguir período de transição declarado, com os detectores mecânicos primeiro em modo de aviso e só depois bloqueantes, e inventário do existente. | convenção | humano | relatório |
| **P5.12** | Atingido o `criterio_fim`, o projecto **deve** seguir o protocolo de encerramento: desligar o watcher, fechar as árvores vivas, arquivar com política de retenção declarada e libertar o espaço de nomes. | mecânica | hook (`criterio_fim` atingido sem encerramento) | bloqueia |

#### 2.5.8 Nota

O documento obriga todas as árvores a declarar como morrem e o projecto a declarar como termina. Isentar-se das duas seria a única incoerência que nenhum detector apanharia, porque o detector faria parte da coisa isenta.

Uma regra que nunca foi precisa não é uma regra barata: é uma regra que só custa. O grau `postulada` existe para que a resposta venha da observação e não da discussão.

---

### 2.6 Regra de saída

Transversal a todos os níveis: handoff, entregue, alerta, relatório.

#### 2.6.1 Conceitos

**A resposta primeiro.** A recomendação ou conclusão encabeça o documento. Abaixo, pilares de suporte, ME entre si, em número reduzido — três ou quatro é o habitual. Na base, a evidência que sustenta cada pilar.

O cold-read é a verificação mecânica desta regra, e é feita por quem não escreveu o output: perfil `verificacao`, sem histórico, pergunta fechada, timeout declarado, e um valor de erro que não se confunde com sucesso.

#### 2.6.2 Regras — Protocolo P6

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P6.1** | Todo o output que sobe **deve** encabeçar com a conclusão, seguida de pilares ME entre si e da evidência que os sustenta. | convenção | gate (cold-read) | fecha com marca |
| **P6.2** | O cold-read **deve** ser feito pelo perfil `verificacao`, sem histórico, com pergunta fechada sobre a acção seguinte e timeout declarado, e devolver `passa`, `falha` ou `nao_corrido`. | mecânica | gate | fecha com marca |

#### 2.6.3 Nota

A árvore é lógica de partição do problema; esta é lógica de comunicação do resultado. Confundi-las produz documentos que expõem a análise em vez de a concluir. Um output que não é decifrável de cima, sem contexto, não cumpre a regra.

A contagem de pilares é indicativa e não se mecaniza: um output com cinco pilares bem separados cumpre melhor a regra do que um com três forçados. O que se mecaniza é quem verifica, com que domínio de valores, e em que prazo.

---

## 3 · Garantias permanentes

### 3.1 Tabela

| Id | Garantia | Regras | Como se obtém | Como se mantém | Falha observável | Detector · cadência |
|---|---|---|---|---|---|---|
| **G1** | Existe um mandato | P0.1–P0.4, P0.7–P0.12 | P0, com os dois testes e os veredictos persistidos | tecto de uma página bloqueia emendas que inchem | frente aberta sem `desbloqueado` | hook · cada abertura de frente e cada escrita no `MANDATO` |
| **G2** | É interpretado igual | P0.2, P0.6, P0.7, P0.12, P3.3, P7.2-humana | não-objectivos e casos decididos, juízes dissimilares | cada divergência vira caso em `CASOS` | sondas de fronteira divergem | hook · cada montagem de contexto; humano · mensal |
| **G3** | Chega a quem precisa | P2.2, P3.2, P3.3, P3.23 | injecção por escopo, não pesquisa; projecção selada na abertura | hook monta o contexto por perfil | sessão produz output sem projecção | hook · cada montagem; gate · cada fecho |
| **G4** | O problema foi partido | P1.2, P1.3, P1.5, P1.8–P1.10 | árvores concorrentes, um eixo por nó | crivo mata as estéreis | árvore única, nó com dois eixos, ramos sobrepostos | hook · cada geração de frente; auditor · mensal; humano · cada abertura de árvore |
| **G5** | As árvores morrem | P1.1, P1.11, P1.13, P1.14, P7.2-humana | condição de morte e estado declarados ao nascer | resolução obrigatória de `retido` e de dependentes | árvore aberta além da condição; ramo preso em referente morto | hook · cada escrita de árvore; humano · mensal |
| **G6** | O caminho é explícito | P2.1–P2.6, P2.8, P2.9, P2.11 | método de procura, mínimo dois | propagação obrigatória e reavaliação com actor | frente sem pressuposto declarado; resultado que não sobe | hook · cada abertura de frente; gate · cada fecho |
| **G7** | Ninguém sai da sua zona | P3.1, P3.14, P3.21, P4.2 | worktree, manifesto de trajectos e hook | hooks fora de todas as zonas; toca write-once | tentativa bloqueada no log; toca efectiva fora da declarada | hook · cada escrita; auditor · mensal |
| **G8** | O decidido não é mexido | P3.6–P3.9, P3.24, P5.5, P5.8 | slugs, índice gerado com grau, quatro graus | slugs nunca reutilizados; índice revalidado em cada edição | regra alterada sem decisão | hook · cada edição; auditor · mensal |
| **G9** | O estado não apodrece | P3.4, P3.25, P7.2-humana | substituição com `base_hash` | serialização de merges e corridas | contradições entre `ESTADO` e `FRENTES` | hook · cada escrita; humano · mensal |
| **G10** | O lixo não entra | P3.10, P3.19, P3.22, P5.6 | esquemas fechados (Anexo A); triagem como árbitro; estado por item | contagem do `INBOX` a cada corrida | `INBOX` cresce mais do que se esvazia | hook · cada escrita; watcher · cada corrida |
| **G11** | Conflitos aparecem | P1.4, P1.15, P2.7, P2.10, P3.17, P3.18, P3.21 | recusa na abertura; três passagens do watcher | arestas declaradas ao desenhar o ramo; corridas registadas | colisão descoberta por acaso; corrida sem passagem registada | hook · cada abertura; gate · cada fecho; watcher · cada corrida |
| **G12** | Decisões são aplicadas | P3.16, P3.28, P5.6, P7.2-humana | `aplicacao_esperada[]` verificada no fecho | aprovação por actor distinto | decisão sem item correspondente | gate · cada fecho; humano · mensal |
| **G13** | Becos não reabrem | P1.6, P1.16, P5.5, P7.2-humana | razão de poda registada e debate de tipo `poda` | slug morto bloqueia recriação | frente repete trabalho já podado | hook · cada edição; humano · mensal |
| **G14** | O rumo é rastreável | P5.1–P5.3, P5.6, P5.7 | emenda datada com alternativa | registo de debates e propagação | alteração ao `MANDATO` sem entrada em `debates/` | hook · cada escrita no `MANDATO` |
| **G15** | Cada papel corre onde deve | P4.1–P4.6, P4.9 | requisitos por papel declarados em `PERFIS` | mudança de runner passa por decisão; hooks vigiados de fora | papel que escreve a correr sem hooks bloqueantes | hook · cada arranque; watcher · cada corrida; auditor · mensal; humano · decisão de alocação |
| **G16** | O governo não incha | P5.4, P5.9, P7.1, P7.2, P7.2-humana, P7.3 | toda a regra nova exige incidente; grau `postulada` | auditoria automática a cada merge e humana mensal | regras sem incidente que as justifique | watcher · cada merge; auditor · mensal |
| **G17** | Os outputs são auto-suficientes | P3.27, P6.1, P6.2 | regra de saída | cold-read por actor distinto em cada fecho | handoff que não devolve o próximo passo | gate · cada fecho; hook · cada escrita do campo `cold_read` |
| **G18** | A leitura é íntegra | P3.5, P3.23, P3.29 | classe de integridade por fonte | conteúdo não verificado entra como dado | item de `INBOX` executado como pedido | hook · cada montagem de contexto |
| **G19** | O governo termina | P5.10, P5.12 | caducidade declarada e protocolo de encerramento | manter exige acto de reafirmação | canon operado além da caducidade; projecto terminado com watcher ligado | auditor · mensal; hook · atingido o `criterio_fim` |
| **G20** | O custo é declarado e respeitado | P0.10, P7.6, P7.7 | orçamento no `MANDATO`; métricas de fluxo | auditoria compara consumo com tecto | consumo acima do orçamento; limiar por revalidar | hook · cada abertura de frente; auditor · mensal |
| **G21** | Os achados fecham | P7.4, P7.5, P7.6 | estado, dono e prazo por achado | achado aberto há dois ciclos trava aberturas | achado sem dono; relatório que ninguém lê | hook · cada abertura de frente; auditor · mensal |
| **G22** | A continuidade está assegurada | P0.9, P0.13, P4.8 | responsável e sucessor com validade | modo degradado declarado; mudança de modelo revalida | responsável indisponível sem regime; modelo mudado sem revalidação | hook · cada arranque de sessão; auditor · mensal |

### 3.2 Manutenção no tempo

| Quando | O quê |
|---|---|
| **A cada fecho de sessão** | automático: gate, selagem em duas fases, merge, regeneração do índice e de `FRENTES`, corrida do watcher |
| **A cada merge** | listagem automática da auditoria (P7.2) |
| **A cada alerta** | sessão fria de triagem; não existe se o alerta estiver vazio |
| **Mensalmente** | auditoria humana (P7.1, P7.2-humana, P7.3) |
| **A cada `falha_de_sistema` ou sinal fora dos limites** | auditoria extraordinária, limitada à listagem afectada |

A auditoria é o único mecanismo que olha para o próprio sistema. Por isso tem duas metades: a que uma máquina pode correr a cada merge, e a que exige julgamento e cabe no orçamento de horas declarado.

**Regras — Protocolo P7**

| Id | Regra | Força | Detector | Consequência |
|---|---|---|---|---|
| **P7.1** | A auditoria humana **deve** correr uma vez por mês, nem mais nem menos, e a auditoria extraordinária **deve** ser disparada por item `falha_de_sistema` ou por sinal fora dos limites declarados, limitada à listagem afectada. | convenção | humano | relatório |
| **P7.2** | A listagem automática **deve** correr a cada merge: ramos `suspenso:` com referente podado, `retido` ou de árvore morta; ciclos em `depende[]`; toca alterada após a abertura; escaladas abertas além do prazo; achados abertos há dois ciclos; worktrees órfãs; corridas falhadas ou com passagem semântica em erro; presença e integridade dos hooks; regras `postuladas` sem incidente; consumo face ao orçamento. | mecânica | watcher | alerta |
| **P7.2-humana** | A listagem humana **deve** ser verificada uma vez por mês: sondas de fronteira; contradições entre `ESTADO` e `FRENTES`; alertas descartados que reapareceram; árvores que excederam a condição de morte; ramos não-raiz sem dependência declarada; nós com mais de um eixo, ramos irmãos sobrepostos e eixos que repartem um driver; árvores de modo diferente fundidas; árvore única em modo Problema ou Decisão; transversal alojado como ramo; regras alteradas sem decisão; regras sem incidente; decisões sem aplicação; conteúdo equivalente sob slugs distintos; mudanças de runner e de modelo sem decisão; sessões seladas sem corrida do watcher; inventário de limpeza; calibração do alerta, pela proporção de itens descartados. | convenção | humano | relatório |
| **P7.3** | O auditor **deve** verificar o próprio canon: obrigações em prosa sem identificador; regras sem detector ou sem consequência; regras de força `convenção` com consequência `bloqueia`; matriz `regra → detector → teste` incompleta; garantias sem regra; garantias cujo detector nomeie um actor que nenhuma das suas regras invoca; pares de regras com detector e consequência incompatíveis sobre a mesma operação; divergência entre `PERFIS`, `TRAJECTOS` e o texto do canon; referências cruzadas não resolvidas; termos usados sem entrada em §0; entradas de §0 sem uso. | mecânica | auditor | relatório |
| **P7.4** | O auditor **não pode** escrever fora do relatório, de `ACHADOS` e de `METRICAS`. | mecânica | hook (zona de `PERFIS`) | bloqueia |
| **P7.5** | Todo o achado **deve** ter estado-do-achado em `ACHADOS`, com dono e prazo; um achado `aberto` há dois ciclos **deve** bloquear a abertura de frente nova. | mecânica | hook (abertura de frente contra `ACHADOS`) | bloqueia |
| **P7.6** | Cada limiar numérico do canon **deve** ter justificação registada e data de revalidação no `MANDATO`; um limiar por revalidar é achado. | mecânica | auditor (`limiares[]` contra data) | relatório |
| **P7.7** | O auditor **deve** registar em `METRICAS` os indicadores declarados: tempo por fecho, proporção de fechos brandos, idade dos itens de `INBOX`, tempo até triagem, razão entre sessões de governo e sessões de trabalho, e consumo face ao orçamento. | mecânica | auditor | relatório |

*Nota.* Sem auditoria, o governo cresce e ninguém nota. A correr mais do que uma vez por mês, o governo consome o projecto — e é por isso que a metade contável corre sozinha e a metade que exige julgamento tem um orçamento de horas contra o qual se dimensiona.

Um relatório só é consequência se o que nele consta tiver dono, prazo e efeito. Sem `ACHADOS`, `relatório` lê-se `nenhuma`.

### 3.3 A garantia que nenhum mecanismo dá

Confinamento impede uma frente de estragar outra. Não impede que faça a coisa errada com perfeição dentro da sua própria zona.

Por isso a projecção não é burocracia: é o único sítio onde fica escrito para que existe aquela frente. E deriva-se do caminho, pelo que não custa nada escrever — mas tem esquema, é selada na abertura e é verificada no fecho, porque o que não tem detector não existe.

Um sistema sem ela continua a funcionar, continua a bloquear escritas indevidas, continua a detectar colisões, e produz, com total ordem e rastreabilidade, trabalho que não serve para nada.

---

## 4 · Tensões em aberto

**T1 · Custo de declarar arestas.** Se declarar dependências não for barato no momento em que o ramo nasce, as arestas ficam vazias e o detector cala-se, pior do que não existir, porque parece estar a vigiar.
*Resolução adoptada:* obrigação no acto de desenhar o ramo (P1.4).
*Por verificar na prática.* Sinal gratuito: ramos não-raiz sem nenhuma aresta. O auditor lista (P7.2-humana); a frequência responde sem ninguém ter de julgar.

**T2 · Completude das dependências.** A obrigação resolve o custo, não a completude. Declara-se o que se vê; o conflito caro é o que não se viu.
*Mitigação:* o detector semântico fica como rede de segurança e indica arestas em falta, com contrato: timeout declarado, valor de erro e alerta de indisponibilidade (P3.18).
*Custo assumido:* uma chamada de modelo por corrida, contabilizada no orçamento (P0.10).

**T3 · Reintrodução por slug novo.** A protecção do decidido só apanha recriação pelo mesmo slug. Conteúdo equivalente com slug diferente escapa ao hook.
*Mitigação:* detecção no auditor (P7.2-humana, conteúdo equivalente sob slugs distintos), não no momento da escrita.

**T4 · Dependência de runner.** Um papel alocado a um runner específico pára quando esse runner está indisponível.
*Resolução adoptada:* P4.5 e P4.6.
*Custo assumido:* indisponibilidade de infraestrutura pára trabalho em vez de o deixar correr sem protecção. É a troca correcta.

**T5 · Inchaço por multiplicação de árvores.** Quatro modos e árvores múltiplas por projecto é o ponto onde o sistema pode crescer sem limite.
*Travões:* P1.1, condição de morte declarada ao nascer; P1.13 e P1.14, que impedem cones presos; verificação na auditoria (P7.2, P7.2-humana).

**T6 · Volume do canon.** Um corpo de regras que cobre todos os caminhos é grande, e um corpo grande é lido por partes ou não é lido.
*Travões:* a coluna *Força*, que distingue o que bloqueia do que se recomenda; a partição de P7.2, que tira da mesa humana o que uma máquina conta; e P5.9, que torna uma regra sem incidente candidata a remoção em vez de património.
*Por verificar na prática:* a proporção de regras que continuam `postuladas` ao fim do prazo declarado.

**T7 · Configuração como novo ponto único de falha.** `PERFIS` e `TRAJECTOS` habilitam os hooks e passam a poder divergir do texto do canon. Uma zona mal declarada desliga silenciosamente um confinamento que o canon promete.
*Mitigação:* item próprio de P7.3, que compara configuração e canon; e P4.5, que verifica a presença e integridade dos hooks de fora.

**T8 · Falha fechada em cadeia.** A serialização (P3.25) e a revalidação de índice (P3.24) transformam atrasos em paragens: uma corrida lenta bloqueia escritas que estavam correctas.
*Custo assumido:* prefere-se parar a perder actualizações em silêncio. Alinhado com T4.

**T9 · Dissimilaridade tem custo.** P0.12 exige juízes distintos, o que encarece a verificação do mandato e obriga a manter mais do que um fornecedor disponível.
*Custo assumido:* três amostras do mesmo modelo dão confiança máxima com o ponto cego alinhado com o do sistema que validam. A concordância mede consistência; o que se quer é correcção.

**T10 · O diagnóstico é postulado.** Os sintomas de §1.2 motivam todo o edifício e não têm, eles próprios, incidente registado. Nada aqui prova que este é o modo de falha dominante.
*Resolução adoptada:* P5.9. Cada regra nasce `postulada` e confirma-se por observação, não por argumento; o que ao fim do prazo nunca foi preciso é candidato a sair.

---

## Anexo A · Esquemas dos ficheiros

Esquemas **fechados**: o hook rejeita a escrita que não tenha os campos obrigatórios e rejeita igualmente o campo não previsto. Todo o ficheiro declara `versao_esquema`, e o modo de escrita de cada trajecto é o que `TRAJECTOS` declara.

Tipos de item do `INBOX`: `descoberta`, `pressuposto_caido`, `pressuposto_resolvido`, `falha_de_sistema`, `fecho_brando`.
Tipos de debate: `rumo`, `runner`, `modelo`, `decisao_de_arvore`, `poda`.
Passagens de alerta: `colisao`, `dependencia`, `semantico`, `semantico_indisponivel`, `merge`.

| Ficheiro | Campos obrigatórios |
|---|---|
| `MANDATO` | `versao_esquema` · `slug` · `objectivos[]{slug, texto, nao_objectivos[]{slug, texto, caso_slug}}` (1–5; ≥2 não-objectivos cada) · `criterio_fim` · `responsavel{nome, contacto, validade}` · `sucessor{nome, contacto, validade}` · `prazo_indisponibilidade` · `orcamento{chamadas_merge, chamadas_fecho, horas_auditoria_mes}` · `limiares[]{nome, valor, justificacao, revalidar_em}` · `veredictos[]{teste, sessao, modelo, versao, dissimilaridade, resultado, data}` · `desbloqueado: data \| null` · `emendas[]{data, decisao_slug, alvo_slug, antes, depois}` |
| `canon/regras.json` | `versao_esquema` · `versao_canon` · `caduca_em` · `regras[]{id, grau: viva \| postulada \| morta, forca: mecanica \| convencao, detector, consequencia, incidente_slug \| null, teste_ref \| null}` |
| `PERFIS` | `versao_esquema` · `perfis[]{slug, zona_leitura[], zona_escrita[], runner, hooks_obrigatorios[], classe_leitura_maxima}` |
| `TRAJECTOS` | `versao_esquema` · `trajectos[]{padrao, nivel: L0 \| L1 \| L2 \| L3 \| L4, modo_escrita: substituicao \| acrescento \| log \| write_once, classe_integridade: canon \| produzido_sob_gate \| nao_verificado, tipos_referencia_admissiveis[]}` |
| `CAMINHO` | `versao_esquema` · `slug` · `pergunta` · `caminhos_abertos[]{slug, linha}` (≥2) · `caminho_actual: slug \| null` · `pressupostos[]{slug, estado, estado_data, discriminante: bool, regra_paragem, sustenta[], frente_slug \| null, incerteza, custo_descobrir_tarde, custo_testar, inconclusivos: int}` · `ordem_ataque[]: pressuposto_slug[]` · `reavaliacoes[]{data, disparo, pressuposto_slug \| null, caminho_antes, caminho_depois, saida: manter \| reordenar \| trocar \| escalar}` |
| `arvores/*` | `versao_esquema` · `slug` · `modo: problema \| caracterizacao \| decisao \| mandato` · `condicao_morte` · `estado: aberta \| morta` · `morta_em: data \| null` · `morte_verificada_por: slug \| null` · `transversais[]{slug, texto}` · `nos[]{slug, pai: slug \| null, eixos[], estado, depende[]{arvore_slug, no_slug}, suspenso_em: slug \| null, crivo: passou \| descartado \| null, razao: texto \| null}` (`razao` obrigatória com `estado: podado`) |
| `tocas/<frente>.json` | `versao_esquema` · `frente_slug` · `data` · `toca_declarado[]` · `ampliacoes[]{data, itens[], veredicto: concedido \| colisao}` |
| `INBOX/*.json` | `versao_esquema` · `slug` · `frente` · `tipo` · `estado: por_processar \| processado \| rejeitado` · `ramo` · `pressuposto` (obrigatório em `pressuposto_caido` e `pressuposto_resolvido`) · `resultado` (obrigatório em `pressuposto_resolvido`) · `toca[]` · `texto` · `classe_integridade` · `modelo` · `versao` · `data` |
| `estado.json` | `versao_esquema` · `slug` · `frente` · `data` · `base_hash` · `projeccao{pressuposto_slug, regra_paragem, fronteiras_negativas[]}` · `estado` (domínio de estado-da-frente) · `toca_efectivo[]` · `depende[]` · `proximo_passo` · `criterio_conclusao` · `cold_read: passa \| falha \| nao_corrido` · `carece_aprovacao: bool` · `modelo` · `versao` |
| `handoff.json` | `versao_esquema` · `slug` · `frente` · `data` · `proximo_passo` · `criterio_conclusao` · `pressupostos_assumidos[]` · `referencias[]{tipo, alvo, hash}` · `cold_read` · `bloqueio{tipo, detalhe} \| null` |
| `debates/*.json` | `versao_esquema` · `slug` · `data` · `tipo` · `decisao` · `alternativa_rejeitada` · `razao` · `afecta[]{tipo, slug}` · `sela[]` · `desbloqueia[]` · `retira[]` · `aplicacao_esperada[]{alvo, criterio}` |
| `indice-decisoes.json` | `versao_esquema` · `gerado_em` · `indice_versao` · `{slug: {grau: livre \| decidido \| selado \| morto, decisoes[], base_merge}}`, gerado por inversão de `debates/` |
| `corridas/<id>.json` | `versao_esquema` · `id` · `data` · `merge_ref` · `passagens[]{nome, estado: corrida \| falhada \| timeout}` · `itens_emitidos[]` · `hooks_verificados: bool` · `duracao` |
| `alerta-estado.log` | `versao_esquema` · `[{hash, estado: novo \| visto \| descartado \| resolvido, data, quem, razao}]`, leitura última-vence |
| `ALERTA` | derivado do log na última corrida · `versao_esquema` · `corrida` · `data` · `itens[]{hash, passagem, par[2], slug_tocado, ramo, origem, estado}`; `hash = H(passagem, par ordenado, slug_tocado)` |
| `ESCALADAS` | `versao_esquema` · `itens[]{slug, data, item_ref, razao, objectivo_slug, estado: aberta \| fechada, prazo}` |
| `APROVACOES` | `versao_esquema` · `itens[]{frente_slug, data, quem, veredicto, razao}` |
| `ESTADO` | `versao_esquema` · `data` · `modo_degradado: bool` · `frentes_abertas[]` · `factos[]{slug, texto, data, origem_frente, corrida}` |
| `FRENTES` | gerado por inversão dos `estado.json` · `versao_esquema` · `gerado_em` · `frentes[]{slug, ramo, arvore_slug, pressuposto, estado, toca[], depende[], worktree, zona}` |
| `REJEICOES` | `versao_esquema` · `itens[]{slug, data, origem, item_ref, razao}` |
| `CASOS` | `versao_esquema` · `casos[]{slug, tarefa, classificacao, nao_objectivo_slug, sonda_slug \| null, modelo, versao, data}` |
| `ACHADOS` | `versao_esquema` · `[{slug, auditoria_slug, regra, severidade, estado: aberto \| aceite \| corrigido, dono, prazo, data}]`, leitura última-vence |
| `METRICAS` | `versao_esquema` · `[{data, indicador, valor, limite}]` |
| `sealed/*` | `versao_esquema` · `slug` · `data` · `pedido_ref` · `output_ref` · `hash_conteudo` · `modelo` · `versao` · `fase: 1 \| 2` |
| `HALT` | `versao_esquema` · `data` · `quem` · `razao` · `escopo` |
