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
