# Arduino DHT11 Temperature and Humidity Monitor

## Overview

This project integrates an Arduino microcontroller with a DHT11 sensor to monitor temperature and humidity levels. The Arduino collects data from the DHT11 sensor and sends it to a computer via a serial port. A Python script runs on the computer, which acts as a Telegram bot, allowing users to request real-time sensor data through chat commands.

## Features

- Real-time monitoring of temperature and humidity.
- Easy integration with Telegram for remote access to sensor data.
- Simple command interface to request updates from the bot.

## Hardware Required

- Arduino board (e.g., Arduino Uno, Nano, or Leonardo)
- DHT11 temperature and humidity sensor
- Jumper wires
- Breadboard (optional)

## Software Required

- Arduino IDE for uploading the Arduino code.
- Python (version 3.6 or higher)
- Python libraries:
  - `pyserial` for serial communication
  - `python-telegram-bot` for creating the Telegram bot

## Installation

1. **Arduino Setup:**
   - Connect the DHT11 sensor to the Arduino according to the wiring diagram.
   - Upload the Arduino code located in the `arduino` directory to your Arduino board using the Arduino IDE.

2. **Python Setup:**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/pattt-coding/Humidity-And-Temperature-From-Arduino-TelegramBOT.git
     cd Humidity-And-Temperature-From-Arduino-TelegramBOT
     ```
   - Install the required Python libraries:
     ```bash
     pip install pyserial python-telegram-bot
     ```
   - Update the Python script with your Telegram bot token and the correct COM port where the Arduino is connected.

## Usage

- Start the Python script to run the Telegram bot:
  ```bash
  python arduinohumidity.py
