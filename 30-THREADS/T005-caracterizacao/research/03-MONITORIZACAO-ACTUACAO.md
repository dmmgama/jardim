---
created: 2026-09-17
thread: T005
tipo: pesquisa
summary: |
  Levantamento do estado da arte em monitorização contínua e actuação automática para um
  jardim de ~75 m² construído sobre laje (cobertura verde com +0,50 m de substrato), em
  Alcântara, Lisboa. Cobre sensores (solo, ar, luz, água, vento, vegetação, sanidade
  fitossanitária), protocolos de transmissão, plataformas de controlo, actuadores (rega,
  fertirrega, iluminação cénica, sombreamento) e estratégias de controlo. Inclui três
  configurações de material com custo e manutenção estimados, o que não vale a pena medir,
  modos de falha, faseamento face à obra, e buracos de pesquisa. Achado central: existe
  detecção acústica precoce do escaravelho-vermelho-da-palmeira com taxas de sucesso >90%
  em ensaios publicados, mas o produto comercial mais próximo do mercado (Picusan/Koppert)
  não tem preço público apurado e não foi confirmada disponibilidade para cliente
  particular em Portugal — fica como recomendação condicional, não como compra pronta.
  Recomendação geral: sistema mínimo de humidade de substrato + chuva + fugas de água
  sobre ESPHome/Home Assistant local, sem cloud obrigatória, com rega ainda decidida por
  temporizador ajustado sazonalmente e não por malha fechada nos dois primeiros anos.
---

# Monitorização e actuação em contínuo — Jardim Alcântara (T005)

> Pesquisa para a T005. Não decide o que se compra — caracteriza o que existe, o que custa
> e o que sobrevive ao abandono. Ver `thread.md` para o mandato e limites.

## Nota metodológica e um aviso ao Arquitecto

O quintal vai ficar **sobre uma laje impermeabilizada, com 0,50 m de substrato**. Isto é
uma cobertura verde (*green roof* / *rooftop garden*), não um jardim de solo natural — e
a literatura de coberturas verdes é explícita: substratos finos falham cedo e falham mal
em clima mediterrânico, porque não há reserva de água lateral nem drenagem profunda para
absorver um erro (Tomasella et al. 2022; ASHS HortTechnology 20(2), 2010). Isto governa
todo este documento: **a humidade do substrato é o único parâmetro cuja falha mata plantas
em dias, não semanas**, e é por isso que recebe o maior peso abaixo.

Este documento **não** recomenda a T005 propor um "digital twin" de monitorização
completo — isso pertence à pesquisa irmã de software. Aqui trata-se apenas de sensores
físicos e dos actuadores que eles disparam.

---

## 1. O que se mede, e com quê

### 1.1 Solo — humidade, o parâmetro mestre

**A diferença entre tecnologias não é cosmética — é a diferença entre um sistema que
funciona e um que mente com confiança.**

| Tecnologia | Princípio | Exactidão realista | Preço unitário | Durabilidade exterior | Veredicto |
|---|---|---|---|---|---|
| **Resistiva** (duas hastes metálicas, tipo "sensor Arduino de 2€") | Resistência eléctrica entre eléctrodos | Erro 3,5–4,1% mas **degrada-se a cada leitura por electrólise** — corrói em semanas ao ar livre em substrato húmido | 1–3 € | Semanas a poucos meses | **Não usar.** Cada medição consome o sensor. Confirmado por *Laboratory Calibration and Performance Evaluation of Low-Cost…* (NCBI PMC7014303). |
| **Capacitiva de baixo custo** (ex. DFRobot/Gravity "corrosion-resistant") | Capacitância entre placas revestidas em resina | Sem calibração específica do substrato, erro pode ultrapassar 10 pontos percentuais de humidade volumétrica; com calibração local, R² > 0,91, erro máx. ~4,6% em ensaios dinâmicos | **18,50 €** (BotnRoll, DFRobot SEN0193/v2, PT, 2026) | 1–3 anos ao ar livre, resistente a imersão | **Usar, mas calibrar no substrato real do jardim** — não confiar na curva de fábrica (calibrada em água ou solo mineral genérico), que não representa um substrato leve de cobertura verde. |
| **FDR** (*Frequency Domain Reflectometry* — ex. Teros, 5TE) | Frequência de ressonância de um oscilador LC no solo | Referência secundária de facto: erro tipicamente <2% com calibração de fábrica, <1% com calibração específica | 80–200 € (não apurado preço PT) | 5–10 anos, uso agronómico contínuo | Investimento sério só se o sistema for para durar. Sobredimensionado para arranque. |
| **TDR** (*Time Domain Reflectometry*) | Tempo de propagação de um pulso electromagnético | Padrão de referência, erro tipicamente <1% (PMC, *Advances in Calibration Methods for FDR-Based Capacitive Soil Moisture Sensors*, 2026) | Centenas a milhares de euros | Alta | **Fora de escala.** Equipamento de estação experimental. |
| **Tensiómetro / Watermark** (potencial matricial) | Resistência de bloco de gesso em equilíbrio com a água do solo | 0–239 cb; Irrometer declara calibração estável comprovada | Watermark 200SS: **≈40 USD/unid.**; revendedor PT (Prilux) existe mas **preço PT não apurado** | Vida de vários anos em campo | **Mede a coisa certa para decidir rega** (o stress que a planta sente, não só o teor de água), mas resposta lenta e histerese em substratos leves — pouco testado neste contexto. |

**Interpretação para este projecto:** num volume de substrato de 0,50 m sobre laje
impermeável, a humidade volumétrica (capacitivo calibrado) é suficiente e mais barata do
que perseguir potencial matricial com tensiómetros — a decisão operacional ("rega ou não
rega hoje") não precisa da precisão física de um tensiómetro, precisa de um limiar
repetível. **Recomenda-se capacitivo calibrado no local, um por zona de rega**, não por
espécie — seria excesso de granularidade face à área.

Temperatura e condutividade eléctrica/salinidade vêm frequentemente **incluídas no mesmo
sensor** capacitivo de gama média (sensores RS485 "3-in-1", 15–35 €, sem fornecedor PT
identificado). **pH de substrato** por sonda permanente é o parâmetro menos fiável de
todos — sondas baratas degradam-se em semanas em substrato húmido e exigem calibração
frequente; **não vale a pena automatizar**, mede-se pontualmente com kit manual 1–2×/ano.

### 1.2 Ar — temperatura, humidade, VPD, CO2

| Parâmetro | Sensor | Preço | Nota |
|---|---|---|---|
| Temperatura + HR | Sensirion SHT31/SHT40 | Preço PT não apurado, ordem de grandeza 8–15 € | ±1,8% HR, ±0,2 °C — exactidão de laboratório num módulo de bolso |
| **VPD** (défice de pressão de vapor) | Não existe sensor — **é sempre calculado** a partir de T + HR (Tetens/Magnus) | 0 € adicional | VPD é o número que interessa fisiologicamente, mas **ao ar livre não se controla** (não há como humidificar um jardim exterior). Decisivo em estufa fechada; aqui é **informativo, não accionável**. Há template pronto na comunidade Home Assistant. |
| CO2 | NDIR (SCD30/SCD41) | 40–60 € | **Não relevante ao ar livre** — não se controla nem varia de forma accionável. Descartar. |

### 1.3 Luz — DLI é o número que decide a espécie, não o lux

Confirma-se: **DLI baixo (5–10 mol·m⁻²·d⁻¹) = sombra; médio (10–15) = meia-sombra; alto
(>15) = sol pleno** (Apogee Instruments; Virginia Tech Extension SPES-720).

| Sensor | O que mede | Erro de conversão | Preço |
|---|---|---|---|
| **Sensor quântico PAR/PPFD** (Apogee DLI-400/500/600) | Fotões PAR directamente | Referência — DLI-400 só sob luz solar; DLI-500/600 corrige para todas as fontes | Não apurado PT; gama internacional 150–400 USD |
| **Fotómetro lux** (BH1750 e afins) | Lux (resposta ao olho humano, não à fotossíntese) | Conversão lux→PAR **varia com o espectro** — sob sol directo o factor é ~0,0185 mol/m²/lux·h, mas **sob copa de árvore ou luz difusa o erro pode passar 30–50%** | 5–20 € |
| **Piranómetro** | Radiação de onda curta total | PAR é ~45% da radiação total em condições padrão, mas a fracção varia com nebulosidade e sombra parcial | Dezenas a centenas de euros |

**Veredicto:** para este jardim, onde a variabilidade espacial é o problema central (0,0 h
a 4,9 h de sol em zonas a metros de distância), **um sensor lux barato (BH1750, 5–8 €) por
zona, com factor de conversão calibrado uma vez contra um sensor PAR de referência
emprestado ou alugado**, dá 80% do valor a 5% do custo. Não vale a pena um DLI-500 por
zona — vale **um** sensor de referência bom, usado para calibrar vários sensores baratos fixos.

### 1.4 Água

| Parâmetro | Sensor | Preço | Nota |
|---|---|---|---|
| Pluviosidade | Pluviómetro de báscula (em estações Ecowitt/Bresser) | Disponível em Worten.pt e Fnac.pt; **preço unitário não apurado** | Serve também vento e ETo |
| Caudal de rega | Sensor de turbina (YF-S201 ou similar) | 5–15 € | Útil para **detectar fuga por diferença** entre caudal esperado e medido |
| **Detecção de fuga** | Sensor de imersão Zigbee (Aqara Water Leak) | **25,90 USD**; alternativa SONOFF ~10–12 USD | IP67, bateria >2 anos, mas **detecta poça, não gotejamento lento** |
| Humidade em parede (infiltração suspeita) | Higrómetro capacitivo ou sonda embutida | Produto dedicado não apurado | **Buraco de pesquisa** — ver §10 |
| Nível de água (pond/piscina) | Ultrassónico ou pressão hidrostática | 15–40 € (JSN-SR04T impermeável) | Simples e barato |

### 1.5 Vento

Anemómetro de conchas incluído em estações domésticas completas. Num recinto de 5,78 m
entre muros de 2,50 m, **o vento medido no topo do mastro não representa o vento ao nível
das plantas** — o recinto é abrigado por desenho. Valor prático: **confirmar que não há
necessidade de "saltar rega por vento"** (critério usado por Rachio/Hydrawise em jardins
abertos), que aqui é provavelmente irrelevante. Não priorizar.

### 1.6 Vegetação — fluxo de seiva, dendrómetros, NDVI

- **Fluxo de seiva:** há investigação recente a baixar o custo para <150 USD (dispositivo
  "Js5", ScienceDirect 2022), mas **não é produto comercial maduro** — exige electrónica
  própria, calibração e manutenção de sondas inseridas no caule.
- **Dendrómetros:** mesma situação — desenvolvimento académico de sistemas de baixo custo
  (ScienceDirect 2026), sem produto de prateleira a preço doméstico apurado.
- **Câmaras NDVI/multiespectrais:** módulos de câmara modificada na ordem de 100–300 €,
  mas para 75 m² com inspecção visual trivial, **o custo de processamento não se paga**.

**Veredicto da secção:** nesta escala, **nenhum sensor de vegetação vale o investimento.**
São ferramentas de investigação agronómica ou de exploração agrícola de grande escala.

### 1.7 Sanidade — *Rhynchophorus ferrugineus* (o achado mais valioso desta pesquisa)

O escaravelho-vermelho-da-palmeira não mostra sintomas visuais até ser tarde de mais — a
detecção visual chega sistematicamente atrasada. A literatura tem duas décadas de trabalho
em **detecção acústica**, porque as larvas a alimentarem-se dentro do estipe produzem som:

- **Prova de conceito consolidada.** *"On the Design of a Bioacoustic Sensor for the Early
  Detection of the Red Palm Weevil"* (Sensors 13(2):1706, 2013, PMC3649424) descreve um
  sensor bioacústico autónomo, instalável por palmeira, com alarme por limiar. **Detecção
  de larvas com apenas duas semanas de idade**, com apenas 5 indivíduos, pela intensidade
  sonora à volta dos 2250 Hz.
- **Desempenho.** Protótipo bioacústico com **taxas médias de detecção superiores a 90%**
  em condições controladas.
- **Machine learning recente.** Trabalho de 2025–2026 (PMC12583683) e *fiber optic
  distributed acoustic sensing* (Sensors 21(5):1592, 2021) — a linha continua activa.
- **Produto comercial identificado, não confirmado.** O **Picusan** (Koppert) combina
  feromona de agregação + sensor com relato remoto. **Preço não apurado** — o site não
  expõe preço público, e não foi confirmada venda directa a particular em Portugal.
  Armadilhas de feromona "burras" são produto corrente na Europa a partir de poucas
  dezenas de euros — mas **essas não dão detecção precoce**, dão contagem de adultos
  capturados, que já é sinal tardio.

**Recomendação prática:**

1. **Curto prazo, garantido:** **armadilha de feromona de agregação convencional**
   (dezenas de euros, feromona substituída a cada 4–6 semanas) — vigilância de presença na
   área, não detecção precoce na árvore, mas é acção concreta e barata. Não substitui
   inspecção visual regular do colo e das folhas mais baixas.
2. **Médio prazo, a confirmar:** sensor acústico comercial na própria palmeira. **Merece
   pedido de orçamento directo ao fabricante** — não se resolve por pesquisa web, porque
   preços de equipamento fitossanitário profissional raramente estão publicados.
3. Dado que a palmeira é **«dado fixo de projecto»** (`ESTADO.md` §03) e insubstituível, o
   custo de um sensor dedicado — mesmo 200–500 € — compara-se ao custo de perder a árvore,
   pelo que **o limiar de "vale a pena" aqui é muito mais permissivo** do que em qualquer
   outro sensor deste documento.

---

## 2. Como se transmite

| Protocolo | Alcance real (com muros de alvenaria) | Consumo | Custo de infra-estrutura | Veredicto para 75 m² |
|---|---|---|---|---|
| **Wi-Fi** | Bom — o recinto tem Wi-Fi disponível | Alto (mau para bateria) | Zero adicional — já existe | **Opção por omissão.** Não há razão para gateway dedicado num espaço de 13 m coberto por Wi-Fi doméstico. |
| **ESP-NOW** | Bom; 13 m com 1–2 muros é trivial para 2,4 GHz | Muito baixo | Zero — usa o próprio ESP32 | Boa alternativa para nós a bateria, sem associar à rede doméstica |
| **Zigbee** | 2,4 GHz, penetração pior que sub-GHz, mas **rede em malha** compensa | Baixo | Dongle coordenador ~20–30 € | Adequado — ecossistema maduro para leak/porta, menos comum para sondas de solo |
| **Bluetooth / BLE** | Curto alcance, suficiente a <15 m | Muito baixo | Zero (hub por vezes necessário) | Adequado para nós próximos de um receptor (ex. Casambi) |
| **LoRaWAN** | Excelente (centenas de metros a km) | Muitíssimo baixo | Gateway dedicado 60–150 € ou rede pública | **Sobredimensionado.** O argumento de penetração é verdadeiro mas **irrelevante a 13 metros dentro do mesmo lote** — LoRaWAN resolve hectares, não quintais. Gateway para 75 m² é desperdício e mais um ponto de falha. |
| **LTE-M / NB-IoT** | Excelente, exige SIM | Baixo | Custo recorrente mensal | **Desnecessário** — há Wi-Fi no local. |
| **Matter/Thread** | Emergente, boa penetração via malha | Baixo | Borda Thread (muitos hubs já incluem) | Interessante mas **ecossistema de sensores de jardim ainda imaturo em 2026** |
| **Z-Wave** | Sub-GHz, boa penetração | Baixo | Hub dedicado | Forte em segurança doméstica, fraco em sensores de jardim |

**Conclusão:** para 13 m dentro do mesmo lote com Wi-Fi instalado, **Wi-Fi directo
(ESPHome) para os nós alimentados, e Zigbee ou BLE para nós a bateria** cobre tudo.
**LoRaWAN, NB-IoT e a maior parte da conversa "protocolo de longo alcance" é ruído de
marketing aplicado à escala errada.** Coerente com o critério do projecto: cada gateway
extra é mais um software a manter e mais uma coisa que pode ficar por fazer.

---

## 3. Onde vive a inteligência

| Plataforma | Local ou cloud | Curva | Risco de abandono | Veredicto |
|---|---|---|---|---|
| **Home Assistant** (+ ESPHome) | **Totalmente local**, self-hosted | Média | Open source, comunidade grande, sem empresa única | **Recomendado como núcleo.** Sobrevive à falência de qualquer fabricante de sensores, porque a integração é por protocolo aberto (MQTT/Zigbee), não por API proprietária. A HA 2025.12 já tem vista dedicada de irrigação. |
| **Node-RED** | Local | Alta liberdade | Open source | Complementar; **opcional** a esta escala |
| **openHAB** | Local | Semelhante ao HA | Open source | Alternativa válida; sem razão forte para preferir |
| **ESPHome** | Local, firmware no ESP32/8266 | Baixa — config YAML declarativa | Projecto irmão da HA | **Peça-chave**: transforma um micro de 3–8 € num sensor Wi-Fi nativo da HA, sem código à mão |
| **Arduino puro** | Local | Alta (C++ manual) | N/A | Mais trabalho manual que ESPHome para o mesmo resultado |
| **Raspberry Pi** | Local | Baixa com imagens prontas | N/A | **Servidor recomendado** — ~60–90 €, sem preço PT apurado |
| **ThingsBoard / InfluxDB+Grafana** | Local ou cloud | Alta — infra de séries temporais industrial | Depende | **Excesso para 75 m².** Brilham com centenas de sensores; aqui seriam brinquedo técnico sem retorno. |
| **Adafruit IO** | Cloud | Baixa | Serviço de terceiro, histórico gratuito→pago | Evitar como dependência crítica |
| **Rachio / Hydrawise / Netro / Gardena smart** | **Cloud obrigatória** para a maioria das funções | Muito baixa — plug-and-play | **Alto.** Hydrawise teve mudanças de modelo de negócio; qualquer destes é uma app e um servidor que podem fechar | Usar **só o controlador de válvulas** (hardware robusto) **mas não a nuvem** — preferir controlar as válvulas a partir do Home Assistant (Shelly + relé, ou controladores genéricos ESPHome). |

**Princípio central, alinhado com o histórico do projecto:** *«Um sistema que morre quando
o fabricante fecha o serviço é um passivo.»* Home Assistant + ESPHome não têm esse risco.
Qualquer sistema comercial de rega deve ser avaliado **pela qualidade do hardware de
válvula, não pela app** — e mesmo assim, preferir que a válvula seja controlável por relé
genérico, para não ficar refém.

---

## 4. O que se acciona

### 4.1 Rega

| Componente | Opção | Preço (PT/EU, 2026) |
|---|---|---|
| Electroválvula 24V, 1" | Rain Bird HV-100 | **21,80 €** (Hidraulicart.pt, 2026) |
| Electroválvula 24V, 1" | Hunter PGV-100 | Casa Alves; preço não apurado |
| Controlador multi-zona | Relé + transformador 24V via ESPHome, ou controlador comercial | DIY: dezenas de euros; comercial: 80–200 € |
| Gota-a-gota / micro-aspersão | Kits Netafim/Rain Bird (Riegopro, Hidraulicart) | Variável, não totalizado |
| Rega subsuperficial | Tubos exsudantes enterrados no substrato | Mesma gama + mão-de-obra |

**Gota-a-gota vs micro-aspersão vs subsuperficial, em substrato de 0,50 m:** a
subsuperficial (ou gota-a-gota rasteiro coberto por mulch) é preferível à micro-aspersão em
clima mediterrânico, porque reduz evaporação directa — **num volume de solo tão pequeno,
cada litro perdido por evaporação é proporcionalmente mais caro** do que em solo natural.

**Rega por ETo vs por sensor de humidade vs por temporizador?**

- **Temporizador simples:** falha exactamente quando mais importa — um Agosto anormalmente
  quente rega o mesmo que um Agosto ameno, e num substrato de 0,50 m a margem de erro é de
  dias. **Não chega sozinho.**
- **ETo (evapotranspiração de referência):** método do Hydrawise, que em testes de
  terceiros regou **10–15% menos água que Rachio** em condições idênticas. Tecnicamente o
  mais correcto **quando bem calibrado**. Mas depende de um coeficiente de cultura (Kc) que
  **não existe calibrado para "mix mediterrânico em substrato leve de 50 cm"** — os
  coeficientes publicados são para relva ou culturas agrícolas em solo profundo. **Não é
  "ligar e esquecer".**
- **Sensor de humidade com limiar:** em substrato fino, **responde mais depressa ao que
  está a acontecer no volume real** — mede directamente a variável que importa. Desvantagem:
  fiabilidade do sensor e necessidade de um por zona hidrologicamente distinta.

**Recomendação:** **sensor de humidade como gatilho primário, temporizador como rede de
segurança dupla** — rega se a humidade cair abaixo do limiar, mas **nunca passa X dias sem
regar** mesmo que o sensor pareça OK. Protege contra sensor avariado a dar leitura
falsa-húmida. ETo fica como refinamento posterior, não como base.

### 4.2 Fertirrega

- **Injectores venturi passivos:** 30 USD (básico) a 80–400 USD com filtro e válvulas; kits
  "EZ-FLO" domésticos 90–250 USD.
- **Dosatron "Hobby Unit"** (doseamento proporcional sem electricidade): **3.799 € com
  IVA** (SaltonVerde) — **claramente desproporcionado** para 75 m².
- **Controladores EC/pH automáticos** (Bluelab, TrolMaster): centenas de euros, pensados
  para hidroponia/cultivo indoor.

**Veredicto: fertirrega automatizada é exagero a esta escala.** Um jardim mediterrânico de
75 m² beneficia de adubação de fundo lenta e reforços pontuais manuais 2–4×/ano — não de
doseamento contínuo. O caso de uso é cultivo intensivo de alta rotação, não jardim
ornamental. **Não recomendado**, nem na configuração "completa" — é o único accionador que
se corta por inteiro do documento.

### 4.3 Iluminação cénica

| Protocolo | Robustez para cenas complexas | Complexidade de manutenção |
|---|---|---|
| **DALI (DALI-2)** | **Benchmark profissional**, linha até 250 m, endereçamento individual robusto | Driver DALI em cada luminária + gateway — investimento inicial maior, mas **extremamente estável**, sem dependência de rede sem fios |
| **Casambi** (BLE) | Cenas complexas, temporizador ou manual, "reliable, scalable, fully configurable" | Alcance **80 m** (vs 250 m do DALI) — num recinto de 13 m não é limitação prática. App própria, mas protocolo suficientemente aberto |
| **Zigbee** (Hue/Tradfri via HA) | Cenas simples a médias; malha pode saturar com tráfego elevado | Mais barato e integrado directamente na HA sem gateway proprietário |
| **DMX** | Standard de espectáculo, altíssima capacidade dinâmica | **Excesso** para jardim residencial — produção de eventos, cablagem própria |
| **KNX** | Automação de edifício, muito robusto | Instalador certificado — **desproporcionado** só para jardim |

**Um projecto real (Giardino Palazzo Pfanner) combinou DALI fixo para projectores
arquitectónicos com Casambi sem fios para a iluminação decorativa** — precedente directo
para «vê-se a luz, nunca a luminária» com ambição cénica: **DALI cablado para os pontos
fixos e permanentes (a palmeira), Casambi para o que precisa de flexibilidade.** Zigbee via
HA é a opção mais barata, mas com tecto de complexidade mais baixo para coreografias de
«duas estações» (dia/noite) do princípio #5.

### 4.4 Sombreamento e protecção

Toldos e velas motorizados existem em Zigbee/KNX/Somfy io-homecontrol — tecnologia madura
de estores, sem particularidade de jardim. Não aprofundado por não haver indicação de que
sombreamento motorizado seja necessidade confirmada (a sombra do recinto é
predominantemente estrutural — muros e copas). **Fica como buraco declarado.**

### 4.5 Alertas — quando avisar em vez de agir sozinho

Regra: **actuar onde o erro é reversível e barato; avisar onde o erro é caro, irreversível,
ou exige julgamento que o sistema não tem.**

| Situação | Actuar sozinho | Só alertar |
|---|---|---|
| Humidade abaixo do limiar, dentro da janela horária | ✅ Rega | |
| Chuva nas últimas 24h acima de um limiar | ✅ Salta o ciclo | |
| Sensor com leitura implausível (0% ou 100% persistente) | | ✅ Sensor avariado — não confiar na decisão automática |
| Fuga de água detectada | | ✅ Alertar já — fechar a válvula geral **é** accionável, mas fechar água a um jardim com árvores vivas por engano é erro caro na direcção oposta; prefere-se confirmação humana rápida |
| Suspeita de RPW (sensor acústico acima do limiar) | | ✅ Sempre — nunca há acção automática sensata para um escaravelho na palmeira |
| Três meses sem interacção do utilizador | | ✅ Sinal de abandono do próprio sistema — ver §8 |

---

## 5. Estratégias de controlo

| Estratégia | Onde compensa | Onde não compensa |
|---|---|---|
| **Limiar simples** | Sempre — base de qualquer automação fiável e a mais fácil de depurar | — |
| **ETo com estação própria** | Se já se tem estação por outra razão — dá ajuste sazonal automático | Exige Kc calibrado, que não existe para este substrato — **compensa como refinamento, não como base** |
| **ETo via API meteorológica** | Mais simples de manter (sem sensores a limpar), boa aproximação para Lisboa | Não capta o **microclima do próprio quintal** — que o dossier já demonstrou ser muito diferente do exterior |
| **Controlo preditivo com previsão** (salta rega se prevista chuva >X mm) | Vale a pena — automação de duas linhas em HA, baixíssima manutenção | — |
| **Aprendizagem automática / ML** | Praticamente nunca, a esta escala | **A complexidade deixa de compensar exactamente aqui.** Precisa de meses de dados rotulados e de alguém a validar que não aprendeu um padrão errado. Para 75 m² com meia dúzia de zonas, **um humano a ajustar dois ou três limiares duas vezes por ano supera qualquer ML** em fiabilidade e esforço. |

**Onde a complexidade deixa de compensar, dito directamente:** no momento em que o sistema
passa a exigir que alguém interprete um dashboard ou ajuste um modelo estatístico para
saber se deve confiar na próxima rega. **Este projecto já perdeu quatro planos por depender
de coisas que "iam acontecer"** — um sistema de rega preditiva por aprendizagem é
exactamente esse tipo de coisa.

---

## 6. Três configurações completas

### (a) Mínima honesta

**Objectivo:** a menor instrumentação que já produz uma decisão diferente da que se tomaria sem ela.

| Item | Especificação | Preço estimado |
|---|---|---|
| 3× sensor de humidade capacitivo | Um por zona hidrológica distinta | 3 × 18,50 € ≈ **55 €** |
| Nós ESPHome (ESP32 + alimentação) | Wi-Fi doméstico existente | ≈15–25 €/nó × 2–3 ≈ **40–60 €** |
| 1× sensor de fuga (Aqara/SONOFF, Zigbee) | Junto ao ponto de alimentação de água | ≈**12–26 €** |
| 1× dongle Zigbee USB | Coordenador para HA | ≈**20–30 €** |
| Home Assistant | Hardware existente ou Raspberry Pi | **0 a ≈70 €** |
| Electroválvula(s) por relé | 1–2 zonas, Rain Bird HV-100 | ≈**22–44 €** |
| **Total material** | | **≈ 150–260 €** |
| **Tempo de instalação** | | Um fim-de-semana |
| **Manutenção anual** | | Recalibração (≈1h), verificação de firmware (≈1h), sem assinaturas |

**O que dá:** sabe-se com confiança quando regar cada zona, e recebe-se aviso de fuga. Sem
iluminação cénica nem detecção fitossanitária — é a base que evita o erro mais caro (matar
plantas por rega errada num substrato fino).

### (b) Equilibrada — recomendada

| Item | Especificação | Preço estimado |
|---|---|---|
| Tudo de (a) | | ≈ 150–260 € |
| Estação meteorológica (Ecowitt/Bresser) | **Preço concreto não apurado** — gama citada 80–200 € | ≈ **80–200 €** *(não apurado)* |
| Sensor lux (BH1750) × 3–4 + 1 PAR de referência emprestado para calibração única | | ≈ **20–40 €** |
| Sensor SHT40 (T + HR) × 1–2 | | ≈ **20–30 €** |
| Electroválvulas até cobrir todas as zonas (3–4) | Rain Bird HV-100 | ≈ **65–87 €** adicionais |
| Kit gota-a-gota/subsuperficial | Netafim/Rain Bird | ≈ **100–200 €** *(depende de metragem)* |
| Armadilha de feromona RPW (vigilância) | Feromona 2–3×/ano | ≈ **30–60 €** + ≈**20–40 €/ano** |
| **Total material** | | **≈ 460–800 €** + rega conforme metragem |
| **Tempo de instalação** | | Um a dois fins-de-semana |
| **Manutenção anual** | | Recalibração (≈2h), limpeza de pluviómetro (≈1h, 2×/ano), feromona (≈15min, 3×/ano), **sem assinaturas de cloud** |

**Porquê esta é a recomendação:** cobre humidade (o parâmetro mestre), luz por zona (a
variável mais desigual no espaço), clima local, e vigilância mínima da palmeira — sem
entrar em fertirrega, sensores de vegetação ou detecção acústica dedicada. É a configuração
que melhor cumpre «o que sobrevive ao abandono»: tudo local, sem assinatura, sem app
obrigatória de terceiro.

### (c) Completa — tudo o que faz sentido, sem ser ficção

| Item | Especificação | Preço estimado |
|---|---|---|
| Tudo de (b) | | ≈ 460–800 € |
| Sensor acústico dedicado à palmeira (Picusan ou equiv.) | **Preço não apurado** — pedido de orçamento necessário | *(estimativa qualitativa: algumas centenas de euros)* |
| Sensor de nível para pond/piscina | Ultrassónico impermeável | ≈ **20–40 €** |
| Sensor de humidade de parede | Produto dedicado não confirmado | *(não apurado)* |
| Hub Casambi para iluminação cénica | | ≈ **60–150 €** |
| Iluminação DALI (pontos fixos) + Casambi (resto) | Depende do número de luminárias | *(não orçamentado — pertence a pesquisa de iluminação dedicada)* |
| **Total adicional face a (b)** | | **Não totalizável com confiança** — os dois itens de maior peso não têm preço apurado |

**Nota de honestidade:** esta configuração é «tudo o que faz sentido», não «tudo o que
existe no catálogo» — **exclui deliberadamente** fertirrega automatizada (§4.2), fluxo de
seiva/dendrómetros (§1.6) e NDVI, por serem investigação ou desproporção, não por esquecimento.

---

## 7. O que NÃO vale a pena medir

Critério: **um parâmetro só vale a pena medir se mudar uma acção.**

1. **CO2 do ar exterior** — não há acção possível num jardim aberto.
2. **pH de substrato em contínuo** — a sonda degrada-se depressa e a correcção de pH é
   intervenção rara, não decisão diária. Kit manual 1–2×/ano.
3. **Fluxo de seiva e dendrómetros** — sinal fisiológico fino, excelente para investigação,
   mas não muda nenhuma decisão que «humidade de substrato + inspecção visual» já não desse.
4. **NDVI/multiespectral** — a área é pequena o suficiente para a inspecção visual
   substituir integralmente o sensor.
5. **VPD medido em contínuo** — ao ar livre não há actuador que responda a VPD que não
   responda melhor a humidade de substrato. Calcula-se por curiosidade, não se actua.
6. **Fertirrega por sensor EC/pH contínuo** — escala e tipo de plantação não o justificam.
7. **Vento em contínuo com actuação automática** — o recinto é estruturalmente abrigado; a
   informação vem grátis com a estação, mas **não justifica sensor dedicado isolado**.
8. **Temperatura de solo separada da humidade** — informativa, raramente muda uma decisão
   isolada em Lisboa; vem grátis nos sensores "3-in-1", mas não justificaria compra própria.

---

## 8. Modos de falha

**O critério que separa «mata plantas» de «só irrita»: o erro acontece num sistema com
reserva (solo profundo, tempo de reacção) ou sem reserva (substrato de 0,50 m sobre laje)?**

| Falha | Consequência | Classe |
|---|---|---|
| **Wi-Fi cai, rega automática não dispara em Agosto** | Substrato de 0,50 m seca em **dias**, não semanas | **MATA** |
| **Sensor avaria preso a "húmido" (falso positivo permanente)** | Sistema nunca rega porque «acha» que está húmido — sem alarme de rede a avisar | **MATA — e é a mais perigosa, porque parece que está tudo bem** |
| **Sensor avaria preso a "seco"** | Rega em excesso contínua — sobre laje impermeável **acumula sem drenar**, asfixia radicular e sobrecarga de peso não planeada | **MATA, mais devagar** |
| **Utilizador ignora o sistema 3 meses** | Com rede de segurança por temporizador, sobrevive; sem ela e com sensor derivado silenciosamente, falha sem ninguém notar | **MATA sem rede de segurança; só IRRITA com ela** |
| **Cloud do fabricante descontinuada** | Com fallback local, perde-se conveniência; se o hardware só funcionar via cloud, **perde-se a rega inteira** | **MATA se a dependência for total** |
| **Sensor de fuga não detecta fuga lenta** | Infiltração continua sem alarme — problema de meses/anos | **Só IRRITA a curto prazo; pode MATAR o edifício a longo prazo** |
| **Dongle Zigbee falha** | Sem alarme de fuga até inspecção manual | **Só IRRITA** |
| **Falso alarme do sensor acústico** | Inspecção manual desnecessária | **Só IRRITA** |
| **Pluviómetro avaria e nunca regista chuva** | Rega a mais em dias de chuva — desperdício, não morte | **Só IRRITA** |

**A implicação mais importante desta secção:** **nenhum sistema de rega totalmente
automática, sem rede de segurança por temporizador, é seguro para este substrato.** A
combinação recomendada em §4.1 não é capricho de engenharia — é a única forma de garantir
que uma falha silenciosa de sensor não se transforma em morte de planta em Agosto.

---

## 9. Faseamento

### Antes da obra (T004) — porque depois fica caro ou impossível

- **Condutas de rega e cabos de baixa tensão sob o substrato**, com saída por zona
  hidrológica — decidir o zonamento de rega **ao mesmo tempo** que a T004 decide a
  geometria, não depois. Depois de impermeabilizada e coberta, abrir valas é obra a refazer.
- **Tomadas de água e electricidade próximas de cada zona**, para evitar cabos à superfície.
- **Ponto de passagem através do muro ou da transição casa-jardim**, para sensor de humidade
  de parede e sondas embutidas.
- **Conduta vazia de reserva** — mesmo sem decidir hoje que sensor vai lá, custa quase nada
  agora e evita levantar tudo daqui a um ano.
- **Posição do sensor acústico na palmeira** — não é obra civil, mas deve ficar decidido
  antes da plantação para não ser esquecido.

### Depois — sem custo de obra

- Todos os sensores sem fio (humidade, luz, T/HR, fuga).
- Estação meteorológica — mastro/suporte, sem interferência com a laje.
- Iluminação Casambi (sem fios) — a qualquer momento; **DALI cablado, não** — esse decide-se
  e cabla-se durante a obra, tal como a rega.
- Ajustes de software (HA, automações, limiares).
- Sensor acústico RPW — instalável sem intervenção na laje, mas **decidir o ponto de
  alimentação eléctrica perto da palmeira antes da obra**, se não for só a bateria.

---

## 10. Buracos — o que não foi apurado

1. **Preço do Picusan (Koppert) ou equivalente de detecção acústica de RPW.** Sem preço
   público; necessário orçamento directo. Não confirmado se há venda a particular em Portugal.
2. **Preço PT concreto de estação Ecowitt/Bresser** com pluviómetro e anemómetro.
3. **Produto dedicado e preço para sensor de humidade embutido em alvenaria** — a maior
   parte do mercado é detecção por imersão, não humidade capilar em parede.
4. **Preço concreto de Raspberry Pi em loja portuguesa em 2026.**
5. **Coeficiente de cultura (Kc) para vegetação mediterrânica em substrato leve de 0,50 m** —
   não existe tabela publicada para este cenário; qualquer ETo terá de partir de aproximação
   e ajuste empírico.
6. **Cobertura de rede LoRaWAN pública em Alcântara** — não verificada, mas também não
   necessária dada a recomendação.
7. **Preço de kits de rega dimensionados à metragem exacta** — depende da geometria que a
   T004 ainda está a fechar.
8. **Peso admissível na laje para os equipamentos mais pesados** (mastro de estação,
   elemento de água) — cruza com `ESTADO.md` §05 sobre carga da piscina. Esta pesquisa não
   avaliou peso de equipamento, só de sensores, que são desprezáveis.
9. **Compatibilidade DALI-Casambi com o catálogo de luminárias que vier a ser escolhido** —
   a combinação é viável e tem precedente, mas não se avaliaram luminárias específicas.

---

## Cruzamento com a T003 (modelo solar)

Esta pesquisa **não contradiz nem se sobrepõe à T003.** A T003 trata de modelação e
simulação preditiva de sol/sombra; este documento trata de sensores físicos e actuadores em
tempo real. O único ponto de contacto é o **sensor lux por zona (§1.3)**, que poderia servir
para *validar* o modelo solar da T003 contra medição real — mas isso é proposta para a fase
2, não decisão desta pesquisa. **Não é recomendação de engolir, complementar ou substituir a
T003** — é nota de fronteira, deixada explícita como a mensagem de abertura pediu.
