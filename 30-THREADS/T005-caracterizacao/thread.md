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
**Estado:** Fase 1 em execução — três pesquisas lançadas em paralelo.

Thread criada e arrancada na mesma sessão, por instrução directa do David
(«cria a thread de imediato e passas logo a funcionar dentro dela»).

---

## HANDOFF  *(para a próxima sessão desta thread)*

**Próximo passo:** Ler as três pesquisas, produzir a síntese cruzada, e levar ao
Arquitecto a proposta de estrutura da fase 2.
**À espera de:** Nada. A fase 1 não depende de terceiros.
**Cuidado com:** O risco desta thread é **produzir uma enciclopédia em vez de uma
regra.** O quintal tem ~75 m². Uma caracterização que exija instrumentação de
estação agronómica falha o mandato, mesmo estando correcta.
