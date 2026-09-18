---
created: 2026-09-18
project: Jardim
tipo: governo
branch: Governo-correcao-v1
summary: |
  Regras da pasta Registos-Arquiteto: registos de sessão feitos a pedido do David, com índice e estado.
---

# Registos do Arquitecto

**O que é.** Memória de sessão em modo Arquitecto, escrita **só a pedido do David** e lida **só a pedido do David**. Não é handoff, não é estado do projecto, não é decisão. É o que o David mandou registar naquela sessão: o que o agente viu, o que lhe foi perguntado, o que respondeu, o feedback que recebeu, o próximo passo.

## Regras

**R1.** Cada registo vive numa **pasta própria** com o nome do ficheiro principal:

```
Registos-Arquiteto/
└── YYYY-MM-DD-ARQ-TEMA-Snn/
    ├── YYYY-MM-DD-ARQ-TEMA-Snn.md   ← o registo
    └── <anexos>                     ← listados no registo
```

`TEMA` é o assunto da sessão em maiúsculas e kebab-case (ex. `ESTADO-GERAL`). `Snn` é o número da sessão nesse tema, com dois dígitos.

**R2.** O registo escreve **o que o David indicar**, organizado por temas numerados (Tema 1, Tema 2, …). Se houver anexos, o registo lista-os e eles ficam na mesma pasta.

**R3.** Todo o registo tem front matter com, no mínimo: `created`, `branch`, `sessao`, `tema`, `summary`. **O campo `branch` é obrigatório** — sem ele não se sabe em que linha do repositório o registo foi feito.

**R4.** Cada registo acrescenta **uma linha** a `Index-registos-arquiteto.md`: data · pasta · estado.

**R5.** Estados possíveis no índice:

| Estado | Significado |
|---|---|
| `ABRIR ESTE` | É o registo que a próxima sessão deve abrir. Só um de cada vez. |
| `Aberto` | Registo com trabalho pendente, mas não é o próximo a abrir. |
| `Fechado` | O que lá está foi tratado. |
| `Anulado` | Deixou de fazer sentido. Fica no índice, não se apaga. |

**R6.** **Leitura on demand.** Quando o David mandar uma sessão ver os registos do Arquitecto, a sessão:
1. Lê este README.
2. Lê `Index-registos-arquiteto.md`.
3. Identifica o registo marcado `ABRIR ESTE`.
4. **Confirma com o David** antes de o abrir.
5. Abre-o e segue o que lá está.

**R7.** Se o David não mandar, esta pasta **ignora-se**. Não entra no arranque de nenhum modo.

**R8.** A sessão que produz um registo **commita antes de fechar**, sem excepção.
