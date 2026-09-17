---
created: 2026-09-15
project: Jardim
thread: T003
tipo: canal
---

# Mensagens — T003 ↔ Arquitecto

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

*(sem mensagens)*

---

### 2026-09-17 — ARQUITECTO → THREAD
**Arranque. Pedido encaminhado da T002, mais um alargamento de âmbito.**

Esta é a primeira mensagem que recebes. Lê-a inteira antes de abrir qualquer outro ficheiro.

---

## 1. O que mudou no projecto desde que foste criada

Foste criada a 2026-09-15 e nunca correste. Nesse intervalo o projecto **mudou de natureza**, e isso
muda o que se espera de ti.

| Data | O que aconteceu |
|---|---|
| 2026-09-16 | Etapa 1 da T001 absorvida. O dossier do Local é canon. Tu foste ratificada, mandato confirmado sem alteração. |
| 2026-09-17 | **A T002 fechou.** O projecto deixou de ser «arranjar o jardim» e passou a ser **fazer o jardim entrar na sala** — a marquise sai, entra envidraçado total. |
| 2026-09-17 | **Abriu a T004 — Geometria**, em urgência. Há ajuda de construção civil **disponível agora** e a plataforma vai avançar. |

**Consequência para ti:** deixaste de ser uma ferramenta de curiosidade e passaste a ter **dois
clientes com perguntas concretas** — a T004, que está no caminho crítico da obra, e o Arquitecto,
que tem de decidir o rebaixamento do muro SW.

**A base de projecto mudou e os teus parâmetros também.** O pavimento vai subir ≈0,50 m. Isso baixa
todos os muros em 0,50 m relativos, e é exactamente o tipo de pergunta para que existes.

---

## 2. O pedido de quantificação — encaminhado

O enunciado técnico completo está em `../T002-jardim-v2/research/03-PEDIDO-T003-COTA.md`.
**Lê-o na íntegra.** São cinco pedidos com prioridade declarada.

**Duas alterações minhas ao pedido, como Arquitecto:**

| Alteração | O quê |
|---|---|
| **O pedido 5 sobe a DECISIVO** | Estava como «só se a palmeira já estiver modelada, não atrasar os outros». **Passa a obrigatório.** Razão: a palmeira está entre o muro SW e o resto do jardim. Sem ela modelada, o pedido 4 responde à pergunta errada — dá «quanto sol entraria» quando a pergunta real é «quanto sol chega ao chão depois de atravessar a copa». A diferença entre sol directo e luz salpicada decide se o rebaixamento do muro vale a obra. |
| **O pedido 1 ganha uma alínea** | Além da área da mancha de sol, dá **a forma e a posição**. 23 m² concentrados num rectângulo utilizável não é a mesma coisa que 23 m² espalhados em manchas de 2 m². A T004 precisa de saber **onde** pôr as coisas, não só quanto espaço há. |

---

## 3. Âmbito novo — captura 3D com telemóvel

**Instrução do David, 2026-09-17.** Queres dados e eles não existem. Esta é a via para os obter.

Passa a caber-te **avaliar e recomendar uma ferramenta de captura 3D operável com telemóvel** —
nuvem de pontos ou equivalente — que produza a geometria de que precisas.

**Isto é alargamento do mandato, não substituição.** Continuas a ser a thread do modelo paramétrico.
A captura é **um meio de alimentar o modelo**, e entra no teu âmbito porque és tu que sabes de que
geometria precisas e com que tolerância.

### O que a captura tem de resolver

Por ordem de valor, não de facilidade:

| # | Alvo | Porque importa | Estado hoje |
|---|---|---|---|
| **1** | **Copa da palmeira** — diâmetro da projecção no solo e altura da base das palmas | **Bloqueia a T004**, que está no caminho crítico da obra. É item 🔴 P2.2 do dossier e nunca foi medido. | Desconhecido |
| **2** | **Altura dos muros, troço a troço** | O parâmetro mais sensível de todo o projecto. 3,00 → 2,50 m **duplicou** a média de sol de Dezembro. E há suspeita nova de que **não têm todos a mesma altura**. | 2,50 m `[observado]`, sem detalhe por troço |
| **3** | **Lodão e citrinheira** — porte e copa | Entram no modelo como obstáculos móveis. | Não medidos |
| **4** | **Cota até onde o muro SW retém terras** | Fronteira suporte/guarda. Define quanto se pode rebaixar sem tocar em estrutura. | Desconhecido |

### As dificuldades reais, para não seres optimista

- **Os muros são o pior caso possível para fotogrametria:** reboco liso, sem textura, em sombra
  permanente sob uma fachada de 15,50 m. A via Google 3D já foi rejeitada por não os resolver
  (`REJEICOES.md` §11).
- **Vegetação é historicamente o ponto fraco** de qualquer reconstrução — folhagem fina, movimento
  com o vento, oclusão.
- **Escala.** Uma nuvem de pontos sem referência de dimensão conhecida dá geometria relativa, não
  cotas. Diz explicitamente como resolves isto.

### O que quero de ti sobre este ponto

1. **Uma recomendação, não um levantamento.** Já existe levantamento de software em
   `../T001-local/research/Jardim_Software_Modelacao_Solar.md`. Não o repitas.
2. **Um procedimento de campo que o David execute sozinho numa tarde** — quantas fotos, de onde,
   que referência de escala, que ordem.
3. **A honestidade de dizer onde a fita métrica ganha.** Se a altura dos muros se resolve melhor com
   um telémetro laser de 30 €, **diz isso e não recomendes a app.** O objectivo é ter o número
   certo, não usar tecnologia.
4. **O que fazer se o telemóvel não tiver LiDAR.** Não assumas hardware que não sabes que existe —
   **pergunta ao David que telemóvel tem** antes de recomendar.

Lancei uma pesquisa sobre o estado da arte em 2026. Anexo-a à tua pasta quando chegar — não faças a
mesma pesquisa outra vez.

---

## 4. Como quero que corras esta sessão

**Em paralelo com as outras threads**, por instrução do David. Não bloqueias ninguém e ninguém te
bloqueia.

**A ordem que recomendo:**

1. **Primeiro o que não precisa de dados novos.** Os pedidos 1–4 do documento da T002 correm com a
   geometria que o dossier já dá — muros, recinto, fachada, cotas. **Não esperes pela palmeira para
   entregar isso.**
2. **Depois a captura.** Recomendação + procedimento de campo, para o David executar.
3. **Por fim o pedido 5**, quando a copa estiver medida.

**Se o passo 1 for trabalho de minutos depois do modelo montado — como a T002 supôs — diz-me e
entrega já.**

---

## 5. Duas regras que continuam a valer

**A tua regra de proveniência mantém-se intacta.** Não copias valores, não escreves caminhos.
Declaras o que precisas, o David indica a origem, escreves em `parametros-activos.yaml` com
`origem:` preenchida. Está registada em `REJEICOES.md` §11 e não é negociável — nem por mim.

**A `PONTE-DADOS.md` já está preenchida.** A fonte é a entrega da etapa 1 da T001. Vais lá buscar os
parâmetros e transcreves o semáforo: 🟡 **não serve para dimensionar**, 🔴 corre em cenários ou fica
declarado como lacuna.

---

## 6. Um aviso

Os números de sol que a T002 usou para fechar o debate do jardim **são estimativa dela, não tua.**
Estão registados com etiqueta. Quando correres o modelo a sério, **é possível que não batam certo.**

Se não baterem, **diz-o alto.** Não ajustes o modelo para reproduzir o que já está escrito — há
decisões tomadas em cima desses números e o valor de existires é precisamente poderes contrariá-los.
