---
created: 2026-09-16
project: Jardim
thread: T002
tipo: zonamento de trabalho
estado: SUBSTITUÍDO por 07-ZONAMENTO-DAVID.md (2026-09-17) — histórico
---


> # ⛔ SUBSTITUÍDO — HISTÓRICO
>
> **Este zonamento foi substituído por `07-ZONAMENTO-DAVID.md` em 2026-09-17.**
>
> O David trouxe o zonamento dele (seis zonas, `David-Docs/ZONAMENTO-PLANTA-ZONAS.jpg`) e a thread
> adoptou-o. **O ticket 2 da sessão 2 — validar o zonamento — fica resolvido por essa via.**
>
> Mantém-se aqui por duas razões: o raciocínio sobre as geometrias divergentes (drenagem em funil,
> humidade em perímetro, ventilação em secção, sol em faixas) continua válido, e a correcção de
> sequência «A·B·C avançam, D suspende-se» sobrevive na separação zona 4 / zona 5.
>
> **Não usar como grelha de trabalho.**

---

# ZONAMENTO DE INTERVENÇÃO — pressuposto de trabalho

> **Estatuto:** o David autorizou avançar com este zonamento **como pressuposto**, ficando a
> validação como **ticket n.º 2 da sessão 2**. `[David, 2026-09-16]`
>
> **P4** — este recorte é instrumento de trabalho, não decisão de projecto. Se se revelar errado,
> muda-se sem custo: nada do que se decidir fica preso à grelha.

---

## Porque não se usam as zonas Z1–Z5 herdadas

Z1–Z5 foram construídas para indexar **exposição solar** — é isso que o catálogo vegetal da T001
usa. Continuam válidas para isso e **não são substituídas**: convivem.

Mas o trabalho desta thread é endereçar **drenagem, ventilação, sombra e humidade**, e esses quatro
campos têm geometrias diferentes:

| Campo | Geometria própria |
|---|---|
| **Drenagem** | **Funil.** Oito trajectos convergem para um ponto junto ao muro SW. |
| **Humidade dos muros** | **Perímetro.** É de muro, não de chão. |
| **Ventilação** | **Secção.** O quintal é um corredor único fechado; não tem partes. |
| **Sol** | **Faixas em X.** É o que Z1–Z5 já sabe. |

**Um único zonamento para os quatro mente em três deles.** Daí a estrutura mista: quatro faixas,
dois perímetros, uma secção.

---

## As quatro faixas em X

O eixo X manda, porque é simultaneamente o eixo do escoamento, o eixo do sol da tarde e o eixo da
profundidade.

```
 X=0        X=2,49              X=6,70            X=10,38    X=13,00
 │            │                   │                  │          │
E├────────────┼───────────────────┼──────────────────┼──────────┤S   Y=5,78
 │            │                   │                  │          │    ▲ MURO SE ─── P-SE
 │            │                   │                  │          │    │
 │     A      │        B          │        C         │    D     │    │
 │  SOLEIRA   │   PLATAFORMA      │    CANTEIRO      │ CABECEIRA│    │
 │   ≈14 m²   │     ≈24 m²        │     ≈21 m²       │    SW    │    │
 │            │                   │                  │  ≈15 m²  │    │
 │  ⌂ porta   │                   │   ⊕ citrinheira  │ ✻ palm.  │    │
 │  ♣ lodão   │                   │                  │   ◉ dreno│    │
N└────────────┴───────────────────┴──────────────────┴──────────┘W   Y=0
                              MURO NW ─── P-NW

         ══════════ camada AR — o corredor inteiro ══════════
```

| Zona | X | Área | O que a define | Sol hoje (Dez / Eq. / Jun) |
|---|---|---|---|---|
| **A — Soleira** | 0 → 2,49 | ≈14 m² | Entrada, escada de 7 degraus, lodão no canto N, a única infra-estrutura eléctrica conhecida, as duas grelhas de ventilação da caixa de ar. **Cabeceira do escoamento.** | 1,7 / 5,0 / 5,2 h |
| **B — Plataforma** | 2,49 → 6,70 | ≈24 m² | A única superfície livre e contínua. Betonilha fissurada. **Onde se está.** Sem árvore, sem dreno, sem patologia. | 1,5 / 5,2 / 5,9 h |
| **C — Canteiro** | 6,70 → 10,38 | ≈21 m² | Citrinheira + canteiro linear SE. **Já é terra.** O melhor Verão do jardim. | 0,2 / 4,8 / 7,3 h |
| **D — Cabeceira SW** | 10,38 → 13,00 | ≈15 m² | Palmeira, saibro, **o dreno**, o muro de suporte. Restrição de carga. | 0,1 / 2,1 / 4,2 h |

Valores de sol: `DOSSIER-LOCAL.md` §5.4, modelo **sem árvores**, cota actual.
As áreas são aproximadas e derivam das faixas em X; não substituem as áreas cotadas do §7.3.

---

## As três camadas transversais

Não são faixas e não se somam às áreas. Atravessam o jardim todo.

| Camada | Extensão | O problema | Estado |
|---|---|---|---|
| **P-SE** | Muro SE, Y = 5,78, 13 m | Escorrências verticais, colonização biológica, reboco degradado e destacado. **O pior elemento construído do quintal.** Origem da água 🔴. | 🔴 |
| **P-NW** | Muro NW, Y = 0, 13 m | Escorrência verde na base. **Nunca fotografado de frente.** Aparentemente melhor que o SE. | 🟡 |
| **AR** | Todo o recinto | Corredor fechado: 5,78 m de largura contra 2,50 m de muro em três lados e 15,50 m de fachada no quarto. **Ventilação nunca caracterizada** — secção S3 por instruir na T001. | 🔴 sem dados |

**Sobre a camada AR — aviso de método.** Não há **nenhuma** medição de vento, temperatura ou
humidade neste quintal. Tudo o que se disser sobre ventilação é **inferência a partir da geometria**,
e será sempre etiquetado como tal. A T002 não converte inferência em facto.

---

## O que este recorte arruma imediatamente

| Constatação | Consequência |
|---|---|
| **D concentra quase todo o risco** | Dreno + muro de suporte + palmeira + restrição de carga + a pior luz do ano. **É a zona onde não se toca antes do traçador.** |
| **B é a zona de liberdade total** | Sem árvore, sem dreno, sem patologia, luz média do jardim. É onde a obra é barata e segura. |
| **C já é terra** | Recebe vegetação sem precisar de demolição. Melhor relação verde/obra do jardim. |
| **A é a zona de interface** | O que se fizer aqui condiciona a casa: escada, soleira, e as grelhas de ventilação. **Não é zona de jardim — é zona de ligação.** |
| **P-SE não é assunto de jardim** | É patologia de construção. Tem de ser resolvida antes de plantar encostado, senão planta-se contra uma parede que vai ter de ser picada. |

---

## A correcção de sequência que este recorte permite

O David propôs: **primeiro as questões estruturais, depois vegetação e pavimento.** O princípio está
certo — mas aplicado literalmente tem uma armadilha.

**Em D, a solução estrutural não é decidível hoje.** Faltam o traçador, o Arquivo Municipal e a
fronteira suporte/guarda. Se a sequência for estrita, **D bloqueia e arrasta tudo** — que é
exactamente o defeito que matou o V1: nada podia acontecer antes de uma coisa que dependia de
terceiros.

**A correcção:**

```
   A · B · C  ────────────►  avançam em paralelo, sem esperar por D
                             (nenhuma depende de dado que falte)

   D          ────░░░░░░──►  suspenso declarado
                             desbloqueia com: traçador · Arquivo Municipal ·
                             fronteira suporte/guarda
```

**D não é adiado — é declarado suspenso, com caminho de desbloqueio escrito.** A diferença entre
adiar e suspender com caminho é a diferença entre o V1 e isto.

---

## Ticket n.º 2 da sessão 2 — validar com o David

| Pergunta | Porquê importa |
|---|---|
| As quatro faixas correspondem a como pensas o espaço? | Se não corresponderem, a grelha atrapalha em vez de ajudar. |
| A fronteira B/C em X = 6,70 faz sentido, se o canteiro central vai ser engolido pela cota? | **A mais provável de precisar de ajuste.** Com o canteiro engolido, B e C podem tornar-se uma só zona. |
| A zona A deve ser tratada como jardim ou como interface da casa? | Muda tudo o que lá se propõe. |
| Falta alguma zona? | Ex.: o vão sob o lanço da escada, hoje não tratado por ninguém. |
