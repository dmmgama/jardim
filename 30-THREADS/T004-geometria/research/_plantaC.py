# -*- coding: utf-8 -*-
"""Variante C — jacuzzi em macico tecnico, escada em L, degraus embutidos."""
import io, os
BASE = os.path.dirname(os.path.abspath(__file__))

LX, LY = 13.00, 5.78
PLAT   = 1.50          # profundidade da plataforma
JAC    = 1.75          # lado do jacuzzi
COB    = 0.35
N_DEG  = 6
ESC_W  = 1.10
MACICO_X0 = PLAT                 # o macico comeca onde acaba a plataforma
MACICO_DX = JAC                  # profundidade do macico em X
TRANS = MACICO_DX                # 1,75
PALM_X, PALM_Y, PALM_R = 11.6, 3.0, 3.1
LOD_X, LOD_Y, LOD_R = 2.6, 0.4, 2.6
CIT_X, CIT_Y = 8.5, 3.2
DRENO_X, DRENO_Y = 11.7, 3.5

S, MT, ML = 60, 78, 92
W = int(LX*S + ML*2); H = int(LY*S + MT + 112)
def X(x): return ML + x*S
def Y(y): return MT + y*S

P=[]; a=P.append
a(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">')
a('''<defs>
<pattern id="hMac" width="8" height="8" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="8" stroke="#8a6d3b" stroke-width="2.4" opacity=".5"/></pattern>
<pattern id="hPla" width="10" height="10" patternUnits="userSpaceOnUse">
  <rect width="10" height="10" fill="#f0e9dc"/>
  <line x1="0" y1="0" x2="0" y2="10" stroke="#c9b79a" stroke-width="1.4"/></pattern>
<pattern id="hTec" width="7" height="7" patternUnits="userSpaceOnUse">
  <rect width="7" height="7" fill="#f7f1e6"/>
  <circle cx="3.5" cy="3.5" r="1.1" fill="#8a6d3b" opacity=".5"/></pattern>
<linearGradient id="agua" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#bfe4ef"/><stop offset="1" stop-color="#8fcede"/></linearGradient>
<marker id="mA" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
  <path d="M0,1 L8,4.5 L0,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
<marker id="mB" markerWidth="9" markerHeight="9" refX="1" refY="4.5" orient="auto">
  <path d="M9,1 L1,4.5 L9,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
</defs>''')

# jardim de fundo
a(f'<rect x="{X(0)}" y="{Y(0)}" width="{LX*S}" height="{LY*S}" fill="#eef2e6"/>')

# ── MACICO: bloco continuo jacuzzi + escada ──
jac_y0 = 0.35
jac_y1 = jac_y0 + JAC
esc_y0 = jac_y1 + 0.25
esc_y1 = esc_y0 + ESC_W

a(f'<rect x="{X(MACICO_X0)}" y="{Y(jac_y0-0.18)}" width="{MACICO_DX*S}" '
  f'height="{(esc_y1-jac_y0+0.36)*S}" fill="#f5efe2" stroke="#8a6d3b" stroke-width="2"/>')
a(f'<rect x="{X(MACICO_X0)}" y="{Y(jac_y0-0.18)}" width="{MACICO_DX*S}" '
  f'height="{(esc_y1-jac_y0+0.36)*S}" fill="url(#hMac)"/>')

# jacuzzi (agua) — topo ao nivel da plataforma
a(f'<rect x="{X(MACICO_X0)}" y="{Y(jac_y0)}" width="{JAC*S}" height="{JAC*S}" '
  f'fill="url(#agua)" stroke="#2f6b7d" stroke-width="2.2"/>')
a(f'<text x="{X(MACICO_X0+JAC/2)}" y="{Y(jac_y0+JAC/2)-6}" text-anchor="middle" '
  f'font-size="12.5" font-weight="700" fill="#1d4654">JACUZZI</text>')
a(f'<text x="{X(MACICO_X0+JAC/2)}" y="{Y(jac_y0+JAC/2)+11}" text-anchor="middle" '
  f'font-size="10" fill="#22505e">1,75 × 1,75</text>')
a(f'<text x="{X(MACICO_X0+JAC/2)}" y="{Y(jac_y0+JAC/2)+25}" text-anchor="middle" '
  f'font-size="10" font-weight="600" fill="#1d4654">topo +1,350</text>')

# escada embutida no macico
a(f'<rect x="{X(MACICO_X0)}" y="{Y(esc_y0)}" width="{MACICO_DX*S}" height="{ESC_W*S}" '
  f'fill="#e7eff2" stroke="#2f6b7d" stroke-width="1.8"/>')
for k in range(1, N_DEG):
    xd = MACICO_X0 + k*COB
    a(f'<line x1="{X(xd)}" y1="{Y(esc_y0)}" x2="{X(xd)}" y2="{Y(esc_y1)}" stroke="#2f6b7d" stroke-width="1.2"/>')
a(f'<text x="{X(MACICO_X0+MACICO_DX/2)}" y="{Y((esc_y0+esc_y1)/2)+4}" text-anchor="middle" '
  f'font-size="11" font-weight="700" fill="#22505e">6 degraus · 0,1417</text>')
a(f'<line x1="{X(MACICO_X0+0.16)}" y1="{Y(esc_y1-0.16)}" x2="{X(MACICO_X0+MACICO_DX-0.16)}" '
  f'y2="{Y(esc_y1-0.16)}" stroke="#22505e" stroke-width="1.4" marker-end="url(#mA)"/>')

# rotulo do macico / vazio tecnico
a(f'<text x="{X(MACICO_X0+MACICO_DX/2)}" y="{Y(jac_y0)-13}" text-anchor="middle" '
  f'font-size="11.5" font-weight="700" fill="#6b5424">MACIÇO TÉCNICO — 1,60 m³</text>')

# ── plataforma ──
a(f'<rect x="{X(0)}" y="{Y(0)}" width="{PLAT*S}" height="{LY*S}" fill="url(#hPla)" '
  f'stroke="#b09a78" stroke-width="1.8"/>')
cxp,cyp = X(PLAT/2), Y(LY/2)
a(f'<text x="{cxp}" y="{cyp}" text-anchor="middle" font-size="12.5" font-weight="700" '
  f'fill="#7a6544" transform="rotate(-90 {cxp} {cyp})">PLATAFORMA +1,350</text>')

# faixa livre (sem macico) — junto ao muro SE, para la da escada
a(f'<text x="{X(MACICO_X0+MACICO_DX/2)}" y="{Y(esc_y1+0.55)}" text-anchor="middle" '
  f'font-size="10.5" font-weight="600" fill="#3f6b32">{LY-esc_y1:.2f} m livre</text>')

# ── jardim ──
gx = PLAT+TRANS
a(f'<text x="{X(gx+(LX-gx)/2)}" y="{Y(5.42)}" text-anchor="middle" font-size="13.5" '
  f'font-weight="700" fill="#3f6b32">JARDIM  ·  +0,500  ·  56,4 m²</text>')

# arvores
a(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="{PALM_R*S}" fill="#4a7c3f" opacity=".16"/>')
a(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="{PALM_R*S}" fill="none" stroke="#3f6b32" stroke-width="1.5" stroke-dasharray="7 5"/>')
a(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="6" fill="#2f5426"/>')
a(f'<text x="{X(PALM_X)}" y="{Y(PALM_Y)-PALM_R*S+18}" text-anchor="middle" font-size="11" font-weight="700" fill="#2f5426">PALMEIRA</text>')
a(f'<text x="{X(PALM_X)}" y="{Y(PALM_Y)-PALM_R*S+31}" text-anchor="middle" font-size="8.5" fill="#8a2f18">⌀ ≈6,2 POR MEDIR 🔴</text>')
a(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="{LOD_R*S}" fill="#4a7c3f" opacity=".12"/>')
a(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="{LOD_R*S}" fill="none" stroke="#3f6b32" stroke-width="1.2" stroke-dasharray="5 4"/>')
a(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="4.5" fill="#2f5426"/>')
a(f'<text x="{X(LOD_X)+11}" y="{Y(LOD_Y)+4}" font-size="10" fill="#2f5426">lodão 🔴</text>')
a(f'<circle cx="{X(CIT_X)}" cy="{Y(CIT_Y)}" r="4.5" fill="none" stroke="#a84a3a" stroke-width="1.5"/>')
a(f'<line x1="{X(CIT_X)-5.5}" y1="{Y(CIT_Y)-5.5}" x2="{X(CIT_X)+5.5}" y2="{Y(CIT_Y)+5.5}" stroke="#a84a3a" stroke-width="1.5"/>')
a(f'<line x1="{X(CIT_X)-5.5}" y1="{Y(CIT_Y)+5.5}" x2="{X(CIT_X)+5.5}" y2="{Y(CIT_Y)-5.5}" stroke="#a84a3a" stroke-width="1.5"/>')
a(f'<text x="{X(CIT_X)}" y="{Y(CIT_Y)-11}" text-anchor="middle" font-size="9" fill="#a84a3a">laranjeira SAI</text>')
a(f'<rect x="{X(DRENO_X)-5}" y="{Y(DRENO_Y)-5}" width="10" height="10" fill="none" stroke="#2f6b7d" stroke-width="1.6"/>')

# muros
a(f'<rect x="{X(0)}" y="{Y(0)}" width="{LX*S}" height="{LY*S}" fill="none" stroke="#1a1a18" stroke-width="3.8"/>')
a(f'<text x="{X(LX/2)}" y="{Y(LY)+31}" text-anchor="middle" font-size="11" font-weight="600" fill="#8a2f18">MURO SE — 0,0 h Dez · patologia 🔴</text>')
a(f'<text x="{X(LX/2)}" y="{Y(0)-27}" text-anchor="middle" font-size="11" font-weight="600" fill="#3f6b32">MURO NW — 4,9 h Dez · a melhor luz</text>')

# cotas
def cH(x0,x1,ypx,txt,cor):
    a(f'<line x1="{X(x0)}" y1="{ypx}" x2="{X(x1)}" y2="{ypx}" stroke="{cor}" stroke-width="1.2" marker-start="url(#mB)" marker-end="url(#mA)"/>')
    a(f'<text x="{(X(x0)+X(x1))/2}" y="{ypx-7}" text-anchor="middle" font-size="11.5" font-weight="600" fill="{cor}">{txt}</text>')
def cV(y0,y1,xpx,txt,cor):
    a(f'<line x1="{xpx}" y1="{Y(y0)}" x2="{xpx}" y2="{Y(y1)}" stroke="{cor}" stroke-width="1.2" marker-start="url(#mB)" marker-end="url(#mA)"/>')
    a(f'<text x="{xpx-5}" y="{(Y(y0)+Y(y1))/2}" text-anchor="middle" font-size="11" font-weight="600" fill="{cor}" transform="rotate(-90 {xpx-5} {(Y(y0)+Y(y1))/2})">{txt}</text>')

cH(0,PLAT,MT-50,"1,50","#7a6544")
cH(PLAT,PLAT+TRANS,MT-50,"1,75","#8a2f18")
cH(PLAT+TRANS,LX,MT-50,f"{LX-PLAT-TRANS:.2f}","#3f6b32")
cH(0,LX,MT-72,"13,00","#1a1a18")
cV(jac_y0,jac_y1,ML-38,"1,75","#2f6b7d")
cV(esc_y0,esc_y1,ML-38,"1,10","#2f6b7d")
cV(esc_y1,LY,ML-38,f"{LY-esc_y1:.2f}","#3f6b32")
cV(0,LY,ML-64,"5,78","#1a1a18")
a('</svg>')
io.open(os.path.join(BASE,"_C.svg"),"w",encoding="utf-8").write("\n".join(P))

# ═════════ CORTE ═════════
CS, CML, CMT = 168, 118, 56
cw, ch = 1020, 430
C=[]; c=C.append
def cx(x): return CML + x*CS
def cy(z): return CMT + (1.58 - z)*CS
c(f'<svg viewBox="0 0 {cw} {ch}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">')
c('''<defs>
<pattern id="cMac" width="8" height="8" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="8" stroke="#8a6d3b" stroke-width="2.4" opacity=".45"/></pattern>
<linearGradient id="cAgua" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#bfe4ef"/><stop offset="1" stop-color="#7cc2d4"/></linearGradient>
<marker id="dA" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
  <path d="M0,1 L8,4.5 L0,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
<marker id="dB" markerWidth="9" markerHeight="9" refX="1" refY="4.5" orient="auto">
  <path d="M9,1 L1,4.5 L9,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
</defs>''')
# betonilha
c(f'<rect x="{cx(-0.45)}" y="{cy(0)}" width="{5.15*CS}" height="22" fill="#d8d2c4" stroke="#a8a08c" stroke-width="1.2"/>')
c(f'<text x="{cx(4.1)}" y="{cy(0)+16}" font-size="10" fill="#6b6455">betonilha existente 0,00</text>')
# plataforma
c(f'<rect x="{cx(-0.45)}" y="{cy(1.35)}" width="{(0.45+PLAT)*CS}" height="{1.35*CS}" fill="#f0e9dc" stroke="#b09a78" stroke-width="1.8"/>')
c(f'<text x="{cx(0.5)}" y="{cy(0.72)}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#7a6544">PLATAFORMA</text>')
c(f'<text x="{cx(0.5)}" y="{cy(0.72)+15}" text-anchor="middle" font-size="9.5" fill="#8a7550">vazio sob estrado</text>')
# macico com jacuzzi
c(f'<rect x="{cx(PLAT)}" y="{cy(1.35)}" width="{JAC*CS}" height="{0.85*CS}" fill="#f5efe2" stroke="#8a6d3b" stroke-width="2"/>')
c(f'<rect x="{cx(PLAT)}" y="{cy(1.35)}" width="{JAC*CS}" height="{0.85*CS}" fill="url(#cMac)"/>')
# agua do jacuzzi: topo +1,35, base +0,65
c(f'<rect x="{cx(PLAT+0.06)}" y="{cy(1.35)}" width="{(JAC-0.12)*CS}" height="{0.70*CS}" fill="url(#cAgua)" stroke="#2f6b7d" stroke-width="2"/>')
c(f'<text x="{cx(PLAT+JAC/2)}" y="{cy(1.02)}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1d4654">JACUZZI 0,70</text>')
c(f'<text x="{cx(PLAT+JAC/2)}" y="{cy(0.57)}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#6b5424">vazio técnico</text>')
# jardim
c(f'<rect x="{cx(PLAT+JAC)}" y="{cy(0.50)}" width="{(4.6-PLAT-JAC)*CS}" height="{0.50*CS}" fill="#dce8d2" stroke="#4a7c3f" stroke-width="1.8"/>')
c(f'<text x="{cx(3.8)}" y="{cy(0.25)+4}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3f6b32">JARDIM</text>')
# niveis
for zz,lbl,cor in [(1.35,"+1,350  sala · plataforma · água","#7a6544"),
                   (0.65,"+0,650  base do jacuzzi","#22505e"),
                   (0.50,"+0,500  jardim","#3f6b32"),
                   (0.0,"0,00  betonilha","#8a8579")]:
    c(f'<line x1="{cx(-0.5)}" y1="{cy(zz)}" x2="{cx(4.65)}" y2="{cy(zz)}" stroke="{cor}" stroke-width="0.9" stroke-dasharray="6 5" opacity=".7"/>')
    c(f'<text x="{cx(4.7)}" y="{cy(zz)+4}" font-size="10.5" font-weight="600" fill="{cor}">{lbl}</text>')
# cota do desnivel
xk = cx(PLAT+JAC+0.22)
c(f'<line x1="{xk}" y1="{cy(1.35)}" x2="{xk}" y2="{cy(0.50)}" stroke="#8a2f18" stroke-width="1.4" marker-start="url(#dB)" marker-end="url(#dA)"/>')
c(f'<text x="{xk+8}" y="{(cy(1.35)+cy(0.50))/2}" font-size="12.5" font-weight="700" fill="#8a2f18">0,85</text>')
# cota horizontal
yk = cy(-0.26)
c(f'<line x1="{cx(PLAT)}" y1="{yk}" x2="{cx(PLAT+JAC)}" y2="{yk}" stroke="#8a2f18" stroke-width="1.3" marker-start="url(#dB)" marker-end="url(#dA)"/>')
c(f'<text x="{(cx(PLAT)+cx(PLAT+JAC))/2}" y="{yk-8}" text-anchor="middle" font-size="12" font-weight="700" fill="#8a2f18">1,75</text>')
c(f'<line x1="{cx(-0.45)}" y1="{yk}" x2="{cx(PLAT)}" y2="{yk}" stroke="#7a6544" stroke-width="1.3" marker-start="url(#dB)" marker-end="url(#dA)"/>')
c(f'<text x="{(cx(-0.45)+cx(PLAT))/2}" y="{yk-8}" text-anchor="middle" font-size="11.5" font-weight="600" fill="#7a6544">1,50</text>')
c(f'<text x="{cx(PLAT)}" y="{cy(1.48)}" font-size="10.5" font-weight="600" fill="#6b5424">corte pelo jacuzzi — a água fica rente à plataforma</text>')
c('</svg>')
io.open(os.path.join(BASE,"_Ccorte.svg"),"w",encoding="utf-8").write("\n".join(C))
print("ok — livre junto ao SE:", round(LY-esc_y1,2), "m")
