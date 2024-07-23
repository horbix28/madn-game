from PIL import Image

# Bild laden
image = Image.open('pin_disabled.png')

# Überprüfen, ob das Bild im Modus '1' ist
if image.mode != '1':
    image = image.convert('1')

# Bildgröße
width, height = image.size

# Pixel-Liste erstellen
pixel_list = []
for y in range(height):
    row = []
    for x in range(width):
        # Pixelwert abrufen (0 oder 1)
        pixel = image.getpixel((x, y))
        row.append(1 if pixel == 255 else 0)
    pixel_list.append(row)

# Pixel-Liste ausgeben
print(pixel_list)