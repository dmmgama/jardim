---
created: 2026-09-20 04:49
chat: Auditoria de documentos de governo por agentes
summary: >
  Relatório consolidado da auditoria aos três documentos de governo: coerência entre
  documentos, padrão de defeitos comum, e recomendação de consolidação.
---

# Auditoria consolidada — arquitectura de governo de projectos com agentes

**Data:** 2026-09-20
**Documentos auditados:** 3
**Método:** um auditor independente por documento (grelha de 5 eixos), mais verificação cruzada entre documentos
**Grelha:** E1 Autossuficiência · E2 Integridade canónica · E3 Clareza · E4 Arquitectura de informação · E5 Operacionalidade
**Fontes de regras:** `cannon-rules` (modo audit) + subconjunto transferível de `diataxis-docs-framework` (27 regras, 35 anti-patterns; excluído tudo o que é específico de documentação pública de produto)

---

## 1 · Quadro geral

| Documento | Achados | CRÍT | MAIOR | MENOR | Veredicto |
|---|:--:|:--:|:--:|:--:|---|
| **D1** · `arquitectura-governo.md` (590 l.) | 33 | 7 | 17 | 9 | Serve para leitura humana integral. Não serve como canon operável por sessão fria. |
| **D2** · `ARQUITECTURA-PROPOSTA2.md` (654 l.) | 28 | 7 | 15 | 6 | Falha nos dois papéis que acumula: nem especificação autónoma nem diff. |
| **D3** · `sintese-protocolo-arvore` (233 l.) | 27 | 5 | 13 | 9 | Não cumpre o propósito declarado: nenhum dos 4 cartões passa o teste de isolamento. |
| **X** · entre documentos | 5 | 2 | 2 | 1 | Ver §2. |
| **Total** | **93** | **21** | **47** | **25** | |

---

## 2 · Coerência entre documentos

Achados que nenhum auditor de documento único pode encontrar. Verificados mecanicamente.

### X1 · CRÍTICO · defeito — Referências cruzadas de D3 quebram contra D2

D3 cita:

| Citação em D3 | Significado assumido | Em D1 | Em D2 |
|---|---|:--:|:--:|
| `P1.7` (§3 l.118; R8 l.218) | "árvores de propósito diferente não se fundem" | ✅ correcto | ❌ é **P1.8**; P1.7 passou a ser "ramo fechado regista resultado e razão" (`[M11]`) |
| `P0.7` (CARTÃO D, l.202) | "desbloqueio pelos dois testes" | ✅ correcto | ❌ são **P0.9/P0.10** (`[M07]`); P0.7 passou a ser "redigido por agente" |

As restantes citações (`P1.1`, `P1.2`, `P1.3`, `P1.4`, `P1.5`, `P1.6`) resolvem em ambos.

**Agravante:** `P0.7` continua a existir em D2 com outro conteúdo. A citação falha em silêncio, não em erro.

*Correcção:* regra de numeração aditiva (ver §4), e reescrita de D3 após consolidação.

### X2 · CRÍTICO · defeito — D3 tem baseline misto

D3 cita a numeração de D1 mas pressupõe mecanismos que só existem em D2.

Verificação mecânica: `cone` e `transitiv` têm **zero ocorrências em D1**. Em D3 aparecem três vezes:

- §0 l.21 — "por toda a detecção ser travessia de arestas"
- §6 l.224 — "o cone a jusante é recalculado por travessia das arestas"
- R5 l.215 — "Cone afectado = a árvore inteira"

**Consequência:** D3 não é aplicável a nenhum dos dois. Contra D1, invoca um mecanismo inexistente. Contra D2, cita duas regras com o número errado.

*Correcção:* fixar o baseline antes de reescrever D3.

### X3 · MAIOR · defeito — Regra fantasma em D1

Critério de sucesso §1.4 l.49: *"Frentes sob tecto — frentes abertas nunca excedem o tecto declarado"*.

Nenhum protocolo de D1 obriga alguém a declarar um tecto. Varrimento de "tecto" em D1: só ocorrem a l.49 e o tecto de uma página do mandato (P0.3, l.533). Critério de sucesso não verificável.

D2 corrige via `[M05]`, `[M06]`, `P1.9`, `P2.8` — e esta é a melhor justificação isolada para a proposta 2. Mas ver **D2·B4/E1f**: a correcção está incompleta.

### X4 · MAIOR · defeito — Secção órfã em D1

O bloco "Evolução" (l.481–524: *Por necessidade* · *Por vontade* · *Por falha do próprio sistema* · *Deriva e inflexão* · *Registo de debates*) **não tem cabeçalho**. Fica pendurado dentro de §2.4.10 "Escolha de agente por papel", com que nada tem a ver.

D2 tem `### 2.5 Evolução` na posição correcta (l.502). O front matter de D1 anuncia "evolução" no `summary` — o conteúdo existe, mas é inalcançável por navegação.

*Correcção:* inserir `### 2.5 Evolução` na l.479 e renumerar os cinco H4 como 2.5.1–2.5.5.

### X5 · MENOR · defeito — Contagem de D2 não bate

Front matter l.6: *"trinta e quatro alterações marcadas `[M01]` a `[M34]`"*. Índice §5: **35 linhas, até `[M35]`**. `[M35]` é auto-referencial — marca o próprio índice.

*Correcção:* corrigir o front matter para trinta e cinco.

---

## 3 · O padrão comum

Os três documentos falham nos mesmos cinco sítios. Isto aponta para defeito de método, não de redacção.

| Padrão | D1 | D2 | D3 |
|---|---|---|---|
| **Regras sem detector nem consequência** | 21 regras · 4 com detector · **0 com consequência** | 4 regras de tecto sem mecanismo nenhum | 5 das 8 regras comuns sem consequência |
| **Garantias apoiadas em mecanismos inexistentes** | `sondas de fronteira`, `quota`, `árbitro em código`, `orçamento`, `tecto` | `validador de esquema` (que `[M28]` declara não existir), pesquisa vectorial pré-v1 | `cone`, `driver` |
| **Homónimo em conceito central** | `caminho` ×2 · `triagem` ×2 | `nível` ×4 | `suspenso` ×2 |
| **Prosa reenuncia o protocolo com redacção divergente** | §2.2/§2.3 vs P1/P2 | 8 obrigações ditas duas vezes | §3 vs §5 |
| **Sem secção de definições** | ausente | ausente | ausente (e §2 l.38 promete um vocabulário que nunca entrega) |

### A observação incómoda

Estes documentos definem um sistema para impedir deriva, e exibem deriva.

O caso mais literal é **D2·B7**: `[M09]` alterou a regra P1.13 (l.184) e **deixou intacta a versão em prosa da mesma obrigação** (l.146), que usa ainda outro modal ("tem de recair"). Isso é exactamente a "deriva não declarada" que o §2.5 do próprio documento existe para tornar impossível.

Causa estrutural: **o corpo de regras não tem mecanismo para a sua própria integridade.** O auditor previsto no sistema audita o projecto, não o canon. As sete verificações que a §3.2 de D1 lhe atribui não incluem nenhuma sobre a consistência do documento que as define.

---

## 4 · Recomendação

Nenhum dos dois documentos de arquitectura é adoptável como está. Não por qualidade — a arquitectura é sólida e original em ambos — mas porque:

- **D1** tem lacunas reais que D2 identificou correctamente: tectos (X3), ramo fechado sem registo (`[M11]`), ausência de teste de discriminação de frente (`[M12]`), propagação de dependências só a um nível (`[M22]`).
- **D2** corrige-as e introduz três contradições próprias (B1, B2, B4) que invalidam parte das correcções que traz.
- **D3** não é aplicável a nenhum dos dois (X1, X2).

Por ordem de execução:

1. **Consolidar numa versão única.** Absorver a substância de D2, eliminar o formato de diff (D2·A1), arquivar D2 como registo de decisão. Enquanto houver duas versões vivas, D3 e tudo o que dele dependa ficam suspensos.
2. **Fixar uma regra de numeração aditiva antes de mais nada.** Regras novas recebem sempre o número seguinte; nunca se insere no meio. Resolve de uma vez X1, D2·B3 (P9 fora de ordem, com P9.2 e P9.5 fantasma) e D2·B6 (colisão do método M1–M7 com os marcadores `[M01]`–`[M35]`). Maior alcance, menor custo do conjunto.
3. **Duas colunas em todas as tabelas de protocolo:** `detectado por` {hook, gate, watcher, auditor, humano} e `consequência` {bloqueia, fecha com marca, alerta, relatório}. Transforma afirmações em regras e expõe quais são convenção.
4. **`§0 · Definições`** nos três documentos. Termos mínimos: **frente, ramo, zona, perfil, projecção, pressuposto, slug, alerta, driver, cone, ME/CE**.
5. **Acrescentar à listagem fixa do auditor a verificação do próprio canon:** obrigações em prosa sem identificador, regras sem detector, garantias sem regra, referências cruzadas não resolvidas.
6. Só depois reescrever D3 contra o resultado.

---

## 5 · Relatórios individuais

- `2026-09-20-auditoria-01-arquitectura-governo.md`
- `2026-09-20-auditoria-02-arquitectura-proposta2.md`
- `2026-09-20-auditoria-03-sintese-protocolo-arvore.md`
