# Visual Timer with Custom Image

Welcome to the Kin\:pathic Visual Timer! This guide provides step-by-step instructions for setting up, navigating, and using your visual timer to manage time effectively with custom images.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware Specifications](#hardware-specifications)
- [Software Specifications](#software-specifications)
- [How to Run the Program](#how-to-run-the-program)
- [License](#license)

## Overview

The Kin\:pathic Visual Timer is designed to assist in time management by displaying a calming, custom image of your choice during countdowns. It is especially useful for educational environments and individuals with unique learning needs. The project is part of a capstone initiative, emphasizing usability and accessibility.

![My Picture](Capstone/my-Timer_image.jpeg)

For Full [User Manual](https://docs.google.com/document/d/1zKiSkMkynA15LEDlfgi2N6uZ_dLe_kZWn2Y_cHhkKe0/edit?usp=sharing) click here.

## Features

- **Customizable Display:** Supports images to visually represent tasks.
- **Multiple Countdown Options:** Adjustable timer durations ranging from 5 to 60 minutes.
- **Audible Alerts:** A beep sound plays when the timer reaches zero.
- **User-Friendly Interface:** Buttons for setting images, adjusting countdown duration, starting/stopping, and resetting the timer.
- **Compact Design:** Powered by rechargeable batteries for portability.

## Hardware Specifications

- **Power Supply:** Rechargeable batteries
- **Display:** The 7” touchscreen display for Raspberry Pi with a resolution of 800 x 480 pixels and multi-touch functionality.
  - **Active Area:** 154.08mm x 85.92mm
  - **Touch Panel:** True multi-touch capacitive touch panel with up to 10 points of touch.
  - **Connection:** Ribbon cable to the DSI port and GPIO for power.
- **Processor:** Raspberry Pi 3B+ for processing and control

## Software Specifications

- **Programming Language:** Python
- **Libraries Used:** Pygame for graphics, interaction and Gpiozero  for setting up pins on Rpi (to speaker for beeping)
- **Timer Logic:** Managed by the Raspberry Pi to ensure precision
- **Modes:** Includes home screen, image selection, and timer countdown modes

## How to Run the Program

1. **Clone the Repository:**

   - Open your terminal or command prompt.
   - Run the command: `git clone <repository_url>`.

2. **Download Required Folders:**

   - Download the `UI` folder (contains button and interface images).
   - Download the `Image` folder (contains default images).
   - Ensure both folders are placed inside the `Capstone` directory.

3. **Navigate to the Directory:**

   - Use `cd Capstone` to move into the project directory.

4. **Install Dependencies:**

   - Ensure Python 3 is installed on your system.
   - Install the required Python libraries using `pip install -r requirements.txt`.
   - Libraries to download: pygame and gpiozero. 

   **Run the Program:**

   - Execute the main script using: `python3 Screen_Codev3.py`.

5. **Follow Navigation Instructions:**

   - Use the program's interface to select images and set timers as described in the features section.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

