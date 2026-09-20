---
created: 2026-09-19 22:14
chat: Governo de projectos multi-frente com agentes
summary: >
  Justificação ponto por ponto das trinta e cinco alterações propostas à arquitectura de
  governo, com o fundamento de cada uma: fonte externa, simetria interna ou pressuposto declarado.
---

# Racional das alterações M01 a M35

## Convenção

Cada entrada declara a alteração, o racional e o fundamento. O fundamento é de um de três tipos:

| Tipo | Significado |
|---|---|
| **Fonte** | apoio em trabalho publicado, nomeado na entrada |
| **Simetria** | a alteração replica uma solução já presente noutro ponto da própria arquitectura |
| **Pressuposto** | a alteração assenta em premissa declarada, não em fonte |

---

## Grupo A · Sintomas e critérios

### M01 · Sintoma do alerta não lido

**Alteração.** Acrescenta-se o sintoma «o alerta existe, está correcto, e ninguém o abriu».

**Racional.** A arquitectura elimina sessões de coordenação porque dependem de convocação. Um ficheiro de alerta depende de consulta, que é a mesma dependência sob outra forma. Um ficheiro vazio e um ficheiro não lido produzem a mesma observação: nada aconteceu.

**Fundamento.** Pressuposto, derivado por aplicação do critério da própria arquitectura. A regra que exclui a convocação humana não distingue entre convocar uma sessão e abrir um ficheiro; a distinção é de custo, não de natureza.

### M02 · Sintoma da investigação repetida

**Alteração.** Acrescenta-se o sintoma «investigação repetida sobre matéria já fechada».

**Racional.** A protecção do decidido actua no momento da escrita. Uma frente que investiga durante três dias matéria já fechada só encontra o bloqueio quando tenta escrever. O custo já foi incorrido.

**Fundamento.** Pressuposto: o custo de uma frente concentra-se na investigação, não na escrita.

### M03 · Retirada da exclusão de frente única

**Alteração.** O âmbito deixa de excluir projectos sem paralelismo.

**Racional.** Dos onze sintomas originais, apenas dois exigem paralelismo — duas frentes na mesma coisa, e uma frente que invalida outra em simultâneo. Os restantes nove ocorrem em sequência: becos reabertos, decisões órfãs, estado contraditório, governo inchado. Um projecto de frente única ao longo de seis meses tem nove dos onze problemas.

**Fundamento.** Simetria com a própria tabela de sintomas da arquitectura, por contagem.

### M04 · Critério de zero sessões de verificação

**Alteração.** Acrescenta-se, como critério de topo, a ausência de sessões cuja função única seja verificar alinhamento.

**Racional.** Os critérios originais medem propriedades do estado — alerta vazio, decisões aplicadas, árvores mortais. Nenhum mede a propriedade que justifica o sistema inteiro. Um sistema pode cumprir os nove critérios originais e continuar a exigir que alguém se sente a verificar.

**Fundamento.** Pressuposto declarado pelo autor do mandato: tempo perdido é contar com um arquitecto que nunca é chamado.

### M05 · Critério e garantia de tectos numéricos

**Alteração.** Acrescenta-se o cumprimento dos tectos como critério e como garantia.

**Racional.** Ver M10 e M13.

**Fundamento.** Simetria: a arquitectura já dispõe de critério e garantia para as árvores mortais; o tecto numérico é o mesmo problema num eixo diferente.

---

## Grupo B · Nascimento

### M06 · Tectos, canal e cadência inscritos no mandato

**Alteração.** O mandato passa a declarar tecto de árvores, tecto de frentes, canal de alerta e cadência de auditoria.

**Racional.** Três destes valores aparecem invocados ao longo da arquitectura — «tecto declarado», «canal», «cadência fixa» — sem que nenhum protocolo fixe onde são declarados. Um valor invocado e não inscrito é um valor que ninguém escreve.

**Fundamento.** Simetria: o mandato já é o local dos valores que governam todo o projecto e mudam por emenda.

### M07 · Separação dos dois testes em regras próprias

**Alteração.** A regra única que exigia ambos os testes desdobra-se em duas.

**Racional.** Os dois testes medem coisas diferentes — compreensão e precisão — e falham de maneiras diferentes, com correcções diferentes. Uma regra única impede registar qual dos dois falhou.

**Fundamento.** Regra de redacção canónica: uma obrigação por regra, para que a violação seja identificável.

---

## Grupo C · Árvore

### M08 · Exaustividade por propósito como regra

**Alteração.** A distinção entre exaustividade estrita e aspiracional passa de prosa a duas regras.

**Racional.** A distinção é a mais operacional de toda a secção da árvore e determina se um ramo pode nascer. Enquanto prosa, não é invocável no momento em que alguém desenha uma árvore de caracterização e é acusado de a deixar incompleta.

**Fundamento.** Simetria com o tratamento dado a «um eixo por nó», que já é regra.

### M09 · Accionabilidade como regra

**Alteração.** O segundo filtro do critério de corte passa a regra.

**Racional.** O primeiro filtro — assimetria — é um juízo de qualidade e não se deixa verificar. O segundo é binário: a variável é controlável ou não é. Um critério binário deve ser regra.

**Fundamento.** Simetria com P1.5, que já converte a triagem de ordem de grandeza em condição de passagem.

### M10 · Tecto de árvores e árvore morta

**Alteração.** Limite numérico de árvores simultaneamente abertas, e proibição de acrescentar ramos a árvore cuja condição de morte se verificou.

**Racional.** A arquitectura identifica a multiplicação de árvores como o ponto de crescimento sem limite e oferece como travão a condição de morte, declarada por quem abre a árvore e verificada por auditoria mensal. É um travão de período longo sobre um risco de período curto. O tecto actua no momento da abertura.

**Fundamento.** Simetria com o tecto de uma página já imposto ao mandato e ao caminho: a arquitectura já aceita limites numéricos arbitrários como travão, em extensão mas não em contagem.

### M11 · Ramo fechado regista resultado e razão

**Alteração.** Estende-se ao ramo fechado a obrigação de registo que existia para o podado.

**Racional.** A arquitectura justifica o registo da poda com a reabertura do ramo dentro de dois meses. Um ramo fechado com resultado é reaberto pela mesma razão — alguém não sabe o que lá se concluiu — e mais facilmente, porque parece ter havido trabalho útil.

**Fundamento.** Simetria com P1.6.

---

## Grupo D · Caminho

### M12 · Teste de discriminação de frente

**Alteração.** O caminho passa a ter critério de desbloqueio simétrico ao do mandato.

**Racional.** O mandato tem dois testes falsificáveis porque a arquitectura reconhece que a transmissão da intenção falha em silêncio. O caminho é a camada de que todas as frentes derivam e tem seis regras de forma e zero verificação de conteúdo. A assimetria não é justificada em lado nenhum. A própria arquitectura declara, na secção sobre a garantia que nenhum mecanismo dá, que a projecção é o único sítio onde fica escrito para que existe uma frente — e não verifica que esse sítio seja lido da mesma maneira por sessões independentes.

**Fundamento.** Simetria com P0.10, e aplicação da lacuna que a própria arquitectura declara.

### M13 · Tecto de frentes

**Alteração.** Limite numérico de frentes simultaneamente abertas.

**Racional.** A tabela de critérios de sucesso original mede «frentes abertas nunca excedem o tecto declarado», e nenhum protocolo declara onde o tecto vive nem qual é. Um critério de sucesso sem valor de referência não é mensurável.

**Fundamento.** Simetria interna: o critério existia sem a regra correspondente.

### M14 · Inconclusivo redesenha e não repete

**Alteração.** A consequência do resultado inconclusivo passa a regra, com a proibição explícita de repetir o teste.

**Racional.** A arquitectura estabelece que o inconclusivo diz algo sobre o sistema, não sobre o projecto: a regra de paragem foi escrita sem critério verificável. Repetir o teste é a resposta natural e é a errada. Uma proibição não escrita não é uma proibição.

**Fundamento.** Simetria com o tratamento já dado ao invalidado, que dispara reavaliação por regra.

---

## Grupo E · Arestas e propagação

### M17, M18 · Substrato de arestas

**Alteração.** As arestas passam a residir em substrato próprio, fora de todas as zonas de escrita, com travessia por consulta.

**Racional.** Três requisitos colidem na versão original. As arestas têm de ser declaradas pelo agente que desenha o ramo; percorridas pelo watcher; e invisíveis ao agente que trabalha, porque a arquitectura exclui o contexto global das sessões. Um ficheiro dentro da worktree satisfaz os dois primeiros e falha o terceiro.

**Fundamento.** Fonte — a arquitectura de quadro negro, formulada no sistema Hearsay-II, estabelece a separação entre fontes de conhecimento que publicam contribuições sem se conhecerem e um repositório partilhado consultado por um componente de controlo. A invisibilidade mútua das fontes é constitutiva do modelo, não acessória.

**Fundamento adicional.** Pressuposto: a travessia transitiva escrita à mão sobre ficheiros dispersos é código que se degrada; expressa como consulta recursiva numa base relacional é uma linha.

### M22 · Cone afectado por travessia transitiva

**Alteração.** A passagem de dependência deixa de seguir arestas directas e passa a calcular o fecho transitivo a jusante.

**Racional.** A versão original apanha quem estava directamente à espera do ramo fechado. A invalidação cara é de segunda ordem: o ramo B reavalia e muda de estado, e o ramo C, que dependia de B e não de A, não é notificado. A arquitectura declara que a passagem de dependência é a mais valiosa e a mais barata; restringi-la ao vizinho directo desperdiça a parte barata.

**Fundamento.** Fonte — a matriz de estrutura de desenho, na formulação de Steward e no desenvolvimento de Eppinger e Browning, existe precisamente para expor o acoplamento indirecto e os ciclos de iteração entre actividades que a leitura sequencial de dependências não revela.

### M34 · Tensão T6

**Alteração.** Declara-se que o substrato de arestas é ponto único de verdade fora do controlo de versões.

**Racional.** A alteração M18 resolve a invisibilidade e cria um ficheiro sem histórico, sem diff e sem merge. Não declarar a tensão seria reproduzir o defeito que a própria arquitectura evita ao listar T1 a T5.

**Fundamento.** Simetria com a secção de tensões em aberto.

---

## Grupo F · Entrega do alerta

### M15, M19, M20 · Alerta empurrado e triagem invocada

**Alteração.** O watcher emite para canal declarado e invoca a triagem. O ficheiro persiste como registo, não como via de entrega.

**Racional.** Ver M01. A arquitectura já estabelece que o watcher é um processo sem modelo, sempre ligado, e que a triagem é uma sessão fria e curta arrancada por ele. A emissão e a invocação são a consequência lógica de um desenho já adoptado; a versão original pára a um passo do fim.

**Fundamento.** Simetria com a regra de alocação já existente, segundo a qual o que está sempre ligado dispara e agenda, e o que julga corre em sessão fria arrancada por ele.

---

## Grupo G · Protecção do decidido

### M21, M23, M30 · Confronto de pesquisa

**Alteração.** Uma pesquisa lançada é comparada contra os ramos fechados e podados antes de ser executada, com sugestão e nunca bloqueio.

**Racional.** Ver M02. A protecção do decidido é um mecanismo de escrita aplicado a um problema de leitura. O momento útil de intervenção é o início da investigação.

**Fundamento.** Pressuposto declarado pelo autor do mandato: qualquer pesquisa lançada deve ser sinalizada se já existiu.

**Ressalva.** A implementação por distância vectorial depende de extensão em fase anterior à versão 1, com alterações incompatíveis previstas. A alteração é normativa; a via é datada.

### M24 · Projecção legível sem razões de fecho

**Alteração.** A vista do mapa destinada a leitura humana omite as razões de fecho e de poda.

**Racional.** A arquitectura estabelece que o mecanismo de bloqueio devolve o identificador da decisão e nunca o conteúdo do debate, com o argumento de que o agente recebe material para parar e não para formar opinião. O argumento aplica-se ao humano que olha para o mapa, e com mais força: é ele que decide reabrir.

**Fundamento.** Simetria com a regra de bloqueio sem razão, aplicada a um segundo destinatário. Pressuposto declarado pelo autor do mandato: um caminho anulado não diz, a quem vê o mapa, por que foi anulado.

---

## Grupo H · Regras órfãs

### M25, M26, M27, M28, M32 · Atribuição de identificador

**Alteração.** Cinco conjuntos normativos que existiam em prosa passam a regras com identificador — regra de saída, regras de alocação de runner, condição de adopção de regra nova, exigência de validador nos campos fechados, listagem fixa do auditor.

**Racional.** A arquitectura distingue regras de justificações em três blocos protocolares e não o faz fora deles. Uma norma sem identificador não é invocável num bloqueio, não é auditável e não tem consequência de incumprimento declarada. A norma que exige incidente registado para adoptar regra nova é o caso mais grave: é a única defesa contra o inchaço do governo e vive como linha de tabela.

**Fundamento.** Regra de redacção canónica aplicada ao próprio documento.

---

## Grupo I · Apresentação

### M16, M29 · Colunas de origem e de via

**Alteração.** As tabelas de ferramentas e de garantias ganham coluna que declara se a peça se monta a partir de ferramenta existente ou se escreve.

**Racional.** A versão original lê-se como oito ferramentas a construir. Seis são ferramentas maduras. A ausência da coluna não é omissão de detalhe: altera a leitura do esforço por uma ordem de grandeza, e leva quem implementar a escrever de raiz o que se instala.

**Fundamento.** Pressuposto: a decisão de montar ou construir é a decisão de maior impacto no custo, e não está representada em lado nenhum do documento.

### M31 · Garantia de que o alerta chega

**Alteração.** Acrescenta-se a garantia, com sinal de falha próprio.

**Fundamento.** Simetria com o formato da tabela de garantias, aplicado a M19.

### M33 · Mitigações declaradas em T1, T3 e T5

**Alteração.** Três das cinco tensões passam a declarar mitigação parcial.

**Racional.** T1, T3 e T5 são mitigáveis por peças que as alterações anteriores introduzem — geração automática do mapa de dependências inicial, equivalência por distância vectorial, e tecto numérico. Manter as tensões sem declarar a mitigação disponível dá a entender que nada mudou.

**Fundamento.** Consequência directa de M33, M23 e M10.

### M35 · Índice de alterações

**Alteração.** Tabela final com marca, secção e alteração.

**Fundamento.** Requisito de comparabilidade.

---

## Alterações não feitas, e porquê

| Elemento | Porque não foi alterado |
|---|---|
| Hierarquia de cinco níveis | não foi encontrada falha nem alternativa superior |
| Escopo por nível | é a peça que resolve o problema de origem; qualquer alteração degrada-a |
| Não-escrita ascendente | condição de todo o resto |
| Watcher sem modelo | a fonte de Cognition sobre decisões implícitas em acções sustenta manter o julgamento fora do processo permanente |
| Quatro saídas de reavaliação | exaustivas e mutuamente exclusivas |
| Estado por substituição, evidência por acrescento | correcto e já operante |
| Quatro níveis de protecção por slug | correcto e já operante |
| Gate de fecho em dois graus | a distinção entre divergência dura e branda protege o ritmo sem abrir o confinamento |
| Cold-read sobre a acção seguinte | a formulação fechada é o que o torna verificável |
| Deriva contra inflexão | a distinção é a definição operacional do problema |

---

## Uma alteração que foi considerada e rejeitada

**Perfil reduzido do sistema, sem repositório nem hooks.**

Foi proposta e retirada. O fundamento da retirada é do autor do mandato e aceita-se integralmente: o custo do governo está no desenho dos mecanismos que impedem a deriva, que é trabalho já feito e não repetível; um hook é execução. Uma versão sem imposição preserva o método e perde a única camada que não existe em mais lado nenhum.

A consequência é que a arquitectura não tem versão degradada. Ou corre onde há imposição, ou não corre.
