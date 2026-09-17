# T005 — ESTADO PARA O ARQUITECTO

**Estado:** `ACTIVA` · `ONGOING` · fase 1 entregue, fase 2 por instruir
**Data:** 2026-09-18 · **Sessões:** 1 · **Assunto:** como se caracteriza este espaço, por disciplina

---

## 1. O que esta thread é agora

Define **a regra de caracterização**: que parâmetros, por disciplina, com que método, tolerância
e critério de suficiência. Não mede nem decide projecto — diz o que tem de ser sabido, e quando
se pode parar.

## 2. Achados, e o que valem

**Três pesquisas independentes convergiram, sem combinação, na mesma reclassificação: o jardim
sobre laje é tecnicamente uma cobertura ajardinada.** Nenhuma foi instruída a concluí-lo. Activa
normativo próprio (FLL), um modo de falha específico (substrato fino seca em **dias**) e uma
ferramenta gratuita de simulação (SWMM Green Roof). **Nenhum documento do projecto o tratava assim.**

**A pesquisa autónoma do David responde à pergunta das camadas** — espessuras FLL, substratos
leves com densidade **saturada** (é a que dimensiona), sobrecarga no muro SW. Esteve disponível
toda a fase 1 **sem ninguém a abrir**.

**A copa da palmeira bloqueia por três razões independentes:** arboricultura (não se avalia o
risco de soterrar o colo sem medir), modelação (cilindro ≠ copa real muda o resultado da sombra),
sanidade (detecção acústica do escaravelho, >90% em ensaios).

## 3. Conhecimento certo

- A reclassificação como cobertura ajardinada — convergência tripla independente.
- **Física TLS vs. fotogrametria:** o reboco liso é o **pior caso para fotogrametria e um dos
  melhores para TLS** (o laser não precisa de textura). **Não contradiz `REJEICOES.md` §11**, que
  rejeitou captura por *telemóvel* — o que separa os casos é física da superfície.
- Cadeia de tratamento de nuvem de pontos **gratuita e em Windows 10** (CloudCompare → malha → motor solar).

## 4. Lacunas

- **Espessuras concretas das camadas: certeza NULA.** Ninguém as propôs; exigem percolação, carga
  admissível e escolha de substrato.
- **Preços:** muito «não apurado» — aluguer de scanner em PT, sensor acústico, estação meteorológica.
- **Nomes de 20 sessões** perdidos: só o David os recupera.
- A T005 **não aplicou a grelha** — a fase 2 não arrancou.

## 5. Impacto cruzado  *(opinião do dono da thread, não facto)*

**T004 — o mais urgente.** Os **+0,50 m estão fixados como cota mas não decompostos em camadas**
(drenante/filtrante/substrato). **Isso é geometria, não acabamento:** define cota final, peso e
comportamento hidráulico. Se a T004 desenhar os 50 cm como bloco homogéneo de terra, **desenha
uma coisa que não vai ser construída assim.** Sinalizado; sem resposta.

**T003.** A pesquisa de software sobrepõe-se ao mandato solar dela. **Não arbitrei** — é do
Arquitecto. Registo o facto técnico: o modelo Python da T002 resolve posição solar mas **não**
sombreamento por geometria 3D complexa, que é o que a copa exige.

**T001.** O `DOSSIER-LOCAL.md` está organizado por objecto físico. **Não tem secção de cobertura
ajardinada — e não podia ter:** quando foi escrito, o jardim era de chão. Não é falha do dossier;
é o limite do método de levantamento por observação.

**ESTADO.md §10.** Todas as recomendações destas pesquisas entram numa conta que não existe — **o
filtro de custo nunca foi aplicado a V2.**

## 6. O que peço ao Arquitecto

1. ⚠ **Encaminhar as camadas à T004.** Único item com relógio a contar.
2. **Ver a síntese** (`research/05-SINTESE-FASE-1.md`) — é a peça, se só ler uma.
3. **Instruir ou adiar a fase 2.** Não arranco sem isso.
4. **Arbitrar T003 × T005.**

**Risco que assumo e assinalo:** cinco pesquisas densas são o material com que se produz uma
enciclopédia. **A fase 2 tem de cortar, não acumular.**
