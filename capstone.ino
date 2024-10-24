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
  tft.setRotation(2);

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
      displayHomeScreen();
      break;
    case 1:
      displayImageSelectionScreen();
      break;
    case 2:
      displayTimerScreen();
      break;
  }
}

// Function for the home screen
void displayHomeScreen() {
  tft.fillScreen(HX8357_WHITE);

  // Draw green bar and text at the top
  displayTitle("Home");

  // Define the sizes and positions for the boxes
  int boxWidth = 100;
  int boxHeight = 100;
  int gap = 60; // Gap for text between the boxes
  int boxX = (tft.width() - boxWidth) / 2;
  int boxY = 80;
  int shadowOffset = 7; // Offset for shadow

  // --- First Box (upper) with shadow and thicker outline ---
  // Draw shadow (slightly offset version of the box)
  tft.fillRoundRect(boxX + shadowOffset, boxY + shadowOffset, boxWidth, boxHeight, 15, tft.color565(0xc9, 0xc9, 0xc9));

  // Draw filled green box
  tft.fillRoundRect(boxX, boxY, boxWidth, boxHeight, 15, tft.color565(0x36, 0xD6, 0x36));

  // Draw thicker black outline around the first box by drawing multiple outlines
  for (int i = 0; i < 3; i++) {
    tft.drawRoundRect(boxX - i, boxY - i, boxWidth + 2 * i, boxHeight + 2 * i, 15 + i, HX8357_BLACK);
  }

  // --- Second Box (lower) with shadow and thicker outline ---
  // Calculate Y position for the second box
  int clockBoxY = boxY + boxHeight + gap + 10;

  // Draw shadow (slightly offset version of the box)
  tft.fillRoundRect(boxX + shadowOffset, clockBoxY + shadowOffset, boxWidth, boxHeight, 15, tft.color565(0xc9, 0xc9, 0xc9));

  // Draw filled blue box
  tft.fillRoundRect(boxX, clockBoxY, boxWidth, boxHeight, 15, tft.color565(0x5B, 0x5B, 0xFF));

  // Draw thicker black outline around the second box by drawing multiple outlines
  for (int i = 0; i < 3; i++) {
    tft.drawRoundRect(boxX - i, clockBoxY - i, boxWidth + 2 * i, boxHeight + 2 * i, 15 + i, HX8357_BLACK);
  }

  // Draw a small circle in the center of the first box
  int circleRadius = 15;  // Adjust size of the circle
  int circleX = boxX + boxWidth / 2;
  int circleY = boxY + boxHeight / 2;
  tft.drawCircle(circleX, circleY, circleRadius, HX8357_BLACK);

  // Draw a rectangle around the circle, extended along the x-axis
  int rectPaddingX = 25;
  int rectPaddingY = 10;
  tft.drawRect(circleX - circleRadius - rectPaddingX, circleY - circleRadius - rectPaddingY,
               2 * (circleRadius + rectPaddingX), 2 * (circleRadius + rectPaddingY), HX8357_BLACK);

  // Draw a small square above the rectangle in the top-left corner
  int squareSize = 10;
  tft.fillRect(circleX - circleRadius - rectPaddingX, circleY - circleRadius - rectPaddingY - squareSize, squareSize + 8, squareSize, HX8357_BLACK);

  // Draw a large circle in the second box
  int largeCircleRadius = boxWidth / 2 - 10;
  int largeCircleX = boxX + boxWidth / 2;
  int largeCircleY = clockBoxY + boxHeight / 2;
  for (int i = 0; i < 3; i++) {
    tft.drawCircle(largeCircleX, largeCircleY, largeCircleRadius + i, HX8357_BLACK);
  }

  // Draw a thick right angle in the center of the circle
  int angleLength = largeCircleRadius / 2;
  tft.fillRect(largeCircleX, largeCircleY, angleLength, 3, HX8357_BLACK);  // Horizontal line
  tft.fillRect(largeCircleX, largeCircleY - angleLength, 3, angleLength, HX8357_BLACK);  // Vertical line

  // Display text between the two boxes
  tft.setTextSize(2);
  tft.setCursor(70, boxY + boxHeight + 10);  // Text between boxes
  tft.println("Image Selection");

  // Text below the second box
  tft.setCursor(70, clockBoxY + boxHeight + 20);
  tft.println("Timer Countdown");
}

// Function for the image selection screen
void displayImageSelectionScreen() {
  tft.fillScreen(HX8357_WHITE);

  // Draw green bar and text at the top
  displayTitle("Image Selection");

  // Draw the largest possible hollow circle in the center of the screen
  int radius = min(tft.width(), tft.height()) / 2 - 10;
  for (int i = 0; i < 3; i++) {
    tft.drawCircle(tft.width() / 2, tft.height() / 2 + 20, radius + i, HX8357_BLACK); 
  }

  // Display text above the circle
  tft.setTextSize(2);
  tft.setCursor(30, tft.height() / 2 - radius - 20);
  tft.println("Displayed is your image");
}

//Displays the Timer Screen
void displayTimerScreen() {
  tft.fillScreen(HX8357_WHITE);

  // Draw blue bar and text at the top
  displayTitle("Timer");

  // Draw the filled blue circle in the center of the screen
  int radius = min(tft.width(), tft.height()) / 2 - 10;  // Reduced padding for larger size
  tft.fillCircle(tft.width() / 2, tft.height() / 2 + 20, radius, tft.color565(0x5B, 0x5B, 0xFF));

  // Draw black outline around the circle
  for (int i = 0; i <= 3; i++) {  // Adjust the loop to make the outline thicker (increase 'i' for more thickness)
    tft.drawCircle(tft.width() / 2, tft.height() / 2 + 20, radius + i, HX8357_BLACK);
  }

  // Draw the reversed spokes (lines starting near the edge and going inward)
  int centerX = tft.width() / 2;
  int centerY = tft.height() / 2 + 20;
  int numSpokes = 24;  // Number of spokes
  for (int i = 0; i < numSpokes; i++) {
    // Calculate angle for each spoke
    float angle = 2 * PI * i / numSpokes;

    // Choose spoke length factor based on whether the index is odd or even
    float spokeLengthFactor = (i % 2 == 0) ? 0.9 : 0.8;

    // Calculate x and y coordinates for the start of each spoke (near the edge)
    int xStart = centerX + radius * cos(angle);
    int yStart = centerY + radius * sin(angle);

    // Calculate x and y coordinates for the end of each spoke (closer to the center)
    int xEnd = centerX + radius * spokeLengthFactor * cos(angle);
    int yEnd = centerY + radius * spokeLengthFactor * sin(angle);

    // Draw the thicker reversed spoke (from outer to inner) by drawing multiple parallel lines
    for (int thickness = -1; thickness <= 1; thickness++) {
      tft.drawLine(xStart + thickness * cos(angle + PI / 2), yStart + thickness * sin(angle + PI / 2),
                   xEnd + thickness * cos(angle + PI / 2), yEnd + thickness * sin(angle + PI / 2), HX8357_BLACK);

    // Display text above the circle (Reset button)
    tft.setTextSize(2);
    tft.setCursor(30, tft.height() / 2 - radius - 20);
    tft.println("Time Set to __ minutes");
    }
  }
}

// Helper function to display a title at the top of the screen with shadow and different bar colors
void displayTitle(const char* title) {

  // Define bar height and shadow offset
  int barHeight = 40;
  int shadowOffset = 3; // Offset for shadow
  
  // Set the color for each screen based on the title
  uint16_t barColor;
  if (strcmp(title, "Home") == 0) {
    barColor = tft.color565(0xD1, 0x2A, 0x2A);  // Red for Home
  } else if (strcmp(title, "Image Selection") == 0) {
    barColor = tft.color565(0x36, 0xD6, 0x36);  // Green for Image Selection
  } else if (strcmp(title, "Timer") == 0) {
    barColor = tft.color565(0x5B, 0x5B, 0xFF);  // Blue for Timer
  } else {
    barColor = HX8357_BLACK;  // Default color if title doesn't match any known screen
  }

  // Draw the shadow (slightly offset version of the bar)
  tft.fillRect(0 + shadowOffset, 0 + shadowOffset, tft.width(), barHeight, tft.color565(0xc9, 0xc9, 0xc9));  // Light grey shadow
  
  // Draw the main colored bar (original position)
  tft.fillRect(0, 0, tft.width(), barHeight, barColor);  // Colored bar depending on the screen

  // Set the text color and size
  tft.setTextColor(HX8357_BLACK);
  tft.setTextSize(3);

  // Calculate the width of the title text to center it
  int16_t x1, y1;
  uint16_t w, h;
  tft.getTextBounds(title, 0, 0, &x1, &y1, &w, &h);

  // Display the title text centered at the top
  tft.setCursor((tft.width() - w) / 2, 10);
  tft.println(title);
}

