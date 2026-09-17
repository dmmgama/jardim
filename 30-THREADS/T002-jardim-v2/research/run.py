from solar import *
from datetime import datetime, timedelta

DATES = [
    ("21 Dez",    datetime(2025,12,21), 0),
    ("Equinocio", datetime(2026,3,21),  0),
    ("21 Jun",    datetime(2026,6,21),  1),
]

ZONES = [
    ("Junto a fachada (X 0-2,5)",      0.0,  2.5,  0.0,  LY),
    ("Plataforma central (X 2,5-6,7)", 2.5,  6.7,  0.0,  LY),
    ("Canteiro da citrinheira",        6.70, 10.38,1.73, 4.64),
    ("Canteiro linear SE",             2.49, 10.24,5.18, LY),
    ("Zona SW / palmeira",             10.38,LX,   0.0,  LY),
    ("Canteiro NW (Y 0-0,60)",         2.49, 10.38,0.0,  0.60),
]

STEP_MIN = 2
GRID = 0.25

def grid_points(x0,x1,y0,y1,step=GRID):
    pts=[]
    nx=max(1,int(round((x1-x0)/step))); ny=max(1,int(round((y1-y0)/step)))
    for i in range(nx):
        for j in range(ny):
            pts.append((x0+(i+0.5)*(x1-x0)/nx, y0+(j+0.5)*(y1-y0)/ny))
    return pts

def zone_hours(pts, date, tz, h):
    h_nw,h_se,h_sw,h_fac = h
    tot=0.0; n=len(pts); dt_h=STEP_MIN/60.0
    t=date.replace(hour=0,minute=0); end=date+timedelta(days=1)
    while t<end:
        elev,az = solar_position(t, tz_offset=tz)
        if elev>0:
            ux,uy,uz = sun_vector_local(elev,az)
            lit=sum(1 for (x,y) in pts if is_sunlit(x,y,ux,uy,uz,h_nw,h_se,h_sw,h_fac))
            tot += (lit/n)*dt_h
        t += timedelta(minutes=STEP_MIN)
    return tot

WHOLE = grid_points(0,LX,0,LY)

def run(label, h, quiet=False):
    if not quiet:
        print(f"\n=== {label} ===")
        print(f"{'Zona':<34}" + "".join(f"{d:>11}" for d,_,_ in DATES))
    out={}
    for (name,x0,x1,y0,y1) in ZONES:
        pts=grid_points(x0,x1,y0,y1)
        vals=[zone_hours(pts,d,tz,h) for _,d,tz in DATES]
        out[name]=vals
        if not quiet:
            print(f"{name:<34}" + "".join(f"{v:>11.1f}" for v in vals))
    vals=[zone_hours(WHOLE,d,tz,h) for _,d,tz in DATES]
    out["MEDIA"]=vals
    if not quiet:
        print(f"{'MEDIA DO JARDIM':<34}" + "".join(f"{v:>11.1f}" for v in vals))
    return out

if __name__=="__main__":
    base = run("BASE - cota actual (muros 2,50 / fachada 15,50)", (2.50,2.50,2.50,15.50))
    plus = run("+0,50 m (muros 2,00 / fachada 15,00)",            (2.00,2.00,2.00,15.00))
    print("\n--- DELTA (+0,50 menos base), horas ---")
    print(f"{'Zona':<34}" + "".join(f"{d:>11}" for d,_,_ in DATES))
    for k in base:
        d=[p-b for p,b in zip(plus[k],base[k])]
        print(f"{k:<34}" + "".join(f"{v:>+11.1f}" for v in d))
