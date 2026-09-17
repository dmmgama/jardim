---
created: 2026-09-18
project: Jardim
tipo: governo
lingua: pt-PT
summary: |
  Instruções de preenchimento do REGISTO-DOCUMENTOS.md: estrutura, colunas, vocabulário
  fechado de Tipos, mecânica dos índices em Obsidian, resolução do problema do campo
  «Supported», casos difíceis e regras de higiene.
aplica-se-a: REGISTO-DOCUMENTOS.md
template: REGISTO-DOCUMENTOS-TEMPLATE.md
---

# REGISTO DE DOCUMENTOS — INSTRUÇÕES

> **Este ficheiro não é o registo.** É o manual do registo. O registo é
> `REGISTO-DOCUMENTOS.md`; o esqueleto vazio é `REGISTO-DOCUMENTOS-TEMPLATE.md`.
> Governo aplicável: `CLAUDE.md` §5.7 (G23–G36) e `30-THREADS/_TEMPLATE/CLAUDE.md` (T18–T23).

---

## 1. O que é e porque existe

O `REGISTO-DOCUMENTOS.md` é o **catálogo único de tudo o que este projecto produziu em
forma de documento** — tenha ido ou não para o NotebookLM, tenha saído de uma sessão de
Arquitecto, de uma thread, ou do próprio David.

**O problema que resolve.** O projecto gera documentos em cinco sítios diferentes
(`30-THREADS/TNNN/research/`, `.../reports/`, `.../entregue/`, `40-PESQUISAS/David/`, raiz)
e por três actores que não se lêem uns aos outros: as threads são territoriais por desenho,
o Arquitecto não abre a pasta das threads por rotina, e o David faz pesquisa fora do ciclo
de sessões. Sem catálogo, ninguém sabe o que existe.

**O custo demonstrado.** A 2026-09-17 descobriu-se que uma pesquisa do David respondia à
questão que a T005 tinha acabado de sinalizar como urgente à T004, e esteve disponível
durante toda a fase 1 sem ninguém a abrir. **O custo de não catalogar não é desarrumação:
é trabalho repetido e decisões tomadas sem informação que já existia.**

**O que este ficheiro NÃO é:**

- Não é `ESTADO.md`. Registar um documento **não decide nada** (G22/G31).
- Não é índice de decisões. É índice de **artefactos**.
- Não é de leitura de arranque. É **on demand** (G26/T21).

---

## 2. Quando se escreve, e por quem

| Momento | Quem | O quê |
|---|---|---|
| **Fim de sessão** (obrigatório) | Toda a sessão que produziu documentos | Bloco de sessão completo, com todos os documentos — os que foram ao notebook e os que não foram (G29.3, T20) |
| **No momento** (não se adia) | Qualquer sessão | Pesquisa que o David declare ter feito — cataloga-se **antes de continuar** (G36) |
| **Entrada própria** | Arquitecto | Resultado de uma consolidação de documentação (G35) |

**Regra de ouro:** um documento que existe no repositório e não está no registo **é um bug**.
Corrige-se acrescentando, nunca reescrevendo (G24).

**Quem pode escrever:** todos. As threads têm aqui a **terceira e última excepção à regra
territorial** (G25, T2).

---

## 3. Estrutura do ficheiro

O ficheiro tem **duas zonas**: o **topo navegável** (quatro blocos) e o **corpo** (quatro
níveis de Dono). Nada mais.

### 3.1 Topo — por esta ordem, sem excepção

**(a) Descrição** — três a seis linhas: o que é o ficheiro, para que serve, e o aviso de
append-only. Escrita uma vez; não se toca.

**(b) Índice geral** — links para as secções principais do próprio ficheiro.
Formato: `- [[REGISTO-DOCUMENTOS#Arquitecto|Arquitecto]]`.

**(c) Índice de Donos** — um link por dono, incluindo cada thread individualmente.
É o índice que responde a *«o que é que a T004 produziu?»*.

**(d) Índice por Tipo** — um bloco por Tipo (Síntese · Report · Research · Dossier · Nota ·
Outros), cada um com a **tag de agregação** e, opcionalmente, um bloco Dataview.
É o índice que responde a *«mostra-me todas as sínteses do projecto»*.

### 3.2 Corpo — quatro níveis de Dono, por esta ordem

```
# 1 · ARQUITECTO          ← sessões de modo Arquitecto
# 2 · THREADS             ← subheading H2 por thread: ## T001 · local, ## T002 · jardim-v2, …
# 3 · DAVID               ← pesquisa autónoma e material próprio (cargo DVD)
# 4 · OUTROS              ← o que não cabe acima: terceiros, documentos herdados, arqueologia
```

**Dentro de cada dono — e dentro de cada thread — os registos são por SESSÃO.**
Cada bloco de sessão tem exactamente duas partes, por esta ordem:

1. **Sumário de sessão** — **1 a 3 linhas**, o que a sessão fez *com documentação*.
   Não é o resumo da sessão; é o resumo do trabalho documental. Ex.: *«Fase 1 da T005:
   quatro pesquisas em paralelo, uma síntese e um report. Três subiram ao notebook.»*
2. **A tabela** de documentos — as oito colunas da §4.

As sessões acumulam por ordem cronológica, a mais recente **no fim** de cada dono.
Isto é consequência directa do append-only: escreve-se onde se chega.

---

## 4. As oito colunas — formato exacto

Cabeçalho canónico, a copiar tal e qual:

```markdown
| Tipo | Data | Dono | Sessão | Título | Ficheiros | Sumário | Supported |
|---|---|---|---|---|---|---|---|
```

### 4.1 `Tipo`

Vocabulário **fechado** de seis valores. Marca-se com **tag hierárquica** — é a tag que faz
o índice automático funcionar (ver §5).

| Valor | Tag | Quando se usa |
|---|---|---|
| Síntese | `#tipo/sintese` | Cruza e conclui sobre **vários** documentos anteriores |
| Report | `#tipo/report` | Relato de trabalho feito: objectivos, método, achados, próximos passos |
| Research | `#tipo/research` | Estado da arte ou investigação externa. **Leva sempre o prompt dentro do ficheiro** |
| Dossier | `#tipo/dossier` | Compilação de referência sobre um objecto ou tema, para consulta |
| Nota | `#tipo/nota` | Registo curto, pontual, sem pretensão de completude |
| Outros | `#tipo/outros` | Governo, auditoria, consolidação — **ou** quando não há certeza |

**Formato na célula:** `#tipo/research` — só a tag, minúsculas, sem acentos, sem negrito.
Obsidian não indexa tags dentro de *code fences*, por isso **não se põe entre crases**.

> **Regra de classificação (G28, T19).** Se o tipo não for evidente, o Agente **DEVE
> perguntar ao David**. **NÃO PODE** classificar ao calha. `Outros` é para quando não há
> certeza **e** a pergunta já foi feita ou não se justifica — não é o caixote do lixo do
> preguiçoso.

**Correspondência com o TIPODOC do NotebookLM:** `Research`→`RESEARCH`, `Report`→`REPORT`,
`Síntese`→`SINTESE`, `Dossier`→`DOSSIER`, `Nota`→`NOTA`, `Outros`→`OUTROS`. Um para um.

### 4.2 `Data`

Data **do documento**, não da sessão que o registou — distinguem-se quando se cataloga
material antigo. Formato `AAAA-MM-DD`, sempre. Ex.: `2026-09-17`.

Se a data for desconhecida (material herdado, arqueologia): `s/d` e o motivo no Sumário.

### 4.3 `Dono`

O cargo: `Arquitecto` · `T001` … `TNNN` · `David` · `Outros`.
Usa-se a forma curta da thread (`T005`), não o nome da pasta.
Corresponde ao `CARGO` da nomenclatura NotebookLM (`TNN` · `ARQ` · `DVD`).

### 4.4 `Sessão`

O **nome da sessão Claude**, entre aspas angulares, tal como aparece no cliente.
Ex.: `«2026.09.17 - Arquiteto - Pesquisa de Catalogacao»`.

Quando não há sessão associada — material do David, documento herdado — escreve-se
`— (sem sessão)`. Nunca se inventa um nome.

### 4.5 `Título`

O título legível do documento, **com wikilink para o ficheiro**.
Formato: `[[caminho/completo/ficheiro|Título Legível]]`

Exemplo real:
```
[[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES|Especialidades de caracterização]]
```

Sem extensão `.md` no caminho (Obsidian resolve). Se o documento **não tem ficheiro no
repositório** (material `DVD` carregado directamente no notebook — ver §7.4), escreve-se o
título em texto simples, sem link, seguido de `*(só no notebook)*`.

### 4.6 `Ficheiros`

Os artefactos em disco: o `.md` original e o `.pdf` do deck, se existir.
**Requisito do David: ver só o nome do ficheiro, sem caminho, mas clicável.**

Em Obsidian isto é o **alias de wikilink** — caminho completo antes do `|`, nome curto depois:

```
[[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md|01-ESPECIALIDADES.md]] · [[30-THREADS/T005-caracterizacao/research/T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf|T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf]]
```

Renderiza como: **01-ESPECIALIDADES.md · T005-26-09-17-RESEARCH-ESPECIALIDADES.pdf** — dois
links, sem caminho visível.

**Regras:**

- Separador entre ficheiros: ` · ` (ponto médio com espaços).
- No `.md` **inclui-se a extensão no caminho** — ao contrário da coluna Título — porque o
  alias tem de mostrar o nome do ficheiro e o link tem de resolver para o ficheiro exacto.
- O `.pdf` **exige sempre** o caminho completo: Obsidian não resolve anexos por nome curto
  com a fiabilidade que resolve notas.
- **Quando não há PDF** (não foi ao notebook): escreve-se `— sem PDF`. Não se deixa vazio,
  não se inventa link. Um wikilink para um ficheiro inexistente renderiza a vermelho e
  parece erro por corrigir; `— sem PDF` é informação.
- **Quando não há `.md`** (material só no notebook): `— sem ficheiro`.

### 4.7 `Sumário`

**Duas linhas.** O que o documento **conclui**, não de que trata. Um sumário que diga
«analisa a drenagem» é inútil; «conclui que a betonilha escoa e a demolição é dispensável»
serve.

Negrito no achado principal. Sem listas, sem quebras de linha — é uma célula de tabela;
usa-se ` · ` para separar ideias.

### 4.8 `Supported` — ver §6

Ficheiros que usaram **este** documento como fonte. Coluna de leitura inversa.
**Leitura obrigatória da §6 antes de preencher.**

---

## 5. Como funcionam os índices

O repositório lê-se em **Obsidian**. As duas mecânicas não são equivalentes:

| Mecanismo | O que faz | O que não faz |
|---|---|---|
| **Tag** (`#tipo/sintese`) | Agrega: um clique lista todas as ocorrências no vault | Não gera texto no ficheiro |
| **Wikilink** (`[[x]]`) | Gera backlink no destino | **Não agrega** — não produz lista por categoria |

### 5.1 Decisão — tags hierárquicas

**Adopta-se `#tipo/<valor>`, hierárquica, minúsculas, sem acentos.**
*(Decisão minha — assinalada para revisão do David.)*

Porquê hierárquica e não plana (`#sintese`):

1. A hierarquia **agrupa no painel de tags** — `tipo` aparece como nó colapsável com os seis
   filhos dentro, em vez de seis tags soltas misturadas com tudo o resto.
2. Clicar em `#tipo` lista **todos** os documentos catalogados; clicar em `#tipo/sintese`
   filtra. A tag plana não dá o nível agregado.
3. Evita colisão: `#nota` e `#report` são palavras demasiado genéricas para um vault que vai
   crescer; `#tipo/nota` é inequívoco.

Sem acentos (`sintese`, não `síntese`) porque tags com acento funcionam mas partem-se em
pesquisas e em qualquer script futuro. O valor legível acentuado vive no índice, não na tag.

**Tag de dono — adopta-se em paralelo:** `#dono/arquitecto` · `#dono/t005` · `#dono/david` ·
`#dono/outros`. **Não vai na tabela** (seria ruído em todas as linhas, já há coluna Dono);
vai **uma vez, no heading do bloco de sessão**, logo abaixo do título. Isto dá o índice
automático por dono sem poluir a tabela. *(Decisão minha.)*

### 5.2 O índice por Tipo — como se monta

Cada bloco do índice tem **três camadas**, por ordem decrescente de robustez:

```markdown
### Sínteses
Tag: #tipo/sintese
<!-- Clicar na tag acima lista todas as sínteses do vault. -->

```dataview
TABLE WITHOUT ID Título, Dono, Data
FROM #tipo/sintese
SORT Data DESC
```
```

1. **A tag** — funciona sempre, em qualquer Obsidian, sem plugins.
2. **O bloco Dataview** — complemento. Se o plugin não estiver instalado, o Obsidian mostra
   o bloco como código: feio, mas não quebra nada, e a tag acima continua a servir.
3. **A lista manual** — só se o David a quiser. Não se recomenda: é a única parte que
   desactualiza em silêncio.

> **Requisito firme:** o ficheiro **tem de ser legível e útil sem plugins**. Dataview é
> sempre complemento, nunca a fonte. Se houver conflito entre «fica bonito com Dataview» e
> «lê-se sem Dataview», ganha o segundo.

> **Ressalva técnica.** Dataview indexa tags **por ficheiro**, não por linha de tabela.
> Como todas as tags vivem num só ficheiro (`REGISTO-DOCUMENTOS.md`), uma query
> `FROM #tipo/sintese` devolve **o ficheiro inteiro**, não as linhas. Os blocos Dataview
> acima ficam no template como **andaime, comentados**, e só se activam se e quando o
> registo passar a uma nota por documento. **Até lá, a tag e o índice manual de Donos são o
> mecanismo real.** *(Decisão minha: não vender automatismo que não funciona.)*

### 5.3 Quem actualiza os índices

| Índice | Manutenção | Quem |
|---|---|---|
| (b) Índice geral | Estático — só muda se se criar secção nova | Arquitecto |
| (c) Índice de Donos | **Manual.** Acrescenta-se uma linha quando nasce uma thread nova | Quem abre a thread = Arquitecto (G9) |
| (d) Índice por Tipo | **Automático via tag.** Não se mexe | Ninguém |

**Uma thread NÃO actualiza os índices do topo.** Acrescenta o seu bloco de sessão no corpo,
debaixo do seu próprio heading, e mais nada. Se o heading da thread ainda não existir no
índice de Donos, a thread **cria o heading no corpo** e deixa nota em `INBOX.md` a pedir ao
Arquitecto que acrescente a linha ao índice. *(Decisão minha: mantém o append-only intacto
e não obriga a thread a editar o topo do ficheiro.)*

---

## 6. O problema do «Supported» — e a sua resolução

### 6.1 O conflito, posto a nu

Sete das oito colunas **descrevem o documento** e são conhecidas no momento em que se
escreve a linha. `Supported` descreve **quem depende dele** — e isso só se sabe *depois*,
quando um documento futuro o usa como fonte.

Manter `Supported` correcto obriga a **voltar atrás e editar uma linha antiga**. O G24 diz
que o ficheiro é **append only**: não se reescreve nem se reordena; corrige-se acrescentando.
São incompatíveis.

### 6.2 As opções

| # | Opção | Custo |
|---|---|---|
| (a) | Excepção declarada ao append-only, só nesta coluna | Abre precedente. Uma vez aberta a porta a editar linhas antigas, perde-se a garantia que torna o ficheiro auditável |
| (b) | Campo fica vazio; regista-se só do lado do documento novo | Barato, mas **perde o índice inverso** — que é precisamente o valor do campo |
| (c) | Secção de dependências no fim, essa sim editável | Preserva o append-only no corpo, mas cria um segundo sítio para procurar |
| (d) | Híbrido | — |

### 6.3 Decisão: **(d) híbrido — coluna congelada + secção viva**

*(Decisão minha. Argumentada abaixo; o David pode reverter para (a) se preferir simplicidade
a garantia.)*

**A regra, em três linhas:**

> 1. A coluna `Supported` é preenchida **uma só vez**, no momento em que a linha nasce, e
>    **nunca mais se toca**. Na esmagadora maioria dos casos nasce com `—`.
> 2. Toda a dependência descoberta **depois** regista-se na secção
>    **`## Dependências entre documentos`**, no fim do ficheiro. **Essa secção — e só essa —
>    é editável.**
> 3. A secção de dependências é a **única excepção ao G24**, e está declarada aqui e no
>    cabeçalho do próprio registo. Fora dela, o append-only é absoluto.

**Porque é que (d) ganha a (a).** O valor do append-only não é estético: é poder abrir o
ficheiro daqui a um ano e saber que nenhuma linha foi alterada desde que foi escrita. Uma
excepção «só para uma coluna» é indistinguível, na prática, de licença para editar — o
próximo agente vê uma linha antiga editada e conclui que editar é aceitável. Confinar toda
a mutabilidade a **uma secção com nome próprio, no fim do ficheiro** mantém a garantia onde
ela importa e torna a excepção visível em vez de dispersa.

**Porque é que (d) ganha a (b).** (b) é a opção honesta mas amputada: perde-se a pergunta
*«se eu revogar este documento, o que é que fica órfão?»* — que é exactamente a pergunta da
consolidação (G32–G35). A secção de dependências devolve-a.

**Porque é que (d) ganha a (c) pura.** (c) esvazia a coluna e obriga a saltar sempre ao fim.
Com (d), a coluna continua a valer para o caso comum (a dependência já é conhecida quando se
escreve: uma síntese que cita quatro pesquisas regista-o *no acto*, do lado das quatro? não —
regista-o do lado da síntese, na coluna `Supported` das pesquisas? também não). Precisando:

**Como se preenche na prática, os dois casos:**

- **Caso comum — dependência conhecida no acto.** A sessão que produz `05-SINTESE-FASE-1`
  sabe que ela consome as pesquisas 01, 03 e 04. Essas três linhas **já existem** (foram
  escritas antes, talvez na mesma sessão). **Não se volta atrás.** Escreve-se uma entrada na
  secção de dependências, e na linha nova da síntese o `Supported` nasce a `—`.
- **Caso raro — dependência simultânea.** Se o documento-fonte e o documento-consumidor
  nascem na **mesma tabela, na mesma sessão**, e a fonte ainda não foi escrita, então
  preenche-se `Supported` da fonte directamente. É a única vez que a coluna nasce preenchida.

**Formato da coluna `Supported`:**
- Vazio: `—`
- Preenchido: `[[caminho/ficheiro|nome-curto.md]]`, múltiplos separados por ` · `

**Formato da secção de dependências** (uma linha por relação, append-only dentro da secção):

```markdown
## Dependências entre documentos

<!-- ÚNICA secção editável deste registo. Excepção declarada ao G24. -->
<!-- Uma linha por relação. A relação lê-se: FONTE → foi usada por → CONSUMIDOR. -->

| Data do registo | Fonte | Usada por | Natureza |
|---|---|---|---|
| 2026-09-17 | [[30-THREADS/T005-caracterizacao/research/01-ESPECIALIDADES.md\|01-ESPECIALIDADES.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Síntese |
| 2026-09-17 | [[40-PESQUISAS/David/2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md\|2026.09.17-RESEARCH-SISTEMAS_DE_COBERTURA_AJARDINADA.md]] | [[30-THREADS/T005-caracterizacao/research/05-SINTESE-FASE-1.md\|05-SINTESE-FASE-1.md]] | Fonte externa citada |
```

Valores de `Natureza` (fechado): `Síntese` · `Fonte externa citada` · `Substituição` ·
`Refutação` · `Deck NotebookLM`.

**Nota de sintaxe:** o `|` do alias dentro de uma célula de tabela markdown **tem de ser
escapado** — `\|` — senão parte a coluna. Vale para todas as colunas com wikilink com alias.
É a causa número um de tabelas partidas neste ficheiro.

---

## 7. Casos difíceis

### 7.1 Documento com vários donos

Duas threads produzem um documento em conjunto, ou o Arquitecto termina o que uma thread
começou.

**Regra:** **um documento, um dono — o de quem o escreveu no fim.** Regista-se **uma vez**,
no bloco desse dono. Na coluna `Dono` escreve-se o dono principal e acrescenta-se o
co-autor: `T004 (+T005)`. No `Sumário` diz-se de onde veio: *«Iniciado na T005, concluído
pelo Arquitecto.»*

**Não se duplica a linha nos dois donos.** Duplicar destrói a contagem e obriga a manter
duas cópias sincronizadas num ficheiro append-only. *(Decisão minha.)*

### 7.2 Documento que substitui outro

**Regra:** o documento novo regista-se **normalmente, como linha nova**. O antigo **não se
toca** — nem se apaga, nem se risca, nem se edita o sumário.

A substituição regista-se **na secção de dependências**, com `Natureza: Substituição`,
lendo-se: *fonte (o antigo) → usada por (o novo)*.

Se a substituição tiver consequência para o NotebookLM — a source antiga passa a `SUPERADO`
(G33) — isso é matéria de consolidação, não de registo. Deixa-se nota em `INBOX.md`.

### 7.3 Documento do David sem sessão associada

É o caso normal do cargo `DVD`. Regista-se no dono **David**, num bloco de sessão cujo
heading é a **data de catalogação**, não de produção:

```markdown
## 2026-09-17 · Catalogação — (sem sessão)
```

Na coluna `Sessão`: `— (sem sessão)`. Na coluna `Data`: a data do documento, se conhecida.

**Obrigações adicionais antes de registar (G36):** localizar e ler o ficheiro (procurar no
repositório **inteiro** antes de concluir que não existe) · verificar o front matter
(`created`, `summary`, `Asked by`) e corrigir o summary se não descrever o conteúdo real ·
confirmar que o **prompt está dentro do ficheiro** e pedi-lo ao David se não estiver ·
**confrontar com o estado do projecto** e sinalizar a quem interessa · perguntar se vai para
o notebook, com cargo `DVD`.

### 7.4 Documento que existe só no NotebookLM e não no repositório

Material que o David carregou directamente. **Não tem ficheiro, logo não tem wikilink.**

- `Título`: texto simples + `*(só no notebook)*`
- `Ficheiros`: `— sem ficheiro`
- `Sumário`: **declara a origem** — quem o trouxe e de onde
- `Dono`: `David` (ou `Outros`, se for de terceiro)

> **O Agente NÃO PODE propor eliminá-lo por não reconhecer a origem: pergunta primeiro.**
> Aconteceu na consolidação de 2026-09-17 — dois ficheiros classificados como «órfãos»
> existiam, e a busca é que tinha sido incompleta.

Se mais tarde o ficheiro aparecer no repositório: **não se edita a linha antiga.** Escreve-se
linha nova no bloco de sessão corrente, com o sumário a dizer *«Localizado a AAAA-MM-DD;
substitui o registo sem ficheiro de AAAA-MM-DD»*, e a relação vai à secção de dependências
com `Natureza: Substituição`.

### 7.5 Documento revogado ou superado

**Não se apaga. Não se risca. Não se edita a linha.**

Regista-se **linha nova** no bloco da sessão que descobriu a revogação, com:
- `Tipo`: `#tipo/nota`
- `Título`: `Revogação de <documento>`
- `Sumário`: o que foi revogado, **porquê**, e a referência à decisão de `ESTADO.md` ou à
  entrada de `REJEICOES.md` que o revoga

E entrada na secção de dependências com `Natureza: Refutação`.

**Porquê assim.** O estado VIGENTE/SUPERADO/REVOGADO/DUPLICADO do G33 é do **NotebookLM**,
não deste registo. Este ficheiro diz *o que foi produzido*; a validade de cada peça vive em
`ESTADO.md` e `REJEICOES.md`. Marcar linhas como revogadas aqui criaria um terceiro sítio
onde a verdade vive — contra o G1. *(Decisão minha.)*

### 7.6 Sessão que não produziu documentos

**Não escreve nada.** Não há bloco de sessão vazio. O registo cataloga artefactos, não
sessões.

### 7.7 Documento produzido e depois apagado na mesma sessão

**Não se regista.** Rascunho não é documento. A fronteira: se foi mostrado ao David ou ficou
em disco no fim da sessão, é documento.

---

## 8. Higiene — o que NUNCA se faz neste ficheiro

1. **NUNCA se reescreve ou reordena** o corpo. Append only (G24). A **única** excepção é a
   secção `## Dependências entre documentos`.
2. **NUNCA se apaga uma linha.** Nem por estar errada — corrige-se com linha nova que declara
   a correcção.
3. **NUNCA se lê por rotina ao arrancar sessão.** Leitura *on demand* (G26, T21). É um
   ficheiro que vai crescer para lá do razoável; lê-se quando se precisa de saber o que
   existe.
4. **NUNCA se toma uma decisão a partir daqui.** Registo não é `ESTADO.md` (G1). Uma
   resposta do NotebookLM também não é decisão (G31).
5. **NUNCA se classifica o Tipo ao calha.** Se não for evidente, pergunta-se (G28, T19).
6. **NUNCA se inventa um wikilink** para um ficheiro que não se confirmou existir. Sem
   ficheiro → `— sem PDF` / `— sem ficheiro`.
7. **NUNCA se deixa de escapar o `|` do alias** dentro de uma célula de tabela: usa-se `\|`.
8. **NUNCA uma thread edita o topo do ficheiro** — índices e descrição são do Arquitecto.
   A thread escreve o seu bloco de sessão no corpo e mais nada.
9. **NUNCA se regista só o que foi ao NotebookLM.** Registam-se **todos** os documentos
   produzidos, com o motivo de não terem ido (G23, T20).
10. **NUNCA se adia a catalogação de uma pesquisa do David** para o fim da sessão (G36).

---

## 9. Checklist de fim de sessão

```
[ ] Todos os documentos produzidos nesta sessão estão na tabela? (os que foram e os que não foram)
[ ] Cada linha tem as 8 colunas preenchidas, nenhuma vazia?
[ ] Tipo marcado com tag #tipo/<valor>, e perguntado ao David se não era evidente?
[ ] Wikilinks com alias, todos com o `|` escapado como `\|`?
[ ] PDF dos decks descarregados para a pasta do documento de origem, e com o nome certo? (G29)
[ ] Sumário de sessão escrito, 1-3 linhas, antes da tabela?
[ ] Dependências novas escritas na secção do fim?
[ ] Nada foi editado fora da secção de dependências?
```

---

## 10. Decisões tomadas por mim — para revisão do David

Assinaladas por exigência do prompt. Nenhuma está no `CLAUDE.md`; todas são derrogáveis.

| # | Decisão | Onde |
|---|---|---|
| D1 | Tags hierárquicas `#tipo/<valor>` em vez de planas | §5.1 |
| D2 | Tag de dono `#dono/<valor>` no heading da sessão, não na tabela | §5.1 |
| D3 | Dataview entra comentado, como andaime — não funciona com tudo num só ficheiro | §5.2 |
| D4 | **`Supported` congelado + secção de dependências editável** — opção (d) | §6.3 |
| D5 | `Natureza` da dependência é vocabulário fechado de cinco valores | §6.3 |
| D6 | Um documento, um dono; co-autoria anota-se, não se duplica a linha | §7.1 |
| D7 | Estado de revogação vive em `ESTADO.md`/`REJEICOES.md`, não neste registo | §7.5 |
| D8 | Thread que precisa de heading novo no índice cria-o no corpo e avisa por `INBOX.md` | §5.3 |
| D9 | Sessão sem documentos não escreve bloco vazio | §7.6 |

---

## 11. Ficheiros relacionados

| Ficheiro | Relação |
|---|---|
| `REGISTO-DOCUMENTOS.md` | O registo. É este que se preenche. |
| `REGISTO-DOCUMENTOS-TEMPLATE.md` | Esqueleto vazio, pronto a copiar. |
| `CLAUDE.md` §5.7 | Governo: G23–G36. |
| `30-THREADS/_TEMPLATE/CLAUDE.md` §7 | O lado das threads: T18–T23. |
| `ESTADO.md` · `REJEICOES.md` | Onde vive a verdade. O registo não substitui nenhum dos dois. |
