---
activo: T0
created: 2026-10-02 12:00
chat: reorganização do projecto e navegador
summary: >
  Árvore de problemas da sessão: problema geral, subproblemas e tarefas, com lógica,
  mandato e perímetro de ficheiros por nó. Fonte de verdade do mod navegador.
---
# MAPA

> Um nó é um cabeçalho `## <ID> — <nome>` seguido de campos. O `activo` no topo é onde estamos.
> Campos: `pai`, `estado` (por abrir · em curso · resolvido · em pausa), `dono`, `lógica` (porque
> existe: que parte da divisão do pai cobre), `divisão` (porque se divide nos filhos), `mandato`,
> `thread`, `ficheiros` (o que o Claude pode ler/escrever com este nó activo; vírgulas; `pasta/` = tudo lá dentro).
> **Rascunho de 2026-10-02**, com as palavras do David. Não verificado como MECE.

## P0 — O projecto está desorganizado
- pai: —
- estado: em curso
- dono: @David
- mandato: Reorganizar o projecto.
- divisão: Pelos exemplos que o David deu (lista não fechada). T0 não é parte do problema: é o
  instrumento que se faz primeiro, para navegar o resto.

## T0 — Construir o mod navegador
- pai: P0
- estado: em curso
- dono: @Claude
- lógica: O David pediu-o como primeira coisa: sem saber a cada momento onde estamos e porquê,
  a reorganização deriva.
- mandato: Mod com problema geral → subproblemas MECE → tarefas; saber sempre onde se está;
  botão PANORAMA (pai, irmãos, filhos, tarefa e mandato; ainda sigo a lógica? sei reformulá-la?);
  perímetro de ficheiros por nó, com caixa de selecção.
- ficheiros: .claude/mods/navegador/

## P1 — O governo não funciona
- pai: P0
- estado: por abrir
- lógica: CLAUDE.md gigante; estrutura do repositório que ninguém sabe explicar nem quando usar o
  quê; o Arquitecto não serve — devia ser um coordenador que conhece o objectivo, estabelece a
  estratégia com o David e sabe que instrumentos tem (threads, etc.).
- ficheiros:

## P2 — Não há objectivo nem ligação do trabalho a ele
- pai: P0
- estado: por abrir
- lógica: O objectivo não existe; o ESTADO.md é uma montanha de informação inútil; os handoffs
  são uma confusão; não há protocolo que associe threads ao objectivo nem diga como se complementam.
- ficheiros:

## P3 — Nada está no sítio
- pai: P0
- estado: por abrir
- lógica: Depois de P1 e P2, é preciso pôr tudo organizado e no sítio.
- ficheiros:
