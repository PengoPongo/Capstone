#include <Adafruit_GFX.h>
#include <Adafruit_HX8357.h>
#include <SD.h>
#include <SPI.h>

#define TFT_CS 10     // Chip select line for TFT
#define TFT_DC 9      // Data/command line for TFT
#define TFT_RST 8     // Reset line for TFT

Adafruit_HX8357 tft = Adafruit_HX8357(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  Serial.begin(9600);
  tft.begin();
  tft.setRotation(1);
  tft.fillScreen(HX8357_BLACK);

  if (!SD.begin(4)) {  // Change SD card CS pin if needed
    Serial.println("SD card initialization failed!");
    return;
  }
  Serial.println("SD card initialized.");

  // Attempt to display BMP file
  if (displayBMP("/Red.BMP")) {
    Serial.println("BMP displayed successfully.");
  } else {
    Serial.println("Failed to display BMP.");
  }
}

bool displayBMP(const char *filename) {
  File bmpFile = SD.open(filename);
  if (!bmpFile) {
    Serial.println("File not found");
    return false;
  }

  uint8_t bmpHeader[54];
  bmpFile.read(bmpHeader, 54);

  // Extract width and height from the BMP header
  int width = bmpHeader[18] + (bmpHeader[19] << 8);
  int height = bmpHeader[22] + (bmpHeader[23] << 8);

  if (width > tft.width() || height > tft.height()) {
    Serial.println("Image too large for display.");
    bmpFile.close();
    return false;
  }

  tft.setAddrWindow(0, 0, width, height);

  uint16_t rowBuffer[width];
  for (int row = height - 1; row >= 0; row--) {
    bmpFile.seek(54 + row * width * 3);  // Seek to the start of each row
    for (int col = 0; col < width; col++) {
      uint8_t b = bmpFile.read();
      uint8_t g = bmpFile.read();
      uint8_t r = bmpFile.read();
      rowBuffer[col] = tft.color565(r, g, b);
    }
    tft.writePixels(rowBuffer, width);  // Draw the row to the screen
  }

  bmpFile.close();
  return true;
}

void loop() {
  // Nothing to do here
}


