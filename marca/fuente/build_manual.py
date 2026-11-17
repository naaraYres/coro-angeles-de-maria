exec(open("build_assets.py").read())
import subprocess

W = 1200
P = []
y = 0
lab = lambda t, x, yy, col: P.append(f'<path d="{montS.path(t, 19, x, yy, 5, "middle")}" fill="{col}"/>')


def place(content, x, yy, s):
    return f'<g transform="translate({x},{yy}) scale({s})">{content}</g>'


# 1. logo principal
H1 = 720
P.append(f'<rect x="0" y="{y}" width="{W}" height="{H1}" fill="{MARFIL}"/>')
P.append(f'<rect x="0" y="{y}" width="{W}" height="{H1}" fill="url(#stars)"/>')
s = 0.98
P.append(place(primary(), W / 2 - 457 * s, y + 20, s))
lab("LOGO PRINCIPAL", W / 2, y + 690, BRONZE := "#7A4A2A")
y += H1

# 2. tiles
H2 = 420; tw = W / 3
P.append(f'<rect x="0" y="{y}" width="{tw}" height="{H2}" fill="{TERRA}"/>')
lab("LOGO SECUNDARIO", tw / 2, y + 55, MARFIL)
s = 0.5
P.append(place(secondary(), tw / 2 - 500 * s, y + 230 - 380 * s, s))
P.append(f'<rect x="{tw}" y="{y}" width="{tw}" height="{H2}" fill="{MARFIL}"/>')
lab("SUBMARCA", tw * 1.5, y + 55, BRONZE)
k = 0.21
P.append(submark(tw * 1.5 - 995 * k, y + 240 - 600 * k, 2080 * k))
P.append(f'<rect x="{2*tw}" y="{y}" width="{tw}" height="{H2}" fill="{OSCURO}"/>')
lab("ÍCONO", tw * 2.5, y + 55, "#E3BE80")
P.append(badge(tw * 2.5, y + 235, 140))
y += H2

# 3. palette
H3 = 400
P.append(f'<rect x="0" y="{y}" width="{W}" height="{H3}" fill="#FFFFFF"/>')
lab("PALETA DE COLORES", W / 2, y + 60, BRONZE)
pal = [(TERRA, "Terracota oscuro"), (MARFIL, "Blanco / Marfil"), (DORADO, "Dorado suave"), (OSCURO, "Vino oscuro")]
for i, (c, n) in enumerate(pal):
    cx = 150 + i * 300
    P.append(f'<circle cx="{cx}" cy="{y + 175}" r="80" fill="{c}" stroke="#e8dccb" stroke-width="2"/>')
    P.append(f'<path d="{montS.path(c, 20, cx, y + 295, 0, "middle")}" fill="{INK}"/>')
    P.append(f'<path d="{mont.path(n, 17, cx, y + 322, 0, "middle")}" fill="{BRONZE}"/>')
P.append(f'<rect x="{W/2-170}" y="{y + 345}" width="340" height="38" rx="19" fill="url(#gold)"/>')
P.append(f'<path d="{montS.path("DORADO METÁLICO · LOGO", 14, W/2, y + 369, 2, "middle")}" fill="{INK}"/>')
y += H3

# 4. typography
H4 = 360
P.append(f'<rect x="0" y="{y}" width="{W}" height="{H4}" fill="{DORADO}"/>')
lab("TIPOGRAFÍA", W / 2, y + 60, INK)
P.append(f'<path d="{gar.path("Aa", 170, 70, y + 255)}" fill="{INK}"/>')
P.append(f'<path d="{garM.path("EB Garamond", 42, 290, y + 160)}" fill="{INK}"/>')
P.append(f'<path d="{mont.path("Títulos y logo", 16, 290, y + 190)}" fill="{INK}"/>')
P.append(f'<path d="{gar.path("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", 19, 290, y + 230)}" fill="{INK}"/>')
P.append(f'<path d="{gar.path("abcdefghijklmnñopqrstuvwxyz 1234567890", 19, 290, y + 258)}" fill="{INK}"/>')
P.append(f'<path d="{mont.path("Aa", 150, 640, y + 255)}" fill="{INK}"/>')
P.append(f'<path d="{montS.path("Montserrat", 38, 880, y + 160)}" fill="{INK}"/>')
P.append(f'<path d="{mont.path("Textos, datos y precios", 16, 880, y + 190)}" fill="{INK}"/>')
P.append(f'<path d="{mont.path("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", 13, 880, y + 230)}" fill="{INK}"/>')
P.append(f'<path d="{mont.path("abcdefghijklmnñopqrstuvwxyz 123", 13, 880, y + 258)}" fill="{INK}"/>')
y += H4

# 5. applications
H5 = 640
P.append(f'<rect x="0" y="{y}" width="{W}" height="{H5}" fill="{MARFIL}"/>')
lab("APLICACIONES", W / 2, y + 55, BRONZE)
cx0, cy0 = 40, y + 100
P.append(f'<g filter="url(#sh)"><rect x="{cx0}" y="{cy0}" width="340" height="200" rx="10" fill="#FFFDF8"/></g>')
s = 0.27
P.append(place(primary(), cx0 + 170 - 457 * s, cy0 + 12, s))
P.append(f'<g filter="url(#sh)"><rect x="{cx0}" y="{cy0+230}" width="340" height="200" rx="10" fill="{TERRA}"/></g>')
P.append(f'<path d="{garM.path("Ángeles de María", 30, cx0 + 24, cy0 + 285)}" fill="{MARFIL}"/>')
for i, t in enumerate(["Coros y eventos", "WhatsApp 999 000 000", "@angelesdemaria", "angelesdemaria.eventos@gmail.com"]):
    P.append(f'<path d="{mont.path(t, 14, cx0 + 24, cy0 + 325 + i * 24)}" fill="{MARFIL}"/>')
P.append(f'<path d="{mont.path("Tarjeta de presentación", 15, cx0 + 170, cy0 + 465, 0, "middle")}" fill="{BRONZE}"/>')
# post
px, py, pw = 420, y + 100, 360; ph = pw * 1.25
P.append(f'<g filter="url(#sh)"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="#FFFDF8"/></g>')
P.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="url(#stars)"/>')
P.append(cherub(px + pw / 2 - 80, py + 25, 160))
P.append(f'<path d="{garM.path("Villancicos", 50, px + pw/2, py + 230, 0, "middle")}" fill="{TERRA}"/>')
P.append(f'<path d="{gar.path("para tu evento", 32, px + pw/2, py + 268, 0, "middle")}" fill="{TERRA}"/>')
for i, t in enumerate(["Encendido de árbol", "Fiestas de fin de año", "Coro de niños y adultos"]):
    P.append(f'<path d="{mont.path(t, 15, px + pw/2, py + 315 + i * 25, 0, "middle")}" fill="{INK}"/>')
P.append(f'<rect x="{px}" y="{py + ph - 54}" width="{pw}" height="54" fill="{OSCURO}"/>')
P.append(f'<path d="{montS.path("Reserva tu fecha de diciembre", 15, px + pw/2, py + ph - 21, 0, "middle")}" fill="{MARFIL}"/>')
P.append(f'<path d="{mont.path("Post para redes", 15, px + pw/2, py + ph + 32, 0, "middle")}" fill="{BRONZE}"/>')
# pattern
qx, qy, qw = 820, y + 100, 340; qh = 450
P.append(f'<g filter="url(#sh)"><rect x="{qx}" y="{qy}" width="{qw}" height="{qh}" fill="{OSCURO}"/></g>')
P.append(f'<rect x="{qx}" y="{qy}" width="{qw}" height="{qh}" fill="url(#pat)"/>')
P.append(f'<path d="{mont.path("Patrón de marca", 15, qx + qw/2, qy + qh + 32, 0, "middle")}" fill="{BRONZE}"/>')
y += H5

star = "M0,-9 L2.4,-2.4 L9,0 L2.4,2.4 L0,9 L-2.4,2.4 L-9,0 L-2.4,-2.4Z"
clef = music.path(CLEF, 40, 25, 75, anchor="middle")
mini = f'<g transform="translate(52,92) scale({50/1508})">{CHERUB}</g>'
extra = f'''<pattern id="stars" width="130" height="130" patternUnits="userSpaceOnUse">
<path d="{star}" transform="translate(22,26) scale(0.7)" fill="{DORADO}" opacity="0.35"/>
<path d="{star}" transform="translate(92,88) scale(0.45)" fill="{DORADO}" opacity="0.3"/></pattern>
<pattern id="pat" width="110" height="150" patternUnits="userSpaceOnUse">
<path d="{clef}" fill="#C69552"/>
<g fill="#C69552">{mini}</g>
<path d="{star}" transform="translate(90,30) scale(0.5)" fill="#E3BE80"/></pattern>
<filter id="sh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#3a2a18" flood-opacity="0.22"/></filter>'''
out = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {y}" width="{W}" height="{y}"><defs>{GOLD}{extra}</defs>{"".join(P)}</svg>'
open("../Manual_Angeles_de_Maria.svg", "w").write(out)
subprocess.run(["rsvg-convert", "-w", "2400", "../Manual_Angeles_de_Maria.svg", "-o", "../Manual_Angeles_de_Maria.png"], check=True)
subprocess.run(["rsvg-convert", "-w", "1100", "../Manual_Angeles_de_Maria.svg", "-o", "/tmp/manual_prev.png"], check=True)
print(y)
