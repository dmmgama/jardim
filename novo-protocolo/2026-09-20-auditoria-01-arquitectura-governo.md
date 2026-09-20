---
created: 2026-09-20 04:49
chat: Auditoria de documentos de governo por agentes
summary: >
  Auditoria integral de arquitectura-governo.md em cinco eixos: 33 achados com citação
  de linha, severidade, tipo e correcção proposta.
---

# Auditoria — `arquitectura-governo.md`

**Documento:** 590 linhas · governance spec / policy · PT
**Modo:** `cannon-rules` audit, conjunto completo R1–R26 + AP1–AP25 (AP25 não aplicável: input completo)
**Diataxis aplicado:** `style-consistent-terminology`, `write-one-purpose-per-doc`, `arch-cross-link-strategy`, *Thesaurus Trap*, *Kitchen Sink Page*, *Rabbit Hole*, *Internal Jargon Guide*. Excluído tudo o que é funil de adopção, SDK, sandbox e versionamento público.

---

## 1 · Veredicto

O documento pensa bem e prescreve mal: a arquitectura é sólida e original, mas só 21 frases do texto são regras marcadas e nenhuma delas declara quem detecta o incumprimento nem o que acontece a seguir.

O defeito dominante é **vocabulário normativo aplicado a uma minoria das obrigações**: cerca de vinte prescrições de igual força vivem em prosa a negrito, indistinguíveis de justificação — um agente frio não consegue derivar a superfície vinculativa.

Serve hoje como documento de arquitectura para leitura humana integral; **não serve** como canon operável por sessão fria sem as correcções do TOP 5.

---

## 2 · Contagem

| Eixo | CRÍTICO | MAIOR | MENOR | Total |
|---|:--:|:--:|:--:|:--:|
| E1 · Autossuficiência | 1 | 3 | 1 | 5 |
| E2 · Integridade canónica | 2 | 6 | 3 | 11 |
| E3 · Clareza | 2 | 2 | 2 | 6 |
| E4 · Arquitectura de informação | 0 | 3 | 2 | 5 |
| E5 · Operacionalidade | 2 | 3 | 1 | 6 |
| **Total** | **7** | **17** | **9** | **33** |

✅ = achado verificado mecanicamente de forma independente.

---

## 3 · TOP 5

1. **E2-02** — Marcar todas as obrigações. Converter as ~20 prescrições em prosa (l.265, 269, 334, 336, 414, 425, 431, 437, 456, 471–477, 501) em alíneas numeradas com **deve**/**não pode**. Sem isto tudo o resto é polimento: o canon não tem superfície vinculativa identificável.
2. **E5-01 + E5-02** — Atribuir a cada regra P um detector e uma consequência. Duas colunas em três tabelas. Transforma 21 afirmações em 21 regras e expõe imediatamente as que são convenção (E5-03).
3. **E2-01** ✅ — Inserir `### 2.5 Evolução` na l.479. Cinco minutos; devolve cinco subsecções órfãs à estrutura e fecha a promessa do front matter.
4. **E3-01 + E3-02** ✅ — Desfazer os dois homónimos (**caminho**, **triagem**). São os dois conceitos mais centrais do documento e cada um tem dois sentidos incompatíveis na mesma tabela.
5. **E1-01** — Criar `§0 · Definições`. É a pré-condição da retoma a frio que a l.46 declara como primeiro critério de sucesso.

---

## 4 · Achados

### E1 · Autossuficiência

**E1-01 · CRÍTICO · defeito** — Ausência total de secção de definições
*Citação:* l.71, 304, 378 (`perfil`); l.71, 381, 539 (`zona`); l.39 (`frente`, primeiro uso); l.414 (`slug`); l.262, 281 (`projecção`)
Os termos que carregam o enforcement nunca são definidos. §2.1 l.71 manda o humano estabelecer "Perfis e zonas" sem dizer o que são. Regras violadas: R7, R17 (count=0 / uso>0); AP *Internal Jargon Guide*.
*Correcção:* secção `§0 · Definições` antes do §1, entrada única por termo, todos os usos posteriores a apontar para lá.

**E1-02 · MAIOR · defeito** — Mecanismos invocados nas garantias e nunca enunciados ✅
*Citação:* l.534, 558 (`sondas de fronteira`); l.542 (`quota` do INBOX, `árbitro em código`); l.541 (`orçamento` de substituição); l.49 (`tecto declarado`)
Nenhum aparece noutro ponto do documento. O "tecto" é critério de sucesso do §1.4 sem valor, sem sítio onde se declara e sem quem o verifica. Regra violada: R18/AP17 (regras fantasma).
*Correcção:* para cada um, criar a regra em P0/P1/P2 que o institui, ou retirar a linha da tabela.

**E1-03 · MAIOR · defeito** — Campos de artefacto usados como interface e nunca especificados
*Citação:* l.279, 488 (`challenges`); l.404, 385 (campo `toca`); l.388, 389 (`carece_aprovacao`); §2.4.5 l.311–333
§2.4.5 define ficheiros mas nenhum esquema. Uma sessão fria não sabe o que escrever em `INBOX/*.json` nem em `estado.json`.
*Correcção:* coluna ou anexo em §2.4.5 com os campos obrigatórios de cada ficheiro `.json`.

**E1-04 · MAIOR · defeito** — A cadência do auditor, que sustenta sete detectores, nunca é fixada
*Citação:* l.293 ("cadência"); l.556 ("Por cadência fixa"); l.560 (só limita o topo: "mais do que uma vez por mês"); l.56 ("ao fim de três meses", sem mecanismo que o avalie)
*Correcção:* declarar a cadência como regra numerada com periodicidade fixa (ex.: `P3.1 — A auditoria **deve** correr uma vez por mês`).

**E1-05 · MENOR · defeito** — Resíduo de proveniência de sessão no front matter
*Citação:* l.3 (`chat: Arquitectura de governo de projectos com agentes`); l.2 (`created`)
Regras violadas: R5/R23; AP19.
*Correcção:* eliminar `chat:`; manter `created` só se o canon declarar um bloco de estado.

### E2 · Integridade canónica

**E2-01 · CRÍTICO · defeito** — Secção sem cabeçalho: falta o `### 2.5` ✅
*Citação:* l.479–524; H4 em l.485, 499, 503, 507, 519; parágrafo de abertura l.481
Cinco H4 e o parágrafo "Um sistema que só impede movimento é uma jaula" ficam pendurados dentro de §2.4.10 "Escolha de agente por papel", com que nada têm a ver. O front matter l.6 promete "evolução" como tópico; é este bloco órfão. Regras violadas: R24; AP22.
*Correcção:* inserir `### 2.5 Evolução` na l.479 e renumerar os cinco H4 como 2.5.1–2.5.5.

**E2-02 · CRÍTICO · defeito** — O vocabulário normativo declarado cobre uma minoria das obrigações
*Citação:* declaração em l.79; honrada apenas nas 21 alíneas P0.1–P2.6. Obrigações de força idêntica em prosa a negrito, sem marcador: l.265 ("Um nível nunca escreve no nível acima"), 269, 334 ("Nunca no mesmo ficheiro"), 336, 414 ("Os slugs são globais, nunca se reutilizam"), 425 ("Nunca o conteúdo do debate"), 431, 437, 456 ("O critério de enforcement é eliminatório"), 471, 473, 475, 477, 501
Um agente que procure o que o vincula lê 21 regras e ignora vinte. Regras violadas: R2, R20/AP18.
*Correcção:* converter cada obrigação em prosa numa alínea numerada (P3.x–P5.x) com **deve**/**não pode**, deixando na prosa só a justificação.

**E2-03 · MAIOR · defeito** — Contradição tripla sobre a escrita do `Arquitecto · rumo` ✅
*Citação:* l.324 (atribui `debates/*.json` a "rumo") vs l.291 ("emenda ao mandato, ou nada") vs l.464 ("conversa, **sem escrita automática**") vs l.501 ("**Nunca escreve no estado**")
Quatro formulações incompatíveis para o mesmo actor.
*Correcção:* fixar a zona de escrita do rumo numa só célula (§2.4.3) e substituir as outras por referência cruzada.

**E2-04 · MAIOR · defeito** — Regras fantasma: garantias que dependem de regras inexistentes
*Citação:* l.548 ("toda a regra nova exige falha observada"); l.54 ("Governo estável"); l.49 (tecto de frentes); l.542 (quota do INBOX)
Pressupõem uma regra de admissão de regras que não existe em P0/P1/P2 nem em prosa. Regra violada: R18.
*Correcção:* enunciar a regra de admissão ("nenhuma regra nova **pode** ser acrescentada sem incidente registado") ou retirar as duas linhas.

**E2-05 · MAIOR · defeito** — O campo `toca` sustenta duas verificações e nenhuma regra obriga a declará-lo
*Citação:* l.404 (base da 1.ª passagem de detecção); l.385 (critério de bloqueio de fecho); l.543 (garantia). P1.4 l.169 cobre dependências; P2.2 l.218 cobre pressuposto e caminho — nenhuma cobre `toca`.
*Correcção:* acrescentar `P2.7 — Cada frente **deve** declarar o que toca antes de abrir`.

**E2-06 · MAIOR · defeito** — A máquina de estados do alerta não tem escritor possível
*Citação:* l.412 (exige `novo`/`visto`/`descartado` com hash persistente entre corridas); l.322 (escrita de `ALERTA` ao watcher, **por substituição**); l.290 (a triagem não tem acesso de escrita a `ALERTA`); l.492 agrava ("Alerta fica novo")
Ninguém pode marcar `visto` ou `descartado`, e a substituição apaga o estado que a regra exige preservar.
*Correcção:* separar `ALERTA` (substituição, watcher) de um `ALERTA-ESTADO` por acrescento escrito pela triagem, e declarar a chave (hash do par).

**E2-07 · MAIOR · defeito** — Contagem errada ✅
*Citação:* l.469 ("**Três** regras de alocação") seguida de quatro parágrafos-regra em l.471, 473, 475, 477
*Correcção:* "Quatro regras de alocação", ou mover "Falha de runner é recusa" (l.477) para §2.4.8 junto ao HALT.

**E2-08 · MAIOR · defeito** — Inventário de actores incoerente entre §2.4.3 e §2.4.10
*Citação:* l.443 ("Os papéis da §2.4.3") vs tabela l.460–467, que acrescenta **Detector semântico** (l.467, não é actor em §2.4.3) e omite **Humano responsável** (l.289). `script` (l.325) e `hook` (l.331) escrevem ficheiros sem constar de §2.4.3.
*Correcção:* uma só tabela de actores em §2.4.3, incluindo script, hook e detector semântico; §2.4.10 passa a acrescentar apenas colunas de requisito.

**E2-09 · MENOR · defeito** — Permissão negativa usada como proibição
*Citação:* P0.8, l.88 ("Nenhuma frente **pode** ser aberta…"); vocabulário em l.79 define **pode** = permitido
A negação fica ambígua entre "não é permitido" e "é permitido não". Regra violada: R9/AP9.
*Correcção:* "Uma frente **não pode** ser aberta antes de P0.7 devolver verdadeiro."

**E2-10 · MENOR · defeito** — Restatement em vez de referência
*Citação:* M7 (l.197) repete P2.4 (l.220); l.427 repete T3 (l.581); l.477 repete T4 (l.585); a frase "Um agente permanente acumula contexto e deriva…" é literal em l.296 e l.471; l.184 repete l.113
Regras violadas: R6/R21; AP15.
*Correcção:* manter a formulação no sítio canónico e substituir as cópias por `ver P2.4` / `ver §2.4.3`.

**E2-11 · MENOR · defeito** — Definições depois do uso
*Citação:* P0.7 (l.87) invoca "teste de reformulação" e "teste de discriminação", definidos em l.94 e l.105; "modo rumo" usado em l.246, caracterizado em l.501; "projecção" em l.262, explicada em l.281
Regra violada: R16; AP14.
*Correcção:* mover o bloco "Critério de desbloqueio da fase" (l.90–107) para antes do Protocolo P0, ou converter as menções antecipadas em referências explícitas.

### E3 · Clareza

**E3-01 · CRÍTICO · defeito** — **caminho** nomeia dois conceitos sem relação ✅
*Citação:* sentido estratégico — §2.3 l.182, nível L1, ficheiro `CAMINHO`. Sentido filesystem — l.304 ("Hook de caminho"), l.73 ("o caminho existe"), l.431 ("o caminho dos hooks"), l.539 ("hook de caminho"), l.473 ("valida caminhos")
A l.539 põe os dois sentidos na mesma frase de garantia. *Nota do revisor: são 4 ocorrências filesystem em 31 usos de "caminho" — real, mas menos extenso do que a formulação sugere.* Regras violadas: R7/R17.
*Correcção:* renomear o segundo sentido para "hook de **trajecto**" ou "hook de **path**" em l.73, 304, 431, 473, 539.

**E3-02 · CRÍTICO · defeito** — **triagem** nomeia dois conceitos sem relação ✅
*Citação:* filtro pré-dados sobre ramos — §2.2 título l.142, P1.5 l.170, l.184, l.150 ("triagem preliminar"). Actor disparado por alerta que escreve `ESTADO`/`FRENTES`/`REJEICOES` — l.261, 275, 290, 318–321, 360, 463, 491, 536, 555
A l.536 usa o primeiro sentido numa tabela onde a coluna vizinha usa o segundo.
*Correcção:* manter "triagem" só para o actor; renomear o filtro para "**crivo de ordem de grandeza**" em l.142, 146, 150, 170, 184, 536.

**E3-03 · MAIOR · defeito** — Um conceito, três nomes
*Citação:* "mandato da frente" (l.273, 383); "projecção" (l.262, 281, 367, 475); "o pressuposto mais a regra de paragem" (l.281, 566)
Agrava por "mandato" já nomear o artefacto L0: a l.273 põe "o mandato da frente" e "o mandato" na mesma linha da tabela com sentidos diferentes.
*Correcção:* usar **projecção** em todo o lado; eliminar "mandato da frente" de l.273 e 383.

**E3-04 · MAIOR · defeito** — O resultado do cold-read tem três nomes e a marca de fecho tem dois
*Citação:* "cold-read falha" (l.389), "cold-read fraco" (l.398), "é inválido" (l.429); `carece_aprovacao` (l.388–389) vs "fecha com marca" (l.398)
Um agente não sabe se "fraco" e "falha" são o mesmo estado.
*Correcção:* fixar um par de valores (`cold_read: passa|falha`) e uma marca (`carece_aprovacao`) e usá-los em l.388, 389, 398, 429.

**E3-05 · MENOR · risco** — Referente indeterminado
*Citação:* l.425 ("Assim o protocolo não contém uma única referência a decisões e continua protegido")
Num documento com P0, P1 e P2, "o protocolo" não identifica nada.
*Correcção:* substituir por "o contexto montado para a sessão".

**E3-06 · MENOR · risco** — Interacção não declarada entre P0.1, P0.2 e P0.3
*Citação:* l.81–83 — até cinco objectivos × até três não-objectivos = quinze não-objectivos, dentro de "uma página" (l.83), nunca definida em unidades
*Nota de concordância:* l.82 diz "duas a três não-objectivos" → "dois a três".
*Correcção:* definir "uma página" em palavras ou tokens e verificar a compatibilidade dos limites.

### E4 · Arquitectura de informação

**E4-01 · MAIOR · defeito** — Hierarquia inconsistente e sem âncoras estáveis
*Citação:* §2.1–§2.3 usam H4 não numerados (l.186 "Método de procura", l.134 "Critério de corte"); §2.4 usa H4 numerados (2.4.1–2.4.10); o bloco órfão de E2-01 volta a não numerar
A justificação de P1.5 (l.142) e o critério de corte (l.134) não têm identificador citável; a l.384 refere "conforme o nível" sem apontar para a tabela de l.419–423. Regras violadas: R13, R22/AP20.
*Correcção:* numerar todos os H4 (2.1.1, 2.2.3…) e substituir as remissões implícitas por referências numeradas.

**E4-02 · MAIOR · defeito** — Mistura de géneros em todos os blocos normativos
*Citação:* §2.2 (l.113–162) mistura definição, critério e justificação; P1 (l.164–172) reenuncia normativamente o que já foi dito; l.174 acrescenta justificação **depois** das regras. Idem §2.3 (l.178–214 → P2 em l.215–222) e §2.1
O implementador não consegue extrair a superfície vinculativa sem ler os ensaios. Regras violadas: R20/AP18; AP *Kitchen Sink Page*.
*Correcção:* separar cada §2.x em `Regras` (só alíneas marcadas) e `Nota / Racional` (tipograficamente distinto), nesta ordem.

**E4-03 · MAIOR · defeito** — Sem camada de navegação para consulta pontual
*Citação:* 590 linhas, 21 regras, 16 garantias, 5 tensões; nenhum índice, sumário de protocolos, glossário ou mapa regra→garantia
O documento só funciona em leitura integral — o oposto do que a l.46 promete ("uma sessão sem histórico retoma"). Regra Diataxis: `arch-cross-link-strategy`.
*Correcção:* acrescentar ao §1 um índice de protocolos (P0.1–P2.6 em uma linha cada) e um mapa regra→garantia→detector.

**E4-04 · MENOR · risco** — §1.4 e §3.1 sobrepõem-se sem mapeamento
*Citação:* §1.4 (9 critérios, l.44–54) e §3.1 (16 garantias, l.531–548), com nomes diferentes para o mesmo item ("Zero decisões órfãs" l.48 vs "Decisões são aplicadas" l.544) e critérios sem garantia correspondente ("Alerta silencioso" l.47)
*Correcção:* acrescentar coluna de referência em §1.4 apontando para a linha de §3.1.

**E4-05 · MENOR · defeito** — §2.4.9 "Regra de saída" enterrada
*Citação:* l.433–439; declara-se "Transversal a todos os níveis" (l.435) mas está como nona subsecção de §2.4, sem identificador e sem garantia correspondente em §3.1
*Correcção:* promover a §2.6 ou a alínea numerada em P0, e criar a linha de garantia correspondente.

### E5 · Operacionalidade

**E5-01 · CRÍTICO · defeito** — 21 regras, 4 com mecanismo de detecção declarado
*Citação:* com detector — P0.7/P0.8 (testes de l.94–105), P1.4 (auditor, l.558), P2.2 (gate S5, l.386). Sem qualquer detector — P0.1–P0.6, P1.1, P1.2, P1.3, P1.5, P1.6, P1.7, P2.1, P2.3, P2.4, P2.5, P2.6. A lista do auditor (l.558) cobre sete itens, dos quais só dois correspondem a regras P.
*Correcção:* coluna "detectado por" em cada bloco de protocolo, valores {hook, gate, watcher, auditor, humano}.

**E5-02 · CRÍTICO · defeito** — Nenhuma regra declara consequência de incumprimento
*Citação:* as únicas consequências do documento são o gate (l.398), os quatro níveis do hook (l.419–423) e o `HALT` (l.431) — e nenhuma está ligada a um identificador P
Violar P1.2, P1.6 ou P2.3 não tem efeito declarado.
*Correcção:* coluna "consequência" em cada bloco, valores {bloqueia, fecha com marca, alerta, relatório de auditoria}.

**E5-03 · MAIOR · risco** — Convenções disfarçadas de regra
*Citação:* P1.2 (l.167), P1.3 (l.168), P1.7 (l.172), P2.1 (l.217) — não verificáveis por máquina, sem detector (E5-01) e sem consequência (E5-02)
*Contestação do revisor:* P1.2 e P1.3 passam a ser verificáveis por consulta se a árvore tiver substrato estruturado — que é exactamente o que D2 propõe com `arestas.db`. São convenções **nesta arquitectura**, não intrinsecamente. Reforça o argumento da proposta 2.
*Correcção:* mover para "Convenções de desenho" ou atribuir-lhes verificação explícita pelo auditor.

**E5-04 · MAIOR · defeito** — Garantia permanente sem mecanismo de manutenção
*Citação:* l.544 — "Decisões são aplicadas | verificação no fecho | **—** | decisão sem item correspondente"
A célula "Como se mantém" está vazia; a garantia obtém-se uma vez e nunca se sustenta. Contradiz o critério de sucesso "Zero decisões órfãs" (l.48).
*Correcção:* preencher com o auditor (acrescentando "decisões sem item" à lista da l.558) ou baixar de garantia para tensão em aberto no §4.

**E5-05 · MAIOR · defeito** — A coluna "Como se detecta a falha" nomeia sintomas sem dono nem cadência
*Citação:* l.543 ("colisão descoberta por acaso"), l.540 ("regra alterada sem decisão correspondente"), l.545 ("frente repete trabalho já fechado"), l.542 ("inbox cresce mais do que se esvazia") — nenhum com actor atribuído nem periodicidade, salvo os sete que a l.558 dá ao auditor
*Correcção:* acrescentar coluna "quem detecta / com que cadência" à tabela l.531–548.

**E5-06 · MENOR · defeito** — O único limiar quantificado não é mensurável
*Citação:* "uma página" em P0.3 (l.83), P2.6 (l.222), l.213 e l.533
Sem unidade, três sessões medem três coisas — exactamente o modo de falha que o teste de discriminação (l.105) existe para apanhar.
*Correcção:* definir em palavras ou tokens.

---

## 5 · O que está bem

As 21 alíneas P0–P2 passam limpas em R3 (zero hedging), R11 (um actor) e R12 (uma obrigação) — redacção normativa de qualidade rara, com numeração contígua e sem colisões.

O §4 é exemplar: cada tensão separa risco residual, resolução adoptada e custo assumido, e T1 (l.576) inventa um sinal gratuito que dispensa julgamento — é o modelo que o resto do documento devia seguir para os detectores.

§2.4.2 é um corolário genuinamente derivado, não uma repetição, e a excepção dos não-objectivos (l.283) é argumentada em vez de decretada.

Todas as referências cruzadas explícitas (§2.2, §2.3, §2.4.3, P1.1, P1.4) resolvem: R18 limpo, ao contrário das referências implícitas (E4-01).
