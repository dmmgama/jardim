# Software para modelar um quintal urbano e a sua exposição solar
## Relatório de investigação — Calçada da Boa Hora 15, Alcântara

**Data:** 15 de Setembro de 2026
**Destinatário:** proprietário tecnicamente competente, Windows
**Pergunta operacional:** obter DLI (mol/m²/dia) por zona e por estação, num quintal de 75 m² fechado por uma fachada de 15,50 m a NE e três muros de 2,50 m

**Convenção de marcação:** **[F]** facto verificado com fonte · **[M]** preço ou valor de mercado · **[E]** estimativa ou juízo meu

---

## 1. Veredicto de abertura

### 1.1 A resposta curta

**Sim, existe software que responde de facto à pergunta do DLI.** Não é o Blender, não é o SketchUp, não é o Google Earth. É **Radiance**, acedido através de **honeybee-radiance em Python puro** — e existe uma segunda via, mais simples de instalar, através do **UMEP/SEBE no QGIS**.

Mas há uma ressalva que tenho de pôr à frente de tudo, porque muda a natureza da recomendação:

> **Nenhum destes programas produz mol/m²/dia directamente.** Todos produzem irradiância solar em **W/m²** ou irradiação acumulada em **kWh/m²**. A passagem para DLI é uma multiplicação por um factor de conversão espectral que **o utilizador tem de aplicar à mão, e que carrega a sua própria incerteza de ±10 a 15%** [E]. Isto não é defeito do software — é que a comunidade de simulação de edifícios mede energia e a comunidade de horticultura mede fotões, e ninguém construiu a ponte.

O factor é este [F]:

```
PPFD (µmol/m²/s) = Irradiância global (W/m²) × f_PAR × J_to_mol
```

onde `f_PAR` ≈ 0,45–0,50 (fracção energética da radiação solar entre 400–700 nm) e `J_to_mol` ≈ 4,6 µmol/J. O produto combinado usado por omissão no package R `bigleaf` é **2,3 µmol/J** (com f_PAR = 0,5) [F, [bigleaf Rg.to.PPFD](https://search.r-project.org/CRAN/refmans/bigleaf/html/Rg.to.PPFD.html)]. A literatura medida dá valores mais baixos: **2,02 mol/MJ em Março e 2,19 mol/MJ em Junho, com f_PAR de 0,45 a 0,48** [F, [Springer, estudos de fFEC](https://link.springer.com/article/10.1007/s00704-010-0368-6)].

**Implicação prática, e é importante:** conforme escolhas 2,02 ou 2,3, o teu DLI varia 14%. Para um valor de ~25 mol/m²/dia isso são ±3,5 mol. Como os teus limiares de decisão são 10 e 15 mol, e a estimativa está nos 25–28, **esta incerteza não te muda a decisão de Verão**. Mas para o Inverno, onde estás a comparar contra 6,7 mol da *Zoysia* 'JaMur', 14% pode ser a diferença entre serve e não serve. [E]

### 1.2 O que recomendo, concretamente

**Recomendo uma combinação de duas ferramentas, por esta ordem:**

**Passo A — `pvlib` + PVGIS com perfil de horizonte (2 a 4 horas de trabalho).** Isto é a via mínima e produz um número defensável de DLI **hoje**. Não modelas geometria 3D nenhuma: converte a tua geometria de muros num **perfil de horizonte em graus por azimute** (que já sabes calcular — tens a trigonometria feita) e alimenta-o ao PVGIS, que devolve séries horárias de radiação directa, difusa e refletida já com esse horizonte aplicado [F, [PVGIS hourly radiation](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/pvgis-tools/hourly-radiation_en)]. Depois somas por dia e multiplicas pelo factor PAR.

**Passo B — Radiance via honeybee-radiance, em Python, sem Rhino (12 a 25 horas).** Isto é o que te dá o que o passo A não dá: **a difusa anisotrópica correctamente obstruída pela geometria real, mais a reflexão dos muros e da fachada, mais as copas com transmissividade sazonal**. É o padrão-ouro e é gratuito.

**Porque não uma só?** Porque o passo A é rápido e serve de sanidade ao passo B. Se os dois divergirem mais de 20%, um dos dois está mal montado — e é assim que descobres qual. [E]

### 1.3 E o medidor de DLI? A resposta honesta

**Compra-o. Mesmo que faças a simulação.** 

Não porque o software falhe, mas porque o software resolve a tua incerteza **geométrica** (a difusa obstruída) e **não** resolve a tua incerteza **espectral** (o factor PAR) nem a **atmosférica local** (a poluição de Lisboa, a névoa do Tejo, a sujidade nas folhas). Um medidor resolve as três de uma vez, porque mede fotões PAR reais no ponto real.

O aparelho certo não é o LightScout DLI 100 — é o **Apogee DLI-500, a 499 USD (≈460 €)**, que mede PAR, DLI e fotoperíodo, **armazena 99 dias de leituras automaticamente**, tem incerteza de calibração de **±5%** e deriva inferior a 2%/ano, com rastreabilidade NIST [F, [Apogee DLI-500](https://www.apogeeinstruments.com/dli-500-par-daily-light-integral-and-photoperiod-meter-full-spectrum-400-700-nm/)]. O LightScout 3405G custa entre 99 e 300 USD [M, [fonte retalhista](https://lighlumete.com/3405g)] mas não tem a mesma especificação de incerteza publicada.

**O trade-off real, dito sem rodeios:**

| | Simulação | Medição |
|---|---|---|
| Quando tens resposta | Esta semana | Junho de 2027, para ter Verão e Inverno |
| Custo | 0 € + 15–30 h do teu tempo | ≈460 € + 14 dias de logging |
| Incerteza no DLI | ±20–30% [E] | ±5% instrumental [F] |
| Resolve a difusa obstruída | Sim (Radiance) | Sim, por medição directa |
| Resolve o factor PAR | Não | Sim |
| Dá-te mapas por zona | Sim, 5 zonas de uma vez | Uma zona por posição de sensor |
| Serve para outra coisa | Sim — desenho, iluminação nocturna | Não |

**A jogada que recomendo:** encomenda o medidor **agora** e faz a simulação **enquanto ele não chega**. O medidor chega em duas semanas; põe-no na plataforma central durante 7 dias de Setembro/Outubro. Setembro não é Junho nem Dezembro, mas **valida a tua simulação contra um número real**, e a partir daí confias na simulação para extrapolar as estações que não mediste. Isto é o melhor dos dois mundos e custa-te 460 € e nenhum mês de espera. [E]

Há um argumento adicional para não esperares por Junho: **a decisão de relva não é reversível de graça.** Se plantares errado, perdes a época e o custo da instalação. 460 € é barato comparado com refazer um relvado de 40 m². [E]

---

## 2. Open source — investigação detalhada

### 2.1 Blender + Sun Position (nativo)

**O que é.** O Sun Position é um add-on **incluído de origem no Blender** (não precisa de download), que posiciona o sol por latitude, longitude, data, hora e fuso. Baseia-se na calculadora online da NOAA, que por sua vez implementa os algoritmos astronómicos de Jean Meeus [F, [Blender Manual — Sun Position](https://docs.blender.org/manual/en/2.83/addons/lighting/sun_position.html)]. Está publicado também como extensão no repositório oficial [F, [extensions.blender.org](https://extensions.blender.org/add-ons/sun-position/)].

**Precisão.** Boa. Existe um artigo SAE de 2024 que **validou o sistema solar do Blender para reconstrução de sombras em peritagem de acidentes** [F, [SAE 2024-01-2476](https://www.sae.org/publications/technical-papers/content/2024-01-2476/)] — se serve para prova forense, serve para o teu quintal. Há também um relato independente de verificação contra um relógio de sol real [F, [lacuisine.tech](https://lacuisine.tech/checking-a-sundials-accuracy-in-blender/)]. A posição solar é o problema fácil; qualquer implementação decente de Meeus dá <0,1° de erro.

**Esforço de modelação para o teu caso.** Baixo. Um rectângulo de 13,00 × 5,78 m e quatro paredes extrudidas fazem-se em Blender em **30 a 60 minutos** com cotas exactas (o Blender aceita valores numéricos directos em metros nos campos de transformação). A varanda em consola são outros 15 minutos. [E]

**O problema, e é fatal para o teu objectivo.** O Blender + Sun Position produz **imagens e animações**. Não produz uma tabela. Não te dá "3,4 horas de sol no ponto X=4, Y=3". Não te dá W/m². Para obter horas de sol tinhas de renderizar N frames e contar píxeis iluminados por zona — o que é possível mas é *scripting* de processamento de imagem, não simulação física. E **não** te dá difusa nem refletida em unidades físicas, porque o Cycles é um renderizador espectralmente normalizado para aparência, não um radiómetro calibrado.

**Veredicto:** **2 horas para uma visualização bonita e uma verificação qualitativa de sombras. Zero para DLI.** [E] Vale como ferramenta de comunicação e para o projecto de desenho, não como instrumento de medida.

### 2.2 VI-Suite — a descoberta mais útil deste relatório

**Isto muda a avaliação do Blender por completo.** O VI-Suite é um add-on que transforma o Blender num **pré/pós-processador para Radiance e EnergyPlus** [F, [VI-Suite](https://blogs.brighton.ac.uk/visuite/)].

**O que faz, nas palavras da documentação:** análises Radiance estáticas e paramétricas para simulação e visualização de **factor de luz do dia, iluminância e irradiância**, mais Climate Based Daylight Modelling. Os resultados são visualizáveis na cena Blender, **plotáveis e exportáveis para CSV** [F]. É GPL v2, gratuito e multiplataforma [F].

**Está vivo?** Sim, e é raro encontrar um add-on de nicho tão mantido. Há posts no blogue oficial referindo compatibilidade com **Blender 4.4 (Março de 2025)** e existe um repositório **vi-suite07 explicitamente "VI-Suite release for Blender 5.1 (experimental)"**, com 597 commits, 47 estrelas e 10 forks [F, [github.com/rgsouthall/vi-suite07](https://github.com/rgsouthall/vi-suite07)]. O autor é Ryan Southall, da Universidade de Brighton. Há também entrada na wiki OSArch [F, [wiki.osarch.org](https://wiki.osarch.org/index.php?title=VI-Suite)].

**Porque é que isto é atraente para ti especificamente.** Modelas a geometria no Blender (fácil, visual, cotado, 1 hora), incluindo as copas da palmeira e do lodão como malhas com material de transmissividade, e obténs **irradiância em W/m² num grid de pontos, em CSV**. É o Radiance com interface gráfica e sem Grasshopper nem Rhino. E o mesmo modelo Blender serve depois para a iluminação cénica nocturna.

**As reservas.** [E] O VI-Suite é software académico de um só autor. A documentação é um PDF. A comunidade é pequena (47 estrelas não é uma multidão) e se encalhares num erro obscuro pode não haver ninguém que responda. Estimo **8 a 15 horas** até ao primeiro resultado de irradiância credível, das quais metade em instalar o Radiance no Windows e descobrir a ordem correcta dos nós.

**Veredicto:** **candidato sério, e a melhor via se quiseres um só modelo para análise solar e para desenho/iluminação.** Ver secção 9, via C.

### 2.3 Ladybug Tools — a família certa, mas atenção a qual porta usas

Esta é a família que resolve o teu problema, mas há **três portas de entrada e duas delas não servem**. Vale a pena separá-las com cuidado porque é aqui que a maior parte dos conselhos online se engana.

#### Porta 1 — Grasshopper/Rhino: funciona, mas é paga
O caminho canónico. Rhino 8 custa **995 €** em licença perpétua para um utilizador na Europa [M, [Rhino Europe pricing](https://www.rhino3d.com/sales/europe/)]. O Grasshopper vem incluído e o Ladybug/Honeybee são gratuitos. Tem os componentes exactos que precisas: **Direct Sun Hours** (calcula horas de sol directo num grid subdividido sobre a geometria, com grid size configurável) [F, [Ladybug Primer — Direct Sun Hours](https://docs.ladybug.tools/ladybug-primer/components/3_analyzegeometry/direct_sun_hours)] e **Incident Radiation** (irradiação incidente, com nota explícita de que incluir geometria de solo bloqueia a reflexão grosseira do solo) [F, [Ladybug Primer — Incident Radiation](https://docs.ladybug.tools/ladybug-primer/components/3_analyzegeometry/incident_radiation)]. Existe ainda a receita **Annual Irradiance** do Honeybee-Radiance [F, [HB-Radiance Primer](https://docs.ladybug.tools/hb-radiance-primer/components/3_recipes/annual_irradiance)].

#### Porta 2 — Ladybug para Blender: NÃO SERVE, e é importante saber porquê
Existe o repositório oficial `ladybug-tools/ladybug-blender`, que usa a interface de scripting visual **Sverchok**. Mas o próprio README avisa: *"We're slowly releasing an incomplete, alpha state version"*. E, decisivo: **"These nodes are _only_ Ladybug for now. You will not find Honeybee, Dragonfly, or Butterfly."** Tem 53 estrelas, 49 commits, e a última release datada é de **29 de Maio de 2024** [F, [ladybug-tools/ladybug-blender](https://github.com/ladybug-tools/ladybug-blender/)].

**Tradução:** sem Honeybee não há Radiance. Sem Radiance não há irradiância, não há difusa obstruída, não há DLI. **Esta porta está fechada para o teu objectivo.** Se leres num fórum que "há Ladybug para Blender", é verdade mas é irrelevante — usa o VI-Suite em vez disso.

#### Porta 3 — Python puro, sem Rhino: FUNCIONA, e é a que recomendo
Esta é a via que responde à tua pergunta e é gratuita. Os packages estão todos no PyPI sob a organização `ladybug-tools` [F, [PyPI ladybug-tools](https://pypi.org/user/ladybug-tools/)]:

- `ladybug` — dados climáticos, posição solar, EPW
- `honeybee` — modelo, descrito como "a python library to create, run and visualize radiance studies", com nota explícita de que **pode ser implementada em Python puro** [F, [ladybug-tools/honeybee](https://github.com/ladybug-tools/honeybee)]
- `honeybee-radiance` — "adds Radiance simulation functionalities to honeybee for daylight/radiation simulation" [F, [PyPI honeybee-radiance](https://pypi.org/project/honeybee-radiance/1.66.106)]
- `lbt-honeybee` — o meta-package que instala tudo

**Instalação em Windows, concreta e verificada:**
1. Instalar o Radiance em `C:\Radiance` (executável oficial) [F]
2. `pip install lbt-honeybee`
3. Verificar com `honeybee-radiance --help` [F, [DeepWiki — Installation and Setup](https://deepwiki.com/ladybug-tools/honeybee-radiance/1.1-installation-and-setup)]

O package procura automaticamente o Radiance nas localizações comuns, mas pode ser necessário configurar caminhos à mão [F]. Requer Python 3.6+ [F].

**Reserva honesta.** [E] A API Python pura é **documentação-pobre comparada com a documentação dos componentes Grasshopper**. O tutorial de prova de conceito que existe (`AntoineDao/lbt-honeybee-tutorial`) tem **0 estrelas e 0 forks**, é sobre LEED a partir de gbXML, e está aparentemente inactivo [F, [repo](https://github.com/AntoineDao/lbt-honeybee-tutorial)]. Vais escrever código lendo *docstrings* e o código-fonte dos componentes Grasshopper (que são Python e estão no GitHub — é aí que aprendes a sequência de chamadas). Estimo **12 a 25 horas** para quem sabe Python mas nunca viu Honeybee. Contra 4 a 8 horas se tivesses Rhino.

**Sobre o "workflow LEED/Radiance" que perguntaste.** LEED é uma certificação de sustentabilidade de edifícios; o seu crédito de luz natural exige provar que X% da área ocupada atinge iluminância entre 300 e 3.000 lux em determinadas horas. Isso gerou toda uma indústria de simulação Radiance com regras fixas. **Para ti é irrelevante** — é sobre lux dentro de salas, não sobre mol/m²/dia num jardim. Mencionei-o só para dizeres que não é o caminho: os *workflows* prontos que encontrares online estão sintonizados para interiores e para lux. O teu caso é *outdoor* e irradiância. [E]

**Fiabilidade do Radiance por baixo.** É o padrão-ouro e tem validação publicada. O Radiance está validado contra os casos analíticos da norma **CIE 171:2006** [F]. Validações empíricas contra medições dão **erro médio absoluto <13% e RMSE <23%** nos melhores casos, com margens aceites na indústria de **20% de Mean Bias Error e 32% de RMSE** [F, [Taylor & Francis, validação experimental](https://www.tandfonline.com/doi/full/10.1080/15502724.2024.2365691); [ScienceDirect, validação empírica de Ladybug e Honeybee](https://www.sciencedirect.com/science/article/abs/pii/S0038092X20307866)]. Nota digna de registo para o teu caso: um estudo concluiu que **a componente difusa é simulada com mais exactidão que a directa** [F, [Academia.edu](https://www.academia.edu/36795005/)] — precisamente ao contrário do teu cálculo analítico, e é exactamente por isso que valem a pena.

**Alerta relevante da literatura:** *"there is no scientific basis for industry-accepted parameter settings"* [F, mesma fonte] — os parâmetros `-ab`, `-ad`, `-as` do Radiance influenciam o resultado e não há valores canónicos. Num espaço com muros reflectores como o teu, o número de *ambient bounces* (`-ab`) importa muito. Usa `-ab 3` ou superior e faz um teste de sensibilidade. [E]

### 2.4 Radiance directamente, em linha de comandos

**O que é.** O motor de *raytracing* fisicamente correcto do Lawrence Berkeley National Laboratory, em desenvolvimento desde os anos 80. A cadeia relevante para ti seria: `gendaylit` (gera descrição do céu a partir de irradiância medida, usando os modelos de Perez para as componentes directa e difusa) [F, [NREL/Radiance gendaylit.c](https://github.com/NREL/Radiance/blob/master/src/gen/gendaylit.c)] → `oconv` (compila a cena) → `rtrace` (traça raios e devolve valores nos pontos que lhe dás) [F, [rtrace man page](https://www.radiance-online.org/learning/documentation/manual-pages/pdfs/rtrace.pdf)] ou `rcontrib` (para coeficientes de luz do dia, essencial para cálculo anual eficiente).

**Quão viável é sem Grasshopper?** Tecnicamente muito viável — a tua geometria são **seis polígonos e três copas**, escreve-se à mão num ficheiro `.rad` em 20 minutos. O problema não é a geometria, é a cadeia de comandos e os parâmetros.

**A dificuldade, sem adoçar.** O site oficial do Radiance diz-o ele próprio: *"New Radiance users face a challenging learning curve ahead, as Radiance is a command line program, and many new users have no previous experience working at the command prompt"*, e que é preciso aprender comandos Unix ou cmd/PowerShell e *scripting* em csh, sh, Python, Perl ou Ruby [F, [Radsite — Learn](https://www.radiance-online.org/learning)].

Pediste-me para dizer se são 40 horas. **A minha estimativa: 25 a 40 horas para chegares a um resultado anual em que confies, se nunca usaste Radiance.** [E] Não é a sintaxe que come o tempo — é perceber a diferença entre irradiância e iluminância nos *outputs*, o que faz cada parâmetro de *ambient*, como montar o cálculo anual sem correr 4.380 simulações independentes, e como o `gendaylit` quer os *inputs* (há relatos em fórum de gente a obter zero componente difusa por passar mal os argumentos [F, [Radiance-general mailing list](https://radiance-general.radiance-online.narkive.com/Q5oGpccB/no-diffuse-component-in-rtrace-with-gendaylit)]).

**Veredicto:** **não vale a pena directamente.** O honeybee-radiance embrulha exactamente esta cadeia e poupa-te 20 horas. Usa Radiance como motor, não como interface. Mas **instala-o**, porque é dependência de tudo o resto. [E]

**Nota lateral útil:** existe o `bifacial_radiance` do NREL, que é um wrapper Python do Radiance para painéis fotovoltaicos bifaciais [F, [NREL/bifacial_radiance](https://github.com/NREL/bifacial_radiance)]. Não é para jardins, mas o código dele é um excelente exemplo legível de como se automatiza Radiance a partir de Python, se quiseres aprender pelo exemplo.

### 2.5 FreeCAD

**BIM/Arch Workbench.** Modela geometria arquitectónica com IFC. Mas a análise solar **não está no BIM Workbench** [F, [freecad-app.com](https://freecad-app.com/workbenches/bim/)].

**Solar Workbench — existe e é mais interessante do que esperava.** Repositório `Francisco-Rosa/Solar`, LGPL-2.1, **25 estrelas, 4 forks, 226 commits**. Faz percurso solar em tempo real, cúpulas de céu, diagramas de irradiação solar, importa ficheiros `.epw`, gera diagramas de equinócios e solstícios [F, [github.com/Francisco-Rosa/Solar](https://github.com/Francisco-Rosa/Solar)]. Há discussão na comunidade OSArch indicando que **usa Ladybug Tools por baixo** e que houve versão lançada em **Maio de 2026** — está vivo [F, [OSArch — FreeCAD Solar Workbench](https://community.osarch.org/discussion/2937/freecad-solar-workbench-using-ladybug-tools)]. Está a trabalhar em **horas de sol directo e irradiâncias em contexto volumétrico** — exactamente o teu caso.

**Mas o aviso é explícito:** os resultados devem ser considerados **experimentais e não recomendados para trabalho profissional, e têm de ser verificados** [F, mesma fonte].

**Veredicto:** [E] projecto promissor, 25 estrelas de maturidade. Vale um olhar de 1 hora por curiosidade, porque se tiver amadurecido dá-te Ladybug numa interface CAD gratuita. **Não construas a tua decisão sobre ele hoje.** Reavalia em 2027.

### 2.6 SketchUp Free (web)

**O que dá.** Modelação por empurrar/esticar, a mais intuitiva que existe; a tua geometria faz-se em **20 a 40 minutos**. Estudos de sombra nativos com *slider* de data e hora, por latitude/longitude.

**Onde falha, e falha em tudo o que importa aqui:** [E]
- **Sem extensões.** O Extension Warehouse é exclusivo das versões desktop pagas. Adeus Curic Sun, adeus qualquer plugin de análise.
- **Sem output quantitativo.** É uma sombra no ecrã. Não conta horas, não dá W/m².
- **Exportação castrada.** A versão gratuita exporta essencialmente só `.skp` e `.stl`. Passar a geometria daqui para Radiance ou Blender é possível via STL mas perdes organização por camadas.
- **Zero difusa e refletida.** Conceito ausente do modelo.

**Veredicto:** ferramenta de esboço rápido e de verificação visual. **Não é instrumento de medida.** Mas se quiseres em 40 minutos ver se a tua intuição sobre as sombras está certa antes de investir horas, é a via mais rápida que existe.

### 2.7 QGIS + UMEP — o candidato surpresa, e forte

Esta foi a segunda descoberta importante. Pediste-me para investigar se o UMEP funciona à escala de 75 m² ou se é grosseiro demais. **Funciona, e a ferramenta certa não é o SOLWEIG — é o SEBE.**

**SOLWEIG** calcula Temperatura Radiante Média (Tmrt) e índices de conforto térmico UTCI e PET [F, [SOLWEIG Manual](https://umep-docs.readthedocs.io/en/latest/OtherManuals/SOLWEIG.html)]. Interessante mas não é o que queres.

**SEBE — Solar Energy on Building Envelopes — é o que queres.** Calcula energia solar potencial píxel a píxel a partir de Modelos Digitais de Superfície, para **superfícies de solo, coberturas e paredes**. Pontos decisivos, todos verificados na documentação oficial [F, [SEBE — UMEP docs](https://umep-docs.readthedocs.io/en/latest/processor/Solar%20Radiation%20Solar%20Energy%20on%20Building%20Envelopes%20(SEBE).html); [tutorial SEBE](https://umep-docs.readthedocs.io/projects/tutorial/en/latest/Tutorials/SEBE.html)]:

1. **A fórmula de irradiância total inclui explicitamente radiação directa, difusa E refletida**, esta última ponderada pelo albedo da superfície. **É exactamente a tríade que te falta.**
2. **Suporta vegetação** através de camadas opcionais: DSM de copa (*canopy*), DSM de zona de tronco, e **transmissividade de luz configurável, com 3% por omissão**. Se não tiveres zona de tronco, gera-a automaticamente.
3. **Output em kWh por píxel**, num raster, mais ficheiro de texto com irradiância nas paredes.
4. Usa algoritmo de *shadow casting* com o DSM e a posição solar para gerar informação píxel a píxel de sombra ou sol.

**Sobre a resolução — a tua pergunta central.** A documentação diz que a resolução espacial é essencial se a área de estudo tiver **grandes variações de altura em distâncias curtas** [F] — que é precisamente o teu caso: 15,50 m de fachada a 5,78 m de um muro de 2,50 m. Os tutoriais usam DSM de **1 metro** [F]. O limite superior é computacional: grelhas acima de **4 milhões de píxeis** devem ser divididas em *tiles* [F].

**Faz as contas:** o teu quintal a **0,10 m de resolução** são 130 × 58 = **7.540 píxeis**. A 0,05 m são 30.160. Estás **duas a três ordens de magnitude abaixo** do limite dos 4 milhões. Podes usar resolução de 5 cm com folga e a máquina nem aquece. [E]

**A resolução não é o problema — o DSM é.** Ninguém te vende um DSM de 5 cm de Alcântara. Tens de **fabricá-lo tu**, e é aqui que está o trabalho real. Duas vias:
- **DSM Generator do UMEP**, que constrói DSMs a partir de dados de edifícios do OpenStreetMap, **e aceita qualquer outro dado vectorial de pegada de edifício que inclua informação de altura dos polígonos** [F, [DSM Generator tutorial](https://umep-docs.readthedocs.io/projects/tutorial/en/latest/Tutorials/DSMGenerator.html)]. Ou seja: desenhas os teus quatro muros como polígonos num shapefile, atribuis alturas (2,50 e 15,50), e ele rasteriza. **Esta é a via, e é boa: as tuas medições de fita passam directamente para o modelo.** [E]
- Nuvem de pontos LiDAR, se houvesse cobertura aérea de Lisboa em alta densidade — há tutorial dedicado [F, [Lidar Processing](https://umep-docs.readthedocs.io/projects/tutorial/en/latest/Tutorials/LidarProcessing.html)]. Improvável que a densidade aérea distinga um muro de 2,50 m.

**Está vivo?** Sim, e com sinal forte: o repositório `UMEP-dev/UMEP` tem 99 estrelas e 26 forks [F], está publicado no repositório oficial de plugins QGIS como **"UMEP for processing 2.0.13"** [F, [plugins.qgis.org](https://plugins.qgis.org/plugins/processing_umep/version/2.0.13/)], e — o sinal mais forte de todos — existe `UMEP-dev/solweig`, uma **reimplementação em Rust das funções do UMEP** [F, [UMEP-dev/solweig](https://github.com/UMEP-dev/solweig)]. Ninguém reescreve código em Rust num projecto abandonado. É consórcio académico internacional (Gotemburgo, Reading).

**Vantagem específica e grande para o teu caso.** A tua sensibilidade à altura dos muros (3,00 vs 2,50 m, que te duplicou a média de Dezembro) testa-se aqui **editando um atributo de altura no shapefile e voltando a correr**. Minutos, não horas. Cumpre o critério que pediste. [E]

**A desvantagem, honestamente.** [E] O UMEP é um "poço de trabalho": cinco camadas raster que têm todas de ter **exactamente a mesma extensão e resolução de píxel** [F], sistemas de coordenadas projectados (para Portugal, ETRS89/PT-TM06, EPSG:3763), ficheiros meteorológicos em formato UMEP. É mais frustração de *plumbing* de SIG do que dificuldade conceptual. Estimo **10 a 18 horas** para quem nunca usou QGIS, **5 a 8 horas** para quem já usou.

**Limitação técnica que tens de saber:** o SEBE trata a vegetação como **voxels com transmissividade uniforme**, não como copas com estrutura de folhas. E a transmissividade é um parâmetro **único, não sazonal** — para o teu lodão de folha caduca tens de correr **duas simulações**: uma de Verão com transmissividade baixa (3–20%) e uma de Inverno com transmissividade alta (60–80%), e usar cada uma na sua estação. É contornável, mas é manual. [E]

**Veredicto:** **o candidato mais forte em relação esforço/resultado depois do pvlib.** Dá-te directa + difusa + refletida + vegetação, em mapas por píxel, gratuitamente, com interface gráfica. Ver secção 9, via B.

### 2.8 Python científico — e a resposta directa à tua pergunta

Perguntaste claramente: "escrever 200 linhas de Python e ter controlo total — para este caso, com geometria tão simples, pode ser a melhor opção. Diz claramente se é."

**Resposta: é a melhor opção para o primeiro número, e não é suficiente para o número final.** Explico as duas metades.

#### `pvlib` — maduro, e com um truque que muda tudo

**Maturidade:** 1.218 estrelas, 214 forks, última actualização em **10 de Agosto de 2026**, versão estável **0.15.2 lançada a 16 de Junho de 2026**. O artigo no Journal of Open Source Software tem **mais de 700 citações** [F, [pvlib/pvlib-python](https://github.com/pvlib/pvlib-python); [Wikipedia — pvlib python](https://en.wikipedia.org/wiki/Pvlib_python)]. Isto é software de qualidade industrial.

**O que traz:** posição solar de alta precisão, decomposição de irradiância, e **múltiplas implementações do modelo de Perez** — o Perez clássico de 1990 e o **Perez-Driesse**, uma reformulação que garante continuidade da função e das primeiras derivadas, substituindo a tabela de coeficientes por *splines* quadráticas [F, [pvlib.irradiance.perez_driesse](https://pvlib-python.readthedocs.io/en/latest/reference/generated/pvlib.irradiance.perez_driesse.html)]. O Perez é o modelo de céu anisotrópico de referência — e anisotropia importa-te, porque a tua difusa não vem uniformemente do céu: vem sobretudo do sector SW que está desobstruído.

**O truque, e é a peça central da via mínima.** `pvlib.iotools.get_pvgis_hourly()` puxa dados horários do PVGIS. E o PVGIS aceita **um perfil de horizonte definido pelo utilizador: elevação em graus, a azimutes igualmente espaçados, no sentido horário a partir do Norte** [F, [pvlib.iotools.get_pvgis_hourly](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.iotools.get_pvgis_hourly.html)]. E devolve as **componentes separadas: directa (beam), difusa e refletida** [F, [PVGIS hourly radiation](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/pvgis-tools/hourly-radiation_en)].

**Porque é que isto é tão bom para ti.** Tu já tens a geometria resolvida analiticamente. Converter a tua geometria num perfil de horizonte é trigonometria que já dominas: para cada azimute de 0 a 350 em passos de 10°, a elevação do obstáculo visto do ponto que estás a analisar. Para X=4, Y=3 (plataforma central):
- azimutes ~60° (fachada a 15,50 m de altura, ~4 m de distância): `atan(15,50/4)` ≈ **75°**
- azimutes ~150° (muro SE de 2,50 m, ~2,8 m): `atan(2,50/2,8)` ≈ **42°**
- azimutes ~240° (muro SW de 2,50 m, ~9 m): `atan(2,50/9)` ≈ **16°**
- azimutes ~330° (muro NW de 2,50 m, ~3 m): `atan(2,50/3)` ≈ **40°**

O PVGIS aplica isto às séries horárias com os seus próprios modelos de céu, sobre **dados climáticos oficiais da Comissão Europeia, satelitários, de 10+ anos**, gratuitos e sem registo [F]. Somas por dia, multiplicas por 0,45 × 4,6, e tens DLI.

**Ganhas:** a difusa deixa de ser um palpite de 20% e passa a ser calculada pelo PVGIS com o teu horizonte real. **É este o salto de qualidade que procuras, e custa-te 2 a 4 horas.** [E]

**Perdes:** três coisas, e é honesto listá-las. (a) O perfil de horizonte é **um por ponto** — cinco zonas, cinco corridas, e o PVGIS trata cada uma como se o horizonte fosse infinitamente distante, o que não é verdade para um muro a 2,8 m. (b) A refletida do PVGIS é o modelo padrão de albedo de solo, **não** a reflexão de uma fachada de 15,50 m a três metros de ti — vai subestimar. (c) **Nada de vegetação.**

**Limitação relevante do pvlib para obstruções:** a função `pvlib.shading.sky_diffuse_passias` existe e calcula redução de difusa por ângulo de mascaramento, mas **assume céu isotrópico e foi desenhada para sombreamento entre filas de painéis** [F, [pvlib.shading.sky_diffuse_passias](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.shading.sky_diffuse_passias.html); [Diffuse Self-Shading](https://pvlib-python.readthedocs.io/en/stable/gallery/shading/plot_passias_diffuse_shading.html)]. Não é geometria de pátio. Não a uses a pensar que resolve o teu caso.

#### `pysolar` e `suncalc-py`
Calculam posição solar e pouco mais. O `pvlib` faz o que eles fazem e muito mais. **Não vale a pena instalar nenhum dos dois.** [E]

#### `shapely` + código próprio — a via de controlo total
Com `shapely` e ~300 linhas fazes: posição solar do `pvlib`, projecção das sombras dos muros para cada hora, teste de contenção do ponto, e **integração numérica do factor de vista do céu por amostragem da cúpula celeste**. Este último é a peça-chave: divides o hemisfério em, digamos, 145 patches (a subdivisão Tregenza padrão), testas se cada patch está visível de cada ponto (raio contra os teus seis polígonos), pesas pela radiância de Perez do patch, e somas. **Isto é fazer um Radiance simplificado à mão.**

**É viável?** Sim. **Vale a pena?** [E] Se gostas de escrever código e queres compreender exactamente o que o número significa, sim, e aprendes mais do que com qualquer GUI. Estimo **15 a 30 horas** e o resultado será bom para directa+difusa. A refletida inter-reflectida (muro→muro→solo) é onde vais desistir ou aceitar uma aproximação de primeira ordem — e é precisamente aí que o Radiance ganha, porque faz isso de graça com `-ab 3`.

**Recomendação de arbitragem:** [E] **faz o pvlib+PVGIS (via curta, 2–4 h). Não faças o shapely+céu-por-patches.** Se o pvlib não te satisfizer, salta directamente para Radiance/honeybee ou UMEP/SEBE, que já resolveram esse problema melhor do que tu o resolverias em 30 horas.

### 2.9 EnergyPlus, OpenStudio, OpenFOAM

**EnergyPlus e OpenStudio:** simuladores de energia de edifícios — cargas térmicas, AVAC, consumo. Precisam de zonas térmicas fechadas. **Um jardim não é uma zona térmica.** Canhão para matar mosquito, e o canhão aponta para o lado errado. [E]

**OpenFOAM:** dinâmica de fluidos computacional. Serviria se a tua pergunta fosse sobre vento ou ilha de calor. **Não tem nada a ver com radiação solar para plantas.** [E]

**Descarta os três.** Nota: o VI-Suite é pré-processador de EnergyPlus *além* de Radiance — ignora essa metade.

**Nota lateral:** o **DAYSIM** é um software de análise de luz natural baseado em Radiance, validado, que modela luz natural anual [F, [reyery/Daysim](https://github.com/reyery/Daysim)]. Historicamente importante (inventou o método dos coeficientes de luz do dia) mas essencialmente **substituído pelo honeybee-radiance**, que faz o mesmo com manutenção activa. Não invistas nele. [E]

---

## 3. Comerciais — e a avaliação sem cerimónia

| Ferramenta | Preço | Avaliação | O que dá que o open source não dá |
|---|---|---|---|
| **Rhino 8 + Grasshopper + Ladybug** | **995 €** perpétuo, 1 utilizador, Europa [M] | 90 dias completos | **A única compra que considerava.** Não é o Ladybug (gratuito) — é o Grasshopper, que transforma 25 h de Python em 6 h de arrastar nós, e a modelação NURBS cotada. Licença perpétua, não subscrição. [E] |
| **SketchUp Pro** | **≈379 €/ano** (re-subscritores europeus, Dez 2025); 399 USD/ano lista [M, [forum Trimble](https://forums.sketchup.com/t/sketchup-purchase-and-exchange-rates/342725); [Trimble plans](https://sketchup.trimble.com/en/plans-and-pricing)] | 30 dias | Modelação mais rápida do mundo + acesso a extensões. **Nenhuma capacidade radiométrica.** Não resolve o DLI, e é subscrição. [E] |
| **Curic Sun** (extensão SketchUp) | Preço não publicado nas fontes que consultei [M] | — | Animação de sol/sombra melhorada. **Qualitativo.** Requer SketchUp Pro. [F, [Curic Sun](https://www.suapp.com/en/plugin/400)] |
| **Sun Diagram Pro** (extensão SketchUp) | **45 USD vitalício** [M, [Gumroad](https://febhouse.gumroad.com/l/Sundiagram)] | — | Análise de sombra para os 12 meses, qualquer dia/hora [F, [sundiagram.com](https://sundiagram.com/)]. Barato e competente — **mas horas de sol, não DLI.** [E] |
| **Sefaira** (Trimble) | Cotação, tipicamente >1.000 €/ano [M] | — | Análise energética de edifícios em fase conceptual. **Orientado a interiores.** Irrelevante. [E] |
| **Pollination** (Ladybug Tools) | Subscrição mensal ou anual; trial de 30 dias; entrada típica 10 utilizadores autorizados + 1 licença concorrente [F, [pollination.solutions/pricing](https://www.pollination.solutions/pricing)]. Valor exacto não publicado sem cotação [M] | 30 dias | Ladybug/Honeybee empacotado com interface, simulação na nuvem, e plugins Rhino/Revit [F, [Rhino Plugin](https://www.pollination.solutions/rhino-plugin)]. **É o Honeybee que já podes ter de graça, com conveniência por cima.** Produto empresarial. [E] |
| **Revit + Insight** | ≈2.800–3.300 €/ano [M] | 30 dias | Nada de relevante. Absurdo para 75 m². [E] |
| **ArchiCAD** | ≈2.500–3.000 €/ano [M] | 30 dias | Idem. [E] |
| **Shadowmap** | **Explorer £30/ano · Home £8,33/mês · Studio £50/mês**; noutra fonte Light 14,99 USD/ano e Pro 9,99 USD/mês [M, [shadowmap.org/pricing](https://shadowmap.org/pricing)] | Versão gratuita limitada | Ver secção 4. |
| **Sun Surveyor** | ≈10–12 € compra única [M] | Versão Lite gratuita [F, [Google Play](https://play.google.com/store/apps/details?id=com.ratana.sunsurveyorlite)] | Ver secção 4. **Melhor euro gasto do relatório.** [E] |
| **PVsyst** | ≈1.000 €/ano [M] | 30 dias | Projecto de centrais fotovoltaicas. Tem cálculo de horizonte e sombreamento próximo bons, mas dá **kWh eléctricos**, não mol de fotões. Errado para o problema. [E] |
| **Autodesk Forma** | Subscrição Autodesk, >1.500 €/ano [M] | Trial | Análise ambiental urbana rápida. **Escala de urbanismo, não de quintal.** [E] |
| **SketchUp Diffusion** | Incluído em subscrições SketchUp [M] | — | Renderização por IA generativa. **Produz imagens plausíveis, não medições.** Zero valor analítico — e potencialmente nocivo, porque produz imagens convincentes e fisicamente falsas. [E] |

**Veredicto da secção 3.** Para o problema do DLI, **nada no mercado comercial justifica o preço**, com uma excepção parcial. A excepção é o **Rhino a 995 €**, e mesmo essa não é sobre capacidade — é sobre comprar 15 a 20 horas do teu tempo. Se valorizas o teu tempo acima de ≈50 €/hora e vais usar o modelo para o projecto de desenho durante anos, o Rhino paga-se. Se não, o honeybee-radiance em Python faz literalmente a mesma simulação, com o mesmo motor, com o mesmo resultado numérico, por 0 €. [E]

**O que compraria, de tudo o que está nesta tabela:** Sun Surveyor, por 12 €. E nada mais.

---

## 4. Aplicações móveis e ferramentas de campo

Esta secção merece mais peso do que se esperaria, porque para **validação** e para **intuição** as apps de AR batem qualquer CAD.

### Sun Surveyor — recomendo
AR do percurso do sol e da lua, bússola 3D, mapas de percurso solar. Explicitamente publicitado para **identificar obstruções potenciais e sombra da envolvente** — é o teu caso [F, [Sun Surveyor](https://spark.mwm.ai/us/apps/sun-surveyor-sun-moon/525176875)]. Tem versão Lite gratuita [F]. ≈10–12 € a versão completa [M].

**Valor real para ti:** [E] vais ao quintal, apontas o telefone, e **vês** onde o sol vai estar a 21 de Dezembro às 11:00 e se o muro SE o tapa. Confirma ou destrói a tua "primeira luz: 21 Dez 10:36" em cinco minutos. É a verificação de sanidade mais barata e mais rápida disponível.

### PhotoPills
Excelente app de planeamento fotográfico com AR solar/lunar. **Detalhe importante e a favor:** reconhece explicitamente que a bússola pode falhar por interferência magnética externa — dispositivos electrónicos, objectos metálicos, campos magnéticos — e por isso **permite calibração manual das vistas de AR**, sobrepondo o percurso à posição correcta mesmo quando a bússola mente [F, [PhotoPills 2.1.1](https://www.photopills.com/blog/update-photopills-2-1-1)].

**Isto responde directamente à tua preocupação.** [E] Num quintal fechado com muros — provavelmente com armadura de betão, canos, talvez gradeamento — a bússola **vai** desviar-se. As apps que só confiam no magnetómetro dão-te azimutes errados em 5 a 20°, o que num cálculo de primeira luz são dezenas de minutos de erro. A calibração manual do PhotoPills é, por isso, **a característica decisiva** para uso em espaço confinado. Há relatos de utilizadores sobre desvios por metal e electrónica próximos, com recomendação de calibrar antes de usar e evitar ambientes metálicos [F, [Sun Seeker review](https://marlvel.ai/intel-report/navigation/sun-seeker-sunlight-tracker)].

**Truque de calibração para o teu caso, e é simples:** [E] num dia de sol, aponta a app a uma sombra real bem definida (o canto do muro SE projectado no chão) e ajusta manualmente até a sobreposição coincidir com a sombra verdadeira. A partir daí a app está calibrada geometricamente, não magneticamente. **É mais fiável do que a bússola em qualquer circunstância.**

### Sun Seeker
Funcionalmente semelhante, 11,99 USD [M]. Escolhe uma das três, não três.

### Shadowmap
Diferente das outras: é **simulação 3D global baseada em dados de edifícios, árvores e terreno**, não AR. Simula luz solar **ao minuto, em qualquer data** [F, [shadowmap.org](https://shadowmap.org/)]. A subscrição Pro desbloqueia o *slider* de data, visualização de 365 dias, liberdade total de câmara e vista em primeira pessoa ao nível do solo [F, [pricing](https://shadowmap.org/pricing)]. Anunciam suporte a **luz solar indirecta e estatísticas mensais** [F], e existe uma API descrita como "the world's first global 3D solar data layer" [F, [Shadowmap API](https://shadowmap.org/api)]. É usada em investigação OSINT, o que atesta seriedade [F, [Bellingcat toolkit](https://bellingcat.gitbook.io/toolkit/more/all-tools/shadowmap)].

**O problema, e é o mesmo do Google (secção 5):** [E] o Shadowmap tem a volumetria do teu **prédio** — não tem os teus **muros de 2,50 m**. E num quintal onde os muros são o que determina tudo excepto a fachada, isso deixa-o a modelar metade do problema. Serve para confirmar o efeito da fachada de 15,50 m; não serve para as tuas cinco zonas.

**Alternativa gratuita mencionável:** ShadeMap, também no toolkit Bellingcat [F, [ShadeMap](https://bellingcat.gitbook.io/toolkit/more/all-tools/shademap)].

### Arcascope
Não encontrei nesta investigação um produto Arcascope de análise solar arquitectónica. A Arcascope é conhecida por apps de ritmo circadiano e sono (Shift, Circadia). **Se é essa, não tem aplicação aqui.** [E] Assinalo como ponto a confirmar, na secção 10.

### Veredicto da secção 4
**Instala o Sun Surveyor ou o PhotoPills hoje, custa 12 €, e vai ao quintal.** [E] Não te dá DLI — nenhuma destas dá, nem finge dar. Mas dá-te em 30 minutos a certeza de que a tua geometria de horizonte está certa, e essa certeza é o alicerce de toda a simulação que vier depois. É o passo 0 de qualquer via.

---

## 5. A via Google 3D — investigada a sério, e o resultado é negativo

Pediste explicitamente esta investigação. Fiz-a, e a conclusão é clara: **esta via não serve para o teu objectivo, por duas razões independentes e cada uma delas suficiente.** Uma é de resolução, outra é legal e afecta-te especificamente por estares em Portugal.

### 5.1 A razão técnica: a malha não tem os teus muros

Colocaste a pergunta crítica exactamente onde ela está: *"a malha do Google tem resolução para representar muros de 2,5 m num quintal de 5,78 m de largura, ou vai amalgamá-los?"*

**Resposta: vai amalgamá-los. Quase com certeza não existem na malha.** [E, com base em factos abaixo]

A documentação de boas práticas do Google Earth Studio diz que **em cidades, as texturas e malhas podem ter qualidade menos-que-ideal ao nível da rua**, e que **há limites para a nitidez da imagem quando a câmara está a baixa altitude** [F, [Earth Studio Best Practices](https://earth.google.com/studio/docs/best-practices/)]. A malha fotogramétrica do Google é reconstruída de fotografia aérea oblíqua: capta bem volumes de edifícios, mal elementos verticais finos e baixos, e tende a fundir estruturas próximas numa superfície contínua.

O teu caso é o pior possível para esta tecnologia: um muro de **0,18 m de espessura e 2,50 m de altura**, num vão de 5,78 m, **debaixo de uma fachada de 15,50 m** que projecta sombra permanente sobre ele na captura aérea. Fotogrametria em sombra permanente, de um objecto de 18 cm de espessura, com a escala de captura aérea — não resolve. A malha vai dar-te um pátio genérico, provavelmente plano, possivelmente com as copas das árvores fundidas no terreno.

**E os teus muros são o problema todo.** Já estabeleceste que baixar os muros de 3,00 para 2,50 m **duplicou a média de Dezembro**. Uma ferramenta que não os tem não pode responder à tua pergunta — vai dar-te números de Dezembro que estão errados por um factor de dois, com aparência credível. **Isso é pior do que não ter ferramenta.** [E]

### 5.2 Google Earth Pro (desktop)

Tem *slider* temporal de luz solar. Muda-se a hora do dia arrastando o *slider* para a direita ou esquerda, e consegue-se ver nascer ou pôr do sol [F]. Mas o Google Earth **não mostra projecções exactas de sombra para todas as regiões — depende dos dados subjacentes**, e há edifícios 3D em cerca de **2.500 localidades em 49 países** [F].

**Veredicto:** ferramenta de contexto e apresentação. Zero valor métrico para ti. [E] Tem uma utilidade lateral real: confirmar a volumetria do quarteirão e o declive a SW, para justificares "horizonte livre a SW". Isso vale meia hora.

### 5.3 Google Earth Studio

Animação com iluminação solar por data/hora. A qualidade da malha depende do tamanho do frame: **renderizar acima do 1080p por omissão dá geometria de muito maior qualidade** [F]. Interessante, mas é uma ferramenta de **cinematografia**. Não produz números. Mesmo problema de malha.

### 5.4 Extrair a malha do Google para Blender — e o lado legal

**As ferramentas existem e estão vivas:**
- `eliemichel/MapsModelsImporter` — o add-on original, via captura RenderDoc [F, [GitHub](https://github.com/eliemichel/MapsModelsImporter)]
- `Sheep-max/MapsModelsImporter-Enhanced` — versão mantida, **suporta RenderDoc 1.13–1.43 e Blender 4.0–5.1+** [F, [GitHub](https://github.com/Sheep-max/MapsModelsImporter-Enhanced)]. Está actualizada para o Blender de hoje.

**O lado legal, sem contornar a questão como pediste.** [F, com base nas fontes abaixo] A captura de dados de renderização do Google Maps/Earth via RenderDoc **pode violar os Termos de Serviço do Google**. Os dados de mapa, modelos 3D e imagens de satélite estão **protegidos por direitos de autor**, e a extração não autorizada pode disparar os mecanismos anti-abuso do Google. O próprio repositório Enhanced declara-se **"For technical research only"** e destina-se "solely for technical research and personal non-commercial learning", proibindo expressamente uso que viole leis, regulamentos ou os ToS do Google [F, [Sheep-max README](https://github.com/Sheep-max/MapsModelsImporter-Enhanced); [blog.exppad.com](https://blog.exppad.com/article/importing-actual-3d-models-from-google-maps)].

A leitura mais permissiva que encontrei é que **pode ser admissível para uso privado, apenas de leitura** (como acontece ao navegar no Google Maps), mas **não para além disso**, e há discussão aberta na comunidade Google Maps sobre a legalidade para trabalhos criativos [F, [Google Maps Community](https://support.google.com/maps/thread/349961684?hl=en); [Map Tiles API Policies](https://developers.google.com/maps/documentation/tile/policies)].

**A minha leitura, e assumo-a como juízo:** [E] para um estudo privado do teu próprio quintal, sem publicação nem uso comercial, o risco prático é próximo de zero e a zona é cinzenta, não negra. **Mas é irrelevante discutir isso**, porque a malha extraída não tem os teus muros. Estarias a correr um risco legal, ainda que pequeno, por um modelo que não responde à pergunta. **Não faças.**

### 5.5 Blosm / blender-osm — e a má notícia para Portugal

O Blosm (`vvoovv/blosm`) importa OpenStreetMap, terreno e cidades 3D do Google para o Blender. Houve um período em que o Google lançou os **3D Tiles através da Map Tiles API**, tornando a importação de cidades 3D no Blender **completamente legal** [F, [Blender Artists](https://blenderartists.org/t/blosm-import-of-google-3d-cities-openstreetmap-terrain/608089/522); [Blosm Gumroad](https://prochitecture.gumroad.com/l/blender-osm)].

**Esse período terminou, e terminou para ti em particular.** [F]

> **O Google deixou de servir 3D Tiles para projectos criados após 8 de Julho de 2025 associados a uma conta com endereço de facturação na UE/EEE.** Os *tiles* fotorrealistas 3D **não estão disponíveis** em projectos ligados a conta de facturação com endereço do Espaço Económico Europeu. A Map Tiles API devolve **erro HTTP 403** a esses pedidos.

Fontes: [F, [Issue #644 do Blosm](https://github.com/vvoovv/blosm/issues/644); [Google — Map Tiles API adjustments for EEA customers](https://developers.google.com/maps/comms/eea/map-tiles); [Photorealistic 3D Tiles overview](https://developers.google.com/maps/documentation/tile/3d-tiles-overview)]. Faz parte dos novos Termos de Serviço específicos do EEE, em vigor desde **8 de Julho de 2025** [F]. O mesmo aconteceu aos 2D Tiles de satélite para desenvolvedores europeus [F, [OSGeo Discourse](https://discourse.osgeo.org/t/google-satellite-2d-tiles-stopped-working-for-european-economic-area-eea-developers/149688)].

**Tradução para a tua situação:** estás em Lisboa. Qualquer conta de facturação Google Cloud que cries tem endereço português, logo EEE. **A via legal de acesso aos 3D Tiles do Google está-te fechada, por política, desde Julho de 2025.** A documentação do Google aconselha, aos utilizadores do EEE, **considerar conjuntos de dados de 3D Tiles com licença aberta** [F].

Isto resolve a questão: a única via de acesso ao Google 3D que te resta é a extração via RenderDoc, que é a zona cinzenta legal — e que, como vimos, dá uma malha que não serve.

### 5.6 Cesium + Google Photorealistic 3D Tiles
O CesiumJS consome 3D Tiles, incluindo os fotorrealistas do Google via API [F]. **Cai exactamente na mesma restrição EEE da secção 5.5.** E o Cesium é um motor de visualização geoespacial — não tem simulação de radiação solar em unidades físicas. Dupla exclusão. [E]

### 5.7 Google Solar API
**Existe e funciona assim:** o *endpoint* `buildingInsights` dá localização, dimensões e potencial solar de um edifício — segmentos de telhado, número de painéis que cabem, potencial solar de disposições de painéis, e deteta painéis já instalados. O `dataLayers` dá GeoTIFFs: **mapas digitais de superfície (DSM), imagem RGB aérea, e fluxo solar** anual e mensal, descrito como "o rendimento anual de uma dada superfície" [F, [Building Insights](https://developers.google.com/maps/documentation/solar/building-insights); [Solar API overview](https://developers.google.com/maps/documentation/solar/overview)].

**Preço:** pay-as-you-go por SKU. **Building Insights tem tecto gratuito de 10.000 pedidos/mês; Data Layers tem tecto gratuito de apenas 1.000 e é significativamente mais caro** por unidade adicional. Uma chamada ao Data Layers cobre todos os GeoTIFFs disponíveis para uma dada latitude/longitude, a preço fixo por chamada bem-sucedida [F, [Usage and Billing](https://developers.google.com/maps/documentation/solar/usage-and-billing)]. **Para o teu uso — meia dúzia de chamadas — ficas dentro do tecto gratuito.** [E]

**Cobertura em Lisboa:** não confirmada. A cobertura expandida de qualidade média está documentada para **Alemanha, Reino Unido, França, Espanha, Itália e Florida** [F, [Expanded Coverage](https://developers.google.com/maps/documentation/solar/expanded-coverage)]. **Portugal não aparece nessa lista.** Há o parâmetro `requiredQuality=BASE` para maximizar a cobertura [F]. Isto é testável em 15 minutos com uma chamada `curl`. Fica na secção 10.

**Serve para um quintal ao nível do solo?** [E] **Não.** Três razões, por ordem de gravidade:
1. **É um produto para telhados.** O modelo de negócio é dimensionar painéis fotovoltaicos. A API está organizada em torno de "roof segments".
2. **A resolução do DSM não está publicada.** Fui à documentação dos Data Layers e **não indica as resoluções disponíveis**; existe um parâmetro `pixelSizeMeters` mas não lista os valores suportados, nem clarifica se o fluxo cobre solo ou só coberturas [F, [Data Layers docs](https://developers.google.com/maps/documentation/solar/data-layers)]. O DSM deriva da mesma fotogrametria aérea da secção 5.1 — **os teus muros de 0,18 m de espessura não estarão lá.**
3. **Dá kWh, não mol.** Mesma conversão espectral por fazer, sem nenhuma das vantagens.

**Veredicto:** engenhoso, gratuito ao teu volume, e errado para o problema.

### 5.8 OpenStreetMap — a alternativa livre, e é honesta
OSM com atributos `building:levels` ou `height`, importado via Blosm (a funcionalidade OSM não depende dos 3D Tiles do Google, logo **não é afectada pela restrição EEE**) [F, [wiki.openstreetmap.org/Blender-osm](https://wiki.openstreetmap.org/wiki/Blender-osm); [OSM Community](https://community.openstreetmap.org/t/blender-osm-openstreetmap-and-terrain-for-blender/67684)]. Ou directamente no **DSM Generator do UMEP**, que foi feito para consumir dados de edifícios OSM [F].

**É mais grosseiro?** Sim, muito: caixas extrudidas, sem detalhe. **Mas é legalmente limpo, gratuito, e — crucialmente — editável.** Podes acrescentar os teus quatro muros à mão com as alturas que mediste com a fita. [E]

**E é isto que inverte a comparação.** O Google dá-te uma malha bonita que não podes editar e que não tem os teus muros. O OSM dá-te uma caixa feia que podes corrigir até ficar exacta. **Para medição, feio-e-exacto ganha a bonito-e-errado, sempre.** Para o teu caso o edifício de 15,50 m vem do OSM (ou desenhas o rectângulo tu, é mais rápido) e os muros desenhas tu. É a via da secção 9 B.

### 5.9 Fotogrametria própria — a boa ideia desta secção

Pediste atenção especial a isto, e tinhas razão em pedir: **é a melhor resposta à pergunta "como modelo isto facilmente", porque a geometria vem da realidade.**

#### Meshroom (AliceVision) — open source, vivo
**Meshroom 2025.1.0, lançado a 18 de Agosto de 2025**, com builds para Linux e **Windows** [F, [Release v2025.1.0](https://github.com/alicevision/Meshroom/releases/tag/v2025.1.0)]. Foi reformulado como *toolbox* de programação visual baseada em nós, com arquitectura de plugins; os pipelines standard (fotogrametria, camera tracking, HDR panorama, Lidar meshing) estão unificados no plugin AliceVision. Há capacidades novas de IA — segmentação semântica, **Gaussian Splatting**, estimativa de profundidade monocular — via MeshroomHub [F].

**Bug a saber de antemão:** a 2025.1.0 **fecha se o caminho de ficheiro tiver espaços** [F, mesma fonte]. Nota-o, porque o teu caminho de projecto tem espaços (`David - Projects`). Usa uma pasta de trabalho tipo `C:\fotogrametria\jardim`.

#### COLMAP
SfM/MVS de referência, reconhecido a par do Meshroom nas comparações de fotogrametria [F, [Springer — COLMAP vs Meshroom](https://link.springer.com/chapter/10.1007/978-3-032-13056-3_38); [comparação](https://slashdot.org/software/comparison/COLMAP-vs-Meshroom/)]. Há inclusive uma issue no Meshroom a discutir casos em que o COLMAP dá resultados significativamente melhores [F, [Issue #2126](https://github.com/alicevision/Meshroom/issues/2126)]. Mais exigente de usar, sem GUI de nós.

#### iPhone com LiDAR — e os números reais de precisão
Aqui os dados são mistos e importa ler com cuidado, porque há muito optimismo publicitário:

**Optimista:** a precisão do Polycam com câmara LiDAR fica **dentro de 2,5 cm de resolução em áreas bem iluminadas e à distância de scan de 1 metro**, comparável a unidades LiDAR autónomas muito mais caras — **mas a precisão degrada-se rapidamente com o aumento da distância de scan** [F, [3dmag.com](https://www.3dmag.com/3d-wikipedia/phone-3d-scanning-lidar-iphone-3d-apps-guide/)].

**Pessimista, e mais relevante:** em documentação à escala de edifício com iPhone 13 Pro, as precisões práticas **agruparam-se nos 10–20 cm a 95% de confiança, e nenhuma app atingiu 95% das distâncias dentro de LOA ≤5 cm** [F, [MDPI](https://www.mdpi.com/2673-7418/3/4/30)].

**E muito divergente entre apps:** num estudo comparativo, o **Polycam Pro apresentou erro médio de 42,58% e o Scaniverse 10,36%** [F, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1877050925026742)]. Densidade de pontos por m²: 9.128 no Polycam contra 1.183 no Scaniverse [F]. Há também um estudo GSA sobre a precisão do Polycam em investigação de campo [F, [GSA 2024](https://gsa.confex.com/gsa/2024AM/webprogram/Paper405030.html)] e uma comparação profissional contra scanning terrestre estabelecido [F, [J.S. Held](https://www.jsheld.com/insights/articles/a-comparison-of-mobile-phone-lidar-capture-and-established-ground-based-3d-scanning-methodologies)].

**A minha leitura para o teu caso.** [E] Contas: um erro de **10 cm na altura de um muro de 2,50 m são 4%**. O teu conflito de fontes (3,00 vs 2,50 m) é de **20%**. Logo, **a fotogrametria de telefone resolve o teu conflito de alturas com margem confortável de cinco para um.** Isso já é um resultado com valor.

E resolve o que **nenhum** cálculo analítico nem malha do Google resolve: **a palmeira, cuja altura e diâmetro de copa não estão medidos.** Uma nuvem de pontos dá-te esses dois números, mais a forma real da copa, mais o lodão, mais a citrinheira. Em vez de estimares "≈5 m" para o lodão, mede-lo.

**Precaução importante que a maior parte dos tutoriais omite:** [E] **a escala.** SfM puro (Meshroom, COLMAP a partir de fotos) reconstrói geometria **sem escala métrica absoluta** — dá-te a forma certa, com o tamanho arbitrário. Solução simples: põe no chão dois objectos a uma distância que mediste com fita (uma régua de 1 m, ou duas marcas a 5,00 m), fotografa-os, e escala a malha por esse par de pontos no Blender. Duas medições de fita e o modelo passa a métrico. **Com iPhone LiDAR isto não é necessário**, porque o LiDAR dá escala absoluta directamente — e é uma vantagem prática grande a favor do telefone com LiDAR sobre o Meshroom.

**Reserva prática séria:** [E] a fotogrametria de uma palmeira é **difícil**. Folhas finas, movimento com a brisa, auto-oclusão, céu de fundo. Espera uma copa reconstruída como uma nuvem ruidosa e cheia de buracos, não como uma superfície limpa. **Para simulação solar isso é aceitável** — o que precisas é do envelope da copa e de uma transmissividade, não da geometria de cada folha. Estimo que a malha bruta precisa de **2 a 4 horas de limpeza no Blender** antes de servir para simulação: fechar buracos, remover ruído, substituir a copa por uma primitiva (elipsóide) das dimensões medidas.

**Esse último ponto é o conselho operacional:** [E] não simules com a malha fotogramétrica bruta. **Usa-a como referência métrica para desenhar geometria limpa por cima.** Importas a nuvem para o Blender, e desenhas os teus seis planos e três elipsóides *ajustados à nuvem*. Ficas com um modelo leve, limpo, com normais correctas — que é o que o Radiance quer — e com dimensões que vieram da realidade em vez de vierem de um corte de arquitectura que já se provou errado em 20%.

### 5.10 Veredicto da secção 5
**A via Google está fechada, por duas razões independentes:**
1. **Técnica:** a malha fotogramétrica não resolve muros de 0,18 m × 2,50 m em sombra permanente sob uma fachada de 15,50 m. E os muros são o problema todo.
2. **Legal e específica a ti:** os 3D Tiles do Google estão indisponíveis para projectos com facturação EEE criados após 8 de Julho de 2025. Estás em Lisboa. A via limpa está fechada; a via cinzenta (RenderDoc) dá a malha inútil do ponto 1.

**O que salvo desta secção, e é muito:** a **fotogrametria própria**. Substitui a malha do Google por uma melhor, é legalmente tua, tem os teus muros verdadeiros, mede-te a palmeira, e resolve o conflito de alturas de 3,00 vs 2,50 m. **50–100 fotos, 1 hora de campo, 2 horas de processamento, 2–4 horas de limpeza.** É o melhor uso possível de uma tarde.

---

## 6. Fluxo de trabalho recomendado, passo a passo

Pediste um caminho, não uma lista. Este é o caminho, com tempos para alguém competente mas novo em cada ferramenta.

### Etapa 0 — Verificação de campo (1,5 h, 12 €)
| | |
|---|---|
| **Ferramenta** | Sun Surveyor ou PhotoPills (telefone) + fita métrica + nível de bolha |
| **Faz** | Calibra manualmente a AR contra uma sombra real (ver secção 4). Confirma os azimutes: SW 240°, SE 150°, NW 330°, NE 60°. **Mede a altura dos quatro muros em três pontos cada** — resolve o conflito 2,50/3,00. **Mede a altura e o diâmetro da copa da palmeira** (triangulação: afasta-te uma distância medida, mede o ângulo ao topo com a app de inclinómetro). Idem lodão. Verifica a primeira luz prevista para hoje, 15 de Setembro (interpola entre os teus 11 Set 12:24 e o equinócio). |
| **Sai** | Uma folha de papel com números verificados. Um `.md` em `10-LOCAL/`. |
| **Porque primeiro** | Todas as etapas seguintes consomem estes números. Errar aqui propaga-se a tudo. E se a AR mostrar que a tua primeira luz está certa ao quarto de hora, ganhas confiança em toda a geometria analítica já feita. |

### Etapa 1 — Número mínimo de DLI (3 h, 0 €)
| | |
|---|---|
| **Ferramenta** | Python + `pvlib` (`pip install pvlib`) |
| **Faz** | Para cada uma das 5 zonas, calcula o perfil de horizonte em 36 azimutes (passos de 10°) por trigonometria — reaproveitas o código que já tens. Chama `pvlib.iotools.get_pvgis_hourly(latitude=38.69967, longitude=-9.19038, components=True, userhorizon=[...])`. Soma GHI por dia para Dez / equinócio / Jun. Multiplica por **0,45 × 4,6 = 2,07** e por 3600 s/h ÷ 10⁶. |
| **Formato** | JSON/CSV do PVGIS → pandas → tabela |
| **Sai** | **Tabela de DLI por zona e estação, com componentes directa e difusa separadas.** |
| **Ganho decisivo** | A difusa deixa de ser o palpite de 20% e passa a vir dos modelos do PVGIS sobre dados satelitários oficiais da UE com o teu horizonte real. **Se esta tabela der Verão >20 mol em todas as zonas menos as duas piores, já tens a tua decisão.** |
| **Calcula duas vezes** | Com factor 2,07 e com 2,3. A diferença é a tua barra de erro espectral. |

### Etapa 2 — Encomenda o medidor (15 min, ≈460 €)
Apogee DLI-500. Chega em ~2 semanas. Enquanto não chega, continuas. Ver etapa 6.

### Etapa 3 — Captura métrica do espaço (1 h campo + 2 h máquina + 3 h limpeza)
| | |
|---|---|
| **Ferramenta** | iPhone com LiDAR + Scaniverse (preferir ao Polycam: erro 10% vs 43%) **ou** 60–100 fotos + Meshroom 2025.1.0 |
| **Faz** | Percorre o quintal em duas voltas a alturas diferentes, sobreposição de 70% entre fotos, evita sol de contraluz, inclui as duas marcas de escala a 5,00 m. Exporta OBJ. |
| **Formato** | `.obj` + `.mtl` → Blender |
| **Atenção** | Pasta sem espaços no caminho, se usares Meshroom. Escala a malha pelas marcas se usares SfM puro. |
| **Sai** | Nuvem/malha métrica com muros reais, palmeira, lodão, citrinheira, varanda. |

### Etapa 4 — Geometria limpa (2 h)
| | |
|---|---|
| **Ferramenta** | Blender (gratuito) |
| **Faz** | Importa a malha. **Não simules com ela.** Desenha por cima: solo 13,00 × 5,78; quatro paredes (15,50 / 2,50 / 2,50 / 2,50); a varanda em consola; três elipsóides para as copas ajustados à nuvem. Separa em objectos nomeados por material: `solo`, `fachada`, `muro_SE`, `muro_NW`, `muro_SW`, `copa_palmeira`, `copa_lodao`, `copa_citrinheira`. Verifica normais (`Shift+N`). |
| **Formato de saída** | `.obj` ou `.rad` |
| **Bónus** | Este é o mesmo modelo que serve para a iluminação cénica e o desenho do jardim. |

### Etapa 5 — Simulação radiométrica (escolhe uma via)

**Via 5a — UMEP/SEBE no QGIS (8–15 h)**
Não usa o Blender. Desenha os muros como polígonos num shapefile com campo de altura, em EPSG:3763. `UMEP > Pre-Processor > Spatial Data > DSM Generator` a 0,10 m. Acrescenta DSM de copa para palmeira e lodão. Corre SEBE duas vezes: Verão (transmissividade 3–10%) e Inverno (lodão a 70%). **Output: raster kWh/m² por píxel** → converte para DLI. **Vantagem: testas 2,50 vs 3,00 m editando um atributo.**

**Via 5b — Radiance via honeybee-radiance (15–25 h)**
Instala Radiance em `C:\Radiance`; `pip install lbt-honeybee`; verifica `honeybee-radiance --help`. Constrói o modelo Honeybee a partir da geometria (Shade faces para os muros, com modificadores de reflectância: ≈0,4 para muro rebocado claro, ≈0,3 para a fachada, ≈0,2 para o solo). Copas como Shade com modificador `trans` (transmissividade 0,05 Verão / 0,7 Inverno para o lodão). Grid de sensores a 0,10 m do solo, espaçamento 0,25 m. Corre a receita **Annual Irradiance** com EPW de Lisboa. Usa `-ab 3` no mínimo e testa `-ab 5`. **Output: W/m² horário por sensor** → DLI.

**Via 5c — VI-Suite no Blender (8–15 h)**
Usa o modelo da etapa 4 directamente. Instala Radiance. Instala vi-suite07 (Blender 5.1) ou master (4.4). Nós de análise de irradiância → **CSV**. Vantagem: um só ficheiro para análise e para desenho.

### Etapa 6 — Validação e calibração (2 h + 7 dias de espera)
Quando o DLI-500 chegar: põe-no na plataforma central, 7 dias. Compara com a simulação para as mesmas datas. **Calcula o factor de correcção** (medido ÷ simulado). Aplica-o às outras estações e zonas. **Isto é o passo que transforma uma simulação de ±25% numa de ±8%.** [E]

### Etapa 7 — Validação geométrica com as fotos EXIF (2 h)
Ver secção 7.

### Resumo de tempos

| Via | Tempo total | Custo | Resultado |
|---|---|---|---|
| **Mínima** (0+1) | **4,5 h** | 12 € | DLI com difusa modelada, sem vegetação |
| **Mínima + medição** (0+1+2+6) | 6,5 h + 14 dias | ≈472 € | DLI validado empiricamente ±8% |
| **Completa** (0–7, via 5b ou 5c) | **30–45 h** + 14 dias | ≈472 € | Modelo 3D reutilizável + DLI calibrado por zona |

---

## 7. Validação com as três fotografias EXIF

Tens um activo melhor do que pensas: **27 Mai 2025 10:59 · 26 Mar 2025 16:47 · 11 Set 2026 12:00**, e as duas primeiras com geometrias de sombra opostas (manhã de fim de Primavera, tarde de equinócio). Isso é um teste com poder discriminante real, porque um erro de geometria que passe num caso falha no outro.

### Procedimento, passo a passo

**1. Fixa os tempos.** Confirma no EXIF se o *timestamp* é local ou UTC, e se o telefone tinha horário de Verão activo (em Portugal, Mai e Mar de 2025 estão em WEST = UTC+1; Set 2026 também). **Um erro de 1 hora desloca o azimute solar ≈15° e invalida o teste.** Verifica cruzando: se houver GPS no EXIF, o campo `GPSTimeStamp` é sempre UTC — compara com o `DateTimeOriginal`.

**2. Recupera a posição da câmara.** Para cada foto, identifica na imagem pontos de geometria conhecida (cantos dos muros, esquadria da porta, peitoris a 2,00 m). Com 4+ pontos e as suas coordenadas 3D, resolve a pose da câmara. Duas maneiras:
   - **Manual no Blender:** add-on **"Camera Calibration using Perspective Views of Rectangles"** ou o **fSpy** (gratuito, com importador Blender) — arrastas linhas de fuga sobre a imagem e ele devolve a pose e a focal. **15–30 min por foto.** É o caminho pragmático.
   - **Automático:** se fizeste a fotogrametria da etapa 3, mete as três fotos históricas no mesmo lote do Meshroom/COLMAP e ele resolve-te a pose **no mesmo referencial da malha**. Elegante, e é o argumento mais forte para fazer a fotogrametria.

**3. Reproduz e sobrepõe.** No Blender/Radiance, põe o sol na data/hora exacta (Sun Position add-on, coordenadas 38,69967 / -9,19038, fuso Europe/Lisbon), renderiza da câmara recuperada, e sobrepõe ao original com o *blend mode* "Difference".

**4. Mede o erro — e mede-o em três métricas, não uma.** [E] Isto é o cerne e é onde a maioria das validações amadoras falha, por medir só uma coisa:

| Métrica | Como medir | Tolerância aceitável |
|---|---|---|
| **Erro posicional da linha de sombra** | Distância no plano do solo entre a aresta de sombra real e simulada, em pontos de referência identificáveis (juntas de pavimento, cantos de canteiro) | **<0,10 m** [E] |
| **IoU da região sombreada** | Intersection over Union: binariza ambas as imagens em sol/sombra na área do solo, calcula área(∩)/área(∪). Trivial em Python com numpy | **>0,90** [E] |
| **Erro angular implícito** | `atan(erro_posicional / distância_ao_obstáculo)`. Um erro de 0,10 m a 3 m do muro são ≈2° | **<2°** [E] |

**5. Diagnostica pela assinatura do erro.** Esta é a parte útil, porque o *padrão* do erro diz-te *qual* parâmetro está mal:

| Sintoma | Causa provável | Acção |
|---|---|---|
| Sombra simulada **mais comprida** que a real, nas duas fotos | Muro modelado **alto demais** | Confirma os 2,50 m — provavelmente é menos |
| Erro nas duas fotos **na mesma direcção azimutal** | Rotação do Norte errada no modelo | Corrige a orientação |
| Erro só na foto da **manhã** (Mai 10:59) | Geometria a **Leste** errada (varanda, fachada) | Remodela a consola |
| Erro só na foto da **tarde** (Mar 16:47) | Geometria a **Oeste** errada (muro SW, palmeira) | Remodela |
| Erro **cresce com a hora** numa só foto | Erro de **tempo/fuso**, não de geometria | Volta ao passo 1 |
| Sombra certa, **mas a penumbra é diferente** | Modelo de céu / difusa | Ajusta `-ab`, turbidez |

Nota técnica pertinente: há validação experimental publicada de métodos baseados em Radiance especificamente para **simulação de penumbras solares** [F, [Taylor & Francis 2024](https://www.tandfonline.com/doi/full/10.1080/15502724.2024.2365691)] — a nitidez da aresta de sombra é sensível ao diâmetro angular do sol (0,53°) e o Radiance trata-o bem. Se a tua penumbra simulada estiver muito mais dura que a real, é sinal de que estás a usar um sol pontual em vez de um disco.

### O limite honesto deste método
**As fotos validam geometria de sombra directa. Não validam DLI.** [E] Uma foto não mede fotões PAR — mede a resposta do sensor da câmara, com balanço de brancos automático, curva de tom, compressão JPEG, e exposição automática. Não há como extrair irradiância absoluta de um JPEG de telemóvel sem calibração radiométrica da câmara.

**Portanto:** as três fotos dão-te **alta confiança na geometria** — o que é muito, porque é a geometria que produz a obstrução, e a obstrução é o que determina tanto a directa como a difusa. Mas o passo de geometria-para-mol continua a depender dos modelos de céu e do factor PAR. **Só o medidor fecha essa lacuna.** É o argumento final a favor dos 460 €.

---

## 8. Tabela comparativa final

| Ferramenta | Licença / custo | Aprendizagem [E] | Precisão geométrica | **DLI em mol/m²/dia?** | Difusa + refletida | Vegetação sazonal | Windows | Output visual | Esforço de modelação, este caso |
|---|---|---|---|---|---|---|---|---|---|
| **`pvlib` + PVGIS** | BSD, **0 €** | **2–4 h** | Perfil de horizonte 1D, por ponto | **Com trabalho** — 1 linha de conversão | **Difusa: sim** (modelos PVGIS + Perez). Refletida: só albedo de solo | **Não** | Sim | Nenhum (gráficos matplotlib) | **Muito baixo** — nenhuma geometria 3D |
| **UMEP / SEBE (QGIS)** | GPL, **0 €** | 8–18 h | Raster; 0,05–0,10 m viável (7,5k px ≪ limite 4M) | **Com trabalho** — kWh → mol | **Sim, ambas** [F] | **Sim**, transmissividade configurável (3% def.) — mas manual por estação | Sim | Mapas raster bons | **Médio** — shapefile de muros + DSM |
| **honeybee-radiance (Python)** | AGPL/GPL, **0 €** | **15–25 h** | Exacta (NURBS/mesh) | **Com trabalho** — W/m² → mol | **Sim, excelente** — padrão-ouro | **Sim**, modificador `trans` | Sim (`C:\Radiance` + pip) | Falsa-cor Radiance | Médio |
| **VI-Suite (Blender)** | GPL v2, **0 €** | 8–15 h | Exacta | **Com trabalho** | **Sim** (Radiance) | Sim | Sim | **Excelente** | **Baixo–médio** |
| **Blender + Sun Position** | GPL, **0 €** | **2 h** | Exacta | **NÃO** | **Não** | Geometria sim, radiativo não | Sim | **Excelente** | Baixo |
| **Radiance CLI puro** | Livre (LBNL), **0 €** | **25–40 h** | Exacta | Com muito trabalho | **Sim, excelente** | Sim | Sim | Falsa-cor | Baixo (6 polígonos) mas *plumbing* alto |
| **`shapely` + código próprio** | BSD, **0 €** | 15–30 h | Tão boa quanto escreveres | Com muito trabalho | Difusa por patches: sim. **Inter-reflexão: não, na prática** | Só se programares | Sim | Nenhum | Médio–alto |
| **FreeCAD Solar WB** | LGPL-2.1, **0 €** | 5–12 h | Exacta | Talvez (em desenvolvimento) | Via Ladybug, incerto | Incerto | Sim | Razoável | Baixo. **Mas: "experimental, não recomendado para trabalho profissional"** [F] |
| **Ladybug-Blender** | AGPL, 0 € | — | — | **NÃO** — só Ladybug, sem Honeybee/Radiance [F] | **Não** | Não | Sim | — | **Excluído: alpha, última release Mai 2024** |
| **SketchUp Free (web)** | Gratuito | **1 h** | Boa | **NÃO** | **Não** | Não | Browser | Bom | **Muito baixo (20–40 min)** |
| **SketchUp Pro + Sun Diagram** | ≈379 €/ano + 45 USD [M] | 3–6 h | Boa | **NÃO** | Não | Não | Sim | Bom | Muito baixo |
| **Rhino + GH + Ladybug** | **995 €** perpétuo [M] | **4–8 h** | Exacta | **Com trabalho** | **Sim, excelente** | **Sim** | Sim | Muito bom | **Baixo** — o mais eficiente de todos, se pagares |
| **Pollination** | Subscrição, cotação [F] | 3–6 h | Exacta | Com trabalho | Sim | Sim | Sim | Muito bom | Baixo |
| **Shadowmap Pro** | £30/ano–£50/mês [M] | **<1 h** | **Volumetria global, sem os teus muros** | **NÃO** | Indirecta anunciada, não auditável | Árvores genéricas | Browser/app | Muito bom | **Nenhum — e é o problema** |
| **Sun Surveyor / PhotoPills** | ≈10–12 € [M] | **<1 h** | AR; bússola sujeita a interferência (PhotoPills permite calibração manual) [F] | **NÃO** | Não | Não | iOS/Android | AR excelente | **Nenhum** |
| **Google Earth Pro** | Gratuito | <1 h | **Insuficiente** — malha amalgama muros de 2,5 m | **NÃO** | Não | Não | Sim | Bom | Nenhum |
| **Google Solar API** | Grátis até 1.000 chamadas Data Layers [F] | 2–4 h | DSM aéreo; resolução não publicada; **orientado a telhados** | **NÃO** (kWh, e não cobre solo) | Interno, opaco | Não | Sim (API) | GeoTIFF | Nenhum. **Cobertura PT não confirmada** |
| **Blosm + Google 3D Tiles** | Add-on pago + API | — | Insuficiente | **NÃO** | Não | Não | Sim | Muito bom | **Excluído: 403 para facturação EEE desde 8 Jul 2025** [F] |
| **Meshroom / Scaniverse** | MPL / freemium | 3–6 h | **10–20 cm @95% (edifício); 2,5 cm @1 m em boas condições** [F] | **NÃO** — é captura, não simulação | Não | Capta a forma real | Sim / iOS | Muito bom | **É o produtor de geometria, não consumidor** |
| **Apogee DLI-500** | **499 USD ≈460 €** [F] | **<1 h** | N/A | **SIM — mede directamente, ±5%** [F] | **Sim, mede tudo junto** | Sim, mede o real | N/A | Nenhum | **Nenhum** |

**A coluna que decide** é a quarta. Lê-a de cima a baixo: **um único produto nesta tabela diz "SIM" sem ressalvas, e é o medidor.** Todo o software diz "com trabalho" ou "não".

---

## 9. Recomendação final — quatro vias

### Via A — MÍNIMA: `pvlib` + PVGIS
**4,5 horas · 12 € (app) · 0 € software**

Etapa 0 (verificação de campo) + Etapa 1 (pvlib com perfil de horizonte por zona). Cinco perfis de horizonte, cinco chamadas ao PVGIS, conversão PAR, tabela.

**A favor:** [E] resposta esta semana. Zero modelação 3D. A difusa deixa de ser um palpite de 20% e passa a vir dos modelos do PVGIS aplicados ao teu horizonte real sobre dados satelitários oficiais da UE — **é exactamente o parâmetro que declaraste ser o mais frágil, e é corrigido em 3 horas.** Dá componentes separadas, o que te deixa ver quanto da resposta é difusa. Ferramenta de qualidade industrial (1.218 estrelas, activa em Agosto de 2026, 700+ citações).

**Contra:** [E] o PVGIS trata o horizonte como infinitamente distante — um muro a 2,8 m não é isso, e vai subestimar ligeiramente a difusa que "espreita" pelas bordas. A refletida é o modelo de albedo de solo, não uma fachada de 15,50 m a três metros (subestima, e talvez significativamente, porque essa fachada é um reflector grande e próximo). **Nenhuma vegetação** — a palmeira e o lodão não existem. Um horizonte por zona, não um mapa.

**Faz isto: sempre, e primeiro.** Não é alternativa às outras vias — é o ponto de partida e o controlo de sanidade de todas elas. [E]

### Via B — PRAGMÁTICA: A + UMEP/SEBE
**15–25 horas · 0 € software**

A via A, mais o SEBE no QGIS a partir de um shapefile de muros que desenhas com as tuas medições.

**A favor:** [E] a melhor relação esforço/resultado com difusa + refletida + vegetação. **Cobre directa, difusa e refletida ponderada por albedo, e vegetação com transmissividade configurável** — a tríade completa mais as copas, documentado oficialmente [F]. Dá **mapas por píxel**, não valores por ponto: vês o gradiente dentro de cada zona, o que é mais informativo que cinco números. Resolução de 5–10 cm sem problema computacional. Testa a sensibilidade 2,50/3,00 m editando um atributo. Interface gráfica; nenhum código obrigatório. Projecto vivo com consórcio académico e reescrita em Rust em curso.

**Contra:** [E] frustração de *plumbing* SIG: cinco rasters com extensão e resolução idênticas, EPSG:3763, formatos meteorológicos UMEP. Transmissividade não-sazonal — duas corridas manuais. E o modelo não é reutilizável para nada mais: um raster de QGIS não te serve para desenhar iluminação nocturna.

### Via C — COMPLETA: A + fotogrametria + VI-Suite ou honeybee-radiance
**30–45 horas · 0 € software (+460 € medidor)**

Etapas 0 a 7 completas. Fotogrametria do espaço real, geometria limpa no Blender, Radiance via VI-Suite (mais fácil) ou honeybee-radiance (mais controlo), validação com as fotos EXIF, calibração com o medidor.

**A favor:** [E] é a única via que produz **um activo, não só um número.** Tens um modelo 3D métrico do teu quintal, derivado da realidade, com os muros verdadeiros, a palmeira medida, a varanda, as copas com transmissividade sazonal. Esse modelo serve para: DLI por zona e estação; estudo de iluminação cénica nocturna (o Radiance simula luminárias tão bem como o sol — é literalmente o que a indústria de iluminação usa); posicionamento de plantas por necessidade de luz; visualização do desenho para terceiros; e teste de qualquer intervenção futura (uma pérgula, mover o canteiro, podar a palmeira) sem construir nada. Motor validado contra CIE 171:2006 com MBE <13% documentado. E as fotos EXIF que já tens dão-te validação geométrica independente.

**Contra:** [E] 30–45 horas. E há um risco de projecto que devo nomear: **a tentação de refinar o modelo em vez de decidir a relva.** Já te assinalaste essa preocupação noutro contexto (a regra O10 sobre iteração de mockup a substituir execução pendente). Esta via é exactamente o tipo de trabalho que pode absorver três fins-de-semana e devolver a mesma decisão que a via A devolveria em três horas.

### Via D — EMPÍRICA: medidor DLI-500
**1,5 h de trabalho + 14 dias de espera por estação · ≈460 €**

**A favor:** [F] ±5% de incerteza de calibração, rastreabilidade NIST, 99 dias de armazenamento automático de DLI e fotoperíodo, 4 anos de garantia. Mede fotões PAR reais: resolve de uma vez a difusa obstruída, a refletida, o factor PAR, a atmosfera de Alcântara e a névoa do Tejo. **Não há incerteza de modelação porque não há modelo.**

**Contra:** [E] uma zona por posição de sensor (mover o sensor multiplica o tempo pelas zonas, ou compras vários). Precisas de Junho e Dezembro para os extremos, e hoje é 15 de Setembro — logo a resposta completa é Junho de 2027. Não te diz nada sobre o que aconteceria se mudasses alguma coisa. Não serve para o projecto de desenho.

### O que recomendo, explicitamente

**Recomendo A + D em paralelo, imediatamente, e B ou C só se A+D não decidirem.**

O raciocínio: [E]

1. **Encomenda o DLI-500 hoje** (15 min, 460 €). Chega em duas semanas. Mede 7 dias em Outubro. Outubro não é Junho nem Dezembro, **mas é um ponto de calibração real**, e um ponto real vale mais que um modelo inteiro sem ancoragem.
2. **Faz a via A esta semana** (4,5 h). Obtém a tabela de DLI com difusa modelada pelo PVGIS.
3. **Quando o medidor tiver 7 dias de Outubro, compara.** Se a via A previr Outubro com erro <15%, **confia na via A para Junho e Dezembro** e decide a relva. Fim.
4. **Se divergirem mais de 25%**, então tens um problema real de modelação — e aí sim vale a pena a via B (mais barata em horas) ou C.

**Porque esta ordem e não outra:** porque a tua pergunta é binária em dois limiares (<10 mol: nenhuma gramínea; >15 mol: abre-se outra família). A tua estimativa actual é 25–28 mol no Verão. **Estás a 67% de margem acima do limiar superior.** Para uma decisão com essa margem, uma simulação de ±25% já decide. Não precisas de ±8% para saber que 25 > 15. **O sítio onde precisas de precisão é o Inverno**, onde 6,7 mol da 'JaMur' está perto do que um quintal com 1,1 h de sol directo em Dezembro pode dar — e o Inverno é precisamente onde o medidor em Dezembro te dá a resposta definitiva, e onde a difusa (que é quase tudo o que há em Dezembro) domina.

### Sob que condição mudaria de recomendação

| Condição | Muda para |
|---|---|
| A via A der Verão entre **12 e 18 mol** (zona de indecisão sobre o limiar de 15) | **Via B**, urgente. Precisas da refletida da fachada e da difusa geometricamente correcta, e o PVGIS não as dá |
| A via A der Inverno **próximo de 6–8 mol** em qualquer zona | **Via D é obrigatória**, com medição em Dezembro. Nenhuma simulação decide nesta margem |
| Decidires avançar a sério com a iluminação cénica e a arte UV | **Via C**, e o custo passa a justificar-se pelo duplo uso. O Radiance é a ferramenta da indústria de iluminação |
| Tiveres ou adquirires **Rhino** | **Via C via Grasshopper**, e o tempo cai de 30–45 h para 12–18 h |
| O medidor de Outubro divergir >25% da via A | **Via B**, para descobrir *porquê* — e suspeita primeiro da refletida da fachada |
| Não quiseres gastar 460 € | **Via B**, e aceita ±25% sem validação empírica. Defensável, mas não verificado |
| Precisares da resposta em 48 h | **Via A, só.** É a única que cabe nesse prazo |

---

## 10. Por confirmar

### Bloqueantes — tens de resolver antes de confiar em qualquer número

1. **A altura real dos quatro muros.** [F: conflito documentado — corte 3,00 m vs observação 2,50 m] Mede com fita em três pontos por muro, a partir do solo do jardim, **não** a partir da cota do vizinho. Sabes que isto duplica a média de Dezembro. É a medição mais rentável que podes fazer, e leva 20 minutos.

2. **A altura e o diâmetro de copa da palmeira.** [F: não medidos] A *Phoenix canariensis* está em X≈11,6 · Y≈3,0, na zona que já tem o pior Inverno (0,1 h). Sem este número, a zona SW não é modelável. Triangulação com a app de inclinómetro: 10 minutos.

3. **A altura real do lodão** (≈5 m é estimativa) e as datas de foliação e queda em Alcântara. [F: folha caduca, despido em Dez-Jan] Para a transmissividade sazonal precisas de saber **quando** muda, não só que muda. Observação própria ou registo local.

4. **O timestamp e o fuso das três fotos EXIF.** Um erro de 1 h desloca o azimute 15° e invalida a validação toda. Cruza `DateTimeOriginal` com `GPSTimeStamp` (que é sempre UTC).

5. **O factor PAR a usar.** [F: 0,45–0,50 × 4,6 µmol/J; combinado 2,02–2,3] Escolhe um, justifica, e **corre todos os cálculos com ambos os extremos** para ter a barra de erro explícita. Um medidor resolve isto definitivamente.

### Só se sabe instalando

6. **Se o `pip install lbt-honeybee` corre limpo no teu Windows 10** com a tua versão de Python. [F: requer Python 3.6+, Radiance em `C:\Radiance`, verificação com `honeybee-radiance --help`] Há relatos de fórum de "Radiance installation not found" [F, [McNeel Forum](https://discourse.mcneel.com/t/ladybugtools-radiance-installation-not-found/131860); [Ladybug Discourse](https://discourse.ladybug.tools/t/radiance-installation/15395)]. 30 minutos para descobrir.

7. **Se o VI-Suite master funciona com a tua versão de Blender.** [F: relatos de OK com 4.4 em Linux e Windows; vi-suite07 é "experimental" para 5.1] Escolhe **Blender 4.4 com o master**, não 5.1 com o experimental. 1 hora.

8. **Se o UMEP DSM Generator aceita polígonos de muro com 0,18 m de espessura** a resolução de 0,10 m sem artefactos de rasterização. [E: um muro de 0,18 m a 0,10 m/píxel são 1,8 píxeis — está no limite] Se der problemas, usa 0,05 m (30k píxeis, ainda trivial) ou modela os muros com espessura de 0,20 m.

9. **A qualidade da reconstrução fotogramétrica da palmeira.** [E: espero nuvem ruidosa] Só scanning diz. E confirma o bug dos espaços no caminho do Meshroom 2025.1.0 [F].

10. **Se o Scaniverse ou o Polycam dão escala absoluta fiável no teu telefone.** [F: 10–20 cm @95% à escala de edifício; 2,5 cm @1 m em boas condições; Scaniverse 10% vs Polycam 43% de erro num estudo] Depende de teres LiDAR. **Confirma se o teu telefone tem LiDAR** — se não tiver, é Meshroom com marcas de escala.

### Só se sabe testando a API

11. **Cobertura da Google Solar API em Lisboa.** [F: expansão documentada para DE, UK, FR, ES, IT, Florida — **Portugal não listado**] Uma chamada `curl` com `requiredQuality=BASE` responde em 15 min. **Nota: mesmo que haja cobertura, concluí que não serve** (telhados, kWh, DSM aéreo sem os teus muros). Confirma por completude, não por esperança.

12. **A resolução real do DSM da Solar API.** [F: não publicada na documentação; existe parâmetro `pixelSizeMeters` sem valores listados] Idem.

### Só se sabe medindo no local

13. **O DLI real.** [E] É a pergunta original e nenhum software a responde sem a conversão espectral. O DLI-500 responde com ±5%.

14. **A reflectância real dos teus muros e da fachada.** [E] O parâmetro mais influente depois da geometria, num espaço fechado. Um muro branco de cal tem ρ≈0,7; rebocado cinza ρ≈0,3; tijolo ρ≈0,25. **Num quintal com uma fachada de 15,50 m a três metros, a diferença entre 0,3 e 0,7 pode valer vários mol/m²/dia.** Fotografa uma carta de cinzas 18% ao lado de cada superfície, ou mede com o próprio DLI-500 apontado à parede.

15. **O desvio magnético dentro do quintal.** [F: interferência magnética documentada como problema de AR; PhotoPills permite calibração manual] Compara o azimute da bússola do telefone com o azimute solar calculado à hora certa. Se divergir >5°, calibra manualmente e não confies na bússola para mais nada.

16. **Se o Arcascope tem algum produto de análise solar arquitectónica.** [E] Não o encontrei nesta investigação — a Arcascope que conheço faz apps de ritmo circadiano. Pode ser confusão de nome com outra ferramenta.

---

## Anexo — Ligações verificadas

**Ladybug Tools / Radiance**
[PyPI ladybug-tools](https://pypi.org/user/ladybug-tools/) · [honeybee](https://github.com/ladybug-tools/honeybee) · [honeybee-radiance](https://github.com/ladybug-tools/honeybee-radiance) · [PyPI honeybee-radiance](https://pypi.org/project/honeybee-radiance/1.66.106) · [Instalação (DeepWiki)](https://deepwiki.com/ladybug-tools/honeybee-radiance/1.1-installation-and-setup) · [ladybug-blender (alpha, Mai 2024)](https://github.com/ladybug-tools/ladybug-blender/) · [Ladybug Primer — Direct Sun Hours](https://docs.ladybug.tools/ladybug-primer/components/3_analyzegeometry/direct_sun_hours) · [Incident Radiation](https://docs.ladybug.tools/ladybug-primer/components/3_analyzegeometry/incident_radiation) · [HB Annual Irradiance](https://docs.ladybug.tools/hb-radiance-primer/components/3_recipes/annual_irradiance) · [Radsite — Learn](https://www.radiance-online.org/learning) · [rtrace man page](https://www.radiance-online.org/learning/documentation/manual-pages/pdfs/rtrace.pdf) · [NREL/Radiance](https://github.com/NREL/Radiance) · [bifacial_radiance](https://github.com/NREL/bifacial_radiance) · [Pollination pricing](https://www.pollination.solutions/pricing)

**Blender**
[Sun Position — Manual](https://docs.blender.org/manual/en/2.83/addons/lighting/sun_position.html) · [Sun Position — Extensions](https://extensions.blender.org/add-ons/sun-position/) · [SAE 2024-01-2476 — validação de sombras](https://www.sae.org/publications/technical-papers/content/2024-01-2476/) · [VI-Suite](https://blogs.brighton.ac.uk/visuite/) · [vi-suite07 (Blender 5.1)](https://github.com/rgsouthall/vi-suite07) · [VI-Suite — OSArch wiki](https://wiki.osarch.org/index.php?title=VI-Suite)

**QGIS / UMEP**
[UMEP](https://github.com/UMEP-dev/UMEP) · [UMEP for processing 2.0.13](https://plugins.qgis.org/plugins/processing_umep/version/2.0.13/) · [SEBE — manual](https://umep-docs.readthedocs.io/en/latest/processor/Solar%20Radiation%20Solar%20Energy%20on%20Building%20Envelopes%20(SEBE).html) · [SEBE — tutorial](https://umep-docs.readthedocs.io/projects/tutorial/en/latest/Tutorials/SEBE.html) · [DSM Generator](https://umep-docs.readthedocs.io/projects/tutorial/en/latest/Tutorials/DSMGenerator.html) · [SOLWEIG](https://umep-docs.readthedocs.io/en/latest/OtherManuals/SOLWEIG.html) · [solweig em Rust](https://github.com/UMEP-dev/solweig)

**Python**
[pvlib-python](https://github.com/pvlib/pvlib-python) · [Wikipedia — pvlib](https://en.wikipedia.org/wiki/Pvlib_python) · [get_pvgis_hourly](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.iotools.get_pvgis_hourly.html) · [perez_driesse](https://pvlib-python.readthedocs.io/en/latest/reference/generated/pvlib.irradiance.perez_driesse.html) · [sky_diffuse_passias](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.shading.sky_diffuse_passias.html) · [PVGIS hourly radiation](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/pvgis-tools/hourly-radiation_en) · [PVGIS online tool](https://joint-research-centre.ec.europa.eu/pvgis-online-tool_en)

**Google — restrições**
[Issue #644 Blosm — 403 EEE](https://github.com/vvoovv/blosm/issues/644) · [Google — Map Tiles API EEA adjustments](https://developers.google.com/maps/comms/eea/map-tiles) · [Photorealistic 3D Tiles overview](https://developers.google.com/maps/documentation/tile/3d-tiles-overview) · [Earth Studio Best Practices](https://earth.google.com/studio/docs/best-practices/) · [Solar API overview](https://developers.google.com/maps/documentation/solar/overview) · [Solar API — Data Layers](https://developers.google.com/maps/documentation/solar/data-layers) · [Solar API — billing](https://developers.google.com/maps/documentation/solar/usage-and-billing) · [Expanded Coverage](https://developers.google.com/maps/documentation/solar/expanded-coverage) · [MapsModelsImporter](https://github.com/eliemichel/MapsModelsImporter) · [MapsModelsImporter-Enhanced](https://github.com/Sheep-max/MapsModelsImporter-Enhanced) · [Map Tiles API Policies](https://developers.google.com/maps/documentation/tile/policies)

**Fotogrametria**
[Meshroom 2025.1.0](https://github.com/alicevision/Meshroom/releases/tag/v2025.1.0) · [Meshroom releases](https://github.com/alicevision/meshroom/releases) · [MDPI — precisão LiDAR iPhone 13 Pro](https://www.mdpi.com/2673-7418/3/4/30) · [ScienceDirect — Polycam vs Scaniverse](https://www.sciencedirect.com/science/article/pii/S1877050925026742) · [J.S. Held — LiDAR móvel vs scanning terrestre](https://www.jsheld.com/insights/articles/a-comparison-of-mobile-phone-lidar-capture-and-established-ground-based-3d-scanning-methodologies) · [COLMAP vs Meshroom](https://link.springer.com/chapter/10.1007/978-3-032-13056-3_38)

**DLI, PAR e turfgrass**
[Apogee DLI-500 — 499 USD](https://www.apogeeinstruments.com/dli-500-par-daily-light-integral-and-photoperiod-meter-full-spectrum-400-700-nm/) · [Apogee — DLI explicado](https://www.apogeeinstruments.com/daily-light-integral-measuring-light-for-plants/) · [bigleaf Rg.to.PPFD](https://search.r-project.org/CRAN/refmans/bigleaf/html/Rg.to.PPFD.html) · [Springer — fFEC / fracção PAR](https://link.springer.com/article/10.1007/s00704-010-0368-6) · [Wikipedia — DLI](https://en.wikipedia.org/wiki/Daily_light_integral) · [Virginia Tech — guia DLI](https://www.pubs.ext.vt.edu/SPES/spes-720/spes-720.html) · [Texas A&M — DLI Zoysia/Bermuda (tese)](https://oaktrust.library.tamu.edu/items/edc2d7fd-3030-4cc4-8e27-118621df244b) · [Crop Science — Chen 2021](https://acsess.onlinelibrary.wiley.com/doi/abs/10.1002/csc2.20515) · [USGA — Minimum DLI](https://www.usga.org/course-care/green-section-record/57/19/minimum-daily-light-integrals.html) · [USGA — DLI para gramíneas de estação quente](https://www.usga.org/content/usga/home-page/course-care/green-section-record/59/16/how-much-light-is-enough--daily-light-integral-requirements-for-.html)

**Validação**
[Taylor & Francis — penumbras solares em Radiance](https://www.tandfonline.com/doi/full/10.1080/15502724.2024.2365691) · [ScienceDirect — validação empírica Ladybug/Honeybee](https://www.sciencedirect.com/science/article/abs/pii/S0038092X20307866) · [Comparação Radiance vs medições in situ](https://www.academia.edu/36795005/)

**Comerciais / campo**
[Rhino — preços Europa](https://www.rhino3d.com/sales/europe/) · [SketchUp — planos](https://sketchup.trimble.com/en/plans-and-pricing) · [Sun Diagram Pro — 45 USD](https://febhouse.gumroad.com/l/Sundiagram) · [Curic Sun](https://www.suapp.com/en/plugin/400) · [Shadowmap — preços](https://shadowmap.org/pricing) · [Shadowmap API](https://shadowmap.org/api) · [Sun Surveyor](https://spark.mwm.ai/us/apps/sun-surveyor-sun-moon/525176875) · [PhotoPills — calibração manual de AR](https://www.photopills.com/blog/update-photopills-2-1-1) · [Bellingcat — Shadowmap](https://bellingcat.gitbook.io/toolkit/more/all-tools/shadowmap)

**Outros**
[FreeCAD Solar Workbench](https://github.com/Francisco-Rosa/Solar) · [OSArch — FreeCAD Solar + Ladybug](https://community.osarch.org/discussion/2937/freecad-solar-workbench-using-ladybug-tools) · [Blender-osm — OSM wiki](https://wiki.openstreetmap.org/wiki/Blender-osm) · [Daysim](https://github.com/reyery/Daysim)

---

## Nota de processo para o Arquitecto

Três observações sobre o enquadramento desta pesquisa no governo do repositório, que deixo à consideração e não decido:

1. **Este relatório não contém decisões.** Por G1, nada aqui existe até passar a `ESTADO.md`. A decisão candidata — "via de modelação solar adoptada" — é do Arquitecto, não desta pesquisa.

2. **Itens 1 a 5 da secção 10 são medições de campo, não de software.** Alturas de muro, altura e copa da palmeira, altura do lodão e datas de foliação. Por G18 pertencem a `10-LOCAL/` como factos do existente. São **bloqueantes de qualquer via**, incluindo a via mínima de 4,5 horas. Sugiro que entrem em `INBOX.md` como pendência de campo, com prioridade acima da escolha de ferramenta — porque escolher software antes de medir os muros é optimizar o instrumento errado.

3. **O conflito documentado de 3,00 vs 2,50 m merece registo formal.** Já tem consequência quantificada (duplicou a média de Dezembro) e a adopção de 2,50 m é uma decisão de facto que, se não estiver em `ESTADO.md`, existe só na conversa. Por G1, convém que exista.

E uma observação substantiva, por O3: **a tentação, depois de um relatório destes, é construir o modelo completo.** A via C é sedutora e é tecnicamente a melhor. Mas a tua pergunta tem 67% de margem acima do limiar de decisão de Verão, e o que falta para o Inverno resolve-se com um aparelho de 460 € e sete dias em Dezembro. Argumento contra a via C como primeiro passo — não contra a via C em absoluto, que se justifica plenamente quando a iluminação cénica entrar em projecto.