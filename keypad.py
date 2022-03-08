import time
import board
import pwmio
import pulseio
import simpleio
from adafruit_motor import servo

import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

import os
import adafruit_imageload

import digitalio
import adafruit_matrixkeypad

import buzzer


# display set up and initialization
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D13
tft_dc = board.D7

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D0)
display = ST7735R(display_bus, width=128, height=128, rotation=90)

splash = displayio.Group()  # main display group
display.show(splash)

main_menu = displayio.Group()
sub_menu1 = displayio.Group()
sub_menu2 = displayio.Group()
error = displayio.Group()

""" 
    Displays the main menu of the robot with bitmaps and texts
    Prompts user for a key from 1-2 and performs their corresponding actions
    If other keys are pressed, display will show an error
    1 - navigates user to a new page where the user can choose individual dance moves to perform
    2 - click to immediately perform all dance moves at once 
"""


def main_menu_display():
    # set up bitmaps for backgrounds
    color_bitmap = displayio.Bitmap(128, 128, 1)
    button1_bitmap = displayio.Bitmap(20, 55, 1)
    button2_bitmap = displayio.Bitmap(20, 55, 1)
    description1_bitmap = displayio.Bitmap(95, 55, 1)
    description2_bitmap = displayio.Bitmap(95, 55, 1)

    # set up color palettes
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background
    button_palette = displayio.Palette(1)
    button_palette[0] = 0x89CFF0  # light blue buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x0B41E0  # average blue background for description

    # set up formatting and placements
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    button1_sprite = displayio.TileGrid(button1_bitmap, pixel_shader=button_palette, x=8, y=6)
    button2_sprite = displayio.TileGrid(button2_bitmap, pixel_shader=button_palette, x=8, y=66)
    description1_sprite = displayio.TileGrid(description1_bitmap, pixel_shader=description_palette, x=28, y=6)
    description2_sprite = displayio.TileGrid(description2_bitmap, pixel_shader=description_palette, x=28, y=66)

    # set up button and description texts
    text_one = label.Label(terminalio.FONT, text="1", scale=3, color=0xFFFFFF, x=11, y=30)
    text_two = label.Label(terminalio.FONT, text="2", scale=3, color=0xFFFFFF, x=11, y=90)
    text_description1 = label.Label(
        terminalio.FONT, text="Choose a\nsequence of\ndance moves!", color=0xFFFFFF, x=32, y=15
    )
    text_description2 = label.Label(terminalio.FONT, text="Perform all\ndance moves!", color=0xFFFFFF, x=32, y=75)

    # show display
    main_menu.append(bg_sprite)
    main_menu.append(button1_sprite)
    main_menu.append(button2_sprite)
    main_menu.append(description1_sprite)
    main_menu.append(description2_sprite)
    main_menu.append(text_one)
    main_menu.append(text_two)
    main_menu.append(text_description1)
    main_menu.append(text_description2)


"""
    Displays the sub menu of the robot with bitmaps and texts
    Prompts user for a key from 1-6 and performs the corresponding dance moves 
    If other keys are pressed, display will show an error
"""


def sub_menu1_display():
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61 # average blue as background

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

    # Create bitmaps for the buttons
    button1_bitmap = displayio.Bitmap(36, 36, 1)
    button2_bitmap = displayio.Bitmap(36, 36, 1)
    button3_bitmap = displayio.Bitmap(36, 36, 1)
    button4_bitmap = displayio.Bitmap(36, 36, 1)
    button5_bitmap = displayio.Bitmap(36, 36, 1)
    button6_bitmap = displayio.Bitmap(36, 36, 1)

    button_palette = displayio.Palette(1)
    button_palette[0] = 0x89CFF0  # light blue buttons

    # created buttons for the dance moves
    button1_sprite = displayio.TileGrid(button1_bitmap, pixel_shader=button_palette, x=7, y=35)
    button2_sprite = displayio.TileGrid(button2_bitmap, pixel_shader=button_palette, x=48, y=35)
    button3_sprite = displayio.TileGrid(button3_bitmap, pixel_shader=button_palette, x=89, y=35)
    button4_sprite = displayio.TileGrid(button4_bitmap, pixel_shader=button_palette, x=7, y=75)
    button5_sprite = displayio.TileGrid(button5_bitmap, pixel_shader=button_palette, x=48, y=75)
    button6_sprite = displayio.TileGrid(button6_bitmap, pixel_shader=button_palette, x=89, y=75)

    # Create button numbers
    prompt = "Choose your dances!"
    text_label = label.Label(terminalio.FONT, text=prompt, color=0xFFFFFF, x=10, y=15)
    text_one_sub = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=20, y=51)
    text_two_sub = label.Label(terminalio.FONT, text="2", scale=2, color=0xFFFFFF, x=61, y=51)
    text_three = label.Label(terminalio.FONT, text="3", scale=2, color=0xFFFFFF, x=102, y=51)
    text_four = label.Label(terminalio.FONT, text="4", scale=2, color=0xFFFFFF, x=20, y=91)
    text_five = label.Label(terminalio.FONT, text="5", scale=2, color=0xFFFFFF, x=61, y=91)
    text_six = label.Label(terminalio.FONT, text="6", scale=2, color=0xFFFFFF, x=102, y=91)
    
    sub_menu1.append(bg_sprite)
    sub_menu1.append(button1_sprite)
    sub_menu1.append(button2_sprite)
    sub_menu1.append(button3_sprite)
    sub_menu1.append(button4_sprite)
    sub_menu1.append(button5_sprite)
    sub_menu1.append(button6_sprite)
    sub_menu1.append(text_label)
    sub_menu1.append(text_one_sub)
    sub_menu1.append(text_two_sub)
    sub_menu1.append(text_three)
    sub_menu1.append(text_four)
    sub_menu1.append(text_five)
    sub_menu1.append(text_six)


def sub_menu2_display():
    # set up bitmaps for backgrounds
    color_bitmap = displayio.Bitmap(128, 128, 1)
    button1_bitmap = displayio.Bitmap(20, 55, 1)
    button2_bitmap = displayio.Bitmap(20, 55, 1)
    description1_bitmap = displayio.Bitmap(95, 55, 1)
    description2_bitmap = displayio.Bitmap(95, 55, 1)

    # set up color palettes
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background
    button_palette = displayio.Palette(1)
    button_palette[0] = 0x89CFF0  # light blue buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x0B41E0  # average blue background for description

    # set up formatting and placements
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    button1_sprite = displayio.TileGrid(button1_bitmap, pixel_shader=button_palette, x=8, y=6)
    button2_sprite = displayio.TileGrid(button2_bitmap, pixel_shader=button_palette, x=8, y=66)
    description1_sprite = displayio.TileGrid(description1_bitmap, pixel_shader=description_palette, x=28, y=6)
    description2_sprite = displayio.TileGrid(description2_bitmap, pixel_shader=description_palette, x=28, y=66)

    # set up button and description texts
    text_one = label.Label(terminalio.FONT, text="7", scale=3, color=0xFFFFFF, x=11, y=30)
    text_two = label.Label(terminalio.FONT, text="8", scale=3, color=0xFFFFFF, x=11, y=90)
    text_description1 = label.Label(
        terminalio.FONT, text="Perform\ndances from\ndance1->dance6", color=0xFFFFFF, x=32, y=15
    )
    text_description2 = label.Label(
        terminalio.FONT, text="Perform\ndance from\ndance6->dance1", color=0xFFFFFF, x=32, y=75
    )

    # show display
    sub_menu2.append(bg_sprite)
    sub_menu2.append(button1_sprite)
    sub_menu2.append(button2_sprite)
    sub_menu2.append(description1_sprite)
    sub_menu2.append(description2_sprite)
    sub_menu2.append(text_one)
    sub_menu2.append(text_two)
    sub_menu2.append(text_description1)
    sub_menu2.append(text_description2)


""" Displays error message on LCD screen when an invalid button is pressed """


def error_display(menu):
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    error.append(bg_sprite)

    text_error = label.Label(terminalio.FONT, text="ERROR:\nINVALID\nBUTTON", color=0xFFFFFF, scale=2, x=25, y=28)
    error.append(text_error)
    display.show(error)
    time.sleep(2)
    display.show(menu)


def loading(GIF_dir):
    # directory on CIRCUITPY where BMP animation frames are stored
    GIF_files = os.listdir(GIF_dir)

    for name in GIF_files:
        filename = GIF_dir + "/" + name
        bitmap, palette = adafruit_imageload.load(filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)  # Create a TileGrid to hold the bitmap
        group = displayio.Group()  # Create a Group to hold the TileGrid
        group.append(tile_grid)  # Add the TileGrid to the Group
        display.show(group)  # Add the Group to the Display


""" Changes the color of a button when its corresponding dance move is being performed by the robot """


def sub_button1_active(button):
    button_bitmap = displayio.Bitmap(36, 36, 1)
    button_palette = displayio.Palette(1)
    button_palette[0] = 0xF0CF89  # yellow buttons

    if button == 1:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=7, y=35)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=20, y=51)
        sub_menu1.append(button_sprite)
        sub_menu1.append(text)
    elif button == 2:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=48, y=35)
        text = label.Label(terminalio.FONT, text="2", scale=2, color=0xFFFFFF, x=61, y=51)
        sub_menu1.append(button_sprite)
        sub_menu1.append(text)
    elif button == 3:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=89, y=35)
        text = label.Label(terminalio.FONT, text="3", scale=2, color=0xFFFFFF, x=102, y=51)
        sub_menu1.append(button_sprite)
        sub_menu1.append(text)
    elif button == 4:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=7, y=75)
        text = label.Label(terminalio.FONT, text="4", scale=2, color=0xFFFFFF, x=20, y=91)
        sub_menu1.append(button_sprite)
        sub_menu1.append(text)
    elif button == 5:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=48, y=75)
        text = label.Label(terminalio.FONT, text="5", scale=2, color=0xFFFFFF, x=61, y=91)
        sub_menu1.append(button_sprite)
        sub_menu1.append(text)
    elif button == 6:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=89, y=75)
        text = label.Label(terminalio.FONT, text="6", scale=2, color=0xFFFFFF, x=102, y=91)
        sub_menu1.append(button_sprite)
        sub_menu1.append(text)

    time.sleep(0.5)
    sub_menu1.pop()
    sub_menu1.pop()


def sub_button2_active(button):
    button_bitmap = displayio.Bitmap(20, 55, 1)
    description_bitmap = displayio.Bitmap(95, 55, 1)

    button_palette = displayio.Palette(1)
    button_palette[0] = 0xE0A50B  # yellow buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x946B00  # gold description

    if button == 7:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=8, y=6)
        description_sprite = displayio.TileGrid(description_bitmap, pixel_shader=description_palette, x=28, y=6)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="7", scale=3, color=0xFFFFFF, x=11, y=30)
        text_description = label.Label(
            terminalio.FONT, text="Perform\ndances from\ndance1->dance6", color=0xFFFFFF, x=32, y=15
        )
    elif button == 8:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=8, y=66)
        description_sprite = displayio.TileGrid(description_bitmap, pixel_shader=description_palette, x=28, y=66)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="8", scale=3, color=0xFFFFFF, x=11, y=90)
        text_description = label.Label(
            terminalio.FONT, text="Perform\ndance from\ndance6->dance1", color=0xFFFFFF, x=32, y=75
            )

    sub_menu2.append(button_sprite)
    sub_menu2.append(description_sprite)
    sub_menu2.append(text)
    sub_menu2.append(text_description)
    time.sleep(0.5)
    sub_menu2.pop()
    sub_menu2.pop()
    sub_menu2.pop()
    sub_menu2.pop()


""" Changes the color of button 2 and description 2 in the main menu 
    Used when the robot is per"""


def main_button_active(button):
    button_bitmap = displayio.Bitmap(20, 55, 1)
    description_bitmap = displayio.Bitmap(95, 55, 1)

    button_palette = displayio.Palette(1)
    button_palette[0] = 0xE0A50B  # yellow buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x946B00  # gold description

    if button == 1:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=8, y=6)
        description_sprite = displayio.TileGrid(description_bitmap, pixel_shader=description_palette, x=28, y=6)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="1", scale=3, color=0xFFFFFF, x=11, y=30)
        text_description = label.Label(terminalio.FONT, text="Choose a\nsequence of\ndance moves!", color=0xFFFFFF, x=32,
                                       y=15)
    elif button == 2:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=8, y=66)
        description_sprite = displayio.TileGrid(description_bitmap, pixel_shader=description_palette, x=28, y=66)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="2", scale=3, color=0xFFFFFF, x=11, y=90)
        text_description = label.Label(terminalio.FONT, text="Perform all\ndance moves", color=0xFFFFFF, x=32,
                                       y=75)
 
    main_menu.append(button_sprite)
    main_menu.append(description_sprite)
    main_menu.append(text)
    main_menu.append(text_description)
    time.sleep(0.5)
    main_menu.pop()
    main_menu.pop()
    main_menu.pop()
    main_menu.pop()


# define correct center angles:
clegl = 90
clegr = 102
cfootl = 92
cfootr = 94


# reset position function
def resetto90():
    leg_left.angle = 90
    leg_right.angle = 102
    foot_left.angle = 92
    foot_right.angle = 90


# ------------SET UP PINS FOR LEGS AND FEET----------------------------
# create a PWMOut object on Pin D9-12.
bot_left = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
bot_right = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
top_left = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
top_right = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
leg_left = servo.Servo(top_left)
leg_right = servo.Servo(top_right)
foot_left = servo.Servo(bot_left)
foot_right = servo.Servo(bot_right)

# -----------------------SET UP MUSIC PINS-----------------------------------------------
PIEZO_PIN = buzzer.PIEZO_PIN
melody1 = buzzer.melody1
melody2 = buzzer.melody2
tempo = buzzer.tempo
# -----------------------------------MOVE SETS FUNCTIONS----------------------------------
move1 = False
move2 = False
move3 = False
move4 = False
move5 = False
move6 = False


# -----------------------------------MOVE 1---------------------------------------------
def move_set1():
    i = 0
    count = 0
    while move1:
        if count != 0:
            i = i + 2
        resetto90()
        for angle in range(60, 120, 6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[i], 0.05)
        i = i + 2
        for angle in range(120, 60, -6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[i], 0.05)
        resetto90()

        t = 0
        for angle in range(90, 150, 6):
            foot_left.angle = angle
            foot_right.angle = 180 - angle
            if t < 0.25:
                j = i + 2
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
            else:
                j = i + 4
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05

        t = 0
        for angle in range(150, 90, -6):
            foot_left.angle = angle
            foot_right.angle = 180 - angle

            if t < 0.25:
                j = i + 6
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
            else:
                j = i + 8
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
        i = j
        resetto90()
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody1[i], tempo / melody1[i + 1])
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody1[i], tempo / melody1[i + 1])

        count = count + 1
        if count == 3:
            # move1 = False
            break


# -----------------------------------MOVE 2---------------------------------------------
def move_set2():
    i = 48
    while move2:
        resetto90()
        for angle in range(102, 41, -12):  # turn right leg
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[i], 0.05)
        i = i + 2
        for angle in range(90, 161, 12):  # turn left leg
            leg_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[i], 0.05)
        for a in range(4):
            i = i + 2
            for angle in range(90, 110, 5):
                foot_left.angle = angle
                foot_right.angle = angle
                simpleio.tone(PIEZO_PIN, melody1[i], 0.025)
            for angle in range(110, 60, -5):
                foot_left.angle = angle
                foot_right.angle = angle
                simpleio.tone(PIEZO_PIN, melody1[i], 0.025)
            for angle in range(60, 90, 5):
                foot_left.angle = angle
                foot_right.angle = angle
                simpleio.tone(PIEZO_PIN, melody1[i], 0.025)
        resetto90()
        simpleio.tone(PIEZO_PIN, melody1[i], 0.5)
        # move2 = False
        break


# -----------------------------------MOVE 3---------------------------------------------
def move_set3():
    i = 0
    count = 0
    while move3:
        resetto90()
        if count == 1:
            i = i + 2
        # right up
        for angle in range(cfootr, cfootr - 81, -40):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        for angle in range(cfootl, cfootl - 61, -20):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        #  \\

        simpleio.tone(PIEZO_PIN, melody2[i], 0.25)
        foot_right.angle = 124  # lift up outward
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        leg_right.angle = 32  # kick
        time.sleep(0.1)
        i = i + 2
        for angle in range(32, 93, 6):  # shake
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        i = i + 2
        for angle in range(93, 32, -6):  # shake
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        resetto90()
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        elif count == 1:
            i = i + 2
            simpleio.tone(PIEZO_PIN, melody2[i], 0.5)

        # --------------------

        # left up
        i = i + 2
        for angle in range(cfootl, cfootl + 81, 40):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        for angle in range(cfootr, cfootr + 61, 20):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)

        #  //
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[i], 0.25)
        elif count == 1:
            i = i + 2
            simpleio.tone(PIEZO_PIN, melody2[i], 0.25)
        foot_left.angle = 50  # lift up outward
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        leg_left.angle = 143  # kick
        time.sleep(0.1)
        i = i + 2
        for angle in range(143, 82, -6):  # shake
            leg_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        i = i + 2
        for angle in range(82, 143, 6):  # shake
            leg_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)

        resetto90()
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)

        count = count + 1
        if count == 2:
            # move3 = False
            break


# -----------------------------------MOVE 4---------------------------------------------
def move_set4():
    count=0
    while move4:
        resetto90()
        time.sleep(0.5)

        # turn lefy
        for angle in range(90, 10, -39):
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(92, 32, -19):
            foot_left.angle = angle
            time.sleep(0.05)
        #  \\

        time.sleep(0.1)
        foot_right.angle = 120  # lift up outward
        time.sleep(1)
        leg_right.angle = 32  # kick
        time.sleep(0.1)

        for angle in range(90, 30, -3):
            leg_left.angle = angle
            time.sleep(0.05)
        for angle in range(32, 102, 3):
            leg_right.angle = angle
            time.sleep(0.05)
        for angle in range(32, 92, 19):
            foot_left.angle = angle
            time.sleep(0.05)
        for angle in range(120, 89, -10):
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(30, 90, 3):
            leg_left.angle = angle
            time.sleep(0.05)

        count = count + 1
        if (count == 2):
            
            resetto90()
            break


# -----------------------------------MOVE 5---------------------------------------------
def move_set5():
    while move5:
        resetto90()
        # 开合
        for i in range(5):
            for i in range(10):
                leg_left.angle = leg_left.angle + 3
                leg_right.angle = leg_right.angle - 3
                foot_right.angle = foot_right.angle + 3
                foot_left.angle = foot_left.angle - 3

            for i in range(10):
                leg_left.angle = leg_left.angle - 3
                leg_right.angle = leg_right.angle + 3
                foot_right.angle = foot_right.angle - 3
                foot_left.angle = foot_left.angle + 3

            resetto90()
        # 左右
        for i in range(5):
            for i in range(20):
                leg_left.angle = leg_left.angle - 2
                leg_right.angle = leg_right.angle - 2

            for i in range(21):
                leg_left.angle = leg_left.angle + 4
                leg_right.angle = leg_right.angle + 4

            for i in range(20):
                leg_left.angle = leg_left.angle - 2
                leg_right.angle = leg_right.angle - 2

        # move5 = False
        for i in range(5):
            for i in range(10):
                foot_right.angle = foot_right.angle - 3
                foot_left.angle = foot_left.angle - 3

            for i in range(10):
                foot_right.angle = foot_right.angle + 3
                foot_left.angle = foot_left.angle + 3
        break


# -----------------------------------MOVE 6---------------------------------------------
def move_set6():
    while move6:
        resetto90()
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4
        for i in range(10):
            leg_right.angle = leg_right.angle + 8
            foot_right.angle = foot_right.angle - 8
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4

        for i in range(20):
            leg_left.angle = leg_left.angle + 2
            foot_left.angle = foot_left.angle - 2
        for i in range(20):
            leg_left.angle = leg_left.angle - 4
            foot_left.angle = foot_left.angle + 4
        for i in range(20):
            leg_left.angle = leg_left.angle + 4
            foot_left.angle = foot_left.angle - 2
        # move6 = False
        break


# -----------------------------END OF MOVE SETS FUNCTIONS SECTION----------------------------------

# ------------SET UP KEYPAD--------------
# latch_pin = digitalio.DigitalInOut(board.D5) #change to another pin if D5 is not working
# sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

# # Create the pin objects in a list
# pins = [sr.get_pin(n) for n in range(1,8)]

rows = [digitalio.DigitalInOut(x) for x in (board.A2, board.A3, board.A4, board.SDA)]
cols = [digitalio.DigitalInOut(x) for x in (board.TX, board.SCL, board.A5)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
# ---------------------------------------

# -------------------------------MAIN PROGRAM-----------------------------------
# read_input = True
# move_sequence =[]
# keeps reading the input until user press key '0'
main_menu_display()
sub_menu1_display()
sub_menu2_display()
while True:
    main_keys = keypad.pressed_keys
    display.show(main_menu)
    if main_keys:
        # main menu
        time.sleep(0.2)
        if main_keys == [1]:
            main_button_active(1)
            display.show(sub_menu1)
            # sub menu 1
            while True: 
                keys = keypad.pressed_keys
                if keys:
                    time.sleep(0.2)
                    if keys == [1]:
                        sub_button1_active(1)
                        move1 = True
                        move_set1()
                        resetto90()
                    elif keys == [2]:
                        sub_button1_active(2)
                        move2 = True
                        move_set2()
                        resetto90()
                    elif keys == [3]:
                        sub_button1_active(3)
                        move3 = True
                        move_set3()
                        resetto90()
                    elif keys == [4]:
                        sub_button1_active(4)
                        move4 = True
                        move_set4()
                        resetto90()
                    elif keys == [5]:
                        sub_button1_active(5)
                        move5 = True
                        move_set5()
                        resetto90()
                    elif keys == [6]:
                        sub_button1_active(6)
                        move6 = True
                        move_set6()
                        resetto90()
                    elif keys == [9]:
                        print("Terminated")
                        break
                    else:
                        error_display(sub_menu1)

        elif main_keys == [2]:
            main_button_active(2)
            display.show(sub_menu2)
            # sub menu 2
            while True: 
                keys = keypad.pressed_keys
                if keys:
                    time.sleep(0.2)
                    if keys == [7]:
                        sub_button2_active(7)
                        #move1 = True
                        #move_set1()
                        #resetto90()
                    elif keys == [8]:
                        sub_button2_active(8)
                        #move2 = True
                        #move_set2()
                        #resetto90()
                    elif keys == [9]:
                        break
                        #move3 = True
                        #move_set3()
                        #resetto90()
                    else:
                        error_display(sub_menu2)
        elif main_keys == [9]:
            break
        else: 
            error_display(main_menu)
