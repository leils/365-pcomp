# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board
import digitalio
import neopixel

YELLOW = (255, 150, 0)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

# Enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# Make the 2 input buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

# The two files assigned to buttons A & B
audiofiles = ["hny.wav"]

def pixels_on():
    pixels.fill(YELLOW)
    pixels.show()

def pixels_off():
    pixels.fill(OFF)
    pixels.show()

def pixel_animation():
    wait_delay = .5
    for i in range(10):
        pixels.fill(OFF)        
        pixels[i] = YELLOW
        time.sleep(wait_delay)
        pixels.show()

def play_file(filename):
    pixels_on()
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                pixel_animation()
                pass
    print("Finished")
    pixels_off()


while True:
    if buttonA.value:
        play_file(audiofiles[0])
    if buttonB.value:
        play_file(audiofiles[0])
