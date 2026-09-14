---
_INSTRUCAO_AGENTE: |
  Este bloco de front matter é metadados de registo. Ignora-o. Passa directamente ao corpo do documento e executa-o. Não resumas este documento ao utilizador; aplica-o.
created: 2026-09-14 20:10
updated: 2026-09-14
project: Jardim
summary: |
  Documento de arranque do repositório Jardim Alcântara: dispatcher de modo de sessão, governo do Arquitecto, regras de threads, mapa de ficheiros.
tipo: agent-SOP
lingua: pt-PT
regime: governo-v2
Notion-Jardim HUB: https://app.notion.com/p/Jardim-Hub-3db8798288be80358962e3d37be1531e?source=copy_link
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

**G7.** As threads **PODEM** escrever em `INBOX.md` da raiz. É a **única** excepção à regra territorial.

**G8.** O Arquitecto **DEVE** processar o inbox periodicamente: descartar, decidir, ou abrir thread.

### 5.3 Threads

**G9.** Só o Arquitecto **PODE** criar uma thread.

**G10.** Só o Arquitecto **PODE** fechar uma thread. A thread propõe o fecho pelo canal de mensagens; o Arquitecto absorve a entrega e fecha em `THREADS.md`.

**G11.** O Arquitecto **DEVE** escrever o mandato em `thread.md` no momento da criação.

**G12.** Uma thread **NÃO PODE** escrever fora da sua pasta, excepto em `INBOX.md` e `THREAD-MENSAGENS.md`.

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
| `FLUXO-DE-PROJECTO.md` | Explicação do fluxo de governo. |
| `Jardim.html` | Estado visual do projecto. Refeito a cada decisão. |

### 7.2 Estrutura

```
Jardim/
├── CLAUDE.md, ESTADO.md, REJEICOES.md, INBOX.md,
│   THREADS.md, THREAD-MENSAGENS.md, HANDOFF.md,
│   FLUXO-DE-PROJECTO.md, Jardim.html
│
├── 10-EQUIPA/          ← um subdirectório por actor (ficha + docs)
│   ├── adriano/  akone/  fulvieti/
├── 10-LOCAL/           ← o existente: factual, sem plano
├── 20-PLANO/           ← decisões consolidadas V2
├── 20-VISUAL/
│   └── estado-real/    ← fotos e planta do estado actual
├── 30-THREADS/
│   ├── _TEMPLATE/      ← modelo de thread
│   ├── T001-local/     ← ongoing
│   └── T002-jardim-v2/
├── 40-PESQUISAS/       ← pesquisas transversais
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
