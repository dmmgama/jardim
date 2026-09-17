---
created: 2026-09-17
project: Jardim
thread: T003
tipo: pesquisa encomendada pelo Arquitecto
estado: entregue — matéria-prima, não decisão
---

# Captura 3D com telemóvel — estado da arte, Setembro 2026

> **Encomendada pelo Arquitecto** ao abrir a T003, para não obrigar a thread a repetir a pesquisa.
> **É matéria-prima com fontes, não decisão.** A recomendação final é da T003, e tem de passar pelo
> crivo do que o modelo precisa. Ver `mensagens.md`, secção 3.
>
> **O agente assinalou explicitamente o que não conseguiu verificar.** Esses pontos estão marcados
> abaixo e **não podem ser tratados como facto.**

---

## A conclusão, à cabeça

**A pesquisa contraria o enunciado do pedido.** Foi pedida uma ferramenta de captura 3D; a resposta
honesta é que **para o alvo mais importante — a altura dos muros — a captura 3D é a ferramenta
errada**, e um telémetro laser de 20–40 € é objectivamente superior.

A captura 3D ganha **apenas** onde a geometria está fora do alcance de uma fita: as copas.

| Alvo | Ferramenta certa | Porquê |
|---|---|---|
| **Altura dos muros, troço a troço** | **Telémetro laser, 20–40 €** | ±1,5 mm por medição pontual, sem deriva, sem depender de textura. O limiar crítico do projecto é 0,5 m — a margem é de três ordens de grandeza. |
| **Copa da palmeira, lodão, citrinheira** | **LiDAR de iPhone Pro (Scaniverse)** | Fora do alcance de fita. Forma irregular. Erro esperado: **vários cm a poucas dezenas de cm** — chega para modelar um cilindro, não para cotas finas. |
| **Cota de retenção do muro SW** | Fita ou telémetro | É uma cota linear acessível. |

**Via recomendada: híbrida.** Telémetro para tudo o que é linha recta acessível; LiDAR só para as
copas. Fazer tudo por scan é mais lento **e** menos fiável.

---

## 1. Hardware — quem tem LiDAR em 2026

**iPhone:** exclusivo da gama **Pro** desde 2020. Têm: 12 Pro/Pro Max até 17 Pro/Pro Max, e iPads
Pro de 2020 em diante. **Não têm:** todos os modelos base, Plus, Air, mini, SE.

**Android — a conclusão importa:** **não existe em 2026 nenhum Android com LiDAR verdadeiro.**
- Google Tango descontinuado em 2018.
- Alguns Samsung antigos (S10 5G, Note10+, S20+/Ultra) tinham sensor ToF — descontinuado, ausente
  nos modelos recentes (S24/S25/S26).
- Pixel 7–10 Pro suportam a Depth API do Android, mas isso é **profundidade computacional
  multi-câmara**, não sensor dedicado. Precisão muito inferior.

> **Consequência dura:** se o telemóvel do David não for iPhone Pro, **não há equivalente Android**.
> A via em Android é sempre fotogrametria pura — que é precisamente o que falha nos muros.

*Fontes: caseadri.com, simplywise.com, droidgurus.com, scanmanifold.com*

---

## 2. Apps — comparação, preços de Setembro 2026

| App | Modelo | Preço | LiDAR | Fotogrametria |
|---|---|---|---|---|
| **Scaniverse** (Niantic) | Freemium | **Captura e processamento on-device gratuitos.** Planos Plus (~20 €/mês) e Pro (~50 €/mês) só para processamento em nuvem e 360° | Sim | Não é o foco |
| **Polycam** | Freemium | Grátis exporta **só GLTF**; Pro 26,99 €/mês ou ~150–200 €/ano | Sim | Sim |
| **RealityScan** (Epic) | Gratuito abaixo de 1 M$/ano de receita | Grátis no caso do David | App mobile grátis | Sim — motor RealityCapture |
| **KIRI Engine** | Freemium | Grátis (3 exports/semana); Premium 6,99 €/mês ou 49,99 €/ano | Sim | Sim |
| **Luma AI** | Freemium | Grátis para uso básico | Não usa LiDAR — fotogrametria na nuvem | Sim |

**Nota que interessa:** o KIRI Engine tem uma função **«Featureless Scan»**, pensada precisamente
para superfícies sem textura. Está atrás do plano pago mais caro. **Pode valer a pena investigar
antes de descartar a via 3D para os muros** — mas não altera a conclusão de que o telémetro é
melhor.

> ⚠ **NÃO VERIFICADO.** O agente não conseguiu confirmar se a Scaniverse mantém em Setembro de 2026
> **todos** os exports do fluxo LiDAR sem paywall. Parece que sim para captura e visualização, mas
> as fontes divergem sobre exports específicos. **Verificar na app antes de depender disto.**

*Fontes: softwaresuggest.com, learn.poly.cam, nianticspatial.com, cgchannel.com, kiriengine.app*

---

## 3. Precisão real — por tipo de alvo

### 3a. Superfícies lisas sem textura — os muros

**Fotogrametria pura falha estruturalmente aqui.** Precisa de pontos-chave distintos entre fotos
para triangular. Uma parede lisa e uniforme em sombra homogénea tem pouquíssimas *features* — o
algoritmo produz buracos, ruído de alta frequência, ou «derrete» a geometria numa superfície
ondulada falsa. É o cenário clássico de falha, bem documentado.

> **Isto confirma, por via independente, a razão pela qual a via Google 3D foi rejeitada**
> (`REJEICOES.md` §11). A razão não era específica do Google — é da fotogrametria.

**LiDAR não depende de textura** — mede tempo de voo de infravermelhos. É **a única via fiável para
os muros**, se se insistir em 3D.
- A ~1 m: precisão **2–3 cm**.
- Degrada visivelmente além de **4–5 m** (alcance útil do sensor).
- Para captar 2,5 m de altura a 2–3 m de distância — possível nos 5,78 m de largura do quintal —
  estás dentro da zona boa.
- Sombra e superfícies escuras reduzem ligeiramente o retorno, mas **muito menos** do que afectam a
  fotogrametria.

### 3b. Vegetação — as copas

Ponto fraco histórico de **ambas** as vias, por razões diferentes:
- **Fotogrametria:** folhas movem-se com o vento entre fotos (fantasmas, ruído); texturas
  repetitivas confundem o *matching*.
- **LiDAR de telemóvel:** o feixe atravessa lacunas entre folhas de forma inconsistente, produzindo
  uma **nuvem difusa** em vez de superfície de copa definida.

**Números publicados** (ForestScanner, iPhone LiDAR para dendrometria): erro médio absoluto de
altura de árvore **8–9 cm**, correlação CCC 0,96.

> ⚠ **Ressalva do próprio agente, que é importante:** esses números são para **troncos e alturas
> totais em condições controladas de floresta, com ajuste de cilindros**. Para uma copa de palmeira
> — forma irregular, palmas pendentes, não cilíndrica — **a fiabilidade é bastante inferior**. A
> ordem de grandeza confiável é **dezenas de cm de incerteza**, não os 8–9 cm.

**Densidade de pontos:** cai de ~7.225 pontos/m² a 25 cm para **~150 pontos/m²** a distâncias
maiores. Para uma copa a vários metros de altura, a nuvem sai **esparsa** — suficiente para
diâmetro e altura aproximados, não para detalhe.

### 3c. Deriva em 13 m — o ponto mais crítico

O LiDAR de telemóvel usa *tracking* visual-inercial (VIO) para se localizar à medida que te moves.
**Este tracking acumula deriva.** A indústria descreve-o sem rodeios: *«walls that should be
ruler-straight end up slightly bent»*; *«accuracy is adequate for visualization but not for
measurement, survey, forensics, or engineering»*.

**A Apple nunca publicou especificação de tolerância oficial.**

> ⚠ **EXTRAPOLAÇÃO, NÃO MEDIÇÃO.** O agente declarou não ter encontrado número publicado para 13 m
> de percurso com iPhone LiDAR — **é uma lacuna de dados**. A estimativa que deu, por analogia com
> scanners portáteis profissionais, é de **vários cm a >10 cm de erro acumulado** entre o início e o
> fim do varrimento. **Tratar como ordem de grandeza, não como facto.**

**A implicação prática é a que interessa:**
- Medir a altura de **um troço** de muro num scan curto e próximo: fiável, ~2–3 cm.
- Medir **os 13 m acumulados** dentro do mesmo modelo contínuo: é aqui que a deriva morde.

---

## 4. Exportação e fluxo até ao modelo

| App | Grátis exporta | Pago desbloqueia |
|---|---|---|
| **Scaniverse** | PLY, OBJ, USDZ, SPZ — **grande parte gratuita on-device** | Nuvem, 360° |
| Polycam | **Só GLTF** | PLY, OBJ, FBX, DAE, STL, LAS, PTS, XYZ, DXF, USDZ |
| RealityScan | Malha e nuvem, uso não-comercial | — |
| KIRI Engine | 3 exports/semana | Ilimitados, quad mesh, PBR |
| Luma AI | Splat (.ply/.splat), vídeo | Malha em alguns planos |

**O fluxo realista até ao modelo paramétrico:**

nuvem de pontos (.ply/.obj, à escala) → **Blender** (gratuito) ou **SketchUp** → usar a nuvem como
**referência visual** e desenhar por cima caixas e cilindros com as dimensões necessárias.

> **Não tentar automatizar a extracção.** O agente foi explícito: não há ferramenta simples de
> telemóvel que converta nuvem em «caixa com dimensão X» de forma fiável para geometria irregular.
> **O fluxo é: nuvem como guia, medição manual das cotas-chave, desenho paramétrico à mão.**
>
> ⚠ **Não verificado:** o agente procurou e **não encontrou** plugin maduro e gratuito que leve
> nuvem de telemóvel directamente a modelo de sombreamento sem modelação manual. Acredita que não
> existe. Não é prova de inexistência, mas é o melhor que a pesquisa deu.

**Para a T003, a consequência é boa:** o input útil não é a nuvem — são **os valores de altura e
diâmetro extraídos dela**, introduzidos como geometria paramétrica simples. É exactamente o que o
`contrato-de-dados.yaml` já pede.

---

## 5. Escala — resolvido, com uma nuance

**LiDAR sai à escala correcta automaticamente.** O sensor mede distância física real. É uma
vantagem prática grande sobre a fotogrametria.

**Fotogrametria pura não tem escala absoluta.** *Structure from motion* resolve forma, não tamanho.
Exige **barra de escala**: objecto de dimensão rigorosamente conhecida visível em várias fotos
(régua, fita esticada e fixada, alvo ArUco impresso), marcado manualmente no pós-processamento.
A literatura recomenda **no mínimo 3 pontos de controlo**, idealmente em planos diferentes.

**Boa prática recomendada mesmo com LiDAR:** deixar **uma fita métrica esticada e visível** num
segmento do muro durante a captura, como verificação independente. Custo zero, e denuncia
imediatamente se o modelo derivou.

---

## 6. Plano B sem iPhone Pro

1. **Pedir emprestado um iPhone Pro por uma tarde.** De longe o mais simples — não é preciso possuir,
   só usar uma vez para as copas. O resto faz-se com telémetro.
2. **Se impossível:** fotogrametria em Android (RealityScan gratuito, ou KIRI/Polycam em modo foto).
   60–150 fotos à volta da árvore, sobrepostas, boa luz, **com alvo de escala conhecida** (p. ex. um
   pau vertical medido, encostado ao tronco). Precisão aceitável para estimar sombreamento; **não
   confiar em cotas finas** sem verificação por fita.
3. **Para os muros, em Android, não vale a pena tentar 3D.** A superfície lisa vai falhar. O
   telémetro é a única via fiável — com ou sem iPhone.

---

## Ressalvas do agente, reunidas

O agente declarou não ter conseguido verificar:

1. Se a **Scaniverse** mantém todos os exports LiDAR sem paywall em Set. 2026.
2. **Erro de deriva em 13 m com iPhone LiDAR** — não há número publicado. A estimativa de
   «vários cm a >10 cm» é extrapolação por analogia.
3. Existência de **plugin maduro e gratuito** que leve nuvem a modelo de sombreamento sem modelação
   manual — procurou e não encontrou.

Os números de dendrometria (8–9 cm) são de **troncos em floresta**, não de copas de palmeira. O
próprio agente assinalou que para o caso concreto a incerteza é maior.
