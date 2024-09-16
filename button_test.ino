/*
  Button

  Turns on and off a light emitting diode(LED) connected to digital pin 13,
  when pressing a pushbutton attached to pin 2.

  The circuit:
  - LED attached from pin 13 to ground through 220 ohm resistor
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.

  created 2005
  by DojoDave <http://www.0j0.org>
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Button
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin1 = 6;  // the number of the pushbutton pin
const int buttonPin2 = 7;  
const int buttonPin3 = 8;
const int buttonPin4 = 9;
const int buttonPin5 = 10;

// variables will change:
int buttonState1 = 0;  // variable for reading the pushbutton status
int buttonState2 = 0;
int buttonState3 = 0;
int buttonState4 = 0;
int buttonState5 = 0;
int buttonPinPressed = 0;

void setup() {
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(LED_BUILTIN, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  buttonState4 = digitalRead(buttonPin4);
  buttonState5 = digitalRead(buttonPin5);

 // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
 if (buttonState1 == HIGH) {
    // turn LED on:
    digitalWrite(LED_BUILTIN, HIGH);
    buttonPinPressed = 1;
  }
  if (buttonState2 == HIGH) {
    // turn LED on:
    digitalWrite(LED_BUILTIN, HIGH);
    buttonPinPressed = 2;
  } 
  if (buttonState3 == HIGH) {
    // turn LED on:
    digitalWrite(LED_BUILTIN, HIGH);
    buttonPinPressed = 3;
  } 
  if (buttonState4 == HIGH) {
    // turn LED on:
    digitalWrite(LED_BUILTIN, HIGH);
    buttonPinPressed = 4;
  } 
  if (buttonState5 == HIGH) {
    // turn LED on:
    digitalWrite(LED_BUILTIN, HIGH);
    buttonPinPressed = 5;
  } 
  else {
    // turn LED off:
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print("no button is pressed \n");
  }

switch (buttonPinPressed){
  case 1:
  Serial.print("button 1 is pressed \n");
    break;

  case 2:
  Serial.print("button 2 is pressed \n");
    break;

  case 3:
  Serial.print("button 3 is pressed \n");
    break;
  
  case 4:
  Serial.print("button 4 is pressed \n");
    break;

  case 5:
  Serial.print("button 5 is pressed \n");
    break;
}
}




