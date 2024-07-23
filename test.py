from PIL import Image, ImageDraw, ImageFont

CANVAS_WIDTH = 128
CANVAS_HEIGHT = 64

def draw_player_status(letters=None, underline_player=None):
    # Canvas erstellen mit schwarzem Hintergrund
    image = Image.new("1", (CANVAS_WIDTH, CANVAS_HEIGHT), 0)  # 0 für schwarz
    draw = ImageDraw.Draw(image)
    
    # Parameter für die Statusanzeige
    player_count = len(letters) if letters else 0
    circle_radius = 6
    circle_y = 8  # y-Position der Kreise
    circle_x_start = CANVAS_WIDTH // (player_count + 1)  # Startposition der ersten Kreis
    
    # Schriftart für Buchstaben
    font = ImageFont.load_default()  # Standard-Schriftart

    # Kreise und Unterstriche zeichnen
    for i in range(player_count):
        # Mittelpunkt des Kreises berechnen
        circle_x = circle_x_start * (i + 1)
        
        # Kreis zeichnen
        draw.ellipse((circle_x - circle_radius, circle_y - circle_radius,
                      circle_x + circle_radius, circle_y + circle_radius), outline=1)
        
        # Buchstaben in den Kreisen schreiben
        if letters:
            text = letters[i]
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            # Buchstaben um 1 Pixel nach oben verschieben
            draw.text((circle_x - text_width // 2, circle_y - text_height // 2 - 1), text, fill=1, font=font)

        # Unterstreichen des Kreises für den aktiven Spieler
        if i == underline_player:
            # Unterstrich 1 Pixel unterhalb der unteren Kante des Kreises
            draw.line((circle_x - circle_radius, circle_y + circle_radius + 2,
                       circle_x + circle_radius, circle_y + circle_radius + 2), fill=1)

    return image


# Beispielnutzung
letters = ['R', 'G', 'B','Y']
image = draw_player_status(letters=letters, underline_player=2)
image.save("out.png")