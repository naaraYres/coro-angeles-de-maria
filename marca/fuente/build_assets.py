import re, subprocess, os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen


class F:
    def __init__(self, p, w=None):
        f = TTFont(p)
        if w and 'fvar' in f:
            f = instancer.instantiateVariableFont(f, {"wght": w})
        self.cmap = f.getBestCmap(); self.gs = f.getGlyphSet(); self.hm = f["hmtx"]; self.upm = f["head"].unitsPerEm

    def width(self, s, size, track=0):
        return sum(self.hm[self.cmap[ord(c)]][0] for c in s) * size / self.upm + track * (len(s) - 1)

    def path(self, s, size, x, base, track=0, anchor="start"):
        w = self.width(s, size, track)
        if anchor == "middle": x -= w / 2
        elif anchor == "end": x -= w
        sc = size / self.upm; pen = SVGPathPen(self.gs)
        for c in s:
            g = self.cmap[ord(c)]
            self.gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x, base)))
            x += self.hm[g][0] * sc + track
        return pen.getCommands()


cinzel = F("fonts/Cinzel.ttf", 600)
gar = F("fonts/EBGaramond.ttf", 450)
garM = F("fonts/EBGaramond.ttf", 500)
mont = F("fonts/Montserrat.ttf", 500)
montS = F("fonts/Montserrat.ttf", 600)
music = F("fonts/NotoMusic-Regular.ttf")
CLEF = chr(0x1D11E)

TERRA, MARFIL, DORADO, OSCURO, INK = "#8F422C", "#F9EDDE", "#C68C5C", "#64190B", "#16131C"
GOLD = '''<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#A8743A"/><stop offset="0.35" stop-color="#E3BE80"/><stop offset="0.55" stop-color="#C69552"/>
<stop offset="0.8" stop-color="#EBCB8F"/><stop offset="1" stop-color="#9E6B34"/></linearGradient>
<linearGradient id="ring" x1="0" y1="0" x2="0.3" y2="1">
<stop offset="0" stop-color="#F4E6C8"/><stop offset="0.18" stop-color="#C9A675"/><stop offset="0.42" stop-color="#8F6A3F"/>
<stop offset="0.6" stop-color="#E9D3A8"/><stop offset="0.82" stop-color="#B08A57"/><stop offset="1" stop-color="#F1E2C2"/></linearGradient>
<filter id="lsh" x="-10%" y="-10%" width="120%" height="125%"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="#3a2a18" flood-opacity="0.22"/></filter>'''


def body(p):
    s = open(p).read()
    s = s[s.index(">", s.index("<svg")) + 1:s.rindex("</svg>")]
    return re.sub(r'fill="[^"]*"', '', s)


CHERUB = body("cherub.svg")  # 1508 x 1427, faces right
WING = body("wing.svg")      # 599 x 663, left wing


def cherub(x, y, w, fill="url(#gold)"):
    sc = w / 1508
    return f'<g transform="translate({x},{y}) scale({sc})" fill="{fill}">{CHERUB}</g>'


def svg(vb, content, bg=None):
    x, y, w, h = vb
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" width="{w}" height="{h}"><defs>{GOLD}</defs>{b}{content}</svg>'


def save(name, s, px=3000):
    os.makedirs("../logos", exist_ok=True)
    open(f"../logos/{name}.svg", "w").write(s)
    subprocess.run(["rsvg-convert", "-w", str(px), f"../logos/{name}.svg", "-o", f"../logos/{name}.png"], check=True)


# ---------- 1. Logo principal ----------
def primary():
    # coordinates measured from the reference image (910 x 650 space)
    o = []
    cx, cy, rx, ry = 457, 360, 418, 258
    sc = 260 / 1508
    o.append(f'''<mask id="angelgap" maskUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="900">
<rect x="-100" y="-100" width="1200" height="900" fill="white"/>
<g transform="translate(340,12) scale({sc})" fill="black" stroke="black" stroke-width="{16/sc}" stroke-linejoin="round">{CHERUB}</g></mask>''')
    o.append(f'<g filter="url(#lsh)"><ellipse cx="{cx}" cy="{cy}" rx="{rx-11}" ry="{ry-11}" fill="#F7ECDF"/></g>')
    o.append(f'<g mask="url(#angelgap)"><ellipse cx="{cx}" cy="{cy}" rx="{rx-11}" ry="{ry-11}" fill="none" stroke="url(#ring)" stroke-width="22"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx-30}" ry="{ry-30}" fill="none" stroke="url(#ring)" stroke-width="5"/></g>')
    S = 128; tr = 2
    o.append(f'<path d="{cinzel.path("Án", S, 343, 340, tr, "end")}" fill="{INK}"/>')
    o.append(f'<path d="{cinzel.path("eles", S, 418, 340, tr)}" fill="{INK}"/>')
    o.append(f'<path d="{cinzel.path("de María", S, 495, 465, tr + 2, "middle")}" fill="{INK}"/>')
    o.append(f'<path d="{music.path(CLEF, 133, 380, 342, anchor="middle")}" fill="url(#gold)"/>')
    t = "COROS & EVENTOS"; w0 = mont.width(t, 40); tr = (465 - w0) / (len(t) - 1)
    o.append(f'<path d="{mont.path(t, 40, 225, 530, tr)}" fill="{INK}"/>')
    o.append(cherub(340, 12, 260))
    return "".join(o)


save("1_Logo_principal", svg((20, 0, 875, 650), primary()))
save("1_Logo_principal_fondo_claro", svg((-40, -40, 995, 730), primary(), "#F4F1EC"))


# ---------- 2. Logo secundario ----------
def secondary(col=MARFIL, sub=MARFIL):
    o = []; cx = 500
    size = 150
    a = "Án"; e = "eles"; cw = 50
    aw, ew = gar.width(a, size), gar.width(e, size)
    x0 = cx - (aw + cw + ew) / 2; b1 = 300
    o.append(f'<path d="{gar.path(a, size, x0, b1)}" fill="{col}"/>')
    o.append(f'<path d="{gar.path(e, size, x0 + aw + cw, b1)}" fill="{col}"/>')
    o.append(f'<path d="{music.path(CLEF, 118, x0 + aw + cw/2, b1 + 22, anchor="middle")}" fill="url(#gold)"/>')
    o.append(f'<path d="{gar.path("de María", size, cx, b1 + 150, 0, "middle")}" fill="{col}"/>')
    o.append(f'<path d="{mont.path("COROS Y EVENTOS", 34, cx, b1 + 225, 9, "middle")}" fill="{sub}"/>')
    return "".join(o)


save("2_Logo_secundario_fondo_terracota", svg((0, 0, 1000, 640), secondary(), TERRA))
save("2_Logo_secundario_transparente_oscuro", svg((150, 80, 700, 480), secondary(INK, INK)))
save("2_Logo_secundario_transparente_claro", svg((150, 80, 700, 480), secondary()))


# ---------- 3. Submarca (opcion 3: AM con alas) ----------
AM = body("am.svg")  # 2080 x 1280


def submark(x=0, y=0, w=2080):
    sc = w / 2080
    return f'<g transform="translate({x},{y}) scale({sc})" fill="url(#gold)">{AM}</g>'


save("3_Submarca_AM", svg((280, 100, 1440, 1020), submark()))
save("3_Submarca_AM_fondo_marfil", svg((0, -100, 2080, 1480), submark(), MARFIL))


# ---------- 4. Icono / brandmark (sin estrellas) ----------
def badge(cx, cy, r, fill="url(#gold)"):
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{fill}" stroke-width="{r*0.03}"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r*0.9}" fill="none" stroke="{fill}" stroke-width="{r*0.012}"/>']
    w = r * 1.2
    o.append(cherub(cx - w / 2, cy - w * 1427 / 1508 / 2, w, fill))
    return "".join(o)


save("4_Icono_fondo_oscuro", svg((0, 0, 1000, 1000), badge(500, 500, 400), OSCURO))
save("4_Icono_transparente", svg((80, 80, 840, 840), badge(500, 500, 400)))
save("4_Angel_solo", svg((0, 0, 1508, 1427), cherub(0, 0, 1508)))


# ---------- 5. Paleta ----------
pal = [(TERRA, "Terracota oscuro"), (MARFIL, "Blanco / Marfil"), (DORADO, "Dorado suave"), (OSCURO, "Vino oscuro")]
o = [f'<path d="{montS.path("PALETA DE COLORES", 34, 800, 110, 6, "middle")}" fill="{INK}"/>']
for i, (c, n) in enumerate(pal):
    x = 200 + i * 400
    o.append(f'<circle cx="{x}" cy="330" r="140" fill="{c}" stroke="#e8dccb" stroke-width="3"/>')
    o.append(f'<path d="{mont.path(n, 32, x, 540, 0, "middle")}" fill="{INK}"/>')
    o.append(f'<path d="{mont.path(c, 32, x, 590, 0, "middle")}" fill="{INK}"/>')
o.append(f'<rect x="560" y="660" width="480" height="70" rx="35" fill="url(#gold)"/>')
o.append(f'<path d="{mont.path("Dorado metálico (logo)", 28, 800, 706, 0, "middle")}" fill="{INK}"/>')
save("5_Paleta", svg((0, 0, 1600, 800), "".join(o), "#FFFFFF"), 2400)

# ---------- 6. Tipografia ----------
o = [f'<path d="{montS.path("TIPOGRAFÍA", 34, 800, 100, 6, "middle")}" fill="{INK}"/>']
o.append(f'<path d="{gar.path("Garamond / Serif", 110, 60, 270)}" fill="{INK}"/>')
o.append(f'<path d="{gar.path("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 44, 60, 350)}" fill="{INK}"/>')
o.append(f'<path d="{gar.path("abcdefghijklmnopqrstuvwxyz", 44, 60, 410)}" fill="{INK}"/>')
o.append(f'<path d="{gar.path("1234567890 @ # & ¡! ¿?", 44, 60, 470)}" fill="{INK}"/>')
o.append(f'<path d="{mont.path("Títulos y logo", 28, 60, 530)}" fill="{TERRA}"/>')
mx = 860
o.append(f'<path d="{montS.path("Montserrat", 96, mx, 270)}" fill="{INK}"/>')
o.append(f'<path d="{mont.path("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 34, mx, 350)}" fill="{INK}"/>')
o.append(f'<path d="{mont.path("abcdefghijklmnopqrstuvwxyz", 34, mx, 410)}" fill="{INK}"/>')
o.append(f'<path d="{mont.path("1234567890 @ # & ¡! ¿?", 34, mx, 470)}" fill="{INK}"/>')
o.append(f'<path d="{mont.path("Textos, datos y precios", 28, mx, 530)}" fill="{TERRA}"/>')
save("6_Tipografia", svg((0, 0, 1600, 600), "".join(o), "#FFFFFF"), 2400)
print("ok")
