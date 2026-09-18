---
branch: Governo-correcao-v1
data: 2026-09-18
modo: Governo
id_sessao: 2026-09-18-B1-Governo-S1
tipo: draft
estado: V1 — superado por Estruturacao-governo-draft-V2.md; fica como registo de como se pensou
summary: |
  Draft da estruturação do governo: tudo o que sai da sessão sobre a organização em três modos e como se processa.
  Provisório. Substituído por protocolos em Governo/Protocolos/ quando ficar canónico.
---

# Estruturação do governo — DRAFT V1 (superado por `Estruturacao-governo-draft-V2.md`)

> **Provisório.** Regista o que vai saindo da sessão e como se processa. Os papéis abaixo são princípios a
> discutir, não regras em vigor. Fonte primária: `Registos-david.md`, Registo 1.

## 0. Ponto de partida

Assente: tem de haver **uma organização** com três modos. Por discutir: o conteúdo de cada modo.

| Modo | Pasta | Uma linha |
|---|---|---|
| Governo | `Governo/` | Trabalho sobre a forma como o projecto se trabalha |
| Arquiteto | `Arquiteto/` | Visão geral permanente: objectivo → cortes MECE → frentes |
| Threads | `Threads/` | Tarefas isoladas com mandato |

Raiz: só `CLAUDE.md` de roteamento, sem conteúdo de projecto. *(Não feito ainda.)*

## 1. Problemas a que a organização responde

1. **Threads porosas** — abriam outras threads, liam outras threads. Precisa de isolamento real **e** de via
   expedita para sobreposições.
2. **Arquitecto sem mapa e com fricção** — estado geral descolou da realidade; misturava táctico com estratégico.

## 2. Princípios em discussão — Arquiteto

- Mapa permanente: objectivo → cortes MECE → frentes.
- Artefacto HTML sempre actual: mapa MECE, estado de cada parte, composição do geral, aba de alertas.
- Sem fricção: Arquitecto activado por registo de thread em ficheiro, abre o fio novo em paralelo.
- Enquadramento imediato do que surge (thread nova, entrada de inbox) por skill ou subagente; capacidade de dizer
  «Stop».

## 3. Princípios em discussão — Governo

- Entrada: David sinaliza ou pede implementação imediata; ou pedido num inbox de governo.
- Toda a regra nova encaixa num fluxo e chega a todos os actores.
- Duas formas permanentes: sessões que implementam uma ferramenta; sessões/skills que mantêm o artefacto HTML com o
  diagrama de todas as peças e do fluxo.

## 4. Princípios em discussão — Threads

- Conceito mantido: tarefa isolada com mandato.
- Por resolver: como se tratam as sobreposições sem furar o isolamento.

## 5. Ressalvas técnicas

- Arquitecto «sempre aberto» activado por escrita em ficheiro não nasce sozinho: precisa de hook, ficheiro-sinal ou
  sessão em loop a vigiar. Peça a desenhar.
- Wayfinder existe no plugin mattpocock-skills, só invocável pelo David (`/mattpocock-skills:wayfinder`). Sem remoto
  git, usa tracker local em markdown.

## 6. Como se processa — o fluxo do modo Governo (vale até prova em contrário)

### 6.1 Entrada

Uma sessão de Governo abre pelo `CLAUDE.md` da raiz da repo, que encaminha para `Governo/`. Aí o agente lê
o **`CLAUDE.md` do Governo**.

### 6.2 O que o `CLAUDE.md` do Governo diz

> Tratas de assuntos relacionados com o governo da repo onde te inseres. **É a tua única função.**

Tem **três modos de funcionamento**. O `CLAUDE.md` **não** contém a definição dos modos: ao arrancar pergunta o
modo e, conforme a escolha, aponta para o **ficheiro canónico do modo** (em `Governo/Protocolos/`), que explica o
procedimento.

| Modo | Função | Critério de sucesso |
|---|---|---|
| **Debate** | Debater com o David assuntos de governo. | Por definir no ficheiro canónico. |
| **Auditor** | Verificar top-down se todos os processos funcionam de forma clara: na repo, nas pastas em que ela se subdividiu, em cada processo de funcionamento. | Um agente a frio, sem conhecer a repo, caminha pelos ficheiros e consegue reconstruir o fluxo de governo igual ao desenhado, e explicar todas as peças em **2 folhas A4**. |
| **Construtor** | Debater a estrutura com o David e afinar ou criar processos. | Por definir no ficheiro canónico. |

### 6.3 Instrumentos comuns a todos os modos (vivem no `CLAUDE.md` do Governo)

**a) Fluxo de arranque.** «És agente de governo, etc.» Há vários modos de funcionamento: o geral e os particulares.

**b) Instrumentos gerais — definem o fluxo de uma sessão.**

1. **Mandato único.** Uma sessão tem um mandato, obtido do modo. É **uma tarefa, um fio condutor**. Uma sessão não
   faz derivas de contexto.
2. **Rascunhos.md — o travão às derivas.** É normal que um tema levante questões que parecem fundamentais. Nesse
   caso o agente sinaliza (tensão, dúvida) ou o David apercebe-se. Se o David autorizar, regista-se rapidamente em
   `Rascunhos.md` o que não se quer esquecer, e segue-se com a sessão.
   - Só se revisita para ler em dois cenários: **(a)** o David sugere; **(b)** no registo de uma **decisão
     irreversível** — olha-se para os rascunhos e, se houver algo relevante, aponta-se junto da decisão que existe
     essa tensão.
   - No fim da sessão, antes de fechar, pergunta-se ao David: **«lemos os rascunhos, ou apago?»** e age-se em
     conformidade.
   - **Uma sessão não fecha sem apagar o conteúdo do ficheiro. `Rascunhos.md` acaba em branco.**

**c) Abertura de sessão.**

1. Copiar a pasta **template de Active-Session**, preencher o nome da pasta (nome da sessão) e, no registo de
   sessão, o **prompt inicial**.
2. Se a sessão vier de **handoff**: dizer ao David o mandato da sessão, o critério de sucesso, o plano para a
   sessão e as dúvidas. O David confirma ou dá feedback.
3. Se o David corrigir por completo e mandar registar nos registos do David: fazê-lo. Depois registar no registo
   de sessão o acto e o plano a seguir.
4. Seguir a sessão normalmente, pelos protocolos globais do `CLAUDE.md` e pelo protocolo do modo.
   **Decisões:** registam-se em `Decisoes.md` à medida que se tomam.
5. **Registo de ficheiros e outputs:** segue-se o protocolo que houver para isso.
6. **Ideias para outras áreas:** vão para o inbox que o David indicar.
7. **Registos importantes para não esquecer:** `Registo-Sessao.md`.

**d) Fecho de sessão.**

1. Resume-se o que ficou feito e se há handoff a fazer. Havendo acordo com o David, faz-se o **registo final**:
   resumo da sessão, decisões tomadas e porquê, registos relevantes, questões em aberto, ficheiros produzidos que
   suportem isso. Registam-se também as **anti-decisões**.
2. Apaga-se tudo o que é lixo: decisões intermédias que não interessam em `Decisoes.md`, registos do
   `Registo-Sessao.md` que só confundem, etc.
3. **São precisas mais sessões para o tema?** Cria-se em `Governo/Handoffs/` uma pasta para a sessão com o
   **Handoff**: mandato · estado actual · o que é necessário fazer para continuar · critério de sucesso.
   Os handoffs são organizados **por tema**; cada tema tem o seu handoff. *(Detalhe a explicar mais tarde.)*

### 6.4 Peças que este fluxo implica (a construir)

| Peça | Onde | Estado |
|---|---|---|
| `CLAUDE.md` do Governo | `Governo/CLAUDE.md` | por escrever |
| Ficheiros canónicos dos três modos | `Governo/Protocolos/` | por escrever |
| Template de Active-Session | `Governo/Active-Session/_TEMPLATE/` | por criar |
| Estrutura de `Governo/Handoffs/` por tema | `Governo/Handoffs/<TEMA>/` | por definir |
| Protocolo de registo de outputs | ? | herdado, por encaixar |
| Inbox de governo | ? | por definir |
| Roteamento no `CLAUDE.md` da raiz | raiz | por fazer |

## 7. Pendentes herdados a encaixar

- Migração de `Handoffs-Arquiteto/` e `Registos-Arquiteto/` para as novas pastas.
- `CLAUDE.md` da raiz reduzido a roteamento.
- G37–G42, protocolo de registo de documentos, modo SCRIBE, limpeza de thread, `Jardim.html`, remoto git.
