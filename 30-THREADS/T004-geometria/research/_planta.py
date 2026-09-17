# -*- coding: utf-8 -*-
"""Gera a planta cotada e o corte da transicao, em SVG a escala, para o HTML."""
import io, os

BASE = os.path.dirname(os.path.abspath(__file__))

# ─────────── geometria real (m) ───────────
LX, LY = 13.00, 5.78          # recinto interior
PLAT   = 1.50                 # profundidade da plataforma em X
TRANS  = 1.75                 # profundidade da transicao em X
ESC_W  = 1.10                 # largura da escada (encostada ao muro SE)
N_DEG  = 6
COB    = 0.35
BANCO_W = 2.00                # largura dos bancos
PALM_X, PALM_Y, PALM_R = 11.6, 3.0, 3.1
LOD_X, LOD_Y, LOD_R = 2.6, 0.4, 2.0
CIT_X, CIT_Y = 8.5, 3.2
DRENO_X, DRENO_Y = 11.7, 3.5

# ─────────── escala ───────────
S   = 62                      # px por metro
MT, ML = 78, 96               # margens topo/esq
W = int(LX*S + ML*2)
H = int(LY*S + MT + 120)

def X(x): return ML + x*S
def Y(y): return MT + y*S

P = []
def add(t): P.append(t)

add(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
    f'font-family="ui-sans-serif,system-ui,sans-serif" class="planta">')

# defs — hachuras
add('''<defs>
<pattern id="hBanco" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="7" stroke="#8a6d3b" stroke-width="2.2" opacity=".55"/></pattern>
<pattern id="hEscada" width="6" height="6" patternTransform="rotate(-45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="6" stroke="#2f6b7d" stroke-width="2" opacity=".5"/></pattern>
<pattern id="hTalude" width="9" height="9" patternUnits="userSpaceOnUse">
  <circle cx="4.5" cy="4.5" r="1.5" fill="#4a7c3f" opacity=".45"/></pattern>
<pattern id="hPlat" width="10" height="10" patternUnits="userSpaceOnUse">
  <rect width="10" height="10" fill="#f0e9dc"/>
  <line x1="0" y1="0" x2="0" y2="10" stroke="#c9b79a" stroke-width="1.4"/></pattern>
<marker id="mA" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
  <path d="M0,1 L8,4.5 L0,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
<marker id="mB" markerWidth="9" markerHeight="9" refX="1" refY="4.5" orient="auto">
  <path d="M9,1 L1,4.5 L9,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
</defs>''')

# ── jardim (fundo) ──
add(f'<rect x="{X(0)}" y="{Y(0)}" width="{LX*S}" height="{LY*S}" fill="#eef2e6"/>')

# ── zona livre (sem degrau) — talude ──
tx0, tx1 = PLAT, PLAT+TRANS
ty0, ty1 = 0, LY-ESC_W
add(f'<rect x="{X(tx0)}" y="{Y(ty0)}" width="{TRANS*S}" height="{(ty1-ty0)*S}" fill="#dce8d2"/>')
add(f'<rect x="{X(tx0)}" y="{Y(ty0)}" width="{TRANS*S}" height="{(ty1-ty0)*S}" fill="url(#hTalude)"/>')

# ── bancos (2 niveis) — encostados ao lado NW, largura BANCO_W ──
by0 = LY-ESC_W-BANCO_W
for i,(x0,x1) in enumerate([(PLAT, PLAT+TRANS/2),(PLAT+TRANS/2, PLAT+TRANS)]):
    add(f'<rect x="{X(x0)}" y="{Y(by0)}" width="{(x1-x0)*S}" height="{BANCO_W*S}" '
        f'fill="#f5efe2" stroke="#8a6d3b" stroke-width="1.6"/>')
    add(f'<rect x="{X(x0)}" y="{Y(by0)}" width="{(x1-x0)*S}" height="{BANCO_W*S}" fill="url(#hBanco)"/>')
add(f'<text x="{X(PLAT+TRANS/2)}" y="{Y(by0+BANCO_W/2)}" text-anchor="middle" '
    f'font-size="13" font-weight="700" fill="#6b5424">BANCOS</text>')
add(f'<text x="{X(PLAT+TRANS/4)}" y="{Y(by0+BANCO_W/2)+17}" text-anchor="middle" '
    f'font-size="10.5" fill="#8a6d3b">+0,925</text>')
add(f'<text x="{X(PLAT+3*TRANS/4)}" y="{Y(by0+BANCO_W/2)+17}" text-anchor="middle" '
    f'font-size="10.5" fill="#8a6d3b">+0,500</text>')

# ── escada: 6 degraus, encostada ao muro SE ──
ey = LY-ESC_W
add(f'<rect x="{X(PLAT)}" y="{Y(ey)}" width="{TRANS*S}" height="{ESC_W*S}" '
    f'fill="#e7eff2" stroke="#2f6b7d" stroke-width="1.6"/>')
for k in range(1, N_DEG):
    xd = PLAT + k*COB
    add(f'<line x1="{X(xd)}" y1="{Y(ey)}" x2="{X(xd)}" y2="{Y(LY)}" stroke="#2f6b7d" stroke-width="1.1"/>')
add(f'<text x="{X(PLAT+TRANS/2)}" y="{Y(ey+ESC_W/2)+4}" text-anchor="middle" '
    f'font-size="12" font-weight="700" fill="#22505e">ESCADA · 6 × 0,1417</text>')
# seta de descida
add(f'<line x1="{X(PLAT+0.2)}" y1="{Y(LY-0.22)}" x2="{X(PLAT+TRANS-0.2)}" y2="{Y(LY-0.22)}" '
    f'stroke="#22505e" stroke-width="1.4" marker-end="url(#mA)"/>')
add(f'<text x="{X(PLAT+TRANS+0.1)}" y="{Y(LY-0.18)}" font-size="10" fill="#22505e">desce</text>')

# ── plataforma ──
add(f'<rect x="{X(0)}" y="{Y(0)}" width="{PLAT*S}" height="{LY*S}" fill="url(#hPlat)" '
    f'stroke="#b09a78" stroke-width="1.6"/>')
add(f'<text x="{X(PLAT/2)}" y="{Y(LY/2)-8}" text-anchor="middle" font-size="13" '
    f'font-weight="700" fill="#7a6544" transform="rotate(-90 {X(PLAT/2)} {Y(LY/2)-8})">PLATAFORMA</text>')
add(f'<text x="{X(PLAT/2)+16}" y="{Y(LY/2)+42}" text-anchor="middle" font-size="11" '
    f'fill="#8a7550" transform="rotate(-90 {X(PLAT/2)+16} {Y(LY/2)+42})">+1,350 · nível da sala</text>')

# ── jardim: etiqueta ──
gx = PLAT+TRANS
add(f'<text x="{X(gx+(LX-gx)/2)}" y="{Y(0.62)}" text-anchor="middle" font-size="14" '
    f'font-weight="700" fill="#3f6b32">JARDIM  ·  +0,500</text>')
add(f'<text x="{X(gx+(LX-gx)/2)}" y="{Y(1.06)}" text-anchor="middle" font-size="11" '
    f'fill="#5b7d4f">{(LX-gx)*LY:.1f} m² — {(LX-gx)*LY/(LX*LY)*100:.0f}% do recinto</text>')

# ── arvores ──
add(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="{PALM_R*S}" fill="#4a7c3f" opacity=".17"/>')
add(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="{PALM_R*S}" fill="none" stroke="#3f6b32" '
    f'stroke-width="1.6" stroke-dasharray="7 5"/>')
add(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="7" fill="#2f5426"/>')
add(f'<text x="{X(PALM_X)}" y="{Y(PALM_Y)-PALM_R*S+20}" text-anchor="middle" font-size="12" '
    f'font-weight="700" fill="#2f5426">PALMEIRA</text>')
add(f'<text x="{X(PALM_X)}" y="{Y(PALM_Y)-PALM_R*S+35}" text-anchor="middle" font-size="9.5" '
    f'fill="#8a2f18">copa ⌀ ≈6,2 m — POR MEDIR 🔴</text>')

add(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="{LOD_R*S}" fill="#4a7c3f" opacity=".13"/>')
add(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="{LOD_R*S}" fill="none" stroke="#3f6b32" '
    f'stroke-width="1.2" stroke-dasharray="5 4"/>')
add(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="5" fill="#2f5426"/>')
add(f'<text x="{X(LOD_X)+12}" y="{Y(LOD_Y)+4}" font-size="10.5" fill="#2f5426">lodão</text>')

add(f'<circle cx="{X(CIT_X)}" cy="{Y(CIT_Y)}" r="5" fill="none" stroke="#a84a3a" stroke-width="1.6"/>')
add(f'<line x1="{X(CIT_X)-6}" y1="{Y(CIT_Y)-6}" x2="{X(CIT_X)+6}" y2="{Y(CIT_Y)+6}" stroke="#a84a3a" stroke-width="1.6"/>')
add(f'<line x1="{X(CIT_X)-6}" y1="{Y(CIT_Y)+6}" x2="{X(CIT_X)+6}" y2="{Y(CIT_Y)-6}" stroke="#a84a3a" stroke-width="1.6"/>')
add(f'<text x="{X(CIT_X)}" y="{Y(CIT_Y)-12}" text-anchor="middle" font-size="10" fill="#a84a3a">laranjeira SAI</text>')

# ── dreno ──
add(f'<rect x="{X(DRENO_X)-6}" y="{Y(DRENO_Y)-6}" width="12" height="12" fill="none" '
    f'stroke="#2f6b7d" stroke-width="1.8"/>')
add(f'<text x="{X(DRENO_X)}" y="{Y(DRENO_Y)+24}" text-anchor="middle" font-size="9.5" fill="#2f6b7d">dreno 🔴</text>')

# ── muros ──
add(f'<rect x="{X(0)}" y="{Y(0)}" width="{LX*S}" height="{LY*S}" fill="none" stroke="#1a1a18" stroke-width="4"/>')

# rotulos de muro
add(f'<text x="{X(LX/2)}" y="{Y(LY)+34}" text-anchor="middle" font-size="11.5" font-weight="600" '
    f'fill="#8a2f18">MURO SE — zona 2 · 0,0 h de sol em Dezembro · patologia 🔴</text>')
add(f'<text x="{X(LX/2)}" y="{Y(0)-30}" text-anchor="middle" font-size="11.5" font-weight="600" '
    f'fill="#3f6b32">MURO NW — zona 6 · 4,9 h em Dezembro · a melhor luz</text>')
add(f'<text x="{X(0)-30}" y="{Y(LY/2)}" text-anchor="middle" font-size="11" fill="#57544c" '
    f'transform="rotate(-90 {X(0)-30} {Y(LY/2)})">FACHADA NE</text>')
add(f'<text x="{X(LX)+30}" y="{Y(LY/2)}" text-anchor="middle" font-size="11" fill="#57544c" '
    f'transform="rotate(90 {X(LX)+30} {Y(LY/2)})">MURO SW (suporte)</text>')

# ─────────── cotas ───────────
def cotaH(x0, x1, ypx, txt, cor="#57544c", peso="600"):
    add(f'<line x1="{X(x0)}" y1="{ypx}" x2="{X(x1)}" y2="{ypx}" stroke="{cor}" stroke-width="1.2" '
        f'marker-start="url(#mB)" marker-end="url(#mA)"/>')
    add(f'<line x1="{X(x0)}" y1="{ypx-5}" x2="{X(x0)}" y2="{ypx+5}" stroke="{cor}" stroke-width="1.2"/>')
    add(f'<line x1="{X(x1)}" y1="{ypx-5}" x2="{X(x1)}" y2="{ypx+5}" stroke="{cor}" stroke-width="1.2"/>')
    add(f'<text x="{(X(x0)+X(x1))/2}" y="{ypx-7}" text-anchor="middle" font-size="11.5" '
        f'font-weight="{peso}" fill="{cor}">{txt}</text>')

def cotaV(y0, y1, xpx, txt, cor="#57544c"):
    add(f'<line x1="{xpx}" y1="{Y(y0)}" x2="{xpx}" y2="{Y(y1)}" stroke="{cor}" stroke-width="1.2" '
        f'marker-start="url(#mB)" marker-end="url(#mA)"/>')
    add(f'<line x1="{xpx-5}" y1="{Y(y0)}" x2="{xpx+5}" y2="{Y(y0)}" stroke="{cor}" stroke-width="1.2"/>')
    add(f'<line x1="{xpx-5}" y1="{Y(y1)}" x2="{xpx+5}" y2="{Y(y1)}" stroke="{cor}" stroke-width="1.2"/>')
    add(f'<text x="{xpx-6}" y="{(Y(y0)+Y(y1))/2}" text-anchor="middle" font-size="11.5" '
        f'font-weight="600" fill="{cor}" transform="rotate(-90 {xpx-6} {(Y(y0)+Y(y1))/2})">{txt}</text>')

cotaH(0, PLAT, MT-52, "1,50", "#7a6544")
cotaH(PLAT, PLAT+TRANS, MT-52, "1,75", "#8a2f18", "700")
cotaH(PLAT+TRANS, LX, MT-52, f"{LX-PLAT-TRANS:.2f}", "#3f6b32")
cotaH(0, LX, MT-76, "13,00", "#1a1a18", "700")

cotaV(0, LY-ESC_W-BANCO_W, ML-42, f"{LY-ESC_W-BANCO_W:.2f} livre", "#3f6b32")
cotaV(LY-ESC_W-BANCO_W, LY-ESC_W, ML-42, "2,00", "#8a6d3b")
cotaV(LY-ESC_W, LY, ML-42, "1,10", "#2f6b7d")
cotaV(0, LY, ML-70, "5,78", "#1a1a18")

add('</svg>')
svg_planta = "\n".join(P)

# ═══════════════ CORTE ═══════════════
CS = 155          # px/m no corte (vertical exagerado? nao — igual nos dois eixos)
CML, CMT = 120, 60
cw, ch = 980, 420
C = []
def c(t): C.append(t)
def cx(x): return CML + x*CS
def cy(z): return CMT + (1.55 - z)*CS   # z em metros, 1.55 no topo

c(f'<svg viewBox="0 0 {cw} {ch}" xmlns="http://www.w3.org/2000/svg" '
  f'font-family="ui-sans-serif,system-ui,sans-serif" class="corte">')
c('''<defs>
<marker id="cA" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
  <path d="M0,1 L8,4.5 L0,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
<marker id="cB" markerWidth="9" markerHeight="9" refX="1" refY="4.5" orient="auto">
  <path d="M9,1 L1,4.5 L9,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
</defs>''')

# betonilha existente (cota 0)
c(f'<rect x="{cx(-0.5)}" y="{cy(0)}" width="{5.6*CS}" height="26" fill="#d8d2c4" stroke="#a8a08c" stroke-width="1.2"/>')
c(f'<text x="{cx(4.5)}" y="{cy(0)+18}" font-size="10.5" fill="#6b6455">betonilha existente — cota 0,00</text>')

# plataforma
c(f'<rect x="{cx(-0.5)}" y="{cy(1.35)}" width="{(0.5+PLAT)*CS}" height="{1.35*CS}" '
  f'fill="#f0e9dc" stroke="#b09a78" stroke-width="1.8"/>')
c(f'<text x="{cx(0.5)}" y="{cy(0.75)}" text-anchor="middle" font-size="12" font-weight="700" fill="#7a6544">PLATAFORMA</text>')
c(f'<text x="{cx(0.5)}" y="{cy(0.75)+16}" text-anchor="middle" font-size="10" fill="#8a7550">vazio sob estrado</text>')
c(f'<text x="{cx(0.5)}" y="{cy(0.75)+30}" text-anchor="middle" font-size="9.5" fill="#3f6b32">↑ ventila a caixa de ar</text>')

# degraus (6 x 0.1417, cobertor 0.35)
z = 1.35
for k in range(N_DEG):
    x0 = PLAT + k*COB
    z_next = z - 0.85/N_DEG
    c(f'<rect x="{cx(x0)}" y="{cy(z)}" width="{COB*CS}" height="{(z-0.0)*CS}" '
      f'fill="#e7eff2" stroke="#2f6b7d" stroke-width="1.4"/>')
    z = z_next

# jardim
c(f'<rect x="{cx(PLAT+TRANS)}" y="{cy(0.50)}" width="{(5.1-PLAT-TRANS)*CS}" height="{0.50*CS}" '
  f'fill="#dce8d2" stroke="#4a7c3f" stroke-width="1.8"/>')
c(f'<text x="{cx(3.9)}" y="{cy(0.25)+4}" text-anchor="middle" font-size="12" font-weight="700" fill="#3f6b32">JARDIM</text>')
c(f'<text x="{cx(3.9)}" y="{cy(0.25)+19}" text-anchor="middle" font-size="9.5" fill="#5b7d4f">substrato + drenante</text>')

# linhas de cota horizontais (niveis)
for zz, lbl, cor in [(1.35,"+1,350  sala / plataforma","#7a6544"),
                     (0.925,"+0,925  patamar · banco 1","#8a6d3b"),
                     (0.50,"+0,500  jardim","#3f6b32"),
                     (0.0,"0,00  betonilha","#8a8579")]:
    c(f'<line x1="{cx(-0.55)}" y1="{cy(zz)}" x2="{cx(5.15)}" y2="{cy(zz)}" stroke="{cor}" '
      f'stroke-width="0.9" stroke-dasharray="6 5" opacity=".75"/>')
    c(f'<text x="{cx(5.2)}" y="{cy(zz)+4}" font-size="10.5" font-weight="600" fill="{cor}">{lbl}</text>')

# cota vertical do desnivel
xk = cx(PLAT+TRANS+0.28)
c(f'<line x1="{xk}" y1="{cy(1.35)}" x2="{xk}" y2="{cy(0.50)}" stroke="#8a2f18" stroke-width="1.4" '
  f'marker-start="url(#cB)" marker-end="url(#cA)"/>')
c(f'<text x="{xk+9}" y="{(cy(1.35)+cy(0.50))/2}" font-size="12.5" font-weight="700" fill="#8a2f18">0,85</text>')

# cota horizontal da transicao
yk = cy(-0.28)
c(f'<line x1="{cx(PLAT)}" y1="{yk}" x2="{cx(PLAT+TRANS)}" y2="{yk}" stroke="#8a2f18" stroke-width="1.3" '
  f'marker-start="url(#cB)" marker-end="url(#cA)"/>')
c(f'<text x="{(cx(PLAT)+cx(PLAT+TRANS))/2}" y="{yk-8}" text-anchor="middle" font-size="12" '
  f'font-weight="700" fill="#8a2f18">1,75</text>')
c(f'<line x1="{cx(-0.5)}" y1="{yk}" x2="{cx(PLAT)}" y2="{yk}" stroke="#7a6544" stroke-width="1.3" '
  f'marker-start="url(#cB)" marker-end="url(#cA)"/>')
c(f'<text x="{(cx(-0.5)+cx(PLAT))/2}" y="{yk-8}" text-anchor="middle" font-size="11.5" '
  f'font-weight="600" fill="#7a6544">1,50</text>')

# detalhe degrau
c(f'<text x="{cx(PLAT)}" y="{cy(1.46)}" font-size="10.5" font-weight="600" fill="#22505e">'
  f'6 degraus · espelho 0,1417 · cobertor 0,35 · 2R+C = 0,633</text>')

c('</svg>')
svg_corte = "\n".join(C)

io.open(os.path.join(BASE, "_svg_planta.svg"), "w", encoding="utf-8").write(svg_planta)
io.open(os.path.join(BASE, "_svg_corte.svg"), "w", encoding="utf-8").write(svg_corte)
print("SVG gerados")
print("jardim util:", round((LX-PLAT-TRANS)*LY,1), "m2 =", round((LX-PLAT-TRANS)/LX*100), "%")
print("largura livre:", round(LY-ESC_W-BANCO_W,2), "m")
