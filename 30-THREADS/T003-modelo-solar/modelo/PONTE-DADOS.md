---
created: 2026-09-15
project: Jardim
thread: T003
tipo: ponte-de-dados
---

# Ponte de dados — como o pacote da T001 chega à T003

**Preenchido pelo David. Lido pela sessão T003 na Fase 1.**

Isto resolve o problema de como entregar dados à T003 sem os copiar para dentro
dela e sem escrever caminhos no código.

---

## Como funciona

1. **Tu preenches a tabela da secção A**, abaixo, quando o pacote da T001
   estiver pronto. Uma linha por bloco de dados. Só três colunas: o que é,
   onde está, e em que estado.
2. **A sessão T003 lê esta tabela** e sabe onde ir buscar cada coisa — sem
   procurar, sem adivinhar.
3. **A sessão extrai os valores** e escreve-os em `parametros-activos.yaml`,
   com `origem:` a apontar para a linha desta tabela.
4. **Quando a T001 corrigir um número**, actualizas a coluna «versão» e a
   sessão T003 relê. O valor tem sempre um dono e uma data.

**Porque não copiar os ficheiros para cá:** duas cópias divergem, e passados
dois meses ninguém sabe qual é a boa. Assim há **uma fonte e um apontador**.

**Porque não pôr os caminhos no código:** os caminhos mudam, e um caminho
dentro do código é um valor escondido. Aqui está à vista, num sítio, e é teu.

---

## A — Origem dos dados

Preenche à medida que o pacote fica pronto. Deixa em branco o que não existir.

**FONTE ÚNICA, declarada pelo David em 2026-09-15:**

> **A entrega da etapa 1 da T001.** O ponto de entrada é a nota de entrega da pasta
> `entregue/` dessa thread, que aponta para o **dossier canónico** — 14 secções,
> com semáforo de fiabilidade (🟢/🟡/🔴) e etiqueta de proveniência em cada valor.
>
> **Pede ao David o caminho exacto.** Não o procures.

**Como ler o dossier — é normativo:**

| Semáforo | Significado | Que decisão suporta |
|---|---|---|
| 🟢 | Desenho cotado, medição, ou observação directa confirmada | Decisão **irreversível** |
| 🟡 | Fonte única ou inferência de fotografia. Coerente, não verificado | Decisão **reversível**. **Nunca dimensionamento.** |
| 🔴 | Desconhecido, ou fontes em conflito | **Bloqueia**, ou obriga a plano B declarado |

Etiquetas: `[desenho]` `[foto]` `[observado]` `[medido]` `[estimado]`.
**`[observado]`** é observação directa do proprietário: sobre *comportamento*
prevalece sobre fotografia; sobre *dimensão* cede ao desenho.

**Regra para a T003:** transcreve o semáforo e a etiqueta para o campo `estado:`
de cada parâmetro em `parametros-activos.yaml`. Um valor 🟡 **não serve para
dimensionar**; um 🔴 corre em cenários ou fica declarado como lacuna.

| # | O que a T003 precisa | Onde está | Estado | Versão / data |
|---|---|---|---|---|
| 1 | Coordenadas geográficas e fuso | Dossier §1 | 🟢 lat/long `[desenho]` · altitude `[estimado]` | 2026-09-15 |
| 2 | Convenção de eixos e designação dos limites | Dossier §2.1 | 🟢 `[desenho]` — diagrama normativo, com termos proibidos | 2026-09-15 |
| 3 | Dimensões interiores do recinto | Dossier §2.2 | 🟢 `[desenho]` | 2026-09-15 |
| 4 | Altura de cada limite, medida do solo do jardim | Dossier §2.2, §4.1 | 🟢 `[observado]` — **conflito RESOLVIDO** | 2026-09-15 |
| 5 | **Quais limites têm horizonte livre do lado de fora** | Dossier §3, §4.2 | 🟢 `[observado]` | 2026-09-15 |
| 6 | **Cota até onde cada limite retém terras** (suporte/guarda) | Dossier §2.4, §4.2 | 🟡 `[observado]` | 2026-09-15 |
| 7 | Altura e posição do edifício confinante | Dossier §2.4, §4.1 | 🟡 `[desenho]` — aceite por verificação de escala | 2026-09-15 |
| 8 | Elementos em consola (varandas, palas) | Dossier §4.1 | 🟡 `[foto]` — **dimensões não cotadas** | 2026-09-15 |
| 9 | Envolvente exterior: construção, taludes, desníveis | Dossier §3 | 🟢/🟡 | 2026-09-15 |
| 10 | Vegetação existente: posição de cada exemplar | Dossier §8 | 🟡 `[desenho]` | 2026-09-15 |
| 11 | Vegetação existente: altura, copa, forma | Dossier §8 | 🔴 **palmeira não medida** · lodão `[estimado]` | 2026-09-15 |
| 12 | Vegetação: caduca ou persistente, período de folha | Dossier §8, §5.6 | 🟢 caduca/persistente `[foto]` · período não declarado | 2026-09-15 |
| 13 | Vegetação: quais têm dimensões **medidas** | Dossier §8 | 🔴 **nenhuma** — todas estimadas | 2026-09-15 |
| 14 | Quais exemplares o projecto obriga a manter | **NÃO ESTÁ NO DOSSIER** | — decisão de projecto, **perguntar ao David** | — |
| 15 | Definição das zonas de análise | Dossier §5.4 | 🟢 — 5 zonas com intervalos em X | 2026-09-15 |
| 16 | Tabela de horas de sol já calculada | Dossier §5.4 | 🟡 `[estimado]` | 2026-09-15 |
| 17 | — e essa tabela **inclui ou exclui** a vegetação? | Dossier §5.4, §5.6 | **EXCLUI.** Declarado «sem árvores». §5.6 lista o que subtrai | 2026-09-15 |
| 18 | Fotografias datadas para validação | Dossier §5.5, §11.3 | 🟢 três, com verdicto de validação já dado | 2026-09-15 |
| 19 | Medições instrumentais de luz | Dossier §10 | 🔴 **não existem** — DLI medido está «por instruir» | — |
| 20 | Levantamento de ferramentas de modelação | `research/` da T001 | — **pedir caminho ao David** | 2026-09-15 |

### ⚠ Quatro avisos que a T003 tem de ler antes de montar o modelo

**1. O azimute mudou. Não uses valores antigos.**
A contradição do azimute do eixo longo foi **resolvida**: adoptado **65°/245°**,
não 60°/240°. Consequência: o plano da fachada passou de 150° para **155°**, e as
horas de entrada do sol foram **recalculadas** (+22 min em Dezembro, +7 em Junho —
maior no Inverno porque o Sol percorre o azimute mais devagar quando está baixo).
**Fonte: dossier §5.3.** Qualquer hora de primeira luz que encontres noutro
documento está desactualizada.

**2. As alturas dos muros deixaram de estar em conflito.**
Fixadas em **≤2,50 m** `[observado]` 🟢, confirmado pelo proprietário. O corte de
arquitectura que indicava 3,00 m era de uma **proposta de ampliação** usada
indevidamente como levantamento — foi anotado e passou a concordar.
**Já não corras cenários de 3,00 m** como se fosse hipótese viva. Usa-os só para
demonstrar sensibilidade, se for útil.

**3. Geometria solar de referência já calculada com NREL SPA.**
Altura solar máxima **27,9°** no Inverno e **74,7°** no Verão, mais gamas de
azimute por estação. **Dossier §5.1.** Se o teu modelo não reproduzir estes
valores, tens erro de latitude, de data, ou de fuso — verifica antes de seguir.

**4. Nenhuma dimensão de copa está medida.**
Todas as árvores têm posição `[desenho]` mas dimensões `[estimado]` ou 🔴. A
palmeira — que sombreia a zona SW **todo o ano** — nunca foi medida.
**Corre-as em intervalo de incerteza, não em valor único.** E é isto que limita
a precisão do cenário de rebaixamento do muro SW, porque a palmeira está
exactamente no caminho da luz que entraria.

**Coluna «Estado»:** usa `medido`, `estimado`, `em-conflito`, `observado`, ou
`não existe`. É o que diz à T003 se pode usar um valor único ou tem de correr
em cenários.

**Coluna «Versão / data»:** para a T003 saber se releu a versão certa depois
de uma correcção.

---

## B — Cenários a ensaiar

O modelo não inventa cenários. Diz aqui o que queres testar.

### B.1 Rebaixamento de limites

Para limites com horizonte livre, onde a altura é variável de projecto:

| Limite | Altura actual | Alturas a ensaiar | Extensão do trecho | Elemento substituto |
|---|---|---|---|---|
| **SW** (X máximo) | ≤2,50 m acima do jardim | **≈1,00 m** de alvenaria (enunciado registado no dossier §6.3) + ensaiar também 1,50 e 2,00 m para ver a curva de ganho | *a declarar — todo o limite ou só um vão?* | **Gradeamento leve** sobre alvenaria. Vazado: tem transmissividade própria, não é obstáculo sólido |

**Enunciado exacto da hipótese, do dossier §6.3:** substituir parte da altura do
muro SW por **≈1 m de alvenaria encimada por gradeamento leve**, para passar luz
e ventilar.

**Factos do local que a condicionam** (dossier §6.3, e um deles é novo):

| Facto | Consequência para o modelo |
|---|---|
| Não há vizinho, construção nem terras alheias do lado de fora | Horizonte livre: o rebaixamento traduz-se em luz real |
| A parte a rebaixar está **acima** das terras retidas | É guarda, não suporte — a intervenção é geometricamente possível |
| Terras retidas: **≈5 m abaixo** da cota do jardim; total do muro ≈7,5 m | Define a fronteira suporte/guarda |
| No Inverno cada 10 cm de muro conta; no Verão não mexe | **O ganho é todo invernal.** Reporta Dezembro em destaque |
| A SW o horizonte já está livre — o ganho é **ao nível do pavimento** | Não esperes ganho em altura; o ganho é em superfície iluminada |
| 🔴 Tipo construtivo, fundação e capacidade de carga **desconhecidos** | Fora do teu âmbito. Não avalies viabilidade |
| **⚠ Toda a água do quintal corre para junto desse muro. A intervenção e o ponto de drenagem estão NO MESMO SÍTIO** | Não é matéria do modelo solar, **mas assinala-o no relatório** — é a ligação que o dossier faz e que pode condicionar a obra |

**Obrigatório ao reportar:** ganho em horas por zona e por estação, para cada
cota, **com e sem a palmeira no caminho**. A palmeira fica entre o muro SW e o
resto do jardim, sombreia a zona SW todo o ano, e **as suas dimensões não estão
medidas** — logo o resultado sai em intervalo, não em número único. Dizer isso
explicitamente é parte da resposta.

**Elemento substituto:** se for vazado (gradeamento, ripado, rede), diz o tipo
— não é obstáculo sólido e tem transmissividade própria.

**Extensão:** rebaixar todo o limite ou só um vão? Um vão cria uma janela de
luz que se move com o Sol, e o modelo tem de representar a extensão real.

### B.2 Posições de vegetação

| Exemplar | Posição actual | Posições a ensaiar | Notas |
|---|---|---|---|
| | | | *a declarar* |

**Antes de ensaiar posições, pergunta ao David quais exemplares o projecto
obriga a manter** — não está no dossier, é decisão de projecto (linha 14 da
tabela A).

### B.3 Sensibilidade a parâmetros incertos

O dossier fechou os conflitos de altura de muro. O que resta incerto é
**vegetação**, e é o que limita a precisão:

| Parâmetro | Valores a ensaiar | Porquê |
|---|---|---|
| **Copa da palmeira** (altura, raio) | Intervalo amplo — 🔴 **nunca medida** | Sombreia a zona SW todo o ano **e está no caminho do ganho do rebaixamento do muro SW**. É a maior fonte de incerteza do modelo, agora que os muros estão fixados |
| **Altura e copa do lodão** | ≈5 m `[estimado]` ± margem | Sombreia a metade NW, **mas só em folha** — despido em Dez/Jan |
| **Consola da fachada** | Profundidade e extensão 🟡 `[foto]`, não cotadas | Projecta sombra própria sobre a zona junto à fachada |
| Alturas de muro | **Não correr como conflito.** Fixadas 🟢 | Usar 3,00 m apenas se quiseres demonstrar sensibilidade |

---

## C — Pergunta a responder primeiro

O modelo pode responder a muitas coisas. Diz qual é a primeira, para a sessão
não se dispersar.

**Proposta, a confirmar ou alterar pelo David:**

```
1. Reproduzir a tabela de sol directo por zona do dossier §5.4, agora COM as
   árvores incluídas. O dossier declara explicitamente que a tabela dele é
   "sem árvores" e lista em §5.6 o que subtrai, mas nunca foi quantificado.
   Entregável: a mesma tabela, com e sem vegetação, lado a lado.

2. Quantificar o rebaixamento do muro SW: quanto sol se ganha em cada zona,
   em Dezembro / equinócio / Junho, para alturas remanescentes de 1,00 /
   1,50 / 2,00 m — com e sem a palmeira no caminho.
```

**Porque esta ordem:** a (1) é validação e produz a linha de base; a (2) é a
decisão que está em cima da mesa. Sem a (1), o ganho da (2) não tem contra o
que ser medido.

**Métrica:** **horas de sol directo** basta para as duas. Não é preciso valor
radiométrico nem DLI — o dossier §10 declara que o DLI medido está «por
instruir», e nenhuma decisão em cima da mesa depende de um limiar radiométrico.

**Se o David quiser alterar,** escreve aqui em vez da proposta.

---

## D — O que ficou em falta

A sessão T003 escreve aqui o que pediu e não obteve, para não se perder entre
sessões. **Esta secção é da T003, não tua.**

| Pedido | Data | Resposta |
|---|---|---|
| | | |

---

## Regras desta ponte

- **A T003 não vai procurar ficheiros** que não estejam nesta tabela. Se falta,
  pergunta.
- **A T003 não copia ficheiros** da T001 para dentro da sua pasta. Lê e extrai.
- **Um valor sem linha nesta tabela não entra** em `parametros-activos.yaml`.
- **Se um dado estiver `em-conflito`**, a T003 corre em cenários e reporta o
  intervalo — nunca escolhe um valor por ela.
- **Correcções na T001 não se propagam sozinhas.** Actualiza a coluna «versão»
  e diz à T003 que releia.
