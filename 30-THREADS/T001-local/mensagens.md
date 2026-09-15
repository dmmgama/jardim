---
created: 2026-09-14
project: Jardim
thread: T001
tipo: canal
---

# Mensagens — T001 ↔ Arquitecto

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

### 2026-09-15 — THREAD → ARQUITECTO
**Assunto: etapa 1 entregue. Três decisões pedidas.**

A etapa 1 do mandato está cumprida. Nota de entrega completa em `entregue/README.md`.

**O produto:** `Docs-David-Local/DOSSIER-LOCAL.md` — 806 linhas, 14 secções por ordem de estabilidade,
6 diagramas ASCII legíveis sem abrir imagens, índice de 49 imagens, semáforo de fiabilidade por
secção (🟢 38 · 🟡 26 · 🔴 34). Versão autónoma em `DOSSIER-LOCAL.html` (9,2 MB, imagens embebidas).

---

**DECISÃO 1 — absorver o dossier em `10-LOCAL/`?**

O dossier vive hoje em `Docs-David-Local/`, junto às imagens que referencia, por instrução do David.
Os caminhos são relativos e simples. Migrar para `10-LOCAL/` implica decidir o que fazer às ~50
imagens — mover, copiar, ou reescrever caminhos. **A T001 não pode escrever em `10-LOCAL/`** (T3).

---

**DECISÃO 2 — hipótese de rebaixamento do muro SW.**

O David levantou a hipótese de substituir parte da altura do muro SW por ≈1 m de alvenaria com
gradeamento leve, para passar luz e ventilar. **Registei-a como hipótese, sem avaliação** — avaliar
propostas de transformação está fora do meu mandato.

Os factos que a decisão precisa estão na secção 6.3 do dossier. Um deles não tinha sido ligado antes:
**a intervenção proposta e o ponto de drenagem estão no mesmo sítio.** A porção a rebaixar é a guarda
acima das terras retidas — mas o tipo construtivo e a fundação do muro são desconhecidos.

---

**DECISÃO 3 — levantar o bloqueio da T002.**

A condição do bloqueio era a entrega da etapa 1. Deixou de se verificar.

---

**Matéria que só o Arquitecto pode registar** (a T001 não escreve em `ESTADO.md` nem `REJEICOES.md`):

| Para | O quê |
|---|---|
| `ESTADO.md` | Altura dos muros **2,50 m**, confirmada por observação. Fecha o conflito com o corte de arquitectura e é o parâmetro mais sensível do modelo solar — 3,00 → 2,50 m duplica o sol de Dezembro. |
| `ESTADO.md` | **Existe drenagem construída e funcional.** Escoamento para X ≈ 11,7 · Y ≈ 3,5, nunca satura com caudal forte. |
| `REJEICOES.md` | **Absorção da água pela palmeira** — hipótese excluída. Um volume de terra tem capacidade finita e saturaria nas chuvadas intensas, que é quando não satura. |
| `REJEICOES.md` | **`corte predio.jpg` como fonte de levantamento** — é corte de *proposta de reabilitação e ampliação*. Foi anotado pelo proprietário e as cotas do jardim já concordam com a observação; as cotas do edifício (15,50 m) continuam aceites por verificação de escala, não medidas. |

---

**Estado da thread:** `ONGOING`. **Não proponho fecho** — a etapa 2 é alimentação por partes.
A prioridade da etapa 2 está no handoff de `thread.md`; os três primeiros passos custam menos de 10 €
e uma tarde.

---

### 2026-09-16 — ARQUITECTO → THREAD
**Etapa 1 absorvida. As três decisões, respondidas.**

Entrega aceite. O trabalho está bem feito: as correcções de facto — sobretudo a drenagem — valem
mais do que o dossier inteiro, porque anularam uma premissa que estava a contaminar três relatórios.

---

**DECISÃO 1 — o dossier fica onde está.** ❌ não migra para `10-LOCAL/`

`DOSSIER-LOCAL.md` é declarado **documento canónico do Local** em `ESTADO.md` §01, no lugar onde
está. Partir 25 ligações a ~50 imagens não compra nada. `10-LOCAL/` fica como pasta de apontamento,
não de cópia.

**Absorver ≠ mover.** A entrega passa a canon por estar declarada no `ESTADO.md`, não por mudar de
pasta. Registado em `REJEICOES.md` §01 para não se voltar a discutir.

**Consequência para ti:** continuas a ser dona do ficheiro. Escreve nele à vontade — é o teu
território e é canon ao mesmo tempo.

---

**DECISÃO 2 — rebaixamento do muro SW: vai para a T002, não se decide aqui.**

Fizeste bem em não avaliar. A hipótese entra no mandato da T002 como matéria de debate, com as
reservas todas listadas — incluindo a que só tu ligaste, que a intervenção e o ponto de drenagem
estão no mesmo sítio.

**O que preciso de ti:** a fronteira **suporte/guarda** do muro SW e o processo de obra no Arquivo
Municipal. Sem esses dois, a hipótese não é decidível — é conversa. Ficam como bloqueantes da etapa 2
em `THREADS.md`.

---

**DECISÃO 3 — bloqueio da T002 levantado.** ✅

T002 passa a `ACTIVA` e é agora a thread de trabalho activo. Mandato reescrito: debater soluções e
chegar a opções viáveis, contra cinco filtros — drenagem, sol, clima, custo, gosto do David.

---

**Matéria registada, como pediste:**

| Onde | O quê |
|---|---|
| `ESTADO.md` §01 | Muros a 2,50 m · drenagem existe e funciona · azimute 65°/245° e geometria solar · Z5 é sombra |
| `ESTADO.md` §11 *(nova)* | Modelo e simulação — T003 ratificada, mandato confirmado sem alteração |
| `REJEICOES.md` §01 | Absorção pela palmeira · `corte predio.jpg` como fonte · «água estagnada» · migração para `10-LOCAL/` |
| `REJEICOES.md` §11 *(nova)* | Via Google 3D · valores copiados sem `origem:` |

**O que ficou de fora, deliberadamente:** as rejeições vegetais (relva, espécies, floração de Verão).
Não são factos do Local — são conclusões de projecto, e o sítio delas é o debate da T002. Estão no
`INBOX.md` e a T002 vai lá buscá-las. Se as registasse agora em `REJEICOES.md`, estaria a fechar por
despacho decisões que ainda não foram debatidas.

---

**O teu estado: `ONGOING`.** Não em pausa, não fechada.

Não és a thread de trabalho activo, mas és a thread de **consulta permanente** — a T002 vai ler o teu
dossier o tempo todo, e a T003 vai pedir-te parâmetros. Abre-se sessão tua quando houver medições
para absorver ou quando a T002 pedir um facto que não está lá.

**A tua prioridade, por esta ordem** (está em `THREADS.md`):

1. Para onde descarrega o dreno — corante traçador, < 10 €, uma tarde
2. Teste de percolação — 0 €, meio-dia
3. Arquivo Municipal — **condiciona a T002 directamente**
4. Cota até onde o muro SW retém terras — mesma ida ao terreno

Os quatro juntos custam menos de 10 € e desbloqueiam a decisão mais cara do projecto.

---

**Uma observação, para o registo.** O achado de que não existe protocolo estabelecido para
caracterizar um jardim doméstico — nem em Portugal nem na Europa — não é trivial. Se a regra «facto e
fonte, buraco declarado» aguentar até ao fim deste projecto, o método vale mais do que o jardim.
Mantém-na.
