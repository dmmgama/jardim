---
created: 2026-09-15
project: Jardim
thread: T003
tipo: pacote-de-arranque
---

# Pacote de arranque — T003 Modelo solar

Preparado pela sessão de 2026-09-15 (T001), com autorização expressa do David
para derrogar G9/T1/T3. Entrada deixada em `INBOX.md` da raiz para o Arquitecto
ratificar.

Este documento existe para que a **sessão T003 decida sem repetir investigação**.

---

## 1. O que se quer, exactamente

Um modelo onde se possa:

1. **Mover uma árvore e ver a sombra mudar.** É o requisito central.
2. Calcular horas de sol directo por zona, por data.
3. Testar a sensibilidade à altura dos obstáculos verticais, que têm conflito de fontes registado.
4. Corrigir números depois de medir, sem refazer nada.

**Não** se quer: medir o DLI que existe hoje. Isso é outro problema, já investigado.

---

## 2. Porque é que o levantamento anterior não responde directamente

O levantamento de ferramentas existente noutra thread (pede a localização ao David) optimizou para
uma pergunta diferente — *"quanto DLI tem este quintal?"* — e recomendou
`pvlib`+PVGIS como via mínima.

> **`pvlib`+PVGIS não serve para mover árvores.** Converte a geometria num
> **perfil de horizonte** — um ângulo por azimute. Não tem objectos. Uma árvore
> não é um obstáculo de horizonte: é um volume no meio do recinto, que projecta
> sombra para um lado e não para o outro conforme a hora.

Tudo o mais nesse relatório é válido e aplica-se. **Lê-o.** Em especial as
secções 2.2 (VI-Suite), 2.7 (UMEP/SEBE), 2.8 (Python) e 7 (validação com EXIF).

---

## 3. As três vias que servem

### Via A — Python próprio (`pvlib` + `shapely`)

A geometria em causa é trivial: um recinto rectangular fechado, mais um punhado
de copas aproximadas por sólidos simples. Projectar sombras destes num plano é
geometria analítica elementar, e `pvlib` dá a posição solar com rigor de
referência.

| | |
|---|---|
| **Mover árvore** | Editar duas coordenadas no YAML. Trivial. |
| **Horas de sol directo** | Rigoroso |
| **Difusa obstruída** | Requer trabalho: factor de vista do céu por hemisfério |
| **Refletida dos muros** | Não, sem esforço considerável |
| **Feedback visual** | O que se programar (matplotlib) |
| **Montagem** | 4–10 h |
| **Risco** | Baixo. Sem dependências frágeis. |

**Quando escolher:** se o objectivo é sobretudo geometria de sombras e iteração
rápida de posições. Dá a resposta de "onde bate o sol e quantas horas" com
rigor total, e é a via onde o modelo paramétrico se implementa mais
naturalmente — o YAML já está desenhado para isto.

### Via B — VI-Suite no Blender

Add-on que transforma o Blender em pré/pós-processador para **Radiance** — o
padrão-ouro de simulação de luz natural, do Lawrence Berkeley National Lab.

| | |
|---|---|
| **Mover árvore** | Arrastar no viewport. **Vê-se a sombra imediatamente.** |
| **Horas de sol directo** | Sim |
| **Difusa obstruída** | Sim, correctamente (Radiance) |
| **Refletida dos muros** | Sim, com albedo por material |
| **Feedback visual** | **Imediato e é o seu ponto forte** |
| **Montagem** | 8–15 h (metade a instalar Radiance no Windows) |
| **Risco** | Add-on de um só autor (Ryan Southall, Univ. Brighton). 47 estrelas no GitHub. Se encalhares num erro obscuro, pode não haver quem responda. |

**Está vivo:** repositório `vi-suite07` para Blender 5.1 (experimental), 597
commits. Compatibilidade confirmada com Blender 4.4 (Março 2025).

**Quando escolher:** se se quiser **um só modelo** que sirva para análise solar
**e** para o desenho do jardim **e** para a iluminação cénica nocturna. O
Radiance é a ferramenta da indústria de iluminação — o mesmo modelo responde às
três perguntas.

### Via C — UMEP/SEBE no QGIS

SEBE = *Solar Energy on Building Envelopes*. Calcula irradiância píxel a píxel
incluindo **directa + difusa + refletida**, com vegetação como voxels de
transmissividade configurável.

| | |
|---|---|
| **Mover árvore** | Editar raster de copa. Menos directo. |
| **Difusa + refletida** | Sim, as três componentes |
| **Vegetação** | Voxels, transmissividade 3% por omissão |
| **Resolução** | Fina com folga — um recinto desta ordem fica ordens de magnitude abaixo do limite de 4M píxeis |
| **Output** | Raster kWh/píxel + irradiância nas paredes em texto |
| **Feedback visual** | Não. É um pipeline: editar, correr, abrir raster. |
| **Montagem** | 10–18 h (5–8 h se já se usou QGIS) |
| **Risco** | Baixo. Consórcio académico (Gotemburgo, Reading), 99 estrelas, reimplementação em Rust em curso. |

**A dificuldade real** não é conceptual: é *plumbing* de SIG. Cinco camadas
raster com extensão e resolução idênticas, CRS projectado (para Portugal
ETRS89/PT-TM06, **EPSG:3763**), meteorologia em formato UMEP.

**O DSM fabrica-se:** desenhar os limites como polígonos num shapefile com
atributo de altura, e o *DSM Generator* rasteriza. As medições de fita passam
directamente para o modelo.

**Quando escolher:** se se quiser mapas de irradiância por píxel com as três
componentes, e não incomodar a ausência de feedback visual.

---

## 4. Recomendação desta sessão

**Via A primeiro, Via B depois se se justificar.**

Razões:

1. **O requisito central é iterar posições de árvores**, e a Via A faz isso com
   duas coordenadas num ficheiro. Nenhuma outra é mais rápida a iterar.
2. **A geometria é trivial** — um recinto e algumas copas. Não justifica
   Radiance para responder "quantas horas de sol tem este ponto".
3. **O `parametros-activos.yaml` já está desenhado para a Via A.** Lê-se com
   `PyYAML` em três linhas.
4. **Risco baixo.** `pvlib` é maduro e mantido; VI-Suite é de um só autor.
5. **A Via B ganha valor quando houver iluminação cénica** a decidir — aí o
   duplo uso justifica as 15 h. Hoje ainda não há.

**A ressalva honesta:** a Via A não dá a difusa obstruída nem a refletida dos
muros sem trabalho considerável. Se a pergunta passar de *"quantas horas de
sol"* para *"quanto DLI exactamente"*, a Via A deixa de bastar. Mas para
**escolher onde pôr uma árvore**, horas de sol directo é a métrica que decide.

---

## 5. Primeiro passo concreto, qualquer que seja a via

**Validar contra as três fotografias EXIF antes de confiar em qualquer número.**

Pede ao David onde estão, e quantas existem. Os parâmetros solares de cada
instante calculam-se a partir da data e hora do EXIF.

**O que faz o teste ser forte:** se houver duas fotografias em que o mesmo lado
do recinto aparece uma vez iluminado e outra em sombra — tipicamente uma de
manhã e outra de tarde — então um modelo que reproduza essa **inversão** está
geometricamente correcto. Pergunta ao David se as fotografias disponíveis têm
essa propriedade; é o que torna a validação conclusiva, e é grátis.

---

## 6. Cuidados que custam horas se forem ignorados

- **Hora legal vs hora solar.** Lisboa usa hora de verão (UTC+1). As horas de
  primeira luz que o David indicar são **locais**. Confirmar o que a biblioteca
  espera — erro de uma hora dá sombras completamente erradas.
- **`pvlib` quer timezone-aware datetimes.** Um datetime *naive* é interpretado
  como UTC e o erro passa despercebido.
- **Exemplares de folha caduca exigem duas simulações** — uma por época de folha,
  outra para o período despido. Um parâmetro único de transmissividade dá o
  Inverno errado, e o Inverno é a estação crítica. Pergunta quais são caducos.
- **Há exemplares cujas dimensões nunca foram medidas.** Correr em intervalo de
  incerteza, não em valor único. Pergunta quais.
- **A altura dos obstáculos verticais é o parâmetro mais sensível do modelo**, e
  tem conflito de fontes registado. Sempre em cenários, até haver medição.
- **Caminho com espaços.** O caminho deste repositório contém espaços. Algumas
  ferramentas de linha de comandos falham silenciosamente por isso; se houver
  fotogrametria, trabalhar numa pasta sem espaços no caminho.

---

## 7. O que esta thread NÃO decide

- **Que espécies plantar.** O catálogo vegetal está a ser produzido em T001.
- **Onde plantar, por razões de projecto.** O modelo diz o que acontece à
  sombra; a decisão do jardim é do Arquitecto.
- **Se vale a pena comprar um medidor de DLI.** Matéria do Arquitecto. O
  relatório de software argumenta que sim (Apogee DLI-500, ≈460 €), mesmo com
  simulação, porque resolve a incerteza espectral que nenhum software resolve.

---

## 8. Ficheiros a ler, por ordem

1. `thread.md` desta pasta — o mandato
2. `modelo/contrato-de-dados.yaml` — o que o modelo precisa, e porquê
3. `research/01-PLANO-DE-SESSAO.md` — a sequência de trabalho
4. O levantamento de ferramentas completo e a base factual do local — **pede
   ambos ao David**; não os vás procurar.
