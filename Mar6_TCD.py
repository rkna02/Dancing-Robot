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

def resetto90():
    leg_left.angle = 90
    leg_right.angle = 102
    foot_left.angle = 92
    foot_right.angle = 90


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
sub_menu = displayio.Group()
error = displayio.Group()


""" 
    Displays the main menu of the robot with bitmaps and texts
    Prompts user for a key from 1-2 and performs their corresponding actions
    If other keys are pressed, display will show an error
    1 - navigates user to a new page where the user can choose individual dance moves to perform
    2 - click to immediately perform all dance moves at once 
"""

def main_menu():
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
        terminalio.FONT, text="Choose an\nindividual\ndance move!", color=0xFFFFFF, x=32, y=15
    )
    text_description2 = label.Label(terminalio.FONT, text="Perform all\ndance moves\nnow!", color=0xFFFFFF, x=32, y=75)

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


def sub_menu():
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Create bitmaps for the buttons
    button1_bitmap = displayio.Bitmap(36, 36, 1)
    button2_bitmap = displayio.Bitmap(36, 36, 1)
    button3_bitmap = displayio.Bitmap(36, 36, 1)
    button4_bitmap = displayio.Bitmap(36, 36, 1)
    button5_bitmap = displayio.Bitmap(36, 36, 1)
    button6_bitmap = displayio.Bitmap(36, 36, 1)

    button_palette = displayio.Palette(1)
    button_palette[0] = 0x89CFF0 # blue buttons

    # created buttons for the dance moves
    button1_sprite = displayio.TileGrid(button1_bitmap, pixel_shader=button_palette, x=7, y=35)
    button2_sprite = displayio.TileGrid(button2_bitmap, pixel_shader=button_palette, x=48, y=35)
    button3_sprite = displayio.TileGrid(button3_bitmap, pixel_shader=button_palette, x=89, y=35)
    button4_sprite = displayio.TileGrid(button4_bitmap, pixel_shader=button_palette, x=7, y=75)
    button5_sprite = displayio.TileGrid(button5_bitmap, pixel_shader=button_palette, x=48, y=75)
    button6_sprite = displayio.TileGrid(button6_bitmap, pixel_shader=button_palette, x=89, y=75)

    # Create button numbers
    prompt = "Choose a dance!"
    text_label = label.Label(terminalio.FONT, text=prompt, color=0xFFFFFF, x=22, y=15)
    text_one_sub = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=20, y=51)
    text_two_sub = label.Label(terminalio.FONT, text="2", scale=2, color=0xFFFFFF, x=61, y=51)
    text_three = label.Label(terminalio.FONT, text="3", scale=2, color=0xFFFFFF, x=102, y=51)
    text_four = label.Label(terminalio.FONT, text="4", scale=2, color=0xFFFFFF, x=20, y=91)
    text_five = label.Label(terminalio.FONT, text="5", scale=2, color=0xFFFFFF, x=61, y=91)
    text_six = label.Label(terminalio.FONT, text="6", scale=2, color=0xFFFFFF, x=102, y=91)

    sub_menu.append(button1_sprite)
    sub_menu.append(button2_sprite)
    sub_menu.append(button3_sprite)
    sub_menu.append(button4_sprite)
    sub_menu.append(button5_sprite)
    sub_menu.append(button6_sprite)
    sub_menu.append(text_label)
    sub_menu.append(text_one_sub)
    sub_menu.append(text_two_sub)
    sub_menu.append(text_three)
    sub_menu.append(text_four)
    sub_menu.append(text_five)
    sub_menu.append(text_six)
    
""" Displays error message on LCD screen when an invalid button is pressed """


def error():
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    error.append(bg_sprite)
    
    text_error1 = label.Label(terminalio.FONT, text="ERROR:", color=0xFFFFFF, scale=2, x=22, y=30)
    text_error2 = label.Label(terminalio.FONT, text="INVALID BUTTON", color=0xFFFFFF, scale=2, x=22, y=75)
    error.append(text_error1)
    error.append(text_error2)


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
    display.release(group)


""" Changes the color of a button when its corresponding dance move is being performed by the robot """


def performing_ind(button):
    button_bitmap = displayio.Bitmap(36, 36, 1)
    button_palette = displayio.Palette(1)
    button_palette[0] = 0xF0CF89  # yellow buttons

    if button == 1:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=7, y=35)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=20, y=51)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 2:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=48, y=35)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=61, y=51)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 3:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=89, y=35)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=102, y=51)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 4:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=7, y=75)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=20, y=91)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 5:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=48, y=75)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=61, y=91)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 6:
        button_sprite = displayio.TileGrid(button_bitmap, pixel_shader=button_palette, x=89, y=75)
        text = label.Label(terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=102, y=91)
        splash.append(button_sprite)
        splash.append(text)
        
    time.sleep(0.5)
    splash.pop()
    splash.pop()


""" Changes the color of button 2 and description 2 in the main menu 
    Used when the robot is per"""


def performing_all():
    button_bitmap = displayio.Bitmap(20, 55, 1)
    description_bitmap = displayio.Bitmap(95, 55, 1)
    
    button_palette = displayio.Palette(1)
    button_palette[0] = 0xF0CF89  # yellow buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x0B41E0  # gold description

    button_sprite = displayio.TileGrid(button2_bitmap, pixel_shader=button_palette, x=8, y=66)
    description_sprite = displayio.TileGrid(description2_bitmap, pixel_shader=description_palette, x=28, y=66)

    # set up button and description texts
    text_two = label.Label(terminalio.FONT, text="2", scale=3, color=0xFFFFFF, x=11, y=90)
    text_description = label.Label(terminalio.FONT, text="Perform all\ndance moves\nnow!", color=0xFFFFFF, x=32, y=75)

    # show display
    splash.append(button_sprite)
    splash.append(description_sprite)
    splash.append(text_two)
    splash.append(text_description)



while True:
    main_menu()
    time.sleep(3)
    sub_menu()
    time.sleep(3)
    loading("GIF/loading")
    time.sleep(3)


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

move1 = False
move2 = False
move3 = False
move4 = False
move5 = False
move6 = True
music = False

count = 0

while move1:
    for angle in range(80, 100, 5):
        leg_left.angle = angle
        leg_right.angle = angle
        time.sleep(0.05)
    for angle in range(100, 80, -5):
        leg_left.angle = angle
        leg_right.angle = angle
        time.sleep(0.05)

    for angle in range(90, 150, 10):
        foot_left.angle = angle
        foot_right.angle = 180 - angle
        time.sleep(0.1)
    for angle in range(150, 90, -10):
        foot_left.angle = angle
        foot_right.angle = 180 - angle
        time.sleep(0.1)
    resetto90()
    time.sleep(0.05)
    count = count + 1
    if count == 3:
        move1 = False

time.sleep(1)
count = 0
while move2:
    resetto90()

    # right up
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

    for angle in range(32, 102, 3):  # shake
        leg_right.angle = angle
        time.sleep(0.01)
    for angle in range(102, 32, -3):  # shake
        leg_right.angle = angle
        time.sleep(0.01)
    resetto90()
    time.sleep(0.5)

    # --------------------

    # left up
    for angle in range(92, 172, 39):
        foot_left.angle = angle
        time.sleep(0.05)
    for angle in range(90, 150, 19):
        foot_right.angle = angle
        time.sleep(0.05)
    #  //

    time.sleep(0.1)
    foot_left.angle = 50  # lift up outward
    time.sleep(1)
    leg_left.angle = 152  # kick
    time.sleep(0.1)

    for angle in range(152, 82, -3):  # shake
        leg_left.angle = angle
        time.sleep(0.01)
    for angle in range(82, 152, 3):  # shake
        leg_left.angle = angle
        time.sleep(0.01)

    resetto90()
    time.sleep(0.5)

    count = count + 1
    if count == 3:
        move2 = False

while move3:

    resetto90()
    for angle in range(102, 41, -4):  # turn right leg
        leg_right.angle = angle
        time.sleep(0.05)
    for angle in range(90, 159, 4):  # turn left leg
        leg_left.angle = angle
        time.sleep(0.05)
    for i in range(5):
        for angle in range(90, 120, 5):
            foot_left.angle = angle
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(120, 60, -5):
            foot_left.angle = angle
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(60, 90, 5):
            foot_left.angle = angle
            foot_right.angle = angle
            time.sleep(0.05)

    resetto90()
    time.sleep(1000)
count4 = 0
while move4:
    resetto90()
    time.sleep(0.5)

    # right up
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
        move4 = False
        resetto90()

while move5:
    resetto90()
    # 开合
    for i in range(5):
        for i in range(10):
            leg_left.angle = leg_left.angle + 3
            leg_right.angle = leg_right.angle - 3
            foot_right.angle = foot_right.angle + 3
            foot_left.angle = foot_left.angle - 3
            time.sleep(0.01)
        for i in range(10):
            leg_left.angle = leg_left.angle - 3
            leg_right.angle = leg_right.angle + 3
            foot_right.angle = foot_right.angle - 3
            foot_left.angle = foot_left.angle + 3
            time.sleep(0.01)
        resetto90()
    # 左右
    for i in range(5):
        for i in range(20):
            leg_left.angle = leg_left.angle - 2
            leg_right.angle = leg_right.angle - 2
            time.sleep(0.005)
        for i in range(21):
            leg_left.angle = leg_left.angle + 4
            leg_right.angle = leg_right.angle + 4
            time.sleep(0.01)
        for i in range(20):
            leg_left.angle = leg_left.angle - 2
            leg_right.angle = leg_right.angle - 2
            time.sleep(0.005)
    move5 = False

while move6:
    resetto90()
    time.sleep(1000)
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

# muisc

# Define pin connected to piezo buzzer.
PIEZO_PIN = board.A1
PIEZO_PIN = board.A1

# Pachelbel's Canon

NOTE_B0 = 31
NOTE_C1 = 33
NOTE_CS1 = 35
NOTE_D1 = 37
NOTE_DS1 = 39
NOTE_E1 = 41
NOTE_F1 = 44
NOTE_FS1 = 46
NOTE_G1 = 49
NOTE_GS1 = 52
NOTE_A1 = 55
NOTE_AS1 = 58
NOTE_B1 = 62
NOTE_C2 = 65
NOTE_CS2 = 69
NOTE_D2 = 73
NOTE_DS2 = 78
NOTE_E2 = 82
NOTE_F2 = 87
NOTE_FS2 = 93
NOTE_G2 = 98
NOTE_GS2 = 104
NOTE_A2 = 110
NOTE_AS2 = 117
NOTE_B2 = 123
NOTE_C3 = 131
NOTE_CS3 = 139
NOTE_D3 = 147
NOTE_DS3 = 156
NOTE_E3 = 165
NOTE_F3 = 175
NOTE_FS3 = 185
NOTE_G3 = 196
NOTE_GS3 = 208
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_DS4 = 311
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_FS4 = 370
NOTE_G4 = 392
NOTE_GS4 = 415
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_CS5 = 554
NOTE_D5 = 587
NOTE_DS5 = 622
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_FS5 = 740
NOTE_G5 = 784
NOTE_GS5 = 831
NOTE_A5 = 880
NOTE_AS5 = 932
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_CS6 = 1109
NOTE_D6 = 1175
NOTE_DS6 = 1245
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_FS6 = 1480
NOTE_G6 = 1568
NOTE_GS6 = 1661
NOTE_A6 = 1760
NOTE_AS6 = 1865
NOTE_B6 = 1976
NOTE_C7 = 2093
NOTE_CS7 = 2217
NOTE_D7 = 2349
NOTE_DS7 = 2489
NOTE_E7 = 2637
NOTE_F7 = 2794
NOTE_FS7 = 2960
NOTE_G7 = 3136
NOTE_GS7 = 3322
NOTE_A7 = 3520
NOTE_AS7 = 3729
NOTE_B7 = 3951
NOTE_C8 = 4186
NOTE_CS8 = 4435
NOTE_D8 = 4699
NOTE_DS8 = 4978
REST = 0

# change this to make the song slower or faster
tempo = 200

melody = [NOTE_C5, 4,
          NOTE_F5, 4, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_E5, 8,
          NOTE_D5, 4, NOTE_D5, 4, NOTE_D5, 4,
          NOTE_G5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
          NOTE_E5, 4, NOTE_C5, 4, NOTE_C5, 4,
          NOTE_A5, 4, NOTE_A5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8,
          NOTE_F5, 4, NOTE_D5, 4, NOTE_C5, 8, NOTE_C5, 8,
          NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,

          NOTE_F5, 2, NOTE_C5, 4,
          NOTE_F5, 4, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_E5, 8,
          NOTE_D5, 4, NOTE_D5, 4, NOTE_D5, 4,
          NOTE_G5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
          NOTE_E5, 4, NOTE_C5, 4, NOTE_C5, 4,
          NOTE_A5, 4, NOTE_A5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8,
          NOTE_F5, 4, NOTE_D5, 4, NOTE_C5, 8, NOTE_C5, 8,
          NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,
          NOTE_F5, 2, NOTE_C5, 4
          ]

# sizeof gives the number of bytes, each int value is composed of two bytes (16 bits)
# there are two values per note (pitch and duration), so for each note there are four bytes
notes = len(melody) / 2

# this calculates the duration of a whole note in ms
wholenote = (60 * 4) / tempo

divider = 0
noteDuration = 0
while music:
    time.sleep(1000)

    # iterate over the notes of the melody.
    # Remember, the array is twice the number of notes (notes + durations)
    for i in range(0, notes * 2, 2):
        # calculates the duration of each note
        divider = melody[i + 1]
        # regular note, just proceed
        noteDuration = (wholenote) / divider

        # we only play the note for 90% of the duration, leaving 10% as a pause
        simpleio.tone(PIEZO_PIN, melody[i], duration=noteDuration)

        # Wait for the specief duration before playing the next note.
        time.sleep(noteDuration)
