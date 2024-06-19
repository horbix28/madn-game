import neopixel_spi as neopixel
import board
from board_renderer import render_board
NUM_PIXELS = 144
PIXEL_ORDER = neopixel.GRB

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS,
                               pixel_order=PIXEL_ORDER,
                               auto_write=True, bit0=0b10000000, brightness=0.01)

EMPTY_COLOR = (255,255,255)


def generate_leds(game_positions):
    fields = {index: EMPTY_COLOR for index in range(40)}
    figures_on_b_fields = {key: 0 for key in game_positions.keys()}
    for player in game_positions:
        # term_reset = Fore.RESET
        for field_id in game_positions[player]:
            if field_id == -1:
                figures_on_b_fields[player] += 1
            else:
                fields[field_id] = player.rgb
    for player in game_positions:
        figs = []
        if figures_on_b_fields.get(player):
            for _ in range(figures_on_b_fields.get(player,0)):
                # print(player, "appending")
                figs.append(player.rgb)
        while len(figs) < 4:
                figs.append(EMPTY_COLOR)
        # print(player.name, figs)
        for fig in figs:
            index = len(fields)
            fields[index] = fig
    for index, value in enumerate(fields.values()):
        # print(value)
        pixels[index] = value
    # print(list(fields.values()))

if __name__ == "__main__":
    from main import Color
    from colorama import Fore
    game_positions = {
        Color("red",(255,0,0), Fore.RED): [-1, 39, 16, -1],
        Color("blue", (0,0,255), Fore.BLUE): [-1, -1, 4, -1],
        Color("yellow", (255,255,0), Fore.YELLOW): [17, -1, 7, 11],
        Color("green", (0,255,0), Fore.GREEN): [-1,-1,-1,-1]
    }
    render_board(game_positions)
    generate_leds(game_positions)

