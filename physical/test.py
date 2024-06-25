from led_control import set_pixel, led_control_thread, command_queue

set_pixel("set", 0, (255, 0, 0))  # Set first pixel to red
set_pixel("set", 3, (255,255,0))
command_queue.put(None)
led_control_thread.join()