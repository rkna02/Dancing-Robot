import time
import board

import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

import os 
import adafruit_imageload

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