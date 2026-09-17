from run import *
import solar
# 1) sensibilidade a resolucao de grelha e passo temporal
print("=== robustez numerica (media do jardim, Dez) ===")
import importlib
for g in [0.5,0.25,0.125]:
    pts=grid_points(0,LX,0,LY,step=g)
    b=zone_hours(pts,DATES[0][1],0,(2.50,2.50,2.50,15.50))
    p=zone_hours(pts,DATES[0][1],0,(2.00,2.00,2.00,15.00))
    print(f"  grelha {g:>5} m -> base {b:.2f} h | +0,50 {p:.2f} h | delta {p-b:+.2f}")

# 2) sensibilidade a incerteza da altura dos muros (<=2,50 e "observado")
print("\n=== e se os muros nao forem exactamente 2,50? (Dez, media) ===")
for hw in [2.20,2.35,2.50,2.65,2.80]:
    b=zone_hours(WHOLE,DATES[0][1],0,(hw,hw,hw,15.50))
    p=zone_hours(WHOLE,DATES[0][1],0,(hw-0.5,hw-0.5,hw-0.5,15.00))
    print(f"  muro {hw:.2f} m -> base {b:.2f} h | +0,50 {p:.2f} h | delta {p-b:+.2f} | racio {p/b if b else 0:.2f}x")

# 3) Quantos m2 do jardim passam o limiar de 3 h em Dezembro?
print("\n=== area (m2) acima de limiares, 21 Dez ===")
def area_above(h, thr, date, tz):
    step=0.25
    pts=grid_points(0,LX,0,LY,step=step)
    cell=step*step
    tot=0
    for (x,y) in pts:
        v=zone_hours([(x,y)],date,tz,h)
        if v>=thr: tot+=cell
    return tot
for lbl,h in [("base",(2.50,2.50,2.50,15.50)),("+0,50",(2.00,2.00,2.00,15.00)),
              ("D (+0,50 & SW 0,50)",(2.00,2.00,0.50,15.00))]:
    a3=area_above(h,3.0,DATES[0][1],0)
    a2=area_above(h,2.0,DATES[0][1],0)
    print(f"  {lbl:<22} >=2h: {a2:5.1f} m2 ({a2/75.1*100:4.1f}%)   >=3h: {a3:5.1f} m2 ({a3/75.1*100:4.1f}%)")
