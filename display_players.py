import time
from PIL import Image, ImageDraw

CANVAS_WIDTH=128
CANVAS_HEIGHT=64


def draw_player_status(filled_circle_player=None, square_player=None):
    # Canvas erstellen mit schwarzem Hintergrund
    image = Image.new("1", (CANVAS_WIDTH, CANVAS_HEIGHT), 0)  # 0 für schwarz
    draw = ImageDraw.Draw(image)

    # Parameter für die Statusanzeige
    player_count = 4
    circle_radius = 6
    circle_spacing = 28  # Abstand zwischen den Kreisen
    circle_y = 8  # y-Position der Kreise
    square_padding = 2  # Abstand des Quadrats vom Kreis

    # Kreise und Quadrat zeichnen
    for i in range(player_count):
        # Mittelpunkt des Kreises berechnen
        circle_x = (CANVAS_WIDTH // (player_count + 1)) * (i + 1)
        
        # Kreise zeichnen
        if i == filled_circle_player:
            draw.ellipse((circle_x - circle_radius, circle_y - circle_radius,
                          circle_x + circle_radius, circle_y + circle_radius), fill=1)
        else:
            draw.ellipse((circle_x - circle_radius, circle_y - circle_radius,
                          circle_x + circle_radius, circle_y + circle_radius), outline=1)
        
        # Quadrat um den aktiven Spieler zeichnen
        if i == square_player:
            draw.rectangle((circle_x - circle_radius - square_padding, circle_y - circle_radius - square_padding,
                            circle_x + circle_radius + square_padding, circle_y + circle_radius + square_padding), outline=1)
    
    return image
# Beispielaufruf der Funktion und Bild anzeigen
image = draw_player_status(filled_circle_player=0, square_player=0)
image.save("out.png")
time.sleep(1)
image = draw_player_status(filled_circle_player=0, square_player=1)
image.save("out.png")
time.sleep(1)
image = draw_player_status(filled_circle_player=0, square_player=2)
image.save("out.png")
time.sleep(1)
image = draw_player_status(filled_circle_player=0, square_player=3)
image.save("out.png")

