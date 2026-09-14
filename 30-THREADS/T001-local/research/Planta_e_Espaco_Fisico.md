---
created: 2026-09-14 20:10
project: Jardim
chat: Migração KB para repo local
summary: >
  Documento-mestre do espaço físico do quintal de Alcântara: geometria, cotas,
  nomenclatura oficial dos muros, árvores e zona hot tub. Prevalece sobre qualquer outro doc.
canon: true
precedencia: 1
---

# Planta e Espaço Físico do Quintal — Documento-Mestre

Este documento é a **referência dimensional e espacial definitiva** do projecto Jardim Alcântara. Em caso de conflito com qualquer outro documento do KB, **este prevalece**.

Deve ser lido em conjunto com os ficheiros de imagem indicados abaixo. Toda a nomenclatura aqui definida (nomes de muros, zonas, eixos) é a nomenclatura oficial do projecto — usar sempre estes termos.

> **Nota de migração (2026-09-14):** os ficheiros de imagem citados abaixo pelo nome simples estão agora em `20-VISUAL/`. Ver mapa de caminhos no `CLAUDE.md` da raiz.

---

## FICHEIROS DE IMAGEM ASSOCIADOS

| Ficheiro no KB | O que mostra | Ponto de vista | Estado representado |
|----------------|-------------|----------------|---------------------|
| `PLANTAREALJARDIM.jpg` | Planta anotada do quintal com cotas, nomes de muros, posição das árvores, canteiros, betonilha e zona hot tub (rectângulo vermelho) | Vista aérea (planta). Norte à esquerda | **Estado actual real** — betonilha cinzenta, canteiros laterais (terra castanha), canteiro central com deck de madeira, árvores nas posições reais |
| `FachadaNortemockup.jpg` | Fachada do prédio (norte), escadas, cotas de altura. Relva é mockup (não existe) | Observador no jardim, a olhar para norte (para a casa) | Mockup — relva não existe, cotas da fachada são reais |
| `FachadaNortereal.jpg` | Mesma vista que o mockup mas com estado real: betonilha degradada, paletes, banco | Observador no jardim, a olhar para norte (para a casa) | **Estado actual real** |
| `VistaJardimNS.jpg` | Vista do jardim com canteiros, posição das árvores, escadas. Relva é mockup sobre betonilha | Observador no topo das escadas (canto NE), a olhar para sul/baixo | Mockup parcial — relva não existe, mas canteiros e posição das árvores são reais |

**Instrução para o LLM:** ao responder sobre o espaço, cruzar sempre a descrição textual abaixo com estas quatro imagens. A `PLANTAREALJARDIM.jpg` é a referência-mestre para geometria e cotas. A `FachadaNortereal.jpg` mostra o estado real da zona norte. A `FachadaNortemockup.jpg` tem as cotas de altura da fachada e escadas. A `VistaJardimNS.jpg` dá a percepção real do espaço e posição das árvores vista das escadas.

---

## CONVENÇÕES E NOMENCLATURA

### Eixos

- **Eixo N→S (comprimento):** 13.00m. Da fachada do prédio (norte) ao muro de fundo (sul). Na planta, da **esquerda para a direita**.
- **Eixo W→E (largura):** 5.78m interior / 6.13m exterior. Na planta, de **baixo para cima**.

### Orientação na planta (`PLANTAREALJARDIM.jpg`)

| Direcção | Posição na planta | Elemento |
|----------|-------------------|----------|
| Norte | Esquerda | Fachada do prédio |
| Sul | Direita | Muro de fundo (muro de suporte) |
| Oeste | Baixo | Muro lateral |
| Este | Cima | Muro lateral |

**Sol:** orientação sudoeste. A fachada norte recebe sol directo durante a tarde.

### Nomes dos muros (usar sempre estes nomes — NUNCA "esquerdo/direito/fundo")

| Nome oficial | Posição | Descrição |
|-------------|---------|-----------|
| **Fachada norte** | Norte (esquerda na planta) | Fachada traseira do prédio. Parede do edifício com porta, janelas e varanda do 1º andar acima. Escadas descem daqui para o jardim. Visível em `FachadaNortereal.jpg` e `FachadaNortemockup.jpg` |
| **Muro sul** | Sul (direita na planta) | Muro de fundo. Muro de suporte de ~95 anos. ~3m de altura pelo lado do jardim. **8m de desnível no tardoz**. Elemento estrutural crítico. Visível ao fundo em `VistaJardimNS.jpg` (muro branco) |
| **Muro este** | Este (topo da planta) | Muro lateral. ~3m de altura. Escadas de acesso encostadas a este muro. Visível à esquerda do observador em `VistaJardimNS.jpg` |
| **Muro oeste** | Oeste (base da planta) | Muro lateral. ~3m de altura. Visível à direita do observador em `VistaJardimNS.jpg`, e à esquerda em `FachadaNortereal.jpg` |

Todos os muros são **brancos** (rebocados/caiados). Devem permanecer brancos — a arte UV do AKone é invisível de dia.

---

## GEOMETRIA DO QUINTAL

### Espaço único

O quintal é um **rectângulo único**, todo à **mesma cota** — 1.60m abaixo do nível da casa. Não existe pátio separado nem plataformas intermédias. Acede-se por uma escada que vence o desnível.

### Dimensões gerais

- **Comprimento (N→S):** 13.00m
- **Largura (W→E):** 5.78m interior / 6.13m exterior
- **Área útil interior:** ~75m²
- **Desnível casa → jardim:** 1.60m (~5 degraus)
- **Desnível muro sul (tardoz):** 8.00m

### Escadas de acesso

- **Posição:** saem da fachada norte, **encostadas ao muro este**
- **Degraus:** ~5
- **Largura:** 1.50m (cota em `FachadaNortemockup.jpg`)
- **Altura:** 1.25m (cota em `FachadaNortemockup.jpg`)
- **Desenvolvimento (N→S):** ~2.43m
- **Chegada:** canto **nordeste** (NE) do jardim

Quem está no topo das escadas olha para **sul e para baixo**. O muro este fica à **esquerda**, o muro oeste à **direita**. Esta perspectiva é o que se vê em `VistaJardimNS.jpg`.

---

## ZONA HOT TUB

### Definição

Não é um espaço separado. É uma **sub-zona dentro do quintal**, no canto **noroeste** (NW), à mesma cota. Assinalada com **rectângulo vermelho** na `PLANTAREALJARDIM.jpg`.

### Limites

| Limite | Elemento |
|--------|----------|
| Norte | Fachada do prédio |
| Este | Lateral das escadas (encostadas ao muro este) |
| Oeste | Muro oeste |
| Sul | **Aberto** — dissolve-se no jardim a ~2.43m da fachada |

### Dimensões

- **N→S:** 2.43m (profundidade, da fachada até onde acabam as escadas)
- **W→E:** 4.29m (largura, do muro oeste até à lateral das escadas)
- **Área:** ~10.4m²

### Carácter

Vista do topo das escadas, parece um **"poço" enclausurado** — limitada em três lados, aberta apenas a sul. Privacidade e identidade visual própria. Visível em `FachadaNortereal.jpg`.

### Cotas da fachada norte (`FachadaNortemockup.jpg`)

- Largura zona hot tub: **4.30m** | Altura fachada até janelas: **2.00m** | Altura escadas: **1.25m** | Largura escadas: **1.50m**

### Conteúdo actual

- Hot tub Intex (~1.92m × 1.88m)
- Árvore decídua no canto NW
- Paletes com almofadas, banco (provisório)
- Betonilha degradada

---

## SUPERFÍCIE ACTUAL

**Betonilha/betão em todo o quintal.** Visível em `PLANTAREALJARDIM.jpg` (cinzento) e `FachadaNortereal.jpg` (fissurada). A relva em `FachadaNortemockup.jpg` e `VistaJardimNS.jpg` é **mockup**. Será demolida na Fase 1.

---

## CANTEIROS EXISTENTES (todos a demolir)

Visíveis na `PLANTAREALJARDIM.jpg` (faixas castanhas) e `VistaJardimNS.jpg`.

- **Canteiro central:** elevado ~40–50cm, murete betão + deck de madeira no topo. A ~2.56m da fachada. ~1.45m largura (W→E)
- **Canteiro lateral este:** faixa de terra ao longo do muro este
- **Canteiro lateral oeste:** faixa de terra ao longo do muro oeste
- **Canteiro lateral sul:** faixa de terra ao longo do muro sul

---

## ÁRVORES — POSIÇÕES ACTUAIS REAIS

### Palmeira das Canárias (Phoenix canariensis) — PROTAGONISTA

- **Posição N→S:** a **2.54m do muro sul** (tronco). Ou seja, a ~10.46m da fachada norte
- **Posição W→E:** deslocada para **este**, a ~35% da largura desde o muro este (~2.0m do muro este, ~3.8m do muro oeste)
- **Características:** tronco baixo e grosso, copa aberta com folhas grandes
- **Na planta:** copa verde grande, lado direito, anotada "PALMEIRA"
- **Em `VistaJardimNS.jpg`:** ao fundo à esquerda (lado do muro este), copa alta dominante
- **Decisão:** MANTER — protagonista absoluta do projecto

### Laranjeira — A TRANSPLANTAR

- **Posição actual:** plantada no solo, **entre o canteiro central e a palmeira**, aproximadamente ao centro da largura
- **Na planta:** anotada "LARANJEIRA", entre o canteiro central (à esquerda/norte) e a palmeira (à direita/sul). Árvore pequena com frutos laranja visíveis
- **Em `VistaJardimNS.jpg`:** árvore pequena/média com tronco fino, visível junto à palmeira
- **Decisão:** TRANSPLANTAR para vaso de barro ≥60cm. Posição futura: possivelmente junto ao **muro este**, mas pode mudar-se decisão consoante épocas do ano (por exemplo inverno no lado das arvores de folha caduca e no verão no muro este, para equilibrar)

### Lodão bastardo (Celtis australis)

- **Posição:** encostado ao **muro oeste**, a cerca de **4m do muro sul** (ou seja, a ~9m da fachada norte)
- **Na planta:** copa grande escura na zona sul, junto ao muro oeste (base da planta). Parte da copa sai para fora do rectângulo do quintal
- **Em `VistaJardimNS.jpg`:** copa grande escura ao fundo à direita (lado do muro oeste). Raízes expostas visíveis
- **Cotas na base da planta:** 10.03m (fachada → lodão) + 2.87m (lodão → muro sul) = ~12.90m
- **Características:** árvore grande, copa significativa no verão (sombra funcional), decídua (ramos nus no inverno)
- **Decisão:** MANTER

### Árvore decídua (junto à fachada)

- **Posição:** canto **NW**, dentro da zona hot tub. Junto à fachada e ao muro oeste
- **Em `FachadaNortereal.jpg` e `FachadaNortemockup.jpg`:** à esquerda da imagem, ramos projectando sombra na fachada branca
- **Características:** árvore grande, copa significativa no verão (sombra funcional), decídua (ramos nus no inverno)
- **Decisão:** MANTER

---

## COTAS DE REFERÊNCIA

### Eixo N→S (junto ao muro este, topo da planta)

Visíveis no topo da `PLANTAREALJARDIM.jpg`:

- **2.56m** — fachada norte → canteiro central / zona da laranjeira
- **6.97m** — zona central (do canteiro à palmeira)
- **2.54m** — palmeira (tronco) → muro sul

Soma: 2.56 + 6.97 + 2.54 = 12.07m. Os ~0.93m em falta face aos 13.00m totais correspondem às espessuras dos canteiros/muretes intercalados.

### Eixo W→E (largura)

- **5.78m** — largura interior (entre faces internas dos muros)
- **6.13m** — largura exterior (entre faces externas dos muros)

### Zona hot tub

- **2.43m** — profundidade N→S (fachada → fim das escadas)
- **4.29m** — largura W→E (muro oeste → lateral das escadas)
- **1.92m** × **1.88m** — dimensões do hot tub Intex
- **1.45m** — distância do canteiro lateral este ao canteiro central

### Fachada norte (de `FachadaNortemockup.jpg`)

- **4.30m** — largura da zona hot tub (W→E), ao nível do chão
- **2.00m** — altura da fachada até às janelas (desde cota do jardim)
- **1.25m** — altura das escadas
- **1.50m** — largura das escadas

---

## DESNÍVEL E MURO DE SUPORTE

- Casa → jardim: **1.60m** (escada ~5 degraus)
- Muro sul tardoz: **8.00m** abaixo da cota do jardim
- Idade: **~95 anos**
- **Implicação:** muro de suporte crítico. Drenagem periférica é prioridade técnica. Zero acumulação de água, zero carga adicional, zero escavação próxima sem avaliação

---

## COMO RELACIONAR PLANTA E FOTOS

### Da planta (`PLANTAREALJARDIM.jpg`) para a realidade

| Na planta | Direcção | Nas fotos |
|-----------|----------|-----------|
| Esquerda | Norte / Fachada | O que se vê em `FachadaNortereal.jpg` e `FachadaNortemockup.jpg` |
| Direita | Sul / Muro fundo | Muro branco ao fundo em `VistaJardimNS.jpg` |
| Cima | Este / Muro lateral | Muro à **esquerda** do observador em `VistaJardimNS.jpg` |
| Baixo | Oeste / Muro lateral | Muro à **direita** do observador em `VistaJardimNS.jpg` |

### Observador no topo das escadas → `VistaJardimNS.jpg`

- Está no **canto NE**, olha para **sul** (para o muro de fundo)
- **À sua esquerda:** muro este (com canteiro lateral)
- **À sua direita:** muro oeste
- **Atrás/direita próxima:** zona hot tub (não visível — está atrás e abaixo do observador)
- **Primeiro plano:** escadas, canteiro lateral este (murete com vegetação)
- **Centro:** canteiro central elevado com deck de madeira
- **Centro-fundo:** laranjeira (tronco fino) + palmeira (copa dominante) — lado esquerdo (este)
- **Fundo-direita:** lodão bastardo (copa grande escura, encostado ao muro oeste)
- **Fundo:** muro sul branco, casas do quarteirão de trás visíveis acima

### Observador no jardim a olhar para norte → `FachadaNortereal.jpg` / `FachadaNortemockup.jpg`

- Está no **jardim** a olhar para **norte** (para a casa)
- **À esquerda:** muro oeste + árvore decídua (zona hot tub)
- **Centro:** fachada do prédio — porta, janelas, varanda acima
- **À direita:** escadas encostadas ao muro este
- **Chão (real):** betonilha degradada e fissurada (`FachadaNortereal.jpg`)
- **Chão (mockup):** relva (`FachadaNortemockup.jpg`) — não existe, é visualização futura
- **Cotas visíveis no mockup:** 4.30m largura, 2.00m altura fachada, 1.25m altura escadas, 1.50m largura escadas
