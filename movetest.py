import time
import board
import pwmio
# import pulseio
import simpleio
import digitalio
import adafruit_matrixkeypad
from adafruit_motor import servo
import buzzer

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
move1 = False
move2 = False
move3 = False
move4 = False
move5 = False
move6 = False

#-----------------------------------MOVE 1---------------------------------------------
def move_set1():
    note = 0
    count = 0
    while move1:
        if count!=0:
            note=note+2
        resetto90()
        for angle in range(60, 120, 6):
            leg_left.angle = angle
            leg_right.angle = angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        i = i+2
        for angle in range(120, 60, -6):
            leg_left.angle = angle
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        resetto90()

        t = 0
        for angle in range(90, 150, 6):
            foot_left.angle = angle
            foot_right.angle = 180-angle
            if t < 0.25:
                j = note+2
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
            else:
                j= note+4
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05

        t = 0
        for angle in range(150, 90, -6):
            foot_left.angle = angle
            foot_right.angle = 180-angle

            if t < 0.25:
                j= note+6
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
            else:
                j= note+8
                simpleio.tone(PIEZO_PIN, melody1[j], 0.05)
                t = t + 0.05
        i = j
        resetto90()
        i = i+2
        simpleio.tone(PIEZO_PIN, melody1[note], tempo/melody1[note+1])
        i = i+2
        simpleio.tone(PIEZO_PIN, melody1[note], tempo/melody1[note+1])

        count= count + 1
        if count == 3:
            #move1 = False
            break

#-----------------------------------MOVE 2---------------------------------------------
def move_set2():
    note = 48
    while move2:
        resetto90()
        for angle in range(102, 41, -12):# turn right leg
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        i = i +2
        for angle in range(90, 161, 12):# turn left leg
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        for a in range(4):
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
        #move2 = False
        break

#-----------------------------------MOVE 3---------------------------------------------
def move_set3():
    note = 0
    count = 0
    while move3:
        resetto90()
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
        elif count ==1:
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
        i = i+2
        for angle in range(143, 82, -6):# shake
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        note = note+2
        for angle in range(82, 143, 6):# shake
            leg_left.angle =  angle
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)

        resetto90()
        simpleio.tone(PIEZO_PIN, melody2[note], 0.5)

        count=count+1
        if count == 2:
            #move3 = False
            break



#-----------------------------------MOVE 4---------------------------------------------
def move_set4():
    note = 0
    count = 0
    while move4:
        resetto90()
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4 
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle + 8
            foot_right.angle = foot_right.angle - 8
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        note = note + 2
        for i in range(10):
            leg_right.angle = leg_right.angle - 4
            foot_right.angle = foot_right.angle + 4
            if i == 6:
                note = note + 2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        
        note = note + 2        
        for i in range(20):
            leg_left.angle = leg_left.angle + 2
            foot_left.angle = foot_left.angle - 2
            if i == 11:
                note = note + 2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.025)
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle - 4
            foot_left.angle = foot_left.angle + 4
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle + 4
            foot_left.angle = foot_left.angle -2
            simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        
        resetto90()
        count=count+1
        if count == 3:
            note = note + 2
            for i in range (10):
                leg_left.angle = leg_left.angle + 3
                leg_right.angle = leg_right.angle - 3
                foot_right.angle = foot_right.angle + 3
                foot_left.angle = foot_left.angle - 3
                simpleio.tone(PIEZO_PIN, melody2[note], 0.025)
            note = note + 2
            for i in range (10):
                leg_left.angle = leg_left.angle - 3
                leg_right.angle = leg_right.angle + 3    
                foot_right.angle = foot_right.angle - 3
                foot_left.angle = foot_left.angle + 3
                simpleio.tone(PIEZO_PIN, melody2[note], 0.025)
            note = note + 2
            for i in range (20):
                leg_left.angle = leg_left.angle - 2
                leg_right.angle = leg_right.angle - 2
                simpleio.tone(PIEZO_PIN, melody2[note], 0.025)
            note = note +2    
            for i in range (21):
                leg_left.angle = leg_left.angle + 4
                leg_right.angle = leg_right.angle + 4
                simpleio.tone(PIEZO_PIN, melody2[note], 0.025)
            note = note +2   
            for i in range (20):
                leg_left.angle = leg_left.angle - 2
                leg_right.angle = leg_right.angle - 2
                simpleio.tone(PIEZO_PIN, melody2[note], 0.025)
            resetto90()
            note = note + 2
            simpleio.tone(PIEZO_PIN, melody2[note], 1)
            break

#-----------------------------------MOVE 5---------------------------------------------
def move_set5():
    while move5:
        resetto90()
        # 开合
        for i in range (0):
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
        for i in range (0):
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
        break


#-----------------------------------MOVE 6---------------------------------------------
def move_set6():

    while move6:
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
        #move4 = False
        resetto90()
        break

#-----------------------------END OF MOVE SETS FUNCTIONS SECTION----------------------------------

#------------SET UP KEYPAD--------------
# latch_pin = digitalio.DigitalInOut(board.D5) #change to another pin if D5 is not working
# sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

# # Create the pin objects in a list
# pins = [sr.get_pin(n) for n in range(1,8)] 

rows = [digitalio.DigitalInOut(x) for x in (board.A2, board.A3, board.A4)]
cols = [digitalio.DigitalInOut(x) for x in (board.TX, board.SCL, board.A5)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
#---------------------------------------

#-------------------------------MAIN PROGRAM-----------------------------------
# read_input = True
# move_sequence =[]
#keeps reading the input until user press key '*'
while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        if (keys == [1]):
            move1 = True
            move_set1()
            resetto90()
            # move_sequence.append("1")
        elif (keys == [2]):
            move2 = True
            move_set2()
            resetto90()
            # move_sequence.append("2")
        elif (keys == [3]):
            move3 = True
            move_set3()
            resetto90()
            # move_sequence.append("3")
        elif (keys == [4]):
            move4 = True
            move_set4()
            resetto90()
            # move_sequence.append("4")
        elif (keys == [5]):
            move5 = True
            move_set5()
            resetto90()
            # move_sequence.append("5")
        elif (keys == [6]):
            move6 = True
            move_set6()
            resetto90()
            # move_sequence.append("6")
        elif (keys == [9]):
            print("Terminated")
            break
    time.sleep(0.2)



#-------------------------------END OF MAIN PROGRAM---------------------------------------
