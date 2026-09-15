---
created: 2026-09-15
project: Jardim
thread: T001
tipo: nota de arqueologia
canon: false
---

# Arqueologia — `Docs-David-Local/arqueologia/`

Material **obsoleto, duplicado ou superado**, retirado da raiz da pasta e guardado aqui.

**Regras aplicadas ao movimento:**

- Nada foi apagado. Nada saiu de `Docs-David-Local/`.
- Só se moveu o que é **comprovadamente** duplicado exacto (MD5 idêntico), quase-duplicado verificado imagem a imagem, ou versão superada por outra que existe na raiz.
- **Nenhum ficheiro referenciado pelo documento canónico `Planta_e_Espaco_Fisico.md` foi movido.** Verificado por `grep` antes do movimento.
- Na dúvida, não se moveu — ver §3.

---

## 1. Ficheiros movidos

| Ficheiro | O que é | Porque foi para aqui | O que o substitui |
|---|---|---|---|
| `Planta_e_Espaco_Fisico_1.html` | Exportação HTML auto-contida do documento canónico, com 33 imagens embebidas em base64. | **Duplicado bit-a-bit.** MD5 `537c44d37841488f815f414e4bb1f45b`, idêntico ao de `Planta_e_Espaco_Fisico.html`; 5 637 463 bytes ambos. Acresce que **ambos os HTML estão desactualizados**: preservam 3 ocorrências de «estagnada», isto é, mantêm a patologia «água estagnada em lençol, sem escoamento aparente» que o canónico retirou como **erro de facto** em 2026-09-15. | `Planta_e_Espaco_Fisico.md` (canónico, rev. 16:30). O HTML da raiz **também deve ser regerado** a partir do `.md` actual — enquanto não for, é uma versão distribuível que afirma um facto falso. |
| `Planta_e_Espaco_Fisico.BACKUP-20260915.md` | Versão do documento canónico **anterior** à revisão de 2026-09-15 16:30. 17 KB, 10 secções. | **Superado.** Não tem a secção «Drenagem», não tem «Geometria solar — valores astronómicos», não tem as três subsecções de prioridade, e **contém «água estagnada» como patologia** — o erro corrigido. Não é fonte válida. Estava na raiz com nome quase igual ao do canónico, a um carácter de distância. | `Planta_e_Espaco_Fisico.md` (30 KB, 11 secções). O backup mantém valor **como registo do que mudou**: o documento quase duplicou de tamanho numa só revisão. |
| `Claude outputs/NOMENCLATURA-EIXOS.png` → guardado aqui como `NOMENCLATURA-EIXOS (Claude outputs).png` | Cópia do diagrama normativo de nomenclatura, eixos e cantos. | **Duplicado bit-a-bit.** MD5 `ebd73b278ee31a3b8a0c62cbb53db8ce`, idêntico ao de `NOMENCLATURA-EIXOS.png` da raiz. Renomeado ao mover para não colidir com o da raiz e para registar a proveniência. | `NOMENCLATURA-EIXOS.png` na raiz — é o ficheiro que o canónico referencia. **`Claude outputs/Jardim_Nomenclatura.svg` ficou onde estava**: é a fonte vectorial editável, não é duplicado, e tem valor próprio. |
| `foto 6Fev.jpg` | Vista geral de Inverno do quintal, 4624×3472. | **Quase-duplicado.** Mesmo enquadramento, mesmos objectos e o mesmo EXIF (2026-02-06 15:10:32, Pixel 7a, com GPS) de `JARDIM-GERAL-inverno.jpg`. MD5 difere apenas por recompressão: 4 193 511 bytes contra 4 199 282. | `JARDIM-GERAL-inverno.jpg` — ligeiramente maior (menos perda) e é o nome que o canónico usa. |
| `google-sol-casa.jpg` | Captura do Google Maps 3D, vista afastada do bairro, 1504×972. | **Quase-duplicado verificado imagem a imagem.** Mesmo enquadramento, mesmas setas amarela e vermelha, mesmo relógio de sistema «06:25», mesma barra de tarefas — idêntico a `ENVOLVENTE-3D-2.jpg` pixel a pixel. Sem informação nova. | `ENVOLVENTE-3D-2.jpg` — nome descritivo e ligeiramente maior (617 923 contra 612 152 bytes). |
| `google-sol-casa2.jpg` | Captura do Google Maps 3D, vista aproximada, 793×527. | **Recorte degradado.** Mesma vista e mesmas anotações vermelha e amarela de `ENVOLVENTE-3D-1.png`, a ~56% da resolução e em JPEG com perda. Sem informação nova. | `ENVOLVENTE-3D-1.png` — PNG sem perda, 1423×949, mostra mais contexto. É a prova visual de que não há obstrução a SW, pressuposto central do cálculo solar. |

**Total: 6 ficheiros.**

---

## 2. Verificação feita antes de mover

| Verificação | Resultado |
|---|---|
| MD5 dos pares de duplicados exactos | `Planta_e_Espaco_Fisico.html` ≡ `_1.html` ✔ · `NOMENCLATURA-EIXOS.png` ≡ cópia em `Claude outputs/` ✔ |
| Inspecção visual dos quase-duplicados | `google-sol-casa.jpg` vs `ENVOLVENTE-3D-2.jpg` — abertos lado a lado, idênticos ✔ |
| Referências no documento canónico | `grep` sobre `Planta_e_Espaco_Fisico.md`: **nenhum** dos 6 ficheiros é referenciado ✔ |
| Referências no `DOSSIER-LOCAL.md` | Aparecem só na tabela de exclusões e na nova subsecção «Arqueologia», que aponta para aqui ✔ |
| Caminho relativo `![](NOMENCLATURA-EIXOS.png)` do canónico | Resolve para a raiz da pasta, onde o ficheiro **permanece** — ligação intacta ✔ |

---

## 3. Candidatos que NÃO foram movidos, e porquê

O inventário lista mais ficheiros como elimináveis ou dispensáveis. Estes ficaram onde estavam:

| Ficheiro | Porque ficou |
|---|---|
| `Planta_e_Espaco_Fisico.html` | É o original do par, não a cópia. Está desactualizado (preserva o erro «água estagnada») e **deve ser regerado**, mas regerar não é mover — e enquanto o `.md` não for reexportado, é o único HTML que resta. Decisão que não cabe neste movimento. |
| `ENVOLVENTE-SW-20260205.jpg` | O inventário chama-lhe «dispensável» — é um recorte muito agressivo de `Foto-Aerea.jpg` e perde a escada, o murete, os arrumos e metade do muro NW. **Mas é referenciado pelo documento canónico** (secção 1 e secção 9). Movê-lo partia a ligação. Fica. |
| `ESTADO-PAVIMENTO-20260209.jpg` | Recorte de `Foto1c-Winter.jpg`, mesmo instante. Referenciado **e embebido** no canónico, e tem papel próprio: o detalhe da lâmina de água. Não é redundante. |
| `Claude outputs/Jardim_Nomenclatura.svg` | Fonte vectorial editável do diagrama normativo. Não é duplicado de nada e tem valor prático próprio. |
| `01-inverno.png` · `02-verão.png` | Têm erro conhecido — foram geradas com «Muros 3 m» e o sombreamento é inválido. **Mas a geometria solar que mostram é válida** e o canónico embebe-as com o aviso ao lado. Corrigir não é arquivar; os SVG na raiz permitem corrigir a legenda sem regerar. |
| `corte predio.jpg` | O desenho de base é uma proposta de reabilitação, não um levantamento — mas foi **anotado e corrigido pelo proprietário** em 2026-09-15 e é hoje a fonte das cotas verticais. Activo, não arqueologia. |

---

## 4. Estado da pasta após o movimento

```
Docs-David-Local/
├── DOSSIER-LOCAL.md                     ← dossier técnico
├── Planta_e_Espaco_Fisico.md            ← CANÓNICO
├── Planta_e_Espaco_Fisico.html          ← desactualizado, a regerar
├── [49 imagens activas]
├── Claude outputs/
│   └── Jardim_Nomenclatura.svg          ← fonte vectorial, mantida
└── arqueologia/                         ← esta pasta
    ├── NOTA.md
    ├── Planta_e_Espaco_Fisico_1.html
    ├── Planta_e_Espaco_Fisico.BACKUP-20260915.md
    ├── NOMENCLATURA-EIXOS (Claude outputs).png
    ├── foto 6Fev.jpg
    ├── google-sol-casa.jpg
    └── google-sol-casa2.jpg
```

**Nada aqui é fonte válida para o projecto.** Consultável, nunca activo.

---

## Adenda — 2026-09-15, fecho da sessão

### `Planta_e_Espaco_Fisico.html`

**O que é.** Versão HTML do documento canónico, exportada a 2026-09-15 06:59.

**Porque foi arquivada.** Preserva três ocorrências de «água estagnada em lençol, sem escoamento
aparente» — erro de facto **retractado** na revisão de 2026-09-15. O quintal escoa; a afirmação era
conclusão tirada de uma única fotografia. Enquanto este ficheiro existisse na raiz, havia uma versão
bem apresentada e circulável a afirmar algo falso.

**O que a substitui.** `DOSSIER-LOCAL.html`, gerado a partir de `DOSSIER-LOCAL.md`, com as imagens
embebidas e o semáforo de fiabilidade por secção.

**Nota.** O par `.md` (`Planta_e_Espaco_Fisico.md`) **permanece na raiz** e está corrigido. Só o HTML
ficou desactualizado, porque não foi regerado depois da revisão.


---

## Adenda 2 — 2026-09-15, consolidação num só canónico

### `Planta_e_Espaco_Fisico.md`

**O que era.** Documento de referência dimensional, revisto ao longo da sessão de 2026-09-15. Foi a
**fonte primária** de que o `DOSSIER-LOCAL.md` foi extraído.

**Porque foi arquivado.** Não estava desactualizado — estava **duplicado**. Os dois documentos
afirmavam os mesmos factos, mantidos em sincronia à mão a cada correcção. Isso não é garantia, é
disciplina; e é exactamente a condição que o mandato da T001 existe para corrigir:

> *em V1 a informação sobre o espaço estava espalhada por três documentos, um Notion e um dossier
> técnico avulso, com divergências entre si (cotas diferentes em fontes diferentes)*

Manter dois canónicos activos recriava o V1. **G1: a verdade vive num sítio só.**

**Verificação feita antes de arquivar.** Comparados os dois documentos:

| Teste | Resultado |
|---|---|
| Valores-chave (2,50 m · 65° · 155° · horas recalculadas · 27,9°/74,7° · 12,81 m) | **Coincidem todos.** Zero divergências |
| 14 blocos de raciocínio do canónico | **Todos presentes** no dossier, alguns com outra formulação |
| Valores numéricos exclusivos do canónico | 6, **nenhum relevante** — ver abaixo |

**Os 6 valores que só existiam aqui, e porque não se perde nada:**

| Valor | Porque não migra |
|---|---|
| `0,65 m` | Limite do critério de Blondel. Norma geral de escadas, não facto deste local |
| `27°` | Arredondamento de `27,9°`, que o dossier tem com precisão |
| `3,8 h` | **Obsoleto.** A média do equinócio é 4,3 h; sobrevivente de um cálculo anterior |
| `5,77 m` | O mesmo que `5,78 m`, na versão da planta da fracção. Diferença de 1 cm |
| `76 %` · `78 %` | Pertencem à contradição **C4**, anulada por comparar grandezas diferentes |

**O que o substitui.** `DOSSIER-LOCAL.md` — mais completo (827 contra 512 linhas), com semáforo de
fiabilidade, índice de 49 imagens, secções por instruir e registo de contradições.

**Consultar quando.** Para ver a redacção original de um facto antes de ser comprimido em tabela, ou
para reconstituir a cadeia de proveniência do dossier.


---

## Adenda 3 — 2026-09-15, limpeza

`Planta_e_Espaco_Fisico_1.html` **eliminado**. Era bit-a-bit idêntico (MD5 `537c44d3…`) a
`Planta_e_Espaco_Fisico.html`, que fica. Duas cópias do mesmo ficheiro de 5,4 MB não preservam mais
informação do que uma.
