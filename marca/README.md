# Marca · Ángeles de María

Todo lo de la identidad visual: logos, manual, colores, fuentes y los archivos para volver a generarlos.

## Carpetas

```
marca/
├── Manual_Angeles_de_Maria.png   Manual de marca en una sola imagen
├── logos/                        Cada pieza en PNG (3000 px) y SVG (vector)
│   ├── 1_Logo_principal          Óvalo con clave de sol y ángel (transparente y con fondo)
│   ├── 2_Logo_secundario         "Ángeles de María" con la clave de sol (terracota, claro, oscuro)
│   ├── 3_Submarca_AM             AM con alas (transparente y con fondo marfil)
│   ├── 4_Icono / 4_Angel_solo    Ángel en círculo y ángel solo
│   ├── 5_Paleta                  Colores
│   └── 6_Tipografia              Fuentes
└── fuente/                       Archivos para editar y volver a generar todo
```

## Colores

| Color | Código | Uso |
| --- | --- | --- |
| Terracota oscuro | `#8F422C` | Botones, logo secundario, tarjeta |
| Blanco / Marfil | `#F9EDDE` | Fondos |
| Dorado suave | `#C68C5C` | Detalles, bordes, tipografía |
| Vino oscuro | `#64190B` | Ícono, pie de página, franjas |
| Tinta | `#16131C` | Texto del logo principal |
| Dorado metálico | degradado `#A8743A → #E3BE80 → #C69552 → #EBCB8F` | Ángel, clave de sol, óvalo |

## Fuentes

- **Títulos y logo:** EB Garamond (logo secundario y títulos) y Cinzel (letras del logo principal)
- **Textos, datos y precios:** Montserrat
- Todas gratis en Google Fonts (licencia SIL Open Font).

## Reglas

- El logo principal no se deforma ni se le cambian colores. El óvalo se abre donde pasa el ángel.
- Datos (teléfono, precios, fechas) siempre en Montserrat, nunca en letra decorativa.
- Sobre fondos oscuros, usar las versiones claras.

## Editar y volver a generar (opcional)

En `marca/fuente/`:

1. Instalar: `pip install fonttools brotli` y tener `rsvg-convert` (librsvg).
2. Crear la carpeta `marca/fuente/fonts/` con estas fuentes de Google Fonts (archivos .ttf):
   `Cinzel.ttf` (variable), `EBGaramond.ttf` (variable), `Montserrat.ttf` (variable), `NotoMusic-Regular.ttf`.
3. `python3 build_assets.py` → vuelve a generar todo en `marca/logos/`.
4. `python3 build_manual.py` → vuelve a generar el manual.

Colores, tamaños y posiciones están al inicio y dentro de cada función de `build_assets.py`.
`cherub.svg` (ángel), `am.svg` (AM con alas) y `wing.svg` (ala) son los dibujos en vector.
