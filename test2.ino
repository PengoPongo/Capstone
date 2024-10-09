#include <SPI.h>
#include "Adafruit_GFX.h"
#include "Adafruit_HX8357.h"

// Pin definitions for the display
#define TFT_CS 10
#define TFT_DC 9
#define TFT_RST 8 // Can be set to -1 if tied to Arduino's reset

// Pin definitions for the buttons
const int buttonPin1 = 2;
const int buttonPin2 = 3;  
const int buttonPin3 = 4;

// variables will change:
int buttonState1 = 0;  // variable for reading the pushbutton status
int buttonState2 = 0;
int buttonState3 = 0;

// Create an instance of the display
Adafruit_HX8357 tft = Adafruit_HX8357(TFT_CS, TFT_DC, TFT_RST);

// Variable to store the current state (0: Home, 1: Image, 2: Timer)
int currentState = 0;

void setup() {
  Serial.begin(9600);
  
  // Initialize the display
  tft.begin();
  
  // Set the screen rotation (optional, can be adjusted)
  tft.setRotation(0);
  
  // Clear the screen
  tft.fillScreen(HX8357_WHITE);
  
  // Set button pins as input
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  
  // Display the initial state (Home)
  displayCurrentState();
}

void loop() {

  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);

  // Check if button 1 is pressed (for Home)
  if (buttonState1 == HIGH) {
    currentState = 0;  // Set state to 0 (Home)
    displayCurrentState();
    delay(300); // Debounce delay
  }

  // Check if button 2 is pressed (for Image)
  if (buttonState2 == HIGH) {
    currentState = 1;  // Set state to 1 (Image)
    displayCurrentState();
    delay(300); // Debounce delay
  }

  // Check if button 3 is pressed (for Timer)
  if (buttonState3 == HIGH) {
    currentState = 2;  // Set state to 2 (Timer)
    displayCurrentState();
    delay(300); // Debounce delay
  }
}

void displayCurrentState() {
  // Determine which screen to display based on the current state
  switch (currentState) {
    case 0:
      displayScreen("Home");
      break;
    case 1:
      displayScreen("Image Selection");
      break;
    case 2:
      displayScreen("Timer");
      break;
  }
}

void displayScreen(const char* title) {
  // Clear the screen to white
  tft.fillScreen(HX8357_WHITE);
  
  // Draw the grey bar at the top
  tft.fillRect(0, 0, tft.width(), 50, 0xd69a);  // Grey bar 50px high
  
  // Set text color and size
  tft.setTextColor(HX8357_BLACK);
  tft.setTextSize(3); // Adjust size for the title
  
  // Calculate the position to center the title text within the grey bar
  int16_t x1, y1;
  uint16_t w, h;
  tft.getTextBounds(title, 0, 0, &x1, &y1, &w, &h);
  int16_t x = (tft.width() - w) / 2;
  int16_t y = (50 - h) / 2; // Center within the grey bar (50px height)
  
  // Set the cursor position to the calculated coordinates
  tft.setCursor(x, y);
  
  // Print the title ("Home", "Image", or "Timer")
  tft.println(title);
}
