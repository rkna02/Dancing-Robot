# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import digitalio
import board
import adafruit_matrixkeypad

# Membrane 3x4 matrix keypad - https://www.adafruit.com/product/419
cols = [digitalio.DigitalInOut(x) for x in (board.A5, board.D1, board.D2)]
rows = [digitalio.DigitalInOut(x) for x in (board.D3, board.A2, board.A3, board.A4)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys == [1]:
        time.sleep(0.5)
        while True:
            pressed_keys = keypad.pressed_keys
            if pressed_keys == [1]:  # press 1 then 1 to show all dance move
                move1 = True;
            elif pressed_keys == [2]:  # press 1 then 1 to show dance move 1
                move2 = True;
            elif pressed_keys == [3]:  # press 1 then 1 to show dance move 2
                move3 = True;
            elif keys == [4]:  # press 1 then 1 to show dance move 3
                move4 = True;
            elif pressed_keys == [5]:  # press 1 then 1 to show dance move 3
                move5 = True;
            elif pressed_keys == [6]:  # press 1 then 1 to show dance move 3
                move6 = True;
        time.sleep(1)
        
    elif keys == [2]:
        time.sleep(0.5)
        while True:
            keys = keypad.pressed_keys
            if pressed_keys = [1]:  # press 1 to start showing all dance moves
                move1 = True;
                move2 = True;
                move3 = True;
                move4 = True;
                move5 = True;
                move6 = True;
        time.sleep(1)
        
    elif (keys == [3] or keys == [4] or keys == [5] or keys == [6] or keys == [7] or keys == [8] or keys == [9]):
        # show error message if pressed
    time.sleep(1)
