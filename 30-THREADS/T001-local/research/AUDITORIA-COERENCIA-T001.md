---
created: 2026-09-15
project: Jardim
thread: T001
tipo: auditoria de coerência
objecto: 30-THREADS/T001-local/ (pasta inteira)
estatuto: diagnóstico e proposta. Não executa nada.
---

# Auditoria de coerência — T001-local

**Âmbito:** a pasta `30-THREADS/T001-local/` inteira, confrontada com `T001-local/CLAUDE.md` (T1–T17) e com `Jardim/CLAUDE.md` (G1–G22).

**O que esta auditoria faz:** inventaria, confronta regra a regra, lista incoerências e propõe um plano de acerto. **Não move, não apaga, não reescreve nada.** A execução é decisão do David; a arrumação fora de `T001-local/` é do Arquitecto.

**Distinção que atravessa todo o documento:**

| | |
|---|---|
| **Violação** | O protocolo dizia uma coisa, fez-se outra, sem autorização. Corrige-se o facto. |
| **Derrogação autorizada** | O protocolo dizia uma coisa, o David mandou outra, a thread obedeceu. Corrige-se o **protocolo**, não o facto. |
| **Lacuna do protocolo** | O protocolo não previu o caso. Acrescenta-se texto. |

---

## 1. Inventário

**73 ficheiros, 5 directórios** (`.`, `Docs-David-Local/`, `Docs-David-Local/arqueologia/`, `Docs-David-Local/Claude outputs/`, `entregue/`, `research/`).

### 1.1 Raiz da thread — 3 ficheiros

| Ficheiro | Bytes | O que é | Previsto pelo protocolo? |
|---|---|---|---|
| `CLAUDE.md` | 3 861 | SOP da thread, T1–T17 | ✔ implícito (é o próprio protocolo) |
| `thread.md` | 9 884 | Mandato · estado · handoff | ✔ §2 |
| `mensagens.md` | 3 494 | Canal ↔ Arquitecto | ✔ §2 |

### 1.2 `entregue/` — 5 ficheiros

| Ficheiro | Bytes | Fase | No sítio? |
|---|---|---|---|
| `.gitkeep` | 0 | infra-estrutura | ✔ |
| `README.md` | 8 742 | **nota de entrega da etapa 1** | ⚠ nome errado — T10.2 exige `NOTA.md` |
| `Planta_e_Espaco_Fisico.md` | 17 409 | **sessão anterior, superado** | ✘ é cópia bit-a-bit do `arqueologia/…BACKUP-20260915.md` |
| `Planta_e_Espaco_Fisico.html` | 5 637 463 | **sessão anterior, superado** | ✘ é cópia bit-a-bit dos dois HTML já arquivados |
| `Jardim_Analise_Decisao_Betonilha.md` | 10 747 | **sessão anterior, matéria de projecto** | ✘ dupla infracção — ver §3.4 |

### 1.3 `research/` — 8 ficheiros

| Ficheiro | Bytes | Natureza | Dentro do mandato? |
|---|---|---|---|
| `.gitkeep` | 0 | infra-estrutura | ✔ |
| `INVENTARIO-DOCS-DAVID-LOCAL.md` | 59 653 | inventário das imagens — insumo directo do dossier | ✔ |
| `Estado_Arte_Caracterizacao_Espaco_Exterior.md` | 20 901 | método de caracterização de espaço exterior | ✔ (é método, não projecto) |
| `Planta_e_Espaco_Fisico.md` | 13 011 | **versão V1**, a matéria-prima que `thread.md` declara | ✔ |
| `Jardim_Software_Modelacao_Solar.md` | 96 848 | escolha de ferramenta de modelação | ⚠ fronteira — ver §3.5 |
| `Jardim_Catalogo_Vegetal.md` | 113 929 | **que espécies plantar** | ✘ **fora do mandato** |
| `Jardim_Relva_Natural_Viabilidade.md` | 129 701 | **instalar relva ou não** | ✘ **fora do mandato** |
| `Jardim_Relva_Natural_Viabilidade_slides.pdf` | 16 804 869 | idem, em slides | ✘ **fora do mandato** |

### 1.4 `Docs-David-Local/` — 49 ficheiros na raiz + 2 subpastas

**Não previsto por nenhuma regra.** Composição:

| Classe | N.º | Exemplos |
|---|---|---|
| **Produto final** | 2 | `DOSSIER-LOCAL.md` (70 KB, 827 linhas) · `DOSSIER-LOCAL.html` (9,66 MB) |
| **Documento canónico de origem** | 1 | `Planta_e_Espaco_Fisico.md` (32 940 B, 512 linhas — a versão viva) |
| **Material bruto do proprietário** | ~30 | `Foto1…Foto5`, `corte predio.jpg`, `Planta Fracao.png`, `JARDIM-PLANTA.jpg`, capturas Google |
| **Produzido por agente** | ~15 | `DIAGRAMA-PLANTA.png`, `DIAGRAMA-SOL.png`, `01-inverno.png/.svg`, `02-verão.png/.svg`, `03-planta-gama-solar.png/.svg`, `SOMBRA-*.png` |
| **Arqueologia** | 7 | `arqueologia/` + `NOTA.md` |
| **Fonte vectorial** | 1 | `Claude outputs/Jardim_Nomenclatura.svg` |

**Confirmação de facto:** o `DOSSIER-LOCAL.md` embebe **11 imagens** por caminho relativo simples (sem barra, sem `../`) e cita **59 nomes de ficheiro em texto** (backticks, tabelas do índice de imagens). O `Planta_e_Espaco_Fisico.md` embebe **14**. Os «~50 caminhos relativos» são, em rigor, **25 embebidos** + 59 citações textuais. A distinção é operacionalmente decisiva — ver §4.A.

---

## 2. Confronto regra a regra

### 2.1 Protocolo local — T1 a T17

| Regra | O que exige | Veredicto | Evidência |
|---|---|---|---|
| **T1** | Não escrever fora da pasta | **VIOLADA — com autorização expressa** | Criou-se `30-THREADS/T003-modelo-solar/` e escreveu-se em `THREADS.md`. Registado no `INBOX.md` como derrogação autorizada pelo David. **Matéria para protocolo, não para censura.** |
| **T2** | Excepções: só `INBOX.md` e `THREAD-MENSAGENS.md` | **CUMPRIDA** nas duas excepções previstas | 16 entradas em `INBOX.md` assinadas `T001`; 1 linha em `THREAD-MENSAGENS.md`. Formato correcto. |
| **T3** | Não escrever em `ESTADO.md`, `REJEICOES.md`, `THREADS.md`, `Jardim.html`, `10-LOCAL/`, `20-PLANO/` | **VIOLADA em `THREADS.md`** (mesma derrogação) · **CUMPRIDA no resto** | `10-LOCAL/` está **vazia** — confirmado. `ESTADO.md` e `REJEICOES.md` intactos. |
| **T4** | Pode ler tudo | **CUMPRIDA** | — |
| **T5** | Mandato fixo | **CUMPRIDA** | O bloco MANDATO de `thread.md` é idêntico ao da criação. |
| **T6** | Estado reescrito, não acumulado | **CUMPRIDA** | Secção única, sem log. |
| **T7** | Actualizar `thread.md` no fim da sessão | **CUMPRIDA** | Estado + handoff presentes, datados 2026-09-15. |
| **T8** | Pedido em `mensagens.md` + linha na raiz + handoff | **CUMPRIDA integralmente** | Os três passos feitos. É o item mais bem executado da thread. |
| **T9** | Não decidir matéria de projecto | **CUMPRIDA no dossier** · **VIOLADA em `research/`** | O dossier regista o rebaixamento do muro SW como hipótese sem avaliação — correcto. Mas `Jardim_Relva_Natural_Viabilidade.md` abre com «**Não instale relva natural neste quintal**» e `Jardim_Analise_Decisao_Betonilha.md` traz «recomendação faseada». São decisões de projecto. |
| **T10** | `entregue/` = produto final + `NOTA.md` | **VIOLADA em ambos os pontos** | O produto final **não está** em `entregue/` (está em `Docs-David-Local/`). A nota chama-se `README.md`, não `NOTA.md`. |
| **T11** | Não declarar fecho | **CUMPRIDA** | `mensagens.md`: «Não proponho fecho». |
| **T12** | ONGOING entrega por partes, cada uma com a sua nota | **CUMPRIDA em espírito, frágil na forma** | A etapa 1 tem nota própria. Mas os três ficheiros da sessão anterior em `entregue/` **não têm nota nenhuma** — foram lá postos sem nota e nunca retirados. |
| **T13** | Português europeu | **CUMPRIDA** | — |
| **T14** | Argumentar contra o David | **CUMPRIDA** | Contestou a leitura da «água estagnada» e o uso do `corte predio.jpg` como levantamento. |
| **T15** | Numerar pressupostos | **PARCIAL** | O dossier usa etiquetas `[desenho]/[foto]/[observado]` e semáforo — sistema equivalente e mais forte. Mas não há numeração P1, P2… como a regra literalmente pede. |
| **T16** | Distinguir facto de interpretação | **CUMPRIDA com excelência** | Semáforo 🟢/🟡/🔴 e etiquetas de proveniência. É o melhor do trabalho. |
| **T17** | Não sugerir engenheiro de estruturas | **CUMPRIDA** | — |

### 2.2 Protocolo da raiz — G9 a G17

| Regra | Veredicto | Evidência |
|---|---|---|
| **G9** — só o Arquitecto cria threads | **VIOLADA — derrogação autorizada e declarada** | T003 criada pela T001. Declarada em `INBOX.md` sob «A ratificar — acto fora de regime», com o texto da autorização. A thread fez o que devia: derrogou, declarou, e pediu ratificação. |
| **G10** — só o Arquitecto fecha | **CUMPRIDA** | — |
| **G11** — mandato em `thread.md` | **CUMPRIDA** | — |
| **G12** — thread não escreve fora, excepto `INBOX.md` e `THREAD-MENSAGENS.md` | **VIOLADA** (mesma derrogação de T003) | — |
| **G13** — `Jardim.html` é do Arquitecto | **CUMPRIDA** (o ficheiro nem existe ainda) | — |
| **G14** — pedido + linha + handoff | **CUMPRIDA** | — |
| **G15** — resposta do Arquitecto | **INAPLICÁVEL** — pendente | `THREAD-MENSAGENS.md` tem `[ ]` por responder desde 2026-09-15. |
| **G16** | **INAPLICÁVEL** | — |
| **G17** — ler `mensagens.md` ao arrancar | **CUMPRIDA** | — |

**Nota sobre G18.** `10-LOCAL/` contém apenas factos. Está **vazia** — a regra é cumprida por omissão, e é exactamente esse vazio que a DECISÃO 1 de `mensagens.md` pede para preencher.

---

## 3. Incoerências

### 3.1 Gravidade ALTA

---

**A1 · O produto final não está em `entregue/`.** — viola **T10.1**

`DOSSIER-LOCAL.md` e `.html`, declarados «documento canónico da entrega» pelo próprio `entregue/README.md`, vivem em `Docs-David-Local/`.

**Mas:** foi instrução expressa do David («mete o dossier na raiz das imagens para não partir ligações», «não mandes nada para fora do Docs-David»). E o `mensagens.md` declarou-o ao Arquitecto: «O dossier vive hoje em `Docs-David-Local/`, junto às imagens que referencia, **por instrução do David**.»

**Classificação: escolha informada do proprietário, declarada pelo canal correcto.** Não é violação a censurar — é **lacuna do protocolo a corrigir** (§5.B1). O protocolo presumiu que o produto final é texto sem dependências binárias. Este não é.

---

**A2 · `entregue/` contém três ficheiros mortos de uma sessão anterior.** — viola **T10.1** e **T12**

| Ficheiro | Estado real |
|---|---|
| `entregue/Planta_e_Espaco_Fisico.md` | MD5 `7d9885a1…` — **idêntico bit-a-bit** a `Docs-David-Local/arqueologia/Planta_e_Espaco_Fisico.BACKUP-20260915.md`. A versão viva (`Docs-David-Local/`, MD5 `dc17290a…`, 512 linhas) tem **178 linhas a mais**. |
| `entregue/Planta_e_Espaco_Fisico.html` | MD5 `537c44d3…` — **idêntico aos dois HTML já arquivados**. Existem portanto **três cópias** do mesmo HTML obsoleto, duas em `arqueologia/` e uma em `entregue/`. |
| `entregue/Jardim_Analise_Decisao_Betonilha.md` | Sem nota, sem menção em `README.md`, sem menção em `thread.md`. |

**Consequência mais grave, e é uma consequência de verdade:** `entregue/Planta_e_Espaco_Fisico.md` e `.html` contêm **2 e 3 ocorrências de «água estagnada»** — o erro de facto que a sessão retractou e que a `arqueologia/NOTA.md` diz, textualmente, ter sido arquivado por ser «uma versão bem apresentada e circulável a afirmar algo falso».

**A NOTA.md arquivou o erro numa pasta e deixou-o intacto noutra.** A operação de arqueologia trabalhou dentro de `Docs-David-Local/` e nunca olhou para `entregue/`. Neste momento, quem abrir `entregue/` — que é exactamente a pasta cujo nome promete «isto é o que vale» — encontra a afirmação falsa em primeiro lugar.

**Classificação: violação pura.** Nenhuma instrução do David cobre isto. É resíduo por omissão.

---

**A3 · Material de projecto atravessou a fronteira do mandato.** — viola **T9** e o bloco «Fora de âmbito» do mandato

O mandato diz, sem margem: *«Fora de âmbito — qualquer decisão de projecto, proposta ou intenção de transformação; avaliação do que deve ser feito.»*

| Ficheiro | Onde | Frase que o denuncia |
|---|---|---|
| `research/Jardim_Relva_Natural_Viabilidade.md` (130 KB) | `research/` | «**Não instale relva natural neste quintal** como solução de cobertura do pavimento.» |
| `research/Jardim_Relva_Natural_Viabilidade_slides.pdf` (16,8 MB) | `research/` | idem, em slides |
| `research/Jardim_Catalogo_Vegetal.md` (114 KB) | `research/` | «que espécies **podem lá viver**» — declara-se «etapa 2 de 3», sendo a 3 a escolha |
| **`entregue/Jardim_Analise_Decisao_Betonilha.md`** | **`entregue/`** | «4 opções e **recomendação faseada**»; «Contém **posição explícita**» |

**O `thread.md` já reconhece dois destes** («o catálogo vegetal e a viabilidade de relva, em `research/`, atravessaram a fronteira do mandato em sessão anterior. Ficam onde estão; não sobem ao Local»). **Reconhecer é correcto e suficiente para `research/`** — T10 e o mandato só governam o que sobe, e `research/` é explicitamente «pode ser caótico».

**O quarto não está reconhecido, e é o grave:** `Jardim_Analise_Decisao_Betonilha.md` está em **`entregue/`**. Material de projecto, com recomendação explícita, na pasta que significa «isto é a entrega do mandato factual». Isto não é deriva contida em `research/` — é deriva **promovida**. Se o Arquitecto absorver `entregue/` sem ler ficheiro a ficheiro, absorve uma recomendação de projecto para dentro do Local.

---

### 3.2 Gravidade MÉDIA

---

**M1 · `entregue/README.md` aponta para fora de si próprio.** — tensão com **T10.2**

A nota de entrega está em `entregue/`; os produtos que descreve estão em `Docs-David-Local/`. Funciona porque os caminhos são escritos como `Docs-David-Local/DOSSIER-LOCAL.md` — relativos à **raiz da thread**, não à pasta onde o ficheiro está. Um leitor que abra `entregue/README.md` e tente seguir o caminho a partir dali não encontra nada.

**Não é ambiguidade do autor** — a nota é explícita: «Tudo vive em `Docs-David-Local/`. Nada foi movido para fora da pasta — a arrumação final é decisão do proprietário.» É **honesta**. É o desenho que está errado, não o texto.

---

**M2 · `README.md` em vez de `NOTA.md`.** — viola **T10.2** literalmente

T10.2: «Escrever `entregue/NOTA.md`». O conteúdo cumpre os quatro requisitos (o que é, como se usa, que decisões pede, o que ficou por fazer) — é excelente. Só o nome é que não bate.

**Consequência real, não formal:** numa thread `ONGOING` sob T12 («entrega-se por partes, **cada uma com a sua nota**»), o nome `README.md` **é singular por natureza**. A segunda entrega não pode chamar-se `README.md` também. O nome escolhido bloqueia a mecânica que T12 exige.

---

**M3 · Três estados declarados divergem do real.**

| Onde | Diz | É |
|---|---|---|
| `THREADS.md` → T001 → Estado | `ONGOING · **etapa 1 em curso**` | **etapa 1 ENTREGUE** desde 2026-09-15 |
| `THREADS.md` → T001 → Sessões | `0` | `1` (o `thread.md` diz `sessoes: 1`) |
| `THREADS.md` → T002 → Estado | `À ESPERA — bloqueada por T001` | A condição de bloqueio caiu; falta o acto do Arquitecto |

**Não é violação da T001 — é o efeito de T3/G12.** A thread **não pode** corrigir `THREADS.md`. Sinalizou pelo canal certo (`THREAD-MENSAGENS.md`, linha `[ ]` de 2026-09-15). **O sistema funcionou; falta o Arquitecto agir.** Registado aqui para que ninguém leia `THREADS.md` e conclua que a etapa 1 está em curso.

---

**M4 · Três ficheiros, três versões do mesmo documento, e uma ainda declara-se canónica.**

| Caminho | Linhas | MD5 | Estatuto |
|---|---|---|---|
| `Docs-David-Local/Planta_e_Espaco_Fisico.md` | 512 | `dc17290a…` | **vivo**, `canon: true`, rev. 2026-09-15 |
| `entregue/Planta_e_Espaco_Fisico.md` | 334 | `7d9885a1…` | superado, com o erro da água |
| `Docs-David-Local/arqueologia/…BACKUP-20260915.md` | 334 | `7d9885a1…` | superado, **declarado** superado |
| `research/Planta_e_Espaco_Fisico.md` | 257 | `ee624d40…` | **versão V1** — matéria-prima legítima |

A quarta linha está certa: `thread.md` declara `research/Planta_e_Espaco_Fisico.md` como material de trabalho, e o front matter dela documenta a migração de 2026-09-14. **Não mexer.**

O problema é que **três ficheiros distintos declaram `canon: true` e `precedencia: 1`** no front matter — o vivo, o de `entregue/` e o de `research/`. Um agente que faça `grep canon: true` encontra três candidatos e não tem como escolher sem abrir os três.

---

**M5 · Uma referência a ficheiro inexistente, no `INBOX.md` da raiz.**

`INBOX.md`, entrada de 2026-09-15 sobre a correcção de premissa da drenagem: «Diagrama: `Docs-David-Local/JARDIM-DRENAGEM-HIPOTESES.jpg`».

**Esse ficheiro não existe.** Foi substituído pelo proprietário por `JARDIM-DRENAGEM-OBSERVADA-ATUAL.jpg` — facto que o próprio dossier documenta na contradição C6 (linha 789). O `INBOX.md` ficou com o nome antigo.

Está fora de `T001-local/`, mas foi a T001 que o escreveu, ao abrigo de T2. **Correcção que cabe à T001.**

---

### 3.3 Gravidade BAIXA

| # | Incoerência | Regra |
|---|---|---|
| **B1** | `thread.md` e `entregue/README.md` dizem «806 linhas»; o ficheiro tem **827**. Discrepância de 21 linhas — o dossier cresceu depois de a nota ser escrita. | — |
| **B2** | `thread.md` diz «índice de 49 imagens»; o índice cataloga 49 ficheiros, mas só **11** estão embebidos no `.md`. A formulação induz em erro quanto ao que se parte se a pasta se mover. | T16 |
| **B3** | `entregue/README.md` §3 diz «**Dois** erros de facto corrigidos» e descreve três (água estagnada, cinco fotos mal descritas, hora de 21 Mar). `thread.md` diz «**Três**». Contradizem-se. | T16 |
| **B4** | `arqueologia/NOTA.md` §1 fecha com «**Total: 6 ficheiros**»; `entregue/README.md` §7 e `thread.md` dizem «**Sete** ficheiros movidos». A pasta tem 7 entradas — 6 movidos + a própria `NOTA.md`. Ambos certos, contagens diferentes, nenhum diz qual. | T16 |
| **B5** | `Docs-David-Local/Claude outputs/` — nome com espaço e em inglês, contendo um único `.svg`. Sobrevivente de estrutura antiga; o `.png` gémeo já foi arquivado. | — |
| **B6** | T15 pede pressupostos numerados `P1, P2…`. A thread usa etiquetas e semáforo — sistema mais forte, mas literalmente não é o que a regra diz. | T15 |
| **B7** | `Docs-David-Local/` inteira está **untracked** no git (49 ficheiros, ~48 MB de binários). Não é violação de nenhuma regra do protocolo, mas o produto final da etapa 1 não está sob controlo de versões. | — |

**Nota sobre falsos positivos verificados.** Os nomes `PXL_20260209_124649846.jpg`, `PXL_20250326_164753287.jpg`, `PXL_20250527_095940977.jpg`, `PXL_20260205_135134704.jpg`, `PXL_20260911_110010464.jpg` e `737257ed-3200-4a7d-b775-255125316de3.jpg` aparecem no dossier §11.6 e **não existem na pasta** — mas são **dados EXIF**, nomes de originais do Google Fotos citados como prova de datação. **Não são ligações partidas.** Verificado um a um.

**Também verificado:** zero imagens órfãs em `Docs-David-Local/` — todas as 49 estão citadas no dossier ou no canónico. O índice de imagens está **completo e correcto**.

---

### 3.4 O caso `Jardim_Analise_Decisao_Betonilha.md` — dupla infracção

Merece linha própria porque falha em dois eixos independentes:

1. **Fase errada** — é produto de uma sessão anterior à etapa 1, nunca absorvido, sem nota (T10.2, T12).
2. **Âmbito errado** — é análise de decisão com recomendação, matéria expressamente fora do mandato (T9).

Qualquer dos dois bastaria para o tirar de `entregue/`. Os dois juntos fazem dele o item mais urgente do plano.

---

### 3.5 O caso `Jardim_Software_Modelacao_Solar.md` — fronteira, não deriva

**Não o classifico como deriva.** É escolha de **método de trabalho** — que ferramenta usar para caracterizar a exposição solar — e T9 autoriza explicitamente: *«Podes decidir o método de trabalho dentro do teu mandato.»* Que tenha produzido matéria para `REJEICOES.md` (via Google 3D fechada) não o transforma em projecto: rejeitar uma ferramenta não é decidir o que fazer ao quintal.

**Fica onde está. Não mexer.** Registado aqui só para que a próxima auditoria não o confunda com os outros três.

---

## 4. PLANO DE ACERTO

### A. Onde deve viver o quê

#### A.0 O facto técnico que decide tudo

Antes das opções, o número que as separa:

| Documento | Imagens **embebidas** (`![](…)`) | Nomes **citados em texto** |
|---|---|---|
| `DOSSIER-LOCAL.md` | **11** | 59 |
| `Planta_e_Espaco_Fisico.md` | **14** | — |
| **Total** | **25** | ~59 |

**Todos os 25 caminhos embebidos são nomes simples** — sem `/`, sem `../`. Verificado por `grep`: zero caminhos com barra.

**Consequência:** um caminho simples resolve na pasta onde o `.md` estiver. Logo — **enquanto o `.md` e as imagens se moverem juntos, nada parte.** As opções que separam `.md` de imagens partem 25 ligações; as que os mantêm juntos partem zero.

**Segundo facto:** `DOSSIER-LOCAL.html` (9,66 MB) tem as imagens **em base64**. É imune a qualquer movimento. Move-se sozinho, sem consequência.

**Terceiro facto:** as 59 citações textuais são **prosa** («ver `Foto2b.jpg`»), não ligações. Não partem — mas passam a mentir se o ficheiro citado deixar de estar onde o leitor espera.

#### A.1 As opções

---

**(i) `Docs-David-Local/` inteira passa a `entregue/Docs-David-Local/`**

| | |
|---|---|
| **Ganha** | T10.1 cumprida na letra: o produto final está em `entregue/`. Um comando, uma operação atómica. |
| **Parte** | **Nada.** O `.md` e as imagens viajam juntos; os 25 caminhos simples continuam a resolver. |
| **Reescrever** | `entregue/README.md` (3 caminhos), `thread.md` (5 menções), `mensagens.md` (2), `arqueologia/NOTA.md` (§4, diagrama da árvore). |
| **Contra** | Enterra 30 fotografias em bruto do proprietário dentro de `entregue/`. `entregue/` deixa de significar «o que vale» e passa a significar «tudo». **É precisamente o que T10 tenta evitar.** |
| **E o pior** | Contraria a instrução do David: «não mandes nada para fora do Docs-David». Mover a pasta inteira **é** mandar o Docs-David para fora de onde está. |

---

**(ii) Só os produtos finais passam; as imagens ficam**

| | |
|---|---|
| **Ganha** | `entregue/` fica limpo: dois ficheiros e uma nota. Semântica pura. |
| **Parte** | **11 ligações no `DOSSIER-LOCAL.md`** — todas as imagens do Anexo e dos diagramas. O `.html` sobrevive (base64). Se também se mover o `Planta_e_Espaco_Fisico.md`, **mais 14**. |
| **Reescrever** | Os 25 caminhos passam a `../Docs-David-Local/…`. Mais as mesmas referências da opção (i). **E `../` é frágil:** qualquer movimento futuro parte-o outra vez. |
| **Veredicto** | **Recomendo contra.** Troca uma incoerência de arrumação por 25 ligações frágeis. O David já a rejeitou de facto, e tinha razão. |

---

**(iii) `Docs-David-Local/` é renomeada e assume-se como a entrega**

Ex.: `Docs-David-Local/` → `entrega-etapa-1/` ou `local/`, com `entregue/` esvaziado ou apontando para ela.

| | |
|---|---|
| **Ganha** | Nome honesto. «Docs-David-Local» descrevia o que a pasta **era** (docs que o David deu); há muito que não descreve o que **é** (a entrega). |
| **Parte** | **Nada** internamente. Mas parte **externamente**: 16 entradas do `INBOX.md` da raiz citam `Docs-David-Local/…`, e a T001 **não pode reescrever** entradas alheias em `INBOX.md` sem pedir (T2 dá permissão para escrever, não para reescrever história). |
| **Reescrever** | Tudo o de (i) + as menções em `INBOX.md` + `THREAD-MENSAGENS.md`. |
| **Contra** | Deixa duas pastas de entrega (`entregue/` vazia e a renomeada), ou obriga a apagar `entregue/` — que está **no `.gitkeep` desde a criação** e é elemento do protocolo. Renomear uma pasta com 49 ficheiros untracked é também a operação com maior risco de perda silenciosa. |

---

**(iv) — RECOMENDADA — `entregue/` torna-se ponteiro; `Docs-David-Local/` fica onde está e é renomeada só se o David quiser**

Desenho:

```
T001-local/
├── thread.md
├── mensagens.md
├── CLAUDE.md
├── Docs-David-Local/          ← INTACTA. Fonte + produto, juntos.
│   ├── DOSSIER-LOCAL.md       ← produto canónico da etapa 1
│   ├── DOSSIER-LOCAL.html
│   ├── Planta_e_Espaco_Fisico.md   ← canónico dimensional
│   ├── [49 imagens]
│   ├── Claude outputs/
│   └── arqueologia/
├── entregue/
│   └── NOTA-etapa-1.md        ← nota + ponteiro explícito. NADA MAIS.
└── research/
    └── [material de trabalho, incl. a deriva declarada]
```

**Movimentos:**

| # | Acção | Porquê |
|---|---|---|
| 1 | `entregue/README.md` → `entregue/NOTA-etapa-1.md` | T10.2 (nome) + T12 (uma nota por entrega, numerável) |
| 2 | Acrescentar à nota um bloco **PRODUTO** no topo, com o caminho canónico e a razão de a entrega não estar fisicamente ali | Resolve M1 sem mover ficheiros |
| 3 | `entregue/Planta_e_Espaco_Fisico.md` → `Docs-David-Local/arqueologia/` ou eliminar | **Duplicado exacto** de ficheiro já arquivado. Contém o erro retractado. |
| 4 | `entregue/Planta_e_Espaco_Fisico.html` → idem | **Terceira** cópia do mesmo HTML obsoleto |
| 5 | `entregue/Jardim_Analise_Decisao_Betonilha.md` → `research/` | T9 + §3.4. Matéria de projecto não fica em `entregue/`. |
| 6 | `INBOX.md`: corrigir `JARDIM-DRENAGEM-HIPOTESES.jpg` → `JARDIM-DRENAGEM-OBSERVADA-ATUAL.jpg` | M5. Ao abrigo de T2. |
| 7 | Corrigir 806→827, «dois/três erros», «6/7 ficheiros», e a formulação «49 imagens» | B1–B4, T16 |

| | |
|---|---|
| **Ganha** | Zero ligações partidas — os 25 caminhos simples nunca se mexem. `entregue/` volta a significar **exactamente** o que T10 quer. A instrução do David é respeitada na letra. `arqueologia/` deixa de ter um erro retractado a viver fora dela. |
| **Parte** | **Nada.** Nenhum ficheiro referenciado por nenhum documento vivo é movido. |
| **Reescrever** | Uma nota + quatro correcções numéricas. Nenhum caminho de imagem. |
| **Custo** | Uma sessão curta. O passo 3/4 exige confirmação do David — são ficheiros, e a política declarada é «nada se apaga». |

**Porque recomendo esta:** é a única que corrige **as três violações reais** (A2, A3, M2) sem tocar em nenhum caminho relativo, e a única que não contraria uma instrução expressa do proprietário. As outras três trocam uma incoerência de arrumação por risco de ligações partidas — e o risco é assimétrico: uma pasta com nome imperfeito é irritante; 25 imagens partidas num documento de 9,66 MB sobre geometria é uma entrega inutilizada.

**Sobre a pergunta directa do David** — «a entrada da thread não é `Docs-David-Local`, é a pasta da thread»: **tem razão, e a opção (iv) é a que o diz por escrito.** A entrada é `thread.md`. A entrega é `entregue/NOTA-etapa-1.md`. `Docs-David-Local/` é o **corpo** da entrega, não a sua porta. O que faltava não era mover ficheiros — era a porta dizer para onde aponta.

**Renomear `Docs-David-Local/`:** defensável, mas **não agora**. Deve ser um passo separado, depois de o Arquitecto decidir a absorção em `10-LOCAL/` — porque se o dossier vai subir, o nome da pasta de origem deixa de importar, e ter-se-á reescrito 16 entradas de `INBOX.md` para nada.

---

### B. Correcções ao protocolo

**Diagnóstico honesto primeiro:** o protocolo está **bem escrito**. T1–T17 são claras e as violações que encontrei são, na maioria, resíduo ou deriva — **não** ambiguidade. Não vou inventar regras para legitimar desarrumação.

**Mas há três lacunas reais**, cada uma delas confirmada por um facto desta sessão.

---

**B1 — `entregue/` não previu produto com dependências binárias.** ★ indispensável

*Facto que a motiva:* o `DOSSIER-LOCAL.md` depende de 11 imagens por caminho relativo. T10 presume que o produto final é auto-contido. Não é. O David, correctamente, recusou mover.

Acrescentar a **§5**, depois de T10:

> **T10-bis.** Quando o produto final depende de ficheiros que não pode carregar consigo — imagens referenciadas por caminho relativo, dados, anexos binários — o produto **PODE** ficar na pasta onde essas dependências vivem, em vez de ser movido para `entregue/`.
>
> Nesse caso, `entregue/NOTA-*.md` **DEVE** abrir com um bloco **PRODUTO** que declare:
> - o caminho exacto do produto, **relativo à raiz da thread**
> - quantos ficheiros o acompanham e de que tipo
> - a razão pela qual não foi movido
>
> **A nota é sempre a porta de entrada da entrega, esteja o produto onde estiver.** O que `entregue/` garante não é a localização física do produto — é que existe **um** sítio onde se diz o que foi entregue e onde está.

---

**B2 — a estrutura de 4 elementos não previu material bruto do proprietário.** ★ indispensável

*Facto que a motiva:* `Docs-David-Local/` existe porque o David entregou ~30 fotografias e plantas. Não são `research/` (não foram produzidas pela thread), não são `entregue/` (não são produto), não cabem em `thread.md`. **A tabela de 4 linhas não tinha linha para elas.**

Substituir a tabela de **§2** por:

| Elemento | Função | Obrigatório |
|---|---|---|
| `thread.md` | Mandato (fixo) · Estado (reescrito) · Handoff | Sim |
| `mensagens.md` | Canal thread ↔ Arquitecto | Sim |
| `research/` | Pesquisas, notas, material produzido pela thread. **Pode ser caótico.** | Sim |
| `entregue/` | **Nota de entrega.** Produto final, quando este for auto-contido (ver T10-bis). | Sim |
| **`fontes/`** | **Material bruto fornecido pelo proprietário ou por terceiros: fotografias, plantas, documentos. Não produzido pela thread.** | Quando existir |
| **`arqueologia/`** | **Material superado pelo trabalho da thread. Só de leitura, nunca fonte válida.** Pode viver dentro de `fontes/`. | Quando existir |

E acrescentar:

> **T18.** Material bruto de terceiros **NÃO PODE** ficar em `research/` nem em `entregue/`. `research/` é o que a thread produziu; `entregue/` é o que a thread entrega. O que veio de fora vive em `fontes/`.
>
> **T19.** Quando a thread supera um ficheiro, **DEVE** movê-lo para `arqueologia/` e registar em `arqueologia/NOTA.md` o que é, porque foi superado, e o que o substitui. **NÃO PODE** apagar.
>
> **T19-bis.** Antes de fechar uma entrega, a thread **DEVE** verificar que nenhuma cópia de material arquivado sobreviveu fora de `arqueologia/` — em particular em `entregue/`.

*T19-bis existe por causa de A2, e só por causa de A2.* O trabalho de arqueologia foi exemplar **dentro** de `Docs-David-Local/` e nunca olhou para `entregue/`. O resultado é que o erro da «água estagnada» está arquivado num sítio e vivo noutro, no sítio com o nome mais promissor. Uma regra de varredura final teria apanhado isto.

---

**B3 — T12 não diz como se nomeia a nota de cada entrega.** ★ indispensável

*Facto que a motiva:* a etapa 1 chamou à sua nota `README.md`. A etapa 2 não pode chamar-se `README.md` também. T12 exige «cada uma com a sua nota» e T10.2 dá um nome singular.

Reescrever **T12**:

> **T12.** Numa thread `ONGOING` não há fecho: entrega-se por partes, cada uma com a sua nota.
>
> Cada entrega tem **a sua própria nota**, nomeada `NOTA-<identificador-da-entrega>.md` — por exemplo `NOTA-etapa-1.md`. **NÃO PODE** haver `README.md` em `entregue/`: o nome é singular e impede a segunda entrega.
>
> Entregas anteriores **NÃO PODEM** ser alteradas nem removidas — ficam como registo do que foi entregue e quando. Se o seu conteúdo for superado, T19 aplica-se: vai para `arqueologia/`, com a nota a dizer o que o substituiu.

---

**B4 — o mandato tem fronteira; o protocolo não tem sanção.** — recomendada, não indispensável

*Facto que a motiva:* três documentos (260 KB + 16,8 MB de slides) atravessaram a fronteira do mandato factual e ninguém os travou. O `thread.md` reconhece-o **depois**.

Acrescentar a **§4**, depois de T9:

> **T9-bis.** Quando o trabalho produzir material **fora do âmbito declarado no mandato**, a thread **DEVE**:
> 1. Mantê-lo em `research/` — nunca em `entregue/`
> 2. Marcá-lo no topo do ficheiro: `> ⚠ FORA DO MANDATO DA T<NNN>. Não sobe à entrega.`
> 3. Sinalizar em `INBOX.md` que existe e a que thread pertenceria
>
> **NÃO PODE** deitar fora o material. A deriva produz frequentemente o trabalho mais valioso — o que não pode é entrar na entrega sem o Arquitecto saber.

*O ponto 2 é o que faltava.* Os três ficheiros derivados não têm marca nenhuma no topo; quem os abrir não sabe que estão fora de âmbito sem ler o `thread.md`.

---

**B5 — T15 não corresponde ao que a thread faz.** — recomendada

A thread substituiu «pressupostos P1, P2…» por etiquetas de proveniência e semáforo — que é **mais forte**, porque classifica cada afirmação e não só as ambíguas. O protocolo devia reconhecê-lo:

> **T15.** **DEVES** numerar os pressupostos (P1, P2, …) quando avançares sob ambiguidade não-bloqueante — **ou** aplicar um sistema equivalente de marcação por afirmação, declarado no documento. O que **NÃO PODE** acontecer é uma afirmação incerta aparecer sem marca.

---

**O que NÃO se deve acrescentar ao protocolo**

| Tentação | Porque não |
|---|---|
| Regra que permita produto final fora de `entregue/` sem nota | Seria legitimar A1 sem o corrigir. T10-bis exige a nota — é essa a diferença entre ordenar e desistir. |
| Regra que permita à thread corrigir `THREADS.md` | T3/G12 estão certas. M3 resolve-se com o Arquitecto a fazer o seu trabalho, não a abrir a porta. |
| Regra sobre nomenclatura de imagens | Não houve problema nenhum: 49 imagens, 49 catalogadas, zero órfãs. Não legislar sobre o que funciona. |
| Regra que proíba material fora do mandato | Proibir não trava; T9-bis **canaliza**, que é o que funciona. |

---

### C. Sequência de execução

**Convenção:** cada passo diz o que faz, o que pode partir, e como se verifica. Os passos 1–4 são independentes entre si. Os 5–7 dependem do 1.

---

**Passo 0 — Rede de segurança** · *sem dependências*

Commit do estado actual, incluindo os 49 ficheiros untracked de `Docs-David-Local/`.

- **Pode partir:** nada. É a operação que garante que os passos seguintes são reversíveis.
- **Verificação:** `git status --porcelain 30-THREADS/T001-local/` devolve vazio.
- **Nota:** ~48 MB de binários. Se o David preferir não os versionar, fazer cópia da pasta para fora do repositório antes do passo 3. **Não avançar sem uma das duas.**

---

**Passo 1 — `entregue/README.md` → `entregue/NOTA-etapa-1.md`** · *depende de 0*

- **Pode partir:** nada aponta para `entregue/README.md` — verificado por `grep` em `thread.md`, `mensagens.md` e no dossier. Zero ocorrências.
- **Verificação:** `grep -rn "entregue/README" 30-THREADS/T001-local/ ../../INBOX.md ../../THREAD-MENSAGENS.md` → vazio.

---

**Passo 2 — Bloco PRODUTO no topo da nota** · *depende de 1*

Inserir antes da secção 1:

```markdown
## PRODUTO — onde está

| | |
|---|---|
| **Canónico** | `Docs-David-Local/DOSSIER-LOCAL.md` — caminho relativo à raiz da thread |
| **Circulável** | `Docs-David-Local/DOSSIER-LOCAL.html` — autónomo, imagens embebidas |
| **Base dimensional** | `Docs-David-Local/Planta_e_Espaco_Fisico.md` |

**Porque não está nesta pasta.** O dossier embebe 11 imagens e o documento dimensional
embebe 14, todas por caminho relativo simples. Movê-los para `entregue/` partiria 25
ligações. Por instrução expressa do proprietário, produto e imagens ficam juntos.
Esta nota é a porta de entrada da entrega; `Docs-David-Local/` é o seu corpo.
```

- **Pode partir:** nada.
- **Verificação:** abrir a nota e seguir os três caminhos a partir da **raiz da thread**.

---

**Passo 3 — Esvaziar `entregue/` do resíduo** · *depende de 0 · **exige decisão do David***

| Ficheiro | Destino proposto | Fundamento |
|---|---|---|
| `Planta_e_Espaco_Fisico.md` | `Docs-David-Local/arqueologia/` ou eliminar | Duplicado exacto (MD5 `7d9885a1…`) de ficheiro já lá arquivado |
| `Planta_e_Espaco_Fisico.html` | idem | Terceira cópia idêntica (MD5 `537c44d3…`) |
| `Jardim_Analise_Decisao_Betonilha.md` | `research/` | T9 + §3.4 — matéria de projecto |

- **Decisão pedida:** arquivar cria uma quarta e quinta cópia do mesmo conteúdo; eliminar contraria «nada se apaga». **Recomendo eliminar os dois `Planta_e_Espaco_Fisico.*`** — a arqueologia já tem o `.md` bit-a-bit idêntico e dois HTML idênticos. Preservar uma sexta cópia do mesmo erro retractado não preserva informação nenhuma. **Mas é decisão do proprietário, não minha.**
- **Pode partir:** nada aponta para estes três ficheiros. Verificado.
- **Verificação:** `grep -rn "entregue/Planta\|Betonilha" 30-THREADS/T001-local/` → só a `arqueologia/NOTA.md` e esta auditoria.
- **Verificação final e mais importante:** `grep -rl "estagnad" 30-THREADS/T001-local/ --include=*.md --include=*.html` deve devolver **apenas** ficheiros dentro de `arqueologia/`, a própria `NOTA.md` que explica a retractação, e o `DOSSIER-LOCAL.md` (onde as 4 ocorrências são o **registo da correcção**, não a afirmação). Se devolver algo em `entregue/`, o passo falhou.

---

**Passo 4 — Corrigir `INBOX.md` (M5)** · *sem dependências*

`JARDIM-DRENAGEM-HIPOTESES.jpg` → `JARDIM-DRENAGEM-OBSERVADA-ATUAL.jpg`, com nota entre parênteses de que o ficheiro foi substituído pelo proprietário (contradição C6).

- **Pode partir:** é uma entrada assinada `T001`, dentro da permissão de T2. **Não tocar em entradas assinadas `arquitecto`.**
- **Verificação:** o nome citado existe em `Docs-David-Local/`.

---

**Passo 5 — Corrigir os números** · *depende de 1, 2* · *B1–B4*

| Onde | De | Para |
|---|---|---|
| `thread.md`, `NOTA-etapa-1.md`, `mensagens.md` | «806 linhas» | «827 linhas» |
| `NOTA-etapa-1.md` §3 | «Dois erros de facto» | «Três erros de facto» |
| `thread.md`, `NOTA-etapa-1.md` | «índice de 49 imagens» | «índice de 49 imagens, das quais 11 embebidas» |
| `NOTA-etapa-1.md` §7, `thread.md` | «Sete ficheiros movidos» | «Seis ficheiros movidos + `NOTA.md`» |

- **Verificação:** `wc -l Docs-David-Local/DOSSIER-LOCAL.md` = 827; contagem de `![` = 11.

---

**Passo 6 — Reescrever `T001-local/CLAUDE.md`** · *depende de 1–5 · **exige aprovação do David***

Aplicar B1 a B5. Só depois da realidade arrumada: um protocolo escrito para legitimar desarrumação legitima a desarrumação.

- **Pode partir:** o próprio protocolo. **Nunca alterar §3 (mandato) — T5.**
- **Verificação:** reler o inventário de §1 contra a nova tabela de §2. Todo o ficheiro deve ter uma linha onde caber. Se algum não couber, a tabela ainda está incompleta.

---

**Passo 7 — Registar em `mensagens.md`** · *depende de 6*

Novo pedido ao Arquitecto, com linha em `THREAD-MENSAGENS.md` (T8, três passos):

1. A estrutura da T001 foi acertada; o produto continua em `Docs-David-Local/`, com ponteiro em `entregue/NOTA-etapa-1.md`
2. **Proposta de alterar o `CLAUDE.md` da T001** — T10-bis, T18, T19, T19-bis, T12 reescrita, T9-bis, T15. Se as regras da thread forem matéria do Arquitecto, é ele que aprova
3. **Recordar que `THREADS.md` está desactualizado** (M3): estado, contagem de sessões, e o bloqueio da T002

- **Verificação:** os três passos de T8 executados — pedido, linha, handoff.

---

**O que NÃO fazer**

| | Porquê |
|---|---|
| Mover `Docs-David-Local/` para `entregue/` | Opção (i) — enterra 30 fotos em bruto na pasta de entrega |
| Mover só o dossier para `entregue/` | Opção (ii) — parte 25 ligações, troca-as por `../` frágeis |
| Renomear `Docs-David-Local/` **agora** | Opção (iii) — obriga a reescrever 16 entradas do `INBOX.md` que podem ficar irrelevantes se o Arquitecto absorver em `10-LOCAL/` |
| Corrigir `THREADS.md` | **T3 proíbe.** Já foi sinalizado pelo canal correcto. |
| Escrever em `10-LOCAL/` | **T3 proíbe.** É a DECISÃO 1 pendente. |

---

## 5. O que NÃO deve mudar

Igualmente importante. **Não mexer em nada desta lista.**

| Elemento | Porquê |
|---|---|
| **`Docs-David-Local/` — composição interna** | 49 imagens, 49 catalogadas, **zero órfãs**, zero ligações partidas. Arrumação correcta, verificada. |
| **Os 25 caminhos relativos simples** | Nomes sem barra são a forma mais robusta que existe: resolvem sempre na pasta do `.md`. **Não converter para `../`.** |
| **`Docs-David-Local/arqueologia/` e a sua `NOTA.md`** | Modelo do que T19 devia exigir: MD5, inspecção visual, `grep` de referências antes de mover, e uma secção §3 a dizer o que **não** se moveu e porquê. **Serve de base ao texto de T19.** |
| **`Claude outputs/Jardim_Nomenclatura.svg`** | Fonte vectorial do diagrama normativo. Não é duplicado. A `NOTA.md` já justificou. |
| **`research/Planta_e_Espaco_Fisico.md` (257 linhas)** | **É a versão V1**, matéria-prima declarada em `thread.md`. Não é duplicado nem resíduo. **Não confundir com as outras três.** |
| **`research/Jardim_Catalogo_Vegetal.md` e `Jardim_Relva_Natural_Viabilidade.*`** | Fora do mandato, **mas em `research/`, que é o sítio certo para a deriva**. O `thread.md` já as declarou. Recebem marca no topo (T9-bis); **ficam onde estão**. |
| **`research/Jardim_Software_Modelacao_Solar.md`** | **Não é deriva** — é método de trabalho, autorizado por T9. Ver §3.5. |
| **`research/INVENTARIO-DOCS-DAVID-LOCAL.md`** | Insumo directo do dossier, e o rasto que explica como cada imagem foi classificada. |
| **`research/Estado_Arte_Caracterizacao_Espaco_Exterior.md`** | Método, não projecto. Dentro do mandato. |
| **O bloco MANDATO de `thread.md`** | **T5: fixo.** Nenhum passo deste plano lhe toca. |
| **Semáforo 🟢/🟡/🔴 e etiquetas de proveniência** | O melhor do trabalho, e cumpre T16 melhor do que T15 pede. **Não substituir por P1, P2…** — alterar T15 em vez disso (B5). |
| **A mecânica de T8** | Executada na íntegra: pedido, linha, handoff. Zero correcções. |
| **`entregue/.gitkeep` e `research/.gitkeep`** | Mantêm as pastas do protocolo vivas em git mesmo quando vazias. |
| **`DOSSIER-LOCAL.html`** | Imagens em base64: imune a qualquer movimento. Regenera-se do `.md`, **nunca se edita à mão** — como o `thread.md` avisa, e como o HTML arquivado prova. |

---

## 6. Resumo

| | |
|---|---|
| **Ficheiros auditados** | 73, em 5 directórios |
| **Regras confrontadas** | 17 locais (T1–T17) + 9 da raiz (G9–G17) |
| **Cumpridas** | 13 de 17 locais · 6 de 9 da raiz |
| **Violadas** | **T10** (produto fora de `entregue/`, nota mal nomeada) · **T9** (projecto em `entregue/`) · **T1/T3/G9/G12** (T003 — **derrogação autorizada e declarada**) · **T12** (frágil) |
| **Incoerências** | **3 ALTAS** · **5 MÉDIAS** · **7 BAIXAS** |
| **Falsos positivos descartados** | 6 nomes `PXL_*`/UUID que são EXIF, não ligações |
| **Ligações de imagem partidas** | **Zero** |
| **Imagens órfãs** | **Zero** |
| **Referências partidas encontradas** | 1 — no `INBOX.md` da raiz (M5) |
| **Opção recomendada** | **(iv)** — `Docs-David-Local/` fica; `entregue/` torna-se nota + ponteiro |
| **Alterações indispensáveis ao protocolo** | **B1** (T10-bis) · **B2** (`fontes/`, `arqueologia/`, T18/T19/T19-bis) · **B3** (T12 reescrita) |

**A conclusão em duas frases.** O protocolo está bem escrito e a realidade desviou-se dele em três pontos — mas **dois dos três desvios são a realidade a ter razão contra o protocolo**, não o contrário: um produto com 25 imagens não cabe em `entregue/` sem se partir, e material bruto do proprietário não tem lugar em nenhum dos quatro elementos previstos. O terceiro desvio — resíduo morto em `entregue/`, com um erro de facto já retractado a viver na pasta com o nome mais promissor — **é violação pura, e é o que urge corrigir.**
