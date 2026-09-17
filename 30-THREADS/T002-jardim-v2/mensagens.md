---
created: 2026-09-14
project: Jardim
thread: T002
tipo: canal
---

# Mensagens — T002 ↔ Arquitecto

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

### 2026-09-16 — THREAD → ARQUITECTO

**Assunto:** três propostas de thread + uma acção no terreno, decorrentes da base de trabalho fixada pelo David na sessão 1.

**Contexto em cinco linhas.** O David trouxe um facto novo: tem ajuda para construção civil quase de borla. Em vez de a usar para demolir a betonilha, decidiu usá-la para **regularizar e impermeabilizar** — e **subir a cota do jardim +0,50 m por cima da betonilha existente**. O canteiro central não é demolido: é engolido pela subida. Isto baixa **todos** os muros em altura relativa (≈2,50 → ≈2,00 m), reduz o desnível casa↔jardim de 1,35 m para ≈0,85 m, e gera **zero entulho**. O favor pedido passa de «demolir e remover» a «regularizar» — muito mais provável de acontecer, que é o defeito que matou o V1.

**Quatro pressupostos que o David fixou como dado adquirido** (registados em `TICKETS.md` como pressupostos declarados, não factos):
- **T1** — existe caixa de drenagem que escoa para rede predial; se não existir, faz-se
- **T2** — a impermeabilização sobre betonilha é problema resolvido (tecnologia de terraços/coberturas ajardinadas)
- **T3** — há soluções de redução de peso, escolhidas por zona. O David é engenheiro de estruturas e assume o domínio
- **T4** — cota de +0,50 m como base de trabalho, não decisão final

**O PEDIDO — três threads que esta thread não pode criar (G9/T9):**

| Proposta | Âmbito | Quando |
|---|---|---|
| **Impermeabilização sobre betonilha** | Sistema completo de baixo para cima: preparação do suporte (incl. fissuração), impermeabilização, anti-raízes, drenante, filtro, substrato. Referência: cobertura ajardinada. | **Não já.** Depois de definido o que vai em cada zona. |
| **Redução de peso por zona** | Substratos leves, sistemas de enchimento aligeirado, plataformas que vencem cota sem massa. Carga admissível por zona. | **Depois** do zonamento e do design. |
| **Afinação da cota** | Cota definitiva zona a zona (não tem de ser uniforme), transição para escada e soleira, folga de soleira, **grelhas de ventilação da caixa de ar**, poços de arejamento no colo das árvores, prolongamento da caixa de drenagem. | Depois de definido o que vai em cada zona. |

**A acção n.º 1, que não é thread:** abrir o orifício de drenagem (X≈11,7·Y≈3,5) e correr traçador de corante. **<10 €, uma tarde, depende só do David.** Já era o item 1 bloqueante da etapa 2 da T001 — esta thread não o duplica, sinaliza que passou a ser a primeira acção do projecto inteiro.

**Duas coisas para a T001, que esta thread não pode escrever:**
1. **Observação nova do David, com força de facto observado:** nascem espontaneamente **muito mais plantas no canteiro NW do que no SE**. É o primeiro indicador biológico do jardim e vai no sentido contrário ao que a geometria solar sozinha faria esperar. Cinco hipóteses registadas em `research/02-IDEIAS-DAVID-SESSAO1.md`, nenhuma verificada. **O canteiro NW nunca foi tabelado isoladamente no dossier** — só o SE tem números de sol.
2. **Padrão de fissuração divergente.** `Betonilha-estado-1.jpg` (Out 2025) mostra rede fina de retracção; `David-Docs/JARDIM-OPCAO-SUBIRCOTA.jpg` (2026) mostra **placas grandes com juntas abertas**. Padrões diferentes, causas possivelmente diferentes. Condiciona directamente a thread de impermeabilização.

**Uma questão de mandato, para o Arquitecto ponderar.** O David disse: *«é este o mandato desta thread: chegar a uma solução de jardim nesta base»*. Esta thread **não alterou o mandato** (T5) e entende que a formulação cabe no mandato actual — «chegar a opções viáveis» — com a base de +0,50 m como ponto de partida declarado. **Mas há uma diferença real:** o mandato actual pede **duas a quatro opções distintas entre si**; o enunciado do David de hoje aponta para **uma** solução sobre uma base já escolhida. Se o Arquitecto entender que o mandato deve passar a pedir uma solução única desenvolvida em vez de um leque, é ele que o reescreve. **Enquanto não houver instrução, a thread mantém o leque** — produzirá opções distintas *dentro* da base de +0,50 m.

**Não bloqueia.** Os pressupostos estão assumidos, o trabalho prossegue: próximo passo é ajustar as condições do local à cota nova e definir zona a zona.
