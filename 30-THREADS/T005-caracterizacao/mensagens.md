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
