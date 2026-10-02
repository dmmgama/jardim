---
created: 2026-10-02 13:00
chat: reorganização do projecto e navegador
summary: >
  Como carregar e usar o mod navegador: comandos, botões, perímetro de ficheiros e limites conhecidos.
---
# navegador

Mod do Claude Code que governa a sessão a partir do `MAPA.md` da raiz. Sem `MAPA.md`, não faz nada.

## Carregar

```
claude --plugin-dir .claude/mods/navegador
```

## O que faz

| Peça | Efeito |
|---|---|
| Status line e barra | Caminho do nó activo e modo. Botões **⏸ PANORAMA** e **Mapa**. |
| `/mapa` | Painel: árvore; «ver» põe um nó no PANORAMA; «activar» muda o nó activo; caixa para abrir ficheiros extra; «Abrir MAPA.md»; «Bash livre»; «Limpar». A selecção vale só para a sessão. |
| `/panorama` | Envia ao Claude só pai (divisão), irmãos, filhos, tarefa e mandato, e as perguntas por ordem. |
| `/activo <id>`, `/estado <id> <estado>` | Mudam o `MAPA.md` sem o Claude o abrir. |
| `/modo <modo> [N]` | Fixa o modo. Responder `geral`, `arquitecto`, `thread 4`… à pergunta de arranque faz o mesmo. |
| Perímetro | Read, Edit, Write, Glob, Grep e NotebookEdit só dentro de: `CLAUDE.md` + base do modo + `ficheiros` do nó activo + extras. O `MAPA.md` nunca, salvo se aberto. Bash só git sem conteúdo, `ls`, `pwd`, `claude plugin`. |
| Contexto | Cada pedido ao modelo leva o nó activo, a lógica, o mandato, a divisão do pai e o perímetro. |

## Limites conhecidos

- O perímetro compara caminhos escritos; ligações simbólicas não são seguidas.
- O Bash é negado por omissão em vez de analisado: um script pode ler qualquer coisa, por isso só passa a lista segura.
- Testado com `claude plugin test` (lógica e hook de perímetro). A interface (barra, painel, botões) ainda não foi vista a correr.
