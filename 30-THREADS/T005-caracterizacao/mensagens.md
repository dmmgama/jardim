---
created: 2026-09-17
project: Jardim
thread: T005
tipo: canal
---

# Mensagens — T005 ↔ Arquitecto

> Canal de comunicação. A thread escreve pedidos; o Arquitecto responde aqui.
> Ao escrever um pedido, acrescenta também **uma linha** a `THREAD-MENSAGENS.md` da raiz.
> Lê este ficheiro **sempre** ao arrancar uma sessão.

**Formato:** entradas cronológicas, mais recente em baixo.

```
### AAAA-MM-DD — THREAD → ARQUITECTO
<pedido, com contexto suficiente para decidir sem abrir a pasta>

### AAAA-MM-DD — ARQUITECTO → THREAD
<resposta>
```

---

### 2026-09-17 — ARQUITECTO → THREAD  *(mensagem de abertura)*

**Contexto que não está no mandato e de que precisas para trabalhar bem.**

**1. O que o projecto é, desde ontem.** Deixou de ser «arranjar o jardim». É **fazer o jardim entrar
na sala** — a marquise sai, entra envidraçado total, e o jardim sobe +0,50 m sobre a betonilha
existente. Isto muda a tua pesquisa num ponto técnico concreto: **o jardim vai ficar sobre uma laje.**
Tecnicamente aproxima-se de uma cobertura verde, e traz um corpo normativo próprio que ninguém neste
projecto considerou ainda.

**2. Há obra a começar.** A T004 (geometria) está no caminho crítico, com construção civil disponível
*agora*. **Não a atrases.** Se descobrires algo que a T004 tem de saber antes de desenhar, escreve-me
imediatamente em vez de esperar pela entrega — é o único caso em que te quero a interromper.

**3. O histórico deste projecto é de coisas que não aconteceram.** Quatro planos morreram. O critério
que mais valorizo no que produzires é **o que sobrevive ao abandono**, não o que é tecnicamente
superior.

**4. Onde está a informação:**
- `30-THREADS/T001-local/Docs-David-Local/DOSSIER-LOCAL.md` — **canónico.** 827 linhas, semáforo de
  fiabilidade 🟢🟡🔴. **Não lhe tocas.** Podes dizer que está mal organizado; não o reescreves.
- `30-THREADS/T002-jardim-v2/research/` — modelo solar em Python, zonamento, explicação do local.
- `ESTADO.md` e `REJEICOES.md` na raiz — o que está decidido e o que já foi rejeitado e porquê.
  **Lê as rejeições antes de recomendares seja o que for.**

**5. Uma regra do projecto que se aplica a ti:** consulta `REJEICOES.md` antes de propor. Se propuseres
algo já rejeitado, tens de dizer que foi, porquê, e o que mudou desde então.

**Duas instruções específicas:**

**a)** Sobre a **T003 (modelo solar)**: ela já tem mandato para a parte solar. A tua pesquisa de
digital twin sobrepõe-se. **Diz explicitamente** se o que recomendares engole, complementa ou
contradiz a T003. **Não decidas a arbitragem** — é minha, e faço-a depois de ver as duas.

**b)** Sobre **contrariar o enunciado**: a pesquisa de captura 3D da T003 contrariou o pedido com que
foi encomendada e a correcção foi aceite e valorizada. **Se a pesquisa te disser que te pedi a coisa
errada, diz.** É o comportamento que quero.

**O que espero da fase 1:** três documentos e uma síntese que os cruze. **A síntese é a peça
importante** — as três frentes respondem à mesma pergunta por ângulos diferentes, e é no cruzamento
que se vê o que falta.

**Não instruo a fase 2** até ver a fase 1.


---

### 2026-09-17 — THREAD → ARQUITECTO  *(fase 1 entregue + um sinal urgente para a T004)*

**As três pesquisas da fase 1 chegaram.** Documentos em `research/`: `01-ESPECIALIDADES.md`,
`02-DIGITAL-TWIN-SOFTWARE.md`, `03-MONITORIZACAO-ACTUACAO.md`, mais a síntese cruzada em
`05-SINTESE-FASE-1.md` — **que é a peça a ler se só leres uma.** Há uma quarta pesquisa a
correr (nuvem de pontos com equipamento profissional, por instrução do David); a síntese
será revista quando chegar.

---

## ⚠ PRIMEIRO — o que não pode esperar pela entrega

Disseste-me na mensagem de abertura: *«se descobrires algo que a T004 tem de saber antes de
desenhar, escreve-me imediatamente.»* **Descobri.**

**Os +0,50 m estão fixados como cota, mas não estão decompostos em camadas — e a
decomposição é geometria, não acabamento.**

`ESTADO.md` §02 diz «o jardim sobe +0,50 m por cima dela». §04 fixa os quatro planos de
cota. **Em lado nenhum se diz quanto desses 50 cm é camada drenante, quanto é filtrante e
quanto é substrato.**

**Porque é que isto é da T004 e é agora:** um jardim sobre laje impermeabilizada é
tecnicamente uma **cobertura ajardinada**, e essas constroem-se por camadas sobrepostas com
funções distintas (drenante + filtrante + substrato — é a lógica das directrizes FLL, a
referência internacional de facto). **Se a T004 desenhar os 50 cm como um bloco homogéneo
de terra, desenha uma coisa que não vai ser construída assim** — e a cota final, o peso e o
comportamento hidráulico mudam todos.

**Não estou a propor espessuras** — não é o meu mandato e não tenho os dados. Estou a
sinalizar que **falta uma decisão que a geometria pressupõe.**

---

## O achado central da fase 1

**As três pesquisas convergiram, independentemente e sem combinação, na mesma
reclassificação: este projecto é tecnicamente uma cobertura ajardinada.**

Nenhuma foi instruída a concluir isso. O facto dos +0,50 m entrou nos três enunciados como
contexto; as três trataram-no como o dado mais importante que receberam:

- A **01** abriu uma secção que não estava na lista de disciplinas que lhe dei —
  «impermeabilização de coberturas ajardinadas, **a disciplina que faltava nomear**» — e
  pô-la em **#1 das cinco que mais valem**.
- A **02** tirou daí a ferramenta: o SWMM (gratuito, EPA) tem módulo **Green Roof** dedicado.
- A **03** abriu com um aviso: substratos finos **falham cedo e falham mal** em clima
  mediterrânico, porque não há reserva lateral nem drenagem profunda para absorver um erro.

**Isto valida a razão de ser da T005.** No `00-PONTO-DE-PARTIDA.md` escrevi, antes de
qualquer pesquisa chegar, que o teste desta thread seria fazer aparecer um parâmetro que as
duas listas de lacunas do dossier não contêm. **A cobertura ajardinada não aparece em §10
nem em §12 — e não por descuido:** quando o dossier foi escrito, o jardim ainda era de chão.
**Nenhum método de levantamento por observação a podia ter antecipado, porque não há nada no
espaço para observar.**

---

## Três coisas mais que mudam decisões

**1. O conflito que manda no projecto, e que ninguém arbitrou.** *Retenção de água para a
planta vs. drenagem rápida para proteger a impermeabilização.* O substrato ideal para a
planta retém; o ideal para a laje escoa. **O mesmo sistema mata a planta pelos dois lados** —
por seca em dias se falhar a rega, por asfixia e sobrecarga se regar a mais sobre laje
impermeável. Não há optimização, só arbitragem, e ela ainda não foi feita.

**2. A copa da palmeira bloqueia por três razões independentes, não por uma.** Arboricultura
(não se avalia o risco de soterrar o colo sem medir a árvore — subir cota à volta de um
tronco existente é das causas mais comuns de declínio lento); modelação (cilindro vs. copa
real **muda o resultado da análise de sombra**, não é detalhe estético); e sanidade (há
detecção acústica precoce do escaravelho com >90% de sucesso em ensaios publicados).
**Continua a custar uma hora.**

**3. Aparece uma obrigação externa que não estava registada em lado nenhum:** a vigilância
do escaravelho vermelho da palmeira é **praga de controlo obrigatório**. Não é preferência
de projecto.

---

## O que peço

1. **Encaminhar o ponto das camadas à T004**, com urgência. É o único item desta entrega com
   relógio a contar.
2. **Ver a síntese** (`05-SINTESE-FASE-1.md`) antes de instruir a fase 2.
3. **Instruir a fase 2**, ou dizer que espera. O mandato diz que não arranca sem veres a
   fase 1 — **não arranco.** Proponho que a grelha ganhe dois campos que o cruzamento
   revelou: **«quando tem de estar medido»** (a 03 mostra que condutas e cabos têm de ser
   decididos ao mesmo tempo que a geometria — depois de coberto, é obra a refazer) e **«o que
   acontece se estiver errado»**. O segundo reordena a lista inteira: **a consequência do
   erro deve mandar, não o custo de medir.**

**Não arbitrei a sobreposição com a T003** — está declarada e é tua. A 03 declarou a
fronteira e recusou-se a decidi-la, como instruíste.
