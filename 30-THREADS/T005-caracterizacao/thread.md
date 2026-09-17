---
created: 2026-09-17
project: Jardim
thread: T005
estado: ACTIVA
tipo: ONGOING
sessoes: 1
---

# T005 — Pesquisa e definição de regras para caracterização do espaço

## MANDATO  *(fixo — não alterar)*

**Organizar a informação que o projecto já tem numa estrutura de caracterização do
espaço conforme ao estado da arte das especialidades envolvidas** — paisagismo,
jardinagem, geotecnia, drenagem, climatologia, e as demais que a própria thread
identificar.

O projecto acumulou muita informação (dossier do Local com 827 linhas, modelo solar
da T002, pesquisas dispersas) **organizada por conveniência de quem a recolheu, não
por disciplina.** Falta saber o que as disciplinas que tratam deste tipo de espaço
consideram ser a caracterização mínima — e, a partir daí, o que este projecto tem,
o que lhe falta, e com que regra se decide que um parâmetro está caracterizado.

### Âmbito

**Fase 1 — pesquisa (esta sessão).** Três frentes em paralelo:

1. **Quem são os especialistas.** Que disciplinas intervêm num projecto desta
   natureza, o que cada uma caracteriza, com que métodos e que normas, e onde se
   sobrepõem ou entram em conflito.

2. **Digital twin — software.** Levantamento de ferramentas open source e
   comerciais que permitam modelar o jardim e a envolvente: geometria, física,
   sol e sombra, luminância, água, solo, vegetação com crescimento. Não só
   caracterizar o existente — **fazer experiências.**

3. **Monitorização e actuação.** Sensores e parâmetros mensuráveis em contínuo, e
   mecanismos de controlo accionáveis a partir dessas medições — rega, iluminação,
   nutrição, sombreamento. Do sensor ao actuador, incluindo o que se mede mal ou
   não vale a pena medir.

**Fase 2 — regras (por instruir).** Converter a pesquisa numa estrutura de
caracterização: que parâmetros, por disciplina, com que método, tolerância e
critério de suficiência. **Não arranca sem o Arquitecto ver a fase 1.**

### Fora de âmbito

- **Decidir o que se planta, constrói ou compra.** A T005 define *como se
  caracteriza*, não o que se faz com a caracterização.
- **Medir no terreno.** A T005 consome e estrutura; as medições são da T001.
- **Refazer o dossier do Local.** O `DOSSIER-LOCAL.md` é canónico. A T005 pode
  dizer que está mal organizado ou incompleto; **não pode reescrevê-lo.**
- **Escolher a ferramenta de modelação.** Recomenda com critério; quem escolhe é o
  Arquitecto, e a T003 tem palavra na parte solar.
- **Construir o digital twin.** Levantamento, não implementação.

### Entrega esperada

**Fase 1:** três documentos de pesquisa em `research/`, mais uma síntese que os
cruze — porque as três frentes respondem à mesma pergunta por ângulos diferentes, e
é no cruzamento que se vê o que falta.

**Tipo:** `ONGOING` — entrega por fases, não fecha na primeira.

### Fronteira com as threads existentes

| Thread | Fronteira |
|---|---|
| **T001 — Local** | A T001 produz factos; a T005 diz que factos deviam existir. **A T005 não escreve no dossier.** |
| **T003 — Modelo solar** | A T003 já escolhe ferramenta para *sol*. A T005 olha para o modelo **inteiro** e tem de dizer explicitamente se o que recomenda engole, complementa ou contradiz a T003. |
| **T004 — Geometria** | Caminho crítico da obra. **A T005 não a atrasa nem a bloqueia.** |

---

## ESTADO FACE AO MANDATO  *(reescrito a cada sessão)*

**Última sessão:** 2026-09-17
**Estado:** **Fase 1 entregue ao Arquitecto.** Quarta pesquisa em curso. Fase 2 por instruir.

Thread criada e arrancada na mesma sessão, por instrução directa do David.

### O que está feito

| Documento | O que é |
|---|---|
| `research/00-PONTO-DE-PARTIDA.md` | Diagnóstico da estrutura de informação existente, **escrito antes de as pesquisas chegarem**, de propósito — para ser possível testar depois se elas respondem à pergunta certa. |
| `research/01-ESPECIALIDADES.md` | 16 disciplinas, com métodos, normas, fase de intervenção e decisões bloqueadas. Matriz de conflitos entre disciplinas. |
| `research/02-DIGITAL-TWIN-SOFTWARE.md` | Nove eixos de software, três pilhas com custo, e cepticismo documentado sobre o termo «digital twin» a esta escala. |
| `research/03-MONITORIZACAO-ACTUACAO.md` | Sensores, protocolos, plataformas, actuadores. Três configurações com custo e manutenção. Modos de falha classificados em «mata» vs. «só irrita». |
| `research/05-SINTESE-FASE-1.md` | **A peça principal.** O que só aparece no cruzamento das três. |
| `mensagens.md` | Entrega comunicada, com sinal urgente para a T004. |

### O achado que justifica a thread

**As três pesquisas convergiram, independentemente e sem combinação, em que o projecto é
tecnicamente uma cobertura ajardinada.** Nenhuma foi instruída a concluí-lo.

Isto **passou o teste** que `00-PONTO-DE-PARTIDA.md` tinha fixado à cabeça: fazer aparecer
um parâmetro que as duas listas de lacunas do dossier não contêm. **Não contêm, e não por
descuido** — quando o dossier foi escrito o jardim ainda era de chão, e nenhum levantamento
por observação podia antecipar uma coisa que ainda não existe no espaço.

### A quarta pesquisa — chegou e está integrada

`research/04-NUVEM-DE-PONTOS.md`, por instrução do David de 2026-09-17: *«tenho eventualmente
possibilidade de arranjar máquina. Só preciso depois de tratar o que daí vier.»*

**Veredicto dividido:** vale a pena **para a copa da palmeira** (forma 3D real com erro de poucos
cm); **não justifica sozinha para os muros** (o telémetro de 30 € continua a ganhar).

**A inversão de intuição:** o reboco liso é o **pior caso para fotogrametria e um dos melhores
para TLS** — o laser mede tempo de voo e não precisa de textura. **Não contradiz `REJEICOES.md`
§11**, que rejeitou captura por *telemóvel*; o que separa os casos é física da superfície, não
qualidade de equipamento.

**A cadeia de tratamento é gratuita e corre em Windows 10** (CloudCompare até à malha, que entra
no motor solar) — responde à preocupação declarada do David. **Síntese actualizada** em §3.1 e §7.

---

## HANDOFF  *(para a próxima sessão desta thread)*

**Última actualização:** 2026-09-18, fim da sessão «2026.09.17 - Arquiteto - Pesquisa de Catalogacao».

---

### Onde a thread está

**Fase 1 entregue e integrada.** Cinco documentos de pesquisa, uma síntese cruzada e um report,
todos em `research/` e `reports/`. **A fase 2 não arrancou e não deve arrancar sem instrução
do Arquitecto** — o mandato é explícito.

**Pedido em mão, sem resposta:** `mensagens.md`, três pontos — encaminhar a questão das camadas
à T004, ver a síntese, instruir ou adiar a fase 2.

---

### ⚠ Uma pesquisa foi lançada e pode ter terminado depois desta nota

**`research/06-AGENTES-E-OPENSOURCE.md`** — agentes de IA, skills e projectos open source
adoptáveis para as áreas que a fase 1 identificou. Três eixos: agentes especializados por
disciplina · open source para análise e estudo · instrumentação, dados e automatização.

**Encomendada pelo David a 2026-09-18**, executada por subagente com instrução para: ler as
cinco pesquisas da fase 1 antes de pesquisar · incluir no report **o prompt integral e a lista
do que leu** · registar em `REGISTO-DOCUMENTOS.md` · carregar no NotebookLM com deck próprio e
PDF descarregado para `research/`.

> **PRIMEIRA COISA A FAZER NA PRÓXIMA SESSÃO: verificar se este trabalho ficou completo.**
>
> | Verificar | Onde |
> |---|---|
> | O report existe e tem o prompt lá dentro | `research/06-AGENTES-E-OPENSOURCE.md` |
> | O PDF do deck foi descarregado | `research/T005-26-09-18-RESEARCH-AGENTES-E-OPENSOURCE.pdf` |
> | A source e o artefacto têm o nome de convenção no NotebookLM | `T005-26-09-18-RESEARCH-AGENTES-E-OPENSOURCE` |
> | A linha entrou no registo | `REGISTO-DOCUMENTOS.md` da raiz |
> | **Não** escreveu no `INBOX.md` da raiz | `INBOX.md` — foi-lhe dada contra-ordem a meio |
>
> **Duas armadilhas conhecidas, das quatro pesquisas anteriores:** o `title` passado na criação
> do deck **não pega** — o artefacto nasce com o nome do notebook e **tem de ser renomeado**; e
> o status fica em `unknown` enquanto gera, não em `in_progress`, pelo que um download
> prematuro falha com erro genérico.

**Porque é que o registo desta pesquisa está aqui e não no `INBOX.md`:** instrução directa do
David, 2026-09-18. O inbox da raiz é do Arquitecto; **o que a thread produz regista-se na
thread**, e sobe pelo canal de mensagens quando houver o que reportar.

---

### Entregue nesta sessão, fora do mandato

**`entregue/protocolo-registo-documentos/`** — instruções, template e draft do protocolo de
registo de documentos, mais um README que os indexa. **Não é matéria do mandato da T005**: foi
encomendado pelo David a meio da sessão e produzido por subagentes. **Está aqui por ser trabalho
desta sessão, não por pertencer à thread** — e a decisão é do Arquitecto, sinalizada no
`INBOX.md`.

---

### Próximo passo

1. **Verificar a pesquisa 06** (quadro acima). Se ficou a meio, completar.
2. **Integrá-la na síntese** — a `05-SINTESE-FASE-1.md` cobre quatro pesquisas, não cinco.
   Tem secção §3.1 dedicada à quarta; a quinta precisa de tratamento equivalente.
3. **Esperar o Arquitecto** para a fase 2.

**À espera de:** resposta em `mensagens.md` aos três pedidos da entrega da fase 1.

---

### Cuidado com

1. **O risco original mantém-se, e agravou-se.** Produzir uma enciclopédia em vez de uma regra.
   São agora **cinco** pesquisas densas. **A fase 2 tem de cortar, não acumular** — uma grelha de
   oito parâmetros que se preenche numa tarde vale mais que uma de trinta que ninguém preenche.
2. **Não arbitrar a sobreposição com a T003.** Está declarada em `ESTADO.md` §11 e é do Arquitecto.
3. **Não atrasar a T004.** Se houver dúvida entre esperar e sinalizar, **sinalizar**.
4. **A pesquisa 06 é sobre ferramentas, não sobre o jardim.** Se a fase 2 começar a desenhar
   automatismos em vez de definir o que se caracteriza e com que tolerância, **saiu do mandato**.
