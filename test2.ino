#include <SPI.h>
#include "Adafruit_GFX.h"
#include "Adafruit_HX8357.h"

// Pin definitions
#define TFT_CS 10
#define TFT_DC 9
#define TFT_RST 8 // Can be set to -1 if tied to Arduino's reset

// Create an instance of the display
Adafruit_HX8357 tft = Adafruit_HX8357(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  Serial.begin(9600);
  
  // Initialize the display
  tft.begin();
  
  // Set the screen rotation (optional, can be adjusted)
  tft.setRotation(1);
  
  // Clear the screen
  tft.fillScreen(HX8357_BLACK);
}

void loop() {
  // Show each name on the screen in large text
  displayName("Davin", HX8357_RED, HX8357_BLACK);
  delay(2000); // Wait for 2 second
  
  displayName("Phat", HX8357_WHITE, HX8357_BLACK);
  delay(2000); // Wait for 2 second
  
  displayName("Kendrys", HX8357_BLUE, HX8357_BLACK);
  delay(2000); // Wait for 2 second
}

void displayName(const char* name, uint16_t textColor, uint16_t backgroundColor) {
  // Clear the screen
  tft.fillScreen(backgroundColor);
  
  // Set text color and size
  tft.setTextColor(textColor);
  tft.setTextSize(5); // text size
  
  // Calculate the position to center the text
  int16_t x1, y1;
  uint16_t w, h;
  tft.getTextBounds(name, 0, 0, &x1, &y1, &w, &h);
  int16_t x = (tft.width() - w) / 2;
  int16_t y = (tft.height() - h) / 2;
  
  // Set the cursor position to the calculated coordinates
  tft.setCursor(x, y);
  
  // Print the name
  tft.println(name);
}
