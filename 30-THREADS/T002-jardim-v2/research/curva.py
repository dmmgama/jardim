from run import *

print("=== PEDIDO 3 - CURVA: media do jardim por cota ===")
print(f"{'Cota':<10}" + "".join(f"{d:>11}" for d,_,_ in DATES) + f"{'ganho Dez':>12}")
prev=None
for c in [0.00,0.20,0.30,0.40,0.50,0.60,0.75,1.00]:
    h=(2.50-c,2.50-c,2.50-c,15.50-c)
    vals=[zone_hours(WHOLE,d,tz,h) for _,d,tz in DATES]
    inc = "" if prev is None else f"{vals[0]-prev:>+12.2f}"
    print(f"+{c:<9.2f}" + "".join(f"{v:>11.2f}" for v in vals) + inc)
    prev=vals[0]

print()
print("=== PEDIDO 4 - cenarios muro SW (gradeamento = transparente) ===")
SW = ("Zona SW / palmeira",10.38,LX,0.0,LY)
pts_sw = grid_points(*SW[1:])
cen = [
 ("A  chao 0,00 | SW 2,50 | outros 2,50", (2.50,2.50,2.50,15.50)),
 ("B  chao +0,50 | SW 2,00 | outros 2,00",(2.00,2.00,2.00,15.00)),
 ("C  chao 0,00 | SW 1,00+grade | outros 2,50",(2.50,2.50,1.00,15.50)),
 ("D  chao +0,50 | SW 0,50+grade | outros 2,00",(2.00,2.00,0.50,15.00)),
 ("D' chao +0,50 | SW 0,00 (so grade) | outros 2,00",(2.00,2.00,0.00,15.00)),
]
print(f"{'Cenario':<52}{'zona SW: Dez/Eq/Jun':>26}   {'media jardim: Dez/Eq/Jun':>26}")
for name,h in cen:
    sw=[zone_hours(pts_sw,d,tz,h) for _,d,tz in DATES]
    md=[zone_hours(WHOLE,d,tz,h) for _,d,tz in DATES]
    print(f"{name:<52}" + f"{sw[0]:>8.1f}{sw[1]:>9.1f}{sw[2]:>9.1f}" + "   " + f"{md[0]:>8.1f}{md[1]:>9.1f}{md[2]:>9.1f}")
