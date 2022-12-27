# adapted from Arduino's Capacitive Touch and Neopixel examples 
# senses capacitive touch and lights the LEDs in a circle

import time
import board
import touchio
import neopixel

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

touchIns = [touchio.TouchIn(pin) for pin in
            (board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.A7)]
lastTouch = touchIns

colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

def handleTouch():
    for i, touchIn in enumerate(touchIns):
        if touchIn.value:
            print('A%d touched' % (i + 1)) 
            flashLEDs(colors[i])

def flashLEDs(color):
    print("trying to flash LEDs")
    pixels.fill(color)
    pixels.show()
    time.sleep(0.25)
    pixels.fill(OFF)
    pixels.show()


while True:
    handleTouch()
    time.sleep(0.1)


