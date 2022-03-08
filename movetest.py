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
    while leg_right.angle < clegr-10:
        leg_right.angle = leg_right.angle + 10
        time.sleep(0.05)


    while foot_left.angle > cfootl+10:
        foot_left.angle = foot_left.angle - 10
        time.sleep(0.05)
    while foot_left.angle < cfootl-10:
        foot_left.angle = foot_left.angle + 10
        time.sleep(0.05)

    while foot_right.angle > cfootr+10:
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
        note = note+2
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

        count= count + 1
        if count == 3:
            #move1 = False
            break

#-----------------------------------MOVE 2---------------------------------------------
def move_set2():
    note = 48
    while move2:
        initial()
        for angle in range(102, 41, -12):# turn right leg
            leg_right.angle =  angle
            simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
        note = note +2
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
        if count == 2:
            #move3 = False
            break



#-----------------------------------MOVE 4---------------------------------------------
def move_set4():
    note = 0
    count = 0
    while move4:
        initial()
        if count !=0:
            note = note + 2
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
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        
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
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        note = note + 2
        for i in range(20):
            leg_left.angle = leg_left.angle + 4
            foot_left.angle = foot_left.angle -2
            simpleio.tone(PIEZO_PIN, melody1[note], 0.025)
        
        resetto90()
        count=count+1
        if count == 3:
            note = note + 2
            for i in range (5):
                leg_left.angle = leg_left.angle + 6
                leg_right.angle = leg_right.angle - 6
                foot_right.angle = foot_right.angle + 6
                foot_left.angle = foot_left.angle - 6
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            note = note + 2
            for i in range (5):
                leg_left.angle = leg_left.angle - 6
                leg_right.angle = leg_right.angle + 6    
                foot_right.angle = foot_right.angle - 6
                foot_left.angle = foot_left.angle + 6
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            note = note + 2
            for i in range (10):
                leg_left.angle = leg_left.angle - 4
                leg_right.angle = leg_right.angle - 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            note = note +2    
            for i in range (11):
                leg_left.angle = leg_left.angle + 8
                leg_right.angle = leg_right.angle + 8
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
            note = note +2   
            for i in range (10):
                leg_left.angle = leg_left.angle - 4
                leg_right.angle = leg_right.angle - 4
                simpleio.tone(PIEZO_PIN, melody1[note], 0.05)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            note = note + 2
            simpleio.tone(PIEZO_PIN, melody1[note], 1)
            resetto90()                                                                                                                                               
            
            break

#-----------------------------------MOVE 5---------------------------------------------
def move_set5():
    while move5:
        initial()
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
        for i in range (10):
            for i in range (5):
                foot_left.angle = foot_left.angle + 12 #抬左
                foot_right.angle = foot_right.angle + 4 #低右
            for i in range (5):
                foot_left.angle = foot_left.angle + 4 #抬左
                foot_right.angle = foot_right.angle - 12 #抬右

            for i in range (5):
                foot_left.angle = foot_left.angle - 16
                foot_right.angle = foot_right.angle - 4

            for i in range (5):
                foot_right.angle = foot_right.angle + 12
        time.sleep(0.1)
        resetto90()
        #slide left
        for i in range (10):
            for i in range (5):
                foot_right.angle = foot_right.angle - 12
                foot_left.angle = foot_left.angle - 4

            for i in range (5):
                foot_right.angle = foot_right.angle - 4
                foot_left.angle = foot_left.angle + 12

            for i in range (5):
                foot_right.angle = foot_right.angle + 16
                foot_left.angle = foot_left.angle + 4

            for i in range (5):
                foot_left.angle = foot_left.angle - 12
        break


#-----------------------------------MOVE 6---------------------------------------------
def move_set6():

    while move6:
        initial()
        time.sleep(0.5)

        #turn left

        for angle in range(cfootr, 10, -39):
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(cfootl, 32, -19):
            foot_left.angle = angle
            time.sleep(0.05)
        #  \\

        time.sleep(0.1)
        foot_right.angle = 150 #lift up outward
        time.sleep(1)
        leg_right.angle =  32 #kick
        time.sleep(0.1)
        
        

        for i in range(3):
            for angle in range(32, clegr, 20):
                leg_right.angle =  angle
                time.sleep(0.05)
            for angle in range(clegl, 30, -6):
                leg_left.angle =  angle
                time.sleep(0.05)
            for angle in range(30, 100, 6):
                leg_left.angle =  angle
                time.sleep(0.05)
            time.sleep(0.5)

        for angle in range(150, cfootr-1, -19):
            foot_right.angle = angle
            time.sleep(0.05)
        
        for angle in range(32, cfootl, 8):
            foot_left.angle = angle
            time.sleep(0.05)
        
        
        
        
        # turn opposite
        resetto90()
        time.sleep(1)
        
        for angle in range(cfootl, cfootl+81, 40):
            foot_left.angle = angle
            #simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
        for angle in range(cfootr, cfootr+61, 20):
            foot_right.angle = angle
            
            #simpleio.tone(PIEZO_PIN, melody2[note], 0.05)
            
        

        foot_left.angle = 50 #lift up outward
        time.sleep(1)
        leg_left.angle =  143 #kick
        time.sleep(0.1)
        
        for angle in range(clegr, clegr+61, 3):
            leg_right.angle =  angle
            time.sleep(0.05)
        for angle in range(143, clegr, -3):
            leg_right.angle =  angle
            time.sleep(0.05)
        for angle in range(cfootr+61, cfootr, -19):
            foot_right.angle = angle
            time.sleep(0.05)
        for angle in range(cfootl+81, cfootl-1, -10):
            foot_left.angle = angle
            time.sleep(0.05)
        for angle in range(clegr+61, clegr-1, -3):
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
        elif (keys == [7]):
            move1 = True
            move_set1()
            resetto90()
            move2 = True
            move_set2()
            resetto90()
            move3 = True
            move_set3()
            resetto90()
            move4 = True
            move_set4()
            resetto90()
            move5 = True
            move_set5()
            resetto90()
            move6 = True
            move_set6()
            resetto90()
        elif (keys == [9]):
            print("Terminated")
            break
    time.sleep(0.2)



#-------------------------------END OF MAIN PROGRAM---------------------------------------
