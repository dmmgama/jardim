"""
Estimativa de sol directo ao nivel do pavimento - quintal Calcada da Boa Hora 15.
Modelo geometrico proprio da T002, para verificar o efeito da subida de cota.
Sem dependencias externas: NOAA solar position + ray casting analitico.
"""
import math
from datetime import datetime, timedelta

LAT = 38.69967
LON = -9.19038
# Geometria interior
LX = 13.00   # X: da fachada (X=0) ao muro SW (X=13)
LY = 5.78    # Y: do muro NW (Y=0) ao muro SE (Y=5.78)

# Azimutes (graus, do Norte, sentido horario)
AZ_SW = 245.0   # normal exterior do muro SW = direccao em que X cresce
AZ_SE = 155.0   # normal exterior do muro SE = direccao em que Y cresce
# Verificacao: SE = SW - 90 -> 245-90 = 155. Consistente com o dossier.

def solar_position(dt_local, lat=LAT, lon=LON, tz_offset=0):
    """NOAA solar position. dt_local em hora local; tz_offset em horas."""
    dt = dt_local - timedelta(hours=tz_offset)
    # Julian day
    y, m = dt.year, dt.month
    d = dt.day + (dt.hour + dt.minute/60 + dt.second/3600)/24
    if m <= 2:
        y -= 1; m += 12
    A = y // 100
    B = 2 - A + A // 4
    jd = math.floor(365.25*(y+4716)) + math.floor(30.6001*(m+1)) + d + B - 1524.5
    jc = (jd - 2451545.0) / 36525.0
    # Geometric mean longitude / anomaly
    gml = (280.46646 + jc*(36000.76983 + jc*0.0003032)) % 360
    gma = 357.52911 + jc*(35999.05029 - 0.0001537*jc)
    ecc = 0.016708634 - jc*(0.000042037 + 0.0000001267*jc)
    gma_r = math.radians(gma)
    ctr = (math.sin(gma_r)*(1.914602 - jc*(0.004817 + 0.000014*jc))
           + math.sin(2*gma_r)*(0.019993 - 0.000101*jc)
           + math.sin(3*gma_r)*0.000289)
    true_long = gml + ctr
    omega = 125.04 - 1934.136*jc
    app_long = true_long - 0.00569 - 0.00478*math.sin(math.radians(omega))
    # Obliquity
    e0 = 23 + (26 + ((21.448 - jc*(46.815 + jc*(0.00059 - jc*0.001813))))/60)/60
    e = e0 + 0.00256*math.cos(math.radians(omega))
    e_r = math.radians(e)
    app_r = math.radians(app_long)
    decl = math.degrees(math.asin(math.sin(e_r)*math.sin(app_r)))
    # Equation of time
    vy = math.tan(e_r/2)**2
    gml_r = math.radians(gml)
    eot = 4*math.degrees(vy*math.sin(2*gml_r) - 2*ecc*math.sin(gma_r)
                         + 4*ecc*vy*math.sin(gma_r)*math.cos(2*gml_r)
                         - 0.5*vy*vy*math.sin(4*gml_r)
                         - 1.25*ecc*ecc*math.sin(2*gma_r))
    # Hour angle
    tst = (dt.hour*60 + dt.minute + dt.second/60) + eot + 4*lon
    ha = tst/4 - 180
    if ha < -180: ha += 360
    ha_r = math.radians(ha)
    lat_r = math.radians(lat)
    decl_r = math.radians(decl)
    cos_z = (math.sin(lat_r)*math.sin(decl_r)
             + math.cos(lat_r)*math.cos(decl_r)*math.cos(ha_r))
    cos_z = max(-1, min(1, cos_z))
    zen = math.degrees(math.acos(cos_z))
    elev = 90 - zen
    # Azimuth
    if abs(math.sin(math.radians(zen))) < 1e-9:
        az = 180.0
    else:
        ca = ((math.sin(lat_r)*cos_z - math.sin(decl_r))
              / (math.cos(lat_r)*math.sin(math.radians(zen))))
        ca = max(-1, min(1, ca))
        az = math.degrees(math.acos(ca))
        if ha > 0:
            az = 360 - az
        az = (az + 180) % 360
    return elev, az

def sun_vector_local(elev, az):
    """
    Vector unitario para o Sol no referencial do jardim.
    Eixo x do jardim aponta para azimute AZ_SW (245). Eixo y para AZ_SE (155).
    Devolve (ux, uy, uz) - componentes horizontais na direccao em que x e y crescem.
    """
    e = math.radians(elev)
    # angulo do sol relativo ao eixo x do jardim
    dx = math.radians(az - AZ_SW)
    dy = math.radians(az - AZ_SE)
    ux = math.cos(e)*math.cos(dx)
    uy = math.cos(e)*math.cos(dy)
    uz = math.sin(e)
    return ux, uy, uz

def is_sunlit(x, y, ux, uy, uz, h_nw, h_se, h_sw, h_fac):
    """
    Ponto (x,y) ao nivel do pavimento ve o Sol?
    Alturas dos obstaculos medidas ACIMA DO PAVIMENTO.
    Muro NW em y=0, SE em y=LY, SW em x=LX, fachada em x=0.
    """
    if uz <= 0:
        return False
    # Fachada (x=0): bloqueia quando o sol esta do lado x<0, i.e. ux<0
    if ux < 0:
        t = x / (-ux)           # distancia horizontal ate ao plano x=0
        if t*uz/1.0 < h_fac:    # altura do raio ao atingir o plano
            # altura do raio no plano = t*(uz/horiz) ; normalizamos abaixo
            pass
    # Fazemos de forma limpa: para cada plano, altura do raio ao cruza-lo
    def blocked(dist_h, comp, h_obst):
        """dist_h: distancia no eixo ate ao plano; comp: componente do vector nesse eixo
        (tem de ter o sinal que leva ao plano). Devolve True se o obstaculo tapa."""
        if comp == 0:
            return False
        t = dist_h / comp   # parametro ao longo do raio (>0 se vai nessa direccao)
        if t <= 0:
            return False
        z = t * uz
        return z < h_obst
    # fachada NE em x=0 -> alcanca-se com ux negativo
    if blocked(0 - x, ux, h_fac): return False
    # muro SW em x=LX -> ux positivo
    if blocked(LX - x, ux, h_sw): return False
    # muro NW em y=0 -> uy negativo
    if blocked(0 - y, uy, h_nw): return False
    # muro SE em y=LY -> uy positivo
    if blocked(LY - y, uy, h_se): return False
    return True
