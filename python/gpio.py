// Blink the LED off and on
import machine
import time

g = machine.Pin(2, machine.Pin.OUT)

while True:
    g.value(0)
    time.sleep(1)
    g.value(1)
    time.sleep(1)
