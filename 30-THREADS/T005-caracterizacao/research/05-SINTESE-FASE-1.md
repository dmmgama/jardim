---
created: 2026-09-17
thread: T005
tipo: sintese
summary: |
  Síntese cruzada das três pesquisas da fase 1 da T005 (especialidades, digital twin,
  monitorização). A peça principal: as três frentes responderam à mesma pergunta por
  ângulos diferentes, e é no cruzamento que aparece o que nenhuma delas viu sozinha.
  Achado central: as três pesquisas convergiram, independentemente e sem combinação,
  na mesma reclassificação do projecto — o jardim sobre laje é tecnicamente uma
  cobertura ajardinada, e isso activa um corpo normativo (FLL), um modo de falha
  (substrato fino seca em dias) e uma ferramenta (SWMM, módulo Green Roof) que nenhum
  documento do projecto tinha. Segundo achado: o conflito retenção-vs-drenagem é o
  compromisso técnico não resolvido mais valioso do projecto. Terceiro: a copa da
  palmeira aparece como bloqueio nas três pesquisas, por três razões independentes.
---

# Síntese da fase 1 — o que as três pesquisas dizem em conjunto

> **O que isto é.** As três frentes da fase 1 foram lançadas em paralelo, com enunciados
> separados e sem conhecimento umas das outras. Esta síntese é a peça que o Arquitecto
> pediu: **não um resumo dos três documentos, mas o que só aparece quando se cruzam.**
>
> Os documentos-fonte são `01-ESPECIALIDADES.md`, `02-DIGITAL-TWIN-SOFTWARE.md` e
> `03-MONITORIZACAO-ACTUACAO.md`. Uma quarta pesquisa — nuvem de pontos com equipamento
> profissional — foi encomendada depois, por instrução do David, e entra em
> `04-NUVEM-DE-PONTOS.md`. **Esta síntese não a cobre**, e será revista quando chegar.

---

## 1. A convergência que não foi encomendada

**As três pesquisas chegaram, independentemente, à mesma reclassificação do projecto.**

Nenhuma foi instruída a fazê-lo. O enunciado de cada uma mencionava que o jardim sobe
+0,50 m sobre a betonilha, como facto de contexto. As três trataram esse facto como o
dado mais importante que receberam:

| Pesquisa | O que disse, sem combinação com as outras |
|---|---|
| **01 — Especialidades** | Abriu uma secção que não estava na lista de disciplinas que lhe dei — **«§6-bis. Impermeabilização e estanquidade de coberturas ajardinadas — a disciplina que faltava nomear»** — e colocou-a em **#1 das cinco que mais valem** para este caso. |
| **02 — Digital twin** | «O jardim sobe +0,50 m sobre laje — isto é, estruturalmente, **uma cobertura verde em escala doméstica.**» E daí tirou a ferramenta: SWMM tem módulo **Green Roof** dedicado, gratuito, validado em investigação de telhados verdes de pequena escala. |
| **03 — Monitorização** | Abriu com um aviso ao Arquitecto: «Isto é uma cobertura verde, não um jardim de solo natural — **e a literatura é explícita: substratos finos falham cedo e falham mal em clima mediterrânico**, porque não há reserva de água lateral nem drenagem profunda para absorver um erro.» |

**Três disciplinas diferentes, três enunciados separados, a mesma conclusão.** Quando isto
acontece, não é opinião — é a natureza do objecto a impor-se.

### Porque é que isto valida a existência da T005

Está escrito em `00-PONTO-DE-PARTIDA.md`, antes de qualquer pesquisa ter chegado, que o
ponto cego do método actual é: *«um parâmetro que ninguém se lembrou de procurar não
aparece em lista nenhuma de lacunas»*. E que o teste da T005 seria **fazer aparecer pelo
menos um parâmetro que as duas listas de lacunas do dossier não contêm.**

**O teste passou, e passou em cheio.** A cobertura ajardinada não aparece no dossier — nem
em §10 («secções por instruir»), nem em §12 («por inspeccionar»), nem em nenhuma das três
prioridades. **Não por descuido**: quando o dossier foi escrito, o jardim ainda era de chão.
A decisão de subir a cota é de 2026-09-17, e nenhum método de levantamento por observação a
podia ter antecipado — porque não há nada no espaço para observar. A coisa ainda não existe.

---

## 2. O conflito que ninguém resolveu, e que manda no projecto

A pesquisa 01 produziu uma matriz de conflitos entre disciplinas. **Um deles destaca-se, e
a própria pesquisa o marca como «o conflito mais valioso identificado»:**

> **Retenção de água para a vegetação vs. drenagem rápida para proteger a impermeabilização.**
>
> O substrato ideal para a planta **retém** água — reduz rega, melhora a sobrevivência na
> seca mediterrânica. O substrato ideal para a laje **escoa depressa** — reduz peso
> saturado, reduz tempo de contacto da água com a membrana, reduz risco de saturação.
>
> A FLL resolve isto com camadas distintas sobrepostas (drenante + filtrante + substrato),
> **mas a espessura de cada camada é uma decisão de compromisso, não uma optimização única
> — e ainda não foi tomada neste projecto.**

### Porque é que este conflito é o mais importante do documento

**Porque as outras duas pesquisas confirmam os dois lados, sem saberem que estavam a
alimentar um conflito.**

- **O lado da planta.** A pesquisa 03 estabelece que num substrato de 0,50 m sobre laje
  impermeável, **a humidade é o único parâmetro cuja falha mata plantas em dias, não
  semanas**. Não há reserva lateral. Não há drenagem profunda. Um erro de rega em Agosto não
  se corrige na semana seguinte.
- **O lado da laje.** A mesma pesquisa 03, na secção de modos de falha, descreve o cenário
  oposto: sensor avariado preso a «seco», sistema rega em excesso continuamente, e **sobre
  laje impermeável a água acumula sem drenar para lado nenhum** — asfixia radicular e
  sobrecarga de peso não planeada.

**O mesmo sistema mata a planta pelos dois lados.** É por isso que é o compromisso mais
valioso: não há optimização, só arbitragem — e a arbitragem ainda não foi feita.

### O que isto implica para a T004 (e é urgente)

A T004 está a fixar a geometria com construção civil disponível *agora*. **A espessura das
camadas — drenante, filtrante, substrato — é geometria.** Não é acabamento que se decide
depois de a plataforma estar construída: é o que define a cota final, o peso e o
comportamento hidráulico de tudo.

> ⚠ **Sinal ao Arquitecto, com pedido de encaminhamento à T004:** os +0,50 m estão fixados
> como *cota*, mas **não estão decompostos em camadas**. `ESTADO.md` §02 diz «o jardim sobe
> +0,50 m por cima dela» e §04 fixa os quatro planos de cota — em lado nenhum se diz quanto
> disso é dreno, quanto é filtro e quanto é terra. **Se a T004 desenhar os 50 cm como um
> bloco homogéneo de terra, desenha uma coisa que não vai ser construída assim.**

---

## 3. A palmeira aparece nas três pesquisas, por três razões diferentes

Isto não estava no enunciado de nenhuma delas como tema central. Apareceu sozinho:

| Pesquisa | Porque é que a palmeira apareceu |
|---|---|
| **01 — Especialidades** | Arboricultura entra em **#2 das cinco que mais valem**. Dois conflitos da matriz são sobre ela: *profundidade de substrato vs. carga admissível* e *colo soterrado vs. cota desejada*. A pesquisa é explícita: **«não há como resolver este conflito sem primeiro medir a árvore.»** E: subir a cota +0,50 m à volta do tronco de uma árvore existente é **«uma das causas mais comuns e mais lentas de declínio arbóreo»**. |
| **02 — Digital twin** | Identificou a vegetação como **«o eixo mais subestimado»** de toda a pesquisa. Modelar a copa como cilindro em vez de geometria real **muda genuinamente o resultado da análise de sombra** — um cilindro sobre-estima no centro e sub-estima nas margens; uma copa irregular produz um padrão fragmentado que o cilindro nunca reproduz. |
| **03 — Monitorização** | Encontrou o que chama **o achado mais valioso da pesquisa**: detecção acústica precoce de *Rhynchophorus ferrugineus*, com **taxas superiores a 90%** em ensaios publicados, capaz de detectar larvas com duas semanas de idade. E o argumento económico: sendo a palmeira «dado fixo de projecto», **o limiar de "vale a pena" é muito mais permissivo aqui** do que em qualquer outro sensor. |

**A leitura cruzada:** a copa da palmeira não é «mais uma medição em atraso». É o
**bloqueio único de maior alcance do projecto** — trava a T004 (geometria), trava a T003
(modelo solar, pedido 5), impede avaliar o risco de soterrar o colo, e impede dimensionar
a carga. Continua a custar **uma hora** (🔴 P2.2).

> **Nota de fronteira, importante.** A pesquisa 03 acrescenta uma obrigação que não é de
> projecto, é externa: a fitopatologia é **a única disciplina com obrigação legal
> confirmada** — vigilância do escaravelho vermelho como praga de controlo obrigatório.
> Isto não é preferência de projecto, e não estava registado em lado nenhum.

---

## 4. Três convergências menores, que valem por serem independentes

### 4.1 «Não compres tecnologia, compra a ferramenta certa»

As pesquisas 02 e 03 chegaram, em domínios completamente diferentes, ao mesmo veredicto de
sobredimensionamento:

- **02:** «Quem vende *digital twin* chave-na-mão para jardins domésticos está a vender
  visualização, não simulação.» ENVI-met a 3.000 €/ano é desproporcionado quando
  SOLWEIG/UMEP, gratuito e mantido por consórcio universitário, faz literalmente a pergunta
  do projecto: *que acontece ao conforto térmico se eu plantar esta árvore aqui*.
- **03:** «LoRaWAN, NB-IoT e a maior parte da conversa "protocolo de longo alcance" é ruído
  de marketing aplicado à escala errada — resolve hectares, não quintais.» E: fertirrega
  automatizada (Dosatron a 3.799 €) é **cortada por inteiro** do documento.

**É a mesma conclusão que a T003 já tinha tirado sobre captura 3D** («compra-se um
telémetro, não se compra software», `ESTADO.md` §11). **Três pesquisas independentes, três
domínios, o mesmo padrão:** a esta escala, a tentação é comprar a ferramenta da escala
acima.

### 4.2 O que sobrevive ao abandono

Instruí as pesquisas 02 e 03 a valorizar isto. Ambas devolveram o mesmo princípio
operacional, com formulações próprias:

- **03:** «Um sistema que morre quando o fabricante fecha o serviço é um passivo.» Daí a
  preferência por Home Assistant + ESPHome, **locais, sem cloud obrigatória** — e a regra de
  usar o hardware de válvula dos fabricantes comerciais **mas não a nuvem deles**.
- **02:** a pilha equilibrada é recomendada em parte por ser **investimento único, sem
  subscrições recorrentes** — o contrário de Vectorworks ou Autodesk Forma.

### 4.3 O DLI, finalmente com dono

`INBOX.md` tem uma compra pendente desde 2026-09-15: **medidor Apogee DLI-500, ≈460 €.** A
pesquisa 03 resolve-a sem a ter visto:

> Um sensor lux barato (BH1750, 5–8 €) por zona, **calibrado uma vez contra um sensor PAR
> de referência emprestado ou alugado**, dá 80% do valor a 5% do custo. Não vale a pena um
> DLI-500 por zona — vale **um** sensor de referência bom, usado para calibrar vários
> baratos fixos.

**Isto muda a decisão de compra**, não apenas o seu custo: a questão deixa de ser «comprar
ou não o Apogee» e passa a ser «arranjar acesso a um Apogee uma vez, para calibrar sensores
de 6 €». O problema do projecto é **variabilidade espacial** (0,0 h a 4,9 h em zonas a
metros de distância) — e para isso preciso de muitos pontos, não de um ponto exacto.

---

## 5. Onde as pesquisas divergem ou deixam tensão

**Honestidade de método: nem tudo convergiu.**

| Tensão | O que é | Como se resolve |
|---|---|---|
| **Sensor lux vs. modelo solar** | A 03 propõe sensores lux por zona; a T003 tem mandato para modelar sol. Ambos produzem «horas de sol por zona» por vias diferentes. | **Não é conflito, é validação.** A própria 03 declara a fronteira e recusa arbitrá-la: o sensor serve para *validar* o modelo contra medição real. Fica **como proposta para a fase 2**, não como decisão. |
| **Python existente vs. Rhino/Ladybug** | A 02 recomenda Rhino+Grasshopper (≈1.800-2.500 €) mas admite que a pilha mínima só-Python é «a segunda escolha honesta», sobretudo porque **já existe modelo Python validado**. | **Decisão do Arquitecto, não da T005.** Mas registe-se: o modelo da T002 resolve posição solar e **não** resolve sombreamento por geometria 3D complexa — que é exactamente o que a copa da palmeira exige. |
| **Custo de instrumentação vs. histórico do projecto** | A 03 recomenda a configuração «equilibrada» a ≈460-800 €. O projecto tem quatro planos mortos e nenhum orçamento de V2 aprovado (`ESTADO.md` §10, filtro 4 nunca aplicado). | **Não é a T005 que decide.** Sinaliza-se que a monitorização entra numa conta que ainda não existe. |

---

## 6. O que isto faz à proposta de estrutura da fase 2

O `00-PONTO-DE-PARTIDA.md` propôs uma grelha de oito campos. **As pesquisas confirmam-na na
forma e corrigem-na no conteúdo** — faltavam dois campos, ambos revelados pelo cruzamento:

| Campo | Estado | Origem |
|---|---|---|
| Parâmetro · Disciplina · Para que decisão serve · Método · Tolerância · Critério de suficiência · Estado actual · Custo | **Confirmados** | `00-PONTO-DE-PARTIDA.md` |
| **Quando tem de estar medido** *(antes da obra / durante / depois)* | **Novo** | A 03 tem uma secção inteira de faseamento: condutas, cabos e passagens **têm de ser decididos ao mesmo tempo que a T004 decide a geometria** — depois de impermeabilizado e coberto, abrir valas é obra a refazer. **Um parâmetro com a tolerância certa e o timing errado é inútil.** |
| **O que acontece se estiver errado** *(classe de falha)* | **Novo** | A 03 classifica modos de falha em «mata» vs. «só irrita». A 01 faz o mesmo implicitamente: soterrar o colo mata a árvore **a prazo**, o que é pior que matá-la depressa, porque não há sinal a tempo de corrigir. **A consequência do erro é o que deve ordenar a lista, não o custo de medir.** |

---

## 7. O que a fase 1 entrega ao Arquitecto, em quatro pontos

1. **O projecto é tecnicamente uma cobertura ajardinada**, e nenhum documento o tratava
   como tal. Três pesquisas independentes convergiram nisto. Activa um corpo normativo
   (FLL), um modo de falha próprio, e uma ferramenta gratuita de simulação (SWMM Green Roof).

2. **Os +0,50 m estão fixados como cota, mas não decompostos em camadas** — e a decomposição
   é geometria, não acabamento. **Isto é matéria da T004 e é urgente**, porque a obra
   arranca.

3. **A copa da palmeira bloqueia por três razões independentes**, não por uma. Continua a
   custar uma hora. É a melhor relação esforço/desbloqueio de todo o projecto.

4. **A grelha da fase 2 ganha dois campos** — *quando tem de estar medido* e *o que acontece
   se estiver errado* — e o segundo reordena a lista inteira: **a consequência do erro manda,
   não o custo de medir.**

---

## 8. O que esta síntese não fez

- **Não aplicou a grelha.** A fase 2 não arranca sem o Arquitecto ver a fase 1 — é
  instrução explícita do mandato.
- **Não arbitrou T003 × T005.** A sobreposição está declarada em `ESTADO.md` §11 e a
  arbitragem é do Arquitecto, depois de ver as duas.
- **Não integrou a pesquisa de nuvem de pontos**, que foi encomendada depois e ainda não
  chegou. Quando chegar, esta síntese é revista — sobretudo o ponto 3, porque o alvo
  declarado dessa pesquisa é exactamente a copa da palmeira.
- **Não orçamentou nada.** O filtro de custo continua por aplicar em V2.
