---
created: 2026-09-15
project: Jardim
thread: T003
estado: ACTIVA
updated: 2026-09-17
sessoes: 0
---

# T003 — Modelo solar paramétrico

## MANDATO  *(fixo — não alterar)*

Construir e manter um **modelo digital paramétrico** do quintal que permita:

1. Reproduzir a geometria do local a partir de variáveis, não de valores fixos no código.
2. Calcular exposição solar por zona e por data — horas de sol directo e irradiância.
3. **Mover árvores e testar posições**, vendo o efeito no sombreamento.
4. Testar sensibilidade a parâmetros incertos (altura dos muros, dimensões das copas).
5. Absorver medições reais quando existirem, sem refazer o modelo.

**Âmbito:**
- Geometria do recinto: muros, fachada, varanda, escada, cotas.
- Vegetação existente como objectos paramétricos móveis: palmeira, lodão, citrinheira.
- Vegetação hipotética: árvores novas em posições a testar.
- Cálculo solar: posição do Sol, sombras projectadas, horas de sol, irradiância.
- Escolha e montagem da ferramenta (ver `research/` de T001 para o levantamento).

**Fora de âmbito:**
- **Que espécies plantar** — é matéria do catálogo vegetal (T001/research) e da decisão do Arquitecto.
- **Onde plantar, por razões estéticas ou de projecto** — o modelo diz o que acontece à sombra; não decide o jardim.
- Drenagem, estrutura, orçamento, arte, iluminação cénica. O modelo pode servir-lhes depois; não são mandato.
- Medição no terreno — T003 consome medições, não as produz. As medições são de T001.

**Entrega esperada:** modelo funcional em `modelo/`, com manual de uso, mais tabelas de exposição solar por cenário testado em `entregue/`.

**Tipo:** `ONGOING` — entrega por partes. O modelo melhora com cada medição que chega.

---

## ALARGAMENTO DE ÂMBITO — captura 3D com telemóvel  *(2026-09-17)*

> Instrução do David, ratificada pelo Arquitecto. **Acrescenta ao mandato, não o substitui.**

Passa a caber a esta thread **avaliar e recomendar uma ferramenta de captura 3D operável com
telemóvel** — nuvem de pontos ou equivalente — que produza a geometria de que o modelo precisa.

**Porquê aqui e não noutra thread:** não é uma decisão de ferramenta, é uma decisão de **requisito**.
Quem sabe de que geometria o modelo precisa, e com que tolerância, é esta thread. Escolher uma app
sem saber que erro é aceitável é escolher às cegas.

### O que a captura tem de resolver

| # | Alvo | Porque importa | Estado hoje |
|---|---|---|---|
| **1** | **Copa da palmeira** — diâmetro da projecção no solo e altura da base das palmas | **Bloqueia a T004**, no caminho crítico da obra. Item 🔴 P2.2 do dossier, nunca medido. | Desconhecido |
| **2** | **Altura dos muros, troço a troço** | O parâmetro mais sensível do projecto. 3,00 → 2,50 m **duplicou** a média de sol de Dezembro. Suspeita nova: podem não ter todos a mesma altura. | 2,50 m `[observado]`, sem detalhe |
| **3** | **Lodão e citrinheira** — porte e copa | Entram no modelo como obstáculos móveis. | Não medidos |
| **4** | **Cota até onde o muro SW retém terras** | Fronteira suporte/guarda. Define quanto se pode rebaixar sem tocar em estrutura. | Desconhecido |

### As dificuldades, declaradas à cabeça

- **Os muros são o pior caso possível para fotogrametria:** reboco liso, sem textura, em sombra
  permanente sob uma fachada de 15,50 m. A via Google 3D já foi rejeitada por não os resolver
  (`REJEICOES.md` §11) — e a razão aplica-se a qualquer reconstrução baseada em imagem.
- **Vegetação é o ponto fraco histórico** de qualquer reconstrução: folhagem fina, movimento com o
  vento, oclusão.
- **Escala.** Uma nuvem de pontos sem referência de dimensão conhecida dá geometria **relativa**,
  não cotas. O procedimento tem de resolver isto explicitamente.

### O que se espera

1. **Uma recomendação, não um levantamento.** Já existe levantamento de software em
   `../T001-local/research/Jardim_Software_Modelacao_Solar.md`. **Não repetir.**
2. **Um procedimento de campo que o David execute sozinho numa tarde** — quantas fotos, de onde,
   que referência de escala, que ordem, que erros evitar.
3. **Dizer onde a fita métrica ganha.** Se a altura dos muros se resolve melhor com um telémetro
   laser de 30 €, **é isso que se recomenda.** O objectivo é ter o número certo, não usar
   tecnologia.
4. **Perguntar ao David que telemóvel tem** antes de recomendar. Não assumir hardware — LiDAR não é
   universal.

**Entrega:** recomendação + procedimento de campo em `entregue/`, autónomo e executável sem o
agente presente.

---

## ESTADO FACE AO MANDATO  *(reescrito a cada sessão)*

**Última sessão:** — (thread criada 2026-09-15, arrancada pelo Arquitecto em 2026-09-17, ainda sem sessão própria)
**Estado:** Pacote de arranque pronto. **Zero dados.** Por decidir a ferramenta, levantar os dados com o David, e montar.

> ### ⚠ LÊ `mensagens.md` ANTES DE TUDO
>
> Há uma mensagem de arranque do Arquitecto de 2026-09-17 com **um pedido de quantificação
> encaminhado** e o contexto do que mudou no projecto desde que foste criada. O projecto mudou de
> natureza: a T002 fechou, abriu a T004 em urgência de obra, e o pavimento vai subir ≈0,50 m.
>
> **Ordem de trabalho recomendada pelo Arquitecto:**
> 1. **Primeiro o que não precisa de dados novos** — os pedidos 1–4 correm com a geometria que o
>    dossier já dá. Não esperar pela palmeira para entregar isso.
> 2. **Depois a captura 3D** — recomendação + procedimento de campo.
> 3. **Por fim o pedido 5** (palmeira), quando a copa estiver medida.
>
> **Um aviso que consta da mensagem:** os números de sol que a T002 usou para fechar o debate são
> estimativa dela, não desta thread. **Se o modelo não os reproduzir, dizê-lo alto** — há decisões
> tomadas em cima deles, e o valor desta thread é poder contrariá-los.

> **REGRA QUE GOVERNA ESTA THREAD — decisão do David, 2026-09-15:**
> A T003 **não copia dados de outras threads e não escreve caminhos de ficheiros.**
> Declara o que precisa; o David indica a origem de cada dado.
> Motivo: evitar duplicação que diverge e números sem dono. Um valor copiado
> fica errado no momento em que a fonte é corrigida, e ninguém repara.

O que já existe nesta pasta:

| Ficheiro | O que é |
|---|---|
| `LEIA-ME-DAVID.md` | Explicação para o David. Não é para o agente executar. |
| `modelo/contrato-de-dados.yaml` | **A peça central.** Declara tudo o que o modelo precisa, `para_que` e `sensibilidade` de cada campo. **Sem valores.** É a especificação, e não se altera. |
| `modelo/parametros-activos.yaml` | **Vazio por desenho.** É onde os valores entram em sessão, cada um com `origem:` declarada pelo David. Sem `origem`, o parâmetro não existe. |
| `research/00-PACOTE-ARRANQUE.md` | As três vias de ferramenta comparadas, com recomendação e ressalvas. |
| `research/01-PLANO-DE-SESSAO.md` | **A sequência de trabalho.** Fases 0 a 4, as perguntas obrigatórias, o que não fazer, e o critério de sucesso. |
| `mockups/layouts-jardim.html` | 11 layouts exploratórios. Material do David, **não é mandato desta thread.** |

**Existe um levantamento de ferramentas já feito** noutra thread — pede ao David a localização antes de decidir a via. As conclusões que importam a esta thread estão resumidas em `research/00-PACOTE-ARRANQUE.md`, mas o documento completo tem o detalhe:

- **`pvlib`+PVGIS não serve** para mover árvores — converte a geometria num perfil de horizonte fixo por azimute, sem objectos.
- **VI-Suite (Blender)** — Radiance com interface gráfica, feedback visual imediato, o mesmo modelo serve depois para iluminação. 8–15 h de montagem. Add-on de um só autor, comunidade pequena.
- **UMEP/SEBE (QGIS)** — directa+difusa+refletida, vegetação como voxels com transmissividade, output em raster. 10–18 h. Pipeline de SIG, sem feedback visual.
- **Python próprio (`pvlib`+`shapely`)** — geometria simples (um recinto e algumas copas), controlo total, árvores como objectos móveis triviais. Dá horas de sol directo com rigor; irradiância difusa obstruída exige trabalho.

**Nenhuma ferramenta produz DLI (mol/m²/dia) directamente** — todas dão W/m² ou kWh/m². A conversão é manual, com incerteza de ±10–15%.

---

## HANDOFF  *(para a próxima sessão desta thread)*

**Próximo passo:** seguir `research/01-PLANO-DE-SESSAO.md`, da Fase 0. Verificar ambiente, decidir a ferramenta, e **depois** levantar os dados com o David em entrevista estruturada pelo contrato.

**À espera de:** **os dados, que só o David pode indicar.** A thread arranca sozinha na parte de ambiente e ferramenta; a partir daí precisa dele.

**Cuidado com:**

- **Não tens dados, e não vais procurá-los.** `modelo/contrato-de-dados.yaml` diz o que precisas. Cada valor entra em `parametros-activos.yaml` com `origem:` declarada pelo David. **Sem origem, o parâmetro não existe** — o modelo assinala-o como ausente e diz que conclusões deixam de ser possíveis.
- **Nenhum caminho de ficheiro no código.** Caminho é argumento, configuração, ou pergunta ao David. Nunca literal.
- **Nenhum valor por omissão.** Se um parâmetro falta, levanta erro e nomeia o campo. É isto que impede o hardcoding de voltar pela porta do fundo.
- **A altura dos obstáculos verticais é o input mais sensível de todo o modelo**, e há **conflito de fontes registado** mais material gráfico produzido com valores divergentes. Pergunta qual é o valor vigente e se já foi medido. Enquanto for estimativa, **corre em cenários, nunca em valor único.**
- **Folha caduca exige duas simulações.** As ferramentas tratam transmissividade como parâmetro único. Pergunta quais exemplares são caducos e qual o período de folha.
- **Há exemplares de vegetação nunca medidos.** Pergunta quais. Esses correm-se em intervalo de incerteza.
- **Valida contra as fotografias datadas antes de reportar um único número.** Pergunta quantas existem e se cobrem geometrias de sombra diferentes — duas com sombras opostas validam a geometria de graça.
- **Fuso horário e hora de verão.** `pvlib` exige datetimes com timezone; um *naive* é lido como UTC e o erro passa despercebido até as sombras não baterem com as fotos.
- **`PyYAML` não estava instalado** neste ambiente (verificado 2026-09-15). Confirma e instala.
- O caminho deste repositório tem espaços. Algumas ferramentas de linha de comandos falham silenciosamente; se houver fotogrametria, trabalhar em pasta sem espaços.
