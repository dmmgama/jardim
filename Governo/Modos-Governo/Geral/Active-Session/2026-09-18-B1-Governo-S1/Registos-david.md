---
branch: Governo-correcao-v1
data: 2026-09-18
modo: Governo
id_sessao: 2026-09-18-B1-Governo-S1
tipo: registos-david
summary: |
  O que o David disse nesta sessão, estruturado. Registo 1: diagnóstico dos dois problemas do projecto e organização
  alvo em três modos (Governo, Arquiteto, Threads).
---

# Registos do David — 2026-09-18-B1-Governo-S1

## Registo 1 — Diagnóstico e organização alvo

**Nota de estatuto.** Os papéis do Arquiteto e do Governo descritos abaixo são **princípios ainda a discutir**, não
definição canónica. O que fica assente é que **tem de haver uma organização** com três modos.

### 1. Princípio de método

A estruturação não tem de ficar toda feita antes de haver trabalho produtivo. Segue-se o wayfinder, mas por
partes, à medida que a organização se fixa.

### 2. Os dois problemas do projecto

**Problema 1 — Threads porosas.**
- Threads abertas acabavam a abrir outras threads, ou porque o David pedia, ou porque de repente fazia sentido.
- Threads liam material de outras threads. Não devia acontecer: mina a tarefa isolada.
- Mas as sobreposições existem, e tem de haver uma forma expedita de as resolver.

**Problema 2 — O Arquitecto.**
A figura existe para ter a visão geral de tudo sem se perder em detalhes. Falhou em dois pontos:

- **a) Fricção.** Estar numa sessão de thread, perceber que ela levanta problemas que devem criar outros caminhos,
  parar, abrir o Arquitecto, ele avaliar tudo. Resultado: atalhos, e o estado geral ficou completamente à balda,
  sem acompanhar a realidade. Tem de se criar um mecanismo sem fricção. Ideia: uma sessão de Arquitecto sempre
  aberta, em paralelo com as das threads; quando uma thread regista algo num ficheiro, o Arquitecto é activado e
  abre logo esse fio, enquanto o David continua o trabalho em paralelo.
- **b) Sem mapa.** O Arquitecto não tem forma estruturada de ver o mapa geral. Por isso confunde e mistura registos
  de decisões tácticas com outros. Precisa de:
  - estrutura;
  - forma expedita de criar o que é pedido (ex.: surge uma thread, e ao mesmo tempo há um skill ou subagente
    lançado que enquadra logo o que surgiu);
  - o mesmo automatismo para o inbox: algo que veja em permanência o quadro geral e faça «Stop» quando tem de fazer.

### 3. O que é o Arquiteto (princípio a discutir)

O mais relevante de tudo: **tem de haver em permanência um mapa do que se está a fazer.**

- Há um objectivo.
- A partir dele traçam-se um ou mais cortes MECE.
- Daí abrem-se frentes.
- Tem de haver sempre um **artefacto HTML** com o mapa MECE, o estado de cada parte e como o geral se está a compor,
  e uma **aba de alertas** para rever o mapa.

Isto é o Arquiteto.

### 4. O que é o Governo (princípio a discutir)

- Quando o David vê que há coisas necessárias a implementar para tornar tudo melhor, abre o modo Governo e sinaliza
  ou pede que algo seja logo posto em prática. Tem de haver forma de o fazer.
- Exemplo: o protocolo de registo de documentação criado recentemente tem de encaixar num fluxo e garantir que todos
  os actores passam a agir assim. Em alternativa, o David lança um pedido num inbox para isso.
- O Governo tem em permanência **duas formas**:
  1. sessões que só implementam uma ferramenta;
  2. sessões ou skills que garantem que há sempre um **artefacto HTML** com o diagrama de todas as peças, para que
     seja claro como tudo flui.

### 5. O que é a Thread

O modo das tarefas isoladas. Conceito mantido.

### 6. Plano de acção imediato

- Criar três pastas no repositório: `Governo/`, `Arquiteto/`, `Threads/`.
- Na raiz fica só um `CLAUDE.md` que faz roteamento ao arrancar a sessão. Regras gerais, nada sobre o que o
  projecto é ou deixa de ser. **Ainda não se faz** (o CLAUDE.md).
- Dentro de `Governo/`: `Raiz-Teste/`, `Protocolos/`, `Handoffs/`, `Active-Session/`.
- Em `Active-Session/`: pasta com o nome desta sessão, com `Registo-Sessao.md`, `Registos-david.md`,
  `Rascunhos.md`, `Decisoes.md` e o provisório `Estruturacao-governo-draft.md`.
- `Registo-Sessao.md`: front matter com branch, data, modo, ID de sessão, sumário; campos Mandato inicial (prompt e
  ficheiros lidos), Acções tomadas, Informações importantes, Próximos passos, Documentos produzidos.
- `Estruturacao-governo-draft.md`: regista tudo o que sair daqui e como se processa. O David dita a seguir.

## Registo 2 — O fluxo do modo Governo (vale até prova em contrário)

Ditado pelo David. Transcrito de forma estruturada em `Estruturacao-governo-draft.md`, §6, que é a versão de
trabalho. Pontos essenciais:

- Sessão de Governo abre pelo `CLAUDE.md` da raiz e lê o `CLAUDE.md` do Governo. Função única: governo da repo.
- Três modos: **Debate**, **Auditor**, **Construtor**. O `CLAUDE.md` não os define; pergunta o modo e aponta para o
  ficheiro canónico do modo.
- Critério de sucesso do Auditor: agente a frio reconstrói o fluxo de governo pelos ficheiros e explica as peças em
  2 folhas A4.
- Instrumentos comuns: mandato único por sessão; `Rascunhos.md` como travão às derivas, lido só a pedido do David
  ou ao registar decisão irreversível, e apagado antes do fecho; abertura por cópia do template de Active-Session;
  handoff apresentado ao David com mandato, critério de sucesso, plano e dúvidas; decisões em `Decisoes.md`;
  ideias para outras áreas no inbox indicado; fecho com registo final, limpeza de lixo, anti-decisões, e handoff
  por tema em `Governo/Handoffs/` se forem precisas mais sessões.

## Registo 3 — Modos, V1 do fluxo e afinações do arranque

- Estamos só a definir a lógica do governo. Modos em `Modos-Governo/`, cada um com pasta a partir de
  `Pasta-Modo-Template/` (Active-Session, Raiz-Teste, Protocolos, Handoffs, Mandato-do-Modo, INBOX). Geral é o modo
  por omissão. Modo novo: linha no índice, cópia do template, sessão `Data-Setup-NomeModo`.
- `fluxo-governo.md` aprovado como V1.
- Afinação do arranque: depois do roteamento, a sessão lê primeiro `Governo-Enquadramento.md` (texto ditado pelo
  David, transcrito nesse ficheiro), depois o índice de modos, depois o mandato da sessão, e entra no modo.
- INBOX: uma por modo; sem modo, cai na do Geral.
- A seguir: handoff.

## Registo 4 — Vista geral, handoff, inbox, âncora

- `CLAUDE.md` da raiz pergunta: **modo? ou vista geral?** Vista geral dá a lista de handoffs por modo e de inboxes
  por modo, para escolher quando não se sabe o que se quer. Escolhido um, manda para o modo, lê o enquadramento, lê
  o handoff pedido.
- Handoff: **autocontido** (tarefa em que não precisa de saber nada, só como agir) ou **enquadrado** («tarefa X para
  fazer Y»). No Geral: tema novo qualquer, handoff específico, enquadrado ou outro.
- Começar só com uma base; não definir já tudo.
- Tem de haver um protocolo que em qualquer modo ou sessão veja um ficheiro de regras, para garantir que os fluxos
  estão claros e o que produz encaixa. Serve para **levar a sessão à terra**: «o que estou a fazer serve os
  processos, ou já vou para o hiperespaço?».
- Inbox: para abrir um tema novo que alguém deixou. Gera um fio de handoffs e uma tarefa específica; ou passa-se a
  entrada para a inbox de outro modo; ou decide-se do que lá está o que faz sentido implementar.

## Registo 5 — Teste: o que está a sessão a fazer?

Perguntou o David: o que está esta sessão a fazer, e qual é o resultado mínimo para atingir o propósito inicial?
Isso tem de estar constantemente claro e registado nos ficheiros básicos, tanto nos fluxos de Governo como nos
fluxos do projecto. Resposta: bloco fixo «Propósito · Resultado mínimo · Estado» no topo do Registo-Sessao.md.

## Registo 6 — Falta uma âncora simples: a árvore da sessão

A sessão começou com um objectivo (definir a estrutura: governo, arquitetura, threads). Foram precisos mecanismos
para o agente funcionar sem se perder; começou-se a criá-los; agora estamos embrulhados nisso e as derivas não se
registaram. Ficheiro base para qualquer sessão em qualquer lado: **diagrama da sessão**. Começa com o objectivo
formulado. Foi preciso parti-lo? Fica a árvore: objectivo/problema inicial em 2 linhas a apontar para o ficheiro
de origem. Fez-se uma tarefa: ramo para baixo. A tarefa dividiu-se: ramos paralelos, e segue-se no ramo em que se
trabalha. Depois da tarefa e do feedback: ver o diagrama de novo para saber onde se está. E por aí fora.

## Registo 7 — Raiz-Teste, Protocolos, simplificação e fecho

- **Raiz-Teste** é laboratório: constrói-se lá a raiz da repo antes de aplicar; quando se mexe no que vai para a raiz
  e se quer ver o fluxo. Só na raiz do Governo, não em cada modo.
- **Protocolos** ficam na raiz do Governo. Os modos servem só para isolar trabalho. Junto dos protocolos há um ficheiro
  que explica como funciona o governo da repo e o fluxo; os protocolos são o que se aplica ao fluxo, os instrumentos
  base que se podem afinar.
- Texto de arranque no fecho: sim.
- **Fecho da sessão:** renomear `CLAUDE.md` da repo para `CLAUDE-projeto.md`; novo `CLAUDE.md` pergunta «governo ou
  projeto»; projeto manda para o que já existe; governo manda para `Governo/CLAUDE.md`, que corre o fluxo definido.
- **Simplificar modos:** Geral (trata de tudo o que é governo) e Auditor (um mandato: ver se tudo está simples e
  coerente). No Geral: o David fala ou vê handoffs e inboxes; consoante o que se for fazer, divide tarefas e cria
  tickets que gere, para não haver confusão: os problemas e onde arrumou. Três temas: **Meta-Governo** (isto),
  **Governo-do-Projeto** (o Arquitecto etc.), **Auditoria**. Função de vista geral.
- Objectivo: simplificar tudo.

## Registo 8 — Controlo dos temas

Faltam duas coisas: (1) o Geral tem de ter o controlo dos temas que há e de como se organizam: o David abre e ele
diz «temos isto e aquilo»; um sítio para registar por tema o que está por fazer, triado da inbox; (2) um sistema
definido para os handoffs: em cada coisa que se abra tem de haver **mandato, estado e handoff**, e o Geral tem de
saber sempre para que serve cada coisa. → `Geral/TEMAS.md` (quadro) + `TEMA.md` em cada tema.
