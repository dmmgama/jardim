---
created: 2026-09-18
thread: T005
tipo: entrega
estado: PROPOSTA — nada em vigor, aguarda o Arquitecto
summary: |
  Entrega do protocolo de registo de documentos. Três ficheiros: as instruções,
  o template e um draft com as regras aplicadas a tudo o que existe no repositório.
  Nada disto está em vigor — são propostas para o Arquitecto ratificar, corrigir
  ou rejeitar. O achado que justifica a entrega: o draft catalogou 58 documentos
  contra 9 no registo em vigor, ou seja 49 documentos que não estavam em índice nenhum.
---

# Protocolo de registo de documentos — entrega da T005

> ⚠ **NADA DISTO ESTÁ EM VIGOR. São propostas.**
>
> **A raiz ficou sem `REGISTO-DOCUMENTOS.md`** — o que lá estava foi movido para aqui a
> 2026-09-18, por instrução do David. **Isto é deliberado:** o antigo não é canon, e deixá-lo na
> raiz fazia-o parecer governo em vigor.
>
> **Consequência a resolver, e é imediata:** as regras G23–G29 do `CLAUDE.md` e as T18–T23 das
> threads **mandam escrever num ficheiro que já não está onde dizem**. Até o Arquitecto decidir,
> **o registo de fim de sessão não tem destino válido.**
>
> **Se o protocolo novo for ratificado:** o `REGISTO-DOCUMENTOS-ANTIGO.md` vai para
> `90-ARQUEOLOGIA/`, o template gera o registo definitivo na raiz, e as regras são reescritas.

---

## 1. O problema

O projecto produz documentos a um ritmo alto e **não sabia o que tinha**. O
`REGISTO-DOCUMENTOS.md` foi criado a 2026-09-17 com uma estrutura simples, por secção temática.

**O draft desta entrega catalogou 58 documentos. O registo em vigor tinha 9.**

Isso não é uma melhoria de formato — **são 49 documentos que não estavam em índice nenhum.**
Quase todo o trabalho do projecto estava fora de qualquer catálogo, incluindo material de threads
fechadas e pesquisa do David.

**Porque é que isto importa, com um caso real:** a 2026-09-18 descobriu-se que uma pesquisa do
David — sobre sistemas de cobertura ajardinada, com espessuras FLL e cargas — **respondia à
questão que a T005 tinha acabado de sinalizar à T004 como urgente.** Esteve disponível durante
toda a fase 1 sem ninguém a abrir. **O custo de não catalogar não é desarrumação: é trabalho
repetido e decisões tomadas sem informação que já existia.**

---

## 2. Os ficheiros

| # | Ficheiro | O que é | Para quê |
|---|---|---|---|
| 1 | [[REGISTO-DOCUMENTOS-INSTRUCOES]] | **A lógica.** 540 linhas: estrutura, as oito colunas com formato exacto, vocabulário de tipos, mecânica dos índices, resolução do «Supported», sete casos difíceis, regras de higiene, e **nove decisões de desenho assinaladas para revisão** | **Ler primeiro.** É o documento que decide como tudo funciona |
| 2 | [[REGISTO-DOCUMENTOS-TEMPLATE]] | **O esqueleto.** 315 linhas: front matter, os quatro índices do topo, os quatro níveis de Dono, e um bloco de sessão preenchido com dados fictícios óbvios | Copiar quando se criar o registo definitivo |
| 3 | [[REGISTO-DOCUMENTOS-DRAFT]] | **As regras aplicadas ao real.** 545 linhas, 58 documentos catalogados, 27 dependências registadas | **A prova.** Serve para ver se as regras resistem aos dados, antes de substituir o que está em vigor |

| 4 | [[REGISTO-DOCUMENTOS-ANTIGO]] | **O que estava em vigor até 2026-09-18.** 9 documentos, estrutura por secção temática. **Movido da raiz para aqui** por instrução do David | **Referência histórica.** Se o protocolo novo for ratificado, **isto vai para `90-ARQUEOLOGIA/` — não é canon** |

**Ordem de leitura recomendada:** 3 → 1 → 2. O draft mostra o resultado; as instruções explicam
porque é assim; o template serve para executar.

---

## 3. A estrutura proposta, em resumo

**Topo:** descrição · índice geral · índice de Donos · índice por Tipo de documento.

**Corpo, em quatro níveis de Dono:** Arquitecto · Threads (subheading por thread) · David · Outros.
Dentro de cada thread, os registos **por sessão**, cada uma com sumário breve e tabela.

**Oito colunas:** `Tipo` (com tag, para agregar) · `Data` · `Dono` · `Sessão` · `Título` (wikilink) ·
`Ficheiros` (só o nome, mas clicável) · `Sumário` (2 linhas) · `Supported`.

**A decisão de desenho central — o «Supported».** A coluna descreve **quem depende do documento**,
o que só se sabe depois. Como o registo é *append only*, mantê-la actualizada obrigaria a editar
linhas antigas. **Solução adoptada:** a coluna nasce preenchida uma vez (quase sempre `—`) e
congela; toda a dependência descoberta depois vai para uma secção **`## Dependências entre
documentos`** no fim — **a única secção editável do ficheiro**.

O argumento: *uma excepção «só numa coluna» é indistinguível, na prática, de licença para editar
linhas antigas.* Confinar a mutabilidade a uma secção com nome próprio torna a excepção **visível
em vez de dispersa**.

---

## 4. ⚠ O que tem de ser resolvido antes de isto entrar em vigor

### Duas contradições com o governo actual

1. **A regra G23 do `CLAUDE.md` manda organizar «por secção temática».** A estrutura proposta é
   **por Dono**. São incompatíveis — **a G23 e o T20 das threads têm de ser reescritos.**
2. **A excepção ao append-only não existe como regra.** A secção de Dependências é editável por
   desenho, mas o `CLAUDE.md` declara o ficheiro *append only* sem excepções (G24).

### Três falhas das instruções, identificadas ao aplicá-las

1. **Não dizem onde param.** Não há critério que separe artefacto de projecto de ficheiro de
   governo. À letra, arrastariam `ESTADO.md`, cinco `CLAUDE.md`, seis `mensagens.md` e as fichas
   de equipa — 30+ linhas de ruído. **Foram excluídos por decisão do subagente**, que a assinalou
   como a de maior impacto do draft. **Precisa de ficar nas instruções, seja qual for o veredicto.**
2. **Não têm modo de migração.** Foram escritas para o fluxo de fim-de-sessão, não para catalogar
   retroactivamente sessões fechadas — que foi exactamente o exercício do draft.
3. **Falta um valor para «a sessão existiu mas o nome não ficou registado».** Só duas sessões têm
   nome escrito em todo o repositório. **20 linhas do draft levam `[não apurado]`, e só o David as
   recupera do cliente Claude.**

### Mais

- **Oito classificações duvidosas** listadas no draft a pedir confirmação. As duas que mais valem:
  12 documentos de trabalho da T002/T004 ficaram como `nota` mas alguns têm 200+ linhas; e o
  `Planta_e_Espaco_Fisico.md` existe em duas cópias que ficaram em **donos diferentes**.
- **Uma pendência de G29 não apurada:** porque é que dois decks cujas sources estão no NotebookLM
  **não têm PDF em disco**.

---

## 5. Tarefa em aberto — automatizar os índices

**O problema, dito sem rodeios:** os índices do topo — por Dono e por Tipo — **são mantidos à
mão**. Cada documento novo obriga a acrescentar a linha no corpo **e** a actualizar dois índices.
**Três coisas a fazer em vez de uma é a definição de passo que se esquece**, e o histórico deste
projecto é de coisas que não aconteceram.

**Agravante conhecido:** as instruções (§5.2) já reconhecem que **o Dataview não resolve isto**
com tudo num só ficheiro — `FROM #tipo/x` devolve o ficheiro inteiro, não as linhas. O
automatismo óbvio está descartado à partida.

**Vias a avaliar, por ordem de esforço:**

| Via | O que seria | Custo |
|---|---|---|
| **MOC / nota por documento** | Uma nota por documento em vez de linhas numa tabela. **Faz o Dataview funcionar de verdade** e os índices passam a gerar-se sozinhos | Muda a arquitectura toda. As instruções já a registam como via de evolução, não adoptada |
| **Script de regeneração** | Um script que lê o corpo e **reescreve os índices**. Corre no fim de sessão, ou em *pre-commit* | Baixo. **Provavelmente a resposta certa a curto prazo** |
| **Dataview com ficheiros separados** | Um registo por thread, em vez de um só | Resolve o Dataview, parte a visão única |
| **Manual, como está** | Nada muda | Zero de setup, e **falha na terceira vez que alguém tiver pressa** |

**Recomendação:** o **script de regeneração**. Trata os índices como *derivados* — o corpo é a
fonte, os índices são saída. **Assim nunca divergem**, e ninguém tem de se lembrar deles.

> **Precedente desta própria entrega:** o subagente que produziu o draft **não construiu o índice
> por Tipo** — teve de ser lançado um segundo para o fazer. **Se falha com um agente a seguir
> instruções escritas, falha com uma pessoa com pressa.**

---

## 6. O que foi verificado

O draft foi validado **por script, não por leitura**:

- Todos os wikilinks resolvem para ficheiro existente — **0 em falta**
- Todas as linhas de documento têm **exactamente 8 colunas**; as de dependência, 4
- **0 aliases com `|` por escapar** — é a causa nº 1 de tabelas partidas em markdown

---

## 7. Proveniência

Produzido na sessão **«2026.09.17 - Arquiteto - Pesquisa de Catalogacao»**, por dois subagentes
`gsd-doc-writer`, a pedido do David:

- O primeiro escreveu as **instruções** e o **template**, a partir da estrutura que o David
  especificou.
- O segundo **leu esses dois ficheiros** e produziu o **draft**, aplicando as regras a todo o
  repositório.

**Os ficheiros nasceram na raiz e foram movidos para aqui** a 2026-09-18, por instrução do David
— para que fique claro que são **entrega de thread**, não governo em vigor.

> **Nota registada no `INBOX.md` da raiz**, para o Arquitecto tratar. Ver a entrada de 2026-09-18
> sobre o protocolo de registo de documentos.
