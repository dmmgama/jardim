---
created: 2026-09-18
project: Jardim
tipo: mandato-de-branch
branch: Governo-correcao-v1
base: master
summary: |
  O que a branch Governo-correcao-v1 existe para fazer: corrigir a falta de governo e a falta de instrumentos
  de visão do estado geral, e estruturar o projecto top-down.
---

# Mandato da Branch — B1 `Governo-correcao-v1`

**Número:** B1 (ver `BRANCHES.md` em `master`). As sessões desta branch chamam-se `YYYY-MM-DD-B1-…`.

> **Regra:** qualquer sessão que detecte estar numa branch que não é a principal **DEVE** ler este ficheiro antes de tudo o resto. Ver `CLAUDE.md` §0.

**Criada:** 2026-09-18, a partir de `master`, na sessão «2026.09.18 - Arquiteto - Estado Geral».
**Decisor:** David.

---

## 1. Porque existe

Na sessão de 2026-09-18 o David pediu ao Arquitecto um panorama do projecto: propósito, estrutura, fios de acção, lacunas, sucesso final. A resposta estava errada em dois sentidos:

1. **Tomou um problema por objectivo.** «Fazer o jardim entrar na sala» é um dos problemas a resolver. O objectivo geral é **desenvolver um jardim tendo em conta as condicionantes locais e o gosto/visão do David.**
2. **Leu bottom-up.** Amontoou o que as threads tinham produzido e chamou-lhe panorama. As threads são tarefas isoladas, abertas para desenvolver certos caminhos; não são a estrutura do projecto.

**Diagnóstico do David:**
- **Falta de governo.**
- **Falta de instrumentos que dêem sempre a visão do estado geral**, ao David e ao agente.

Esta branch existe para corrigir as duas coisas sem contaminar `master` enquanto a correcção não estiver fechada.

## 2. O que a branch tem de produzir

### 2.1 Instrumentos (feitos nesta sessão)

| Instrumento | Onde | Para quê |
|---|---|---|
| **Registos do Arquitecto** | `Registos-Arquiteto/` | Memória de sessão a pedido do David. README, índice com estado (`ABRIR ESTE` · `Aberto` · `Fechado` · `Anulado`), uma pasta por registo. Leitura e escrita só a pedido. |
| **Handoffs por tema** | `Handoffs-Arquiteto/` | Continuidade em modo Arquitecto, por **Tema**. Cada tema tem protocolo de arranque e handoffs numerados. Temas iniciais: GERAL, GOVERNO, REGISTOS-ARQUITETO. |
| **Arranque por comando** | `CLAUDE.md` §0 | «Arranque Arquiteto» · «Arranque TEMA» · «Arranque Thread» · «Arranque Thread TNNN». Substitui a pergunta «ARQUITECTO ou THREAD?». |
| **Mandato da branch** | este ficheiro | Toda a branch tem um. Lê-se sempre que se está numa branch. |
| **Campo `branch`** | todos os registos e handoffs | Para se saber sempre em que linha do repositório o ficheiro foi escrito. |
| **Commit no fecho** | `CLAUDE.md` | Toda a sessão commita antes de fechar. Sem excepção. |
| **Texto de arranque** | `CLAUDE.md` §0.3 | No fecho, o agente dá ao David o texto a colar na sessão seguinte. |
| **Índice de branches** | `BRANCHES.md` em `master` | Número `Bn`, datas, mandato, estado. Só isto se escreve em `master` enquanto a branch estiver activa. |

### 2.2 Estruturação do projecto (próximo passo — skill wayfinder)

A leitura correcta do projecto é **top-down**, por esta ordem:

1. **O objectivo.** Desenvolver um jardim tendo em conta as condicionantes locais e o gosto/visão do David.
2. **O que significa desenvolver um jardim?** Que áreas envolve?
3. **Condicionantes locais.** Como se repartem? Como interagem?
4. **Gosto e visão do David.** Qual é? Como se estrutura?
5. **Essa estruturação chega?** Se sim: que tickets abrir? Quais em paralelo, quais em série? Como se avalia a evolução? E as descobertas novas?
6. **Consolidação.** Como se vai consolidando tudo de forma estruturada, e evoluindo à medida que se avança? Onde está o plano de acção agêntico e o plano de acção do David?
7. **Governo.** Está a funcionar? Que modos deve o Arquitecto ter? Como se regista a documentação de forma a não misturar decisões antigas com o estado actual?

**A sessão seguinte desta branch faz isto, de forma rápida, com o skill wayfinder.** Só depois se volta ao tema GERAL.

## 3. O que a branch não faz

- Não decide projecto: nada entra em `ESTADO.md` ou `REJEICOES.md` salvo instrução expressa do David.
- Não abre nem fecha threads.
- Não responde aos pedidos pendentes das threads — isso é tema GERAL, depois da estruturação.
- Não ratifica por si os protocolos pendentes do inbox (G37–G42; registo de documentos). Ficam listados no handoff do tema GOVERNO para o David decidir.

## 4. Como fecha

A branch funde-se em `master` quando o David disser que a correcção de governo está fechada. Antes da fusão: este ficheiro é actualizado com o que ficou feito e o que ficou por fazer, e o último handoff do tema GOVERNO diz onde se retoma em `master`.
