
from shutil import move
import time

import board
import pwmio
import simpleio
import digitalio
import adafruit_matrixkeypad
from adafruit_motor import servo
import buzzer
import Mar6_TCD

#define correct center angles:
clegl = 90
clegr = 102
cfootl = 92
cfootr = 94

#reset position fuction
def resetto90():
    leg_left.angle = 90
    leg_right.angle = 102
    foot_left.angle = 92
    foot_right.angle = 90

#------------SET UP PINS FOR LEGS AND FOOTS----------------------------
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

#-----------------------SET UP MUSIC PINS-----------------------------------------------
PIEZO_PIN = buzzer.PIEZO_PIN
melody1   = buzzer.melody1
melody2   = buzzer.melody2
tempo     = buzzer.tempo
#-----------------------------------MOVE SETS FUNCTIONS----------------------------------
move1 = True
move2 = True
move3 = True
move4 = True
move5 = True
move6 = True

#-----------------------------------MOVE 1---------------------------------------------
def move_set1():
    i = 0
    count = 0
    while move1:
        if count!=0:
            i=i+2
        resetto90()
        for angle in range(60, 120, 6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[i], 0.05)
        i = i+2
        for angle in range(120, 60, -6):
            leg_left.angle = angle
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody1[i], 0.05)
        resetto90()

        t = 0
        for angle in range(90, 150, 6):
            foot_left.angle = angle
            foot_right.angle = 180-angle
            if t < 0.25:
                j = i+2
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
            else:
                j= i+4
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05

        t = 0
        for angle in range(150, 90, -6):
            foot_left.angle = angle
            foot_right.angle = 180-angle

            if t < 0.25:
                j= i+6
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
            else:
                j= i+8
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
        i = j
        resetto90()
        i = i+2
        simpleio.tone(PIEZO_PIN, melody1[i], tempo/melody1[i+1])
        i = i+2
        simpleio.tone(PIEZO_PIN, melody1[i], tempo/melody1[i+1])

        count= count + 1
        if count == 3:
            for a in range(i+2,len(melody1), 2):
                simpleio.tone(PIEZO_PIN, melody1[a], tempo/melody1[a+1])
            break

#-----------------------------------MOVE 2---------------------------------------------
def move_set2():
    i = 0
    count = 0
    while move2:
        resetto90()

        #right up
        for angle in range(cfootr, cfootr-81, -40):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        for angle in range(cfootl, cfootl-61, -20):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        #  \\

        simpleio.tone(PIEZO_PIN, melody2[i], 0.25)
        foot_right.angle = 124 #lift up outward
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        i = i + 2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        leg_right.angle =  32 #kick
        time.sleep(0.1)
        i = i + 2
        for angle in range(32, 93, 6):# shake
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        i = i + 2
        for angle in range(93, 32, -6):# shake
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        resetto90()
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        elif count ==1:
            i = i + 2
            simpleio.tone(PIEZO_PIN, melody2[i], 0.5)

    #--------------------

        #left up
        i = i+2
        for angle in range(cfootl, cfootl+81, 40):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        for angle in range(cfootr, cfootr+61, 20):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
            
        #  //
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[i], 0.25)
        elif count == 1:
            i = i+2
            simpleio.tone(PIEZO_PIN, melody2[i], 0.25)
        foot_left.angle = 50 #lift up outward
        i = i+2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        i = i+2
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)
        leg_left.angle =  143 #kick
        time.sleep(0.1)
        i = i+2
        for angle in range(143, 82, -6):# shake
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)
        i = i+2
        for angle in range(82, 143, 6):# shake
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[i], 0.05)

        resetto90()
        simpleio.tone(PIEZO_PIN, melody2[i], 0.5)

        count=count+1
        if count == 2:
            break

#-----------------------------------MOVE 3---------------------------------------------
def move_set3():
    while move3:
        resetto90()
        for angle in range(102, 41, -4):# turn right leg
            leg_right.angle =  angle
            time.sleep(0.05)
        for angle in range(90, 159, 4):# turn left leg
            leg_left.angle =  angle
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
        break


#-----------------------------------MOVE 4---------------------------------------------
def move_set4():
    while move4:
        resetto90()
        time.sleep(0.5)

        #right up
        for angle in range(90, 10, -39):
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(92, 32, -19):
            foot_left.angle = angle
            time.sleep(0.05)
        #  \\

        time.sleep(0.1)
        foot_right.angle = 120 #lift up outward
        time.sleep(1)
        leg_right.angle =  32 #kick
        time.sleep(0.1)


        for angle in range(90, 30, -3):
            leg_left.angle =  angle
            time.sleep(0.05)
        for angle in range(32, 102, 3):
            leg_right.angle =  angle
            time.sleep(0.05)
        for angle in range(32, 92, 19):
            foot_left.angle = angle
            time.sleep(0.05)
        for angle in range(120, 89, -10):
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(30, 90, 3):
            leg_left.angle =  angle
            time.sleep(0.05)

        count=count+1
        if(count == 2):
            resetto90()
            break

#-----------------------------------MOVE 5---------------------------------------------
def move_set5():
    while move5:
        resetto90()
        # 开合
        for i in range (5):
            for i in range (10):
                leg_left.angle = leg_left.angle + 3
                leg_right.angle = leg_right.angle - 3
                foot_right.angle = foot_right.angle + 3
                foot_left.angle = foot_left.angle - 3
                time.sleep(0.01)
            for i in range (10):
                leg_left.angle = leg_left.angle - 3
                leg_right.angle = leg_right.angle + 3    
                foot_right.angle = foot_right.angle - 3
                foot_left.angle = foot_left.angle + 3
                time.sleep(0.01)
            resetto90()
        #左右
        for i in range (5):
            for i in range (20):
                leg_left.angle = leg_left.angle - 2
                leg_right.angle = leg_right.angle - 2
                time.sleep(0.005)
            for i in range (21):
                leg_left.angle = leg_left.angle + 4
                leg_right.angle = leg_right.angle + 4
                time.sleep(0.01)
            for i in range (20):
                leg_left.angle = leg_left.angle - 2
                leg_right.angle = leg_right.angle - 2
                time.sleep(0.005)
        # move5 = False
        break

#-----------------------------------MOVE 6---------------------------------------------
def move_set6():
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
            foot_left.angle = foot_left.angle -2
        # move6 = False
        break

#-----------------------------END OF MOVE SETS FUNCTIONS SECTION----------------------------------

#------------SET UP KEYPAD--------------
# latch_pin = digitalio.DigitalInOut(board.D5) #change to another pin if D5 is not working
# sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

# # Create the pin objects in a list
# pins = [sr.get_pin(n) for n in range(1,8)] 

cols = [digitalio.DigitalInOut(x) for x in (board.A2, board.A3, board.A4)]
rows = [digitalio.DigitalInOut(x) for x in (board.TX, board.SCL, board.A5)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
#---------------------------------------
def performing_sequence(move_sequence):
    number_of_move = min(len(move_sequence), 10)
    for i in range(0, number_of_move , 1):
        if (move_sequence[i] == 1):
            move_set1()
        elif (move_sequence[i] == 2):
            move_set2()
        elif (move_sequence[i] == 3):
            move_set3()
        elif (move_sequence[i] == 4):
            move_set4()
        elif (move_sequence[i] == 5):
            move_set5()
        elif (move_sequence[i] == 6):
            move_set6()
#-------------------------------MAIN PROGRAM-----------------------------------
read_input = True
move_sequence =[]

Mar6_TCD.main_menu_display()
Mar6_TCD.sub_menu1_display()
Mar6_TCD.sub_menu2_display()
#keeps reading the input until user press key '7'
while True:
    main_keys = keypad.pressed_keys
    Mar6_TCD.display.show(Mar6_TCD.main_menu)

    if main_keys:
        print("Main Key Pressed: ", main_keys)
        Mar6_TCD.display.show(Mar6_TCD.main_menu)

        if main_keys:
            time.sleep(0.2)
            if main_keys == [1]:
                Mar6_TCD.main_button_active(1)
                Mar6_TCD.display.show(Mar6_TCD.sub_menu1)
                    # sub menu 1
                while (True):
                    keys = keypad.pressed_keys
                    if keys:
                        time.sleep(0.2)
                        if (keys == [1]):
                            Mar6_TCD.sub_button1_active(1)
                            move_sequence.append("1")
                        elif (keys == [2]):
                            Mar6_TCD.sub_button1_active(2)
                            move_sequence.append("2")
                        elif (keys == [3]):
                            Mar6_TCD.sub_button1_active(3)
                            move_sequence.append("3")
                        elif (keys == [4]):
                            Mar6_TCD.sub_button1_active(4)
                            move_sequence.append("4")
                        elif (keys == [5]):
                            Mar6_TCD.sub_button1_active(5)
                            move_sequence.append("5")
                        elif (keys == [6]):
                            Mar6_TCD.sub_button1_active(6)
                            move_sequence.append("6")
                        elif (keys == [7]):
                            if (len(move_sequence) >= 1):
                                print("Playing Move Sequence")
                                performing_sequence(move_sequence)
                            else:
                                print("Nothing to perform")
                            move_sequence = {}
                        elif keys == [9]:
                            print("Terminated")
                            break
                        else :
                            print("Invalid Input: CHOOSE 1 -> 6 TO ADD THE MOVES TO THE SEQUENCE, # TO PLAY THE SEQUENCE")
                            Mar6_TCD.error_display(Mar6_TCD.sub_menu1)

            elif (main_keys == [2]):
                Mar6_TCD.main_button_active(2)
                Mar6_TCD.display.show(Mar6_TCD.sub_menu2)
                #sub_menu2
                while True:
                    keys = keypad.pressed_keys
                    if (keys == [7]):
                        Mar6_TCD.sub_button2_active(7)
                        move_set1()
                        move_set2()
                        move_set3()
                        move_set4()
                        move_set5()
                        move_set6()
                    elif (keys == [8]):
                        Mar6_TCD.sub_button2_active(8)
                        move_set6()
                        move_set5()
                        move_set4()
                        move_set3()
                        move_set2()
                        move_set1()

                    elif keys == [9]:
                        break
                    else :
                        print("Invalid Input: CHOOSE 7 OR 8")
                        Mar6_TCD.error_display(Mar6_TCD.sub_menu2)
            elif main_keys == [9]:
                break
            else :
                print ("Invalid Input: CHOOSE 1 OR 2")
                Mar6_TCD.error_display(Mar6_TCD.main_menu)

#-------------------------------END OF MAIN PROGRAM---------------------------------------