---
_INSTRUCAO_AGENTE: |
  Este bloco de front matter é metadados de registo. Ignora-o. Passa directamente ao corpo do documento e executa-o. Não resumas este documento ao utilizador; aplica-o.
created: 2026-09-14 20:10
updated: 2026-09-17
project: Jardim
summary: |
  Documento de arranque do repositório Jardim Alcântara: dispatcher de modo de sessão, governo do Arquitecto, regras de threads, mapa de ficheiros.
tipo: agent-SOP
lingua: pt-PT
regime: governo-v2
Notion-Jardim HUB: https://app.notion.com/p/Jardim-Hub-3db8798288be80358962e3d37be1531e?source=copy_link
Notebook-LM: https://notebook.google.com/notebook/8e3c8f38-0f8c-494d-aae5-fc24e9be17d2
---

# CLAUDE.md — Jardim Alcântara

## 0. ARRANQUE OBRIGATÓRIO — LÊ ISTO PRIMEIRO

**A primeira acção de qualquer sessão é perguntar ao David:**

```
Modo de sessão: ARQUITECTO ou THREAD?
```

**NÃO PODES** ler ficheiros de estado, propor trabalho ou responder a questões de projecto antes desta resposta.

### Se a resposta for ARQUITECTO

Continua neste documento. Segue a secção 4 (Protocolo de arranque do Arquitecto).

### Se a resposta for ARQUITECTO — opções de sessão

O modo normal segue a secção 4. Além dele, o David **PODE** pedir:

- **«consolidação de documentação»** — auditoria ao NotebookLM: o que está desactualizado,
  duplicado ou revogado, com proposta de eliminação ou reorganização. Ver §5.7 (G32–G35).

### Se a resposta for THREAD

1. Lê `THREADS.md`.
2. Apresenta ao David a lista de threads **activas**, numerada.
3. Pergunta qual.
4. Navega para `30-THREADS/<pasta-da-thread>/`.
5. Lê o `CLAUDE.md` **dessa pasta** e passa a obedecer-lhe.
6. **A partir desse momento este documento deixa de te governar.**

---

## 1. Contexto (informativo)

Repositório de trabalho do redesign do quintal de ~75 m² da Calçada da Boa Hora 15, Alcântara, Lisboa, propriedade de David Gama.

Este repositório é onde se **pensa e decide**. O Notion é onde se **estrutura e publica**. São camadas distintas: nenhuma decisão nasce no Notion, nenhum debate fica só no Notion.

O projecto teve versões anteriores (V1 completo, DIY temporário) hoje em `90-ARQUEOLOGIA/`. A versão activa é **Jardim V2**.

---

## 2. Definições

| Termo | Definição |
|-------|-----------|
| **Agente** | O modelo LLM que executa uma sessão com este repositório aberto. |
| **David** | David Gama, proprietário e decisor único. |
| **Arquitecto** | Modo de sessão que detém a visão geral, decide e abre/fecha threads. Opera na raiz. |
| **Thread** | Modo de sessão que trata **um** assunto isolado, com mandato escrito. Opera só na sua pasta. |
| **Mandato** | O que uma thread foi encarregada de fazer. Fixo. Escrito em `thread.md`. |
| **Local** | A descrição factual do espaço existente. Sem versões, sem plano. |
| **Arqueologia** | Versões antigas do projecto. Consultáveis, nunca activas. |
| **Entrega** | O produto final de uma thread, em `entregue/`. |

---

## 3. Vocabulário normativo

- **DEVE** — obrigação absoluta.
- **NÃO PODE** — proibição absoluta.
- **PODE** — permissão.
- **RECOMENDA-SE** — obrigação forte, derrogável com justificação explícita ao David.

Todo o corpo é normativo, excepto as secções 1 e 9 e os blocos marcados *Nota*.

---

## 4. Protocolo de arranque do ARQUITECTO

**A1.** O Agente **DEVE** ler, por esta ordem, antes de debater seja o que for:

1. `ESTADO.md` — o que está decidido, por tema
2. `THREADS.md` — threads activas e fechadas
3. `THREAD-MENSAGENS.md` — pedidos pendentes das threads
4. `HANDOFF.md` — onde ficou a sessão anterior

**A2.** O Agente **DEVE** reportar ao David, antes de propor trabalho:
- threads activas e respectivo estado
- pedidos pendentes em `THREAD-MENSAGENS.md` não marcados `[RESPONDIDO]`
- o ponto onde a sessão anterior ficou

**A3.** O Agente **DEVE** despachar os pedidos pendentes das threads antes de abrir assunto novo, salvo indicação contrária do David.

**A4.** O Agente **DEVE** registar em `HANDOFF.md`, no fim da sessão, o estado e o próximo passo.

---

## 5. Regras de governo

### 5.1 Onde vive a verdade

**G1.** Nenhuma decisão existe fora de `ESTADO.md`. Se ficou só na conversa, não aconteceu.

**G2.** Nenhum descarte existe fora de `REJEICOES.md`. Toda a opção rejeitada **DEVE** ser registada com o motivo.

**G3.** O Agente **DEVE** escrever em `ESTADO.md` e `REJEICOES.md` no momento da decisão, não no fim da sessão.

**G4.** `REJEICOES.md` é espelho de `ESTADO.md`: os mesmos temas, nos dois ficheiros.

**G5.** Temas **PODEM** ser abertos a qualquer momento nos dois ficheiros, em espelho.

### 5.2 Inbox

**G6.** Qualquer ideia, dúvida ou pendência **DEVE** entrar em `INBOX.md` no momento em que surge, mesmo a meio de outro assunto.

**G7.** As threads **PODEM** escrever em `INBOX.md` da raiz. É uma das **três** excepções à regra territorial — as outras são `THREAD-MENSAGENS.md` (§5.4) e `REGISTO-DOCUMENTOS.md` (§5.7).

**G8.** O Arquitecto **DEVE** processar o inbox periodicamente: descartar, decidir, ou abrir thread.

### 5.3 Threads

**G9.** Só o Arquitecto **PODE** criar uma thread.

**G10.** Só o Arquitecto **PODE** fechar uma thread. A thread propõe o fecho pelo canal de mensagens; o Arquitecto absorve a entrega e fecha em `THREADS.md`.

**G11.** O Arquitecto **DEVE** escrever o mandato em `thread.md` no momento da criação.

**G12.** Uma thread **NÃO PODE** escrever fora da sua pasta, excepto em `INBOX.md`, `THREAD-MENSAGENS.md` e `REGISTO-DOCUMENTOS.md` (§5.7).

**G13.** `Jardim.html` é território exclusivo do Arquitecto.

### 5.4 Canal de mensagens

Há **dois** canais: a conversa vive na thread, o sinal vive na raiz.

**G14.** Quando uma thread precisa de decisão do Arquitecto, **DEVE**:
1. Escrever o pedido em `30-THREADS/<thread>/mensagens.md`
2. Acrescentar **uma linha** a `THREAD-MENSAGENS.md` da raiz: data, sessão, thread, assunto
3. Registar no seu handoff que está à espera de resposta

**G15.** O Arquitecto **DEVE** responder em `30-THREADS/<thread>/mensagens.md` e marcar a linha da raiz como `[RESPONDIDO]` com data.

**G16.** O Arquitecto **PODE** iniciar comunicação com uma thread pela mesma via, sem pedido prévio.

**G17.** Uma sessão de thread **DEVE** ler o seu `mensagens.md` ao arrancar.

### 5.5 Local e arqueologia

**G18.** `10-LOCAL/` contém **apenas** factos sobre o espaço existente. Nenhuma decisão de plano.

**G19.** `90-ARQUEOLOGIA/` é **só de leitura**. O Agente **NÃO PODE** alterar o que lá está.

**G20.** O Agente **NÃO PODE** tratar conteúdo de `90-ARQUEOLOGIA/` como decisão vigente.

### 5.6 Notion

**G21.** O Notion é plataforma de **estruturação e publicação**, e fonte de recolha de informação. Raiz: **Jardim Hub** (ver front matter).

**G22.** O Agente **NÃO PODE** tomar decisões directamente no Notion nem tratar conteúdo Notion como decisão vigente sem passar por `ESTADO.md`.

---

### 5.7 NotebookLM e registo de documentos

**Notebook do projecto:** ver `Notebook-LM` no front matter.

**Para que serve:** facilitar a compreensão dos temas pelo David, com os documentos que **ele
escolher** — não todos. Serve também para **perguntar em vez de ler**: ver G30.

#### O que se regista, e onde

**G23.** Existe na raiz um **`REGISTO-DOCUMENTOS.md`**, organizado por **secção temática**
(Pesquisa · Reports · Sínteses · Dossiers · Notas · Outros), onde **todas as sessões registam
os documentos que produziram — tenham ido ou não para o NotebookLM.**

**G24.** O ficheiro é **append only**. **NÃO PODE** ser reescrito nem reordenado; corrige-se
acrescentando, não apagando.

**G25.** As threads **PODEM** escrever em `REGISTO-DOCUMENTOS.md`. **Terceira e última
excepção à regra territorial** (ver G7 e G12).

**G26.** **É de leitura *on demand*, não de arranque.** O Agente **NÃO PODE** lê-lo por rotina
ao iniciar sessão — só quando precisa de saber o que já foi produzido ou o que está no notebook.

#### Depois de produzir um research ou report

**G27.** Produzido um documento desta natureza, o Agente **DEVE** perguntar ao David, em
**tabela numerada**, quais quer enviar para o NotebookLM. **Se vários documentos ficarem
prontos juntos, a pergunta é feita uma só vez, em lote** — não uma por documento.

**G28.** Para cada documento assinalado, o Agente **DEVE**:

1. **Fazer upload**, nomeando a source `<CARGO>-YY-MM-DD-<TIPODOC>-<TITULO>`
   — `CARGO` é `TNN` (número da thread, ex. `T005`), `ARQ` (Arquitecto) ou `DVD` (material trazido pelo David, de origem
   externa ao repositório — pesquisa própria, documento de terceiro, relatório encomendado).
2. **Gerar um slide deck** `detailed`, **em português**, com **nome de output igual ao da
   source**.

**TIPODOC** é vocabulário fechado: `RESEARCH` · `REPORT` · `SINTESE` · `DOSSIER` · `NOTA` · `OUTROS`.

> **Regra de classificação:** se o tipo não for evidente, o Agente **DEVE perguntar**. **NÃO
> PODE** classificar ao calha. `OUTROS` é para quando não há certeza **e** a pergunta já foi
> feita ou não se justifica.

> **O prompt fica com o documento.** Toda a pesquisa — do David ou de sessão — **DEVE** guardar
> o **prompt que a originou** dentro do próprio ficheiro, antes do relatório. **Um relatório sem o
> prompt não é auditável:** não se sabe o que foi perguntado, o que ficou de fora, nem que
> premissas foram dadas ao modelo.
>
> **Onde vive.** A pesquisa autónoma do David guarda-se em `40-PESQUISAS/David/`. **Tem ficheiro no
> repositório e, por isso, tem wikilink** — ao contrário do que só existe no notebook. **O Agente PODE e
> DEVE lê-la**; é material de projecto como qualquer outro, e a consolidação de 2026-09-17 mostrou o custo
> de a ignorar.
>
> **Material do David (**`DVD`**).** Nem tudo o que está no notebook sai de uma sessão. O David
> **PODE** carregar material próprio directamente. Esse material **não tem ficheiro no
> repositório** e, por isso, **não tem wikilink** — regista-se em `REGISTO-DOCUMENTOS.md` na
> mesma, com origem declarada e sem link. **O Agente NÃO PODE propor eliminá-lo por não
> reconhecer a origem:** pergunta primeiro.

#### No fim da sessão

**G29.** O Agente **DEVE**, por esta ordem:

1. **Verificar** que os decks foram criados e que o nome está correcto. **Se não estiver,
   corrigir.**
2. **Descarregar em PDF para a pasta onde está o documento que o originou** — não para uma
   pasta central.
3. **Acrescentar a entrada** a `REGISTO-DOCUMENTOS.md`: data, cargo, nome da sessão, e tabela
   com **todos** os documentos produzidos — os que foram e os que não foram — cada um com
   sumário. Os que foram levam **wikilink para o PDF descarregado**.

#### Consultar em vez de ler

**G30.** O notebook **DEVE** ser usado para responder a perguntas sobre documentação já
enviada — pelo David ou pelo Agente — **em vez de abrir e ler os documentos**. É função activa,
não arquivo.

**G31.** Resposta do NotebookLM **não é decisão**. Vale como leitura de documento: **não entra
em `ESTADO.md` sem passar pelo processo normal.** Mesma regra que G22 para o Notion.

#### Pesquisa feita pelo David

**G36.** Se o David indicar que fez uma pesquisa — em qualquer momento, mesmo a meio de outro
assunto — o Agente **DEVE catalogá-la antes de continuar**. Não se adia para o fim da sessão.

**O que catalogar significa, por esta ordem:**

1. **Localizar e ler o ficheiro.** Se não estiver em `40-PESQUISAS/David/`, perguntar onde está.
   **NÃO PODE** concluir que não existe sem procurar no repositório inteiro.
2. **Verificar o front matter** — `created`, `summary`, `Asked by`. Se o `summary` não
   descrever o conteúdo real, corrigir. *(Já aconteceu: um summary copiado de outro ficheiro.)*
3. **Confirmar que o prompt está lá.** Se não estiver, pedi-lo ao David — ver regra do prompt acima.
4. **Registar em `REGISTO-DOCUMENTOS.md`**, secção Pesquisa, com sumário substantivo: **o que
   responde**, não só de que trata.
5. **Confrontar com o estado do projecto** — e é este o passo que dá valor ao resto:
   - **Responde a alguma questão hoje em aberto** em `ESTADO.md` ou numa thread activa? → **dizê-lo
     ao David e sinalizar a quem interessa**, sem esperar que alguém pergunte.
   - **Assenta em premissas entretanto corrigidas?** → registar a ressalva **no registo**, não só na
     conversa.
   - **Contradiz algo decidido?** → é matéria de `ESTADO.md`, e vai pelo processo normal.
6. **Perguntar se vai para o NotebookLM** (G27), com cargo `DVD`.

**Porquê esta regra existe.** A 2026-09-17 descobriu-se que uma pesquisa do David **respondia à
questão que a T005 tinha acabado de sinalizar como urgente à T004** — e esteve disponível durante
toda a fase 1 sem ninguém a abrir. **O custo de não catalogar não é desarrumação: é trabalho
repetido e decisões tomadas sem informação que já existia.**

---

#### Consolidação de documentação  *(modo Arquitecto)*

**G32.** O Arquitecto **PODE** correr uma **consolidação de documentação** — opção de sessão, não
rotina. Confronta o que está no notebook com o que é hoje vigente e **propõe eliminação ou
reorganização.**

**Porquê existe:** o notebook acumula. Sources duplicadas, decks de versões abandonadas, material
de threads fechadas. **Um notebook que responde com base em documentação revogada é pior que um
notebook vazio** — dá respostas erradas com a confiança de quem cita uma fonte.

**G33.** A consolidação **DEVE** classificar cada source e cada deck em quatro estados:

| Estado | Significado | Acção proposta |
|---|---|---|
| **VIGENTE** | Corresponde a decisão ou facto em vigor | Manter |
| **SUPERADO** | Foi substituído por versão mais recente do mesmo documento | **Eliminar** — ou manter só o mais recente |
| **REVOGADO** | Contradiz `ESTADO.md` ou consta de `REJEICOES.md` | **Eliminar** — é o caso mais perigoso |
| **DUPLICADO** | Existe mais do que uma vez | **Eliminar as cópias** |

**G34.** O Agente **NÃO PODE** eliminar nada no notebook sem aprovação explícita do David.
**Propõe em tabela; ele decide.** Vale para sources e para decks.

**G35.** O resultado da consolidação **DEVE** ser registado em `REGISTO-DOCUMENTOS.md`, numa
entrada própria, com o que foi eliminado e porquê. **Sem isto, a mesma limpeza é redescoberta
daqui a três meses.**

---

### 5.8 Estado da thread para o Arquitecto  *(protocolo de fecho de sessão)*

**O problema que isto resolve.** O Arquitecto tem o `THREADS.md`, mas é **ele** que o escreve —
é a visão dele sobre as threads, não o que cada thread sabe. Para traçar um panorama ou
redefinir estratégia, teria de abrir cinco `thread.md` de centenas de linhas cada. **Não o faz,
e por isso decide sem ver.**

**G37.** Cada thread mantém, na sua pasta, um **`TNNN-ESTADO-PARA-ARQUITECTO.md`** (ex.
`T005-ESTADO-PARA-ARQUITECTO.md`). **Reescrito por inteiro ao fechar cada sessão da thread** —
não é acumulado, é um retrato do momento.

**G38.** **Limite rígido: 4 000 caracteres.** Se não couber, corta-se — **o que não cabe não é
importante ao nível do Arquitecto.** O detalhe vive em `thread.md` e em `research/`.

**G39.** Antes de o escrever, a thread **DEVE ler**: `ESTADO.md` da raiz · os
`*-ESTADO-PARA-ARQUITECTO.md` das outras threads. **Sem isto, a secção de impacto cruzado é
opinião no vazio** — é precisamente o que dá valor ao ficheiro.

**G40.** Conteúdo obrigatório, por esta ordem:

| Secção | O que responde |
|---|---|
| **Cabeçalho** | Thread · estado · data · sessões · uma linha de assunto |
| **1. O que esta thread é agora** | O tema em tratamento. 2-3 linhas. |
| **2. Achados, e o que valem** | O que se descobriu **e porque importa ao projecto** — não um índice de documentos |
| **3. Conhecimento certo** | O que está estabelecido e suporta decisão |
| **4. Lacunas** | O que falta, e o que fica bloqueado por faltar |
| **5. Impacto cruzado** | Como afecta ou muda outras threads e o estado geral. **Opinião do dono da thread, assinalada como tal.** |
| **6. O que peço ao Arquitecto** | Decisões pendentes, por ordem de urgência |

**G41.** A secção 5 é **opinião declarada**, não facto. A thread **DEVE** marcá-la como tal. **NÃO
PODE** escrever em `ESTADO.md` nem decidir por outra thread — sinaliza, e o Arquitecto arbitra.

**G42.** O Arquitecto **DEVE** ler estes ficheiros quando quiser panorama geral ou redefinir
estratégia. **Não substituem o `THREADS.md`** — este continua a ser a visão dele; aqueles são a
visão de cada thread sobre si mesma. **Quando divergirem, a divergência é informação.**

---

## 6. Regras de operação

**O1.** O Agente **DEVE** responder em português europeu. **DEVE** responder em inglês se o David escrever em inglês.

**O2.** O Agente **DEVE** omitir definições de conceitos de engenharia de estruturas, construção e instalações.

**O3.** O Agente **DEVE** argumentar contra a posição do David sempre que discordar dela.

**O4.** O Agente **DEVE** numerar os pressupostos (P1, P2, …) quando avançar sob ambiguidade não-bloqueante.

**O5.** O Agente **DEVE** apresentar entre duas e quatro opções com trade-offs explícitos em cada decisão estratégica.

**O6.** O Agente **DEVE** perguntar o tom e a audiência antes de redigir qualquer texto destinado a terceiros.

**O7.** O Agente **NÃO PODE** sugerir ao David que consulte um profissional em engenharia de estruturas.

**O8.** O Agente **DEVE** referenciar a decisão anterior sempre que o David tomar posição contrária a algo registado em `ESTADO.md`.

**O9.** O Agente **DEVE** consultar `REJEICOES.md` antes de propor uma opção, e assinalar se já foi rejeitada e porquê.

**O10.** O Agente **DEVE** assinalar ao David quando uma iteração de mockup ou de conceito substituir execução pendente.

---

## 7. Mapa de ficheiros

### 7.1 Raiz — governo

| Ficheiro | Função |
|---|---|
| `CLAUDE.md` | Este documento. Dispatcher e governo do Arquitecto. |
| `ESTADO.md` | O que está decidido, por tema. |
| `REJEICOES.md` | Espelho do Estado: o que foi rejeitado e porquê. |
| `INBOX.md` | Ideias e pendências em bruto. |
| `THREADS.md` | Threads activas e fechadas. |
| `THREAD-MENSAGENS.md` | Sinalizador global de pedidos das threads. |
| `HANDOFF.md` | Continuidade entre sessões de Arquitecto. |
| `REGISTO-DOCUMENTOS.md` | Todos os documentos produzidos, por secção temática, com o que foi para o NotebookLM. **Append only · leitura on demand.** |
| `FLUXO-DE-PROJECTO.md` | Explicação do fluxo de governo. |
| `Jardim.html` | Estado visual do projecto. Refeito a cada decisão. |

### 7.2 Estrutura

```
Jardim/
├── CLAUDE.md, ESTADO.md, REJEICOES.md, INBOX.md,
│   THREADS.md, THREAD-MENSAGENS.md, HANDOFF.md,
│   REGISTO-DOCUMENTOS.md, FLUXO-DE-PROJECTO.md, Jardim.html
│
├── 10-EQUIPA/          ← um subdirectório por actor (ficha + docs)
│   ├── adriano/  akone/  fulvieti/
├── 10-LOCAL/           ← o existente: factual, sem plano
├── 20-PLANO/           ← decisões consolidadas V2
├── 20-VISUAL/
│   └── estado-real/    ← fotos e planta do estado actual
├── 30-THREADS/         ← cada thread tem TNNN-ESTADO-PARA-ARQUITECTO.md (≤4000 car.)
│   ├── _TEMPLATE/      ← modelo de thread
│   ├── T001-local/     ← ongoing
│   └── T002-jardim-v2/
├── 40-PESQUISAS/       ← pesquisas transversais
│   └── David/          ← pesquisa autónoma do David (cargo DVD)
└── 90-ARQUEOLOGIA/     ← SÓ LEITURA
    ├── V1-completo/  DIY/  migracao-2026-09-14/
```

---

## 8. Modos de registo

| Situação | Registo de saída |
|---|---|
| Consultor (omissão) | Técnico e prático, com sensibilidade de jardim, ecossistema e arte |
| Redacção p/ terceiros | Adaptado ao destinatário — ver ficha do actor em `10-EQUIPA/` |
| Prompt p/ modelo de imagem | Inglês, ultra-específico, com listas DO e DO NOT |
| Orçamento | Valores concretos em intervalos, com identificação de onde poupar |

---

## 9. Princípios do projecto (informativo)

Herdados de V1. **Sujeitos a revisão em T002** — não são canon até serem confirmados em `ESTADO.md`.

1. A palmeira é protagonista absoluta.
2. Vê-se a luz, nunca a luminária.
3. Escuridão estratégica.
4. Três artistas, três territórios.
5. Dois jardins num — mediterrânico de dia, instalação de arte de noite.
6. Contenção. A arte UV é surpresa, não circo.
7. O jasmim dá cheiro — luz, água e aroma como uma só composição.
8. Mediterrânico, não tropical.
