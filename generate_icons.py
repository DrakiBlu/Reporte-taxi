"""
Genera los íconos PNG del taxi para todas las densidades de Android.
Se ejecuta en GitHub Actions antes de compilar el APK.
"""
from PIL import Image, ImageDraw
import os

SIZES = {
    'mipmap-mdpi':    48,
    'mipmap-hdpi':    72,
    'mipmap-xhdpi':   96,
    'mipmap-xxhdpi':  144,
    'mipmap-xxxhdpi': 192,
}

def draw_taxi_icon(size):
    s = size / 192.0

    # Fondo azul marino #003366
    img = Image.new('RGBA', (size, size), (0, 51, 102, 255))
    d = ImageDraw.Draw(img)

    # ── Cabina (trapecio amarillo) ──
    cabin = [
        (int(45*s), int(100*s)),
        (int(55*s), int(58*s)),
        (int(137*s), int(58*s)),
        (int(147*s), int(100*s)),
    ]
    d.polygon(cabin, fill=(255, 215, 0))

    # ── Letrero blanco en el techo ──
    d.rounded_rectangle(
        [int(74*s), int(27*s), int(118*s), int(48*s)],
        radius=max(1, int(5*s)),
        fill=(255, 255, 255)
    )

    # ── Ventana izquierda (azul oscuro) ──
    lw = [
        (int(56*s), int(98*s)),
        (int(60*s), int(65*s)),
        (int(91*s), int(65*s)),
        (int(89*s), int(98*s)),
    ]
    d.polygon(lw, fill=(26, 74, 138))

    # ── Ventana derecha (azul oscuro) ──
    rw = [
        (int(136*s), int(98*s)),
        (int(132*s), int(65*s)),
        (int(101*s), int(65*s)),
        (int(103*s), int(98*s)),
    ]
    d.polygon(rw, fill=(26, 74, 138))

    # ── Franja amarilla oscura ──
    d.rectangle(
        [int(18*s), int(95*s), int(174*s), int(108*s)],
        fill=(249, 168, 37)
    )

    # ── Cuerpo inferior (amarillo) ──
    d.rounded_rectangle(
        [int(18*s), int(100*s), int(174*s), int(158*s)],
        radius=max(1, int(9*s)),
        fill=(255, 215, 0)
    )

    # ── Ruedas ──
    for cx in [int(57*s), int(135*s)]:
        cy = int(158*s)
        # Neumático
        r = int(19*s)
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(34, 34, 34))
        # Aro
        r2 = int(8*s)
        d.ellipse([cx-r2, cy-r2, cx+r2, cy+r2], fill=(180, 180, 180))

    # ── Faro delantero (blanco-amarillo) ──
    d.ellipse(
        [int(154*s), int(112*s), int(172*s), int(126*s)],
        fill=(255, 255, 200)
    )

    # ── Luz trasera (roja) ──
    d.ellipse(
        [int(20*s), int(112*s), int(38*s), int(126*s)],
        fill=(204, 0, 0)
    )

    return img


base = 'android/app/src/main/res'
for folder, size in SIZES.items():
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    img = draw_taxi_icon(size)
    for name in ['ic_launcher.png', 'ic_launcher_round.png', 'ic_launcher_foreground.png']:
        img.save(os.path.join(path, name))
    print(f'  {size}x{size}px → {folder}')

print('✓ Todos los íconos generados.')
