---
created: 2026-09-20 04:49
chat: Auditoria de documentos de governo por agentes
summary: >
  Auditoria integral da síntese do protocolo de árvore em cinco eixos, com teste de
  isolamento dos quatro cartões e análise de cobertura do roteamento: 27 achados.
---

# Auditoria — `2026-09-20-sintese-protocolo-arvore-definicao-e-uso.md`

**Documento:** 233 linhas · 1961 palavras ≈ 3,5k tokens · SOP de agente / canónico operacional · PT
**Modo:** `cannon-rules` audit
**Diataxis aplicado:** arquitectura de informação, terminologia consistente, *Dead End*, *Kitchen Sink*. Excluído tudo o que é específico de documentação pública de produto.

**Requisito de desenho que domina a auditoria:** o documento declara-se destinado a leitura por agentes dentro de protocolos, com economia de contexto como requisito duro (l.36), roteamento antes de conteúdo, e cartões que o agente lê selectivamente — "lê **só os cartões que te saíram**" (l.48). Declara ainda que os quatro cartões são "auto-suficientes" (l.22). O eixo E1 é, por isso, dominante, e tem um teste próprio: **cada cartão tem de funcionar isoladamente.**

---

## 1 · Veredicto

O esqueleto de roteamento existe e é bom, mas o documento **não serve hoje o propósito declarado**: nenhum dos quatro cartões passa o teste de isolamento, e a própria instrução de leitura (l.48) aponta para secções erradas por causa da dupla numeração.

**Defeito dominante:** o documento promete "quatro cartões auto-suficientes" (l.22) e mantém fora dos cartões — ou fora do documento — cinco conceitos que os cartões usam como critério de decisão: `driver`, `ME/CE`, `cone`, `suspenso`, e as regras externas `P0.7`/`P1.3`.

**Economia de contexto real:** ~30%, não a que a forma sugere. A instrução de leitura chega depois de 21% do texto, e §3 (236 palavras) é lida integralmente por todos os agentes, incluindo os dois a quem não se aplica.

---

## 2 · Contagem

| Eixo | CRÍTICO | MAIOR | MENOR | Total |
|---|:--:|:--:|:--:|:--:|
| E1 · Autossuficiência | 2 | 5 | 1 | 8 |
| E2 · Integridade canónica | 2 | 2 | 3 | 7 |
| E3 · Clareza | 0 | 2 | 2 | 4 |
| E4 · Arquitectura de informação | 1 | 2 | 1 | 4 |
| E5 · Operacionalidade | 0 | 2 | 2 | 4 |
| **Total** | **5** | **13** | **9** | **27** |

Defeitos: 24 · Riscos: 3 (E3-1, E4-3, E4-4).
✅ = achado verificado mecanicamente de forma independente.

---

## 3 · Teste de isolamento dos cartões

Caminho de leitura testado, conforme l.48: §0 Definição + §1 Porta + §2 Roteamento + §3 Tabela + o cartão + §5 Regras. Nada mais.

| Cartão | Auto-suficiente? | Dependências fora do cartão | Veredicto |
|---|:--:|---|---|
| **A · PROBLEMA** (l.124–139) | **Não** | `driver` (l.131) — nunca definido em lado nenhum; `ME/CE` (l.132) — nunca expandido; `cone prioritário` (l.138) — indefinido, e a única frase que o explicaria está em §6 (l.224), fora do caminho; "→ escala" (l.138) — destinatário não especificado. `P1.2`/`P1.5`/`P1.6` têm glosa suficiente em §5 (OK) | Falha por 3 conceitos-critério indefinidos. O critério de escolha de eixo (l.131) é inaplicável. |
| **B · CARACTERIZAÇÃO** (l.143–169) | **Não** | `P1.3` (l.159) — única citação externa sem qualquer glosa, e a frase "é assim que se lê `P1.3` aqui" **afirma uma reinterpretação de um texto que o leitor não tem**; `suspenso` (l.162) só aparece em l.108 com outra semântica; "opções vivas" (l.161) pressupõe CARTÃO C aberto; `ME/CE` | Falha. Obriga a carregar o protocolo externo — anula o requisito da l.36. |
| **C · DECISÃO** (l.173–186) | **Quase** | `driver` — não usado no cartão, mas é o 1.º critério de desempate em §3 (l.115), obrigatório para C por C ser sempre concorrencial (l.112); `suspenso: <ramo de B>` (l.184) sem semântica definida; `dominância` (l.183) sem teste; `ME/CE` | O mais próximo de passar. Falha pelo desempate indefinido e pela linha `Poda` ausente. |
| **D · MANDATO** (l.190–203) | **Não** | `P0.7` (l.202) — única ocorrência da família P0.x, zero glosa; "desbloqueio de `P0.7`" é ininteligível sem o protocolo inteiro; `MANDATO` (l.202–203) é o entregável e nunca é especificado; "volta a §2" (l.203) ambíguo por dupla numeração; `ME/CE` | Falha de forma mais grave: a condição de morte do cartão depende de uma regra externa não citável. |

### Custo de contexto do caminho mínimo

| Cartão | Caminho declarado (§0–§3 + cartão + §5) | Caminho real de um agente que lê o ficheiro de cima (inclui 415 palavras de preâmbulo antes de a instrução aparecer na l.48) | Poupança real |
|---|---|---|:--:|
| A | 865 pal ≈ 1,6k tk | 1280 pal ≈ 2,3k tk | 35% |
| B | 988 pal ≈ 1,8k tk | 1403 pal ≈ 2,5k tk | 28% (+ protocolo externo por `P1.3`) |
| C | 846 pal ≈ 1,5k tk | 1261 pal ≈ 2,3k tk | 36% |
| D | 838 pal ≈ 1,5k tk | 1253 pal ≈ 2,3k tk | 36% (+ protocolo externo por `P0.7`) |

O piso teórico (cartão + §0–§3 + §5, sem moldura) seria ~1,5k tk, 43% do documento. **A moldura de síntese custa 415 palavras a todos os agentes.**

---

## 4 · Cobertura do roteamento

Quinze combinações não vazias saem de §2 (l.83: "podem sair-te várias"). A tabela §3 (l.104–110) tem cinco linhas. As combinações com D reencaminham para §2 (l.110), pelo que herdam a cobertura da combinação sem D.

| Combinação | Linha em §3 | Coberta? |
|---|---|---|
| A | l.105 "só A" | Sim |
| B | — | **Não** |
| C | l.106 "só C" | Sim |
| D | l.110 "D + qualquer" | Parcial — "qualquer" pressupõe segunda árvore |
| A+B | l.109 | Parcial — ordem condicionada, sem alternativa; acoplamento por "igual" |
| A+C | — | **Não** |
| A+D | l.110 → A | Sim |
| B+C | l.108 | Sim |
| B+D | l.110 → B | **Não** (herda a lacuna de "só B") |
| C+D | l.110 → C | Sim |
| A+B+C | — | **Não** |
| A+B+D | l.110 → A+B | Parcial |
| A+C+D | l.110 → A+C | **Não** |
| B+C+D | l.110 → B+C | Sim |
| A+B+C+D | l.110 → A+B+C | **Não** |

**Cinco combinações sem linha, seis parciais.** As lacunas não são exóticas: "só B" (caracterizar terreno sem decisão pendente) e "A+C" (procurar causa com opções já na mesa) são dos casos mais frequentes.

---

## 5 · TOP 5

1. **E2-2 — resolver a dupla numeração.** Sem isto a instrução de roteamento aponta para as secções erradas e nada do resto é executável. Correcção barata, ganho total.
2. **E1-1 a E1-7 — bloco de definições mínimo em §0** (`driver`, `ME/CE`, `cone`, `suspenso`, `caminho`) e glosa de toda a citação externa (`P0.7`, `P1.3`). Uma correcção fecha os sete achados e é a única que torna verdadeira a promessa da l.22.
3. **E4-1 + E4-2 — "Como ler" no topo; mandato, método e fontes fora do ficheiro.** Leva a poupança real de ~30% para ~55% e elimina o *kitchen sink*.
4. **E2-1 — reconciliar R1 com CARTÃO B.** Contradição frontal entre a regra comum e metade dos cartões; hoje B e D são ilegais sob R1.
5. **E2-3 — as três linhas em falta em §3** (só B, A+C, A+B+C). Fecha o roteamento: hoje há casos frequentes que saem de §2 e não aterram em lado nenhum.

---

## 6 · Achados

### E1 · Autossuficiência (dominante)

**E1-1 · CRÍTICO · defeito** — `driver` usado quatro vezes, definido zero ✅
*Citação:* l.21, l.115, l.116, l.131
É o 1.º critério de desempate (l.115) e o critério de escolha de eixo do CARTÃO A (l.131); a l.21 chama-lhe "o critério de que este sistema mais depende". Uso órfão (R17/R16).
*Correcção:* definir em §0 — "Driver = a variável cuja variação muda o resultado; o corte não a deve repartir."

**E1-2 · CRÍTICO · defeito** — `P0.7` citado sem glosa
*Citação:* l.202. Única ocorrência da família P0.x. A condição de morte de CARTÃO D ("não sobrevive ao desbloqueio de `P0.7`") exige carregar o protocolo externo inteiro — exactamente o que a l.36 declara requisito duro evitar.
*Correcção:* substituir por condição própria — "morre ao entregar o `MANDATO` e não reabre".

**E1-3 · MAIOR · defeito** — `P1.3` é a única regra P1.x citada sem conteúdo no próprio documento
*Citação:* l.159. As restantes têm glosa: P1.1→R6, P1.2→R1, P1.4→R4, P1.5→l.133, P1.6→R7, P1.7→R8. Pior: "é assim que se lê `P1.3` aqui" afirma uma reinterpretação de um texto ausente.
*Correcção:* enunciar em R2 o que P1.3 obriga, ou remover a citação e manter a regra local.

**E1-4 · MAIOR · defeito** — `ME` / `CE` nunca expandidos ✅
*Citação:* l.132, 159, 179, 180, 198, 212. Verificado: zero ocorrências de "mutuamente exclusivo" ou "colectivamente exaustivo" no documento. A sigla só existe como tag de front matter (l.6), que não está no caminho de leitura.
*Correcção:* expandir em §0 — "ME = mutuamente exclusivo. CE = colectivamente exaustivo."

**E1-5 · MAIOR · defeito** — `cone` usado como condição de morte e como âmbito de impacto, nunca definido
*Citação:* l.138 (condição de morte de A), l.215 (R5). A única frase que o explicaria (l.224) está em §6, que a l.48 manda ignorar.
*Correcção:* mover l.224 para §0 e definir "cone = conjunto de ramos alcançáveis a jusante por travessia de arestas".

**E1-6 · MAIOR · defeito** — `suspenso` com dois sentidos incompatíveis
*Citação:* l.108 e l.184 (dependência declarada com referente: `suspenso: <ramo de B>`) vs l.162 (marca de ramo não discriminante, sem referente). Nenhum dos dois é definido. Regras violadas: R7/R17.
*Correcção:* reservar `suspenso: <ramo>` para dependência; usar outro rótulo (`retido`) no caso de B.

**E1-7 · MAIOR · defeito** — Promessa de vocabulário não cumprida
*Citação:* l.38 promete "vocabulário do protocolo — ramo, aresta, poda, fecho, condição de morte, triagem, caminho, pressuposto, frente, slug, cone" e o documento não define nenhum. `frente` nunca reaparece; `fecho` nunca reaparece fora do título de §6; `slug` aparece uma vez (l.215) sem definição. Regra violada: R19 (órfãos).
*Correcção:* definir os termos em §0, ou apagar a lista e a promessa.

**E1-8 · MENOR · defeito** — Artefactos invocados e não especificados
*Citação:* l.202–203 (`MANDATO` é o entregável de D sem formato, campos ou critério de aceitação); l.217 (`projecção` invocada uma única vez, sem definição, e R7 manda registar a razão da poda mas diz que a projecção nunca a mostra — sem dizer onde fica)
*Correcção:* "`MANDATO` = eixos nomeados com as palavras do humano + exemplos de contraste"; "razão registada no ramo".

### E2 · Integridade canónica

**E2-1 · CRÍTICO · defeito** — R1 contradiz metade dos cartões ✅
*Citação:* l.211 (R1: "Um eixo por nó (`P1.2`). Compõem-se por níveis, **nunca no mesmo nível**") vs l.145 ("Os ramos de primeiro nível não são partes. **São eixos**"), l.164 ("exaustividade **dentro de cada eixo, não entre eixos**"), l.212 (R2 pressupõe a coexistência)
B e D são ilegais sob R1.
*Correcção:* R1 — "Um eixo por nó em A e C; em B e D os eixos coexistem no primeiro nível."

**E2-2 · CRÍTICO · defeito** — A dupla numeração torna a instrução de roteamento literalmente falsa ✅
*Citação:* l.48 vs l.14, 26, 34, 44, 230. Estrutura verificada: `## 0-4` externos (Sumário, Mandato, Método, Corpo, Fontes) e `### 0-6` internos (Definição, Porta, Roteamento, Tabela, Cartões, Regras, Fecho).
"Lê §0 e §1" aponta, no nível externo, para Sumário e Mandato. "Lê só os cartões que te saíram em **§4**" aponta para **§4 Fontes** (l.230), que está vazia. "Volta a §2" (l.110, l.203) aponta para Método. A nota da l.46 não resolve — cita-se a numeração de um relatório que o agente não tem. Regras violadas: R18/R24/R22.
*Correcção:* renumerar o corpo interno (§A0–§A6) ou eliminar a moldura externa.

**E2-3 · MAIOR · defeito** — Cinco combinações do roteamento sem linha em §3
*Citação:* l.104–110 vs l.83. Ver tabela §4. Um agente com G3 isolado sai do roteamento sem instrução de ordem, acoplamento ou concorrência.
*Correcção:* acrescentar linhas "só B", "A+C", "A+B+C" e trocar "D + qualquer" por "D, sozinha ou acompanhada".

**E2-4 · MAIOR · defeito** — A triagem substituta de B não tem teste aplicável em percurso "só B"
*Citação:* l.161 ("este eixo discrimina entre as opções vivas?") — num percurso "só B" não há opções vivas; as opções pertencem a C. O cartão contradiz o seu próprio teste de suficiência (l.167), que já não depende de opções.
*Correcção:* "Discrimina entre um objecto que aqui seria bom e um que seria mau?" — alinhar com l.167.

**E2-5 · MENOR · defeito** — Tratamento inconsistente do mesmo problema em dois cartões
*Citação:* l.133 (triagem de A: "mudava a decisão?") vs l.161 (B diagnostica em si própria que "não há ainda decisão contra a qual triar")
*Correcção:* reformular a triagem de A — "mudava a causa provável?".

**E2-6 · MENOR · defeito** — Reafirmação de obrigações
*Citação:* l.118 ≈ l.218 (quase palavra a palavra); l.131/l.178 ≈ l.211 ("um eixo por nó (`P1.2`)" três vezes); l.169 ≈ l.183 (proibição de pesos normalizados em B e em C)
§3 e §5 estão ambos no caminho mínimo de todos os agentes — a duplicação é custo puro, não redundância defensiva. Regras violadas: R6/R21.
*Correcção:* manter em §5, cortar de l.118, 131, 178; promover l.169/l.183 a R9 comum.

**E2-7 · MENOR · defeito** — "Regras comuns" com derrogações não marcadas
*Citação:* l.217 (R7: poda com razão) vs l.201 (D: "não se poda") e l.162 (B: "proibida enquanto a árvore está aberta"). Nada marca quais das oito regras são derrogáveis por cartão.
*Correcção:* R7 — "salvo onde o cartão o proíba (B enquanto aberta, D sempre)".

### E3 · Clareza

**E3-1 · MAIOR · risco** — As portas de roteamento sobrepõem-se e não há desempate
*Citação:* l.86 (G1: "estado indesejado cuja causa se procura") e l.93 (G3: "falta conhecer o objecto ou o terreno antes de se poder escolher") sobrepõem-se em quase todos os casos reais; l.96 (G4) não diz quem pôs as opções na mesa nem se contam opções implícitas
Duas sessões sobre o mesmo caso produzem roteamentos diferentes — e o documento só tem desempate entre árvores concorrentes, não entre portas.
*Correcção:* um exemplo-âncora de uma linha por porta, e a nota "se G1 e G3 saírem ambas, ver linha A+B".

**E3-2 · MAIOR · defeito** — "Integridade do driver" é circular no CARTÃO A
*Citação:* l.115 — manda escolher o corte que mantém "o driver **provável**" inteiro, quando em A o driver é precisamente o que ainda se desconhece. É o 1.º critério de desempate, e o que a l.21 declara mais estruturante.
*Correcção:* inverter a ordem — assimetria esperada primeiro; integridade do driver só quando há driver candidato nomeado.

**E3-3 · MENOR · defeito** — Referência posicional e ordem condicional sem alternativa
*Citação:* l.109 — a célula de Acoplamento diz "igual", referência a uma célula escrita em termos de B e C, que o leitor tem de traduzir para A e B (R22). A coluna Ordem é condicional ("quando a causa depende de terreno desconhecido") sem dizer qual é a ordem no caso contrário.
*Correcção:* escrever a célula por extenso e acrescentar "caso contrário, A e B em paralelo".

**E3-4 · MENOR · defeito** — Quatro designações para a mesma coisa
*Citação:* l.105, 108, 122, 30 — "cartão", "caso", "propósito", "tipo de árvore". A coluna "Árvores" de §3 mistura duas contagens na mesma célula ("1 propósito, ≥2 concorrentes").
*Correcção:* fixar "propósito = cartão" e separar a coluna em "propósitos" e "árvores concorrentes".

### E4 · Arquitectura de informação

**E4-1 · CRÍTICO · defeito** — A instrução "Como ler" chega depois de 21% do documento
*Citação:* l.48 vs l.36. São 415 palavras de sumário, mandato e método que nenhum agente precisa. O documento declara a economia de contexto requisito duro e gasta-a antes de a enunciar. Um agente só descobre que podia ter saltado depois de já ter lido.
*Correcção:* mover o bloco "Como ler" para imediatamente abaixo do título (l.12).

**E4-2 · MAIOR · defeito** — *Kitchen sink page*: síntese e documento operacional no mesmo ficheiro
*Citação:* l.26–42 (mandato, método), l.230–232 (§4 Fontes, secção vazia mantida por simetria de template: "Sem secção de fontes no relatório original", e que colide com o §4 interno — Cartões); l.28, 40, 46, 232 são história de produção do documento dentro do corpo canónico (R23)
*Correcção:* passar §1, §2 e §4 para front matter ou documento irmão; deixar no ficheiro §0 + corpo.

**E4-3 · MAIOR · risco** — Conteúdo operacional colocado fora do caminho de leitura
*Citação:* l.222–228 (§6 Fecho contém a única explicação de cone/travessia, l.224, e a justificação operacional do ramo morto, l.226) vs l.48 ("Ignora o resto")
Nenhum agente o lê.
*Correcção:* mover l.224 para §0 e l.226 para R7; apagar §6.

**E4-4 · MENOR · risco** — §3 impõe custo a B e D sem contrapartida
*Citação:* l.102–120. §3 tem 236 palavras, é a secção mais pesada do caminho mínimo, e é lida inteira por todos — incluindo o bloco Concorrência/Desempate (l.112–116), que só se aplica a A e C.
*Correcção:* mover l.112–116 para dentro dos cartões A e C.

### E5 · Operacionalidade

**E5-1 · MAIOR · defeito** — Metade de §5 é conselho com etiqueta de regra
*Citação:* l.211–218. R1, R2, R3, R4 e R8 não têm consequência de incumprimento. Só R5 ("redesenha-se, não se remenda"), R6 ("sem ela, não abras") e R7 (razão registada) a têm — e §1 (l.67–76) tem-na nas cinco linhas.
*Correcção:* acrescentar a cada R a acção de reparação, no formato de R5.

**E5-2 · MAIOR · defeito** — Os critérios que fecham árvores e desempatam concorrentes são os menos testáveis
*Citação:* l.163 ("saturação: dois ciclos consecutivos de investigação" — sem definir ciclo); l.138 ("cone prioritário esgotado" — sem definir prioritário nem esgotado); l.115 ("assimetria esperada", "accionabilidade" — sem escala); l.183 ("dominância" — sem teste); l.112 ("eixos conceptuais distintos" — sem critério de distinção). Regra violada: R10.
São exactamente os pontos onde o julgamento não especificado custa mais: duas sessões param em sítios diferentes.
*Correcção:* um teste binário de uma linha ao lado de cada primeira ocorrência.

**E5-3 · MENOR · defeito** — Nenhum vocabulário modal declarado
*Citação:* l.77, 147, 118, 162, 201, 161, 200. Coexistem imperativo ("não abras", "Declara"), proibição impessoal ("Nunca se fundem", "proibida", "não se poda") e constatação ("não se aplica", "é defeito"). O agente não distingue obrigação de descrição.
*Correcção:* declarar em §0 que o imperativo é obrigação e uniformizar as proibições numa só forma.

**E5-4 · MENOR · defeito** — A grelha dos quatro cartões não é a mesma
*Citação:* l.128–139, 157–165, 176–186, 195–203. C não tem linha `Poda` (A, B e D têm); A não tem `Ao fechar` (B tem); só B tem `Forma`; só A tem `Ordem de ataque`.
O agente não distingue omissão de silêncio deliberado, e não pode comparar cartões porque nunca lê dois.
*Correcção:* fixar a mesma lista de linhas nos quatro cartões, com "—" onde não se aplica.

---

## 7 · O que está bem

A porta de entrada (l.67–76) é a melhor peça do documento: cinco sinais, cada um com destino e consequência — é o formato que §5 devia ter.

A assimetria concorrência-sim em A/C, concorrência-não em B/D (l.112–113) é uma distinção real, bem enunciada e com justificação curta.

O reconhecimento explícito de que o roteamento devolve vários cartões (l.83) resolve de facto a pergunta "de quantas árvores preciso" — o problema é a tabela que se lhe segue, não a ideia.

Os dois registos de CARTÃO B (l.147–154) e a obtenção de eixos por contraste em D (l.197) são as instruções mais difíceis do conjunto e estão certas.
