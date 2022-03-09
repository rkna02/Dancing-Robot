import time
import board
import pwmio
import pulseio
import simpleio
from adafruit_motor import servo
import terminalio
import displayio
import adafruit_imageload
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import digitalio
import adafruit_matrixkeypad
import buzzer
import gc

gc.enable()

# display set up and initialization
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D13
tft_dc = board.D7

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D0)
display = ST7735R(display_bus, width=128, height=128, rotation=270)

splash = displayio.Group()
display.show(splash)


def main_menu_display():
    """
        Displays the main menu of the robot with bitmaps and texts
        Prompts user for a key from 1-2 and performs their corresponding actions
        If other keys are pressed, display will show an error
        1 - navigates user to a new page where the user can choose individual dance moves to perform
        2 - navigates user to a new page where the user can choose to perform all dance moves in order/in reverse order
    """

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
    # average blue background for description
    description_palette[0] = 0x0B41E0

    # set up formatting and placements
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)
    button1_sprite = displayio.TileGrid(
        button1_bitmap, pixel_shader=button_palette, x=8, y=6)
    button2_sprite = displayio.TileGrid(
        button2_bitmap, pixel_shader=button_palette, x=8, y=66)
    description1_sprite = displayio.TileGrid(
        description1_bitmap, pixel_shader=description_palette, x=28, y=6)
    description2_sprite = displayio.TileGrid(
        description2_bitmap, pixel_shader=description_palette, x=28, y=66)

    # set up button and description texts
    text_one = label.Label(terminalio.FONT, text="1",
                           scale=3, color=0xFFFFFF, x=11, y=30)
    text_two = label.Label(terminalio.FONT, text="2",
                           scale=3, color=0xFFFFFF, x=11, y=90)
    text_description1 = label.Label(
        terminalio.FONT, text="Choose a\nsequence of\ndance moves!", color=0xFFFFFF, x=32, y=15
    )
    text_description2 = label.Label(
        terminalio.FONT, text="More options!", color=0xFFFFFF, x=32, y=91)

    # append and show display
    splash.append(bg_sprite)
    splash.append(button1_sprite)
    splash.append(button2_sprite)
    splash.append(description1_sprite)
    splash.append(description2_sprite)
    splash.append(text_one)
    splash.append(text_two)
    splash.append(text_description1)
    splash.append(text_description2)


def sub_menu1_display():
    """
        Displays the menu when user choosess option 1 from the main menu of the robot
        Prompts user for a key from 1-6 and performs the corresponding dance moves
        If other keys are pressed, display will show an error
    """

    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # average blue as background

    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)

    # Create bitmaps for the buttons
    button1_bitmap = displayio.Bitmap(36, 36, 1)
    button2_bitmap = displayio.Bitmap(36, 36, 1)
    button3_bitmap = displayio.Bitmap(36, 36, 1)
    button4_bitmap = displayio.Bitmap(36, 36, 1)
    button5_bitmap = displayio.Bitmap(36, 36, 1)
    button6_bitmap = displayio.Bitmap(36, 36, 1)

    # Create palette for the button color
    button_palette = displayio.Palette(1)
    button_palette[0] = 0x89CFF0  # light blue buttons

    # created button backgrounds for the dance moves
    button1_sprite = displayio.TileGrid(
        button1_bitmap, pixel_shader=button_palette, x=7, y=35)
    button2_sprite = displayio.TileGrid(
        button2_bitmap, pixel_shader=button_palette, x=48, y=35)
    button3_sprite = displayio.TileGrid(
        button3_bitmap, pixel_shader=button_palette, x=89, y=35)
    button4_sprite = displayio.TileGrid(
        button4_bitmap, pixel_shader=button_palette, x=7, y=75)
    button5_sprite = displayio.TileGrid(
        button5_bitmap, pixel_shader=button_palette, x=48, y=75)
    button6_sprite = displayio.TileGrid(
        button6_bitmap, pixel_shader=button_palette, x=89, y=75)

    # Create button numbers
    prompt = "Choose your dances!"
    text_label = label.Label(
        terminalio.FONT, text=prompt, color=0xFFFFFF, x=10, y=15)
    text_one_sub = label.Label(
        terminalio.FONT, text="1", scale=2, color=0xFFFFFF, x=20, y=51)
    text_two_sub = label.Label(
        terminalio.FONT, text="2", scale=2, color=0xFFFFFF, x=61, y=51)
    text_three = label.Label(terminalio.FONT, text="3",
                             scale=2, color=0xFFFFFF, x=102, y=51)
    text_four = label.Label(terminalio.FONT, text="4",
                            scale=2, color=0xFFFFFF, x=20, y=91)
    text_five = label.Label(terminalio.FONT, text="5",
                            scale=2, color=0xFFFFFF, x=61, y=91)
    text_six = label.Label(terminalio.FONT, text="6",
                           scale=2, color=0xFFFFFF, x=102, y=91)

    # append and display menu
    splash.append(bg_sprite)
    splash.append(button1_sprite)
    splash.append(button2_sprite)
    splash.append(button3_sprite)
    splash.append(button4_sprite)
    splash.append(button5_sprite)
    splash.append(button6_sprite)
    splash.append(text_label)
    splash.append(text_one_sub)
    splash.append(text_two_sub)
    splash.append(text_three)
    splash.append(text_four)
    splash.append(text_five)
    splash.append(text_six)


def sub_menu2_display():
    """
        Displays the menu when user chooses option 2 from the main menu of the robot
        Prompts user for a key from 7-8 and performs the corresponding dance moves
        If other keys are pressed, display will show an error
    """

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
    # average blue background for description
    description_palette[0] = 0x0B41E0

    # set up formatting and placements
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)
    button1_sprite = displayio.TileGrid(
        button1_bitmap, pixel_shader=button_palette, x=8, y=6)
    button2_sprite = displayio.TileGrid(
        button2_bitmap, pixel_shader=button_palette, x=8, y=66)
    description1_sprite = displayio.TileGrid(
        description1_bitmap, pixel_shader=description_palette, x=28, y=6)
    description2_sprite = displayio.TileGrid(
        description2_bitmap, pixel_shader=description_palette, x=28, y=66)

    # set up button and description texts
    text_one = label.Label(terminalio.FONT, text="7",
                           scale=3, color=0xFFFFFF, x=11, y=30)
    text_two = label.Label(terminalio.FONT, text="8",
                           scale=3, color=0xFFFFFF, x=11, y=90)
    text_description1 = label.Label(
        terminalio.FONT, text="Perform all\ndances now!", color=0xFFFFFF, x=32, y=15
    )
    text_description2 = label.Label(
        terminalio.FONT, text="Play mini\nmovie now!", color=0xFFFFFF, x=32, y=75
    )

    # append and show display
    splash.append(bg_sprite)
    splash.append(button1_sprite)
    splash.append(button2_sprite)
    splash.append(description1_sprite)
    splash.append(description2_sprite)
    splash.append(text_one)
    splash.append(text_two)
    splash.append(text_description1)
    splash.append(text_description2)


def error_display():
    """ 
        Displays error message on LCD screen when an invalid button is pressed
        Different buttons can be invalid based on the current menu
        Please see menu functions for specific details
    """

    # define and display background of error message
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    text_error = label.Label(
        terminalio.FONT, text="ERROR:\nINVALID\nBUTTON", color=0xFFFFFF, scale=2, x=25, y=28)
    splash.append(text_error)

    # shows error message for 2 seconds then erases it
    time.sleep(2)
    splash.pop()
    splash.pop()

def move_display(movename):
    """
        Displays the move name before performing a dance move
    """
    
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x221D61  # Dark blue as background
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    text_error = label.Label(
        terminalio.FONT, text=f"Loading:\n{movename}\n", color=0xFFFFFF, scale=2, x=20, y=30)
    splash.append(text_error)

    # shows error message for 2 seconds then erases it
    time.sleep(1.3)
    splash.pop()
    splash.pop()
    


def clear_menu(menu):
    """
        Clears everything from the current menu
        PARAM menu: must be one of the strings "main_menu", "sub_menu1", "sub_menu2"
    """

    if menu == "sub_menu1":
        for i in range(0, 14):
            splash.pop()
    elif menu == "main_menu" or menu == "sub_menu2":
        for i in range(0, 9):
            splash.pop()


def main_button_active(button):
    """
        Changes the color of button1 or button2 in the main menu when pressed
        The color changes for 0.4 seconds then goes back to its original color
        PARAM button: the button reference number that will modify the corresponding button color
    """

    button_bitmap = displayio.Bitmap(20, 55, 1)
    description_bitmap = displayio.Bitmap(95, 55, 1)

    button_palette = displayio.Palette(1)
    button_palette[0] = 0xE0A50B  # yellow buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x946B00  # gold description

    if button == 1:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=8, y=6)
        description_sprite = displayio.TileGrid(
            description_bitmap, pixel_shader=description_palette, x=28, y=6)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="1",
                           scale=3, color=0xFFFFFF, x=11, y=30)
        text_description = label.Label(terminalio.FONT, text="Choose a\nsequence of\ndance moves!", color=0xFFFFFF,
                                       x=32,
                                       y=15)
        splash.append(button_sprite)
        splash.append(description_sprite)
        splash.append(text)
        splash.append(text_description)
    elif button == 2:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=8, y=66)
        description_sprite = displayio.TileGrid(
            description_bitmap, pixel_shader=description_palette, x=28, y=66)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="2",
                           scale=3, color=0xFFFFFF, x=11, y=90)
        text_description = label.Label(terminalio.FONT, text="More options!", color=0xFFFFFF, x=32,
                                       y=91)
        splash.append(button_sprite)
        splash.append(description_sprite)
        splash.append(text)
        splash.append(text_description)

    time.sleep(0.4)
    splash.pop()
    splash.pop()
    splash.pop()
    splash.pop()


def sub_button1_active(button):
    """ Changes the color of a button when its corresponding dance move is being performed by the robot """

    button_bitmap = displayio.Bitmap(36, 36, 1)
    button_palette = displayio.Palette(1)
    button_palette[0] = 0xF0CF89  # yellow buttons

    if button == 1:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=7, y=35)
        text = label.Label(terminalio.FONT, text="1",
                           scale=2, color=0xFFFFFF, x=20, y=51)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 2:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=48, y=35)
        text = label.Label(terminalio.FONT, text="2",
                           scale=2, color=0xFFFFFF, x=61, y=51)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 3:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=89, y=35)
        text = label.Label(terminalio.FONT, text="3",
                           scale=2, color=0xFFFFFF, x=102, y=51)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 4:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=7, y=75)
        text = label.Label(terminalio.FONT, text="4",
                           scale=2, color=0xFFFFFF, x=20, y=91)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 5:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=48, y=75)
        text = label.Label(terminalio.FONT, text="5",
                           scale=2, color=0xFFFFFF, x=61, y=91)
        splash.append(button_sprite)
        splash.append(text)
    elif button == 6:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=89, y=75)
        text = label.Label(terminalio.FONT, text="6",
                           scale=2, color=0xFFFFFF, x=102, y=91)
        splash.append(button_sprite)
        splash.append(text)

    time.sleep(0.5)
    splash.pop()
    splash.pop()


def sub_button2_active(button):
    button_bitmap = displayio.Bitmap(20, 55, 1)
    description_bitmap = displayio.Bitmap(95, 55, 1)

    button_palette = displayio.Palette(1)
    button_palette[0] = 0xE0A50B  # yellow buttons
    description_palette = displayio.Palette(1)
    description_palette[0] = 0x946B00  # gold description

    if button == 7:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=8, y=6)
        description_sprite = displayio.TileGrid(
            description_bitmap, pixel_shader=description_palette, x=28, y=6)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="7",
                           scale=3, color=0xFFFFFF, x=11, y=30)
        text_description = label.Label(
            terminalio.FONT, text="Perform all\ndances now!", color=0xFFFFFF, x=32, y=15
        )
        splash.append(button_sprite)
        splash.append(description_sprite)
        splash.append(text)
        splash.append(text_description)

    elif button == 8:
        button_sprite = displayio.TileGrid(
            button_bitmap, pixel_shader=button_palette, x=8, y=66)
        description_sprite = displayio.TileGrid(
            description_bitmap, pixel_shader=description_palette, x=28, y=66)

        # set up button and description texts
        text = label.Label(terminalio.FONT, text="8",
                           scale=3, color=0xFFFFFF, x=11, y=90)
        text_description = label.Label(
            terminalio.FONT, text="Play mini\nmovie now!", color=0xFFFFFF, x=32, y=75
        )
        splash.append(button_sprite)
        splash.append(description_sprite)
        splash.append(text)
        splash.append(text_description)

    time.sleep(0.5)
    splash.pop()
    splash.pop()
    splash.pop()
    splash.pop()


def loading(image, dir):
    """
        shows the loading screen before performing dance moves
        PARAM image: 0 or 1, image reference number
        PARAM dir: image directory
    """

    filename = f"{dir}/upload{image}.bmp"
    bitmap, palette = adafruit_imageload.load(
        filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
    splash.append(tile_grid)  # Add the TileGrid to the Group


def loading_movie(image, dir):
    """
        shows the loading screen before playing the mini movie
        PARAM image: image reference number
        PARAM dir: image directory
    """

    filename = f"{dir}/upload ({image}).bmp"
    bitmap, palette = adafruit_imageload.load(
        filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
    splash.append(tile_grid)  # Add the TileGrid to the Group


# define correct center angles:
clegl = 90
clegr = 102
cfootl = 92
cfootr = 94

# ------------SET UP PINS FOR LEGS AND FOOTS----------------------------
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


# reset position fuction
def resetto90():
    while leg_left.angle > clegl + 10:
        leg_left.angle = leg_left.angle - 10
        time.sleep(0.05)
    while leg_left.angle < clegl - 10:
        leg_left.angle = leg_left.angle + 10
        time.sleep(0.05)

    while leg_right.angle > clegr + 10:
        leg_right.angle = leg_right.angle - 10
        time.sleep(0.05)
    while leg_right.angle < clegr - 10:
        leg_right.angle = leg_right.angle + 10
        time.sleep(0.05)

    while foot_left.angle > cfootl + 10:
        foot_left.angle = foot_left.angle - 10
        time.sleep(0.05)
    while foot_left.angle < cfootl - 10:
        foot_left.angle = foot_left.angle + 10
        time.sleep(0.05)

    while foot_right.angle > cfootr + 10:
        foot_right.angle = foot_right.angle - 10
        time.sleep(0.05)
    while foot_right.angle < cfootr - 10:
        foot_right.angle = foot_right.angle + 10
        time.sleep(0.05)

    leg_left.angle = clegl
    leg_right.angle = clegr
    foot_left.angle = cfootl
    foot_right.angle = cfootr


def initial():
    leg_left.angle = clegl
    leg_right.angle = clegr
    foot_left.angle = cfootl
    foot_right.angle = cfootr


# -----------------------SET UP MUSIC PINS-----------------------------------------------
PIEZO_PIN = buzzer.PIEZO_PIN
melody1 = buzzer.melody1
melody2 = buzzer.melody2
tempo = buzzer.tempo
# -----------------------------------MOVE SETS FUNCTIONS----------------------------------
move1 = True
move2 = True
move3 = True
move4 = True
move5 = True
move6 = True


# -----------------------------------MOVE 1---------------------------------------------
def move_set1():
    note = 0
    count = 0
    gc.collect()
    loading(0, "/GIF/gif1/")
    while move1:
        if count != 0:
            note = note + 2
        initial()
        for angle in range(60, 120, 6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note + 2
        gc.collect()
        for angle in range(120, 60, -6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        gc.collect()
        resetto90()
        loading(1, "/GIF/gif1/")
        splash.pop(0)

        # four move
        # (foot: /\,_ _,/\,_ _)
        # (leg: l, mid, r, mid)
        note = note + 2

        for f in range(5):  # 1
            foot_left.angle = foot_left.angle + 5
            foot_right.angle = foot_right.angle - 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle + 10
            leg_right.angle = leg_right.angle + 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        note = note + 2
        for angle in range(5):  # 2
            foot_left.angle = foot_left.angle - 5
            foot_right.angle = foot_right.angle + 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle - 10
            leg_right.angle = leg_right.angle - 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        resetto90()
        note = note + 2
        for f in range(5):  # 3
            foot_left.angle = foot_left.angle + 5
            foot_right.angle = foot_right.angle - 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle - 10
            leg_right.angle = leg_right.angle - 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        note = note + 2
        for angle in range(5):  # 4
            foot_left.angle = foot_left.angle - 5
            foot_right.angle = foot_right.angle + 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle + 10
            leg_right.angle = leg_right.angle + 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        resetto90()

        note = note + 2
        simpleio.tone(PIEZO_PIN, melody1[note], tempo / melody1[note + 1])
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody1[note], tempo / melody1[note + 1])

        loading(0, "/GIF/gif1/")
        splash.pop(0)
        count = count + 1
        gc.collect()

        if count == 3:
            # move1 = False
            break

    gc.collect()
    splash.pop()


# -----------------------------------MOVE 2---------------------------------------------
def move_set2():
    note = 48
    count = 0
    gc.collect()
    loading(1, "/GIF/gif2/")
    while move2:
        initial()
        for angle in range(clegr, clegr - 71, -12):  # turn right leg
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note + 2
        gc.collect()
        for angle in range(clegl, clegl + 71, 12):  # turn left leg
            leg_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        gc.collect()
        for a in range(4):
            note = note + 2
            if count % 2 == 0:
                loading(1, "/GIF/gif2/")
            else:
                loading(2, "/GIF/gif2/")
            splash.pop(0)

            for angle in range(3):  # 90->120
                foot_left.angle = foot_left.angle + 8
                foot_right.angle = foot_right.angle + 8
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            for angle in range(6):  # 120->60
                foot_left.angle = foot_left.angle - 8
                foot_right.angle = foot_right.angle - 8
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            for angle in range(3):  # 60->90
                foot_left.angle = foot_left.angle + 8
                foot_right.angle = foot_right.angle + 8
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)  # not tested
            gc.collect()
            count = count + 1
        gc.collect()
        resetto90()
        simpleio.tone(PIEZO_PIN, melody1[note], 0.5)
        # move2 = False
        break

    gc.collect()
    splash.pop()


# -----------------------------------MOVE 3---------------------------------------------
def move_set3():
    note = 0
    count = 0
    gc.collect()
    loading(0, "GIF/gif3/")
    while move3:
        initial()
        if count == 1:
            note = note + 2
        # right up
        for angle in range(cfootr, cfootr-81, -40):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()
        for angle in range(cfootl, cfootl-61, -20):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()

        #  \\
        simpleio.tone(PIEZO_PIN, melody2[note], 0.25)

        foot_right.angle = cfootr+30  # lift up outward
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        leg_right.angle = clegr-50  # kick
        time.sleep(0.1)
        note = note + 2
        gc.collect()
        loading(1, "GIF/gif3/")
        splash.pop(0)

        for angle in range(clegr-50, clegr+21, 7):  # shake
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        note = note + 2
        gc.collect()
        for angle in range(clegr+20, clegr-51, -7):  # shake
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()
        resetto90()
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        elif count == 1:
            note = note + 2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        gc.collect()
    # --------------------
        loading(0, "GIF/gif3/")
        splash.pop(0)
        # left up
        note = note+2
        gc.collect()
        for angle in range(cfootl, cfootl+81, 40):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()
        for angle in range(cfootr, cfootr+61, 20):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()

        #  //
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[note], 0.25)
        elif count == 1:
            note = note+2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.25)

        foot_left.angle = cfootl-30  # lift up outward
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        leg_left.angle = clegl+50  # kick
        time.sleep(0.1)
        note = note+2
        gc.collect()
        loading(1, "GIF/gif3/")
        splash.pop(0)

        for angle in range(clegl+50, clegl-21, -7):  # shake
            leg_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        note = note+2
        gc.collect()
        for angle in range(clegl-20, clegl+51, 7):  # shake
            leg_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()

        resetto90()
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)

        loading(0, "GIF/gif3/")
        splash.pop(0)
        count = count+1
        gc.collect()
        if count == 2:
            #move3 = False
            break

    gc.collect()
    splash.pop()


# -----------------------------------MOVE 4---------------------------------------------
def move_set4():
    note = 0
    count = 0
    gc.collect()
    loading(0, "/GIF/gif4/")
    while move4:
        initial()
        if count != 0:
            note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        gc.collect()
        note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle + 8
            foot_right.angle = foot_right.angle - 8
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        gc.collect()
        note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4
            if i == 5:
                note = note + 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note + 2
        gc.collect()
        loading(1, "GIF/gif4/")
        splash.pop(0)

        for i in range(20):
            leg_left.angle = leg_left.angle + 2
            foot_left.angle = foot_left.angle - 2
            if i == 10:
                note = note + 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle - 4
            foot_left.angle = foot_left.angle + 4
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle + 4
            foot_left.angle = foot_left.angle - 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        gc.collect()
        loading(0, "GIF/gif4/")
        splash.pop(0)
        resetto90()
        count = count+1
        if count == 3:
            note = note + 2
            for i in range(5):
                leg_left.angle = leg_left.angle + 6
                leg_right.angle = leg_right.angle - 6
                foot_right.angle = foot_right.angle + 6
                foot_left.angle = foot_left.angle - 6
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            note = note + 2
            for i in range(5):
                leg_left.angle = leg_left.angle - 6
                leg_right.angle = leg_right.angle + 6
                foot_right.angle = foot_right.angle - 6
                foot_left.angle = foot_left.angle + 6
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            note = note + 2
            for i in range(10):
                leg_left.angle = leg_left.angle - 4
                leg_right.angle = leg_right.angle - 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            note = note + 2
            gc.collect()
            loading(1, "GIF/gif4/")
            splash.pop(0)
            for i in range(11):
                leg_left.angle = leg_left.angle + 8
                leg_right.angle = leg_right.angle + 8
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            note = note + 2
            for i in range(10):
                leg_left.angle = leg_left.angle - 4
                leg_right.angle = leg_right.angle - 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            loading(0, "GIF/gif4/")
            splash.pop(0)
            note = note + 2
            simpleio.tone(PIEZO_PIN, melody1[note], 1)
            resetto90()

            break

        gc.collect()
    gc.collect()
    splash.pop()

# -----------------------------------MOVE 5---------------------------------------------


def move_set5():
    note = 0
    count = 0
    gc.collect()
    loading(0, "GIF/gif5/")
    while move5:
        initial()
        # slide right
        for a in range(3):

            if count != 0 or a != 0:
                note = note + 2
            for i in range(5):
                foot_left.angle = foot_left.angle + 12  # 抬左
                foot_right.angle = foot_right.angle + 4  # 低右
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            if a == 1:
                note = note + 2
            for i in range(5):
                foot_left.angle = foot_left.angle + 4  # 抬左
                foot_right.angle = foot_right.angle - 12  # 抬右
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            loading(1, "GIF/gif5/")
            splash.pop(0)
            note = note + 2
            for i in range(5):
                foot_left.angle = foot_left.angle - 16
                foot_right.angle = foot_right.angle - 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            if a == 1:
                note = note + 2
            for i in range(5):
                foot_right.angle = foot_right.angle + 12
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            loading(0, "GIF/gif5/")
            splash.pop(0)

        resetto90()

        # slide left

        for a in range(3):

            note = note + 2
            for i in range(5):
                foot_right.angle = foot_right.angle - 12
                foot_left.angle = foot_left.angle - 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            if (count == 0 and a == 1) or (count == 1 and a == 0):
                note = note + 2

            for i in range(5):
                foot_right.angle = foot_right.angle - 4
                foot_left.angle = foot_left.angle + 12
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            loading(1, "GIF/gif5/")
            splash.pop(0)

            if count == 1 and a == 2:
                note = note
            else:
                note = note + 2
            for i in range(5):
                foot_right.angle = foot_right.angle + 16
                foot_left.angle = foot_left.angle + 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            if count == 0 and a == 1:
                note = note + 2
            for i in range(5):
                foot_left.angle = foot_left.angle - 12
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            gc.collect()
            loading(0, "GIF/gif5/")
            gc.collect()
            splash.pop(0)

        resetto90()

        count = count + 1
        if count == 2:
            break

        gc.collect()
    gc.collect()
    splash.pop()


# -----------------------------------MOVE 6---------------------------------------------
def move_set6():
    note = 0
    gc.collect()
    loading(0, "/GIF/gif6/")
    while move6:
        initial()
        # turn left
        time.sleep(0.5)

        for angle in range(cfootr, cfootr-81, -40):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        for angle in range(cfootl, cfootl-60, -20):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()
        #  \\

        simpleio.tone(PIEZO_PIN, melody2[note], 0.1)
        foot_right.angle = cfootr+50  # lift up outward
        simpleio.tone(PIEZO_PIN, melody2[note], 0.1)

        loading(1, "/GIF/gif6/")
        splash.pop(0)
        count = 0
        for i in range(4):
            if i != 0:
                note = note + 2
            for angle in range(clegr-70, clegr+1, 20):  # kick
                leg_right.angle = angle
                simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            if i != 0:
                simpleio.tone(PIEZO_PIN, melody2[note], 0.35)
            note = note + 2
            for angle in range(clegl, 39, -5):  # bend down
                leg_left.angle = angle
                simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            if i == 0 or i == 2:
                note = note + 2
            for angle in range(40, clegl+1, 5):  # get up
                leg_left.angle = angle
                simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            gc.collect()

            if count % 2 == 0:
                loading(0, "/GIF/gif6/")
            else:
                loading(1, "/GIF/gif6/")
            splash.pop(0)
            count = count + 1
            gc.collect()
        resetto90()
        gc.collect()
        # turn right
        time.sleep(0.2)
        note = note + 2
        for angle in range(cfootl, cfootl+81, 40):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        for angle in range(cfootr, cfootr+61, 20):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        gc.collect()
        simpleio.tone(PIEZO_PIN, melody2[note], 0.1)
        foot_left.angle = cfootl-50  # lift up outward
        simpleio.tone(PIEZO_PIN, melody2[note], 0.1)
        gc.collect()
        loading(0, "/GIF/gif6/")
        gc.collect()
        splash.pop(0)
        count = 0
        for i in range(4):
            if i != 0:
                note = note + 2
            for angle in range(clegl+70, clegl-1, -20):  # kick
                leg_left.angle = angle
                simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            if i != 0 and i != 2:
                simpleio.tone(PIEZO_PIN, melody2[note], 0.35)
            elif i == 2:
                simpleio.tone(PIEZO_PIN, melody2[note], 0.1)
                note = note + 2
                simpleio.tone(PIEZO_PIN, melody2[note], 0.25)
            note = note + 2
            for angle in range(clegr, clegr+51, 5):  # bend down
                leg_right.angle = angle
                simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            if i != 3:
                note = note + 2
            for angle in range(clegr+50, clegr-1, -5):  # get up
                leg_right.angle = angle
                simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            gc.collect()

            if count % 2 == 0:
                loading(1, "/GIF/gif6/")
            else:
                loading(0, "/GIF/gif6/")
            splash.pop(0)
            count = count + 1

        gc.collect()
        resetto90()
        break

    gc.collect()
    splash.pop()

# -----------------------------END OF MOVE SETS FUNCTIONS SECTION----------------------------------


# ------------SET UP KEYPAD--------------
# latch_pin = digitalio.DigitalInOut(board.D5) #change to another pin if D5 is not working
# sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

# # Create the pin objects in a list
# pins = [sr.get_pin(n) for n in range(1,8)]

rows = [digitalio.DigitalInOut(x) for x in (board.A2, board.A3, board.A4)]
cols = [digitalio.DigitalInOut(x) for x in (board.TX, board.SCL, board.A5)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
# ---------------------------------------

# ----------------------------HELPER FUNCTIONS----------------------------------------------------
# helper function to perform individual move 3 times


def performing_individual(move):
    # perform 3 times
    for i in range(0, 1, 1):
        if (move == 1):
            move_display("Tip top")
            gc.collect()
            move_set1()
        elif (move == 2):
            move_display("Happy\nwander")
            gc.collect()
            move_set2()
        elif (move == 3):
            move_display("Cute\nkick")
            gc.collect()
            move_set3()
        elif (move == 4):
            move_display("Beat\nwalking")
            gc.collect()
            move_set4()
        elif (move == 5):
            move_display("Slide")
            gc.collect()
            move_set5()
        elif (move == 6):
            move_display("Nodding")
            gc.collect()
            move_set6()
            

# helper function to perform user move sequence

def performing_sequence(move_sequence):
    number_of_move = min(len(move_sequence), 10)
    for i in range(0, number_of_move, 1):
        if (move_sequence[i] == 1):
            move_display("Tip top")
            gc.collect()
            move_set1()
        elif (move_sequence[i] == 2):
            move_display("Happy\nwander")
            gc.collect()
            move_set2()
        elif (move_sequence[i] == 3):
            move_display("Cute\nkick")
            gc.collect()
            move_set3()
        elif (move_sequence[i] == 4):
            move_display("Beat\nwalking")
            gc.collect()
            move_set4()
        elif (move_sequence[i] == 5):
            move_display("Slide")
            gc.collect()
            move_set5()
        elif (move_sequence[i] == 6):
            move_display("Nodding")
            gc.collect()
            move_set6()

# helper function to perform all moves sequentially in the direction specified by user


def performing_all(direction):
    if (direction == 'f'):
        move_set1()
        gc.collect()
        move_set2()
        gc.collect()
        move_set3()
        gc.collect()
        move_set4()
        gc.collect()
        move_set5()
        gc.collect()
        move_set6()
        gc.collect()
    elif (direction == 'r'):
        move_set6()
        move_set5()
        move_set4()
        move_set3()
        move_set2()
        move_set1()

# ----------------------------------------END OF HELPER FUNCTIONS SECTION----------------------------------------------


# -------------------------------------------------------MAIN PROGRAM--------------------------------------------------
# User can choose for the robot to perform either 1 move, a sequence of move (order specified by user) or perfroming all the move sets at once(reverse or forward)
# At main menu on the LCD, press 1 or 2 to choose between perform sequence/individual mode and perform all mode
# Choose 1: navigate to sub menu 1
#    Sub menu 1:
#       - Selecting keys from 1 -> 6 to choose the corresponding move set
#       - Choosing more than once to customize the sequence of move to perform (choose one to perform only one move)
#       - After choosing, presssing key '7' to start performing
#       - Pressing key '9' to go back to main menu
#
# Choose 2: navigate to sub menu 2:
#    Sub menu 2:
#       - Pressing key '7' to perfrom all moves in the forward direction (1 -> 6)
#       - Pressing key '8' to perform all moves in the reverse direction (6 -> 1)
#       - Pressing key '9' to go back to the main menu

# At the main menu, pressing key '9' to turn off the robot


move_sequence = []
main_menu_display()
gc.collect()

while True:
    main_keys = keypad.pressed_keys

    if main_keys:
        time.sleep(0.2)
        # [1] to navigate to the sub menu for user to customize their own move sequence
        if main_keys == [1]:
            gc.collect()
            main_button_active(1)
            gc.collect()
            clear_menu("main_menu")
            gc.collect()
            sub_menu1_display()
            gc.collect()
            # sub menu 1
            while True:
                keys = keypad.pressed_keys
                # waiting for user's inputs
                # user chooses move by selecting 1 -> 6 on key pad
                if keys:
                    time.sleep(0.2)
                    # press 1 -> 6 to select move set
                    if (keys == [1]):
                        gc.collect()
                        sub_button1_active(1)
                        gc.collect()
                        move_sequence.append(1)
                    elif (keys == [2]):
                        gc.collect()
                        sub_button1_active(2)
                        gc.collect()
                        move_sequence.append(2)
                    elif (keys == [3]):
                        gc.collect()
                        sub_button1_active(3)
                        gc.collect()
                        move_sequence.append(3)
                    elif (keys == [4]):
                        gc.collect()
                        sub_button1_active(4)
                        gc.collect()
                        move_sequence.append(4)
                    elif (keys == [5]):
                        gc.collect()
                        sub_button1_active(5)
                        gc.collect()
                        move_sequence.append(5)
                    elif (keys == [6]):
                        gc.collect()
                        sub_button1_active(6)
                        gc.collect()
                        move_sequence.append(6)

                    # press key "7" to start playing
                    elif (keys == [7]):
                        # if only 1 move is chosen, perform it 3 times
                        if (len(move_sequence) == 1):
                            gc.collect()
                            clear_menu("sub_menu1")
                            gc.collect()
                            performing_individual(move_sequence[0])
                            gc.collect()
                        # if more than 1 move are chosen, perform the moves in the order of choosing
                        elif (len(move_sequence) > 1):
                            print("Playing Move Sequence")
                            gc.collect()
                            clear_menu("sub_menu1")
                            gc.collect()
                            performing_sequence(move_sequence)
                            gc.collect()
                        # do nothing if no move are chosen
                        else:
                            print("Nothing to perform")

                        gc.collect()
                        move_sequence.clear()
                        gc.collect()
                        sub_menu1_display()
                        gc.collect()

                    # go back to the main menu by pressing 9
                    elif keys == [9]:
                        print("Terminated")
                        gc.collect()
                        clear_menu("sub_menu1")
                        gc.collect()
                        main_menu_display()
                        gc.collect()
                        break
                    else:
                        gc.collect()
                        error_display()
                        gc.collect()

                    gc.collect()
                gc.collect()
            gc.collect()

        # press [2] to navigate to sub menu 2 on the LCD to go to performing all the moves mode
        elif (main_keys == [2]):
            gc.collect()
            main_button_active(2)
            gc.collect()
            clear_menu("main_menu")
            gc.collect()
            sub_menu2_display()
            gc.collect()
            # sub_menu2
            while True:
                keys = keypad.pressed_keys
                if keys:
                    time.sleep(0.2)
                    if (keys == [7]):
                        gc.collect()
                        sub_button2_active(7)
                        gc.collect()
                        clear_menu("sub_menu2")
                        gc.collect()
                        # perform all the moves in the formward direction (1 -> 6)
                        performing_all('f')
                        gc.collect()
                    elif (keys == [8]):
                        gc.collect()
                        sub_button2_active(8)
                        gc.collect()
                        clear_menu("sub_menu2")
                        gc.collect()
                        loading_movie(0, "/GIF/minimovie/")
                        gc.collect()
                        for i in range(1, 42):
                            loading_movie(i, "/GIF/minimovie/")
                            splash.pop(0)
                            gc.collect()
                        gc.collect()
                        splash.pop()
                    # press 9 to go back to main menu
                    elif keys == [9]:
                        gc.collect()
                        clear_menu("sub_menu2")
                        gc.collect()
                        main_menu_display()
                        gc.collect()
                        break
                    # display error if select other keys
                    else:
                        gc.collect()
                        error_display()
                        gc.collect()

                    gc.collect()
                    sub_menu2_display()
                    gc.collect()
                gc.collect()
            gc.collect()

        # At main menu, press 9 to turn off the robot
        elif main_keys == [9]:
            break

        else:
            gc.collect()
            error_display()
            gc.collect()

        gc.collect()
    gc.collect()

# -------------------------------END OF MAIN PROGRAM---------------------------------------
