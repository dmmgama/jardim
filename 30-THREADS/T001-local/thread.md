---
created: 2026-09-14
project: Jardim
thread: T001
assunto: Local — descrição do espaço existente
estado: ONGOING
etapa_1: ENTREGUE 2026-09-15
sessoes: 1
---

# T001 — Local

## MANDATO  *(fixo — não alterar)*

Produzir e manter a **descrição factual inequívoca do espaço existente**, de modo a que qualquer plano futuro assente numa base robusta e não contestada.

O problema que esta thread resolve: em V1 a informação sobre o espaço estava espalhada por três documentos, um Notion e um dossier técnico avulso, com divergências entre si (cotas diferentes em fontes diferentes) e contaminada por decisões de projecto. Não havia nenhum sítio onde estivesse escrito, sem opinião, **o que o quintal é**.

**Âmbito**

Tudo o que é facto verificável sobre o espaço, incluindo:

- Geometria: dimensões, cotas, desníveis, orientação, nomenclatura dos limites
- Exposição: sol por estação e por hora, sombras, vento, microclima
- Materiais e estado: pavimento, muros, revestimentos, patologias
- Estruturas: muros de suporte, escadas, canteiros, fachada
- Árvores e vegetação existentes: espécie, porte, posição, estado sanitário
- Infraestrutura: água, electricidade, drenagem, esgoto — o que existe e onde
- Condicionantes: condomínio, acessos, servidões, ruído, privacidade
- Envolvente: o que confina, o que se vê, quem vê

**Fora de âmbito**

- Qualquer decisão de projecto, proposta ou intenção de transformação
- Avaliação do que *deve* ser feito
- Orçamentos, faseamento, equipa

Se, ao trabalhar, surgir ideia de projecto: vai para `INBOX.md` da raiz, não para aqui.

**Entrega esperada**

Documentos factuais em `10-LOCAL/`, via `entregue/`, em duas etapas:

**Etapa 1 — o cenário completo *(prioritária e bloqueante)*.** Um retrato do jardim inteiro, suficiente para que qualquer agente ou pessoa que o leia tenha o mesmo entendimento do espaço sem ter assistido a nenhuma sessão. Cobertura de todo o quintal, mesmo que a profundidade varie. É explicitamente aceitável — e desejável — que diga **o que não se sabe**: um buraco identificado vale mais do que um preenchimento plausível.

> **T002 está bloqueada até esta etapa entregar.** Não há debate possível sobre o que fazer ao espaço enquanto não houver acordo sobre o que o espaço é.

**Etapa 2 — aprofundamento por tema *(ongoing)*.** Depois da etapa 1, a thread passa a alimentar o Local por partes, conforme o projecto pedir profundidade.

Regra de escrita: **facto e fonte**. Cada afirmação diz de onde vem — medição directa, planta, foto, documento, ou observação do David. O que for estimativa ou inferência é marcado como tal. O que for desconhecido fica escrito como desconhecido, não se preenche com plausível.

**Tipo:** `ONGOING` com **primeira entrega fechada e bloqueante**.

---

## MATERIAL DE TRABALHO

| Fonte | Onde | Natureza |
|---|---|---|
| `Planta_e_Espaco_Fisico.md` | `research/` | Documento V1. Tem a melhor geometria disponível, **mas está contaminado** por decisões de projecto e tem divergência de cota por resolver. Matéria-prima, não facto. |
| Fotos do estado real | `20-VISUAL/estado-real/` | Planta anotada, fachada norte, vista das escadas, nocturnas. |
| Notion — Jardim Hub | link no `CLAUDE.md` da raiz | **Fonte por explorar.** Contém dossier técnico da palmeira (risco fitossanitário, *Rhynchophorus*) nunca integrado no repositório. |
| Arqueologia | `90-ARQUEOLOGIA/` | Só leitura. Extrair factos, ignorar decisões. |
| David | conversa | Única fonte para o que não está documentado. Medições, observação, história do espaço. |

---

## PRIORIDADES DE ARRANQUE  *(etapa 1)*

1. **Varrer todas as fontes** — planta V1, fotos, Notion, arqueologia. Recolher tudo o que é afirmação factual sobre o espaço, com a origem de cada uma.
2. **Recuperar o dossier da palmeira do Notion.** É o material técnico mais sério que existe e está fora do repositório. A palmeira é o elemento de maior valor e maior risco do quintal.
3. **Separar facto de decisão.** A planta V1 mistura os dois ("canteiro central: ELIMINAR" não é um facto sobre o espaço). Fica só o que descreve, não o que prescreve.
4. **Resolver contradições, ou registá-las como abertas.** Começando pela cota casa→jardim: 1,60 m vs 1,70 m.
5. **Inventariar os buracos.** O que não se sabe e teria de ser medido, fotografado ou observado. Esta lista é entregável: é ela que diz ao David o que tem de ir ver ao quintal.
6. **Produzir o cenário completo** e entregá-lo.

### Mínimo de cobertura da etapa 1

Nenhum destes pontos pode ficar por abordar — ainda que a resposta seja "desconhecido":

- Geometria e cotas · limites e nomenclatura
- Superfície actual e seu estado
- Muros: os quatro, incluindo o muro de suporte sul
- Fachada norte e escadas
- Canteiros existentes
- Árvores: espécie, porte, posição, estado
- Exposição solar por estação · sombras
- Água, electricidade, drenagem, esgoto — o que existe e onde
- Envolvente: o que confina, quem vê, o que se vê
- Condicionantes: condomínio, acessos, ruído

---

## ESTADO FACE AO MANDATO  *(reescrito a cada sessão)*

**Última sessão:** S1 — 2026-09-15
**Estado:** **Etapa 1 ENTREGUE.** Aguarda absorção pelo Arquitecto.

O cenário completo do jardim está produzido em `Docs-David-Local/DOSSIER-LOCAL.md` (806 linhas, 14
secções, 6 diagramas ASCII, índice de 49 imagens, semáforo por secção) e na versão autónoma
`DOSSIER-LOCAL.html`. Nota de entrega em `entregue/README.md`.

**T002 deixou de estar bloqueada por esta thread.**

### Cobertura face ao mínimo exigido

| Ponto do mandato | Estado |
|---|---|
| Geometria e cotas · limites e nomenclatura | 🟢 |
| Superfície actual e seu estado | 🟢 / 🟡 |
| Muros: os quatro, incluindo o de suporte | 🟢 geometria · 🔴 tipo construtivo e fundação |
| Fachada norte e escadas | 🟢 |
| Canteiros existentes | 🟢 |
| Árvores: espécie, porte, posição, estado | 🟡 — citrinheira por confirmar, copas não medidas |
| Exposição solar por estação · sombras | 🟢 — NREL SPA, validado com 3 fotos datadas |
| Água, electricidade, drenagem, esgoto | 🟡 drenagem · 🔴 destino da descarga · 🔴 electricidade |
| Envolvente: o que confina, quem vê | 🟢 confinação · 🔴 exposição visual |
| Condicionantes: condomínio, acessos, ruído | 🔴 — por instruir |

**Semáforo global:** 🟢 38 · 🟡 26 · 🔴 34.

### O que a sessão estabeleceu

**Três conflitos fechados.** Altura dos muros a **2,50 m** `[observado]` — era o item 1 e a maior fonte
de erro do modelo solar. Corte de arquitectura anotado pelo proprietário (era de *proposta de
ampliação*, usado como levantamento). Drenagem construída **existe e funciona**, estabelecido por
observação de caudal.

**Três erros de facto corrigidos.** «Água estagnada sem escoamento aparente» — retirado, era conclusão
tirada de uma fotografia. Cinco fotografias mal descritas no índice, incluindo `Foto2b`, única fonte
sobre electricidade do acervo. E a hora de entrada do sol em 21 Mar (11:28), que não correspondia a
nenhum plano de fachada plausível — corrigida para 12:40.

**Oito contradições, sete encerradas.** Cinco resolvidas, duas anuladas por não serem contradições.
A única aberta (C5) não afecta o quintal. Destaque: **C3 — azimute do eixo longo — resolvida a favor
de 65°/245° e aplicada**, com as horas de entrada do sol recalculadas por posição solar.

**Etiqueta `[observado]`** criada: sobre comportamento prevalece sobre foto; sobre dimensão cede ao
desenho.

**Auditoria de coerência e acerto da pasta.** `research/AUDITORIA-COERENCIA-T001.md` confrontou os 73
ficheiros contra as regras T1–T17: 15 incoerências, 3 altas. Corrigidas:

| | |
|---|---|
| **A2** — violação de T10 | `entregue/` guardava duas cópias mortas com «água estagnada», o erro retractado nesta sessão. Estavam bit-a-bit idênticas a ficheiros já em `arqueologia/`. **Eliminadas.** |
| **A3** — violação de T9+T10 | `Jardim_Analise_Decisao_Betonilha.md` estava em `entregue/` com fase e âmbito errados. **Movido para `research/`.** |
| **A1** — lacuna, não violação | Produto fora de `entregue/` foi decisão informada do David. **Corrigiu-se o protocolo**, não a arrumação. |

**Protocolo alterado** (`CLAUDE.md` da thread): **T9-bis** (fora do mandato fica marcado em
`research/`) · **T10-bis** (produto pode viver com as suas dependências binárias, desde que a nota o
declare) · **T12** reescrita (`NOTA-<entrega>.md`; `README.md` proibido) · **T18/T19/T19-bis**
(estrutura passa a 6 elementos; varredura total ao arquivar por erro de facto). Registo em §7 do
`CLAUDE.md`.

**A entrega é `entregue/NOTA-etapa-1.md`**, que abre com bloco PRODUTO a apontar para
`Docs-David-Local/`. A porta é o `thread.md`; o corpo é a pasta de fontes.

**Um canónico, um só: `DOSSIER-LOCAL.md`.** O `Planta_e_Espaco_Fisico.md` duplicava-o — mesmos
factos, sincronizados à mão — e saiu de circulação. Verificado antes: valores-chave todos
coincidentes, raciocínio todo presente no dossier, e os valores exclusivos eram arredondamentos e um
número obsoleto.

---

## HANDOFF  *(para a próxima sessão desta thread)*

**Próximo passo:** etapa 2 — aprofundamento por tema. Não arrancar sem saber o que o Arquitecto
decidiu quanto à absorção do dossier.

**À espera de:** resposta do Arquitecto (ver `mensagens.md`). Três pontos: absorver o dossier em
`10-LOCAL/`, avaliar a hipótese de rebaixamento do muro SW, levantar o bloqueio da T002.

**Prioridade da etapa 2** — o que desbloqueia mais, por ordem:

1. **Destino do dreno** (X ≈ 11,7 · Y ≈ 3,5). Corante traçador: < 10 €, uma tarde. Responde à mesma
   pergunta que escavar.
2. **Teste de percolação.** Eliminatório para qualquer vegetação de solo. 0 €, meio-dia + 1 noite.
3. **Processo de obra no Arquivo Municipal.** Gratuito a consultar, até 10 dias para certidão.

**Cuidado com:**

- **Não reabrir conflitos fechados.** Muros a 2,50 m e drenagem funcional estão estabelecidos por
  observação directa do proprietário. Se surgir fonte que os contradiga, é a fonte que cede.
- **Só uma contradição continua aberta** (C5, cotas da planta da fracção) e **não afecta o quintal**.
  Sete das oito foram resolvidas ou anuladas em 2026-09-15 — ver secção 13 do dossier. Não as
  reabrir sem fonte nova.
- **Azimute do eixo longo é 65°/245°**, não 60°/240°. Plano da fachada a **155°**. Aplicado em ambos
  os documentos. `Sol-Planta.jpg` ainda mostra os valores antigos no painel — foi despromovido a
  qualidade **B** e não deve ser usado para orientação.
- **Não deslizar para projecto.** O catálogo vegetal e a viabilidade de relva, em `research/`,
  atravessaram a fronteira do mandato em sessão anterior. Ficam onde estão; não sobem ao Local.
- **`DOSSIER-LOCAL.html` regenera-se do `.md`**, nunca se edita à mão. O HTML antigo foi arquivado
  precisamente por ter divergido.
- **A palmeira inspecciona-se pela coroa**, não pelo tronco, para sinais de *Rhynchophorus*.
- **T19-bis é nova e existe por um erro concreto desta sessão.** Ao arquivar algo por erro de facto,
  varrer a pasta inteira — incluindo `entregue/`. Arquivar uma cópia e deixar outra viva é pior do
  que não ter arquivado nenhuma.
- **Um canónico, um só.** `DOSSIER-LOCAL.md`. Não recriar um segundo documento com os mesmos factos —
  foi assim que nasceram as cotas divergentes do V1 (G1).
- **`Docs-David-Local/` está untracked no git** (~48 MB, com o produto final lá dentro). Fora do
  alcance da thread; assinalado ao Arquitecto.
