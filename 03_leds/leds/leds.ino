#include <Adafruit_CircuitPlayground.h>
// Turns LEDs on with right button. off with left. 

void setup() {
  CircuitPlayground.begin();
  CircuitPlayground.clearPixels();
}

void loop() {
  if (CircuitPlayground.leftButton()) {
    ledsOn();
  } else if (CircuitPlayground.rightButton()) {
    ledsOff();
  }
  delay(10);
}

void ledsOn() {
  CircuitPlayground.setPixelColor(0, 255,   0,   0);
  CircuitPlayground.setPixelColor(1, 128, 128,   0);
  CircuitPlayground.setPixelColor(2,   0, 255,   0);
  CircuitPlayground.setPixelColor(3,   0, 128, 128);
  CircuitPlayground.setPixelColor(4,   0,   0, 255);

  CircuitPlayground.setPixelColor(5, 0xFF0000);
  CircuitPlayground.setPixelColor(6, 0x808000);
  CircuitPlayground.setPixelColor(7, 0x00FF00);
  CircuitPlayground.setPixelColor(8, 0x008080);
  CircuitPlayground.setPixelColor(9, 0x0000FF);
}

void ledsOff() {
  CircuitPlayground.clearPixels();
  delay(100);
}
