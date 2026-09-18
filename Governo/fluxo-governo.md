---
created: 2026-09-18
branch: Governo-correcao-v1
tipo: fluxo
estado: provisório
versao: V2.1
summary: |
  Diagramas dos fluxos de governo ditados pelo David a 2026-09-18: organização em três modos, entrada numa sessão
  de Governo, ciclo de vida de uma sessão, Rascunhos, modos de Governo e criação de modo novo, estrutura de pastas.
---

# Fluxo do Governo — diagramas

**V1** registada a 2026-09-18 (aprovada pelo David «bastante bem por agora»). **V1.1**: afinação do arranque
(Governo-Enquadramento.md, inbox por modo). **V1.2**: «modo ou vista geral», handoff como mandato, dois tipos de
handoff, inbox como semente de tema, âncora de regras. **V1.3**: bloco Propósito · Resultado mínimo · Estado no Registo-Sessao; template de Active-Session. **V1.4**: Arvore.md por sessão.
**V2** (fecho da S1): raiz pergunta GOVERNO/PROJETO · dois modos (Geral, Auditor) · três temas do Geral ·
protocolos e Raiz-Teste só na raiz do Governo · texto de arranque no fecho. **V2.1**: quadro `TEMAS.md` + `TEMA.md` por tema.

> Provisório. Fonte: `Modos-Governo/Geral/Active-Session/2026-09-18-B1-Governo-S1/Registos-david.md` (Registos 1 e 2)
> e `Estruturacao-governo-draft.md`. Os papéis de Arquiteto e Governo em §1 são princípios a discutir.

## 1. A organização — três modos

```mermaid
flowchart TB
    R["CLAUDE.md da raiz<br/>só roteamento · regras gerais<br/>não sabe o que é o projecto"]
    R --> G["GOVERNO<br/>trabalho sobre a forma<br/>como o projecto se trabalha"]
    R --> A["ARQUITETO<br/>visão geral permanente<br/>objectivo → cortes MECE → frentes"]
    R --> T["THREADS<br/>tarefas isoladas<br/>com mandato"]

    A -. "abre / enquadra" .-> T
    T -. "regista em ficheiro → activa" .-> A
    G -. "regras chegam a todos os actores" .-> A
    G -. "regras chegam a todos os actores" .-> T

    A --- AH["artefacto HTML<br/>mapa MECE · estado de cada parte<br/>composição do geral · aba de alertas"]
    G --- GH["artefacto HTML<br/>diagrama de todas as peças<br/>como tudo flui"]
```

**Princípios a discutir (não canónicos):**
- Arquiteto sempre aberto em paralelo, activado quando uma thread regista algo; abre logo o fio novo. Enquadra o que surge (thread nova, inbox) por skill ou subagente; diz «Stop» quando tem de ser.
- Governo tem duas formas permanentes: sessões que implementam uma ferramenta; sessões ou skills que mantêm o artefacto HTML do fluxo.
- Threads: isolamento real, mais via expedita para sobreposições (por resolver).

## 2. Entrada numa sessão de Governo (V2)

```mermaid
flowchart TB
    D["David abre sessão"] --> R["CLAUDE.md raiz<br/>GOVERNO ou PROJETO?"]
    R -- "PROJETO" --> CP["CLAUDE-projeto.md<br/>(Arquitecto · Threads)"]
    R -- "GOVERNO" --> GC["Governo/CLAUDE.md"]
    GC --> E["Protocolos/Governo-Enquadramento.md<br/>função única · regra inegociável · âncora"]
    E --> I["Index-Modos-Governo.md<br/>Geral · Auditor"]
    I --> Q{"Modo? ou Vista geral?"}
    Q -- "vista geral" --> VG["Geral/TEMAS.md: temas · estado ·<br/>último handoff · por fazer<br/>+ inboxes"]
    VG --> ESC["David escolhe"]
    Q -- "modo" --> MD["modo"]
    ESC --> MD
    MD --> M{"mandato = ?"}
    M -- handoff --> H["Handoff<br/>autocontido · enquadrado"]
    M -- inbox --> IB["abrir tema · passar a outro modo ·<br/>decidir o que implementar"]
    M -- prompt --> P["tema novo · outro"]
    H & IB & P --> ENTRA["entra no modo → §3"]
```

## 3. Ciclo de vida de uma sessão de Governo

```mermaid
flowchart TB
    subgraph ABERTURA
        A1["copiar template de Active-Session<br/>nome da pasta = nome da sessão"] --> A2["Registo-Sessao.md ← prompt inicial<br/>+ bloco PROPÓSITO · RESULTADO MÍNIMO · ESTADO<br/>Arvore.md ← objectivo na raiz"]
        A2 --> A3{"vem de handoff?"}
        A3 -- sim --> A4["dizer ao David: mandato ·<br/>critério de sucesso · plano · dúvidas"]
        A3 -- não --> A6
        A4 --> A5{"David confirma?"}
        A5 -- "corrige por completo" --> A5b["registar em Registos-david.md<br/>+ acto e novo plano em Registo-Sessao.md"]
        A5 -- confirma --> A6["seguir a sessão"]
        A5b --> A6
    end

    subgraph SESSÃO
        A6 --> S1["Governo/CLAUDE.md + Protocolos/<br/>+ Mandato-do-Modo.md"]
        S1 --> S2["Decisoes.md ← decisões à medida"]
        S1 --> S3["outputs → protocolo de registo<br/>que houver"]
        S1 --> S4["ideias de outras áreas → INBOX.md<br/>do modo (sem modo: Geral)"]
        S1 --> S5["não esquecer → Registo-Sessao.md"]
        S1 --> S6["deriva? → Rascunhos.md<br/>(ver §4)"]
        S1 --> S9["após cada tarefa e feedback:<br/>olhar Arvore.md · onde estou?"]
        S1 --> S8["mandato mudou? → reescrever<br/>bloco Propósito/Resultado/Estado"]
        S1 --> S7["âncora: «serve os processos<br/>ou hiperespaço?»<br/>Governo-Enquadramento.md"]
    end

    subgraph FECHO
        S1 --> F1["resumir o que ficou feito<br/>há handoff?"]
        F1 --> F2{"acordo com David?"}
        F2 -- sim --> F3["registo final: resumo · decisões e porquê ·<br/>anti-decisões · registos relevantes ·<br/>questões em aberto · ficheiros produzidos"]
        F3 --> F4["apagar lixo: decisões intermédias,<br/>registos que confundem"]
        F4 --> F5["«lemos Rascunhos, ou apago?»<br/>→ Rascunhos.md fica em branco"]
        F5 --> F6{"precisa de mais sessões?"}
        F6 -- sim --> F7["Handoffs/&lt;Tema&gt;/Handoff-Sn.md<br/>+ actualizar TEMA.md e TEMAS.md"]
        F6 -- não --> F8
        F7 --> F8["commit"]
        F8 --> F9["texto de arranque da<br/>sessão seguinte, no chat"]
    end
    F1 -. "relê âncora" .-> S7
```

## 4. Rascunhos.md — o travão às derivas

```mermaid
flowchart LR
    T["tema levanta questão<br/>que parece fundamental"] --> S["agente sinaliza tensão/dúvida<br/>ou David apercebe-se"]
    S --> P{"David autoriza<br/>registar?"}
    P -- sim --> W["escrever rapidamente<br/>em Rascunhos.md"] --> C["continuar a sessão<br/>sem deriva"]
    P -- não --> C

    W -. "só se lê em 2 cenários" .-> L1["David sugere"]
    W -. "só se lê em 2 cenários" .-> L2["ao registar decisão irreversível:<br/>há tensão relevante? → apontar<br/>junto da decisão"]
    W -. "fim de sessão" .-> E["«lemos, ou apago?»<br/>→ ficheiro acaba em branco"]
```

## 5. Modos e temas (V2)

```mermaid
flowchart TB
    I["Index-Modos-Governo.md"]
    I --> Ge["GERAL · activo<br/>tudo o que é governo · vista geral"]
    I --> Au["AUDITOR · por definir<br/>um mandato: simples e coerente?<br/>sucesso: 2 A4 a frio"]
    Ge --> T1["Handoffs/Meta-Governo/<br/>o próprio governo"]
    Ge --> T2["Handoffs/Governo-do-Projeto/<br/>regime Arquitecto · Threads"]
    Ge --> T3["Handoffs/Auditoria/<br/>o que vai ao Auditor"]
    T3 -.-> Au
    N["modo novo (só se o David pedir)"] --> N1["linha no índice → copiar<br/>Pasta-Modo-Template/ → Data-Setup-NomeModo"]
```

Um tema é uma pasta em `Handoffs/<Tema>/` com **`TEMA.md`** (mandato fixo · estado · por fazer) e os handoffs.
O quadro de todos os temas é **`Geral/TEMAS.md`**: é o que se lê quando o David pergunta «o que temos?».

## 6. Estrutura de pastas (V2)

```mermaid
flowchart LR
    Rz["raiz da repo"] --> C0["CLAUDE.md<br/>GOVERNO ou PROJETO"]
    Rz --> CP["CLAUDE-projeto.md<br/>regime antigo, intacto"]
    Rz --> Gv["Governo/"]
    Gv --> GC["CLAUDE.md"]
    Gv --> RM["README.md<br/>como funciona + fluxo"]
    Gv --> FG["fluxo-governo.md"]
    Gv --> PR["Protocolos/<br/>Governo-Enquadramento ·<br/>Arvore-da-Sessao · Handoff-Template"]
    Gv --> RT["Raiz-Teste/<br/>laboratório da raiz"]
    Gv --> MG["Modos-Governo/"]
    MG --> IX["Index-Modos-Governo.md"]
    MG --> TP["Pasta-Modo-Template/"]
    MG --> Ge["Geral/"]
    MG --> Au["Auditor/"]
    Ge & Au & TP --> MM["Mandato-do-Modo.md · INBOX.md"]
    Ge & Au & TP --> AS["Active-Session/<br/>Sessao-Template/ · &lt;sessão&gt;/"]
    Ge --> TM["TEMAS.md · quadro"]
    Ge & Au & TP --> HO["Handoffs/&lt;Tema&gt;/<br/>TEMA.md · YYYY-MM-DD-Handoff-Sn.md"]
```

## 7. Lacunas (V2)

| # | Lacuna | Onde |
|---|---|---|
| L2 | Auditor por definir: sessão `Data-Setup-Auditor` | §5 |
| L4 | Protocolo de registo de outputs por definir | §3 |
| L7 | Mecanismo de activação do Arquiteto por escrita de ficheiro | §1 (Governo-do-Projeto) |
| L8 | Via expedita para sobreposições entre threads | §1 (Governo-do-Projeto) |
| L10 | `Arquiteto/` e `Threads/` na raiz estão vazias; o regime do projecto continua em `CLAUDE-projeto.md` e `30-THREADS/` | §6 (Governo-do-Projeto) |
| L11 | `Handoffs-Arquiteto/` e `Registos-Arquiteto/` na raiz: migrar ou manter | §6 (Governo-do-Projeto) |

Fechadas em V2: L1 (Governo/CLAUDE.md), L3 (template), L5 (roteamento), L6 (Raiz-Teste e Protocolos), L9 (vista geral = listagem).
