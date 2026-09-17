---
created: 2026-09-17
thread: T005
tipo: analise
summary: |
  Análise da estrutura de informação que o projecto já tem, feita antes de as
  pesquisas chegarem. Estabelece o problema que a T005 existe para resolver:
  o dossier está organizado por objecto físico, não por disciplina, e por isso
  não consegue responder à pergunta "isto está caracterizado?".
---

# Ponto de partida — o que o projecto já tem, e porque não chega

> **Nota de método.** Escrito **antes** de as três pesquisas chegarem, de propósito.
> Se escrevesse depois, arriscava-me a descrever o problema com o vocabulário das
> respostas — e deixaria de ser possível ver se as pesquisas respondem à pergunta
> certa. Isto é o diagnóstico a partir do material existente.

---

## 1. O que existe

**O `DOSSIER-LOCAL.md` é bom.** 827 linhas, 14 secções, semáforo de fiabilidade por
afirmação (🟢 38 · 🟡 26 · 🔴 34), 49 imagens fichadas, 6 diagramas ASCII, uma secção
de contradições com balanço explícito. **Não é o problema desta thread.** É
provavelmente a melhor peça de documentação do projecto.

**A sua estrutura:**

| § | Secção | Organizada por |
|---|---|---|
| 1 | Dados gerais | — |
| 2 | Geometria | **objecto** |
| 3 | Envolvente e implantação | **objecto** |
| 4 | Estruturas | **objecto** |
| 5 | Exposição solar | **fenómeno** |
| 6 | Água | **fenómeno** |
| 7 | Superfícies | **objecto** |
| 8 | Vegetação | **objecto** |
| 9 | Infra-estrutura | **objecto** |
| 10 | Secções por instruir | **lacuna** |
| 11 | Índice de imagens | fonte |
| 12 | Por inspeccionar | **lacuna** |
| 13 | Contradições | **higiene** |

---

## 2. O diagnóstico

**A organização é por objecto físico e por fenómeno — "o que está lá" e "o que lhe
acontece".** É a organização natural de quem levantou o espaço a olhar para ele, e
funciona muito bem para *descrever*.

**Falha noutra coisa: não sabe dizer quando pode parar.**

O dossier tem duas listas de lacunas — §10 (doze secções por instruir) e §12 (por
inspeccionar, em três prioridades). São ambas listas de **coisas que faltam**,
ordenadas por consequência percebida. Nenhuma delas responde a:

- **Quem diz que estes são os parâmetros que faltam?** A lista foi construída por
  observação do que não estava documentado — não por confronto com o que uma
  disciplina exige. **Um parâmetro que ninguém se lembrou de procurar não aparece
  em lista nenhuma de lacunas.** É o ponto cego estrutural do método actual.
- **Com que exactidão é que cada um chega?** O dossier tem 🟢🟡🔴, que é fiabilidade
  da *fonte*, não tolerância do *valor*. «Muros a 2,50 m 🟢 [observado]» não diz se
  ±5 cm chega. Para decidir plantação chega; **para dimensionar drenagem sobre laje,
  não sei, e o dossier também não sabe que não sabe.**
- **Caracterizado para quê?** O mesmo parâmetro serve decisões com exigências
  diferentes. Não há um critério de suficiência declarado em lado nenhum.

---

## 3. A prova de que isto não é teórico

**Três exemplos, todos do material existente.**

### 3.1 O jardim sobre laje não tem secção nenhuma

Decidiu-se em 2026-09-17 que o jardim sobe **+0,50 m sobre a betonilha
impermeabilizada.** Tecnicamente, isso deixa de ser um jardim de terreno e passa a
ser **muito próximo de uma cobertura verde** — que é uma coisa com literatura,
normas e modos de falha próprios.

**O dossier não tem uma secção de cobertura verde**, porque quando foi escrito o
jardim ainda era de chão. **E não vai passar a ter por observação**, porque não há
nada no espaço para observar: a coisa ainda não existe. Só aparece se alguém
perguntar *«que disciplina trata disto, e o que é que ela exige saber?»*

**É exactamente o mandato da T005**, e é o melhor argumento a favor da thread.

### 3.2 O DLI está listado como lacuna, mas não como critério

S2 pede «DLI medido... 60–200 €/sensor, 2–4 semanas por estação». Correcto e útil.

**Mas o DLI não é um facto a coleccionar — é o número que decide que planta vive em
cada zona.** A diferença entre listá-lo como lacuna e usá-lo como critério é a
diferença entre um inventário e uma regra. Uma lista de lacunas não diz **que valor
de DLI é suficiente para quê**, e é isso que faz falta.

### 3.3 A secção 10 chama-se "por instruir" e tem doze temas

Solo · DLI · microclima · vento · cargas · acessos · privacidade · ruído ·
condomínio · coroa dos muros · muro NW · orifício de drenagem.

**Repara na composição da lista.** Estão lá coisas de disciplinas completamente
diferentes — agronomia, luminotecnia, climatologia, acústica, direito da propriedade
horizontal, geotecnia — **todas ao mesmo nível, na mesma tabela, ordenadas por
esforço de obtenção.**

Isso torna-as comparáveis pelo custo, o que é útil para planear uma tarde de
trabalho. **E torna-as incomparáveis por tudo o resto** — porque «ruído» e «cargas
do muro SW» não são o mesmo tipo de coisa, não falham da mesma maneira, e não
bloqueiam as mesmas decisões.

---

## 4. O que a T005 tem de produzir para valer a pena

Não é mais informação. **É uma grelha que transforme "o que falta" em "o que falta,
para quê, com que tolerância, e como sei que cheguei lá".**

A forma provável — a confirmar contra as três pesquisas:

| Campo | O que responde |
|---|---|
| **Parâmetro** | O quê |
| **Disciplina** | Quem o reclama |
| **Para que decisão serve** | **O campo mais importante.** Um parâmetro sem decisão associada não se mede. |
| **Método** | Como se obtém |
| **Tolerância exigida** | Quanto erro a decisão aguenta |
| **Critério de suficiência** | Como sei que parei |
| **Estado actual** | O que já existe, com a etiqueta do dossier |
| **Custo de obter** | Para priorizar |

**O teste que esta grelha tem de passar:** aplicada ao material existente, **tem de
fazer aparecer pelo menos um parâmetro que nenhuma das duas listas de lacunas do
dossier contém.** Se não fizer aparecer nada de novo, a T005 produziu formatação e
o Arquitecto deve dizê-lo.

---

## 5. O risco desta thread, repetido de propósito

**Produzir uma enciclopédia em vez de uma regra.** O quintal tem ~75 m². As três
pesquisas vão devolver muito material — especialidades, software, sensores — e a
tentação é catalogar tudo.

**O contrapeso:** este projecto tem quatro planos mortos e uma obra a começar. O que
sobrevive é o que é curto e accionável. **Uma grelha de trinta parâmetros que ninguém
preenche vale menos que uma de oito que se preenche numa tarde.**
