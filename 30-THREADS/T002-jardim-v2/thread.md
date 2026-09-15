---
created: 2026-09-14
updated: 2026-09-16
project: Jardim
thread: T002
assunto: Jardim V2 — soluções e opções viáveis
estado: ACTIVA
sessoes: 0
---

# T002 — Jardim V2

## MANDATO  *(fixo — não alterar)*

> Reescrito pelo Arquitecto em 2026-09-16, por instrução do David. Substitui o mandato de 2026-09-14,
> que era «explorar a oportunidade vantajosa e definir V2». O enunciado do David:
> *«debater soluções para o jardim possíveis, tendo em conta as questões como drenagem, sol, clima,
> custo e o meu gosto. E chegar a opções viáveis.»*

**Debater soluções possíveis para o jardim e chegar a opções viáveis.**

Uma opção é **viável** quando sobrevive aos cinco filtros abaixo e o David a quer. Não basta ser
bonita, nem ser barata, nem ser tecnicamente possível — tem de ser as três coisas ao mesmo tempo, e
tem de sobreviver a Agosto e a Dezembro neste quintal concreto.

### Os cinco filtros

Toda a proposta atravessa estes cinco. Uma proposta que falhe um filtro não é opção — é ideia
descartada, e vai para `REJEICOES.md` com o motivo.

| # | Filtro | O que pergunta |
|---|---|---|
| 1 | **Drenagem** | O que é que isto faz à descarga que já existe e funciona? |
| 2 | **Sol** | Aguenta 4,3 h no equinócio, 1,1 h em Dezembro, e todo o sol nas horas de calor? |
| 3 | **Clima** | Aguenta o Verão de Lisboa e o Inverno húmido e escuro deste recinto? |
| 4 | **Custo** | Quanto custa a fazer, e quanto custa a manter por ano? |
| 5 | **Gosto do David** | Ele quer isto? É a última palavra e não se argumenta contra ela — argumenta-se **antes**, com factos. |

**O filtro 5 não é decorativo.** Quatro planos morreram; nenhum morreu por ser tecnicamente inviável.
Uma solução que o David não queira é tempo perdido, por mais correcta que seja. Perguntar cedo.

### Âmbito

- Debater o que o jardim pode ser, com liberdade — registo, uso, ambiente, o que se vê e o que se
  sente lá.
- **Passar cada hipótese pelos cinco filtros** e dizer explicitamente qual falha e porquê.
- Chegar a **duas a quatro opções viáveis**, distintas entre si, cada uma com o que implica: obra,
  vegetação, custo a fazer, custo a manter, o que se perde ao escolhê-la.
- Rever os 8 princípios herdados de V1: quais se mantêm, quais caem, quais nascem. **Não são canon
  até serem confirmados em `ESTADO.md`.**
- Identificar que decisões precisam de thread própria.
- Faseamento — com atenção a não repetir o encadeamento rígido que bloqueou V1.

### Fora de âmbito

- **Factos sobre o espaço existente.** São da T001. Lê o dossier canónico (ver abaixo) ou pergunta
  pelo canal de mensagens. **Não os redescubras nem os recalcules.**
- **Quantificação de sombra** para cenários novos. É da T003 — pede pelo canal.
- Execução, contactos, negociação com fornecedores.
- Estrutura do Notion.

### Entrega esperada

Documento em `entregue/` com as opções viáveis, cada uma atravessada pelos cinco filtros, mais nota
explicativa. O Arquitecto absorve para `ESTADO.md`, `REJEICOES.md` e `20-PLANO/`.

**Tipo:** `NORMAL` — fecha quando as opções estiverem entregues e absorvidas.

---

## O QUE JÁ SE SABE — ler antes de debater

**O documento canónico do Local é `../T001-local/Docs-David-Local/DOSSIER-LOCAL.md`.**
827 linhas, com semáforo de fiabilidade por secção. 🟢 suporta decisão irreversível · 🟡 só decisão
reversível, nunca dimensionamento · 🔴 bloqueia ou obriga a plano B declarado.

**Lê também `ESTADO.md` §01 e `REJEICOES.md` §01–§11 na raiz.** A regra O9 obriga: consultar as
rejeições **antes** de propor, e assinalar se já foi rejeitado e porquê.

### Os factos que mais condicionam o debate

| Facto | Consequência |
|---|---|
| **Muros a 2,50 m, corredor de 5,78 m, sol de Inverno a 27,9°** | A sombra de Inverno é de ≈4,7 m — quase a largura inteira. **O Inverno não é escuro por orientação, é por proporção.** |
| **4,3 h de sol no equinócio, 1,1 h em Dezembro, tudo à tarde** | Abaixo do limiar de qualquer gramínea (mínimo 3 h). E o problema **não é o Inverno** — é o Verão, porque a exigência de luz duplica com o calor e o sol todo vem nas horas de stress térmico. |
| **A drenagem existe e funciona** | Liga-se ao que existe, não se constrói de zero. **O erro caro deste projecto é destruir ou entupir com entulho uma descarga que funciona há décadas.** |
| **Z5 é sombra, não meia-sombra** (0,0 / 1,0–1,5 / 2,5–3,0 h) | A copa da palmeira sombreia-a todo o ano. Trata-se como Z4. |
| **Z5 não comporta árvore nova nem canteiro elevado** | Terra vegetal saturada: 40 cm = ~700 kg/m². Em ≈15 m², até ~15 t no tardoz de um muro de suporte de ~95 anos. |
| **A palmeira compete por água em todo o raio da copa** | Raiz fibrosa e não agressiva — **boa notícia para o muro**. Mas tudo o que se plantar em Z5 e no extremo de Z3 cresce mais devagar do que qualquer ficha indica. |
| **Execução no terreno: zero** | Sem custo afundado, sem obra a corrigir. V2 arranca de folha limpa. |

### Material de trabalho já produzido pela T001

Não é canon — é matéria-prima com fontes. Está em `../T001-local/research/`:

| Ficheiro | O que dá |
|---|---|
| `Jardim_Catalogo_Vegetal.md` (104 KB) | Espécies viáveis por zona Z1–Z5 × cenário de profundidade P1–P4, 10 estratos. **Sem recomendação de escolha** — a escolha é deste debate. |
| `Jardim_Relva_Natural_Viabilidade.md` (123 KB) | Porque é que gramíneas não funcionam, com limiares publicados e fontes. Alternativa proposta: *Zoysia tenuifolia* em placa nos ≈38 m² da metade NE + *Dichondra repens* nas zonas sombrias + SW mineral e leve. |
| `Jardim_Software_Modelacao_Solar.md` | Levantamento de ferramentas. Via Google 3D fechada. |
| `Estado_Arte_Caracterizacao_Espaco_Exterior.md` | Como se caracteriza um espaço exterior. |

**Uma reserva sobre este material:** foi escrito em grande parte sobre a premissa errada de que a
água estagnava. A correcção já foi aplicada nos ficheiros, mas a consequência ainda não foi toda
digerida — **as mediterrânicas de folha rija deixaram de estar excluídas por encharcamento** e
voltam a ser candidatas em Z1–Z3. A rejeição por falta de luz mantém-se intacta em Z4 e Z5.

---

## A HIPÓTESE EM CIMA DA MESA — rebaixar o muro SW

Levantada pelo David em 2026-09-15. **Pode ser o maior ganho de luz disponível no projecto**, e é
por isso que entra aqui e não numa thread própria.

**Os dois factos que a tornam possível:**
- O muro SW **não tem nada do lado de fora** — sem vizinhos, sem construção.
- **A parte que tapa o jardim não tem função de suporte.** Só a porção abaixo do nível das terras
  retidas é estrutural; o que está acima é **guarda**.

**Consequência:** a altura desse muro deixa de ser dado do local e passa a ser **variável de
projecto**.

**Porque pode valer muito:** num recinto estreito e fundo a altura dos limites domina o Inverno —
está registado que 0,50 m de diferença **duplicou** a média de sol de Dezembro. O sol de Inverno vem
de S/SW a ≈27° de altura, exactamente o quadrante deste muro. E a Z5 é hoje a pior zona do jardim.

**As reservas, todas por resolver:**
- A palmeira fica entre o muro e o resto do jardim. O sol que entrar **atravessa a copa**, que é
  pinada e dá luz salpicada, não sol directo.
- **A intervenção proposta e o ponto de drenagem estão no mesmo sítio.**
- A fronteira suporte/guarda **ainda não foi medida**. Se for mal identificada, um rebaixamento corta
  estrutura em vez de guarda.
- O tipo construtivo e a fundação do muro são **desconhecidos** — está no Arquivo Municipal, por
  consultar.
- Por decidir, e fora do âmbito da T003: admissibilidade estrutural, condomínio, privacidade sobre o
  logradouro, ruído, segurança (**queda de 7–8 m do lado de fora**), enquadramento legal.

**Como tratar:** debate-se aqui como hipótese de projecto. **Não se decide sem os dados que faltam.**
Pede-se à T003 a quantificação do ganho — horas por zona e por estação, para cada cota de
rebaixamento, com e sem a vegetação no caminho. A admissibilidade é decisão do Arquitecto.

---

## CONTEXTO HERDADO — porque morreram os quatro planos

| Plano | Data | Âmbito | Porque parou |
|---|---|---|---|
| V1 completo (F1–F6) | até Mar 2026 | 7.800–12.500 € | Dependia de três terceiros e de encadeamento rígido. |
| Conceito 3 ambientes (Adriano) | Fev 2026 | 1.200 € mão-de-obra | Recusado: sem discriminação. Adriano sem resposta desde 2026-03-01. |
| DIY temporário | Mai–Jul 2026 | ~500 € declarado / 675–1.048 € real | Janela Mai–Set 2026 expirou sem balanço. |
| Dossier palmeira | Mai 2026 | 300–600 € + 50–400 €/ano | Nunca integrado. |

**A leitura do Arquitecto, que esta thread tem de levar a sério:**

V1 não parou por ser ambicioso demais. Parou porque **nada podia acontecer antes da demolição, e a
demolição dependia de terceiros não controlados.** O DIY foi o recuo correcto perante isso, mas foi
desenhado *ao lado* do plano grande, não dentro dele — daí o conflito dos canteiros. E **também não
arrancou.**

**Baixar a ambição já foi tentado e não resolveu.** V2 tem de resolver **dependência e sequência**,
não apenas tamanho.

> **Teste a aplicar a cada opção antes de a declarar viável:**
> *«O que é a primeira coisa que acontece nesta opção, e depende de quem?»*
>
> Se a resposta for «de um terceiro que ainda não disse que sim», a opção tem o mesmo defeito que
> matou V1. Ou se corrige, ou vai para `REJEICOES.md`.

### Os 8 princípios herdados de V1 — a rever, não são canon

1. A palmeira é protagonista absoluta.
2. Vê-se a luz, nunca a luminária.
3. Escuridão estratégica.
4. Três artistas, três territórios.
5. Dois jardins num — mediterrânico de dia, instalação de arte de noite.
6. Contenção. A arte UV é surpresa, não circo.
7. O jasmim dá cheiro — luz, água e aroma como uma só composição.
8. Mediterrânico, não tropical.

---

## PERGUNTAS DE ARRANQUE

Para o David, na primeira sessão. **Ouvir primeiro, estruturar depois.**

1. **O que queres fazer neste espaço?** Estar, receber, ver da janela, tratar dele, esquecê-lo.
   Define tudo o resto.
2. **Quanto tempo por mês estás disposto a dar-lhe?** É a variável que mais separa opções viáveis de
   opções bonitas.
3. **Que ordem de grandeza de orçamento?** Não o número exacto — o escalão. Centenas, dois mil,
   cinco mil.
4. **O que é que V1 tinha que ainda queres?** E o que é que já não queres.
5. **Há alguma janela temporal a respeitar?** A da laranjeira é Fev–início de Março, e é mais dura
   que qualquer roadmap.

---

## ESTADO FACE AO MANDATO  *(reescrito a cada sessão)*

**Última sessão:** —
**Estado:** Por arrancar. Mandato reescrito em 2026-09-16, bloqueio levantado, base factual
disponível. Nenhuma sessão de debate ainda.

---

## HANDOFF  *(para a próxima sessão desta thread)*

**Próximo passo:** primeira sessão de debate. Começar pelas perguntas de arranque — **ouvir o David
antes de propor seja o que for.** Só depois passar hipóteses pelos cinco filtros.

**À espera de:** nada. Pode arrancar.

**Cuidado com:**

- **O quinto plano.** É o risco desta thread, e é real. Um documento bonito que não arranca é o que
  este projecto já produziu quatro vezes. Uma opção só é viável se a **primeira coisa a acontecer**
  não depender de ninguém de fora.
- **Não redescobrir o Local.** O dossier existe e tem semáforo. Se um facto for 🔴, diz-se que é 🔴 e
  declara-se plano B — não se inventa.
- **Consultar `REJEICOES.md` antes de propor** (regra O9). Se já foi rejeitado, dizê-lo e dizer
  porquê. Reabrir é legítimo; reabrir sem saber que se está a reabrir, não.
- **Perguntar o gosto cedo.** O filtro 5 aplicado no fim desperdiça o trabalho todo.
