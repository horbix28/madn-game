import asyncio
import neopixel_spi as neopixel
import board

NUM_PIXELS = 144
PIXEL_ORDER = neopixel.GRB
spi = board.SPI()
pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=True, bit0=0b10000000, brightness=0.3)

async def blink_led(pixels, index, color, blink_delay, blink_count):
    for _ in range(blink_count):
        print("blinking", index, "with color", color)
        pixels[index] = color
        await asyncio.sleep(blink_delay / 1000)
        pixels[index] = (0, 0, 0)
        await asyncio.sleep(blink_delay / 1000)

async def handle_led_commands(command_queue):
    while True:
        command_data = await command_queue.get()
        if command_data is None:  # Shutdown signal
            break

        command, index, color, *args = command_data
        print(f"Handling command: {command} for index {index} with color {color}")

        if command == "set":
            pixels[index] = color
            print(f"Pixel {index} set to {color}")
        elif command == "blink":
            blink_delay, blink_times = args
            await blink_led(pixels, index, color, blink_delay, blink_times)

def set_pixel(command_queue, index, color):
    command_queue.put_nowait(("set", index, color))

def blink_pixel(command_queue, index, color, blink_delay, blink_times):
    command_queue.put_nowait(("blink", index, color, blink_delay, blink_times))

async def main():
    command_queue = asyncio.Queue()
    led_task = asyncio.create_task(handle_led_commands(command_queue))
    
    try:
        set_pixel(command_queue, 0, (255, 0, 0))
        await asyncio.sleep(1)
        blink_pixel(command_queue, 10, (200, 200, 100), 500, 20)
        await asyncio.sleep(1)
        set_pixel(command_queue, 1, (0, 255, 0))
        await asyncio.sleep(1)
        set_pixel(command_queue, 2, (0, 0, 255))
        await asyncio.sleep(1)
        set_pixel(command_queue, 0, (0, 0, 0))
        await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        command_queue.put_nowait(None)  # Send shutdown signal to the coroutine
        await led_task  # Ensure the task exits cleanly

if __name__ == "__main__":
    asyncio.run(main())
