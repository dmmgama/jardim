# -*- coding: utf-8 -*-
"""Duas variantes de transicao, lado a lado, a mesma escala."""
import io, os
BASE = os.path.dirname(os.path.abspath(__file__))

LX, LY = 13.00, 5.78
PLAT   = 1.50
TRANS  = 1.75
ESC_W  = 1.10
N_DEG  = 6
COB    = 0.35
JAC    = 1.75
PALM_X, PALM_Y, PALM_R = 11.6, 3.0, 3.1
LOD_X, LOD_Y = 2.6, 0.4
CIT_X, CIT_Y = 8.5, 3.2
DRENO_X, DRENO_Y = 11.7, 3.5

S = 58
MT, ML = 74, 88
W = int(LX*S + ML*2)
H = int(LY*S + MT + 108)

DEFS = '''<defs>
<pattern id="hB%s" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="7" stroke="#8a6d3b" stroke-width="2.2" opacity=".55"/></pattern>
<pattern id="hE%s" width="6" height="6" patternTransform="rotate(-45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="6" stroke="#2f6b7d" stroke-width="2" opacity=".5"/></pattern>
<pattern id="hT%s" width="9" height="9" patternUnits="userSpaceOnUse">
  <circle cx="4.5" cy="4.5" r="1.5" fill="#4a7c3f" opacity=".45"/></pattern>
<pattern id="hP%s" width="10" height="10" patternUnits="userSpaceOnUse">
  <rect width="10" height="10" fill="#f0e9dc"/>
  <line x1="0" y1="0" x2="0" y2="10" stroke="#c9b79a" stroke-width="1.4"/></pattern>
<marker id="mA%s" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
  <path d="M0,1 L8,4.5 L0,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
<marker id="mB%s" markerWidth="9" markerHeight="9" refX="1" refY="4.5" orient="auto">
  <path d="M9,1 L1,4.5 L9,8" fill="none" stroke="#57544c" stroke-width="1.3"/></marker>
</defs>'''


def planta(var):
    """var 'A' = escada no muro SE, jacuzzi pousado.
       var 'B' = escada ao centro, jacuzzi encastrado (modelo 3D do David)."""
    P = []
    a = P.append
    u = var
    def X(x): return ML + x*S
    def Y(y): return MT + y*S

    a(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
      f'font-family="ui-sans-serif,system-ui,sans-serif">')
    a(DEFS % (u,u,u,u,u,u))
    a(f'<rect x="{X(0)}" y="{Y(0)}" width="{LX*S}" height="{LY*S}" fill="#eef2e6"/>')

    if var == "A":
        # escada encostada ao muro SE; bancos a norte dela; faixa livre no topo
        esc_y0, esc_y1 = LY-ESC_W, LY
        banco_y0, banco_y1 = LY-ESC_W-2.00, LY-ESC_W
        livre_y0, livre_y1 = 0, banco_y0
        jac_x, jac_y = PLAT+TRANS+0.30, 0.45      # pousado no jardim, canto N
    else:
        # escada ao centro; faixa de degraus a toda a largura; jacuzzi encastrado
        esc_y0, esc_y1 = 1.95, 1.95+ESC_W
        banco_y0, banco_y1 = None, None
        livre_y0, livre_y1 = None, None
        jac_x, jac_y = PLAT+TRANS+0.15, 3.35      # encastrado, junto aos degraus

    # ── faixa de transicao ──
    if var == "A":
        a(f'<rect x="{X(PLAT)}" y="{Y(livre_y0)}" width="{TRANS*S}" height="{(livre_y1-livre_y0)*S}" fill="#dce8d2"/>')
        a(f'<rect x="{X(PLAT)}" y="{Y(livre_y0)}" width="{TRANS*S}" height="{(livre_y1-livre_y0)*S}" fill="url(#hT{u})"/>')
        a(f'<text x="{X(PLAT+TRANS/2)}" y="{Y((livre_y0+livre_y1)/2)}" text-anchor="middle" '
          f'font-size="11" font-weight="700" fill="#3f6b32">TALUDE</text>')
        a(f'<text x="{X(PLAT+TRANS/2)}" y="{Y((livre_y0+livre_y1)/2)+14}" text-anchor="middle" '
          f'font-size="9.5" fill="#5b7d4f">2,68 m sem degrau</text>')
        # bancos
        for (x0,x1) in [(PLAT, PLAT+TRANS/2),(PLAT+TRANS/2, PLAT+TRANS)]:
            a(f'<rect x="{X(x0)}" y="{Y(banco_y0)}" width="{(x1-x0)*S}" height="{(banco_y1-banco_y0)*S}" '
              f'fill="#f5efe2" stroke="#8a6d3b" stroke-width="1.5"/>')
            a(f'<rect x="{X(x0)}" y="{Y(banco_y0)}" width="{(x1-x0)*S}" height="{(banco_y1-banco_y0)*S}" fill="url(#hB{u})"/>')
        a(f'<text x="{X(PLAT+TRANS/2)}" y="{Y((banco_y0+banco_y1)/2)+4}" text-anchor="middle" '
          f'font-size="12" font-weight="700" fill="#6b5424">BANCOS</text>')
    else:
        # degraus a toda a largura, faixa continua
        a(f'<rect x="{X(PLAT)}" y="{Y(0)}" width="{TRANS*S}" height="{LY*S}" '
          f'fill="#f5efe2" stroke="#8a6d3b" stroke-width="1.5"/>')
        a(f'<rect x="{X(PLAT)}" y="{Y(0)}" width="{TRANS*S}" height="{LY*S}" fill="url(#hB{u})"/>')
        for k in range(1, N_DEG):
            xd = PLAT + k*COB
            a(f'<line x1="{X(xd)}" y1="{Y(0)}" x2="{X(xd)}" y2="{Y(LY)}" stroke="#8a6d3b" stroke-width="1"/>')
        a(f'<text x="{X(PLAT+TRANS/2)}" y="{Y(0.55)}" text-anchor="middle" '
          f'font-size="12" font-weight="700" fill="#6b5424">DEGRAUS-PLANO</text>')
        a(f'<text x="{X(PLAT+TRANS/2)}" y="{Y(0.92)}" text-anchor="middle" '
          f'font-size="9.5" fill="#8a6d3b">a toda a largura · 5,78 m</text>')

    # ── escada (o lanço por onde se desce) ──
    a(f'<rect x="{X(PLAT)}" y="{Y(esc_y0)}" width="{TRANS*S}" height="{ESC_W*S}" '
      f'fill="#e7eff2" stroke="#2f6b7d" stroke-width="1.7"/>')
    for k in range(1, N_DEG):
        xd = PLAT + k*COB
        a(f'<line x1="{X(xd)}" y1="{Y(esc_y0)}" x2="{X(xd)}" y2="{Y(esc_y1)}" stroke="#2f6b7d" stroke-width="1.1"/>')
    a(f'<text x="{X(PLAT+TRANS/2)}" y="{Y((esc_y0+esc_y1)/2)+4}" text-anchor="middle" '
      f'font-size="11" font-weight="700" fill="#22505e">ESCADA</text>')
    a(f'<line x1="{X(PLAT+0.18)}" y1="{Y(esc_y1-0.18)}" x2="{X(PLAT+TRANS-0.18)}" y2="{Y(esc_y1-0.18)}" '
      f'stroke="#22505e" stroke-width="1.3" marker-end="url(#mA{u})"/>')

    # ── plataforma ──
    a(f'<rect x="{X(0)}" y="{Y(0)}" width="{PLAT*S}" height="{LY*S}" fill="url(#hP{u})" '
      f'stroke="#b09a78" stroke-width="1.7"/>')
    cxp, cyp = X(PLAT/2), Y(LY/2)
    a(f'<text x="{cxp}" y="{cyp}" text-anchor="middle" font-size="12" font-weight="700" '
      f'fill="#7a6544" transform="rotate(-90 {cxp} {cyp})">PLATAFORMA +1,350</text>')

    # ── jacuzzi ──
    if var == "A":
        a(f'<rect x="{X(jac_x)}" y="{Y(jac_y)}" width="{JAC*S}" height="{JAC*S}" '
          f'fill="#cfe8f0" stroke="#2f6b7d" stroke-width="2"/>')
        a(f'<text x="{X(jac_x+JAC/2)}" y="{Y(jac_y+JAC/2)}" text-anchor="middle" font-size="11" '
          f'font-weight="700" fill="#22505e">JACUZZI</text>')
        a(f'<text x="{X(jac_x+JAC/2)}" y="{Y(jac_y+JAC/2)+15}" text-anchor="middle" font-size="9.5" '
          f'fill="#2f6b7d">pousado · topo +1,20</text>')
    else:
        a(f'<rect x="{X(jac_x)}" y="{Y(jac_y)}" width="{JAC*S}" height="{JAC*S}" '
          f'fill="#cfe8f0" stroke="#2f6b7d" stroke-width="2" stroke-dasharray="6 4"/>')
        a(f'<text x="{X(jac_x+JAC/2)}" y="{Y(jac_y+JAC/2)}" text-anchor="middle" font-size="11" '
          f'font-weight="700" fill="#22505e">JACUZZI</text>')
        a(f'<text x="{X(jac_x+JAC/2)}" y="{Y(jac_y+JAC/2)+15}" text-anchor="middle" font-size="9.5" '
          f'fill="#2f6b7d">encastrado · rente</text>')
        # acesso tecnico por resolver
        a(f'<rect x="{X(jac_x+JAC)}" y="{Y(jac_y)}" width="{0.90*S}" height="{JAC*S}" '
          f'fill="#fbeeea" stroke="#8a2f18" stroke-width="1.4" stroke-dasharray="4 3"/>')
        a(f'<text x="{X(jac_x+JAC+0.45)}" y="{Y(jac_y+JAC/2)}" text-anchor="middle" font-size="9" '
          f'font-weight="700" fill="#8a2f18" transform="rotate(-90 {X(jac_x+JAC+0.45)} {Y(jac_y+JAC/2)})">0,90 acesso?</text>')

    # ── jardim ──
    gx = PLAT+TRANS
    ytxt = 5.35 if var=="A" else 0.55
    if var == "A":
        a(f'<text x="{X(gx+(LX-gx)/2)}" y="{Y(5.35)}" text-anchor="middle" font-size="13" '
          f'font-weight="700" fill="#3f6b32">JARDIM +0,500 — 56,4 m²</text>')
    else:
        a(f'<text x="{X(gx+(LX-gx)/2)}" y="{Y(5.35)}" text-anchor="middle" font-size="13" '
          f'font-weight="700" fill="#3f6b32">JARDIM +0,500 — 56,4 m²</text>')

    # ── arvores ──
    a(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="{PALM_R*S}" fill="#4a7c3f" opacity=".16"/>')
    a(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="{PALM_R*S}" fill="none" stroke="#3f6b32" '
      f'stroke-width="1.5" stroke-dasharray="7 5"/>')
    a(f'<circle cx="{X(PALM_X)}" cy="{Y(PALM_Y)}" r="6" fill="#2f5426"/>')
    a(f'<text x="{X(PALM_X)}" y="{Y(PALM_Y)-PALM_R*S+18}" text-anchor="middle" font-size="11" '
      f'font-weight="700" fill="#2f5426">PALMEIRA</text>')
    a(f'<text x="{X(PALM_X)}" y="{Y(PALM_Y)-PALM_R*S+31}" text-anchor="middle" font-size="8.5" '
      f'fill="#8a2f18">⌀ ≈6,2 POR MEDIR</text>')

    LOD_R2 = 2.6
    a(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="{LOD_R2*S}" fill="#4a7c3f" opacity=".12"/>')
    a(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="{LOD_R2*S}" fill="none" stroke="#3f6b32" '
      f'stroke-width="1.2" stroke-dasharray="5 4"/>')
    a(f'<circle cx="{X(LOD_X)}" cy="{Y(LOD_Y)}" r="4.5" fill="#2f5426"/>')
    a(f'<text x="{X(LOD_X)+11}" y="{Y(LOD_Y)+4}" font-size="10" fill="#2f5426">lodão</text>')

    a(f'<circle cx="{X(CIT_X)}" cy="{Y(CIT_Y)}" r="4.5" fill="none" stroke="#a84a3a" stroke-width="1.5"/>')
    a(f'<line x1="{X(CIT_X)-5.5}" y1="{Y(CIT_Y)-5.5}" x2="{X(CIT_X)+5.5}" y2="{Y(CIT_Y)+5.5}" stroke="#a84a3a" stroke-width="1.5"/>')
    a(f'<line x1="{X(CIT_X)-5.5}" y1="{Y(CIT_Y)+5.5}" x2="{X(CIT_X)+5.5}" y2="{Y(CIT_Y)-5.5}" stroke="#a84a3a" stroke-width="1.5"/>')
    a(f'<text x="{X(CIT_X)}" y="{Y(CIT_Y)-11}" text-anchor="middle" font-size="9" fill="#a84a3a">laranjeira SAI</text>')

    a(f'<rect x="{X(DRENO_X)-5}" y="{Y(DRENO_Y)-5}" width="10" height="10" fill="none" stroke="#2f6b7d" stroke-width="1.6"/>')

    # ── muros ──
    a(f'<rect x="{X(0)}" y="{Y(0)}" width="{LX*S}" height="{LY*S}" fill="none" stroke="#1a1a18" stroke-width="3.6"/>')
    a(f'<text x="{X(LX/2)}" y="{Y(LY)+30}" text-anchor="middle" font-size="10.5" font-weight="600" '
      f'fill="#8a2f18">MURO SE — 0,0 h Dez · patologia 🔴</text>')
    a(f'<text x="{X(LX/2)}" y="{Y(0)-26}" text-anchor="middle" font-size="10.5" font-weight="600" '
      f'fill="#3f6b32">MURO NW — 4,9 h Dez · a melhor luz</text>')

    # ── cotas ──
    def cotaH(x0,x1,ypx,txt,cor):
        a(f'<line x1="{X(x0)}" y1="{ypx}" x2="{X(x1)}" y2="{ypx}" stroke="{cor}" stroke-width="1.1" '
          f'marker-start="url(#mB{u})" marker-end="url(#mA{u})"/>')
        a(f'<text x="{(X(x0)+X(x1))/2}" y="{ypx-6}" text-anchor="middle" font-size="11" '
          f'font-weight="600" fill="{cor}">{txt}</text>')
    def cotaV(y0,y1,xpx,txt,cor):
        a(f'<line x1="{xpx}" y1="{Y(y0)}" x2="{xpx}" y2="{Y(y1)}" stroke="{cor}" stroke-width="1.1" '
          f'marker-start="url(#mB{u})" marker-end="url(#mA{u})"/>')
        a(f'<text x="{xpx-5}" y="{(Y(y0)+Y(y1))/2}" text-anchor="middle" font-size="10.5" '
          f'font-weight="600" fill="{cor}" transform="rotate(-90 {xpx-5} {(Y(y0)+Y(y1))/2})">{txt}</text>')

    cotaH(0, PLAT, MT-46, "1,50", "#7a6544")
    cotaH(PLAT, PLAT+TRANS, MT-46, "1,75", "#8a2f18")
    cotaH(PLAT+TRANS, LX, MT-46, f"{LX-PLAT-TRANS:.2f}", "#3f6b32")
    cotaH(0, LX, MT-68, "13,00", "#1a1a18")

    if var == "A":
        cotaV(0, banco_y0, ML-36, "2,68", "#3f6b32")
        cotaV(banco_y0, banco_y1, ML-36, "2,00", "#8a6d3b")
        cotaV(esc_y0, esc_y1, ML-36, "1,10", "#2f6b7d")
    else:
        cotaV(0, esc_y0, ML-36, "1,95", "#8a6d3b")
        cotaV(esc_y0, esc_y1, ML-36, "1,10", "#2f6b7d")
        cotaV(esc_y1, LY, ML-36, "2,73", "#8a6d3b")
    cotaV(0, LY, ML-62, "5,78", "#1a1a18")

    a('</svg>')
    return "\n".join(P)

io.open(os.path.join(BASE,"_A.svg"),"w",encoding="utf-8").write(planta("A"))
io.open(os.path.join(BASE,"_B.svg"),"w",encoding="utf-8").write(planta("B"))
print("ok")
