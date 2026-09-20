---
created: 2026-09-19 21:50
chat: Arquitectura de governo de projectos com agentes
summary: >
  Justificação ponto a ponto das dezoito alterações propostas, com a base de cada uma:
  falha observada, fonte externa, ou pressuposto declarado.
---

# Relatório de alterações

Uma entrada por alteração. Cada uma declara a sua **base**, que é de um de quatro tipos:

| Tipo | Significado |
|---|---|
| **Observada** | falha visível no material do sistema existente |
| **Fonte** | prática documentada por terceiro, com origem identificada |
| **Derivada** | consequência lógica de outra alteração já aceite |
| **Pressuposto** | juízo meu, sem fonte nem observação — o mais fraco, e assinalado como tal |

Das dezoito: quatro observadas, oito com fonte, três derivadas, três por pressuposto.

---

## A1 · A raiz carrega o mandato

**Existe:** o `CLAUDE.md` da raiz roteia e declara explicitamente que não sabe o que é o projecto.

**Proponho:** uma linha com o ponteiro para `MANDATO.md`.

**Porquê:** sem mandato acessível, nenhuma sessão consegue classificar o que produz. Uma sessão pode saber que está a trabalhar bem e não ter como saber se está a trabalhar no que interessa.

**Base — Fonte.** O GitHub Spec Kit separa deliberadamente duas coisas que costumam ser confundidas: o ficheiro de configuração do agente (`AGENTS.md`), que é descartável e específico do fornecedor, e a `constitution.md`, que governa o produto e encabeça a cadeia durável. A recomendação explícita é que o ficheiro de configuração transporte um **ponteiro de uma linha**, nunca uma cópia — copiar quebra a fonte única e garante divergência de versões.

**Custo de não alterar:** cada sessão reconstrói a sua noção de objectivo a partir do que lhe calhou ler.

---

## A2 · Watcher como quarto ponto de entrada

**Existe:** três modos, todos interactivos. Nada corre sem ti presente.

**Proponho:** um processo sem modelo, disparado por commit, que cruza declarações e escreve em `ALERTA.md`.

**Porquê:** com threads em paralelo, o conflito entre duas frentes só aparece quando alguém repara. Não há mecanismo que repare.

**Base — Fonte + Observada.** A separação entre processo persistente e sessão de julgamento é a conclusão directa de duas coisas: a literatura sobre deriva em sistemas multi-agente, que documenta divergência semântica em cerca de metade dos workflows ao fim de algumas centenas de interacções, e o teu próprio relato de correres várias threads em simultâneo enquanto trabalhas noutras.

**Nota sobre a alternativa que rejeitei:** propuseste uma sessão de Arquitecto permanente a avaliar o estado geral. Rejeitei em favor de um daemon sem modelo mais sessões frias. Razão: uma sessão LLM de longa duração acumula contexto e é o candidato número um a deriva — e seria o pior sítio possível, porque é o que julga tudo o resto.

---

## A3 · Enquadramento como montagem de contexto por perfil

**Existe:** o Enquadramento é leitura de protocolos pela própria sessão, antes de escolher modo.

**Proponho:** contexto montado à entrada, cortado pelo perfil. Cada nível recebe o nível imediatamente acima, não o topo.

**Porquê:** carregar tudo em todas as sessões aumenta a variância interpretativa em vez de a reduzir — o documento compete com a tarefa pela atenção.

**Base — Fonte + tua.** A tese é tua, e foi a primeira coisa que disseste nesta sessão: nem todas as sessões têm de saber o mandato geral. O que acrescentei foi a razão pela qual é seguro: cada nível classifica contra o nível de cima, e derrapar é sair do **seu** pressuposto, não do mandato. Do lado das fontes, a documentação da Anthropic sobre sistemas multi-agente descreve o contrato de delegação em quatro campos — objectivo, formato de output, fontes e fronteiras — e identifica descrições insuficientes como causa dominante de duplicação e lacunas entre subagentes.

**Excepção que introduzi:** os não-objectivos não são escopáveis. Uma fronteira que não está carregada não bloqueia nada, e o erro provável não é cair fora de um objectivo — é cair fora do mandato todo.

---

## A4 · Origem única do mandato de sessão

**Existe:** três origens — handoff, inbox, prompt — com o mesmo destino.

**Proponho:** as três passam a ser gatilhos; a fonte é sempre o `CAMINHO.md`.

**Porquê:** três origens de mandato são três formatos, três níveis de detalhe e três interpretações possíveis da mesma frente.

**Base — Derivada** de A15 e da camada de caminho. Se a projecção é derivável, ter três formas de a escrever é redundância que só produz divergência.

---

## A5 · Critério de sucesso verificável

**Existe:** a abertura apresenta mandato, critério de sucesso, plano e dúvidas, e espera confirmação.

**Proponho:** se o critério não puder ser avaliado por comparação objectiva no fecho, a sessão não arranca.

**Porquê:** um critério que exige julgamento no fecho transforma todo o fecho numa negociação.

**Base — Observada, no teu próprio sistema.** A correcção que fizeste à `Vista-Geral.md` — "sabes a origem, não o fim", que gerou a decisão "tarefa sem fim não é tarefa" e o acrescento dos campos *serve para* e *feito quando* — é exactamente esta regra. Proponho elevá-la de correcção pontual a condição de arranque.

---

## A6 · Dúvida declara pressuposto e continua

**Existe:** as dúvidas concentram-se na abertura; durante a sessão não há mecanismo, e o canal §4 implica esperar.

**Proponho:** pressuposto declarado com grau de confiança, e a sessão prossegue.

**Porquê:** com várias threads a correr e um só humano, qualquer espera acumula sessões paradas.

**Base — Fonte.** É a prática estabelecida em planeamento sob incerteza: o Discovery-Driven Planning de McGrath e MacMillan (HBR, 1995) trata pressupostos como hipóteses explícitas a testar, em vez de os deixar implícitos ou de esperar por certeza antes de avançar. A diferença face ao teu modelo actual não é avançar sem saber — é **registar** o que se assumiu.

---

## A7 · `estado.json` com campos fechados

**Existe:** o estado da thread vive em prosa, dentro do `thread.md`.

**Proponho:** ficheiro estruturado com `serve`, `toca`, `depende_de`, `pressupostos`.

**Porquê:** nenhuma detecção automática é possível sobre prosa. É a condição necessária de A2, A17 e da detecção por dependência.

**Base — tua.** Foi proposta tua, nestes termos, e adoptei-a inteira. O que acrescentei foi a condição: **campos fechados, enums, zero texto livre nos campos que o detector lê**. Se o modelo puder redigir, redige bem e o varrimento não apanha nada.

---

## A8 · Fecho em dois níveis

**Existe:** "acordo com o David" é condição única para escrever o registo final.

**Proponho:** divergência dura bloqueia; branda fecha com marca e sobe ao alerta.

**Porquê:** o bloqueio total é síncrono contigo. Com threads em paralelo, acumulam-se sessões abertas à espera — e o sistema volta a ser burocracia, só que num sítio diferente.

**Base — Pressuposto declarado.** Não tenho fonte para a divisão exacta entre dura e branda, nem observação que a valide. O raciocínio é: o primeiro nível protege o projecto, o segundo protege o ritmo, e só o primeiro justifica parar alguém. A fronteira entre os dois é calibração, e vai estar errada à primeira.

---

## A9 · Verificação de aplicação antes do commit

**Existe:** o fecho escreve decisões, anti-decisões e abertos, limpa e faz commit.

**Proponho:** nenhuma decisão sobrevive ao fecho sem item de aplicação ou linha de rejeição.

**Porquê:** decisões que não se aplicam acumulam-se e ninguém nota, porque estão registadas — parecem tratadas.

**Base — Observada, e é a mais directa de todas.** No material que me deste, a sessão `2026-09-18-B1-Governo-S2` fechou com seis decisões registadas, todas apontando para alterações no `CLAUDE.md`, no fluxo, no Enquadramento e nos templates, e o próprio registo diz: nada disso foi ainda escrito, sem commit. Não é hipótese — é a falha, documentada pelo teu sistema, sobre si próprio.

---

## A10 · Handoff em JSON, validado a frio

**Existe:** handoff por tema, com actualização de `TEMA.md` e `TEMAS.md`.

**Proponho:** JSON com campos obrigatórios, validado por leitura a frio antes de a sessão fechar.

**Porquê:** um handoff que parece completo a quem viveu a sessão pode ser inútil para quem não a viveu — e não há maneira de saber sem testar.

**Base — Observada, no teu sistema.** Já fizeste este teste uma vez: um subagente sem contexto leu apenas a `Arvore.md` e soube responder a três perguntas em treze. O mecanismo existe, funcionou, e revelou um problema real. Proponho promovê-lo de experiência a gate.

**Critério que introduzi:** o teste é sobre a acção seguinte, não sobre compreensão. Um handoff em que o agente percebe o tema mas não sabe o que fazer a seguir é inválido.

---

## A11 · Quota à entrada em vez de limpeza no fim

**Existe:** o fecho apaga decisões intermédias e registos que confundem.

**Proponho:** máximo dois itens promovidos por sessão; zero é resultado legítimo.

**Porquê:** limpar depois de escrever é mais caro do que não escrever, e depende de alguém se lembrar de limpar.

**Base — Fonte.** É o padrão convergente em vários sistemas de memória de agentes. O `agent-memory-kit` propõe zero a dois itens duráveis no fecho de sessão. O `context-kernel` separa um store curado, que o agente nunca escreve, de um journal descartável onde escreve à vontade, com promoção manual — justificando-o explicitamente como prevenção de degradação da memória. O `memd` põe a decisão final do que pode mudar em código Python, não no modelo.

---

## A12 · Modo Auditor definido

**Existe:** o modo está declarado como "por definir", com sucesso fixado em duas páginas lidas a frio.

**Proponho:** disparo por cadência, leitura total, escrita só no relatório, e sete verificações concretas.

**Porquê:** é o único mecanismo que olha para o próprio sistema. Sem ele, o governo cresce e ninguém repara.

**Base — Fonte, para o desenho das verificações.** A prática documentada em sistemas de avaliação de agentes separa um conjunto de casos de alta confiança — canários, que devem passar sempre e cuja falha dispara investigação imediata — de sondas de casos ambíguos. A Microsoft documenta a mesma estrutura em três categorias para detecção de regressão e drift.

**Nota:** mantive o teu critério de sucesso. Duas páginas lidas a frio é melhor critério do que qualquer um que eu inventasse.

---

## A13 · Regra de admissão no Meta-Governo

**Existe:** o Meta-Governo é um dos três temas, sem regra de entrada.

**Proponho:** nenhuma regra nova entra sem modo de falha observado que a justifique.

**Porquê:** um tema dedicado ao próprio governo, sem travão, cresce indefinidamente — e cada regra parece razoável no momento em que se escreve.

**Base — Pressuposto declarado, com apoio circunstancial.** Não tenho fonte. O apoio é a observação de que esta sessão produziu, em poucas horas, catorze regras e cinco protocolos para um sistema que nunca correu. Se o travão não existir, o padrão repete-se.

---

## A14 · Sete ficheiros novos

**Base:** cada um deriva de uma alteração já justificada. `MANDATO.md` de A1; `CAMINHO.md` de A4 e A15; `arvores/` do instrumento de partição; `CASOS.md` do teste de discriminação; `ALERTA.md` de A2; `debates/` e `indice-decisoes.json` da protecção do decidido.

**Sobre `arvores/` — Fonte.** O método de partição é o que descreveste: MECE com um eixo por nó, múltiplas árvores concorrentes no dia 1, corte avaliado por assimetria e acionabilidade, e triagem por ordem de grandeza antes de recolher dados. Adoptei-o como o deste. A distinção que acrescentei — exclusividade mútua sempre, exaustividade estrita só na árvore de problema e aspiracional na de caracterização — é **pressuposto meu**, e é a parte mais discutível: numa árvore que cresce por investigação, exigir exaustividade à partida exige conhecer o espaço antes de o investigar.

**Sobre `indice-decisoes.json` — tua.** O desenho é teu: slugs em tudo, índice gerado por script, hook que pára e alerta. O que acrescentei foram três coisas: a referência vive só do lado da decisão, pelo que o protocolo nunca menciona nada; o alerta devolve o identificador e o facto, nunca o conteúdo do debate; e quatro níveis em vez de dois, porque sem gradação tudo o que foi alguma vez debatido fica intocável.

---

## A15 · Projecção derivada em vez de redigida

**Existe:** `thread.md` com mandato, estado e handoff, escrito à mão.

**Proponho:** gerado do `CAMINHO.md` — objectivo é o pressuposto mais a regra de paragem; fronteiras negativas são os pressupostos das outras threads.

**Porquê:** uma projecção redigida à mão é trabalho por thread, e é onde a interpretação diverge silenciosamente.

**Base — Fonte + Derivada.** O contrato de quatro campos vem da documentação da Anthropic sobre orquestração de subagentes, que identifica a fronteira negativa — dizer explicitamente o que não fazer, por ser trabalho de outro — como parte necessária da delegação. A derivação automática é consequência de existir uma camada de caminho: se os pressupostos já estão escritos e atribuídos, redigi-los outra vez é duplicação.

---

## A16 · Arquitecto em dois modos

**Existe:** o Arquitecto é um papel único, disparado por ti.

**Proponho:** triagem disparada por alerta, que escreve no estado; rumo aberto só por ti, que produz emenda ao mandato ou nada e nunca escreve no estado.

**Porquê:** disseste que o Arquitecto não serve para nada e que o processo é burocrático. Concordo com o diagnóstico: um papel que aprova sem poder rejeitar é um carimbo, e sem mandato o único critério que lhe resta é "parece razoável", que qualquer sessão já aplica.

**Base — Observada + Pressuposto.** O diagnóstico é teu e a observação é directa. A separação em dois modos é **pressuposto meu**: se o mesmo modo decidisse rumo e triasse alertas, cada alerta reabriria a discussão de rumo. A invariante de que o modo rumo nunca escreve no estado é o que faz a separação ser real e não nominal.

---

## A17 · Schema obrigatório no `INBOX`

**Existe:** qualquer um escreve no `INBOX` a qualquer momento, em formato livre.

**Proponho:** `serves`, `effect`, `toca`, `depende_de` obrigatórios.

**Porquê:** a captura livre é a força do mecanismo e deve manter-se; o que muda é que o item tem de declarar o suficiente para ser triado sem ser lido por inteiro.

**Base — Derivada** de A7. Os mesmos campos, no mesmo formato, na fronteira entre thread e governo.

**Risco que assumo:** atrito na captura. Se declarar os campos for mais caro do que escrever a ideia, as pessoas deixam de capturar — e perder captura é pior do que ter itens mal classificados.

---

## A18 · Eliminação do canal síncrono

**Existe:** a thread pede em `mensagens.md`, sinaliza na raiz, regista que espera e termina. O Arquitecto responde noutra sessão. A sessão seguinte da thread destrava.

**Proponho:** eliminar. A thread declara o pressuposto que assumiu, prossegue, e regista a questão no `INBOX`. O Arquitecto processa em lote.

**Porquê:** são **três sessões para uma pergunta**. Esse desenho é correcto num sistema onde o respondente é um recurso escasso e partilhado entre muitos pedidos. Aqui o respondente és tu, e o custo é latência pura: pagas o preço de um sistema distribuído sem ter a concorrência que o justifica.

**Base — Observada** no teu próprio diagrama de sequência, que descreve o ciclo em quatro segmentos e dois participantes assíncronos.

**Custo de aceitar, e é real:** uma thread pode trabalhar uma sessão inteira sobre um pressuposto errado antes de alguém corrigir. Em troca, nenhuma das outras espera.

**Quando reverter:** se o pressuposto declarado se revelar errado com frequência e o custo do retrabalho exceder o da latência. É a condição de reabertura desta decisão, e deve ser registada com ela.

---

# Notas finais

## O que não alterei, e porquê importa

Duas peças passaram por exame e ficaram intactas.

O **`Rascunhos.md`** — um registo cuja função é não ser lido, que trava deriva intra-sessão a custo zero e que já trata o caso da decisão irreversível. Não tenho nada melhor a propor e não conheço equivalente em nenhum dos sistemas que examinei.

O par **`research/` + `entregue/`** com `NOTA.md` — dá lugar próprio ao caos. Os sistemas de memória de agentes que examinei chegam à mesma conclusão por outro caminho, separando um journal descartável de um store curado. Tu já o tinhas, com a vantagem de distinguir também o que sobe do que fica.

## As três alterações mais fracas

Por ordem de fragilidade, para saberes onde atacar primeiro:

**A8**, a fronteira entre divergência dura e branda — pressuposto sem fonte nem calibração, e vai estar errada à primeira.

**A13**, a regra de admissão no Meta-Governo — apoiada apenas na observação desta sessão, que não é amostra.

**A17**, o schema obrigatório no `INBOX` — o risco de matar a captura livre é real e não tenho forma de o avaliar sem uso.

## A alteração de maior impacto

**A18.** É a única eliminação pura, muda o comportamento de todas as threads, e o seu custo — trabalho sobre pressuposto errado — só se manifesta depois de aceite. Se houver uma para discutir antes de aplicar, é esta.
