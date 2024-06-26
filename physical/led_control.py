import asyncio
import board
import neopixel_spi as neopixel

NUM_PIXELS = 144
PIXEL_ORDER = neopixel.GRB

spi = board.SPI()
pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=True, bit0=0b10000000, brightness=0.3)
blink_tasks = {}

# Funktion zum Setzen einer LED auf eine statische Farbe
def set_static_color(index, color):
    pixels[index] = color


# Asynchrone Blinkfunktion
async def blink_led(index, color, blink_duration, sleep_duration):
    while True:
        pixels[index] = color
        await asyncio.sleep(blink_duration)
        pixels[index] = (0, 0, 0)
        await asyncio.sleep(sleep_duration)

# Funktion zum Starten des Blinkens
def start_blinking(index, color, blink_duration, sleep_duration):
    if index in blink_tasks:
        stop_blinking(index)
    task = asyncio.create_task(blink_led(index, color, blink_duration, sleep_duration))
    blink_tasks[index] = task
    return task

# Funktion zum Stoppen des Blinkens
def stop_blinking(index):
    if index in blink_tasks:
        blink_tasks[index].cancel()
        del blink_tasks[index]
        # Setze die LED nach dem Stoppen auf Schwarz
        pixels[index] = (0, 0, 0)

async def main():
    set_static_color(5, (255, 0, 0))  # LED bei Index 5 auf Rot setzen
    start_blinking(10, (0, 255, 0), 0.5, 0.5)  # LED bei Index 10 blinkt Grün
    start_blinking(9, (255, 255, 0), 0.5, 0.5)  # LED bei Index 10 blinkt Grün
    start_blinking(8, (0, 255, 255), 0.5, 0.5)  # LED bei Index 10 blinkt Grün
    j=121-1
    for i in range(15,120):
        j-=1 
        start_blinking(i, (j, 30, i), 0.5, 0.5)  # LED bei Index 10 blinkt Grün

    # Lassen Sie das Programm laufen, während das Blinken aktiv ist
    try:
        await asyncio.sleep(5)  # Laufzeitdauer für das Blinken
        stop_blinking(10)
        await asyncio.sleep(2)  # Laufzeitdauer für das Blinken
        stop_blinking(9)
        await asyncio.sleep(2)  # Laufzeitdauer für das Blinken
    finally:
        for led_id in tuple(blink_tasks.keys()):
            stop_blinking(led_id)
        await asyncio.gather(*blink_tasks.values(), return_exceptions=True)

# Starten des Event-Loops
if __name__ == "__main__":
    asyncio.run(main())