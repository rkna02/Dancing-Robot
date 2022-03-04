# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# extra libraries needed:
# - adafruit_74hc595
import time
import board
import digitalio
import adafruit_74hc595
import adafruit_matrixkeypad

latch_pin = digitalio.DigitalInOut(board.D5) #change to another pin if D5 is not working
sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

# Create the pin objects in a list
pins = [sr.get_pin(n) for n in range(1,8)] 
 
# Membrane 3x4 matrix keypad - https://www.adafruit.com/product/419
cols = [digitalio.DigitalInOut(x) for x in (pins[0], pins[1], pins[2])]
rows = [digitalio.DigitalInOut(x) for x in (pins[3], pins[4], pins[5], pins[6])]

# 3x4 matrix keypad - Rows and columns are mixed up for https://www.adafruit.com/product/3845
# Use the same wiring as in the guide with the following setup lines:
# cols = [digitalio.DigitalInOut(x) for x in (board.D11, board.D13, board.D9)]
# rows = [digitalio.DigitalInOut(x) for x in (board.D12, board.D5, board.D6, board.D10)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

options = {1: move1,
           2: move2,
           3: move3,
           4: move4 
        }
while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        if (keys == 1):
            move1 = True
            break
        elif (keys == 2):
            move2 = True
            break
        elif (keys == 3):
            move3 = True
            break 
        elif (keys == 4):
            move4 = True
            break 
        else: 
            resetto90()
            break
    time.sleep(0.1)
