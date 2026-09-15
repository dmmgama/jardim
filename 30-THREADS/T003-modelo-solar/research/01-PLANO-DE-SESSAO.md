---
created: 2026-09-15
project: Jardim
thread: T003
tipo: plano-de-execucao
---

# Plano da primeira sessão — T003

Lê isto depois de `thread.md` e `mensagens.md`. É a sequência de trabalho.

> **REGRA QUE GOVERNA ESTA THREAD:** não tens dados. Tens um contrato que diz
> **o que precisas**. Cada dado vem de o David te dizer onde está.
> **Não vais procurar ficheiros noutras pastas por iniciativa própria.**
> Não escrevas caminhos no código nem valores no código.

---

## Fase 0 — Antes de pedir nada (30 min)

**0.1** Lê `modelo/contrato-de-dados.yaml` de ponta a ponta. É a especificação
do que o modelo precisa e porquê. Não é um formulário a despachar: cada campo
tem `para_que` e `sensibilidade`, e isso determina a ordem em que perguntas.

**0.2** Lê `research/00-PACOTE-ARRANQUE.md` — as três vias de ferramenta
comparadas, com a recomendação e a sua justificação.

**0.3** Verifica o ambiente, porque condiciona a via:

```
python --version
python -c "import pvlib" 2>&1
python -c "import shapely" 2>&1
python -c "import yaml" 2>&1
```

`PyYAML` é preciso para ler os parâmetros. Já se sabe que **não estava
instalado** neste ambiente — confirma e instala se necessário.

**0.4** Decide a via **antes** de pedir dados, porque a via determina que
dados fazem falta. Se a decisão não for óbvia, pergunta ao David em vez de
assumir.

---

## Fase 1 — Levantamento de dados, com o David (1 sessão de conversa)

### 1.0 Começa por ler a ponte

**`modelo/PONTE-DADOS.md`** é onde o David declara **onde está cada bloco de
dados**, em que estado, e que versão. É o teu ponto de partida.

| Situação na ponte | O que fazes |
|---|---|
| Tabela A preenchida | Lês as fontes que ela indica e extrais os valores |
| Parcialmente preenchida | Usas o que há; perguntas o resto |
| Vazia | Fazes a entrevista completa e **preenches a ponte à medida que ele responde** |

A ponte tem também a **secção B (cenários a ensaiar)** e a **secção C (a
pergunta a responder primeiro)**. Sem a C, não sabes que ferramenta serve nem
onde parar.

**A secção D é tua:** escreves lá o que pediste e não obtiveste.

### Como conduzir

- **Um bloco de cada vez**, na ordem do contrato (localização → orientação →
  recinto → obstáculos → vegetação → zonas → validação → saída).
- Para cada campo `bloqueante`, pergunta explicitamente: **onde está este
  dado?** O David responde com um ficheiro, um valor, ou "não existe".
- Regista a resposta em `modelo/parametros-activos.yaml`, **incluindo o campo
  `origem:` com o que ele disse.**
- Se ele disser "não existe" ou "não foi medido": escreve em `lacunas:` e
  **continua**. Não bloqueies a sessão inteira por um campo.

### Perguntas que não podes deixar de fazer

Estas são as que decidem a qualidade do resultado:

1. **Altura dos obstáculos verticais, medida desde o solo do jardim.**
   O contrato assinala que há **conflito de fontes não resolvido** neste
   parâmetro e material gráfico produzido com valores diferentes.
   Pergunta: *qual é o valor vigente, já foi medido, e há material a corrigir?*
   **É o input mais sensível do modelo inteiro.**

2. **A convenção de eixos e a designação dos limites.**
   Há nomenclatura normativa estabelecida noutra thread. Pede-a em vez de
   inventares — é o que torna os teus outputs comparáveis com o resto do
   projecto.

3. **Quais exemplares de vegetação têm dimensões medidas e quais não.**
   Há notícia de exemplares nunca medidos. Esses correm-se **em intervalo**,
   não em valor único.

4. **Que exemplares o projecto obriga a manter.**
   Separa o fixo do móvel. Sem isto não sabes que cenários são legítimos.

5. **Folha persistente ou caduca, por exemplar.**
   Determina se precisas de **duas simulações por estação**.

6. **Existe uma tabela de horas de sol já calculada por outra via?**
   E — pergunta crítica — **inclui ou exclui a vegetação?** É a tua referência
   de validação, e se a comparares com o âmbito errado vais achar que tens um
   bug quando não tens.

7. **Que fotografias datadas existem, e cobrem geometrias de sombra
   diferentes?** Duas fotos com sombras opostas validam a geometria de graça.

8. **Qual a pergunta a responder primeiro**, e se basta horas de sol ou é
   preciso valor radiométrico. Determina a via e evita trabalho a mais.

9. **Que limites têm horizonte livre do lado de fora — e até que cota retêm
   terras?** Esta é a pergunta que abre o cenário de maior potencial do modelo,
   e foi levantada pelo David em 2026-09-15:

   > Um limite sem construção do lado de fora tem altura **rebaixável**. E num
   > muro que retém terras, só a parte **abaixo** do nível das terras tem função
   > de suporte — a parte acima é **guarda**, e essa pode em princípio baixar.

   Porque importa tanto: num recinto estreito e fundo, a altura dos limites
   **domina o Inverno**. Está registado que uma variação de 0,50 m na altura
   duplicou a média de sol de Dezembro. Rebaixar um limite no quadrante de onde
   vem o sol de Inverno é potencialmente o maior ganho disponível — maior do que
   qualquer escolha de planta.

   **Perguntar:** a que cota termina a parte que retém terras · quanto sobra
   acima · se está medido ou é observação · que alturas interessa ensaiar · que
   extensão do limite (tudo ou só um vão) · se o elemento substituto é vazado.

   **Cuidado obrigatório ao reportar:** se houver copa de vegetação entre o
   limite rebaixado e a zona a beneficiar, **o ganho real pode ser muito
   inferior ao geométrico**. Reporta sempre **com e sem** a vegetação no
   caminho — é a informação que decide se o rebaixamento vale a pena.

   **Fora do teu âmbito:** se o rebaixamento é admissível — estrutural, legal,
   condomínio, privacidade, ruído. Tu quantificas o ganho de luz. A decisão é
   do Arquitecto.

### Ao fim da Fase 1

Escreve em `mensagens.md` um resumo do que obtiveste e do que ficou em falta.
Se faltar algum `bloqueante`, **diz ao David que conclusões deixam de ser
possíveis** — não avances a fingir que tens tudo.

---

## Fase 2 — Montar o modelo (4–10 h, via Python)

**2.1 Estrutura.** Três módulos, e nenhum deles com valores lá dentro:

| Módulo | Responsabilidade |
|---|---|
| leitura | Carrega `parametros-activos.yaml`, valida presença dos bloqueantes, **falha com mensagem clara** se faltar algum |
| geometria | Constrói planos (limites) e sólidos (copas) a partir dos parâmetros |
| solar | Posição do Sol por instante; projecta sombras; agrega por zona |

**2.2 Invariante a respeitar em todo o código:**

> Se um parâmetro não está em `parametros-activos.yaml`, o código **não tem
> valor por omissão**. Levanta erro e nomeia o campo em falta.

É isto que impede o hardcoding de voltar a entrar pela porta do fundo.

**2.3 Cenários, não valores únicos.** Onde o contrato marcar `cenarios:`,
o modelo corre todos e apresenta o intervalo. A altura dos obstáculos vai
quase certamente cair aqui.

**2.4 Duas passagens para folha caduca.** Uma por época de folha, outra para
o período despido, com as datas que o David indicar.

---

## Fase 3 — Validar antes de acreditar (2 h)

**Não reportes um único número antes desta fase.**

**3.1 Validação geométrica contra as fotografias datadas.**
Para cada foto: calcula a posição solar naquele instante, gera o padrão de
sombra previsto, compara com o que a foto mostra. Regista a comparação numa
tabela — previsto contra observado.

**Critério de aceitação:** se houver fotos com geometrias opostas e o modelo
reproduzir a inversão, a geometria está correcta. Se não reproduzir, tens um
erro de azimute, de fuso horário, ou de altura de obstáculo — por essa ordem
de probabilidade.

**3.2 Validação contra a tabela de referência existente.**
Compara zona a zona. Atenção ao âmbito: se a referência **exclui** vegetação
e o teu modelo a **inclui**, os teus valores devem ser **iguais ou menores**,
nunca maiores. Um valor maior é sinal de erro, não de bom resultado.

**3.3 Sanidade nas horas de primeira luz.** Se houver horas de primeira luz
já calculadas, o teu modelo deve reproduzi-las. É um teste rápido e apanha
erros de fuso.

---

## Fase 4 — Responder à pergunta do mandato (a parte útil)

Só agora. Com o modelo validado:

**4.1** Corre o estado actual e produz a tabela de horas de sol por zona.
**4.2** Corre os cenários de posição que o David indicou, um a um.
**4.3** Produz o comparativo: que muda em cada zona, em cada estação.
**4.4** Diz o que o modelo **não** sabe — incerteza herdada dos parâmetros
estimados, e o que mudaria se fossem medidos.

Entrega em `entregue/` com nota explicativa, e propõe ao Arquitecto pelo canal
de mensagens.

---

## O que NÃO fazer

- **Não** ir procurar dados noutras pastas do repositório por iniciativa
  própria. Pede ao David.
- **Não** escrever caminhos de ficheiros no código. O caminho é argumento,
  configuração, ou pergunta.
- **Não** copiar valores de documentos de outras threads para dentro do
  código. Passam por `parametros-activos.yaml`, com origem declarada.
- **Não** preencher um parâmetro em falta com um valor plausível.
- **Não** reportar números antes da Fase 3.
- **Não** decidir que espécie plantar nem onde, por razões de projecto.
  O modelo diz o que acontece à sombra; a decisão do jardim é do Arquitecto.
- **Não** alargar o mandato. Se o trabalho mostrar que o mandato é
  insuficiente, escrever ao Arquitecto.

---

## Cuidados técnicos que custam horas

- **Fuso horário e hora de verão.** `pvlib` exige datetimes com timezone.
  Um datetime *naive* é interpretado como UTC e o erro passa despercebido
  até as sombras não baterem com as fotos.
- **Azimute.** Confirma a convenção (0=N, sentido horário) contra a fonte
  que o David indicar. Erro de sinal ou de referencial é o bug mais comum.
- **Altura medida desde onde.** Solo do jardim, não cota da rua, não solo
  exterior. Num recinto no topo de um desnível, confundir isto é fácil e é fatal.
- **Caminhos com espaços.** Este repositório tem espaços no caminho. Algumas
  ferramentas de linha de comandos falham silenciosamente; se usares
  fotogrametria, trabalha numa pasta sem espaços.
- **Resolução da grelha.** Num recinto pequeno podes ser fino sem custo.
  Não é aqui que está o problema — o problema é a qualidade dos inputs.

---

## Critério de sucesso desta primeira sessão

Não é ter o modelo completo. É:

1. `parametros-activos.yaml` preenchido com **origem declarada** em cada campo,
   e as lacunas escritas.
2. A via de ferramenta **decidida e justificada**.
3. O modelo a correr e a **reproduzir as fotografias datadas**.
4. `thread.md` com estado reescrito e handoff.

Se conseguires isto, a thread cumpriu o arranque. Os cenários de posição de
árvores são a sessão seguinte, e serão rápidos porque a infra-estrutura já
existe.
