# T003 — o que isto é, e o que vai acontecer

*Escrito para ti, não para o agente. 2026-09-15.*

---

## Em duas linhas

A T003 constrói um **modelo digital do quintal** onde podes mover uma árvore
e ver a sombra mudar. Está preparada para **não ter dados nenhuns** — pede-te
tudo, tu dizes onde está.

---

## Porque é que não tem dados

Pediste isto explicitamente, e fizeste bem. A versão anterior desta pasta tinha
um ficheiro com os valores todos copiados da T001 — geometria, alturas,
posições das árvores. Isso cria dois problemas:

1. **Duplicação que divergem.** No momento em que corriges um número na T001,
   a T003 fica errada e ninguém repara. Foi exactamente assim que nasceram
   as duas cotas em conflito no projecto antigo.
2. **Números sem dono.** Passados três meses, ninguém sabe se o `2,50` da T003
   é o mesmo `2,50` da T001, ou uma estimativa que alguém lá pôs.

Agora a T003 **não sabe nada**. Tem uma lista do que precisa, e a obrigação de
te perguntar.

---

## Os ficheiros, e para que servem

| Ficheiro | O que é |
|---|---|
| **`LEIA-ME-DAVID.md`** | Este. Para ti. |
| `thread.md` | O mandato da thread e onde ela ficou. Governo. |
| `mensagens.md` | Canal entre a thread e o Arquitecto. |
| **`modelo/contrato-de-dados.yaml`** | **A peça central.** Lista tudo o que o modelo precisa, porquê, e o que acontece se estiver errado. **Não tem valores.** |
| **`modelo/PONTE-DADOS.md`** | **É aqui que entregas o pacote da T001.** Uma tabela: o que é, onde está, em que estado. Preenches tu. |
| `modelo/parametros-activos.yaml` | Vazio. É onde os valores entram, quando tu disseres de onde vêm. |
| `research/00-PACOTE-ARRANQUE.md` | As opções de ferramenta comparadas, com recomendação. |
| `research/01-PLANO-DE-SESSAO.md` | A sequência de trabalho que o agente vai seguir. |
| `mockups/layouts-jardim.html` | Os 11 layouts. Exploratório, não oficial, e não é mandato desta thread. |

---

## O que vai acontecer quando abrires a sessão T003

**Sessão nova** → responde `THREAD` → escolhe T003.

Ela vai fazer isto, por esta ordem:

### 1. Verificar o ambiente (~30 min)
Ver se tens Python, `pvlib`, `shapely`, `PyYAML`. **Já se sabe que o `PyYAML`
não está instalado** — apareceu neste ambiente hoje. Ela instala.

### 2. Entrevistar-te
É a fase que te vai custar tempo, e é o ponto todo. Ela percorre o contrato
e pergunta, bloco a bloco: **onde está este dado?**

Tu respondes com o ficheiro, o valor, ou "não existe". Ela escreve a resposta
**e a origem** no `parametros-activos.yaml`.

**As perguntas que ela é obrigada a fazer:**

- **Altura dos muros, medida do solo do jardim.** Está registado que há
  conflito de fontes e material gráfico com valores diferentes. Ela vai
  perguntar qual é o valor vigente e se já mediste.
- A convenção de eixos e nomes dos muros — para os outputs serem comparáveis
  com o resto do projecto.
- Quais árvores têm dimensões **medidas** e quais são estimadas.
- Quais árvores o projecto obriga a manter (separar o fixo do móvel).
- Folha caduca ou persistente, por árvore.
- Se já existe tabela de horas de sol — e **se inclui ou exclui a vegetação**.
- Que fotografias datadas existem.
- Qual a pergunta que queres responder primeiro.

Se disseres "não existe", ela escreve em `lacunas:` e continua. Não bloqueia.

### 3. Montar o modelo (4–10 h de trabalho dela)
Três módulos: ler parâmetros, construir geometria, calcular sol.
Com uma regra rígida: **se um parâmetro falta, o código dá erro e diz qual.**
Nunca assume um valor por omissão. É isso que impede o hardcoding de voltar.

### 4. Validar antes de te dar um único número
Ela está proibida de reportar resultados antes de validar contra as
**fotografias datadas**. Se tiveres duas fotos com sombras opostas, o modelo
que reproduza a inversão está geometricamente certo. Custa zero e é o melhor
teste que existe.

### 5. Só então responder à pergunta
Tabela de horas de sol por zona, e os cenários de posição de árvore que
quiseres testar.

---

## O que ela NÃO vai fazer

- Não vai procurar ficheiros pelo repositório por iniciativa própria.
- Não vai escrever caminhos no código.
- Não vai copiar valores de documentos de outras threads.
- Não vai preencher um dado que falta com um número plausível.
- Não vai decidir que espécie plantar nem onde — isso é do Arquitecto.

---

## Como entregas o pacote da T001

**Em `modelo/PONTE-DADOS.md`.** Preenches uma tabela com três colunas: **o que
é · onde está · em que estado**. Vinte linhas, e deixas em branco o que não
existir.

Não copias ficheiros para cá, e não escreves caminhos em código nenhum. A
sessão T003 lê a tabela, vai buscar os valores às fontes que indicares, e
escreve-os em `parametros-activos.yaml` com a origem a apontar para a linha
da tabela.

**Porque assim e não a copiar os ficheiros:** duas cópias divergem. No dia em
que corriges um número na T001, a cópia na T003 fica errada e ninguém repara —
foi assim que nasceram as duas cotas em conflito no projecto antigo. Com a
ponte há **uma fonte e um apontador**, e cada valor tem dono e data.

Quando corrigires algo na T001, actualizas a coluna «versão» e dizes à T003 que
releia. Correcções não se propagam sozinhas — por desenho.

A ponte tem mais duas secções que só tu podes preencher:

- **B — cenários a ensaiar.** O modelo não inventa cenários. Dizes que alturas
  de muro, que posições de árvore, que valores de parâmetro incerto.
- **C — a pergunta a responder primeiro.** Sem isto a sessão dispersa-se. E diz
  se basta horas de sol ou se precisas de valor radiométrico — determina a
  ferramenta.

---

## O muro rebaixável: o que disseste hoje muda o modelo

Disseste duas coisas que, juntas, abrem a melhor hipótese que apareceu neste
projecto:

1. O limite SW **não tem nada do lado de fora** — sem vizinhos, sem construção.
2. **A parte que tapa o jardim não tem função de suporte.** Só a parte abaixo
   do nível das terras retém; acima é guarda.

**Consequência:** a altura desse limite deixa de ser um dado do local e passa a
ser uma **variável de projecto**. Podes rebaixar, e o modelo passa a ter um
cenário para quantificar.

**Porque pode valer muito:** num recinto estreito e fundo, a altura dos limites
**domina o Inverno** — está registado que 0,50 m de diferença duplicou a média
de sol de Dezembro. O sol de Inverno vem de S/SW a cerca de 27° de altura, e é
precisamente esse o quadrante do limite que podes baixar. **A zona SW é hoje a
pior do jardim** (praticamente zero horas em Dezembro). Rebaixar abre o
quadrante de onde vem a luz que falta.

**A reserva, e é real: a palmeira está no caminho.** Fica entre esse limite e o
resto do jardim. O sol que entrar pelo rebaixamento atravessa a copa dela. A
copa é pinada e deixa passar luz salpicada, não sol directo — ajuda, mas não é
a mesma coisa.

**É exactamente para isto que o modelo serve.** Mandei a T003 reportar sempre
**com e sem a vegetação no caminho**, para cada cota de rebaixamento. Sem isso
podias rebaixar 1,5 m de muro e ganhar quase nada, ou ganhar muito — e a
diferença não se adivinha, calcula-se.

**Duas coisas que a T003 não decide:** se o rebaixamento é admissível
(estrutura, condomínio, privacidade, ruído) e onde exactamente está a fronteira
entre suporte e guarda. A primeira é do Arquitecto; a segunda é medição.

---

## Duas coisas que te dizem respeito, e não ao agente

### A altura dos muros é o número mais importante do projecto

Baixar de 3,00 para 2,50 m **duplicou** a média de sol de Dezembro no cálculo
que já existe. Enquanto esse valor for estimado, tudo o que o modelo disser
sobre o Inverno tem incerteza de 100% — e o Inverno é a estação que decide
a relva e a paleta de plantas.

**Uma fita métrica resolve isto em cinco minutos.** É a coisa de maior retorno
que podes fazer ao projecto, e não precisa de software nenhum.

### Podes montar o software antes de medir

Instalar e validar contra as fotos **não depende das medições**. A validação
geométrica testa se o modelo está bem montado, não se os números estão certos.
Faz sentido montar agora e medir em paralelo.

O que **não** deves fazer é tomar decisões com os números que ele devolver
enquanto a altura dos muros for estimativa.

---

## Sobre a ferramenta

A recomendação é **Python próprio** (`pvlib` + `shapely`), não Blender nem QGIS.
Razão: o quintal é geometricamente trivial — seis planos e três elipsóides —
e mover uma árvore passa a ser editar duas coordenadas. 4–10 h de montagem,
risco baixo.

O Blender com VI-Suite ganha se e quando quiseres o **mesmo modelo** a servir
a iluminação cénica nocturna. Aí as 15 h justificam-se pelo duplo uso. Hoje
ainda não há essa necessidade.

A ressalva honesta: o Python próprio dá **horas de sol directo** com rigor.
Não dá a luz difusa obstruída pelos muros nem a refletida, sem trabalho
considerável. Para escolher onde pôr uma árvore, horas de sol é a métrica
que decide. Se a pergunta mudar para "quanto DLI exactamente", muda a
ferramenta.

---

## Resumo do que tens de fazer

1. **Preencher `modelo/PONTE-DADOS.md`** quando o pacote da T001 estiver pronto
   — tabela A (onde está cada dado), B (cenários a ensaiar), C (pergunta a
   responder primeiro).
2. Abrir sessão nova, modo THREAD, escolher T003.
3. Responder ao que faltar.
4. Em paralelo, e independente de tudo: **medir a altura dos muros com fita** —
   e, no limite SW, **medir também até que cota retém terras**. Essa cota é o
   que define quanto podes rebaixar.
