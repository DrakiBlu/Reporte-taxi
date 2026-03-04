"""
Genera los íconos PNG del taxi (Frontal Material) para todas las densidades de Android.
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
    scale = size / 108.0

    # Lienzo transparente
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Fondo circular azul marino (#003366) 
    d.ellipse([4*scale, 4*scale, 104*scale, 104*scale], fill=(0, 51, 102))

    # Ruedas oscuras (#222222)
    radius3 = max(1, int(3*scale))
    d.rounded_rectangle([30*scale, 72*scale, 40*scale, 84*scale], radius=radius3, fill=(34, 34, 34))
    d.rounded_rectangle([68*scale, 72*scale, 78*scale, 84*scale], radius=radius3, fill=(34, 34, 34))

    # Cabina superior (#FFC107)
    d.polygon([(38*scale, 36*scale), (70*scale, 36*scale), (78*scale, 50*scale), (30*scale, 50*scale)], fill=(255, 193, 7))

    # Cuerpo base (#FFD700)
    radius8 = max(1, int(8*scale))
    d.rounded_rectangle([26*scale, 50*scale, 82*scale, 70*scale], radius=radius8, fill=(255, 215, 0))

    # Parabrisas (#1A4A8A)
    d.polygon([(40*scale, 39*scale), (68*scale, 39*scale), (74*scale, 48*scale), (34*scale, 48*scale)], fill=(26, 74, 138))

    # Reflejo parabrisas (#4D7BB0) para dar profundidad
    d.polygon([(42*scale, 40*scale), (60*scale, 40*scale), (63*scale, 45*scale), (37*scale, 45*scale)], fill=(77, 123, 176))

    # Letrero de TAXI blanco en techo
    radius2 = max(1, int(2*scale))
    d.rounded_rectangle([46*scale, 28*scale, 62*scale, 34*scale], radius=radius2, fill=(255, 255, 255))
    d.rectangle([50*scale, 30*scale, 58*scale, 32*scale], fill=(51, 51, 51))

    # Franja a cuadros (simulada)
    d.rectangle([20*scale, 58*scale, 88*scale, 62*scale], fill=(51, 51, 51))
    for x in range(24, 84, 8):
        d.rectangle([x*scale, 58*scale, (x+4)*scale, 62*scale], fill=(255, 255, 255))

    # Faros principales (blancos)
    d.ellipse([26*scale, 61*scale, 34*scale, 69*scale], fill=(255, 255, 255))
    d.ellipse([74*scale, 61*scale, 82*scale, 69*scale], fill=(255, 255, 255))

    # Parrilla central
    radius1 = max(1, int(1*scale))
    d.rounded_rectangle([46*scale, 65*scale, 62*scale, 71*scale], radius=radius1, fill=(51, 51, 51))

    # Luces intermitentes / direccionales (naranjas)
    d.ellipse([20*scale, 63*scale, 24*scale, 67*scale], fill=(255, 152, 0))
    d.ellipse([84*scale, 63*scale, 88*scale, 67*scale], fill=(255, 152, 0))

    return img

base = 'android/app/src/main/res'
for folder, size in SIZES.items():
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    img = draw_taxi_icon(size)
    for name in ['ic_launcher.png', 'ic_launcher_round.png', 'ic_launcher_foreground.png']:
        img.save(os.path.join(path, name))
    print(f'  {size}x{size}px -> {folder}')

print('Nuevos iconos frontales premium generados.')
