# adapted from Arduino's Capacitive Touch and Neopixel examples 
# senses capacitive touch and lights the LEDs in a circle

import time
import board
import touchio
import neopixel

# Color list 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

touchIns = [touchio.TouchIn(pin) for pin in
            (board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.A7)]

LIGHT_DURATION = .1

# Setup 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

# How long we want the LED to stay on
BLINK_ON_DURATION = 0.5

# How long we want the LED to stay off
BLINK_OFF_DURATION = 0.25

# When we last changed the LED state
LAST_BLINK_TIME = -1

CURRENT_COLOR = BLUE
led_is_on = False

def turn_on(c):
    pixels.fill(c)
    pixels.show()

def turn_off(): 
    pixels.fill(OFF)
    pixels.show()

def handle_cap():
    global CURRENT_COLOR
    for i, touchIn in enumerate(touchIns):
        if touchIn.value:
            print('A%d touched' % (i + 1)) 
            CURRENT_COLOR = colors[i]

while True: 
    handle_cap()
    now = time.monotonic()
    if led_is_on: 
        if now >= LAST_BLINK_TIME + BLINK_ON_DURATION: 
            turn_off()
            led_is_on = not led_is_on
            LAST_BLINK_TIME = now
    if not led_is_on:
        if now >= LAST_BLINK_TIME + BLINK_OFF_DURATION:
            turn_on(CURRENT_COLOR)
            led_is_on = not led_is_on
            LAST_BLINK_TIME = now




