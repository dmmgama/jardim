---
created: 2026-09-20 04:49
chat: Auditoria de documentos de governo por agentes
summary: >
  Auditoria integral de ARQUITECTURA-PROPOSTA2.md em cinco eixos, mais auditoria de
  integridade dos 35 marcadores de alteração: 28 achados com citação de linha.
---

# Auditoria — `ARQUITECTURA-PROPOSTA2.md`

**Documento:** 654 linhas · governance spec · PT · versão paralela com 35 marcadores `[Mnn]`
**Modo:** `cannon-rules` audit, uma passagem completa. Vocabulário modal declarado na l.88
**Diataxis aplicado:** *Kitchen Sink*, *Thesaurus Trap*, *Dead End*, *Abstract Description*, *Internal Jargon*, *Orphan Docs*. Excluído funil de adopção, SDK, sandbox, partner docs.

---

## 1 · Veredicto

**Como especificação autónoma não serve:** seis alterações centrais (`[M03]`, `[M11]`, `[M12]`, `[M16]`, `[M25]`, `[M29]`) estão redigidas como *delta* — "é retirada", "convertida em regra", "coluna acrescentada", "deixa de ser nula" — e são indecifráveis sem a versão de referência, que não acompanha.

**Como diff também não serve:** não há texto anterior em lado nenhum, pelo que ninguém reconstrói o que mudou.

O documento falha nos dois papéis que tenta acumular.

**Defeito dominante:** narração de mutação dentro do corpo canónico (R23/AP19), que arrasta consigo contradições substantivas — a mais grave é `[M24]` a tornar irrecuperável exactamente a razão de fecho que `[M11]` acabou de mandar registar.

---

## 2 · Contagem

| Eixo | CRÍTICO | MAIOR | MENOR | Total |
|---|:--:|:--:|:--:|:--:|
| E1 · Autossuficiência | 1 | 3 | 0 | 4 |
| E2 · Integridade canónica | 4 | 5 | 1 | 10 |
| E3 · Clareza | 0 | 1 | 3 | 4 |
| E4 · Arquitectura de informação | 1 | 2 | 1 | 4 |
| E5 · Operacionalidade | 1 | 4 | 1 | 6 |
| **Total** | **7** | **15** | **6** | **28** |

Defeitos: 24 · Riscos: 4.
*Nota de numeração: o identificador B9 não foi atribuído no relatório original; a sequência salta de B8 para B10.*
✅ = achado verificado mecanicamente de forma independente.

---

## 3 · Auditoria de marcadores

Extracção mecânica de todas as ocorrências `[Mnn]` no corpo (l.1–613), confrontada com o índice §5 (l.618–654) e com a contagem anunciada no front matter (l.6).

**Conformes — 31 de 35:** M01, M02, M03, M04, M06, M07, M08, M09, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M25, M26, M27, M28, M29, M30, M31, M32, M34. Presentes no corpo, presentes no índice, âmbito declarado coincidente com as linhas onde ocorrem.

**Não conformes:**

| Marca | Corpo (l.) | §5 declara | Veredicto |
|---|---|---|---|
| **M05** | 61 (§1.4), 576 (§3.1) | `1.4, 3.1 — critério e garantia: tectos numéricos` | ✅ **CRÍTICO.** O âmbito bate, a substância não. A garantia da l.576 é "O sistema não consome sessões / existe sessão cuja função é verificar alinhamento" — assunto de **M04**, não tectos. Verificado: **zero ocorrências de "tecto" em §3.1**. O índice descreve uma linha que não foi escrita. |
| **M04** | 60, 63 (§1.4) | `1.4` | **MAIOR.** A sua substância tem efeito em §3.1 (l.576) mas o índice restringe-o a 1.4. Espelho do erro de M05. |
| **M24** | 168, 344, 451, **582** | `2.2, 2.4.5, 2.4.8` | **MAIOR.** Ocorrência em §3.2 (l.582, "regeneração do mapa") ausente do âmbito declarado. Comparar com M22, que na mesma l.582 declara correctamente `3.2`. |
| **M33** | 602, 606, 610 (§4) | `4 — mitigações de T1, T3 e T5` | **MENOR.** Um identificador para três alterações independentes em três tensões distintas. Viola R13: não é possível citar "a mitigação de T5" por marcador. |
| **M35** | ausente do corpo; só no título de §5 (l.616) | `5 — este índice` | ✅ **CRÍTICO de contagem.** Ver abaixo. |

**Contagem** ✅ — Front matter l.6: "trinta e quatro alterações `[M01]` a `[M34]`". Índice §5: **35 linhas, até M35**, auto-referencial. Uma das duas afirmações é falsa e o documento não diz qual.

Acresce que a convenção de leitura (l.11) — "secções sem marcador são idênticas em substância" — **não prevê secções inteiramente novas**: §5 não existe na referência e §4·T6 também não, pelo que a convenção não cobre o seu próprio índice.

**Marcador que altera e deixa o texto adjacente no comportamento antigo:** confirmado em três pontos — ver B11.

**Alteração substantiva não marcada:** não detectável com fiabilidade sem a referência. O que é detectável, e está reportado, é o inverso: alterações marcadas que não são substantivas (`[M16]`, `[M29]` anunciam uma coluna, não uma regra) e texto não marcado que a convenção obriga a considerar idêntico mas que descreve comportamento que outra alteração revogou (B11).

---

## 4 · TOP 5

1. **B1** (l.168 vs 449) — `[M24]` torna irrecuperável a razão que `[M11]` acabou de mandar registar. Mata a garantia "Becos não reabrem" e esvazia P1.6/P1.7. Contradição frontal, custo de correcção mínimo.
2. **B4 + E1f** (l.576, 624; P0.5/P1.9/P1.10/P2.8) — quatro regras de tecto sem garantia, sem contador e sem auditor, e uma linha de garantia com o marcador errado. Todo o bloco `[M05]`/`[M10]`/`[M13]` é hoje declaração de intenção.
3. **A1** (l.46, 166, 313, 430, 463, 552, 594) — a narração de diff dentro do corpo canónico é o que impede o documento de funcionar isoladamente. Sete frases a reescrever resolvem o defeito dominante.
4. **B2** (l.432 vs 307/491) — o confronto de pesquisa está alocado a um componente que só corre no merge. `[M21]`/`[M23]` não são executáveis como estão, e `[M30]` depende deles.
5. **B3** (l.493–498) — P9.4/P9.1/P9.6/P9.3 fora de ordem, com dois identificadores fantasma sob um título que diz "quatro". O achado mais barato de corrigir e o mais visível para quem tenta citar uma regra.

---

## 5 · Achados

### E1 · Autossuficiência

**A1 · CRÍTICO · defeito** — Sete passagens do corpo canónico descrevem a própria mutação
*Citação:* l.46 ("A exclusão … **é retirada**"), l.166 ("Fechado regista **igualmente**"), l.313 ("Coluna de origem **acrescentada**"), l.430 ("**A versão que segue apenas as arestas directas** deixa escapar"), l.463 ("**Convertida** em regra"), l.552 ("Coluna de via **acrescentada**"), l.594 ("A garantia **deixa de ser nula e passa a parcial**")
Um agente sem a referência não sabe o que era nulo, o que se acrescentou, nem o que "igualmente" significa. Regras violadas: R23; AP19.
*Correcção:* reescrever as sete em forma prescritiva ("A projecção contém X"; "A garantia é parcial: …") e empurrar o delta para o índice §5.

**A2 · MAIOR · defeito** — `arestas.db` nunca é especificado
*Citação:* l.318 ("base relacional de ficheiro único"), l.340 ("nós, arestas, níveis"), l.356, l.612 ("ficheiro binário"). Substrato das garantias l.567 e l.568 e do cálculo do cone.
Não há esquema, não há contrato de escrita, e nunca se declara que as dependências de **P1.4** são o que alimenta as arestas — a ligação entre a regra que obriga a declarar e o substrato que armazena está apenas implícita.
*Correcção:* acrescentar regra em P1 que vincule a declaração de P1.4 à escrita de aresta, e especificar as colunas de `arestas.db`.

**A3 · MAIOR · defeito** — "Canal de alerta" obrigatório e nunca definido
*Citação:* l.95 (P0.6), l.326, l.438, l.572
Não há critério que qualifique um canal, não há formato de item, e não há comportamento declarado para canal indisponível — ao contrário de **P9.3**, que trata explicitamente o hook indisponível.
*Correcção:* definir "canal de alerta" em §2.4.4 e acrescentar a P9 a regra de recusa/degradação em canal indisponível, simétrica a P9.3.

**A4 · MAIOR · defeito** — Duas garantias assentes num artefacto que o documento diz não existir
*Citação:* l.565, l.566 (§3.1 dá "validador de esquema" como via de "O estado não apodrece" e "O lixo não entra") vs l.544 (`[M28]`: "Sem ele, é convenção")
*Correcção:* marcar as duas vias como `por implementar` ou rebaixar as garantias a intenção até o esquema existir.

### E2 · Integridade canónica

**B1 · CRÍTICO · defeito** — `[M24]` contradiz o mecanismo de bloqueio ✅
*Citação:* l.168 ("as razões … residem no substrato e são **devolvidas apenas por mecanismo de bloqueio**") vs l.449 ("O alerta devolve o identificador da decisão e o facto de existir. **Nunca** o conteúdo do debate, a alternativa rejeitada ou **a razão**")
Directamente incompatíveis. **Consequência: a razão que `[M11]`/P1.7 obriga a registar não tem leitor nenhum**, e a garantia "Becos não reabrem" (l.570) perde o mecanismo.
*Correcção:* abrir excepção explícita na l.449 para a razão de fecho/poda, ou retirar de l.168 a cláusula "devolvidas apenas por mecanismo de bloqueio".

**B2 · CRÍTICO · defeito** — O confronto de pesquisa está alocado a um componente que não pode executá-lo
*Citação:* l.432 (`[M23]` atribui o confronto à "passagem semântica", executado "antes de [a pesquisa] ser executada", i.e. dentro da sessão — S4, l.403) vs l.428, 567 (a passagem semântica é uma das três passagens do *watcher*), l.491 (o detector semântico corre "dentro do watcher"), l.307 (o watcher dispara "cada merge")
Um componente que só corre no merge não pode intervir antes de uma pesquisa intra-sessão.
*Correcção:* mover o confronto de pesquisa para o hook de caminho (S4) e deixar na passagem semântica do watcher apenas a detecção pós-merge.

**B3 · CRÍTICO · defeito** — Regras P9 fora de ordem, com identificadores fantasma ✅
*Citação:* l.493–498. `[M26]` anuncia "**Quatro** regras de alocação, com identificador" e enuncia **P9.4, P9.1, P9.6, P9.3** — por esta ordem. **P9.2 e P9.5 nunca são enunciadas em lado nenhum.** O espaço P3–P8 está inteiramente vazio, sem nota de reserva. Regras violadas: R24, R18.
*Correcção:* renumerar para P9.1–P9.4 por ordem, ou enunciar P9.2 e P9.5 e corrigir "quatro" no título.

**B4 · CRÍTICO · defeito** — Regra sem garantia e garantia com marcador errado ✅
*Citação:* l.576 (garantia marcada `[M05]` é sobre sessões de verificação — assunto de M04) vs l.61, l.624 (índice declara que M05 produz em 3.1 uma garantia sobre tectos, que não existe)
Resultado duplo: **regra sem garantia** — P0.5, P1.9, P1.10 e P2.8 criam tectos e a tabela de garantias permanentes ignora-os — e **garantia com marcador errado**.
*Correcção:* remarcar a l.576 como `[M04]` e acrescentar linha de garantia "Os tectos são respeitados" marcada `[M05]`.

**B5 · MAIOR · defeito** — `[M33]` atribui ao auditor uma verificação que `[M32]` não lhe dá
*Citação:* l.610 ("o tecto … verificado pelo auditor") vs l.588 (`[M32]` fixa a listagem do auditor em sete itens, nenhum deles o tecto)
A listagem é declarada "fixa", pelo que não há margem interpretativa.
*Correcção:* acrescentar "árvores e frentes acima do tecto" à listagem de `[M32]`.

**B6 · MAIOR · defeito** — Colisão de espaço de nomes: M1–M7 vs `[M01]`–`[M35]` ✅
*Citação:* l.197–203 (método de procura usa M1 a M7); l.216 ("os pressupostos por ordem de **M5**"); l.203 ("antes de **M6** devolver resultado")
Genuinamente ambíguas contra `[M05]` (tectos) e `[M06]` (mandato declara canal). Regra violada: R18 (unicidade de âncora).
*Correcção:* renomear os passos do método para `Q1`–`Q7` ou `MP1`–`MP7`.

**B7 · MAIOR · defeito** — A prosa de §2.2 é uma segunda enunciação do Protocolo P1
*Citação:* l.134, 136, 138, 146, 150, 156, 158, 166 contra P1.2, P1.3, P1.5, P1.8, P1.9, P1.11, P1.12, P1.13
Oito obrigações ditas duas vezes, em redacções diferentes, uma com identificador e outra sem. Regras violadas: R6/R21.
**O risco já se materializou:** `[M09]` alterou P1.13 (l.184) e deixou intacta a versão em prosa (l.146), que usa ainda outro modal ("tem de recair"). *Este é o caso mais literal de deriva não declarada — dentro do documento que existe para a tornar impossível.*
*Correcção:* reduzir a prosa de §2.2 a explicação conceptual e remeter cada obrigação para o identificador P1.x.

**B8 · MENOR · defeito** — Seis formas modais onde o vocabulário declara três
*Citação:* declaração em l.88. Usos divergentes: l.100 ("Nenhuma frente **pode** ser aberta" — permissão negativa a significar proibição, R9), l.146 ("tem de recair"), l.156 ("não se fundem"), l.184 ("só **pode**"). Acresce P9.1 (l.496), que empacota duas obrigações e dois modais numa frase, violando R12.
*Correcção:* converter l.100 e l.184 para `não pode`, l.146 e l.156 para `deve`/`não pode`, e partir P9.1 em duas regras.

**B10 · MAIOR · defeito** — Item do auditor sem substrato onde persistir
*Citação:* l.588 (`[M32]` encarrega o auditor de listar "alertas descartados que reapareceram") vs l.339 (`ALERTA` é escrito por **substituição**), l.353 (proíbe estado e evidência no mesmo ficheiro), l.436 (regra do descartado)
Um ficheiro substituído não guarda histórico de descartes. Nem o item do auditor nem a regra da l.436 têm onde persistir.
*Correcção:* declarar um ficheiro de acumulação para hashes descartados, ou retirar o item da listagem de `[M32]`.

**B11 · MAIOR · defeito** — Texto não marcado continua a codificar o comportamento revogado
*Citação:* `[M19]`/`[M31]` mudam o alerta de ficheiro-que-alguém-abre para entrega empurrada. Três passagens **não marcadas** — que a convenção da l.11 obriga a ler como "idênticas em substância" — descrevem o comportamento antigo: l.53 (critério de sucesso mede "o **ficheiro** de alertas vazio"), l.322 (linha do *Watcher* em §2.4.4 não menciona canal nem invocação), l.339 (`ALERTA` em §2.4.5 dá como escrita apenas "substituição")
O sintoma `[M01]` ("a detecção produz ficheiro, não notificação") é exactamente o que estas três linhas continuam a codificar.
*Correcção:* propagar `[M19]` às l.53, 322 e 339 e marcá-las.

### E3 · Clareza

**C1 · MAIOR · defeito** — "Nível" designa quatro coisas sem relação
*Citação:* l.274 (patamares hierárquicos L0–L4), l.340 (coluna de `arestas.db`), l.420 (dois patamares do gate de fecho), l.442 (quatro níveis de protecção de slug). A l.402 — "bloqueia ou alerta, conforme **o nível**" — é impossível de resolver sem adivinhar qual dos quatro. Regras violadas: R7/R17; AP *Thesaurus Trap* invertido.
*Correcção:* fixar "nível" para L0–L4 e renomear os outros três ("patamar de gate", "grau de protecção", coluna de `arestas.db`).

**C2 · MENOR · defeito** — Dois nomes para o conteúdo do `INBOX`
*Citação:* l.511 ("frente marca **challenges** no INBOX" — termo inglês, nunca definido) vs l.341 ("descobertas por processar")
*Correcção:* substituir "challenges" por "descobertas" na l.511.

**C3 · MENOR · risco** — Comportamento da sessão em `decidido` indeterminado
*Citação:* l.445 (o nível `decidido` "alerta, **pede confirmação humana**") vs l.416 ("Não existe estado de espera") e l.401 (padrão declarado em S4 é bloquear-e-continuar)
Não se sabe se a sessão prossegue, bloqueia, ou fecha com `carece_aprovacao`.
*Correcção:* declarar explicitamente o comportamento por referência a uma das três saídas já definidas.

**C4 · MENOR · risco** — Frase de efeito sem critério verificável
*Citação:* l.121 ("consultado por travessia e **nunca lido**") — consultar é ler. A intenção presumível já está na frase seguinte; a formulação paradoxal não é testável (R10).
*Correcção:* substituir por "legível apenas por travessia mecânica; nenhum agente lhe acede".

**C5 · MENOR · defeito** — "Zona protegida" nunca definida e em colisão
*Citação:* l.496 (P9.1). Colide com as zonas de escrita por perfil (l.81) e com os níveis de protecção de slug (l.442).
*Correcção:* definir "zona protegida" em §2.4.8 ou reformular P9.1 em termos de "zona de escrita".

### E4 · Arquitectura de informação

**D1 · CRÍTICO · defeito** — Contradição factual no metadado de âmbito ✅
*Citação:* l.6 ("trinta e quatro alterações `[M01]` a `[M34]`") vs l.616–654 (35 linhas, até `[M35]`)
*Correcção:* corrigir o front matter para "trinta e cinco alterações `[M01]` a `[M35]`".

**D2 · MAIOR · defeito** — Âmbito declarado de `[M24]` omite §3.2
*Citação:* l.643 vs l.582
*Correcção:* `M24 | 2.2, 2.4.5, 2.4.8, 3.2`.

**D3 · MAIOR · defeito** — Convenção de leitura incompleta em dois pontos
*Citação:* l.11. Não declara que existe um índice em §5 — o leitor percorre 600 linhas de marcadores antes de saber que há tabela. Não prevê secções inteiramente novas: a regra "secções sem marcador são idênticas em substância" não classifica §5 nem T6. AP *Dead End*: nenhuma passagem marcada remete para a referência nem diz como obtê-la.
*Correcção:* acrescentar à l.11 o ponteiro para §5 e a regra para secções novas.

**D4 · MENOR · defeito** — `[M33]` marca três mitigações independentes
*Citação:* l.602, 606, 610
*Correcção:* desdobrar em `[M33]`, `[M33b]`, `[M33c]` ou renumerar.

### E5 · Operacionalidade

**E1f · CRÍTICO · defeito** — Quatro regras de tecto sem mecanismo nenhum
*Citação:* P0.5 (l.94), P1.9 (l.180), P1.10 (l.181), P2.8 (l.230)
Nenhuma ferramenta de §2.4.4 conta árvores ou frentes abertas; nenhum ficheiro de §2.4.5 guarda a contagem; a listagem fixa do auditor (l.588) não a verifica; §3.1 não tem garantia correspondente (B4). Quatro obrigações sem detecção e sem consequência — intenção declarada, não regra operacional.
*Correcção:* atribuir a contagem ao watcher no merge e acrescentar o item à listagem de `[M32]`.

**E2f · MAIOR · defeito** — A falha que a garantia promete detectar é indetectável
*Citação:* l.572 — garantia `[M31]` "O alerta chega"; detecção declarada: "alerta correcto e **não lido**"
Nada no documento observa leitura: o canal é um serviço de notificação sem retorno, não há recibo, e a triagem é invocada pelo watcher independentemente de alguém ler.
*Correcção:* substituir a detecção por algo observável ("item de alerta sem sessão de triagem correspondente no prazo X") ou declarar recibo de leitura.

**E3f · MAIOR · defeito** — Duas alterações que prometem um identificador e não o entregam
*Citação:* l.463 (`[M25]`: "uma regra verificável por mecanismo tem **identificador e consequência de incumprimento**, como as restantes" — e não lhe é atribuído identificador nenhum); l.528 (`[M27]`: "A condição é regra, **com identificador**" — idem)
Contrasta com `[M26]`, que na mesma matéria atribuiu P9.x. Regra violada: R13.
*Correcção:* atribuir identificadores (p. ex. P3.1 para a regra de saída, P3.2 para a condição de adopção) e enunciar a consequência.

**E4f · MAIOR · defeito** — Uma garantia, três mecanismos incompatíveis
*Citação:* l.571 (`[M30]` dá como via a "pesquisa vectorial") vs l.432 (`[M23]` atribui o mesmo trabalho à passagem semântica, que é "chamada única de modelo", l.428) vs l.606 (T3: a ferramenta vectorial "está em fase anterior à versão 1")
Garantia permanente sustentada por tecnologia por implementar e por dois mecanismos que não são o mesmo.
*Correcção:* fixar um mecanismo e marcar a garantia como `por implementar` até existir.

**E5f · MAIOR · defeito** — `[M28]` é um diagnóstico, não uma alteração
*Citação:* l.544. Constata que campos fechados sem validador são convenção e não cria regra, esquema, responsável nem prazo. Marcada como alteração, é substancialmente inerte — e deixa duas garantias de §3.1 (l.565, 566) apoiadas num artefacto inexistente (ver A4).
*Correcção:* converter em regra com identificador ("A escrita em `debates/*.json` **deve** ser rejeitada se não validar contra o esquema") ou passar `[M28]` a tensão em §4.

**E6f · MENOR · defeito** — O fluxo L3·F5 perde dois terços dos disparos
*Citação:* l.391 (F5 dispara a travessia transitiva apenas em "Fecho de ramo") vs l.430 (o mecanismo declara três disparos: ramo fechado, ramo podado, **ou decisão alterada**)
*Correcção:* alinhar F5 com os três disparos da l.430.

---

## 6 · O que está bem

O vocabulário normativo é declarado antes de qualquer regra (l.88) — R1 cumprido, o que é raro em documentos deste género.

A disciplina marcador-a-marcador é genuinamente alta: 31 dos 35 marcadores batem certo entre corpo e índice, incluindo âmbitos múltiplos difíceis como `[M22]` (quatro secções) e `[M15]` (três).

§4 declara cinco tensões por resolver e `[M34]` acrescenta uma que é **desfavorável à própria proposta** — o documento não esconde o custo do substrato de arestas.

A separação entre estado substituível e evidência acumulável (l.353) e o princípio "um nível nunca escreve no nível acima" (l.278) são as duas regras estruturais que sustentam o resto, e estão ambas bem formuladas.
