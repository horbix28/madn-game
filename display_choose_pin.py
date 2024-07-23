import time
from PIL import Image, ImageDraw, ImageFont
import random

HOLLOW_PIN = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
]
FILLED_PIN = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
]

DISABLED_PIN = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
]

CANVAS_WIDTH = 128
CANVAS_HEIGHT = 64
PIN_SPACING = 4  # Variabler Abstand zwischen den Pins


def draw_pixelart(image, pixelart, x_offset, y_offset):
    draw = ImageDraw.Draw(image)
    for y, row in enumerate(pixelart):
        for x, pixel in enumerate(row):
            if pixel:  # Wenn der Pixel "an" ist (1 oder True)
                draw.point((x_offset + x, y_offset + y), fill=1)

def draw_pin_display(pin_states, active_index):
    # Canvas erstellen mit schwarzem Hintergrund
    image = Image.new("1", (CANVAS_WIDTH, CANVAS_HEIGHT), 0)  # 0 für schwarz
    
    # Parameter für die Pin-Anzeige
    pin_width = 9
    pin_height = 16
    pin_y_offset = CANVAS_HEIGHT - pin_height - 2  # Y-Position am unteren Rand
    
    # Berechnung der Gesamtbreite der Pins inklusive Abstand
    total_pin_width = len(pin_states) * pin_width + (len(pin_states) - 1) * PIN_SPACING
    start_x = (CANVAS_WIDTH - total_pin_width) // 2  # X-Position um die Pins mittig zu platzieren
    
    # Pins zeichnen
    for i, state in enumerate(pin_states):
        pin_x = start_x + i * (pin_width + PIN_SPACING)  # X-Position für jeden Pin
        if i == active_index:
            pin_pixelart = FILLED_PIN
        elif state:
            pin_pixelart = HOLLOW_PIN
        else:
            pin_pixelart = DISABLED_PIN
        
        draw_pixelart(image, pin_pixelart, pin_x, pin_y_offset)
    
    return image

# Beispiel-Pin-Zustände und aktueller Index
# pin_states = [True, False, True, True]
active_index = -1
states = str(input("states: ")).split(",")
pin_states = [True if i == "T" else False for i in states]

while True:
    image = draw_pin_display(pin_states=pin_states, active_index=active_index)
    image.save("out.png")
    # active_index = int(input("active: "))
    active_index = (active_index + 1) % 4 if input(": ") == "n" else active_index
