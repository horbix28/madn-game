import threading
import queue
import time

import neopixel_spi as neopixel
import board
NUM_PIXELS = 144
PIXEL_ORDER = neopixel.GRB

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS,
                               pixel_order=PIXEL_ORDER,
                               auto_write=True, bit0=0b10000000, brightness=0.3)




# pixels = [(0,0,0) for i in range(NUM_PIXELS)]
command_queue = queue.Queue()

import threading
import queue
import time

blinking_threads = {}
command_queue = queue.Queue()


def blink_led(pixels, index, color, blink_delay, blink_count):
    for _ in range(blink_count):
        print("blinking", index, "with color", color)
        pixels[index] = color
        time.sleep(blink_delay/1000)
        pixels[index] = (0,0,0)
        time.sleep(blink_delay/1000)
    blinking_threads.pop(index)

def handle_led_commands():
    while True:
        print(pixels)
        try:
            args  = command_queue.get()
            command, index, color, *_ = args
            print(command, index, color)
            if command is None:  # Shutdown signal
                break
            # elif 0 <= index < NUM_PIXELS:
            #     print("index not valid")
            #     break
            elif command == "set":
                pixels[index] = color
                print(f"Pixel {index} set to {color}")  # Add this line for debugging
            elif command == "blink":
                _,_,_, blink_delay, blink_times = args
                if blinking_threads.get(index):
                    print("!!!!! led", index, "already blinking")
                else:
                    led_blink_thread = threading.Thread(target=blink_led, args=(pixels, index, color,blink_delay,blink_times))
                    led_blink_thread.daemon = True
                    led_blink_thread.start()
                    print(f"Pixel {index} started {color} blinking")  # Add this line for debugging
                    blinking_threads[index] = led_blink_thread
                
        except queue.Empty:
            print("queue empty")
            # Hier kannst du weitere Aktionen ausführen, wenn keine Befehle vorhanden sind
            pass

def set_pixel(index, color):
    command_queue.put(("set", index, color),block=False)
def blink_pixel(index, color, time_off, blink_times):
    command_queue.put(("blink", index, color, time_off, blink_times),block=False)

led_control_thread = threading.Thread(target=handle_led_commands)
led_control_thread.daemon = True
led_control_thread.start()




if __name__ == "__main__":
    # manual test goes here
    # Example usage
    try:
        set_pixel(0, (255, 0, 0))  # Set first pixel to red
        time.sleep(1)
        blink_pixel(10,(200,200,100),500, 20)
        blink_pixel(11,(100,200,50),500, 20)
        blink_pixel(12,(0,200,50),500, 20)
        blink_pixel(15,(230,150,0),250, 21)
        time.sleep(1)
        set_pixel(1, (0, 255, 0))  # Set second pixel to green
        time.sleep(1)
        print(blinking_threads)
        set_pixel(2, (0, 0, 255))  # Set third pixel to blue
        time.sleep(1)
        set_pixel(0, (0, 0, 0))    # Turn off first pixel
        time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        for thread in tuple(blinking_threads.values()): # very ugly way of waiting for all blink threads to finish
            thread.join()
        command_queue.put(None)  # Send shutdown signal to the thread
