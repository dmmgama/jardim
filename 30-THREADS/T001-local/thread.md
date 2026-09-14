---
created: 2026-09-14
project: Jardim
thread: T001
assunto: Local — descrição do espaço existente
estado: ONGOING
sessoes: 0
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

**Última sessão:** —
**Estado:** Por arrancar, **etapa 1**. Pasta criada, mandato escrito, matéria-prima em `research/`. `10-LOCAL/` vazia.

**Prioridade máxima do projecto:** T002 (Jardim V2) está bloqueada até esta etapa entregar.

---

## HANDOFF  *(para a próxima sessão desta thread)*

**Próximo passo:** Executar a etapa 1. Varrer as fontes, separar facto de decisão, produzir o cenário completo do jardim e a lista de buracos.

**À espera de:** nada. O David é fonte para o que não está documentado — perguntar durante a sessão.

**Cuidado com:**

- **Não copiar a planta V1 para `10-LOCAL/`.** Mistura medição com decisão. "Canteiro central: ELIMINAR" não é um facto sobre o espaço.
- **Não preencher lacunas com o plausível.** Um "desconhecido" escrito vale mais do que um número inventado — foi assim que nasceram as duas cotas em conflito.
- **Não deslizar para projecto.** Ideia de transformação vai para `INBOX.md` da raiz, não para aqui.
- **Não confundir profundidade com cobertura.** A etapa 1 precisa de cobrir o jardim todo; aprofundar é a etapa 2.
