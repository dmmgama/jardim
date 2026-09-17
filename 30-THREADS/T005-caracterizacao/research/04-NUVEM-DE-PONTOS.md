---
created: 2026-09-17
thread: T005
tipo: pesquisa
summary: |
  Avalia levantamento por nuvem de pontos com equipamento profissional (TLS, SLAM
  handheld, fotogrametria DSLR, drone) para o quintal de Alcântara, em contraste com
  a conclusão anterior (T005/02) de que captura por telemóvel não serve para os muros.
  Confirma que TLS de estação fixa resolve o reboco liso porque mede tempo de voo do
  laser e não depende de textura — ao contrário da fotogrametria, que falha pela mesma
  razão física independentemente da câmara usada. Para os muros, o telémetro laser de
  30 € já dá ±1,5 mm de altura; a nuvem de pontos só acrescenta valor em verticalidade,
  empeno e geometria completa do troço — não na cota simples. Para a copa da palmeira
  (bloqueio nº1 do projecto), a nuvem TLS ou SLAM ganha por larga margem sobre medição
  manual, com erro esperado de poucos cm em vez de dezenas. A ênfase do documento está
  no pós-processamento: cadeia completa de formatos, registo, limpeza, segmentação
  (CSF), extracção de geometria (planos de muro, convex/alpha hull de copa, malha para
  análise solar), com caminho 100% open source (CloudCompare) para quem não tem acesso
  a software de fabricante. Acesso pela casa (7 degraus) elimina TLS de tripé pesado
  como primeira escolha e favorece SLAM handheld, mais leve e mais rápido. Procedimento
  de campo de uma tarde incluído. Veredicto: vale a pena, mas só para a copa da árvore
  e para verticalidade dos muros — não para a cota simples dos muros, que o telémetro
  já resolve.
---

# Nuvem de pontos com equipamento profissional — captura e tratamento

## 0. Enquadramento

A pesquisa anterior (`02-DIGITAL-TWIN-SOFTWARE.md`) concluiu que LiDAR de iPhone e
fotogrametria de telemóvel não servem para medir os muros (erro de dezenas de cm
contra ±1,5 mm de um telémetro laser de 30 €) e que, para a copa da palmeira, o LiDAR
de iPhone dá 10–56 cm de erro consoante o estudo. Essa conclusão está aceite e não é
reaberta aqui.

O que muda agora é a categoria de equipamento: **varrimento profissional**, possivelmente
emprestado ou alugado — TLS de estação fixa, SLAM handheld, ou fotogrametria com câmara
dedicada e alvos codificados. É outra ordem de grandeza de precisão e a conclusão
anterior não se transfere automaticamente. Esta pesquisa testa-a de novo, para este
equipamento, e dá peso desproporcional ao **pós-processamento** — porque foi isso que o
utilizador identificou como a sua real incerteza: *"tenho eventualmente possibilidade de
arranjar máquina; só preciso depois de tratar o que daí vier."*

Todos os preços e especificações foram verificados por pesquisa web em Setembro de 2026.
Onde não foi possível confirmar um valor, está marcado **"não apurado"**.

---

## 1. O equipamento

### 1.1 TLS — Terrestrial Laser Scanner de estação fixa

| Modelo | Precisão declarada | Alcance | Peso/tripé | Nota |
|---|---|---|---|---|
| **Leica BLK360 G2** | Ruído de superfície 6 mm (modo Dense+), 12 mm (Dense), 25 mm (Fast+) | Até ~60 m | ~1 kg, compacto, monta em tripé fotográfico ligeiro | Scan completo em ~20 s. Mais um "point-and-shoot" do que instrumento de topografia pesado — o mais transportável dos TLS de estação fixa |
| **Leica RTC360** | 1,9 mm a 10 m / 3 mm ao nível de resolução mais alto | Até 130 m | Tripé robusto, ~5,3 kg a unidade | Substituído nominalmente pela série RTC300/500/700 lançada em 2026, mas ainda o modelo mais citado no mercado de aluguer |
| **FARO Focus Premium** | 1,5 mm a 10 m (resolução 1×) | Até 200 m (90% reflectividade) | ~4,2 kg, tripé topográfico | Referência de precisão da categoria "survey-grade" compacta |
| **Trimble X7** | mm-level, calibração automática em campo | Até 80 m | Tripé robusto | Menos citado em fontes consultadas — **não apurado em detalhe** |

**Quantas estações para 13,00 × 5,78 m com árvores a obstruir?** Não há fonte específica
para um pátio desta dimensão exacta. Por analogia com protocolos de inventário florestal
em parcelas de 50×50 m (que usam tipicamente 5 estações — uma central e quatro periféricas,
ajustadas para minimizar oclusão, com 20 min por estação incluindo montagem), e escalando
para baixo: um recinto de 75 m² fechado por dois muros longos deveria ficar coberto com
**4 a 6 estações** — uma a cada extremidade do eixo comprido, duas a meio junto a cada
muro (para rasância mínima sobre o próprio muro), e uma ou duas adicionais atrás da copa
das árvores para preencher a sombra de varrimento que a folhagem projecta. Isto é
**extrapolação, não um número verificado em fonte**; o número real só se confirma em campo.

**Registo entre estações:** por alvos (esferas reflectoras ou checkerboards) ou por
"cloud-to-cloud" sem alvos, quando há sobreposição suficiente (recomenda-se 30–40%) e
geometria reconhecível. Esferas têm a vantagem de serem vistas de qualquer ângulo com
centróide preciso; checkerboards são hoje o alvo mais universal. Em espaço pequeno e
com boa sobreposição, registo automático "cloud-to-cloud" no próprio software (Cyclone
Register 360, FARO SCENE) costuma bastar sem alvos físicos — reduz trabalho de campo.

### 1.2 SLAM / handheld móvel

| Modelo | Precisão indoor | Alcance | Peso | Nota |
|---|---|---|---|---|
| **Leica BLK2GO** | ±1 cm em ambiente indoor, scan de ~2 min; precisão relativa 6–15 mm | 25 m | ~0,8 kg, um só instrumento na mão | Sem GNSS/RTK — depende inteiramente de SLAM/loop closure |
| **GeoSLAM ZEB Horizon / ZEB Revo RT** | ~6 mm em área de teste de 500 m² | Variável | Portátil ao ombro/mão | Aluguer disponível na Europa (ver 1.7) |
| **NavVis VLX** | Recomenda percurso em loop, andar a ritmo normal para reduzir deriva | Até 100 m (LiDAR duplo) | Mochila, mais pesado | Orientado a levantamentos de maior escala |

**Deriva num percurso de 13 m:** a fonte mais concreta encontrada situa a deriva
acumulada em torno de 5 mm em interiores, com o BLK2GO a citar ±1 cm num scan de 2 min.
A correcção por **loop closure** — fechar o percurso voltando ao ponto de partida ou
cruzando trajectórias já percorridas — é o mecanismo central de controlo de deriva em
todos estes sistemas: o algoritmo reconhece sobreposição de geometria e redistribui o
erro acumulado ao longo do percurso todo. **Um percurso de 13 m é curto e fechável em
loop com facilidade — isto joga fortemente a favor do SLAM para este espaço.** É
plausível esperar deriva residual da ordem de poucos mm a ~1 cm no pior caso, desde
que o operador feche pelo menos um loop.

**Comparação honesta TLS vs. SLAM para este espaço:** o TLS de estação fixa dá mais
precisão absoluta (mm vs. cm), mas exige múltiplas montagens de tripé num espaço
apertado, com transporte de equipamento mais pesado através de 7 degraus. O SLAM é
mais rápido (um único percurso contínuo de 2–5 min cobre o recinto todo), mais leve
para transportar, e a curta distância do percurso mitiga o seu ponto fraco (deriva).
**Para este recinto especificamente, SLAM handheld é provavelmente a escolha mais
pragmática**, sacrificando alguma precisão absoluta que, para os alvos deste projecto
(copa de árvore, verticalidade de muro), não é o factor limitante.

### 1.3 Estação total

Não produz nuvem densa — produz pontos discretos, mas com precisão de 1–2 mm
(robótica) a poucos mm, e alcance/estabilidade muito superiores a qualquer scanner.
O papel correcto da estação total aqui não é substituir a nuvem, é **fornecer pontos
de controlo de altíssima confiança** (cantos do recinto, base de cada árvore, cotas de
referência) contra os quais a nuvem TLS/SLAM se georreferencia e se valida. Numa
parcela pequena com controlo por estação total, sub-centímetro é realista até para
a nuvem inteira. Para 75 m², provavelmente dispensável em rigor — mas é a forma mais
barata de detectar se o SLAM está a acumular erro sistemático, cruzando 3-4 distâncias
medidas por estação total (ou mesmo por telémetro laser bem calibrado) contra as
mesmas distâncias na nuvem processada.

### 1.4 Fotogrametria com câmara dedicada e alvos codificados

**Isto não resolve o problema do reboco liso, pela mesma razão física que elimina o
telemóvel.** Fotogrametria (Structure-from-Motion) depende de encontrar pontos
homólogos — textura, variação de cor ou relevo — em múltiplas fotografias para
triangular a geometria. Um muro rebocado liso, sem textura, em sombra permanente, é
o pior caso possível: superfície homogénea, sem feições para o algoritmo casar entre
fotos. Uma câmara DSLR/mirrorless de 24-45 MP não resolve isto — o problema não é
resolução de pixel, é ausência de sinal geométrico na superfície. Estudos mostram
RMSE da ordem de 8 mm em comparações de fotogrametria close-range contra LiDAR de
iPhone em superfícies com textura suficiente; sem textura, a técnica degrada de forma
não quantificável a partir das fontes consultadas — na prática, produz superfícies
ruidosas ou buracos onde o algoritmo simplesmente não converge.

**Onde a fotogrametria com alvos codificados ganha:** não nos muros, mas potencialmente
na copa das árvores, onde há abundante textura (folhas, ramos, contraste de luz),
e como complemento de cor/textura a um TLS que só dá geometria em tons de cinzento de
intensidade. Alvos codificados (códigos binários impressos, detectados automaticamente)
substituem a marcação manual de pontos de controlo e permitem escalar e orientar o
modelo com rigor superior a fotogrametria "solta". Mas para os muros especificamente,
esta técnica está eliminada pela física da superfície, não pela qualidade do
equipamento.

### 1.5 Drone / UAV

Não investigado em profundidade porque a resposta é evidente pelas dimensões do
espaço: um corredor de 5,78 m de largura entre muros de 2,50 m com copas de árvores
a variar em altura torna o voo automático de drone impraticável — margens de
segurança de voo automático GPS-denied não cabem, e a proximidade a muros e folhagem
é risco de colisão elevado. A excepção teórica seria um **drone de interior de voo
manual, pequeno, sem GPS** (ex. micro-drones usados em inspecção industrial) operado
por piloto experiente — mas isto não traz vantagem sobre SLAM handheld, que cobre o
mesmo volume com mais precisão e sem risco de colisão. **Não apurado** um modelo
concreto de drone de interior aplicável; a exclusão assenta em geometria do espaço,
não em falta de pesquisa dedicada.

### 1.6 Acesso — o equipamento tem de entrar pela casa, descer 7 degraus

| Equipamento | Peso/volume | Viabilidade de acesso |
|---|---|---|
| Leica BLK360 G2 + tripé fotográfico | ~1 kg + tripé leve | Sem problema — cabe numa mochila |
| TLS "survey-grade" (RTC360, FARO Focus) | 4–5,3 kg + tripé robusto (~2-3 kg) | Transportável à mão por um adulto, mas incómodo em escadas estreitas com viragens; **verificar largura da marquise e da porta envidraçada antes de reservar** |
| BLK2GO / GeoSLAM handheld | <1 kg, um só volume | Melhor caso de acesso — nenhuma restrição plausível |
| NavVis VLX (mochila) | Mais pesado, usa-se às costas | Viável, mas o operador tem de descer 7 degraus com carga às costas — atenção a equilíbrio |
| Estação total + tripé | ~5-6 kg + tripé + prisma | Viável mas mais um item a transportar |
| Drone | N/A | Excluído por dimensão do espaço, não por acesso |

**Conclusão de acesso:** nada aqui é fisicamente impeditivo, mas o SLAM handheld é
claramente o que menos fricção introduz — um volume, sem tripé, sem múltiplas viagens.
Isto reforça a recomendação do ponto 1.2.

### 1.7 Custo de aluguer em Portugal

Apurado parcialmente. Fontes portuguesas identificadas:
- **Topogis** (topogis.pt) — vende e tem "campanhas de aluguer" de scanners FARO;
  preço não publicado, **não apurado** sem contacto directo.
- **Grupo Acre** (grupoacre.com.pt) — revende e aluga tecnologia Leica em Portugal,
  incluindo BLK360 e modelos de gama P (ex. Leica P40); preço de aluguer **não
  apurado** — página não expõe tarifário público.
- **Global Geosystems** (global-geosystems.com/pt-pt) — distribuidor, venda de BLK360
  G2 em segunda mão a €17.750; sem informação de aluguer.

Referências internacionais (não aplicáveis directamente a Portugal, mas úteis como
ordem de grandeza): Leica BLK360 a partir de ~$563/mês em plataformas de aluguer nos
EUA; GeoSLAM ZEB Horizon a partir de ~$1.084/mês. Aluguer diário costuma rondar uma
fracção do mensal (tipicamente 1/10 a 1/15 do valor mensal por dia em equipamento
topográfico, por analogia de mercado — **não confirmado para scanners 3D
especificamente**).

**Conclusão sobre custo:** não foi possível apurar tarifário diário concreto em
Portugal sem contacto directo com Topogis, Grupo Acre ou Geonorth. Isto é uma lacuna
real do documento — ver secção "Buracos".

---

## 2. O que este espaço concreto faz ao varrimento

### 2.1 Reboco liso sem textura

**Mata a fotogrametria, mas não mata o TLS.** Confirmado: o laser de um TLS mede
tempo de voo (ou diferença de fase) do próprio feixe reflectido pela superfície — não
precisa de reconhecer feições visuais para triangular. Um muro branco liso e sem
relevo é, do ponto de vista de um scanner laser, uma superfície perfeitamente
mensurável, contanto que reflicta o suficiente do comprimento de onda usado.
Investigação dedicada a este exacto problema (TLS sobre rebocos, PMC/MDPI 2025)
confirma: rebocos com textura raspada geram ~26% mais desvio-padrão nas medições de
distância do que rebocos lisos — ou seja, **a textura prejudica ligeiramente o TLS
(dispersão do feixe em relevo), o oposto do que acontece à fotogrametria.** Superfícies
brancas lisas deram os melhores resultados num estudo que testou branco, vermelho,
azul e verde a 35 m. **Isto é a distinção central que justifica a pesquisa: o muro
mais hostil à fotogrametria é, por acaso, um dos mais favoráveis ao TLS.**

### 2.2 Copas de palmeira e árvores

Oclusão e folhagem fina são o desafio conhecido da técnica em qualquer escala —
literatura de inventário florestal (escala de parcelas de 50×50 m) trata exactamente
disto com "abordagem multi-scan": o que fica oculto numa estação é capturado por
outra, com sobreposição recomendada de 30–40% entre estações. À escala de uma única
árvore num pátio de 75 m², o mesmo princípio aplica-se a fortiori — com 3-4 posições
de varrimento à volta da base da palmeira (não só as estações gerais do recinto),
consegue-se cobertura quase completa da copa, excepto o topo absoluto se não houver
posição elevada.

**Movimento com o vento durante o varrimento:** não foi encontrada fonte que
quantifique isto directamente para folhagem em vento ligeiro urbano. É um problema
conhecido em SLAM/TLS de vegetação em geral — o próprio movimento da folha entre
passagens de laser introduz ruído que se manifesta como "espessamento" ou desfoque
da copa na nuvem, mais do que erro sistemático de posição do tronco/ramos principais.
Recomenda-se varrimento em dia de vento fraco a calmo — factor prático a controlar no
procedimento de campo, não um impeditivo.

### 2.3 Recinto estreito e fundo com muros altos

Ângulos rasantes (o feixe atingindo o muro em incidência muito oblíqua, próximo do
paralelo à superfície) degradam a precisão e podem criar sombras de varrimento —
zonas do muro que nenhuma estação "vê" de frente. Isto reforça a necessidade de
múltiplas estações distribuídas ao longo do eixo comprido (13 m), e não apenas duas
nos extremos — o meio do recinto precisa de pelo menos uma estação lateral para evitar
que o troço central de cada muro seja varrido só em ângulo raso pelas estações das
pontas.

### 2.4 Sombra permanente / pouca luz

**Não afecta a geometria do TLS** — o scanner é uma fonte de luz activa (o próprio
laser), pelo que funciona identicamente com sol directo, sombra ou escuridão total, ao
contrário da fotogrametria passiva que depende de luz ambiente. **Afecta apenas a
captura de cor RGB** sobreposta à nuvem (a maioria dos TLS tem câmara interna ou
externa para colorir os pontos) — em pouca luz, essa componente de cor fica escura ou
ruidosa, mas a geometria (o que interessa para muros, cotas e volumes) não é
comprometida. Para SLAM handheld com câmara embutida, o mesmo se aplica à componente
visual; alguns sistemas SLAM dependem parcialmente de features visuais para tracking,
o que pode, em teoria, ser prejudicado em luz muito baixa — mas os modelos LiDAR-SLAM
(BLK2GO, GeoSLAM) fazem tracking primariamente pelo próprio LiDAR, não pela câmara, o
que os torna relativamente robustos a pouca luz.

---

## 3. O TRATAMENTO — a cadeia de pós-processamento

Esta é a secção com mais peso, porque é onde está a real incerteza do utilizador.

### 3.1 Formatos de saída

| Formato | Neutralidade | Conteúdo | Nota |
|---|---|---|---|
| **E57** (ASTM E2807) | **Vendor-neutral, standard de indústria para arquivo e troca** | Geometria + pose do scanner + intensidade + cor + imagem panorâmica, tudo num ficheiro | Nenhum fabricante grava nativamente em E57 — cada um regista no seu próprio formato (FLS FARO, PTX/PTG Leica, TZF Trimble) e **exporta** para E57 a pedido |
| **LAS/LAZ** | Neutro, standard geoespacial (ASPRS) | Geometria + classificação, sem pose de scanner nem imagem panorâmica; LAZ é a versão comprimida | Preferido para pipelines GIS/geoespaciais; LAZ pode reduzir tamanho de ficheiro drasticamente sem perda de dados |
| **PTS/PLY** | Neutros, simples | Coordenadas (+ cor opcional), sem estrutura de metadados rica | Bons para troca simples entre software open source (Meshlab, CloudCompare) |
| **RCP/RCS** (Autodesk) | **Proprietário** | Formato indexado, optimizado para streaming de biliões de pontos no ecossistema Autodesk | Um-sentido: construído a partir de fontes abertas, não o contrário. Só útil se o destino for Revit/AutoCAD |

**Recomendação prática:** pedir sempre **E57** como entrega da própria máquina (a
maioria dos softwares de fabricante consegue exportar para E57 mesmo em versão
gratuita/trial), porque é o único formato que preserva pose de scanner e cor, e é
lido por praticamente todo o software de processamento, incluindo os open source.

### 3.2 Registo/alinhamento de varrimentos múltiplos

**Na máquina/software de fabricante:** normalmente automático ou semi-automático em
tempo real ou quase — o BLK2GO e equivalentes SLAM fazem o registo continuamente
durante a captura, como parte do próprio algoritmo SLAM. TLS de estação fixa
normalmente exige um passo de registo pós-captura no software do fabricante (Cyclone
Register 360, FARO SCENE), que consegue registo automático "cloud-to-cloud" quando há
sobreposição suficiente, sem necessidade de alvos físicos — mas alvos aumentam a
robustez em espaços com pouca geometria distintiva.

**No computador, com CloudCompare (open source):** CloudCompare tem uma ferramenta de
alinhamento manual ("Align — point pairs picking", escolhendo 3-4 pontos homólogos
manualmente em cada par de nuvens) seguida de refinamento automático por **ICP**
(Iterative Closest Point) — o algoritmo padrão da indústria para afinar registo depois
de um alinhamento grosseiro. Isto funciona bem quando já se tem uma boa estimativa
inicial (por exemplo, se cada scan já vem georreferenciado à mesma origem pelo
software da própria máquina) ou quando há sobreposição substancial e geometria
reconhecível entre scans. **Se a máquina só exportar scans separados sem qualquer
registo prévio**, alinhar tudo manualmente em CloudCompare é o passo mais trabalhoso
e sujeito a erro de todo o fluxo — mais um argumento para preferir equipamento cujo
software próprio já faça o registo antes de entregar o ficheiro final.

### 3.3 Limpeza e filtragem

CloudCompare tem ferramentas de:
- **Remoção de outliers estatísticos** (SOR — Statistical Outlier Removal), que
  elimina pontos isolados / ruído aleatório.
- **Selecção manual** ("Segment" tool com polígono/caixa) para apagar manualmente
  pessoas em movimento, objectos temporários, ou folhagem claramente distorcida por
  movimento durante o varrimento.
- **Subamostragem** (subsampling espacial ou aleatório) para reduzir densidade
  excessiva sem perder a forma — importante porque uma nuvem de um recinto de 75 m²
  varrido por TLS de alta resolução pode facilmente ultrapassar dezenas de milhões
  de pontos, tornando o processamento lento num portátil comum.

### 3.4 Software de processamento

| Software | Licença | Plataforma | Faz | Não faz / limitações |
|---|---|---|---|---|
| **CloudCompare** | **Gratuito, open source, GPL** | **Windows/Mac/Linux** | Registo (manual + ICP), limpeza, segmentação manual, cálculo de distâncias nuvem-a-nuvem, ajuste de planos, secções transversais, classificação CSF (plugin), reconstrução de malha (Poisson via plugin) | Interface pouco amigável, sem registo automático "cloud-to-cloud" tão robusto quanto Cyclone/SCENE para grandes conjuntos; sem motor CAD paramétrico |
| **PDAL** | Gratuito, open source | Win/Mac/Linux (linha de comandos) | Pipeline de processamento em lote, conversão de formatos, filtros (incluindo CSF) | Sem interface gráfica — exige scripting; mais adequado a automatizar do que a explorar interactivamente |
| **Open3D** | Gratuito, open source (Python) | Win/Mac/Linux | Biblioteca de processamento programático — ICP, reconstrução de malha, downsampling | Exige programação Python; não é ferramenta "aponta e clica" |
| **Meshlab** | Gratuito, open source | Win/Mac/Linux | Processamento e reparação de malhas (mais vocacionado para malha do que nuvem bruta) | Menos vocacionado para nuvens TLS de grande escala do que CloudCompare |
| **Potree** | Gratuito, open source | Visualização web | Visualização de nuvens muito grandes via browser, partilha fácil com terceiros | Não processa — é só visualização/partilha |
| **Autodesk ReCap Pro** | ~$350/ano (subscrição) | Windows/Mac | Registo, limpeza, integração directa com Revit/AutoCAD | Custo recorrente; formato nativo (RCP) proprietário |
| **Leica Cyclone / Register 360** | $4.500–6.500/ano (gama enterprise) | Windows | Registo automático de altíssima robustez, nativo para dados Leica | Caro; algumas ferramentas exigem hardware Leica para desbloquear funcionalidade completa |
| **FARO SCENE** | Licença comercial — **não apurado** | Windows | Registo nativo de dados FARO | Orientado ao ecossistema FARO |
| **Trimble RealWorks** | Comercial — **não apurado** | Windows | Registo e processamento para dados Trimble | Idem |
| **Bentley Pointools** | Comercial — **não apurado** | Windows | Integração com ecossistema Bentley (MicroStation) | Nicho fora do ecossistema Autodesk/Leica |

**Resposta directa à nota do utilizador:** se o utilizador tiver acesso à máquina mas
não ao software do fabricante (cenário plausível se o equipamento for emprestado por
terceiros sem licença cedida), **o caminho é: pedir que a entrega seja em E57** (ou
LAS/LAZ) já registado (se possível) pelo operador da máquina, e depois fazer tudo o
resto — limpeza, segmentação, extracção de geometria, malha — **inteiramente em
CloudCompare**, que corre nativamente em Windows 10. Isto é viável e coberto em
detalhe na secção 3.6. O único ponto onde a ausência de software de fabricante dói
verdadeiramente é se os scans vierem **não registados**: nesse caso, o registo manual
em CloudCompare é trabalhoso mas não impossível para 4-6 estações num espaço pequeno
com boa sobreposição.

### 3.5 Segmentação e classificação

**CSF — Cloth Simulation Filter** (disponível como plugin nativo do CloudCompare): o
algoritmo inverte a nuvem, simula um pano de tecido a cair sobre a superfície
invertida, e classifica como "chão" tudo o que fica próximo da superfície final do
pano, e como "não-chão" (vegetação, muros, objectos) o resto. É hoje um dos métodos
de classificação de terreno mais usados, com poucos parâmetros a afinar (resolução do
pano, rigidez, limiar de classificação) e boa precisão. **Funciona bem a esta escala**
— foi desenhado originalmente para levantamentos aéreos de grande área, mas o
princípio (distância vertical a uma superfície simulada) escala perfeitamente para
baixo, incluindo pátios pequenos, desde que a base seja razoavelmente plana (que é o
caso, sobre betonilha).

Separar **muros** de **vegetação** e **chão** de forma automática é mais difícil e
menos garantido por ferramentas prontas a usar — machine learning para classificação
semântica de nuvens de pontos (redes como PointNet e variantes) existe, mas exige
treino ou modelos pré-treinados que raramente estão afinados para um cenário tão
específico e pequeno como um pátio doméstico. **Na prática, para um espaço de 75 m²,
a segmentação manual em CloudCompare** (seleccionar com a ferramenta "Segment" os
pontos que pertencem a cada muro, à copa de cada árvore, ao chão) **é mais rápida e
mais fiável do que tentar afinar um classificador automático** — é um trabalho de
minutos a poucas horas, não de dias, dado o tamanho do conjunto de dados.

### 3.6 Extracção de geometria utilizável — a pergunta que interessa ao projecto

**Plano de muro (altura, verticalidade, troço a troço):**
Em CloudCompare, seleccionar a porção de nuvem correspondente ao muro e usar
"Fit Plane" para ajustar um plano matemático aos pontos. O software devolve os
parâmetros do plano e o desvio-padrão dos pontos em relação a ele — isso é
directamente uma medida de **planaridade** (quão irregular é a superfície real
contra um plano ideal). Para **verticalidade**, compara-se a normal do plano ajustado
com a vertical teórica (eixo Z) — o ângulo entre as duas dá o desvio de prumo do muro,
troço a troço se se segmentar o muro em várias secções e ajustar um plano a cada uma.
A ferramenta **"Cross Section"** permite cortar fatias horizontais ou verticais da
nuvem e extrair o perfil 2D em cada corte — útil para ver como a altura ou a
verticalidade do muro varia ao longo dos 13 m, algo que um telémetro pontual nunca
mostra.

**Volume e diâmetro de copa de árvore — o alvo nº1:**
Métodos estabelecidos na literatura (fontes ScienceDirect/MDPI consultadas):
- **Convex hull** — o invólucro convexo mínimo que contém todos os pontos da copa.
  Simples e rápido, mas sobrestima volume em copas irregulares ou com reentrâncias
  (sobrestimação sistemática documentada na literatura).
- **Alpha shape** — generalização do convex hull que permite "concavidades", seguindo
  a forma real da copa com mais fidelidade; um parâmetro alpha controla o quão
  apertado o invólucro se ajusta aos pontos.
- **Voxelização** — divide o espaço em cubos (voxels) e conta os voxels ocupados por
  pontos da copa; dá directamente um volume sem depender de forma geométrica
  assumida.
- **Combinação alpha shape + voxel** — segundo um estudo comparativo (ScienceDirect,
  2024), é a combinação que mais se aproxima do "volume biomassa óptimo" e tem
  maior correlação com biomassa medida em campo — a referência mais forte encontrada
  para este propósito.
- **Concave hull por fatias** ("slice method") — mostrou-se mais robusto e menos
  sensível a nuvens incompletas do que alpha shape 3D puro num estudo dedicado a
  volume de copa por LiDAR veicular — relevante porque uma copa de palmeira varrida
  de poucas posições terrestres nunca será 100% completa (o topo e o interior denso
  ficam parcialmente ocultos).
- **TreeQSM** — vai mais longe: ajusta cilindros segmentados a tronco e ramos
  individuais, reconstruindo a estrutura da árvore ramo a ramo. É a ferramenta certa
  para uma árvore de estrutura lenhosa clara (o lodão, por exemplo), mas **uma
  palmeira não tem ramos no sentido lenhoso — tem um tronco único e folhas grandes
  emergindo do topo (a coroa)**, pelo que TreeQSM é desenhado para a árvore errada
  neste caso. Para a palmeira, **alpha shape ou concave hull por fatias sobre a
  massa de pontos da coroa** é a abordagem correcta, não reconstrução de estrutura
  ramificada.

Tudo isto é executável em CloudCompare: segmentar a copa, exportar para uma
ferramenta de alpha shape (algumas implementações existem como plugins de terceiros
ou via Python/Open3D, que tem `alpha_shape` nativo), ou aproximar com convex hull
directamente disponível no CloudCompare como primeira estimativa rápida.

**Modelo digital de terreno / cotas:**
Depois de classificar "chão" com CSF, os pontos de chão classificados já constituem
uma nuvem de terreno; interpolando-a numa grelha regular (rasterização), obtém-se um
MDT (modelo digital de terreno) com cotas em qualquer ponto — directamente útil para
o problema do jardim subir +0,50 m sobre a betonilha existente, permitindo calcular
volume de aterro necessário com precisão muito superior a estimativas por régua.

**Conversão para malha utilizável em análise solar:**
CloudCompare tem o plugin **qPoissonRecon** (implementação da reconstrução de
superfície de Poisson, algoritmo académico de referência de Kazhdan/Johns Hopkins),
que gera uma malha triangular contínua a partir de uma nuvem de pontos com normais
calculadas. É particularmente adequado a formas orgânicas — copas de árvore incluídas
— e devolve uma medida de "densidade" que sinaliza zonas onde a nuvem original era
esparsa (útil para saber onde a malha resultante é fiável e onde é extrapolação). A
malha resultante em formato OBJ/PLY é importável em Rhino/Grasshopper e, por extensão,
no motor Ladybug/Honeybee já identificado na pesquisa anterior como a espinha dorsal
de análise solar do projecto — fechando a cadeia inteira, do scanner ao cálculo de
horas de sol sobre uma copa real.

### 3.7 Onde a cadeia parte — o que consome mais tempo

Sem fonte quantitativa directa para este ponto específico, mas por convergência das
fontes sobre fluxo de trabalho de reality capture: os dois pontos de maior atrito
identificados são (a) **registo manual** quando a máquina não entrega scans já
alinhados — é tedioso, exige escolher pontos homólogos com cuidado, e erros aqui
propagam-se para tudo o resto; e (b) **segmentação manual** de vegetação vs.
estrutura quando não há classificador automático afinado — em nuvens grandes, isto é
literalmente clicar e seleccionar milhares de vezes se feito com descuido, ou
poucas horas se feito com boas ferramentas de selecção por caixa/polígono e CSF a
tratar do chão automaticamente. **A combinação mais provável de fazer alguém
desistir é: máquina emprestada sem tempo para aprender a exportar correctamente +
scans não registados + primeira tentativa de usar CloudCompare sem qualquer tutorial
prévio.** Mitiga-se dedicando 1-2 horas a um tutorial de CloudCompare antes do dia de
campo, não depois.

---

## 4. Comparação honesta com as alternativas já estabelecidas

### 4.1 Para os muros

O telémetro laser de ~30 € dá ±1,5 mm de **distância pontual** — suficiente e melhor
do que muitas nuvens de pontos para uma simples cota de altura ponto-a-ponto. **A
nuvem de pontos não bate essa precisão pontual isolada**, mas acrescenta o que o
telémetro estruturalmente não pode dar:
- **Verticalidade e empeno ao longo de todo o comprimento do muro** — o telémetro dá
  um ponto de cada vez; a nuvem dá o perfil contínuo dos 13 m, revelando se o muro
  entorta, se há zonas de desaprumo localizado, se a altura varia de troço a troço
  (o que é plausível em muros de meação antigos).
- **Geometria completa para o modelo 3D** — se o destino final é um modelo Rhino
  alimentando Ladybug/Honeybee, uma nuvem TLS dá directamente a superfície real do
  muro (incluindo eventuais salientes, cunhais, vãos), poupando o trabalho de
  desenhar manualmente a partir de medições pontuais dispersas.
- **Conclusão honesta:** para a pergunta estreita "qual é a altura do muro", o
  telémetro continua a vencer em rácio custo-precisão-simplicidade. Para "qual é a
  geometria completa e verdadeira do muro, incluindo desvios", a nuvem vale o
  trabalho — mas só se o utilizador já for fazer o varrimento por causa da árvore
  (ver 4.2). **Não justifica, isoladamente, todo o esforço de aluguer e
  processamento só para os muros.**

### 4.2 Para a copa da palmeira — aqui a nuvem ganha por larga margem

**Quantificação:** medição manual de copa de palmeira com fita métrica e vara —
mesmo com boa técnica, envolve estimar o diâmetro máximo da coroa a partir do chão,
com linha de vista limitada pela própria copa e pelo tronco, e projectar
verticalmente uma forma que, vista de baixo, é dificilmente perceptível na sua
extensão real. Erros de 0,5 a mais de 1 m no diâmetro de copa não são invulgares
nesta técnica — não há fonte quantitativa directa para palmeiras especificamente,
mas por analogia com os erros de 10-56 cm já documentados para LiDAR de iPhone
(pesquisa anterior), medição manual sem instrumento tende a ser pior ainda, porque
depende inteiramente do julgamento visual do operador a partir de um único ponto de
observação no chão.

Uma nuvem TLS ou SLAM bem executada, com múltiplas posições à volta da base da
palmeira, produz um envelope 3D real da copa com erro esperado na ordem de **poucos
centímetros** (consistente com as precisões de 6-25 mm por ponto individual citadas
para os equipamentos na secção 1, com o erro do volume final dependendo mais da
completude da cobertura — quantas posições, quão bem se contornou a oclusão — do que
da precisão intrínseca do instrumento). **Isto é uma melhoria de uma ordem de
grandeza sobre medição manual, e ainda uma melhoria clara sobre LiDAR de iPhone.**

### 4.3 O mínimo que resolve o bloqueio nº1

Esta é a pergunta que a pesquisa anterior já obrigou a fazer com honestidade, e
continua válida: **será que uma tarde com fita métrica, vara telescópica e
fotografia calibrada (várias fotos da copa contra um fundo com escala conhecida, de
vários ângulos, medindo manualmente a projecção da copa no chão com uma fita à volta
da base) resolve o problema a um custo e complexidade muito menores?**

Resposta honesta: **parcialmente, e com lacunas conhecidas.** O método manual
consegue razoavelmente bem o **diâmetro de projecção no plano horizontal** (a sombra
que a copa projectaria directamente para baixo, medida com fita à volta da base e
correcção trigonométrica pela altura estimada), que é o dado que mais interessa para
um cálculo de sombra simplificado. O que o método manual **não consegue** é a forma
tridimensional real da coroa — a palmeira tem folhas a alturas e ângulos distintos, o
que produz um padrão de sombra fragmentado (já identificado na pesquisa anterior)
que um "disco" ou "cilindro" simplificado nunca reproduz correctamente ao longo do
dia, à medida que o ângulo do sol muda.

**Portanto:** se o objectivo é uma estimativa aproximada de sombra ao meio-dia, o
método manual + fotografia chega lá com esforço mínimo. Se o objectivo é um cálculo
de horas de sol directo ao longo de todo o dia e do ano (que é precisamente o que
Ladybug/Honeybee foram escolhidos para fazer, segundo a pesquisa anterior), a forma
tridimensional real da copa importa, e **é aí que a nuvem de pontos deixa de ser luxo
tecnológico e passa a ser a ferramenta certa para o problema.** O entusiasmo
tecnológico não decide isto — a natureza do cálculo que se quer fazer a jusante é que
decide, e o projecto já escolheu (na T005/02) um motor de análise solar que precisa
de geometria real, não de uma aproximação grosseira.

---

## 5. Procedimento de campo — uma tarde, não topógrafo

Assumindo SLAM handheld (recomendação da secção 1.2 e 1.6) como primeira escolha, com
nota de adaptação para TLS de estação fixa entre parêntesis:

1. **Antes de sair de casa com o equipamento:** carregar a bateria completamente,
   confirmar cartão de memória vazio, e ler o manual rápido de exportação — saber
   *antes* do dia de campo como se exporta para E57, para não descobrir problemas de
   formato depois de devolver a máquina.

2. **Reconhecimento do espaço (10 min):** caminhar o recinto sem gravar, identificar
   zonas de oclusão previsível (sob a copa da palmeira, atrás do lodão, cantos
   apertados) e planear mentalmente o percurso ou as posições de estação.

3. **Captura SLAM (15-25 min):**
   - Iniciar a gravação junto à entrada (porta envidraçada / base dos degraus).
   - Caminhar devagar e de forma constante ao longo do perímetro do recinto,
     mantendo o scanner em movimento suave, sem paragens bruscas.
   - Contornar cada árvore de perto, incluindo uma volta completa à base da
     palmeira e do lodão, angulando o scanner para cima para capturar o máximo de
     copa visível de baixo.
   - Fechar pelo menos **um loop completo** — voltar ao ponto de partida ou cruzar
     uma trajectória já percorrida — para permitir correcção de deriva por loop
     closure (secção 1.2).
   - Se o equipamento permitir, fazer uma segunda passagem a uma altura diferente
     (ex. de um patamar elevado, se existir, ou simplesmente com o braço esticado
     para cima) para melhorar a cobertura do topo das copas.

   **[Nota TLS de estação fixa]:** 4-6 estações (secção 1.1), cada uma com ~5-10 min
   de varrimento + 5 min de montagem/nivelamento do tripé — orçar 1h30-2h30 só para
   captura, mais tempo do que o SLAM.

4. **Verificação no local, antes de arrumar o equipamento (15-20 min) — o passo mais
   importante deste procedimento:**
   - Se o software do equipamento permitir pré-visualização no ecrã do dispositivo
     ou de um tablet/telemóvel ligado, **verificar visualmente que os muros
     aparecem como planos contínuos e sem buracos grandes**, e que a copa das
     árvores tem densidade de pontos visível (não apenas o tronco).
   - Verificar se houve fecho de loop bem sucedido (indicador de qualidade, se o
     software o mostrar).
   - Se possível, repetir uma passagem rápida (5 min) numa zona que pareça fraca na
     pré-visualização — é gratuito fazê-lo no momento, e impossível depois de
     devolver o equipamento.

5. **Medições de controlo independentes (10 min) — antes ou depois do varrimento:**
   Medir com o telémetro laser 3-4 distâncias de referência simples (ex. comprimento
   total de um muro, distância entre dois pontos fixos opostos, altura num ponto
   conhecido). Estas medições servem para **validar a nuvem depois de processada**
   — se a distância medida na nuvem processada bater com o telémetro dentro de 1-2
   cm, há confiança de que o processamento não introduziu erro grosseiro.

6. **Erros típicos de principiante a evitar:**
   - Caminhar depressa demais durante captura SLAM — degrada a qualidade do
     tracking.
   - Não fechar nenhum loop — perde-se a correcção de deriva mais eficaz disponível.
   - Esquecer de capturar as zonas junto ao tecto/copa, olhando só para a frente —
     é preciso apontar deliberadamente para cima.
   - Varrer em dia de vento — introduz ruído na folhagem (secção 2.2).
   - Não verificar a exportação antes de devolver o equipamento — o erro mais caro
     possível.

**Tempo total realista:** 1h30-2h para SLAM incluindo verificação, 2h30-3h30 para
TLS de estação fixa múltipla. Ambos cabem numa tarde.

---

## Veredicto

**Vale a pena, mas não para tudo.** Para os muros isoladamente, não — o telémetro
laser já resolve a pergunta que interessa (altura, cota) com precisão superior e
custo irrisório; a nuvem só acrescenta verticalidade/empeno ao longo do comprimento,
que é valor real mas não crítico. **Para a copa da palmeira — o bloqueio nº1 do
projecto — sim, com convicção**: é o único método, entre os avaliados nesta e na
pesquisa anterior, capaz de produzir uma forma 3D real da coroa com erro de poucos
centímetros, contra dezenas de cm de LiDAR de telemóvel ou erro provavelmente maior
ainda de medição manual. Se a máquina for conseguida por outra razão (ex. para a
copa), aproveitar a mesma sessão para varrer os muros é trabalho adicional quase
gratuito — mas não justificaria, isoladamente, todo o esforço de aluguer e
processamento.

## Cadeia recomendada completa

1. **Equipamento:** SLAM handheld (Leica BLK2GO ou GeoSLAM ZEB) — mais leve, mais
   rápido, menos fricção no acesso pela casa, precisão (±1 cm indoor) mais do que
   suficiente para os alvos deste projecto.
2. **Captura:** uma tarde, ~1h30-2h incluindo verificação no local (secção 5).
3. **Exportação:** pedir E57 (ou LAS/LAZ) já registado, se o software da máquina o
   permitir — evita o passo de registo manual mais custoso.
4. **Processamento:** CloudCompare (gratuito, Windows 10) para limpeza, classificação
   CSF do chão, segmentação manual de muros/árvores/vegetação.
5. **Extracção:**
   - Muros: "Fit Plane" + análise de desvio para verticalidade/empeno por troço.
   - Copa da palmeira: segmentar, aplicar alpha shape ou concave hull por fatias
     (via Open3D/Python se necessário) para volume e diâmetro real.
   - Chão: pontos CSF classificados como terreno → MDT para cálculo de aterro.
6. **Malha final:** Poisson Surface Reconstruction (plugin CloudCompare) sobre a
   copa → exportar OBJ/PLY → importar em Rhino → alimentar Ladybug/Honeybee.
7. **Validação:** cruzar 3-4 distâncias medidas por telémetro laser contra a nuvem
   processada antes de dar o trabalho por concluído.
8. **Custo:** equipamento (aluguer não apurado em euros concretos — ver Buracos);
   software: 0 € (caminho open source integral).

## O caminho só-open-source

Assumindo zero acesso a software de fabricante — cenário mais provável se a máquina
for emprestada sem licença cedida:
- **Exigir/negociar exportação em E57** por quem opera a máquina (mesmo sem
  licença completa, a maioria dos fabricantes permite exportação básica em trial ou
  versão gratuita do seu visualizador).
- **CloudCompare** cobre registo (manual + ICP), limpeza, CSF, ajuste de planos,
  secções, reconstrução de malha por Poisson — tudo o que este projecto precisa,
  nativamente em Windows 10, sem custo.
- **Open3D (Python)** como complemento pontual só se for necessário alpha shape para
  a copa da árvore, que o CloudCompare não tem tão desenvolvido nativamente como
  convex hull — exige alguma disposição para correr um script Python, mas é um
  script curto e bem documentado na biblioteca.
- **Potree**, opcional, só se for útil partilhar a nuvem processada com terceiros
  (ex. um paisagista) via browser sem instalar nada.
- **Nada nesta cadeia é Linux-only ou Mac-only** — todos os itens listados correm em
  Windows 10.

## Buracos

- **Custo de aluguer diário em Portugal**, em euros concretos, para qualquer dos
  modelos citados — não apurado. Requer contacto directo com Topogis, Grupo Acre ou
  Geonorth (fontes identificadas na secção 1.7).
- **Número exacto de estações TLS necessárias para 13,00 × 5,78 m com estas árvores**
  — extrapolado por analogia de protocolos de parcelas florestais maiores, não
  verificado para este tamanho específico de recinto.
- **Erro quantificado de folhagem em movimento com vento ligeiro** durante
  varrimento — problema identificado qualitativamente, sem número de referência
  encontrado nas fontes consultadas.
- **Modelo concreto de drone de interior** aplicável, caso a exclusão por dimensão do
  espaço seja reconsiderada no futuro — não investigado em detalhe.
- **Preço de licença de FARO SCENE e Trimble RealWorks** — não apurado.
- **Largura exacta da marquise e da porta envidraçada** — necessária para confirmar
  com segurança que um TLS de estação fixa robusto (FARO Focus, RTC360, com o
  respectivo tripé) passa sem problema; assumido viável mas não verificado contra
  medidas reais da casa.
