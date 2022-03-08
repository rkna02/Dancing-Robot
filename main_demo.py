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


#------------SET UP PINS FOR LEGS AND FOOTS----------------------------
# create a PWMOut object on Pin D9-12.
bot_left  = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
bot_right = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
top_left  = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
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
# move1 = True
# move2 = True
# move3 = True
# move4 = True
# move5 = True
# move6 = True

#reset position fuction
def resetto90():
    while leg_left.angle > clegl+10:
        leg_left.angle = leg_left.angle - 10
        time.sleep(0.05)
    while leg_left.angle < clegl-10:
        leg_left.angle = leg_left.angle + 10
        time.sleep(0.05)

    while leg_right.angle > clegr+10:
        leg_right.angle = leg_right.angle - 10
        time.sleep(0.05)
    print(leg_right.angle)
    while leg_right.angle < clegr-10:
        print("hi")
        leg_right.angle = leg_right.angle + 10
        time.sleep(0.05)


    while foot_left.angle > cfootl+10:
        foot_left.angle = foot_left.angle - 10
        time.sleep(0.05)
    while foot_left.angle < cfootl-10:
        foot_left.angle = foot_left.angle + 10
        time.sleep(0.05)

    while foot_right.angle > cfootr + 10:
        foot_right.angle = foot_right.angle - 10
        time.sleep(0.05)
    while foot_right.angle < cfootr-10:
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

#-----------------------------------MOVE 1---------------------------------------------
def move_set1():
    note = 0
    count = 0
    # while move1:
    while (count != 3):
        if count!=0:
            note=note+2
        initial()
        for angle in range(60, 120, 6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note+2
        for angle in range(120, 60, -6):
            leg_left.angle = angle
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        resetto90()
        
        # four move 
        # (foot: /\,_ _,/\,_ _)
        # (leg: l, mid, r, mid)

        note = note + 2
        for f in range(5): #1
            foot_left.angle = foot_left.angle + 5
            foot_right.angle = foot_right.angle - 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle + 10
            leg_right.angle = leg_right.angle + 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)

        note = note+2
        for angle in range(5):#2
            foot_left.angle = foot_left.angle - 5
            foot_right.angle = foot_right.angle + 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle - 10
            leg_right.angle = leg_right.angle - 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)

        resetto90()
        note = note+2
        for f in range(5):#3
            foot_left.angle = foot_left.angle + 5
            foot_right.angle = foot_right.angle - 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle - 10
            leg_right.angle = leg_right.angle - 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)

        note = note+2
        for angle in range(5):#4
            foot_left.angle = foot_left.angle - 5
            foot_right.angle = foot_right.angle + 5
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            leg_left.angle = leg_left.angle + 10
            leg_right.angle = leg_right.angle + 10
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            
        resetto90()
        note = note+2
        simpleio.tone(PIEZO_PIN, melody1[note], tempo/melody1[note+1])
        note = note+2
        simpleio.tone(PIEZO_PIN, melody1[note], tempo/melody1[note+1])

        count = count + 1
        # if count == 3:
        #     break

#-----------------------------------MOVE 2---------------------------------------------
def move_set2():
    note = 48
    # while move2:
    initial()
    for angle in range(102, 41, -12):# turn right leg
        leg_right.angle =  angle
        simpleio.tone(PIEZO_PIN, melody1[note], 0.05)

    note = note +2
    for angle in range(90, 161, 12):# turn left leg
        leg_left.angle =  angle
        simpleio.tone(PIEZO_PIN, melody1[note], 0.05)

    for i in range(4):
        note = note + 2
        for angle in range(90, 110, 10):
            foot_left.angle = angle
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)

        for angle in range(110, 60, -10):
            foot_left.angle = angle
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)

        for angle in range(60, 90, 10):
            foot_left.angle = angle
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
    resetto90()
    simpleio.tone(PIEZO_PIN, melody1[note], 0.5)
    # return

#-----------------------------------MOVE 3---------------------------------------------
def move_set3():
    note = 0
    count = 0
    # while (move3):
    while (count != 2):
        initial()
        if count == 1:
            note = note + 2

        #right up
        for angle in range(cfootr, cfootr-81, -40):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        for angle in range(cfootl, cfootl-61, -20):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        #  \\

        simpleio.tone(PIEZO_PIN, melody2[note], 0.25)
        foot_right.angle = 124 #lift up outward
        note = note + 2

        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        leg_right.angle =  32 #kick
        time.sleep(0.1)

        note = note + 2
        for angle in range(32, 93, 6):# shake
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)

        note = note + 2
        for angle in range(93, 32, -6):# shake
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)

        resetto90()
        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        elif count == 1:
            note = note + 2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.5)

    #--------------------

        #left up
        note = note+2
        for angle in range(cfootl, cfootl+81, 40):
            foot_left.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        for angle in range(cfootr, cfootr+61, 20):
            foot_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)   
        #  //

        if count == 0:
            simpleio.tone(PIEZO_PIN, melody2[note], 0.25)
        elif count == 1:
            note = note+2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.25)

        foot_left.angle = 50 #lift up outward
        note = note+2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)

        note = note+2
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        leg_left.angle =  143 #kick
        time.sleep(0.1)

        note = note+2
        for angle in range(143, 82, -6):# shake
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)

        note = note+2
        for angle in range(82, 143, 6):# shake
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)
        resetto90()

        count=count+1
        # if count == 2:
        #     return


#-----------------------------------MOVE 4---------------------------------------------
def move_set4():
    note = 0
    count = 0
    # while (move4):
    while (count != 3): #perform 2 times
        initial()
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4 
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle + 8
            foot_right.angle = foot_right.angle - 8
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4
            if i == 5:
                note = note + 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        
        note = note + 2        
        for i in range(20):
            leg_left.angle = leg_left.angle + 2
            foot_left.angle = foot_left.angle - 2
            if i == 10:
                note = note + 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle - 4
            foot_left.angle = foot_left.angle + 4
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle + 4
            foot_left.angle = foot_left.angle -2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        
        resetto90()
        count = count+1

    #At the third time
    if count == 3:
        note = note + 2
        for i in range (10):
            leg_left.angle = leg_left.angle + 3
            leg_right.angle = leg_right.angle - 3
            foot_right.angle = foot_right.angle + 3
            foot_left.angle = foot_left.angle - 3
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note + 2
        for i in range (10):
            leg_left.angle = leg_left.angle - 3
            leg_right.angle = leg_right.angle + 3    
            foot_right.angle = foot_right.angle - 3
            foot_left.angle = foot_left.angle + 3
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note + 2
        for i in range (20):
            leg_left.angle = leg_left.angle - 2
            leg_right.angle = leg_right.angle - 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note +2    
        for i in range (21):
            leg_left.angle = leg_left.angle + 4
            leg_right.angle = leg_right.angle + 4
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note +2   
        for i in range (20):
            leg_left.angle = leg_left.angle - 2
            leg_right.angle = leg_right.angle - 2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
            
        note = note + 2
        simpleio.tone(PIEZO_PIN, melody1[note], 1)
        resetto90()

#-----------------------------------MOVE 5---------------------------------------------
def move_set5():
    # while move5:
    resetto90()
    # 开合
    # for i in range (0):
    for i in range (10):
        leg_left.angle = leg_left.angle + 3
        leg_right.angle = leg_right.angle - 3
        foot_right.angle = foot_right.angle + 3
        foot_left.angle = foot_left.angle - 3

    for i in range (10):
        leg_left.angle = leg_left.angle - 3
        leg_right.angle = leg_right.angle + 3    
        foot_right.angle = foot_right.angle - 3
        foot_left.angle = foot_left.angle + 3
    
    resetto90()
    #左右
    # for i in range (0):
    for i in range (20):
        leg_left.angle = leg_left.angle - 2
        leg_right.angle = leg_right.angle - 2
        
    for i in range (21):
        leg_left.angle = leg_left.angle + 4
        leg_right.angle = leg_right.angle + 4
        
    for i in range (20):
        leg_left.angle = leg_left.angle - 2
        leg_right.angle = leg_right.angle - 2
            
    #slide right
    for i in range (3):
        for i in range (10):
            foot_right.angle = foot_right.angle + 2
            foot_left.angle = foot_left.angle + 4
        time.sleep(1)
        for i in range (10):
            foot_right.angle = foot_right.angle - 6
            foot_left.angle = foot_left.angle + 4

        for i in range (10):
            foot_right.angle = foot_right.angle - 2
            foot_left.angle = foot_left.angle - 8

        for i in range (10):
            foot_right.angle = foot_right.angle + 6
    time.sleep(1)
    resetto90()
    #slide left
    for i in range (3):
        for i in range (10):
            foot_right.angle = foot_right.angle - 4
            foot_left.angle = foot_left.angle - 2            
        time.sleep(1)

        for i in range (10):
            foot_right.angle = foot_right.angle - 4
            foot_left.angle = foot_left.angle + 5

        for i in range (10):
            foot_right.angle = foot_right.angle + 8
            foot_left.angle = foot_left.angle + 2

        for i in range (10):
            foot_left.angle = foot_left.angle - 5

#-----------------------------------MOVE 6---------------------------------------------
def move_set6():

    # while move6:
    resetto90()
    time.sleep(0.5)

    #turn lefy
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
    resetto90()
        

#-----------------------------END OF MOVE SETS FUNCTIONS SECTION----------------------------------

#------------SET UP KEYPAD--------------
cols = [digitalio.DigitalInOut(x) for x in (board.A2, board.A3, board.A4)]
rows = [digitalio.DigitalInOut(x) for x in (board.TX, board.SCL, board.A5)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
#----------------------------HELPER FUNCTIONS----------------------------------------------------
#helper function to perform individual move 3 times
def performing_individual(move):
    #perform 3 times
    for i in range(0, 3, 1):
        if (move == 1):
            move_set1()
        elif (move == 2):
            move_set2()
        elif (move == 3):
            move_set3()
        elif (move == 4):
            move_set4()
        elif (move == 5):
            move_set5()
        elif (move == 6):
            move_set6()
#helper function to perform user move sequence
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

#helper function to perform all moves sequentially in the direction specified by user
def performing_all(direction):
    if (direction == 'f'):
        move_set1()
        move_set2()
        move_set3()
        move_set4()
        move_set5()
        move_set6()
    elif (direction == 'r'):
        move_set6()
        move_set5()
        move_set4()
        move_set3()
        move_set2()
        move_set1()
#----------------------------------------END OF HELPER FUNCTIONS SECTION---------------------------------------------- 
#-------------------------------------------------------MAIN PROGRAM--------------------------------------------------
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
Mar6_TCD.main_menu_display()
Mar6_TCD.sub_menu1_display()
Mar6_TCD.sub_menu2_display()
while True:
    main_keys = keypad.pressed_keys
    Mar6_TCD.display.show(Mar6_TCD.main_menu)

    if main_keys:
        print("Main Key Pressed: ", main_keys)
        Mar6_TCD.display.show(Mar6_TCD.main_menu)

        if main_keys:
            time.sleep(0.2)
            # [1] to navigate to the sub menu for user to customize their own move sequence
            if main_keys == [1]:
                Mar6_TCD.main_button_active(1)
                Mar6_TCD.display.show(Mar6_TCD.sub_menu1)

                # sub menu 1
                while (True):
                    keys = keypad.pressed_keys
                    # waiting for user's inputs
                    # user chooses move by selecting 1 -> 6 on key pad
                    if keys:
                        time.sleep(0.2)
                        #press 1 -> 6 to select move set
                        if (keys == [1]):
                            Mar6_TCD.sub_button1_active(1)
                            move_sequence.append(1)
                        elif (keys == [2]):
                            Mar6_TCD.sub_button1_active(2)
                            move_sequence.append(2)
                        elif (keys == [3]):
                            Mar6_TCD.sub_button1_active(3)
                            move_sequence.append(3)
                        elif (keys == [4]):
                            Mar6_TCD.sub_button1_active(4)
                            move_sequence.append(4)
                        elif (keys == [5]):
                            Mar6_TCD.sub_button1_active(5)
                            move_sequence.append(5)
                        elif (keys == [6]):
                            Mar6_TCD.sub_button1_active(6)
                            move_sequence.append(6)

                        # press key "7" to start playing
                        elif (keys == [7]):  
                            # if only 1 move is chosen, perform it 3 times
                            if (len(move_sequence == 1)):
                                performing_individual(move_sequence[0])
                            # if more than 1 move are chosen, perform the moves in the order of choosing
                            elif (len(move_sequence) > 1):
                                print("Playing Move Sequence")
                                performing_sequence(move_sequence)
                            #do nothing if no move are chosen
                            else:
                                print("Nothing to perform")
                            move_sequence.clear()

                        #go back to the main menu by pressing 9
                        elif keys == [9]:
                            print("Terminated")
                            break 
                        else :
                            Mar6_TCD.error_display(Mar6_TCD.sub_menu1)
            
            #press [2] to navigate to sub menu 2 on the LCD to go to performing all the moves mode
            elif (main_keys == [2]):
                Mar6_TCD.main_button_active(2)
                Mar6_TCD.display.show(Mar6_TCD.sub_menu2)
                #sub_menu2
                while True:
                    keys = keypad.pressed_keys
                    if (keys == [7]):
                        Mar6_TCD.sub_button2_active(7)
                        performing_all('f') #perform all the moves in the formward direction (1 -> 6)
                    elif (keys == [8]):
                        Mar6_TCD.sub_button2_active(8)
                        performing_all('r') #perform all the moves in the reverse direction (6 -> 1)
                    #press 9 to go back to main menu
                    elif keys == [9]:
                        break
                    #display error if select other keys
                    else :
                        Mar6_TCD.error_display(Mar6_TCD.sub_menu2)

            #At main menu, press 9 to turn off the robot
            elif main_keys == [9]:
                break

            else :
                Mar6_TCD.error_display(Mar6_TCD.main_menu)
    
#-------------------------------END OF MAIN PROGRAM---------------------------------------