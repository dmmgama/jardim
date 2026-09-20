# Auditoria consolidada — `arquitectura-governo-arvore.md`

**Alvo:** revisão de 2026-09-20 06:10 (781 linhas · 60 regras · 17 garantias · Anexo A com 16 esquemas)
**Data da auditoria:** 2026-09-20
**Lentes:** quatro auditorias independentes, sem contacto entre si

| Lente | Foco | Produziu |
|---|---|---|
| Master Plan Architect | red teaming, pressupostos frágeis, blast radius, anti-scope-creep | 26 achados · 7 vectores de falha fora de T1–T5 · lista de cortes |
| Software Architect | domínio, fronteiras, acoplamento, concorrência, trade-offs | 32 achados · integridade do Anexo A campo-a-campo · 2 ADRs |
| Workflow Architect | todos os caminhos, máquinas de estado, contratos de handoff | 40 achados · registo de 32 workflows · 6 máquinas de estado · 22 resíduos |
| Blind spot pass (método Thariq Shihipar, Anthropic) | enquadramento: o que nunca foi considerado | 12 pressupostos tácitos · 7 domínios ausentes · 12 perguntas · 8 referências externas |

---

## 1 · Veredicto consolidado

O documento é **forte como modelo conceptual e fraco como contrato executável**. A tese central — separar mandato, caminho e frente; matar cortes estéreis de graça com o crivo antes de os testar caro com frentes; distinguir deriva de inflexão — é sólida e rara. A disciplina formal (numeração aditiva, entrada única por termo, detector e consequência por regra) está acima da média do género.

O que falha é a camada de execução, e falha de forma sistemática: **foi especificada por nome e não por contrato**. As quatro lentes, sem se conhecerem, convergiram no mesmo diagnóstico por caminhos diferentes:

- **Não é implementável como está.** Pelo menos oito artefactos que os hooks têm de ler não existem: `Perfis e zonas`, o mapa trajecto→nível, o mapa trajecto→modo de escrita, a projecção, o estado da árvore, o `pai` dos nós, o registo de corridas do watcher, o registo de regras.
- **Três garantias não têm regra que as implemente** (G10, G11, G12) e o actor mais importante do sistema — o watcher — não aparece no detector de nenhuma das 60 regras.
- **Há perda de dados silenciosa em quatro sítios**: `ALERTA` substituído em corridas concorrentes, itens do gate destruídos pela corrida seguinte, `HALT` a bloquear a selagem, merge falhado depois de uma selagem irreversível.
- **O documento reprova o seu próprio P7.3**: tem obrigações em prosa que a Convenção de leitura desobriga, garantias sem regra, termos sem entrada em §0, e entradas em §0 sem uso (`Driver` não reaparece uma única vez).
- **E é cego ao custo de se operar a si próprio**: zero ocorrências de *token*, *custo*, *orçamento*, *latência*, *métrica*, *sucessão*, *migração*, *arquivo*.

Contagem de cobertura operacional: das 32 cadeias que os próprios fluxos do documento pressupõem, **6 estão especificadas, 11 parciais e 15 ausentes**.

---

## 2 · Bloco A · Convergências

Achados encontrados **independentemente por duas ou mais lentes**. São os mais sólidos do lote: sobreviveram a olhares que procuravam coisas diferentes.

| # | Convergência | Lentes | Consequência |
|---|---|---|---|
| **C1** | **P3.2 contradiz P3.3**, ambas `hook · bloqueia`. P3.2 proíbe contexto acima do nível imediato; P3.3 obriga a carregar os não-objectivos (L0) inteiros em toda a sessão que classifique. A excepção vive só em prosa (§2.4.2) — e a Convenção de leitura diz que prosa não obriga, logo também não isenta. | Plan · Arch | O hook bloqueia se carregar e bloqueia se não carregar. Impasse em S3 para todos os perfis, porque por §2.4.2 todos classificam. |
| **C2** | **`ALERTA` é substituição, o watcher dispara a cada merge, e não há lock, ordem nem versão.** Acresce que P3.16 manda o *gate* escrever num ficheiro cujo escritor declarado é o watcher. | Plan · Arch · Flow | Dois fechos próximos e a segunda corrida apaga os itens da primeira. Todo o fecho brando com `carece_aprovacao` é destruído no merge seguinte. G11 falha em silêncio, com `ALERTA` vazio — o "caso normal" de §1.4 — e dois conflitos reais por detectar. |
| **C3** | **`ALERTA-ESTADO` é um mapa `{hash: estado}` com modo de escrita acrescento** (P3.4), e P3.10 exige estado para cada item mas só a triagem escreve — e a triagem só acorda depois de o item existir. | Arch · Flow | Transitar `novo`→`visto` exige reescrever uma chave que P3.4 proíbe. E `visto` não tem transição de saída: todo o item triado e não descartado é reemitido a cada merge, para sempre. O critério "alerta silencioso" de §1.4 é destruído pelo primeiro item triado. |
| **C4** | **O "hash do par" nunca é definido.** Não se sabe se inclui a passagem, o slug tocado, nem se `par[2]` é ordenado. | Plan · Arch · Flow | Se o par bastar, um conflito real recorrente fica suprimido para sempre por P3.11 — e um `descartado` na passagem de colisão silencia também a de dependência e a semântica. Se incluir o conteúdo, `descartado` nunca adere e `ALERTA` nunca fica vazio. Uma das duas falhas é certa. |
| **C5** | **`HALT` destrói o estado que diz proteger.** P3.13 recusa *qualquer* escrita, incluindo `handoff.json` e a selagem — e §2.4.8 justifica o desenho dizendo que "matar a meio deixa ficheiros parciais". | Plan · Arch · Flow | Produz exactamente o estado parcial que invoca para se justificar. A retoma a frio — primeiro critério de §1.4 — falha no único incidente para o qual o mecanismo existe. Sem esquema, sem origem, sem procedimento de saída. |
| **C6** | **Detector `humano` com consequência `bloqueia`** em nove regras (P0.5–P0.7, P1.8, P4.1, P4.3, P7.1–P7.3). | Plan · Arch · Blind | Um humano não é um trinco. P1.8 diz que uma árvore não pode abrir com sinal de porta de entrada verdadeiro e "bloqueia" — não existe campo, hook ou ficheiro que o faça. O leitor não distingue estas de P3.13, que bloqueia mesmo. G1, G4 e G15 assentam em disciplina apresentada como *enforcement*. |
| **C7** | **Ninguém tem zona de escrita no `INBOX`, que é acrescento e não tem campo de estado nem `slug`.** | Plan · Arch · Flow | Não existe a operação "processar". A falha observável de G10 — "`INBOX` cresce mais do que se esvazia" — é estruturalmente garantida. E colide com P3.6, que é hook bloqueante sobre "todo o artefacto". |
| **C8** | **G10 e G11 anulam-se mutuamente.** A triagem só acorda por alerta; com `ALERTA` vazio — o caso que §1.4 declara normal — a triagem nunca corre e o `INBOX` nunca é drenado. | Flow · Plan | O critério de sucesso de uma garantia é a condição de falha da outra. |
| **C9** | **P3.15 é inexecutável.** Obriga a triagem a decidir se um item "toca no mandato", e §2.4.2 nega-lhe o nível L0 que teria de consultar; além disso o detector declarado ("a triagem não tem zona em `MANDATO`") não detecta a falha descrita — que é resolver o item **dentro da própria zona** e marcá-lo `descartado`. | Plan · Flow | Sumidouro perfeito para a classe de eventos que existe para escalar. P3.11 garante que o item nunca volta; P7.2 procura "descartados que reapareceram", que P3.11 tornou impossíveis. |
| **C10** | **O canal de escalada triagem→humano não existe**: sem payload, sem registo, sem estado `escalado` (o item fica `novo`), e **não existe notificação em toda a arquitectura**. | Flow · Blind | A escalada pressupõe que o humano lê o `ALERTA` por iniciativa própria. G14 depende disso. |
| **C11** | **O auditor é o terminal de nove a treze regras e não tem ciclo de vida.** Quem o executa está em contradição (§2.4.3 diz agente; P7.1–P7.3 dão detector `humano`; P7.4 dá `hook`), o relatório não tem esquema, trajecto, slug nem estado de achado, e nenhuma regra obriga a lê-lo. | **As quatro** | Assimetria fatal: os alertas do watcher têm estado, hash e supressão; os achados do auditor nascem, são escritos e morrem. G4, G5, G9, G13 e G16 dependem inteiramente disto. §1.2 lista "ficheiros de registo que ninguém lê" como sintoma a eliminar — e o auditor produz exactamente um. |
| **C12** | **O canon não está sob o seu próprio governo**, e P5.4 isenta-se a si própria: exige incidente registado para *regra nova* e as 60 regras iniciais não têm nenhum. | Plan · Arch · Blind | Sem slug (contra P3.6), sem zona, sem actor, sem registo de regras com `incidente_slug`. Quando o governo está errado, não há procedimento. G16 depende da memória do auditor. |
| **C13** | **`toca[]` é cruzado só no fecho, e é anulável por quem ele restringe.** `estado.json` é substituição na zona da própria frente: basta reescrever `toca[]` para coincidir com o que se tocou. E não existe procedimento de redeclaração, enquanto P3.12 proíbe esperar. | Plan · Arch · Flow | O patamar duro do gate é auto-certificável. Como não há saída legal para a sessão bloqueada, a degradação previsível é declarar `toca[]` largo na abertura — o que mata G11 pelo lado do ruído, a falha que §1.4 nomeia sem identificar que é a estrutura das regras que a produz. |
| **C14** | **P3.5 é indecidível.** "Não pode conter conteúdo reconstruível por ferramenta", com detector `hook · bloqueia`. E `sealed/` guarda referências a ficheiros de worktrees efémeras que nada protege de apagamento. | Plan · Arch · Flow | O detector não é implementável e a promessa de §2.4.6 — que a narrativa "vive na proveniência selada, recuperável" — é falsa: quando a frente morre, a proveniência é um conjunto de ponteiros mortos. |
| **C15** | **O cold-read é auto-certificado e não tem valor de erro.** O campo `cold_read` vive em `estado.json`, escrito pela própria frente; o agente verificador não tem perfil entre os quatro de §0, logo S2 recusa-lhe o arranque; e `passa \| falha` não representa "não corrido". | Plan · Flow · Blind | §2.4.4 diz que o cold-read "substitui a confiança"; na forma actual substitui confiança por auto-certificação. G17 fica sem base. |
| **C16** | **P2.5 é inaplicável como esquematizada.** `pressupostos[]` não tem data e `reavaliacoes[]{data, saida}` não referencia o pressuposto: não há chave de junção para verificar "reavaliação datada" posterior à queda. | Arch · Flow · Plan | Qualquer reavaliação anterior satisfaz o hook para qualquer pressuposto. G6 fica sem suporte. E P2.5 só dispara na abertura de frente nova: um projecto que não abra frentes nunca reavalia. |
| **C17** | **Estados absorventes indesejados**: `suspenso:` cujo referente é podado ou cuja árvore morre; `retido` após a morte da árvore de Caracterização; `visto`; `descartado`; `morto`. E o grafo `depende[]` não tem proibição de ciclos nem detector deles. | Plan · Flow | Cones inteiros presos por construção, dentro de um sistema cuja tese é que as árvores têm de morrer (G5). A regra de poda de Decisão — "`suspenso` não se poda antes do referente devolver" — torna o ramo imortal quando o referente nunca devolve. |
| **C18** | **O "orquestrador" é usado como disparador da frente (§2.4.10, §2.4.11) e não consta da tabela que §2.4.3 declara única de actores.** | Arch · Flow | O ponto de entrada do sistema — quem decide que frente abre — não está modelado. |
| **C19** | **§0 e P7.3 falham o próprio teste.** Sem entrada: `runner`, `orquestrador`, `merge`, `sessão`, `handoff`, `Rascunhos`, `milestone`, `estado`. `estado` tem seis sentidos activos, `modo` três, `decisão` quatro, `alerta` três. E `Driver`, definido em §0, não reaparece uma única vez. | Plan · Arch | P7.3 procura "termos sem entrada em §0" e nunca "entradas sem uso", nem **contradições entre regras** — a classe a que pertencem C1, C3 e C9. É um *linter* de forma a fazer-se passar por verificação de consistência. |

---

## 3 · Bloco B · Defeitos que impedem a implementação

Sem resolver isto, nenhum hook se escreve.

| # | Falta | Regras que ficam inexecutáveis | Correcção mínima |
|---|---|---|---|
| B1 | **`Perfis e zonas` não é ficheiro nem esquema** (só uma linha em §2.1.1) | P3.1, P3.2, P3.14, P4.2, P5.2, P7.4 · G3, G7, G15 | `PERFIS` no Anexo A: `perfis[]{slug, zona_leitura[], zona_escrita[], runner, hooks_obrigatorios[]}`, escrito só pelo humano, residente fora de todas as zonas |
| B2 | **Não existe mapa trajecto→nível nem trajecto→modo de escrita.** §2.4.5 usa quatro modos ("substituição", "acrescento", "write-once", "livre"); P3.4 só nomeia dois. Oito ficheiros não constam da hierarquia L0–L4 | P3.1, P3.4 | Manifesto de trajectos com `nivel` e `modo_escrita`, com os quatro modos nomeados; P3.4 remete para o manifesto em vez da prosa |
| B3 | **`arvores/*.nos[]` não tem `pai` e `eixo` é singular** | P1.2, P1.3 · cone, folha, profundidade desigual · representabilidade de Caracterização e Mandato | `pai: slug \| null` e `eixos[]` com cardinalidade condicionada ao `modo`. Separar em §0 `cone_estrutural` de `cone_de_dependencia` (hoje são duas estruturas sob um nome) |
| B4 | **`arvores/*` não tem campo de estado da árvore** | P1.11 (detector: "estado da árvore") · G5 · o travão único de T5 | `estado: aberta \| morta`, `morta_em`, `morte_verificada_por` |
| B5 | **A projecção não tem esquema, ficheiro nem detector** | §3.3 declara-a o único sítio onde fica escrito para que existe uma frente · G3 | Bloco `projeccao{pressuposto_slug, regra_paragem, fronteiras_negativas[]}` em `estado.json`, ou ficheiro selado na abertura |
| B6 | **Nenhum artefacto regista uma corrida do watcher** | P3.17 (detector: "sessões seladas sem corrida do watcher") · P3.11 · calibração de P7.2 | `corridas/<id>.json` com merge, entrada, itens e passagens executadas; no mínimo `corrida{id, data, merge_ref}` em `ALERTA` |
| B7 | **Não existe registo de regras** com `incidente_slug`, `grau`, `detector`, `consequencia` | P5.4, P5.5, P7.3 · G16 | `canon/regras.json`, ou front-matter por regra no próprio documento |
| B8 | **Cinco esquemas sem `slug`** (`INBOX/*`, `estado.json`, `handoff.json`, `REJEICOES`, `CASOS`) | P3.6, hook bloqueante sobre "todo o artefacto" | Acrescentar `slug`, ou restringir P3.6 à lista de §0 |
| B9 | **`indice-decisoes.json` não carrega o grau** e não tem `base_merge`; `debates/` não sabe exprimir *desselar* nem *retirar* | P3.7, P3.8, P3.9 · G8, G13 · dois dos quatro graus de §2.4.8 não são representáveis | `{slug: {grau, decisoes[], base_merge}}` + `sela[]`, `desbloqueia[]`, `retira[]` no debate + regra de precedência entre decisões sobre o mesmo slug |
| B10 | **`debates/` tem um escritor (rumo) e quatro produtores de decisão**: rumo (P5.3), alocação de runner (P4.4), opção escolhida em árvore de Decisão, poda de ramo | P5.6 · G13 — a poda nunca entra no índice, logo o hook nunca bloqueia a recriação: G13 combina duas regras que não se tocam | Campo `tipo` no debate e zona de escrita por tipo |
| B11 | **Nenhum esquema tem versão; não há integridade referencial entre ficheiros.** O documento depende de `protocolo-arvore-definicao-e-uso` **v2** sem contrato de compatibilidade | evolução sem reescrita · P5.x | `versao_esquema` em todos os ficheiros; item novo em P7.2 para referências pendentes |
| B12 | **O preâmbulo do Anexo A diz "campos obrigatórios" (esquema aberto); G10 e §2.5.5 invocam "campos fechados"** | G10 ("o lixo não entra") | Decidir: fechar o esquema, ou reescrever G10 |

---

## 4 · Bloco C · Caminhos, estados e limpeza

### 4.1 Workflows ausentes de maior consequência

| Workflow | Estado | Lacuna |
|---|---|---|
| **Merge de frente** | **Ausente** | Não há ramo de falha em lado nenhum — e um conflito de merge *é* a colisão que a passagem de colisão existe para apanhar: **o detector é desligado pelo evento que devia detectar**. Pior: a selagem precede o merge e `sealed/` é write-once, logo o estado fica selado e não fundido, sem reversão possível |
| **Subida de `confirmado` / `inconclusivo`** | **Ausente** | Os tipos de `INBOX` são `descoberta`, `pressuposto_caido`, `falha_de_sistema`. Não existe canal para um pressuposto confirmado subir — e toda a ordem de ataque de MP5 depende de "avança para o seguinte", que ninguém executa |
| **Fecho limpo de frente** | Parcial | Só a triagem escreve `FRENTES` e só acorda por alerta: uma frente que feche bem fica listada como aberta para sempre |
| **Propagação de emenda ao mandato** | **Ausente** | Pode invalidar pergunta de decisão, caminhos, pressupostos e projecções de todas as frentes vivas. Nada obriga a revalidar nem a notificar, e `desbloqueado` não é reposto |
| **Aprovação de `carece_aprovacao`** | **Ausente** | Ninguém aprova: a triagem não tem zona em `estado.json` e a própria frente pode limpar a marca ao substituir o ficheiro na sessão seguinte |
| **Sessão que não consegue fechar (S5 duro)** | **Ausente** | Não pode fechar, não pode esperar (P3.12), não pode escrever fora da zona. Nenhuma saída documentada |
| **Recuperação pós-`HALT`** | **Ausente** | Sem inventário de worktrees não fundidas, sem inventário de selagens sem merge, sem reconciliação, sem registo |
| **Falha do detector semântico** | **Ausente** | Chamada de modelo sem timeout, sem valor de erro, sem consequência: a rede de segurança de T2 degrada-se em silêncio |
| **Poda de ramo com frente viva em cima** | **Ausente** | Nada verifica frentes abertas antes de podar; a frente, que classifica só contra o seu pressuposto, nunca descobre |
| **Limpeza de worktrees** | **Ausente** | Nenhum actor, nenhuma cadência, ausente de P7.2 |
| **Adopção / migração** | **Ausente** | §2.1 abre com "nada arranca antes desta fase estar fechada" e P0.8 bloqueia toda a abertura de frente. Um projecto a meio só adopta parando tudo |
| **Nascimento (P0)** | Parcial | Nenhum dos quatro perfis pode escrever `MANDATO` e `Perfis e zonas`. O dia 1 não tem actor legal |

### 4.2 Ordem e concorrência — pressupostos nunca declarados

1. O merge tem sempre êxito.
2. Uma corrida do watcher termina antes de a seguinte começar.
3. O script de indexação corre antes do watcher no mesmo merge — se correr depois, a protecção avalia contra índice velho.
4. Corre no máximo uma sessão de triagem de cada vez: `ESTADO` e `FRENTES` são substituição, sem token de versão, logo actualização perdida.
5. Sessões já a correr revalidam o índice — não há invalidação: uma sessão aberta antes do merge continua a ver `livre` um slug que passou a `selado`.
6. Cada decisão passa por um merge. As produzidas em modo rumo, que corre em interface de chat, podem não passar — e então G8 nunca se activa para elas.

### 4.3 Inventário de limpeza — 22 resíduos, zero actores

Nenhum tem quem o destrua, e nenhum consta de P7.2: worktrees de frentes fechadas, abandonadas ou com merge falhado; ficheiros parciais pós-`HALT`; selagens sem merge (impossíveis de anular, porque write-once); `research/` (declarado "livre, não se disciplina"); `Rascunhos` de sessão bloqueada; itens de `INBOX` por processar e rejeitados; `ALERTA-ESTADO` com `visto` perpétuo e em crescimento indefinido; hashes `descartado` a suprimir colisões futuras; itens do gate destruídos pela substituição seguinte; frentes abertas sem sessão; frentes listadas como abertas após fecho limpo; ramos `em desenvolvimento` de frentes mortas; ramos `suspenso:` com referente morto; ramos `retido` após morte da árvore; ficheiros de árvores mortas; escaladas nunca atendidas; achados de auditoria nunca corrigidos; `sealed/` sem rotação.

---

## 5 · Bloco D · Pontos cegos de enquadramento

O que as três primeiras lentes não podiam ver, porque trabalham dentro do enquadramento do documento.

### 5.1 O que o documento assume sem dizer

| # | Pressuposto tácito | O que parte se for falso |
|---|---|---|
| UK1 | **O diagnóstico de §1.2 é verdadeiro e foi observado.** 11 sintomas apresentados como factos etiológicos, sem N, sem caso, sem projecto nomeado — e todo o edifício deriva deles | Se o modo de falha dominante for outro (o humano perde interesse, a prioridade muda, o custo excede o valor), 60 regras tratam uma doença que o doente não tem, e operá-las é a causa de morte |
| UK2 | **O canon está isento da sua própria regra de prova.** P5.4 exige incidente para regra nova; as 60 iniciais não têm nenhum | P5.4 congela um palpite e proíbe alternativas: rigidez sem evidência |
| UK3 | **Há um humano responsável e está sempre lá.** Zero ocorrências de sucessão, ausência, delegado, substituto | Nove regras com detector `humano`. Seis semanas de indisponibilidade e o sistema não pode emendar-se (P5.1), desbloquear (P0.7), auditar (P7.1) nem alocar runner (P4.3) — e também não morre. Deriva silenciosa com aparência de ordem |
| UK4 | **Ler é grátis; o custo é escrever** (§1.2 di-lo literalmente) | Zero ocorrências de *token*, *custo*, *orçamento*, *latência*. Contexto por sessão + não-objectivos sempre + cold-read por fecho + detector semântico por merge + triagem por alerta + auditoria mensal: o mecanismo de protecção é o maior consumidor do projecto |
| UK5 | **O tempo humano é ilimitado.** P7.2 são 16 verificações mensais sem estimativa de duração | Se custar 6 horas, é feita duas vezes e abandonada — e com ela caem os únicos detectores de G2, G4, G5, G9, G12, G13, G15, G16 |
| UK6 | **"Detector" significa "mecanismo"; escrito = obrigado a acontecer** | Ver C6. A coluna dá a todas as regras a mesma aparência de força |
| UK7 | **Uma regra em prosa torna-se um hook correcto.** Zero ocorrências de teste, ensaio ou simulação de hook | Há `HALT` para o hook *ausente* (P4.5) e nenhuma defesa para o hook *errado*, que é muito mais provável. P7.3 audita o canon contra si próprio, nunca contra a implementação |
| UK8 | **O relatório é uma consequência.** 13 regras têm `relatório` como única consequência | Ver C11. Deviam ler-se `nenhuma` |
| UK9 | **O substrato do modelo é estável e irrelevante.** Zero referências a versão de modelo ou prompt em qualquer esquema | `sealed/` não é reprodutível. P0.7 valida o mandato através de um teste executado num modelo que muda a cada poucos meses, e a validade caduca sem ninguém saber. P4.4 exige decisão para mudar de *runner* e nenhuma para mudar de *modelo* — que é a variável que muda o comportamento |
| UK10 | **Três sessões limpas são três juízes independentes** | Erros de modelos idênticos são correlacionados. Três sessões que se enganam da mesma maneira devolvem `passa` com confiança máxima: o teste tem o ponto cego alinhado com o do sistema que valida. Idem para o cold-read. Concordância mede consistência, não correcção — e o documento lê-a como correcção |
| UK11 | **O mundo é o repositório.** Toda a detecção assenta em merge, worktree, `toca[]` e JSON | Trabalho que não passa por ficheiro — uma chamada, uma negociação, uma medição — é invisível. Numa frente maioritariamente fora do disco, `ALERTA` vazio significa cegueira, não saúde, e o sistema não distingue os dois casos |
| UK12 | **Um projecto de cada vez, num disco.** "Slug: identificador global e único" — global em que âmbito? | Com dois projectos: slugs colidem ou fragmentam-se, `HALT` pára os dois ou nenhum, o índice sela slugs alheios. Se colidir, P3.6 é violada por construção. Decidir hoje custa uma linha; depois é renomear slugs, que P3.6 proíbe |

### 5.2 Domínios inteiros ausentes

| # | Ausente | Sintoma que vai aparecer | Precedente a importar |
|---|---|---|---|
| UU1 | **Validação distinta de verificação.** Sete números arbitrários (1 página, 2–3 não-objectivos, ≥2 árvores, factor dez, mensal) apresentados como se fossem derivados. O documento verifica que são cumpridos; nunca demonstra que controlam o que dizem controlar | Discussões insolúveis daqui a três meses sobre se o mandato devia ter duas páginas, sem critério para resolver. Os números tornam-se dogma por antiguidade | **HACCP**, princípios 2 e 6: cada limite crítico exige validação documentada, separada da verificação |
| UU2 | **Instrumentação do processo.** Zero ocorrências de métrica, medir, indicador. Mede conformidade, nunca fluxo | G16 contou a única coisa contável sem instrumentação: o número de regras. Um governo com 60 regras estáveis que consome 80% do esforço está, por G16, saudável. O sistema morre por asfixia com todas as garantias verdes | **SPC / Shewhart** e **métricas DORA**. Corolário: a auditoria devia disparar por sinal fora de controlo, não por calendário (P7.1) |
| UU3 | **Integridade de leitura.** Confinamento de escrita excelente (zonas, P3.1, P3.14, G7); modelo de confiança de leitura inexistente. `research/` é "livre e não se disciplina"; `INBOX.texto` é escrito por frentes e lido pela triagem | Uma sessão de triagem lê um item cujo `texto` contém instruções e resolve-o como pedido. Não deixa rasto: nenhuma zona foi violada, a escrita está dentro da zona da triagem, G7 continua verde | **Modelo de Biba** (*no read up* de integridade) e **taint tracking**. O documento implementou metade de um modelo de segurança e chamou-lhe confinamento |
| UU4 | **Adopção e migração** | Big bang ou nada. O sistema fica por adoptar e é usado "em espírito", que é o mesmo que não ser usado | **Strangler Fig** (Fowler); *expand/contract*; hooks primeiro em modo de aviso |
| UU5 | **Fim, arquivo e retenção.** P0.4 obriga a declarar `criterio_fim` e nada diz o que se faz quando é atingido | Projectos terminados com watcher ligado, a consumir chamadas e a gerar alertas sobre trabalho que ninguém faz | **ISO 15489**: retenção e disposição declaradas no acto de criação do registo |
| UU6 | **Fim de vida do próprio governo.** Nada declara este sistema um fracasso | O documento obriga todas as árvores a declarar como morrem (P1.1) e o projecto a declarar como termina (P0.4), e isenta-se das duas. Ao sexto mês é operado por inércia; a única saída documentada é a emenda, que exige o humano que já desistiu | **Cláusula de caducidade** (*sunset clause*): manter o governo passa a exigir um acto, em vez de o abandonar exigir um |
| UU7 | **Ergonomia do operador único.** Automatiza o fácil e concentra no humano o julgamento residual, intermitente e difícil | Fadiga e abandono entre a semana 6 e a 10, precisamente quando o sistema começa a dar valor — e ao abandonar, o humano perdeu a prática de fazer manualmente o que o sistema fazia | **"Ironies of Automation"**, Bainbridge (1983). O documento é um caso de manual |

---

## 6 · Onde as lentes divergem

| Questão | Posição A | Posição B | Comentário |
|---|---|---|---|
| Modos Caracterização e Mandato | **Cortar**: Caracterização é a fonte do deadlock de `retido`, não concorre e não decide; Mandato é uma conversa, não uma partição de espaço | **Corrigir o esquema**: `eixos[]` e `pai` tornam-nos representáveis | Depende de UK1 e de T5. Sem evidência de que quatro modos resolvem quatro problemas reais, cortar é mais barato e reversível |
| `ESTADO` e `REJEICOES` | **Cortar**: escritores sem leitor declarado, reproduzem o sintoma de §1.2 | **Enriquecer** com proveniência por facto, ou **gerar `FRENTES` por inversão** dos `estado.json` | Gerar por inversão resolve também o fecho limpo que nunca actualiza `FRENTES`; é a mais forte das três |
| `ALERTA-ESTADO` | **Cortar**: `ALERTA` acrescento com `fechado_em` e razão elimina C3, C4 e dois itens de P7.2 | **Log de corridas + projecção**: mais poderoso, mas introduz um terceiro modo de escrita e obriga a reescrever P3.4 | A é v1, B é v2. Ambas resolvem o essencial |
| Detector semântico | **Cortar**: sugestões que nenhuma regra obriga a tratar; despesa por merge sem consequência | **Dar-lhe contrato**: timeout, valor de erro, alerta de indisponibilidade | Se ficar, tem de ter contrato; sem contrato, corta-se |
| **O problema existe?** | As três primeiras lentes assumem que sim e trabalham dentro do enquadramento | **Blind spot**: §1.2 é etiologia postulada, sem um único incidente registado — e é o próprio P5.4 que exige incidentes | É a divergência que importa. Resolve-se com a pergunta 1 |

---

## 7 · Plano de correcção, por ordem

**Camada 0 — sem isto não há implementação.** B1–B12 acima: criar `PERFIS`; manifesto de trajectos com nível e modo de escrita; `pai` e `eixos[]` nos nós; estado da árvore; esquema da projecção; registo de corridas do watcher; `slug` nos cinco esquemas em falta; grau no índice e `sela`/`desbloqueia`/`retira` nos debates; `tipo` no debate; `versao_esquema`; decidir se o esquema é aberto ou fechado.

**Camada 1 — perda de dados e silenciamento.** Ramo de falha do merge, e inverter selagem↔merge ou selar em duas fases; excepção de drenagem em P3.13 para `handoff.json` e selagem; canal próprio para o item do gate, que não pode ser `ALERTA`; `toca_declarado[]` write-once contra `toca_efectivo[]` calculado do diff, mais o evento "ampliação de toca" cruzado em tempo real; canal de escalada com estado `escalado` e prazo; estado nos itens de `INBOX` e zona para o marcar; serialização de merges e corridas, com `base_hash` nos ficheiros de substituição.

**Camada 2 — garantias fantasma.** Regra que obrigue o watcher a correr as três passagens e a registar a origem de cada item — hoje o watcher não aparece em detector nenhum; regra para a contagem de `INBOX` que G10 lhe atribui; decidir G12, com regra de aplicação verificável ou assumindo cadência mensal; `ACHADOS` com estado, dono e prazo, dual de `ALERTA-ESTADO`; estado `resolvido` em `ALERTA-ESTADO` e caducidade de `visto`; **coluna *Força* ∈ {mecânica, convenção}**, com proibição de uma regra `convenção` declarar `bloqueia`; alargar P7.3 a contradições entre regras, entradas de §0 sem uso, e garantias cujo detector nomeie um actor que nenhuma das suas regras invoca.

**Camada 3 — decisões que só o autor pode tomar.** As doze perguntas abaixo.

**Cortes propostos, para compensar o que acima se acrescenta:** `ESTADO` e `REJEICOES`, detector semântico, modo Caracterização e estado `retido`, modo Mandato como árvore, `ALERTA-ESTADO`, P3.9, P3.5 na forma actual, a contagem de pilares em P6.1, P1.7 e P1.10, e P7.2 reduzida à metade automatizável corrida a cada merge. O núcleo que sobrevive — cerca de vinte regras — sustenta G1, G6, G7, G8, G11, G14 e G17, as sete que justificam o documento existir.

---

## 8 · As doze perguntas, por custo de descobrir tarde

1. **Existe algum projecto real em que tenhas observado e registado os 11 sintomas de §1.2? Quantos, em quantos projectos?** Se zero ou um, §1.2 é postulado e o canon deve nascer com um núcleo mínimo e crescer por incidente, como P5.4 exige de todos os outros.
2. **Quantas horas por mês aceitas gastar em P7.2, P7.3, sondas e leitura de relatórios? Diz um número.** Abaixo de quatro, P7.2 tem de ser partida em automática e humana, e a auditoria passa a disparar por sinal.
3. **O que acontece ao projecto se ficares indisponível seis semanas?** Define se precisas de sucessor no `MANDATO` ou de modo degradado declarado.
4. **Quem lê o relatório do auditor, e o que acontece a um achado que fica dois ciclos por resolver?** Se a resposta for "nada", treze regras são decorativas.
5. **Quando o modelo subjacente mudar de versão, o que se revalida?** Decide se `sealed/` é proveniência a sério e se P0.7 tem prazo de validade.
6. **As três sessões do teste de discriminação e o cold-read correm no mesmo modelo?** Se sim, não são três juízes: são três amostras.
7. **Quantos projectos vão correr em simultâneo nesta instalação?** Uma linha hoje; impossível depois, porque P3.6 proíbe renomear slugs.
8. **O primeiro projecto é greenfield ou já está a meio?** Decide se precisas de protocolo de adopção ou de uma exclusão explícita em §1.3.
9. **Qual é o orçamento de chamadas de modelo por merge e por fecho?** Sem tecto, o primeiro mês de facturação torna-se o verdadeiro auditor.
10. **Quem escreve os hooks, e existe um teste que prove que cada hook recusa o caso que a regra proíbe?** Sem isso, a coluna *Detector* é uma declaração de intenção.
11. **O conteúdo de `research/` e o campo `texto` de `INBOX` entram no contexto montado de outra sessão?** Se sim, tens uma superfície de injecção com a triagem como alvo e nenhum modelo de integridade de leitura.
12. **Qual é o critério que declara este sistema um fracasso e manda desligá-lo?** A pergunta mais barata de responder hoje e a mais cara de nunca ter sido feita.

---

## 9 · O que está bem e não se toca

Nenhuma das correcções acima exige mexer nisto, e as quatro lentes assinalaram-no em separado:

- **Numeração aditiva com grau `morto`** (P5.5) e a proibição de renumerar.
- **Separação crivo / caminho** (§2.3.1): o crivo mata de graça, antes de haver dados; o caminho testa caro, com dados reais. É a melhor ideia do documento.
- **Distinção deriva / inflexão** (§2.5.4): o sistema não impede movimento, torna impossível alterar o mandato sem emendar o mandato.
- **P4.1**: um processo permanente não pode julgar. Correcto e bem fundamentado.
- **§3.3**: o reconhecimento explícito de que nenhum mecanismo impede fazer a coisa errada com perfeição dentro da própria zona. É a frase mais honesta do documento — e é precisamente a projecção, que ela declara ser o único remédio, que não tem esquema nem detector.
- **A exigência de que cada regra tenha detector e consequência.** A disciplina é rara e vale manter.

O que falha é que cumprir a coluna não é ter o mecanismo: metade dos detectores lê um campo que o interessado escreve, nove apontam para um humano com consequência bloqueante, um aponta para si próprio (P4.5), e o actor mais importante do sistema não aparece em detector nenhum. **A Convenção de leitura protege contra obrigações em prosa; não protege contra detectores em prosa.** É isso que P7.3 deveria passar a procurar primeiro.
