---
created: 2026-09-20
documento: relatório de alterações a `arquitectura-governo-arvore.md`
alvo: revisão de 2026-09-20 06:10 (781 linhas · 60 regras · 17 garantias · 14 esquemas)
fonte: dossiê de correcções (vinculativo) · auditoria consolidada de quatro lentes
summary: >
  Registo de rastreabilidade das correcções aplicadas ao canon de governo: o que mudou,
  que achado o motivou, que garantia restaura, que alternativas foram rejeitadas,
  que parâmetros ficam pendentes do autor e que custo e riscos permanecem.
---

# Relatório de alterações

Este documento não é canon. O canon é `arquitectura-governo-arvore.md` e lê-se sem referência ao que existiu antes. Aqui regista-se o oposto: a proveniência de cada regra. Quem perguntar dentro de seis meses porque é que P3.10 está escrita assim encontra a resposta na secção 2, linha C3.

---

## 1 · Sumário executivo

**Números.** 28 regras corrigidas, 41 regras novas, 1 regra reformulada sem mudar de identificador (P3.9), 0 regras renumeradas, 0 regras retiradas. O corpo passa de 60 para 101 identificadores, mais a partição de P7.2 em automática e humana. O Anexo A passa de 14 para 24 esquemas: 10 artefactos novos, 14 esquemas corrigidos, 1 ficheiro retirado (`ALERTA-ESTADO`, absorvido por `alerta-estado.log` e por `ALERTA` derivado). As garantias passam de 17 para 22: G18 a G22 novas, G10, G11 e G12 corrigidas de fantasma para executável. As tensões passam de 5 para 10: T6 a T10 declaram o custo das próprias correcções. §0 recebe 13 entradas novas e três desambiguações obrigatórias (`estado`, `cone`, `alerta`). As regras ganham uma quinta coluna, *Força*. Da auditoria, 69 achados entram na matriz de rastreabilidade: 66 implementados ou parcialmente implementados, 3 não implementados.

**Substância, primeiro parágrafo.** O diagnóstico consolidado das quatro lentes foi que o documento é forte como modelo conceptual e fraco como contrato executável: a camada de execução foi especificada por nome e não por contrato. As correcções atacam esse defeito em três frentes. Primeira, dar existência aos artefactos que os hooks tinham de ler e não existiam — `PERFIS`, `TRAJECTOS`, `corridas/<id>.json`, `canon/regras.json`, a projecção com esquema, o estado da árvore, o `pai` dos nós (B1–B7). Segunda, fechar os quatro sítios de perda de dados silenciosa: `ALERTA` substituído em corridas concorrentes (C2), itens do gate destruídos pela corrida seguinte (C2), `HALT` a bloquear a selagem que diz proteger (C5), merge falhado depois de selagem irreversível (§4.1). Terceira, separar o que é mecanismo do que é disciplina: a coluna *Força* ∈ {mecânica, convenção}, com a proibição de uma regra `convenção` declarar `bloqueia`, resolve as nove regras que apontavam um humano como trinco (C6) sem lhes tirar a obrigação.

**Segundo parágrafo.** Três classes de correcção não derivam de defeitos internos mas de domínios inteiramente ausentes, apontados pela lente de enquadramento. Custo: o documento tinha zero ocorrências de *token*, *custo*, *orçamento* e *métrica*, e o mecanismo de protecção é o maior consumidor do projecto (UK4); P0.10 obriga o `MANDATO` a declarar orçamento, P7.7 obriga o auditor a registar métricas de fluxo, `METRICAS` dá-lhes ficheiro, e G20 fecha o par. Continuidade: o sistema assume um humano sempre presente (UK3); P0.9 exige `responsavel` e `sucessor`, P0.13 declara modo degradado, G22 fecha. Fim: o documento obriga toda a árvore a declarar como morre e o projecto a declarar como termina, e isenta-se das duas (UU5, UU6); P5.10 dá-lhe caducidade, P5.12 dá-lhe protocolo de encerramento, G19 fecha. Acresce a integridade de leitura: o confinamento de escrita estava completo e o modelo de confiança de leitura não existia (UU3); P3.23 classifica toda a fonte e proíbe montar como instrução o que é `nao_verificado`, e G18 fecha.

**Terceiro parágrafo.** As correcções custam. O corpo cresce 68%; 31 das 41 regras novas têm consequência `bloqueia`; a abertura de frente passa a ser cruzada por sete verificações bloqueantes (P0.8, P0.10, P0.13, P2.5, P2.10, P2.11, P7.5); a serialização de merges (P3.25) e a revalidação de índice (P3.24) transformam atrasos em paragens; `PERFIS` e `TRAJECTOS` criam um ponto único de falha que antes não existia. Isto tensiona directamente T5 e G16 — o critério de sucesso «governo estável» mede o número de regras e o número de regras acabou de subir. As travagens declaradas são três: a coluna *Força*, que impede que volume se traduza automaticamente em bloqueio; P7.2 partida, que tira da carga humana tudo o que um watcher consegue correr; e P5.9, que faz nascer toda a regra do corpo inicial com grau `postulada` e a torna candidata a remoção se nenhum incidente a confirmar. A secção 8 quantifica o custo e a secção 9 lista o que permanece por resolver, incluindo o que nenhuma correcção resolve.

---

## 2 · Matriz de rastreabilidade

**Convenção de leitura da matriz.** A auditoria atribui lentes explicitamente só no Bloco A. Nos restantes blocos aplica-se a atribuição por produção declarada em §1 da auditoria: Bloco B (integridade do Anexo A campo-a-campo) → *Arch*; Bloco C (workflows, máquinas de estado, resíduos) → *Flow*; Bloco D (pressupostos tácitos, domínios ausentes) → *Blind*; a lista de cortes de §7 → *Plan*. As divergências entre lentes (§6 da auditoria) e os cortes propostos (§7) não são achados e tratam-se nas secções 5 e 6 deste relatório.

### 2.1 Bloco A · Convergências

| Achado | Lente(s) | Defeito | Regra ou artefacto alterado | Natureza | Garantia que restaura |
|---|---|---|---|---|---|
| **C1** | Plan · Arch | P3.2 proíbe o que P3.3 obriga; a excepção vive em prosa (§2.4.2) e prosa não isenta | P3.2 (salvaguarda no texto da regra), P3.3 (alargada a `CASOS`) | corrigidas | G2, G3 |
| **C2** | Plan · Arch · Flow | `ALERTA` é substituição, sem lock, ordem nem versão; P3.16 manda o gate escrever no ficheiro do watcher | P3.16 (item vai para `INBOX` tipo `fecho_brando`), P3.25, `corridas/<id>.json`, `ALERTA` derivado | corrigidas + novas | G11 |
| **C3** | Arch · Flow | mapa `{hash: estado}` em acrescento; `visto` sem transição de saída; só a triagem escreve e só acorda depois | P3.10 (o watcher inscreve `novo`), `alerta-estado.log`, `ALERTA` regenerado | reformulada (D3) | G10, G11 |
| **C4** | Plan · Arch · Flow | o hash do par nunca é definido | `ALERTA`: `hash = H(passagem, par ordenado, slug_tocado)`; P3.11 condicionada a mudança de conteúdo | corrigidas | G11 |
| **C5** | Plan · Arch · Flow | `HALT` recusa a escrita de `handoff.json` e a selagem, e produz o estado parcial que invoca para se justificar | P3.13 (excepção de drenagem), P3.30 (esquema e procedimento de saída) | corrigida + nova | G17 |
| **C6** | Plan · Arch · Blind | detector `humano` com consequência `bloqueia` em nove regras | coluna *Força*; P0.5, P0.6, P4.1, P4.3 → `convenção`/`relatório`; P0.7 → mecânica via P0.12; P1.8 por aplicação da regra geral | corrigidas | G1, G4, G15 |
| **C7** | Plan · Arch · Flow | ninguém tem zona de escrita no `INBOX`, que não tem `slug` nem estado | P3.22, esquema de `INBOX/*.json` | nova + esquema | G10 |
| **C8** | Flow · Plan | G10 e G11 anulam-se: a triagem só acorda por alerta e `ALERTA` vazio é o caso normal | P3.19 (contagem e limiar do `INBOX`), P3.16 (canal próprio), P2.8 | novas | G10 |
| **C9** | Plan · Flow | P3.15 é inexecutável: obriga a decidir «toca no mandato» sem L0, e o detector declarado não detecta a falha descrita | P3.15 (detector `gate` na escrita de estado de alerta; triagem recebe slugs), `ESCALADAS` | corrigida + artefacto | G14 |
| **C10** | Flow · Blind | o canal de escalada triagem→humano não existe: sem payload, sem registo, sem estado | `ESCALADAS`, P3.15, P2.11 | novo | G14 |
| **C11** | as quatro | o auditor é terminal de nove a treze regras e não tem ciclo de vida; os achados nascem, são escritos e morrem | `ACHADOS`, P7.5, P7.1 (auditoria extraordinária), P7.2 partida | novo | G4, G5, G9, G13, G16 |
| **C12** | Plan · Arch · Blind | o canon não está sob o seu próprio governo; P5.4 isenta-se a si própria | P5.8, P5.9, `canon/regras.json` | novas | G16 |
| **C13** | Plan · Arch · Flow | `toca[]` é cruzado só no fecho e é anulável por quem ele restringe | P3.21 (`toca_declarado[]` write-once contra `toca_efectivo[]`), P2.10, `estado.json` | novas | G11 |
| **C14** | Plan · Arch · Flow | P3.5 é indecidível; `sealed/` guarda ponteiros para worktrees efémeras | P3.5 (lista branca + `hash_conteudo` + proibição de apagar referente), esquema de `sealed/` | reformulada | §2.4.6 (proveniência recuperável) |
| **C15** | Plan · Flow · Blind | o cold-read é auto-certificado, o verificador não tem perfil e `passa\|falha` não representa «não corrido» | P3.27 (perfil `verificacao`, domínio de três valores), P6.2 | nova + corrigida | G17 |
| **C16** | Arch · Flow · Plan | P2.5 não tem chave de junção entre `pressupostos[]` e `reavaliacoes[]`; e só dispara na abertura de frente | P2.5 (reescrita), P2.9 (actor e cadência), `CAMINHO` | corrigidas + nova | G6 |
| **C17** | Plan · Flow | estados absorventes (`suspenso`, `retido`, `visto`, `descartado`, `morto`) e ausência de proibição de ciclos em `depende[]` | P1.12, P1.13, P1.14, P1.16, P3.10 (caducidade de `visto`), P3.11 | novas + corrigidas | G5, G13 |
| **C18** | Arch · Flow | o orquestrador dispara a frente e não consta da tabela única de actores | P4.9 | nova | G15 |
| **C19** | Plan · Arch | §0 sem oito entradas, com `estado` em seis sentidos e `Driver` sem uso; P7.3 nunca procura contradições entre regras | §0 (13 entradas novas, 3 desambiguações), P7.3 (alargada) | corrigidas | G16 |

### 2.2 Bloco B · Defeitos que impediam a implementação

| Achado | Lente(s) | Defeito | Regra ou artefacto alterado | Natureza | Garantia que restaura |
|---|---|---|---|---|---|
| **B1** | Arch | `Perfis e zonas` não é ficheiro nem esquema; P3.1, P3.2, P3.14, P4.2, P5.2, P7.4 ficam inexecutáveis | `PERFIS` | novo | G3, G7, G15 |
| **B2** | Arch | não existe mapa trajecto→nível nem trajecto→modo de escrita; §2.4.5 usa quatro modos e P3.4 nomeia dois | `TRAJECTOS`, P3.4 (remete para o manifesto) | novo + corrigida | G9 |
| **B3** | Arch | `arvores/*.nos[]` sem `pai`, com `eixo` singular; Caracterização e Mandato não são representáveis | `arvores/*` (`pai`, `eixos[]`), §0 (`cone_estrutural` / `cone_de_dependencia`), P1.2 (detector `hook`) | esquema + corrigida | G4 |
| **B4** | Arch | `arvores/*` sem campo de estado da árvore; P1.11 declara um detector que não tem campo | `arvores/*` (`estado`, `morta_em`, `morte_verificada_por`), P1.1 | esquema + corrigida | G5 |
| **B5** | Arch | a projecção não tem esquema, ficheiro nem detector, e §3.3 declara-a o único remédio | `estado.json` (bloco `projeccao{...}`) | esquema | G3 |
| **B6** | Arch | nenhum artefacto regista uma corrida do watcher | `corridas/<id>.json`, P3.17, P3.18 | novo + corrigida | G11 |
| **B7** | Arch | não existe registo de regras com `incidente_slug`, `grau`, `detector`, `consequencia` | `canon/regras.json`, P5.8, P5.9 | novo + novas | G16 |
| **B8** | Arch | cinco esquemas sem `slug`, contra P3.6, que é hook bloqueante sobre «todo o artefacto» | `INBOX/*`, `estado.json`, `handoff.json`, `REJEICOES`, `CASOS` | esquemas | G8 |
| **B9** | Arch | `indice-decisoes.json` não carrega o grau nem `base_merge`; `debates/` não sabe exprimir *desselar* nem *retirar* | `indice-decisoes.json` (`{slug: {grau, decisoes[], base_merge}}`), `debates/*` (`sela[]`, `desbloqueia[]`, `retira[]`) | esquemas | G8 |
| **B10** | Arch | `debates/` tem um escritor e quatro produtores de decisão; a poda nunca entra no índice | `debates/*` (campo `tipo`), P1.16 | esquema + nova | G13 |
| **B11** | Arch | nenhum esquema tem versão; não há integridade referencial nem contrato com o canon operacional v2 | `versao_esquema` em todos os ficheiros, item novo em P7.2 | transversal | evolução sem reescrita |
| **B12** | Arch | o preâmbulo do Anexo A diz esquema aberto; G10 e §2.5.5 invocam campos fechados | Anexo A: esquema **fechado** (campo não previsto é rejeitado) | transversal | G10 |

### 2.3 Bloco C · Caminhos, concorrência e limpeza

| Achado | Lente(s) | Defeito | Regra ou artefacto alterado | Natureza | Garantia que restaura |
|---|---|---|---|---|---|
| **§4.1 Merge de frente** | Flow | sem ramo de falha; a selagem precede o merge e `sealed/` é write-once | P3.20 (`merge_pendente`, item `falha_de_sistema`), P3.17 (selagem em duas fases) | novas + corrigida | G11 |
| **§4.1 Subida de `confirmado`** | Flow | não existe canal para um pressuposto resolvido subir; MP5 depende de «avança para o seguinte», que ninguém executa | P2.8, `INBOX` tipo `pressuposto_resolvido` | nova + esquema | G6 |
| **§4.1 Fecho limpo de frente** | Flow | só a triagem escreve `FRENTES` e só acorda por alerta: a frente fica aberta para sempre | `FRENTES` gerado por inversão dos `estado.json` | reformulado (D2) | G9 |
| **§4.1 Propagação de emenda** | Flow | nada obriga a revalidar caminhos, pressupostos e projecções, e `desbloqueado` não é reposto | P5.7 | nova | G1, G6 |
| **§4.1 Aprovação de `carece_aprovacao`** | Flow | ninguém aprova, e a própria frente limpa a marca ao substituir o ficheiro | P3.28, `APROVACOES` | nova + artefacto | G12 |
| **§4.1 S5 duro sem saída** | Flow | não pode fechar, não pode esperar (P3.12), não pode escrever fora da zona | P3.26 (Rascunhos → `descoberta`), P3.20, P3.21 (ampliação de toca como evento), `ESCALADAS` | novas | G17 |
| **§4.1 Recuperação pós-`HALT`** | Flow | sem inventário, sem reconciliação, sem registo | P3.30, P3.31 | novas | G17 |
| **§4.1 Falha do detector semântico** | Flow | chamada de modelo sem timeout, sem valor de erro, sem consequência | P3.18, P6.2, `ALERTA` (passagem `semantico_indisponivel`), `corridas/*` (`timeout`) | novas + esquema (D4) | G11 |
| **§4.1 Poda com frente viva** | Flow | nada verifica frentes abertas antes de podar | P1.15, P1.13 | novas | G5, G13 |
| **§4.1 Limpeza de worktrees** | Flow | nenhum actor, nenhuma cadência, ausente de P7.2 | P3.31, item novo em P7.2 | nova + corrigida | G9 |
| **§4.1 Adopção / migração** | Flow | §2.1 e P0.8 obrigam a big bang | P5.11 | nova | G19 |
| **§4.1 Nascimento (P0)** | Flow | nenhum dos quatro perfis pode escrever `MANDATO` e `Perfis e zonas`: o dia 1 não tem actor legal | P0.11 | nova | G1 |
| **§4.2.1** | Flow | pressupõe-se que o merge tem sempre êxito | P3.20 | nova | G11 |
| **§4.2.2** | Flow | pressupõe-se que uma corrida do watcher termina antes da seguinte | P3.25 | nova | G11 |
| **§4.2.3** | Flow | pressupõe-se que a indexação corre antes do watcher no mesmo merge | P3.17 (ordem explícita) | corrigida | G8 |
| **§4.2.4** | Flow | pressupõe-se uma triagem de cada vez; `ESTADO` e `FRENTES` são substituição sem token de versão | P3.25 (`base_hash`), `FRENTES` por inversão, `ESTADO` com proveniência por facto | nova + reformulados | G9 |
| **§4.2.5** | Flow | pressupõe-se que sessões a correr revalidam o índice; não há invalidação | P3.24, `indice-decisoes.json` (`indice_versao`) | nova + esquema | G8 |
| **§4.2.6** | Flow | decisões produzidas em modo rumo podem não passar por merge, e G8 nunca se activa para elas | **parcial**: P3.24 e `indice_versao` detectam o índice velho; nenhuma regra obriga a decisão de rumo a passar por merge | parcial | G8 (parcial) |
| **§4.3** | Flow | 22 resíduos, zero actores, nenhum em P7.2 | P3.31 (inventário com actor e cadência), P7.2 (worktrees órfãs, ramos `suspenso` com referente morto, escaladas abertas, achados abertos), P1.14, P3.22, `alerta-estado.log`, P5.12 (retenção) | novas + corrigidas | G9, G13 |

### 2.4 Bloco D · Enquadramento

| Achado | Lente(s) | Defeito | Regra ou artefacto alterado | Natureza | Garantia que restaura |
|---|---|---|---|---|---|
| **UK1** | Blind | o diagnóstico de §1.2 é etiologia postulada, sem incidente registado | **parcial**: P5.9 (grau `postulada`, candidata a remoção sem incidente), T10 | nova + tensão | G16 |
| **UK2** | Blind | o canon está isento da sua própria regra de prova (P5.4) | P5.8, P5.9, `canon/regras.json` | novas | G16 |
| **UK3** | Blind | pressupõe-se um humano responsável sempre presente | P0.9, P0.13, `MANDATO` (`responsavel`, `sucessor`, `prazo_indisponibilidade`) | novas | G22 |
| **UK4** | Blind | «ler é grátis»: zero ocorrências de custo, orçamento, latência | P0.10, P7.7, `METRICAS` | novas + artefacto | G20 |
| **UK5** | Blind | P7.2 são 16 verificações mensais sem estimativa de duração | P7.2 partida em automática (`watcher`) e humana; `orcamento.horas_auditoria_mes` | corrigida | G20 |
| **UK6** | Blind | «detector» lido como «mecanismo»; a coluna dá a todas as regras a mesma aparência de força | coluna *Força* ∈ {mecânica, convenção}, com proibição de `convenção` + `bloqueia` | transversal | G15 |
| **UK7** | Blind | há defesa para o hook ausente (P4.5) e nenhuma para o hook errado | P4.7 (teste negativo obrigatório, matriz `regra → detector → teste`), P7.3 (matriz incompleta é achado) | nova + corrigida | G15 |
| **UK8** | Blind | 13 regras têm `relatório` como única consequência e deviam ler-se `nenhuma` | P7.5 (estado, dono, prazo; dois ciclos bloqueiam abertura de frente), `ACHADOS` | nova + artefacto | G21 |
| **UK9** | Blind | zero referências a versão de modelo ou prompt; `sealed/` não é reprodutível | P3.29, P4.8, `sealed/`, `CASOS`, `INBOX/*` (`modelo`, `versao`) | novas + esquemas | G8, G17 |
| **UK10** | Blind | três sessões limpas do mesmo modelo são três amostras, não três juízes | P0.12 (dissimilaridade declarada, veredictos persistidos), P3.27 | novas | G1, G2, G17 |
| **UK11** | Blind | «o mundo é o repositório»: trabalho fora do disco é invisível e `ALERTA` vazio não distingue saúde de cegueira | **não implementado** | — | — |
| **UK12** | Blind | «slug global e único» sem âmbito declarado; com dois projectos, colisão ou fragmentação | **não implementado**; só P5.12 liberta o espaço de nomes no encerramento | parcial | — |
| **UU1** | Blind | validação distinta de verificação: sete números arbitrários apresentados como derivados | P7.6 (justificação e data de revalidação por limiar), `MANDATO.limiares[]` | nova + esquema | G16 |
| **UU2** | Blind | instrumentação do processo: mede conformidade, nunca fluxo | P7.7, `METRICAS`, P7.1 (auditoria extraordinária por sinal) | novas + artefacto | G20 |
| **UU3** | Blind | integridade de leitura inexistente: `research/` livre e `INBOX.texto` escrito por frentes | P3.23, `classe_integridade` nos esquemas, `PERFIS.classe_leitura_maxima` | nova + esquemas | G18 |
| **UU4** | Blind | adopção e migração ausentes: big bang ou nada | P5.11 | nova | G19 |
| **UU5** | Blind | P0.4 obriga a declarar `criterio_fim` e nada diz o que se faz quando é atingido | P5.12 | nova | G19 |
| **UU6** | Blind | nada declara este sistema um fracasso; o governo isenta-se do que obriga às árvores | P5.10 (caducidade do canon) | nova | G19 |
| **UU7** | Blind | ergonomia do operador único: automatiza o fácil e concentra o julgamento residual no humano | **parcial**: P0.13, P7.2 partida, P5.11, P0.10 (`horas_auditoria_mes`) | parcial | G20, G22 |

**Cobertura.** 69 achados na matriz: 19 (Bloco A) + 12 (Bloco B) + 19 (Bloco C, incluindo 12 workflows, 6 pressupostos de ordem e o inventário de resíduos) + 19 (Bloco D). Implementados: 62. Parciais: 4 (§4.2.6, UK1, UK12, UU7). Não implementados: 1 (UK11), mais os dois parciais sem regra própria. As 12 perguntas de §8 da auditoria traduzem-se em parâmetros pendentes (secção 7) e em decisões fixadas (secção 5); nenhuma fica sem destino.

---

## 3 · Alterações por protocolo

### 3.1 P0 · Nascimento

**Corrigidas**

- **P0.2.** Dizia: «o mandato **deve** declarar dois a três não-objectivos por objectivo». Passa a: «**deve** declarar **pelo menos** dois não-objectivos por objectivo». O tecto colidia com o procedimento de correcção do próprio §2.1.1 — «acrescentar não-objectivos e registar em `CASOS`» —, que ao terceiro não-objectivo ficava proibido. O controlo de volume passa inteiro para P0.3.
- **P0.3.** Mantém o tecto de uma página e ganha base de contagem: contam-se os valores de texto, excluindo chaves e slugs. Um hook que bloqueia por contagem tem de contar algo definido (UU1, P7.6).
- **P0.5, P0.6.** Força `convenção`, consequência `relatório`. Um humano não é um trinco (C6); a obrigação mantém-se, a aparência de mecanismo cai.
- **P0.7.** Passa a força mecânica com detector `hook`: lê os veredictos persistidos pelas sessões de verificação de P0.12. Deixa de ser uma afirmação sobre o que o humano fez e passa a ser uma leitura de ficheiro.

**Novas**

- **P0.9.** O `MANDATO` declara `responsavel` e `sucessor`, com contacto e data de validade. Fecha UK3: nove regras dependiam de um humano cuja ausência não estava modelada.
- **P0.10.** O `MANDATO` declara orçamento — chamadas de modelo por merge e por fecho, horas-humano por mês para auditoria — e o excesso bloqueia a abertura de frente nova. Fecha UK4 e dá mecanismo a G20.
- **P0.11.** A fase de nascimento é executada pelo humano responsável fora do regime de perfis; `desbloqueado` é a fronteira de entrada no regime. Fecha o «dia 1 sem actor legal» (§4.1).
- **P0.12.** Os testes de discriminação e de reformulação correm em três sessões com dissimilaridade declarada, e os três veredictos são persistidos com `modelo` e `versao`. Fecha UK10: concordância de três amostras do mesmo modelo mede consistência, não correcção.
- **P0.13.** Com o responsável indisponível além do prazo declarado, o projecto entra em modo degradado: as frentes abertas continuam, nenhuma abre, o facto é registado. Fecha a segunda metade de UK3 — o sistema que não pode emendar-se e também não morre.

### 3.2 P1 · Árvore

**Corrigidas**

- **P1.1.** Acrescenta ao que já obrigava (modo e condição de morte) a declaração de estado (`aberta`/`morta`), com morte datada e atribuída. Sem campo de estado, o detector de P1.11 apontava para nada (B4).
- **P1.2.** Dizia auditor · relatório. Passa a hook · bloqueia, contando eixos distintos entre os filhos de um nó. Só é executável depois de `eixos[]` e `pai` existirem (B3).
- **P1.9.** Passa a hook · bloqueia na geração da primeira frente a partir de uma árvore. A contagem de árvores no mesmo modo é verificável; não precisava de auditor.
- **P1.8.** Não é nomeada no dossiê. Resolve-se por aplicação da regra geral da coluna *Força*: detector `humano` com consequência `bloqueia` é proibido, logo P1.8 passa a `convenção`/`relatório`. Registado aqui para que a ausência não se leia como omissão.

**Novas**

- **P1.12.** O grafo `depende[]` não pode conter ciclos. Fecha metade de C17: o documento proíbe ciclos causais na porta de entrada e permitia-os no grafo de dependências.
- **P1.13.** A poda ou morte de um ramo liberta para reavaliação obrigatória todos os ramos que dele dependem; `retido` conta como resultado negativo; a reavaliação ganha terceira saída, `referente_morto → podar com razão herdada`. Fecha o estado absorvente `suspenso:` com referente morto.
- **P1.14.** À morte de uma árvore, todo o ramo `retido` transita para `podado` com razão, ou para `fechado` se entregou significado. Fecha o deadlock de `retido` sem cortar o modo Caracterização (D1).
- **P1.15.** Podar um ramo com frente aberta emite `ramo_podado_sob_frente` e fecha a frente com razão herdada. Detector `watcher`, consequência alerta.
- **P1.16.** A poda produz entrada em `debates/` de tipo `poda`. É o que torna G13 real: sem entrada no índice, o slug podado nunca fica `morto` e o hook nunca bloqueia a recriação (B10).

### 3.3 P2 · Caminho

**Corrigidas**

- **P2.5.** Dizia: «um pressuposto invalidado **deve** disparar reavaliação antes de abrir frente nova», com detector «`invalidado` sem reavaliação datada». Não havia chave de junção: `pressupostos[]` não tinha data e `reavaliacoes[]` não referenciava o pressuposto, pelo que qualquer reavaliação anterior satisfazia o hook para qualquer pressuposto. Passa a comparar `pressupostos[].estado_data` com `reavaliacoes[].data` para o mesmo `pressuposto_slug` (C16).

**Novas**

- **P2.8.** O resultado de um pressuposto sobe por item de `INBOX` de tipo `pressuposto_resolvido`, e a triagem propaga-o a `CAMINHO.pressupostos[]` e reordena `ordem_ataque[]`. Fecha o canal ausente de que dependia toda a ordem de ataque de MP5.
- **P2.9.** A reavaliação ganha actor: o perfil `caminho`, disparado por pressuposto invalidado, por cadência declarada ou pelo humano; escreve só em `CAMINHO`; a saída é uma das quatro e fica registada. Fecha a segunda metade de C16 — um projecto que não abra frentes nunca reavaliava.
- **P2.10.** A abertura de frente cruza `toca[]` contra as frentes abertas e recusa em colisão. Prevenção na abertura, que é barata, em lugar de detecção no fecho, que é cara (C13).
- **P2.11.** `inconclusivo` repetido sobre o mesmo pressuposto além de um tecto declarado escala ao humano. Sem tecto, «redesenhar o teste, não repetir» é um ciclo sem saída.

### 3.4 P3 · Desenvolvimento

**Corrigidas**

- **P3.2.** Ganha no texto da regra: «…salvo os não-objectivos e os casos, nos termos de P3.3». A excepção estava em §2.4.2 e a Convenção de leitura desobriga a prosa — logo também não a deixava isentar. Sem isto, o hook bloqueava se carregasse e bloqueava se não carregasse (C1).
- **P3.3.** Alargada a `CASOS`: não-objectivos **e** casos carregados inteiros em toda a sessão que classifique. Os casos são o produto da correcção de P0.7 e não chegavam a quem classifica.
- **P3.4.** Deixa de nomear dois modos em prosa e remete para o manifesto `TRAJECTOS`, com os quatro modos nomeados: substituição, acrescento, log, write-once (B2).
- **P3.5.** Dizia «não pode conter conteúdo reconstruível por ferramenta», com hook bloqueante — indecidível. Passa a lista branca de tipos de referência admissíveis em `sealed/`, mais `hash_conteudo` do referente, mais proibição de apagar um referente de selagem. Sem a última, a proveniência de uma frente morta é um conjunto de ponteiros mortos (C14).
- **P3.9.** Reformulada, não cortada (D6). O aviso devolve identificador e grau, nunca conteúdo, alternativa ou razão. O conceito muda de nome para **aviso de protecção**, com entrada própria em §0, porque `alerta` tinha três sentidos activos (C19).
- **P3.10.** Dizia que cada item de `ALERTA` deve ter estado em `ALERTA-ESTADO` e que só a triagem escreve — e a triagem só acorda depois de o item existir, num ficheiro de acrescento onde transitar de estado exige reescrever uma chave. Passa a: o watcher inscreve `novo` ao emitir; só a triagem transita `novo → visto | descartado | resolvido`; `visto` tem caducidade declarada. Fecha C3 e o `visto` perpétuo de §4.3.
- **P3.11.** Deixa de suprimir por hash indefinidamente: não se reemite `descartado` nem `resolvido` **enquanto o par não mudar de conteúdo**, e a reabertura por decisão do humano fica registada. Resolve o dilema de C4 pelo lado em que um conflito real recorrente não fica suprimido para sempre.
- **P3.13.** Ganha excepção de drenagem: com `HALT` presente, o hook permite exclusivamente a escrita de `handoff.json` e a selagem da sessão em curso. O desenho anterior produzia o estado parcial que invocava para se justificar (C5).
- **P3.15.** O detector deixa de ser «a triagem não tem zona em `MANDATO`» — que não detecta a falha descrita — e passa a `gate` na escrita de estado de alerta: transição para `descartado` ou `resolvido` num item cujo par toque slug de objectivo bloqueia e exige humano. A triagem recebe os **slugs** dos objectivos, não o texto, o que mantém o escopo de §2.4.2 (C9).
- **P3.16.** O item do fecho brando vai para `INBOX` de tipo `fecho_brando`, nunca para `ALERTA`. O gate escrevia num ficheiro cujo escritor declarado é o watcher, e a corrida seguinte destruía-o (C2).
- **P3.17.** Ordem explícita: selar (fase 1) → merge → regenerar índice → watcher → selar (fase 2). Toda a corrida do watcher fica registada. Fecha §4.2.3 e dá detector a B6.

**Novas**

- **P3.18.** O watcher corre as três passagens a cada corrida e regista a passagem de origem de cada item. O actor mais importante do sistema não aparecia no detector de nenhuma das 60 regras; é o que torna G11 real.
- **P3.19.** O watcher conta os itens `por_processar` do `INBOX` e emite alerta acima do limiar declarado; todo o item `pressuposto_caido` gera alerta imediato. É a contagem que G10 atribuía ao watcher e que nenhuma regra obrigava, e quebra o impasse de C8.
- **P3.20.** Um merge falhado deixa a frente em `merge_pendente`, emite `falha_de_sistema` e alerta de passagem `merge`, e atribui a resolução ao humano; a selagem em duas fases impede selar o que não fundiu.
- **P3.21.** `toca_declarado[]` é write-once na abertura, fora da zona da frente; o gate compara-o com `toca_efectivo[]` calculado do diff; ampliar a toca é evento próprio, cruzado em tempo real. Fecha a auto-certificação de C13 e dá saída legal à sessão que descobre que toca mais.
- **P3.22.** Todo o item de `INBOX` tem `slug` e `estado`, e a triagem escreve o estado e devolve o resultado ao autor. Cria a operação «processar», que não existia (C7).
- **P3.23.** Integridade de leitura: toda a fonte tem classe (`canon`, `produzido_sob_gate`, `nao_verificado`) e conteúdo `nao_verificado` não pode ser montado como instrução. Fecha UU3 e é a base de G18.
- **P3.24.** O hook revalida `indice_versao` em cada edição e recusa a escrita quando o índice mudou desde o arranque da sessão (§4.2.5).
- **P3.25.** Merges e corridas do watcher são serializados; todo o ficheiro de substituição carrega `base_hash` (§4.2.2, §4.2.4).
- **P3.26.** O conteúdo de `Rascunhos` que sobreviva à sessão converte-se em item `descoberta` antes de o gate verificar o vazio. Sem isto, «Rascunhos não vazio → não fecha» é um beco (§4.1, S5 duro).
- **P3.27.** O cold-read é executado pelo perfil `verificacao`, único com zona no campo `cold_read`; domínio `passa | falha | nao_corrido`, com `nao_corrido` tratado como divergência branda (C15).
- **P3.28.** A marca `carece_aprovacao` é levantada por actor distinto da frente, em `APROVACOES`; a frente não pode transitá-la de `true` para `false`.
- **P3.29.** Todo o output de agente registado carrega `modelo` e `versao` (UK9).
- **P3.30.** `HALT` ganha esquema e procedimento de saída: inventário de worktrees não fundidas, inventário de selagens sem merge, decisão por item, registo de `falha_de_sistema`.
- **P3.31.** Toda a worktree de frente fechada, abandonada ou em `merge_pendente` consta do inventário de limpeza, com actor e cadência (§4.3).

### 3.5 P4 · Alocação

**Corrigidas**

- **P4.1, P4.3.** Força `convenção`, consequência `relatório`. São decisões de alocação tomadas por um humano; não há trinco (C6). O conteúdo de P4.1 não muda: um processo permanente continua a não poder julgar.
- **P4.5.** O detector deixa de ser o próprio hook a verificar a sua presença no arranque — auto-referência — e passa a `watcher`: o processo persistente confirma a cada corrida a presença dos hooks. A verificação sai de dentro do que verifica.

**Novas**

- **P4.6.** A indisponibilidade de hook escreve `HALT` com `razao: hook_indisponivel`. Converte a recusa individual de P4.5 em paragem declarada, alinhada com T4.
- **P4.7.** Uma regra de força mecânica não entra em vigor sem teste negativo que demonstre que o detector recusa o caso proibido, com matriz `regra → detector → teste`. Fecha UK7: havia defesa contra o hook ausente e nenhuma contra o hook errado.
- **P4.8.** Uma mudança de modelo exige decisão registada e obriga a repetir P0.7 e as sondas de fronteira. P4.4 exigia decisão para mudar de runner e nenhuma para mudar de modelo, que é a variável que muda o comportamento (UK9).
- **P4.9.** O orquestrador consta da tabela de actores, com disparo declarado e zona nula. O ponto de entrada do sistema não estava modelado (C18).

### 3.6 P5 · Evolução

Nenhuma regra de P5 é corrigida no texto; o protocolo corrige-se por adição. P5.4 mantém-se e deixa de ser isenta a si própria por força de P5.9.

**Novas**

- **P5.7.** Toda a emenda ao `MANDATO` repõe `desbloqueado: null` até novo teste, dispara reavaliação do caminho e emite alerta a cada frente aberta cuja projecção dependa de objectivo emendado. Fecha a propagação ausente (§4.1) e liga-se a G1.
- **P5.8.** O canon é artefacto governado: tem slug, reside em zona exclusiva do perfil `rumo`, e é alterado por emenda datada com decisão em `debates/`. Fecha C12 pelo lado da escrita.
- **P5.9.** Uma regra do corpo inicial nasce com grau `postulada`; confirma-se com o primeiro incidente que a motive e, sem incidente ao fim do prazo declarado, é candidata a remoção. Fecha C12 e UK2 pelo lado da prova, e é o travão declarado de T6 e o único tratamento possível de UK1.
- **P5.10.** O canon declara caducidade: sem reafirmação activa no fim de cada período declarado, entra em `caduco`. Manter o governo passa a exigir um acto, em vez de o abandonar exigir um (UU6).
- **P5.11.** A adopção por um projecto em curso segue período de transição declarado, com os detectores mecânicos primeiro em modo de aviso e só depois bloqueantes, e inventário do existente (UU4). Força `convenção`.
- **P5.12.** Atingido o `criterio_fim`, o projecto segue protocolo de encerramento: desligar o watcher, fechar árvores vivas, arquivar com política de retenção declarada, libertar o espaço de nomes (UU5).

### 3.7 P6 · Saída

- **P6.1.** A estrutura mantém-se. A contagem de pilares — três ou quatro, ME entre si — passa a força `convenção`: é regra de comunicação, não facto verificável por máquina, e o cold-read não a mede.
- **P6.2.** Alinhada com P3.27: o cold-read é feito pelo perfil `verificacao`, devolve `passa | falha | nao_corrido` e tem timeout declarado. Deixa de ser auto-certificado e deixa de não ter valor de erro (C15).

### 3.8 P7 · Auditoria

**Corrigidas**

- **P7.1.** A cadência mensal mantém-se para a parte humana e acrescenta-se **auditoria extraordinária** disparada por `falha_de_sistema`, limitada à listagem afectada. A auditoria deixa de ser só calendário e passa a disparar por sinal (UU2).
- **P7.2.** Partida em duas: **P7.2 automática**, corrida a cada merge com detector `watcher`, e **P7.2-humana**, mensal. A listagem cresce com onze itens: ramos `suspenso:` com referente morto ou de árvore morta; ciclos em `depende[]`; `toca` alterado após abertura; escaladas abertas além do prazo; achados abertos há dois ciclos; worktrees órfãs; corridas do watcher falhadas ou com passagem semântica em erro; presença e integridade dos hooks; regras `postuladas` sem incidente; consumo face ao orçamento; referências pendentes entre esquemas. A partição é o que impede que UK5 se realize: uma listagem que custa seis horas é feita duas vezes e abandonada, e com ela caem os detectores únicos de G2, G4, G5, G9, G12, G13, G15 e G16.
- **P7.3.** Alargada de *linter* de forma a verificação de consistência: passa a procurar contradições entre regras (pares com detector e consequência incompatíveis sobre a mesma operação); entradas de §0 sem uso; garantias cujo detector nomeie actor que nenhuma das suas regras invoca; regras de força `convenção` com consequência `bloqueia`; matriz `regra → detector → teste` incompleta. C1, C3 e C9 pertencem todas a uma classe que P7.3 não procurava (C19).

**Novas**

- **P7.5.** Todo o achado tem estado em `ACHADOS` (`aberto`, `aceite`, `corrigido`), dono e prazo; um achado `aberto` há dois ciclos bloqueia a abertura de frente nova. É o que torna `relatório` uma consequência e fecha C11 e UK8; sem isto, treze regras leem-se `nenhuma`.
- **P7.6.** Cada limiar numérico tem justificação registada e data de revalidação; um limiar por revalidar é achado. Separa validação de verificação (UU1).
- **P7.7.** O auditor regista as métricas de fluxo declaradas — tempo por fecho, proporção de fechos brandos, idade dos itens de `INBOX`, tempo até triagem, razão entre sessões de governo e sessões de trabalho, consumo face ao orçamento — e a auditoria extraordinária dispara por sinal fora dos limites. Fecha UU2 e é a metade de G20 que mede.

---

## 4 · Alterações ao Anexo A

O preâmbulo do Anexo A muda de natureza: os esquemas passam a **fechados**. Um campo não previsto é rejeitado pelo hook. Era a condição que B12 impunha para G10 («o lixo não entra») deixar de ser retórica. Todos os ficheiros ganham `versao_esquema` (B11).

### 4.1 Artefactos novos

| Ficheiro | Escrita | Quem | Campos | Que regra passa a ser executável |
|---|---|---|---|---|
| `PERFIS` | substituição | humano | `versao_esquema` · `perfis[]{slug, zona_leitura[], zona_escrita[], runner, hooks_obrigatorios[], classe_leitura_maxima}` | P3.1, P3.2, P3.14, P4.2, P5.2, P7.4 (B1); `classe_leitura_maxima` habilita P3.23 |
| `TRAJECTOS` | substituição | humano | `versao_esquema` · `trajectos[]{padrao, nivel, modo_escrita, classe_integridade}` | P3.1 e P3.4 (B2): o hook de trajecto deixa de ler prosa |
| `corridas/<id>.json` | acrescento | watcher | `id` · `data` · `merge_ref` · `passagens[]{nome, estado: corrida\|falhada\|timeout}` · `itens_emitidos[]` · `duracao` | P3.17, P3.18, P3.11, P7.2 automática (B6) |
| `alerta-estado.log` | log | watcher, triagem | `[{hash, estado, data, quem, razao}]`, leitura última-vence | P3.10, P3.11, P3.15 (C3): transitar estado deixa de exigir reescrever uma chave |
| `ACHADOS` | log | auditor, humano | `[{slug, auditoria_slug, regra, severidade, estado, dono, prazo, data}]` | P7.5 (C11, UK8): dual de `alerta-estado.log` para o lado do auditor |
| `ESCALADAS` | acrescento | triagem | `itens[]{slug, data, item_ref, razao, objectivo_slug, estado, prazo}` | P3.15, P2.11 (C10): a escalada deixa de ser a esperança de que o humano leia `ALERTA` |
| `APROVACOES` | acrescento | humano, triagem | `itens[]{frente_slug, data, quem, veredicto, razao}` | P3.28 (§4.1): dá actor à aprovação de `carece_aprovacao` |
| `canon/regras.json` | substituição | rumo | `versao_canon` · `caduca_em` · `regras[]{id, grau: viva\|postulada\|morta, forca, detector, consequencia, incidente_slug, teste_ref}` | P5.4, P5.5, P5.8, P5.9, P5.10, P4.7, P7.3 (B7, C12) |
| `HALT` | write-once | humano, watcher | `data` · `quem` · `razao` · `escopo` | P3.13, P3.30, P4.6 (C5): deixa de ser presença sem origem |
| `METRICAS` | acrescento | auditor | `[{data, indicador, valor, limite}]` | P7.7, P7.1 extraordinária (UU2) |

### 4.2 Esquemas corrigidos

**`MANDATO`** — acrescenta `slug`, `versao_esquema`, `responsavel`, `sucessor`, `orcamento{chamadas_merge, chamadas_fecho, horas_auditoria_mes}`, `prazo_indisponibilidade`, `limiares[]{nome, valor, justificacao, revalidar_em}`. `nao_objectivos[]` deixa de ser lista de texto e passa a `{slug, texto, caso_slug}`; `emendas[]` passa de `{data, decisao_slug}` a `{data, decisao_slug, alvo_slug, antes, depois}`. Habilita P0.9, P0.10, P0.13, P7.6 e P5.7 (que precisa de `alvo_slug` para saber que frentes alertar). `slug` no não-objectivo é o que permite P3.15 dar slugs à triagem em vez de texto.

**`CAMINHO`** — `pressupostos[]` acrescenta `estado_data`, `sustenta[]`, `frente_slug`, `incerteza`, `custo_descobrir_tarde`, `custo_testar`; `reavaliacoes[]` acrescenta `disparo`, `pressuposto_slug`, `caminho_antes`, `caminho_depois`; `ordem_ataque[]` passa a tipado como `pressuposto_slug[]`. Habilita P2.5 (chave de junção), P2.8 (reordenação verificável) e P2.9 (`disparo` registado). Os três campos de custo tornam MP5 calculável em vez de declarativa.

**`arvores/*`** — acrescenta `estado`, `morta_em`, `morte_verificada_por`; `nos[]` acrescenta `pai` e substitui `eixo` por `eixos[]`, acrescenta `suspenso_em: slug | null`; `estado` do nó passa a enumerado; `razao` obrigatória quando `podado`; `depende[]` passa a referência qualificada `{arvore_slug, no_slug}`. Habilita P1.1, P1.2, P1.11, P1.12, P1.13, P1.14 e a representabilidade dos modos Caracterização e Mandato (B3, B4). A referência qualificada é o que permite detectar ciclos entre árvores, não apenas dentro de uma.

**`INBOX/*.json`** — acrescenta `slug`, `estado` (`por_processar`, `processado`, `rejeitado`), `modelo`, `versao`, `classe_integridade`; `pressuposto` passa a condicionado ao `tipo`; os tipos passam de três a cinco: `descoberta`, `pressuposto_caido`, `pressuposto_resolvido`, `falha_de_sistema`, `fecho_brando`. Habilita P3.22 (a operação «processar»), P3.19 (a contagem), P2.8 (a subida do pressuposto resolvido), P3.16 (o canal próprio do gate) e P3.23 (`texto` entra marcado como `nao_verificado`).

**`estado.json`** — acrescenta `slug`, `data`, `projeccao{pressuposto_slug, regra_paragem, fronteiras_negativas[]}`, `base_hash`, `modelo`, `versao`. `toca_declarado[]` **sai do ficheiro** para escrita write-once fora da zona da frente; permanece `toca_efectivo[]`, calculado do diff. Habilita B5 (a projecção deixa de existir só em prosa), P3.21 (fim da auto-certificação de C13), P3.25 (`base_hash`), P3.27 (`cold_read` sai para a zona do perfil `verificacao`) e P3.28 (`carece_aprovacao` deixa de ser transitável pela frente).

**`handoff.json`** — acrescenta `slug`, `data`, `cold_read`, `bloqueio{tipo, detalhe}`; `referencias[]` passa a tipado. Habilita P3.13 na excepção de drenagem (há o que escrever quando `HALT` está presente) e P3.20 (`bloqueio` exprime `merge_pendente`).

**`debates/*.json`** — acrescenta `tipo: rumo|runner|decisao_de_arvore|poda|modelo`, `sela[]`, `desbloqueia[]`, `retira[]`, `aplicacao_esperada[]`; `afecta[]` passa a referências qualificadas. Habilita B9 (os graus `selado` e `morto` passam a ser produzíveis), B10 (zona de escrita por tipo, quatro produtores), P1.16, P4.8 e G12 — `aplicacao_esperada[]` é o que o gate verifica para que «decisões são aplicadas» tenha detector.

**`indice-decisoes.json`** — passa de `{slug_afectado: [decisao_slug]}` a `{slug: {grau, decisoes[], base_merge}}` e acrescenta `gerado_em` e `indice_versao`. Habilita P3.8 (o hook lê o grau em vez de o inferir), P3.24 (revalidação de índice) e a precedência entre decisões sobre o mesmo slug.

**`ALERTA`** — passa a **derivado**, regenerado a partir de `corridas/*` e de `alerta-estado.log`, em lugar de substituído a cada corrida. Acrescenta `corrida` e `data`; `itens[]` acrescenta `passagem` (com os valores novos `merge` e `semantico_indisponivel`), `slug_tocado` e `origem`; o `hash` passa a definido como `H(passagem, par ordenado, slug_tocado)`; sai `decisao_slug`, porque o aviso de protecção tem canal próprio (P3.9). Habilita C2, C3, C4 e P3.18.

**`ESTADO`** — `factos[]` acrescenta `data`, `origem_frente`, `corrida`. Mantém-se como ficheiro de substituição, e não é cortado (D2): ganha proveniência por facto, o que dá ao auditor matéria para o item «contradições entre `ESTADO` e `FRENTES`» de P7.2.

**`FRENTES`** — deixa de ser escrito pela triagem e passa a **gerado por inversão** dos `estado.json`, como `indice-decisoes.json`. Acrescenta `depende[]`, `arvore_slug`, `worktree`, `zona`, e `estado` com domínio enumerado (`aberta`, `em_trabalho`, `bloqueada`, `merge_pendente`, `carece_aprovacao`, `fechada`, `abandonada`, `obsoleta`). Corrige de uma vez o fecho limpo que nunca actualizava `FRENTES` (§4.1) e a actualização perdida de §4.2.4, porque deixa de haver escrita concorrente.

**`REJEICOES`** — acrescenta `slug` e `item_ref`. Não é cortado (D2); ganha a referência que o liga ao item de `INBOX` que o originou, o que dá leitor declarado ao ficheiro.

**`CASOS`** — acrescenta `slug`, `nao_objectivo_slug`, `sonda_slug`, `modelo`, `versao`. `nao_objectivo_slug` liga o caso ao não-objectivo que ele delimita, o que torna P3.3 alargada carregável por escopo em vez de inteira; `modelo` e `versao` registam em que substrato a classificação foi feita (UK9).

**`sealed/`** — deixa de ser só um modo de escrita e ganha esquema próprio: `{slug, data, pedido_ref, output_ref, hash_conteudo, modelo, versao, fase}`. `hash_conteudo` torna P3.5 decidível; `fase` distingue a selagem pré-merge da pós-merge exigida por P3.17 e P3.20; `modelo` e `versao` são a condição de `sealed/` ser proveniência reprodutível (C14, UK9).

### 4.3 Retirado

**`ALERTA-ESTADO`** deixa de existir como ficheiro. O seu conteúdo distribui-se por `alerta-estado.log` (o registo das transições, em log, leitura última-vence) e por `ALERTA` regenerado (a projecção corrente). É a única amputação de artefacto do lote, e é consequência de D3, não de um corte.

---

## 5 · Decisões de desenho e alternativas rejeitadas

As sete decisões fixadas na Parte 0 do dossiê. Cada uma resolve uma divergência entre lentes ou uma escolha que a auditoria deixou em aberto.

### D1 · Os quatro modos de árvore mantêm-se

**Contexto.** A lente de red teaming propôs cortar os modos Caracterização e Mandato: Caracterização é a fonte do deadlock de `retido`, não concorre e não decide; Mandato é uma conversa, não uma partição de espaço. A lente de arquitectura propôs corrigir o esquema: `eixos[]` e `pai` tornam ambos representáveis (B3).

**Decisão.** Corrigir o esquema. Os quatro modos mantêm-se.

**Alternativa rejeitada.** Cortar os dois modos. Era mais barato e mais reversível, e resolvia o deadlock de `retido` por eliminação.

**Consequências.** Cortar um modo é alteração de desenho, não correcção de defeito, e o pedido é implementar as falhas, não amputar o modelo do autor. O deadlock de `retido` passa a ser resolvido por regra (P1.14), não por remoção do estado. Mantém-se aberta a tensão T5, porque quatro modos continuam a ser o ponto onde o sistema pode crescer sem limite; o travão continua a ser P1.1 mais, agora, P1.13 e P1.14.

### D2 · `ESTADO` e `REJEICOES` corrigem-se; `FRENTES` passa a gerado

**Contexto.** Três posições: cortar `ESTADO` e `REJEICOES` por serem escritores sem leitor declarado, que reproduzem o sintoma de §1.2; enriquecê-los com proveniência por facto; ou gerar `FRENTES` por inversão dos `estado.json`.

**Decisão.** Corrigir. `FRENTES` passa a gerado por inversão; `ESTADO` ganha proveniência por facto; `REJEICOES` ganha `slug` e `item_ref`.

**Alternativa rejeitada.** Cortar os dois ficheiros.

**Consequências.** A inversão corrige simultaneamente três achados que o corte não corrigia: o fecho limpo que nunca actualizava `FRENTES` (§4.1), a actualização perdida por substituição concorrente (§4.2.4) e a ausência de estado enumerado da frente. O custo é um segundo gerador por inversão a correr a cada merge, com a mesma exigência de ordem que P3.17 impõe ao índice de decisões.

### D3 · `ALERTA-ESTADO` reformula-se em log de corridas mais projecção

**Contexto.** Uma posição propunha cortar `ALERTA-ESTADO` e transformar `ALERTA` em ficheiro de acrescento com `fechado_em` e razão, o que eliminava C3, C4 e dois itens de P7.2. Outra propunha log de corridas mais projecção, mais poderoso, mas com um terceiro modo de escrita e reescrita de P3.4.

**Decisão.** Log de corridas mais projecção: `corridas/<id>.json` em acrescento, `alerta-estado.log` em log com leitura última-vence, `ALERTA` derivado e regenerado.

**Alternativa rejeitada.** `ALERTA` em acrescento com `fechado_em`.

**Consequências.** Resolve de uma vez quatro coisas que a alternativa resolvia em parte: a substituição concorrente (C2), o mapa em acrescento onde transitar exige reescrever uma chave (C3), o `visto` perpétuo (§4.3) e a ausência de registo de corrida (B6). O custo é o quarto modo de escrita, `log`, que obriga P3.4 a remeter para `TRAJECTOS` — o que B2 já exigia por outra razão — e um ficheiro que cresce sem tecto, cuja rotação cai no inventário de P3.31.

### D4 · O detector semântico ganha contrato

**Contexto.** Uma posição propunha cortá-lo: produz sugestões que nenhuma regra obriga a tratar e custa uma chamada de modelo por merge sem consequência declarada. Outra propunha dar-lhe contrato.

**Decisão.** Dar contrato: timeout declarado, valor de erro, alerta de indisponibilidade, estado da passagem registado em `corridas/*`.

**Alternativa rejeitada.** Cortar.

**Consequências.** É a única mitigação declarada de T2 — a completude das dependências —, e sem ela T2 fica sem resolução nenhuma. Sem contrato, degradava-se em silêncio, que é o modo de falha que §1.4 mais teme. O custo é a chamada por merge entrar no orçamento de P0.10 e a passagem em `timeout` passar a ser item de P7.2 automática.

### D5 · Numeração aditiva, sem excepção

**Contexto.** Corrigir 28 regras e acrescentar 41 abria a hipótese de reorganizar a numeração por tema.

**Decisão.** Aditiva. Regra que sobrevive mantém o identificador, mesmo com o texto corrigido; regra nova recebe o número seguinte do seu protocolo; nenhuma regra é renumerada; regras retiradas não aparecem no corpo e ficam registadas neste relatório.

**Alternativa rejeitada.** Renumerar por tema ou por força.

**Consequências.** É a regra do próprio documento (P5.5 e a Convenção de numeração aditiva), e preservar identificadores mantém resolvíveis todas as referências externas — auditoria, este relatório, futuros `debates/`. O custo é que a ordem de leitura de P3 deixa de ter relação com a ordem de execução: P3.17 descreve a sequência que P3.20 e P3.25 condicionam, e P3.10 lê-se antes de P3.19, que é o que a faz disparar.

### D6 · Os cortes propostos não se executam

**Contexto.** A lente de red teaming propôs uma lista de cortes para compensar o que as correcções acrescentam, estimando que o núcleo sobrevivente — cerca de vinte regras — sustenta G1, G6, G7, G8, G11, G14 e G17.

**Decisão.** Não executar os cortes, com duas excepções absorvidas pela correcção: `ALERTA-ESTADO` desaparece como ficheiro por via de D3, e P3.9 é reformulada em vez de cortada.

**Alternativa rejeitada.** Executar a lista de cortes.

**Consequências.** O pedido é implementar correcções, e cortar é decisão de produto do autor. A consequência assumida é T6: o corpo cresce 68% e o critério de sucesso «governo estável» fica pior no acto de se corrigir. A lista fica registada na secção 6 como recomendação não executada, com o núcleo identificado, de modo a que o autor a possa executar depois sem repetir a análise.

### D7 · O inchaço declara-se em vez de se esconder

**Contexto.** Corrigir todos os defeitos faz o corpo crescer, e o crescimento tensiona T5 e G16, que medem exactamente isso.

**Decisão.** Compensar com dois mecanismos e declarar o resto: a coluna *Força*, que impede que uma regra nova se traduza automaticamente em bloqueio, e a partição de P7.2 em automática e humana, que impede que o crescimento da listagem se traduza em horas humanas. O custo remanescente declara-se em T6 e nesta secção 8.

**Alternativa rejeitada.** Manter quatro colunas e absorver o crescimento em silêncio.

**Consequências.** G16 passa a ter um numerador honesto: 41 regras novas, das quais nenhuma tem incidente registado, todas nascendo `postuladas` por P5.9. Isto torna o canon imediatamente não conforme à sua própria P5.4 — e é essa não conformidade que P5.9 existe para gerir por observação, ao longo do prazo declarado, em vez de por argumento.

---

## 6 · Recomendações não executadas

### 6.1 Cortes propostos pela lente de red teaming

| Corte proposto | Estado | Razão de não executar |
|---|---|---|
| `ESTADO` e `REJEICOES` | não executado | D2: a inversão de `FRENTES` resolve os achados que o corte resolvia, e mais dois. Os ficheiros ganham leitor declarado em vez de desaparecerem |
| Detector semântico | não executado | D4: é a única mitigação declarada de T2. Cortá-lo deixaria T2 sem resolução |
| Modo Caracterização e estado `retido` | não executado | D1: P1.14 resolve o deadlock por regra. Cortar o modo é decisão de desenho do autor |
| Modo Mandato como árvore | não executado | D1: `eixos[]` e `pai` tornam-no representável (B3) |
| `ALERTA-ESTADO` | **absorvido** | D3: desaparece como ficheiro, por reformulação e não por corte |
| P3.9 | **absorvida** | D6: reformulada como *aviso de protecção*, com o canal separado de `ALERTA` |
| P3.5 na forma actual | **absorvida** | Reformulada em lista branca mais `hash_conteudo`, em vez de retirada (C14) |
| Contagem de pilares em P6.1 | não executado | Mantida com força `convenção`: obriga sem bloquear |
| P1.7 e P1.10 | não executado | Nenhum achado as declara defeituosas; o corte era por volume, não por defeito |
| P7.2 reduzida à metade automatizável | **parcialmente executado** | Partida em automática e humana, sem eliminar a parte humana. A parte humana encolhe por delegação, não por remoção |

O núcleo de vinte regras identificado pela lente — o que sustenta G1, G6, G7, G8, G11, G14 e G17 — não foi isolado no canon. Se o autor decidir executar os cortes, é essa a lista de partida, e a coluna *Força* mais `canon/regras.json` dão-lhe o inventário para o fazer sem repetir a auditoria.

### 6.2 Divergências entre lentes resolvidas de um lado

| Questão | Lado adoptado | Lado não adoptado | Onde se decidiu |
|---|---|---|---|
| Modos Caracterização e Mandato | corrigir o esquema | cortar os dois modos | D1 |
| `ESTADO` e `REJEICOES` | corrigir e gerar `FRENTES` por inversão | cortar | D2 |
| `ALERTA-ESTADO` | log de corridas mais projecção (v2) | `ALERTA` em acrescento com `fechado_em` (v1) | D3 |
| Detector semântico | dar contrato | cortar | D4 |
| «O problema existe?» | não resolvida por corte nem por argumento: P5.9 submete as 41 regras novas e as 60 originais a confirmação por incidente, e T10 declara o diagnóstico postulado | assumir §1.2 como verdadeiro (três lentes) ou suspender o canon até haver incidentes (lente de enquadramento) | D7, P5.9, T10 |

### 6.3 Achados não implementados

- **UK11 · «O mundo é o repositório».** Toda a detecção assenta em merge, worktree, `toca[]` e JSON. Trabalho que não passa por ficheiro é invisível, e numa frente maioritariamente fora do disco `ALERTA` vazio significa cegueira e não saúde — o sistema não distingue os dois casos. Nenhuma correcção foi introduzida. Qualquer correcção exigiria um canal de declaração de trabalho não-ficheiro, o que é alteração de desenho.
- **UK12 · Âmbito do espaço de nomes.** «Slug: identificador global e único» continua sem âmbito declarado. Com dois projectos na mesma instalação, os slugs colidem ou fragmentam-se, `HALT` pára os dois ou nenhum, e o índice sela slugs alheios. P5.12 liberta o espaço de nomes no encerramento, o que pressupõe a questão resolvida sem a resolver. Custa uma linha hoje e é impossível depois, porque P3.6 proíbe renomear slugs. Fica na secção 7 como parâmetro pendente.
- **§4.2.6 · Decisões de rumo que não passam por merge.** O modo rumo corre em interface de chat e as decisões que produz podem não passar por merge, caso em que G8 nunca se activa para elas. P3.24 e `indice_versao` detectam que o índice está velho; nenhuma regra obriga a decisão de rumo a passar por merge antes de valer. Implementação parcial.

---

## 7 · Parâmetros pendentes do autor

O canon declara estes campos obrigatórios e não lhes fixa valor. Todos residem no `MANDATO`, em `limiares[]{nome, valor, justificacao, revalidar_em}`, salvo indicação em contrário. Por P7.6, um limiar sem justificação ou por revalidar é achado.

| # | Parâmetro | Regra que o consome | Efeito de valor baixo | Efeito de valor alto |
|---|---|---|---|---|
| 1 | `orcamento.chamadas_merge` | P0.10, P3.18 | bloqueia a abertura de frente cedo e com frequência | o tecto não morde e UK4 mantém-se por inteiro |
| 2 | `orcamento.chamadas_fecho` | P0.10, P3.27, P6.2 | fechos bloqueados por orçamento em vez de por divergência | idem |
| 3 | `orcamento.horas_auditoria_mes` | P0.10, P7.2-humana | força a parte humana de P7.2 a encolher; abaixo de quatro horas obriga a delegar mais itens ao watcher | P7.2-humana cresce até ao ponto de UK5: feita duas vezes e abandonada |
| 4 | `prazo_indisponibilidade` | P0.13 | modo degradado disparado por uma ausência ordinária | deriva silenciosa com aparência de ordem (UK3) |
| 5 | limiar de itens `por_processar` no `INBOX` | P3.19 | alerta permanente; a triagem passa a ser o trabalho | G10 não dispara e o `INBOX` cresce mais do que se esvazia |
| 6 | `timeout` do detector semântico | P3.18, P6.2 | passagem semântica em `timeout` em todas as corridas; T2 fica sem mitigação efectiva | o merge espera pelo modelo; a serialização de P3.25 propaga a espera |
| 7 | caducidade de `visto` | P3.10 | reemissão do mesmo item a cada corrida; ruído | `visto` volta a ser supressão de facto, que é C3 por outra via |
| 8 | tecto de `inconclusivo` repetido | P2.11 | escalada por um segundo teste mal desenhado | ciclo de redesenho sem saída |
| 9 | prazo por severidade de achado | P7.5 | achados de baixa severidade bloqueiam a abertura de frente | «dois ciclos» torna-se o único prazo efectivo |
| 10 | período de caducidade do canon | P5.10 | reafirmação como ritual frequente | o governo é operado por inércia antes de caducar (UU6) |
| 11 | prazo de regra `postulada` sem incidente | P5.9 | regras removidas antes de haver oportunidade de as violar | P5.9 nunca dispara e C12 volta por inteiro |
| 12 | período de transição de adopção | P5.11 | detectores bloqueantes antes de o existente estar inventariado | adopção «em espírito», que é o mesmo que não adoptar (UU4) |
| 13 | cadência de reavaliação do caminho | P2.9 | reavaliação como rotina, o que dilui a saída `manter` | o caminho só se reavalia por pressuposto caído, que é C16 residual |
| 14 | cadência do inventário de limpeza | P3.31 | custo humano recorrente sobre resíduo que não incomoda | os 22 resíduos de §4.3 acumulam entre inventários |
| 15 | limites das métricas de fluxo | P7.7 | auditoria extraordinária disparada por ruído | o sinal nunca sai dos limites e UU2 mantém-se |
| 16 | política de retenção no encerramento | P5.12 | arquivo destruído antes de ser consultado | armazenamento sem disposição declarada (ISO 15489) |
| 17 | âmbito do espaço de nomes dos slugs | P3.6, P5.12 | um espaço por projecto: `HALT` e o índice ficam por projecto, e a partilha de canon exige tradução | espaço global: colisão entre projectos, que P3.6 torna irreparável (UK12) |
| 18 | os sete números herdados: página (500 palavras), objectivos (1–5), não-objectivos (piso 2), árvores concorrentes (≥2), factor do crivo (dez), cadência da auditoria (mensal), pilares de saída (3–4) | P0.1–P0.3, P1.9, P1.5, P7.1, P6.1 | — | P7.6 obriga cada um a ter justificação registada e data de revalidação; nenhum deixa de ser arbitrário por antiguidade (UU1) |

---

## 8 · Custo assumido

**Volume.** O corpo de regras passa de 60 para 101 identificadores, mais a partição de P7.2: um crescimento de 68%. O Anexo A passa de 14 para 24 esquemas. As garantias passam de 17 para 22 e as tensões de 5 para 10. §0 cresce 13 entradas e três desambiguações. O documento que declara em §1.2 que «governo que cresce mais depressa que o projecto» é um sintoma a eliminar acaba de crescer sem que o projecto tenha crescido. G16 mede o número de regras e a medição piora no acto da correcção. Os travões declarados — coluna *Força*, P7.2 partida, P5.9 — reduzem o custo operacional do volume, não o volume.

**Bloqueio.** Das 41 regras novas, 31 têm consequência `bloqueia`. A abertura de frente passa a ser cruzada por sete verificações bloqueantes: `desbloqueado` (P0.8), orçamento (P0.10), modo degradado (P0.13), reavaliação pendente (P2.5), colisão de toca (P2.10), `inconclusivo` repetido (P2.11), achado aberto há dois ciclos (P7.5). O fecho de sessão passa a ser cruzado por P3.16, P3.21, P3.22, P3.24, P3.26, P3.27 e P3.28. A probabilidade de um dia de trabalho começar por desbloquear o sistema sobe com cada uma delas.

**Novos pontos únicos de falha.** `PERFIS` e `TRAJECTOS` habilitam os hooks e passam a poder divergir da prosa do canon: um erro num deles desliga ou aperta indevidamente toda a camada de confinamento, e nenhum hook se auto-verifica contra o texto. `canon/regras.json` torna-se o registo de que P4.7, P5.9, P5.10 e P7.3 dependem; sem ele, quatro regras ficam sem detector. O watcher, que não aparecia em detector nenhum, passa a ser o detector declarado de P3.18, P3.19, P4.5, P4.6, P1.15 e P7.2 automática: o processo mais simples do sistema torna-se o mais carregado. T7 declara isto; a mitigação é um item de P7.3, que é auditoria, não mecanismo.

**Falha fechada em cadeia.** P3.25 serializa merges e corridas; P3.24 recusa a escrita quando o índice mudou desde o arranque da sessão; P4.6 converte hook indisponível em `HALT`. Cada uma transforma um atraso numa paragem. Em conjunto, uma corrida de watcher em `timeout` — parâmetro 6 da secção 7 — pode encadear-se em merges em fila, sessões com índice velho a recusar escritas, e `HALT`. É a mesma troca de T4, agora aplicada em três sítios em vez de um. T8 declara-a.

**Custo de verificação dissimilar.** P0.12 exige três veredictos com dissimilaridade declarada — modelos ou fornecedores distintos, ou o humano como terceiro juiz — e P3.27 tira o cold-read da frente e dá-o a um perfil próprio. O ganho é que a concordância deixa de ser medida de consistência disfarçada de correcção (UK10). O custo é operacional e financeiro: mais um fornecedor a configurar, ou o humano no caminho crítico de cada desbloqueio de mandato e de cada fecho. T9 declara-o. O orçamento de P0.10 é o sítio onde esse custo se torna visível antes da facturação.

**Custo de proveniência.** `modelo` e `versao` em `sealed/`, `INBOX/*`, `CASOS` e em todo o output de agente (P3.29) tornam a proveniência reprodutível e aumentam o volume de cada registo. `hash_conteudo` em `sealed/` obriga a calcular e guardar o hash de cada referente e a impedir o seu apagamento (P3.5), o que mantém vivas worktrees que de outro modo se destruiriam — e é exactamente o resíduo que P3.31 tem de inventariar.

---

## 9 · Riscos que permanecem

**O diagnóstico continua postulado.** §1.2 apresenta 11 sintomas como factos etiológicos, sem N, sem caso e sem projecto nomeado, e todo o edifício deriva deles (UK1). Nenhuma correcção resolve isto: nem P5.9, que apenas o torna observável ao longo do prazo declarado, nem T10, que o declara. Se o modo de falha dominante for outro — o humano perde interesse, a prioridade muda, o custo excede o valor — 101 regras tratam uma doença que o doente não tem, e operá-las é a causa de morte. É o risco de maior consequência do sistema e é irredutível por desenho: só se resolve por incidentes registados ao longo de meses.

**O canon nasce não conforme à sua própria P5.4.** As 41 regras novas não têm incidente que as motive, tal como as 60 originais. P5.9 gere a não conformidade em vez de a eliminar, e depende de um prazo que o autor ainda não fixou (parâmetro 11).

**Trabalho fora do disco continua invisível** (UK11, não implementado). `ALERTA` vazio continua a não distinguir saúde de cegueira numa frente que trabalha maioritariamente fora de ficheiros.

**O âmbito dos slugs continua por declarar** (UK12, não implementado). É a decisão mais barata de hoje e a mais cara de adiar, porque P3.6 proíbe renomear.

**A reintrodução por slug novo continua a escapar** (T3). Conteúdo equivalente com slug diferente não é apanhado pelo hook; a detecção continua a ser um item de P7.2 executado por comparação humana.

**A completude das dependências continua sem solução** (T2). D4 dá contrato ao detector semântico; contrato não é completude. O conflito caro continua a ser o que ninguém viu e ninguém declarou.

**Ninguém verifica os verificadores.** P4.7 exige teste negativo por regra mecânica e P7.3 declara achado a matriz incompleta. Nenhuma regra verifica que o teste negativo testa o caso certo, e P7.3 continua a auditar o canon contra si próprio — nunca contra a implementação (UK7, residual).

**A dissimilaridade é declarada, não verificada.** P0.12 obriga a declarar modelos ou fornecedores distintos e a persistir `modelo` e `versao`. Um operador que declare dissimilaridade que não existe passa o teste; a única detecção é a comparação humana dos três veredictos em auditoria.

**A ironia da automação mantém-se** (UU7, parcial). O sistema continua a automatizar o fácil e a concentrar no humano o julgamento residual, intermitente e difícil — e as correcções aumentam a carga humana em pelo menos cinco sítios novos: `APROVACOES` (P3.28), `ESCALADAS` (P3.15, P2.11), `ACHADOS` com dono e prazo (P7.5), procedimento de saída de `HALT` (P3.30) e resolução de `merge_pendente` (P3.20). P0.13 e a partição de P7.2 mitigam a ausência e o volume; nenhuma mitiga a fadiga entre a semana 6 e a 10.

**O volume tensiona a própria tese.** T6 declara-o e P5.9 é o único mecanismo de reversão. Se o autor não fixar o prazo de caducidade da regra `postulada`, o corpo de 101 regras é permanente por omissão — e um governo com 101 regras estáveis que consuma a maior parte do esforço é, por G16, saudável. É a falha que UU2 descreve e que P7.7 só detecta se os limites do parâmetro 15 forem fixados.
