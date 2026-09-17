---
created: 2026-09-17
thread: T005
tipo: pesquisa
summary: |
  Levantamento de software para modelar o Jardim de Alcântara (~75 m²) como "digital twin"
  experimental — caracterização do existente + simulação de cenários (sombra, água, vista,
  crescimento). Cobre nove eixos: geometria/BIM, sol/sombra, vegetação, água/drenagem,
  microclima, iluminação nocturna, captura da realidade, plataformas "digital twin" e
  cola/automação Python. Conclui que não existe uma plataforma única de "digital twin" a
  esta escala — o termo é, na prática, uma combinação manual de 3-5 ferramentas ligadas por
  scripts Python, com re-importação de geometria sempre que algo muda. Confirma a conclusão
  anterior sobre fotogrametria/LiDAR: para muros lisos, telémetro laser vence qualquer app;
  para copas de árvores, LiDAR de iPhone Pro serve com erro de dezenas de cm (10-56 cm
  consoante o estudo). Recomenda pilha equilibrada: Rhino + Grasshopper + Ladybug/Honeybee
  como espinha dorsal paramétrica-solar, com The Grove (Blender) para a copa real da
  palmeira e DIALux evo para a componente nocturna.
---

# Software para Digital Twin do Jardim — Caracterização e Experimentação

## 0. Enquadramento e método

Esta pesquisa responde a uma pergunta operacional, não académica: **que ferramentas permitem testar "se eu puser esta árvore aqui, o que acontece à sombra / à água / à vista?" repetidamente, sem recomeçar de zero em cada iteração?**

Foram excluídas à partida ferramentas que só desenham (sem simular) e ferramentas que só simulam com geometria pré-cozinhada sem permitir alterar parâmetros. A pesquisa assume Windows 10 como plataforma principal e assinala sempre que uma ferramenta é macOS-only ou Linux-only — nesses casos, a ferramenta está efectivamente eliminada, não apenas penalizada.

Todos os preços e versões foram verificados via pesquisa web em Setembro de 2026. Onde não foi possível confirmar um valor, está marcado **"não apurado"**.

---

## 1. Geometria e modelação base (CAD/BIM)

A pergunta central deste eixo: qual ferramenta aguenta ser a **espinha dorsal paramétrica** — o modelo único de onde tudo o resto deriva, sem reconstrução manual a cada iteração?

| Ferramenta | Licença/custo | Plataforma | Curva de aprendizagem | Maturidade | Nota |
|---|---|---|---|---|---|
| **Blender** | Gratuito, open source | Win/Mac/Linux | Média-alta (interface própria, enorme comunidade) | Muito madura, activamente desenvolvida | Modelação livre + add-ons de vegetação (Sapling, The Grove) + motor de render (Cycles/EEVEE) no mesmo pacote |
| **SketchUp** (Free/Pro) | Free (web, limitado) / Pro ≈ $299-799/ano | Win/Mac | Baixa — a mais acessível do mercado | Muito madura | Fraca em paramétrico nativo; ganha poder com plugins |
| **FreeCAD** | Gratuito, open source | Win/Mac/Linux | Alta — interface confusa, mas verdadeiramente paramétrico | Madura, desenvolvimento activo (v1.0 em 2024) | Motor paramétrico genuíno de graça, mas sem ecossistema de plugins de paisagismo/solar comparável a Rhino |
| **Rhino + Grasshopper** | Rhino ≈ $995 licença perpétua (não apurado para 2026); Grasshopper incluído | **Windows nativo** (Mac atrasado em plugins) | Rhino: baixa-média. Grasshopper: alta (programação visual) | Muito madura, standard de facto em computational design | **É a única combinação que liga nativamente geometria → análise solar (Ladybug/Honeybee) → paisagismo (Lands Design) — sem sair do ambiente.** Licença perpétua, não subscrição |
| **Revit** | Subscrição Autodesk, ≈ $2.500-2.900/ano | Windows apenas | Alta | Muito madura | BIM de edifícios, não de jardins — sobredimensionado e mal talhado para paisagismo puro |
| **Vectorworks Landmark** | ≈ $128/mês anual ($1.530/ano) | Win/Mac | Média | Madura, módulo de paisagismo dedicado com base de dados horticultural | Única ferramenta **desenhada de raiz para paisagismo profissional**. Preço elevado para uso doméstico |

**Lands Design / RhinoLands** (plugin Rhino dedicado a paisagismo): a partir de **$779** licença perpétua, sem subscrição. Traz terreno, floresta, rega e simulação de sombra/estações integradas no Rhino.

**Conclusão do eixo:** Rhino + Grasshopper é a única espinha dorsal que liga nativamente aos eixos 2 (solar) e 9 (automação) sem middleware. FreeCAD é a alternativa gratuita, mas fica isolado — não há Ladybug para FreeCAD. Blender é o melhor terreno para vegetação realista (eixo 3), mas fraco em análise quantitativa nativa.

---

## 2. Sol, sombra e radiação

| Ferramenta | Licença/custo | Plataforma | Vegetação real (não caixas) | Maturidade |
|---|---|---|---|---|
| **Ladybug + Honeybee** (Grasshopper/Rhino) | Gratuito, open source | Windows (Rhino nativo Win) | **Sim** — qualquer malha 3D pode ser objecto de sombreamento, incluindo copas modeladas como geometria real. Sunlight Hours Analysis calcula horas de sol directo sobre qualquer geometria, árvore incluída | Muito madura, referência académica, validada empiricamente contra medições de campo |
| **Radiance** | Gratuito, open source | Win/Mac/Linux (linha de comandos) | Sim, ray-tracing genuíno — motor por trás do Honeybee e do DIALux/Relux | Muito madura (décadas), motor de referência da indústria |
| **ClimateStudio** (plugin Rhino) | Preço sob consulta — **não apurado** | **Windows apenas** | Sim, herda o motor Radiance/EnergyPlus | Madura, usada em escritórios profissionais; interface mais polida que Ladybug, mas fechada/paga |
| **Autodesk Forma** | $185/mês ou $1.445/ano standalone | Cloud (browser) | Trata vegetação "como qualquer outra geometria" no cálculo solar; no vento usa densidade de área foliar fixa (0,25) — aproximação, não copa real | Madura, desenvolvimento activo rápido |
| **pvlib / pysolar** (Python) | Gratuito | Qualquer SO | Não fazem sombreamento 3D nativo — calculam posição solar e irradiância; sombreamento por geometria exige combinar com trimesh/pyvista | Muito maduras, pvlib é standard da indústria fotovoltaica |

**Nota crítica confirmada pela pesquisa:** o eixo 3 (vegetação) não é acessório deste eixo — é decisivo. Ladybug/Honeybee aceitam qualquer malha como obstrução solar; a precisão do resultado depende inteiramente de a copa ser modelada como volume real e não como cilindro. Um cilindro sobre-estima sombra no centro e sub-estima nas margens; uma copa irregular (como a palmeira real) produz um padrão de sombra fragmentado que um cilindro nunca reproduz.

O modelo solar Python já existente (geometria NOAA) resolve posição do sol e ângulos; **não resolve sombreamento por geometria 3D complexa.** Para isso, a via natural é alimentá-lo com uma malha (trimesh) e projectar raios, ou migrar o cálculo de sombra para Ladybug/Honeybee, que já têm o motor construído.

---

## 3. Vegetação e crescimento — o eixo mais subestimado

| Ferramenta | Licença/custo | Plataforma | Realismo de copa | Estado de manutenção |
|---|---|---|---|---|
| **Sapling Tree Gen** (add-on Blender) | Gratuito, incluído no Blender | Win/Mac/Linux | Procedural genérico (algoritmo Weber & Penn), não são espécies reais nomeadas | Versão melhorada da comunidade no GitHub; o original tem décadas e pouca manutenção oficial — **comunidade, não fabricante** |
| **Arbaro** | Gratuito, open source (Java) | Win/Mac/Linux | Mesmo algoritmo de base (Weber & Penn) | SourceForge sem actividade recente confirmada — **provável abandonware** |
| **The Grove 3D** | Comercial — **preço não apurado** | Blender e Houdini | **Crescimento procedural genuíno com simulação de luz/competição por espaço** — simula como o ramo cresce em direcção à luz. O mais avançado para representar como a copa se desenvolveria num espaço com sombra de muros | Activamente desenvolvido |
| **Laubwerk Plants Kits** | Por pacote — **preço não apurado** | 3ds Max, Maya, C4D, SketchUp | Modelos de espécies reais fotografados, com variantes sazonais e LOD | **Sem confirmação de actualização recente em 2026** — risco de estagnação |
| **SpeedTree** | Indie $199/ano; Pro $499-899/ano; bibliotecas +$999/ano | Win/Mac | Alto realismo visual, orientado a jogos/VFX — espécies genéricas parametrizáveis | Muito activo, SpeedTree 10 em 2024 |

**Avaliação para este projecto:** nenhuma destas ferramentas tem uma "palmeira das Canárias específica com esta copa" pronta a importar com garantia solar. A via realista é: (1) obter a geometria aproximada real por LiDAR grosseiro (aceitando o erro de dezenas de cm), **ou** (2) usar The Grove/Sapling para gerar uma copa parametricamente plausível e **ajustar à silhueta observada em fotografia**. A segunda via é mais barata e provavelmente mais rigorosa do que tentar escanear uma copa de palmeira com um iPhone.

---

## 4. Água, drenagem e escoamento

| Ferramenta | Licença/custo | Plataforma | Escala adequada a 75 m²? |
|---|---|---|---|
| **EPA SWMM** | Gratuito, domínio público (EPA) | Windows nativo | Sim — tem categorias de LID dedicadas a **Green Roof** e **Rain Garden**, configuráveis directamente. Estudos publicados validam o uso em telhados verdes de escala pequena (Nash-Sutcliffe 0,70-0,89 em calibração) |
| **PCSWMM** (interface comercial sobre SWMM) | Comercial — **não apurado** | Windows | Desproporcionado face ao SWMM gratuito |

**Avaliação:** o jardim sobe +0,50 m sobre laje — isto é, estruturalmente, **uma cobertura verde em escala doméstica.** O SWMM com módulos Green Roof/Rain Garden é a ferramenta correcta e gratuita. Não há necessidade de ferramenta comercial — SWMM é o standard usado inclusive em investigação académica de telhados verdes de pequena escala.

---

## 5. Microclima e conforto térmico

| Ferramenta | Licença/custo | Plataforma | Resolução | Realista para 75 m²? |
|---|---|---|---|---|
| **ENVI-met** | ≈ **3.000 €/ano** comercial | Windows | Até 0,5 m, modela árvores em 3D, trocas de calor solo-planta-ar | Tecnicamente sim, mas o custo anual é **desproporcionado** para projecto doméstico único |
| **UMEP** (plugin QGIS) | **Gratuito**, open source | Win/Mac/Linux | Requer QGIS 4.0+ (versão em desenvolvimento activo à data) | Sim, alternativa directa e gratuita |
| **SOLWEIG** (dentro do UMEP) | Gratuito | Win/Mac/Linux | 1 m, calcula Temperatura Radiante Média, UTCI, PET, Sky View Factor | **É a ferramenta certa.** Aplicações documentadas incluem exactamente "comparar cenários de plantação de árvores" |
| **OpenFOAM** | Gratuito, open source | Linux nativo (Win via WSL2) | CFD completo | Poderoso a mais, curva elevada para o retorno |
| **SimScale** | **Gratuito no Community**: 10 simulações, até 3.000 core-hours | Cloud (browser) | CFD via browser | Nível gratuito plausivelmente suficiente para uma simulação de vento pontual |

**Avaliação:** SOLWEIG/UMEP é o par correcto — gratuito, mantido por consórcio universitário (Gotemburgo/Helsínquia/Reading), e literalmente desenhado para a pergunta *"que acontece ao conforto térmico se eu plantar esta árvore aqui"*. ENVI-met é a referência do sector, mas o custo anual não se justifica para uso único e doméstico.

---

## 6. Luminância e iluminação nocturna

| Ferramenta | Licença/custo | Plataforma | Maturidade |
|---|---|---|---|
| **DIALux evo** | **Gratuito** (todas as funções core, incluindo uso comercial) | Windows nativo | Muito madura — DIALux evo 14, actualizações regulares em 2026. Importa modelos 3D; +2,5 milhões de luminárias de 450+ fabricantes |
| **ReluxDesktop** | **Gratuito** | Windows | Muito activa — 2026.2 com ferramentas 2D-para-3D; forte no mercado europeu |
| **AGi32** | ≈ $990/ano utilizador único; ≈ $1.490/ano multi | Windows | Muito madura, referência norte-americana |
| **Radiance** | Gratuito | Win/Mac/Linux (CLI) | O motor mais rigoroso fisicamente, mas exige scripting |

**Avaliação:** DIALux evo é a escolha óbvia — gratuito, maduro, importa modelos 3D existentes, e tem exactamente o caso de uso *"planear jardins com precisão, posicionar luminárias, minimizar poluição luminosa e encandeamento"*. Não há razão para pagar AGi32 aqui.

---

## 7. Captura da realidade — fotogrametria e LiDAR

Esta pesquisa **confirma** a conclusão da pesquisa anterior, com dados adicionais:

- Estudo de 2026 com iPhone 13 Pro em documentação de edifícios: para a app **Scaniverse**, desvio médio de **44 cm** e RMSE de **56 cm** face a laser scanning terrestre — significativamente pior que outras apps no mesmo hardware.
- Estudos gerais situam a exactidão LiDAR de iPhone em **10-20 cm a 95% de confiança**, sublinhando que "a escolha de software e o tipo de cena dominam o resultado, mesmo no mesmo hardware".
- Estudo de campo com iPhone 17 Pro + Scaniverse (Julho 2026, raízes de pinheiro): RMSE de 22,2 cm (8,4%).

**Nada contraria a conclusão anterior.** Para muros lisos rebocados, um telémetro laser (20-40 €, ±1,5 mm) continua a vencer qualquer solução de software **por ordens de magnitude**. Para copas (superfícies irregulares com textura natural — o caso favorável), o erro de dezenas de cm é aceitável para estudo de sombra aproximado, mas **não é dado de projecto rigoroso** — é ponto de partida para modelar manualmente (eixo 3), não um scan definitivo.

---

## 8. Plataformas integradas de "digital twin" — cepticismo obrigatório

Pesquisa directa por "digital twin" + jardim residencial devolveu três tipos de resultado:

1. **Conteúdo de marketing/blog** que usa a expressão para descrever, na prática, exactamente a combinação de ferramentas desta pesquisa — sem que exista um produto único que a entregue integrada.
2. **Plataformas de escala urbana/industrial** — operam a escala de bairro/cidade, com equipas e orçamentos incomparáveis a 75 m².
3. **Software de paisagismo doméstico** (GardenBox 3D, SimLab VR Garden, Houseplan) que por vezes se auto-descreve como "digital twin" mas é um visualizador 3D com biblioteca de plantas — **não simula sombra dinâmica, água ou crescimento com rigor físico.** É desenho bonito, não experimentação.

**Veredicto sobre o termo:** a esta escala, "digital twin" não é um produto que se compra — é uma **arquitectura de ficheiros e scripts** que o utilizador monta: um modelo geométrico único (Rhino/Blender) como fonte de verdade, alimentando motores especializados (Ladybug para sol, SOLWEIG para microclima, SWMM para água, DIALux para luz), com reexportação sempre que a geometria muda. **Quem vende "digital twin" chave-na-mão para jardins domésticos está a vender visualização, não simulação.**

---

## 9. Cola e automação

| Ferramenta | Função no workflow | Estado |
|---|---|---|
| **pvlib** (Python) | Posição solar, irradiância, submódulo `shading` | Muito madura, standard da indústria solar |
| **trimesh** | Carregar/gerar/manipular malhas triangulares; interopera com Shapely e PyVista | Muito madura, activa |
| **shapely** | Geometria 2D (polígonos de zonas, áreas de sombra projectada) | Standard de facto |
| **pyvista** | Visualização e processamento de malhas 3D | Muito madura, activa |
| **rasterio** | Dados raster geoespaciais (exportar mapas do SOLWEIG) | Standard geoespacial |
| **Grasshopper** | Cola nativa dentro do Rhino — liga geometria a Ladybug/Honeybee/Lands Design | Ver eixo 1 |
| **Dynamo** | Equivalente para Revit — só relevante se Revit entrar pela casa | Madura |

**Avaliação:** para quem já tem o modelo solar próprio em Python validado, o caminho de menor atrito é **não abandonar Python** — usar trimesh para importar geometria (via OBJ/glTF) e projectar sombras com o motor NOAA existente, reservando Ladybug/Honeybee para quando for preciso radiação acumulada rigorosa. Evita duplicar esforço e mantém **uma única fonte de verdade geométrica.**

---

## 10. Interoperabilidade — onde a informação morre

| Formato | Bom para | Onde perde informação |
|---|---|---|
| **OBJ** | Geometria pura, universalmente suportado | Sem metadados semânticos — "palmeira" chega como triângulos anónimos |
| **glTF/GLB** | Geometria + materiais + hierarquia | Sem semântica de domínio; ecossistema de análise solar suporta-o pior que OBJ |
| **IFC** | BIM de edifícios, rico em metadados | Standard de **edifícios**, não paisagismo — árvores e terreno não têm classes IFC maduras. Forçar o jardim em IFC é usar a ferramenta errada |
| **gbXML** | Geometria para simulação energética | Produz frequentemente inconsistências que distorcem a simulação — perdas confirmadas mesmo entre ferramentas do mesmo fabricante |
| **CityGML** | Modelos urbanos à escala de cidade | Sobredimensionado para 75 m² |

**Conclusão do eixo:** a travessia mais limpa é **Rhino/Blender → nativo Grasshopper → Ladybug/Honeybee** (mesmo ecossistema, sem exportação intermédia); e **exportação manual de geometria simplificada → SWMM/SOLWEIG** (que recebem polígonos/rasters, não malhas 3D complexas). Não há formato único que atravesse os nove eixos sem perda. **Implicação prática: o modelo geométrico "mestre" deve viver numa única ferramenta e todas as reexportações devem ser scriptadas, nunca manuais** — só assim sobrevive a repetição de "e se puser a árvore aqui" dezenas de vezes.

---

## 11. O que NÃO vale a pena

- **ENVI-met.** A mais rigorosa do mercado, mas **3.000 €/ano** é custo de consultoria recorrente para execução única. SOLWEIG/UMEP cobre o essencial de graça.
- **Revit + Dynamo**, salvo se a casa já for modelada em Revit por outro motivo. Ferramenta de edifícios aplicada a problema de paisagem — mal talhada e cara.
- **CityGML e "smart city".** Sobredimensionado por definição.
- **SpeedTree Pro + biblioteca** ($999/ano) — orientado a jogos/VFX; não justifica subscrição recorrente para 3-4 árvores.
- **OpenFOAM directo** sem experiência prévia em CFD — curva medida em semanas, não horas.
- **Qualquer plataforma vendida como "digital twin" residencial** — visualizadores, não motores de simulação. Bons para "mostrar uma imagem", inúteis para "calcular se a sombra muda".
- **Fotogrametria/LiDAR como fonte de dados de muro.** Reconfirmado: o erro é incompatível com o rigor exigido. Telémetro laser continua a ser a ferramenta certa.

---

## 12. Três pilhas concretas

### (a) Mínima — Python + open source, quase zero custo

Blender (modelação + Sapling) → OBJ → trimesh/pyvista/shapely ligado ao modelo solar NOAA existente → SOLWEIG/UMEP (QGIS) para microclima → SWMM para água → DIALux evo para luz nocturna.

- **Custo:** 0 € de software (+ telémetro ~20-40 €, já necessário independentemente).
- **Tempo de montagem:** 2-4 semanas de curva cumulativa.
- **Exige:** Python intermédio (**o utilizador já tem modelo Python funcional — é o maior indicador de sucesso**); Blender básico; conceitos de QGIS.
- **Onde parte:** colagem manual e scriptada, sem suporte comercial. SOLWEIG em QGIS4 estava em versão de desenvolvimento — risco de instabilidade. Vegetação limitada ao que Sapling aproximar.

### (b) Equilibrada — melhor retorno por esforço

Rhino + Grasshopper (perpétua) → Ladybug + Honeybee (gratuitos, dentro do Rhino) → Lands Design (~$779, perpétua) → The Grove (Blender) para a copa da palmeira, importada via OBJ → DIALux evo → SOLWEIG/UMEP para microclima.

- **Custo:** ≈ **1.800-2.500 € de investimento único**, sem subscrições recorrentes.
- **Tempo de montagem:** 3-6 semanas.
- **Exige:** modelação NURBS básica (fácil), lógica de nós em Grasshopper (prática, não programação textual).
- **Onde parte:** licença perpétua **por versão** — actualizações maiores podem exigir nova compra. Ligação a SOLWEIG continua a exigir exportação manual (não há plugin directo Rhino→UMEP).

### (c) Ambiciosa — sem restrição de orçamento

Rhino + ClimateStudio + Vectorworks Landmark (~$1.530/ano) + ENVI-met (~3.000 €/ano) + SpeedTree Pro + biblioteca + AGi32 (~$990-1.490/ano) + SimScale pago.

- **Custo:** **6.000-8.000 €/ano recorrentes**, mais investimento inicial.
- **Onde parte:** o retorno marginal sobre (b) é real mas desproporcionado para execução doméstica única. Faz sentido para um atelier que factura a múltiplos clientes.

---

## 13. Veredicto

**A pilha equilibrada (b)** — Rhino + Grasshopper + Ladybug/Honeybee + Lands Design, com The Grove para a copa da palmeira e DIALux evo para a luz.

É a única combinação que liga geometria, solar e paisagismo **dentro do mesmo ambiente** sem exportação/reimportação manual a cada iteração — o requisito central da pergunta original. O custo é investimento único, não recorrente. A curva é a mais bem documentada do mercado. E resolve o ponto que esta pesquisa identificou como subestimado: **modelar a copa da palmeira como geometria real em vez de um cilindro muda genuinamente o resultado da análise de sombra.**

A pilha mínima (a) é a segunda escolha honesta, sobretudo porque **o utilizador já tem competência Python comprovada** — mas exige montar mais peças à mão e perde a integração nativa.

---

## 14. Buracos — o que não foi apurado

- **Preço exacto de Rhino 8/9 para 2026** — usado valor histórico (~$995) sem confirmação directa.
- **Preço de The Grove 3D** — site oficial não devolveu número.
- **Preço de Laubwerk e se continua actualizado em 2026** — risco de estagnação não confirmado nem afastado.
- **Preço de PCSWMM e de ClimateStudio** — ambos "sob consulta".
- **Estabilidade da versão UMEP/SOLWEIG para QGIS4** — descrita como "development release"; não confirmado se já há release estável.
- **Existe plugin directo Rhino → SWMM ou Rhino → UMEP/SOLWEIG?** Não encontrado; presume-se que não, mas não exaustivamente descartado.
- **Confirmação definitiva de que nenhum Android tem LiDAR equivalente em 2026** — não reaberto de raiz; nada nos resultados o contradisse.
