import time
import board
import pwmio
# import pulseio
# import simpleio
import digitalio
import adafruit_74hc595
import adafruit_matrixkeypad
from adafruit_motor import servo

from multiprocessing import Process
import Mar6_TCD
import buzzer

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

#-----------------------------------MOVE SETS FUNCTIONS----------------------------------
move1 = False
move2 = False
move3 = False
move4 = False
move5 = False
move6 = False
music = False

count = 0
#-----------------------------------MOVE 1---------------------------------------------
def move1():
    for angle in range(80, 100, 5):
        leg_left.angle = angle
        leg_right.angle = angle
        time.sleep(0.05)
    for angle in range(100, 80, -5):
        leg_left.angle = angle
        leg_right.angle =  angle
        time.sleep(0.05)

    for angle in range(90, 150, 10):
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.1)
    for angle in range(150, 90, -10):
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.1)
    resetto90()
    time.sleep(0.05)
    count=count+1
    if count == 3:
        move1 = False

time.sleep(1)
count = 0

#-----------------------------------MOVE 2---------------------------------------------
def move2():
    resetto90()

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

    for angle in range(32, 102, 3):# shake
        leg_right.angle =  angle
        time.sleep(0.01)
    for angle in range(102, 32, -3):# shake
        leg_right.angle =  angle
        time.sleep(0.01)
    resetto90()
    time.sleep(0.5)

#--------------------

    #left up
    for angle in range(92, 172, 39):
        foot_left.angle = angle
        time.sleep(0.05)
    for angle in range(90, 150, 19):
        foot_right.angle = angle
        time.sleep(0.05)
    #  //

    time.sleep(0.1)
    foot_left.angle = 50 #lift up outward
    time.sleep(1)
    leg_left.angle =  152 #kick
    time.sleep(0.1)

    for angle in range(152, 82, -3):# shake
        leg_left.angle =  angle
        time.sleep(0.01)
    for angle in range(82, 152, 3):# shake
        leg_left.angle =  angle
        time.sleep(0.01)

    resetto90()
    time.sleep(0.5)

    count=count+1
    if count == 3:
        move2 = False

#-----------------------------------MOVE 3---------------------------------------------
def move3():
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


#-----------------------------------MOVE 4---------------------------------------------
def move4():
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
        move4 = False
        resetto90()

#-----------------------------------MOVE 5---------------------------------------------
def move5():
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
    move5 = False

#-----------------------------------MOVE 6---------------------------------------------
def move6():
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

#-----------------------------END OF MOVE SETS FUNCTIONS SECTION----------------------------------

#--------------------------RUN TASKS IN PARALLEL-------------------------------
def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()


#-------------------------------MAIN PROGRAM-----------------------------------

#------------SET UP KEYPAD--------------
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

# options = {1: move1,
#            2: move2,
#            3: move3,
#            4: move4 
#         }
#---------------------------------------

read_input = True
move_sequence =[]
#keeps reading the input until user press key '*'
while read_input:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        if (keys == 1):
            move1 = True
            move_sequence.append("1")
        elif (keys == 2):
            move2 = True
            move_sequence.append("2")
        elif (keys == 3):
            move3 = True
            move_sequence.append("3")
        elif (keys == 4):
            move4 = True
            move_sequence.append("4")
        elif (keys == 5):
            move5 = True
            move_sequence.append("5")
        elif (keys == 6):
            move6 = True
            move_sequence.append("6")
        elif (keys == '*'): 
            read_input = False
    time.sleep(0.1)


# might be an issue: music and TCD is in an infinite while loop
music = Process (target = buzzer.play_music)
display_TCD = Process(target= Mar6_TCD.TCD_display)

music.start()
display_TCD.start()
for move in move_sequence:
    if (move == "1"):
        # run_cpu_tasks_in_parallel(tasks = [move1, buzzer.play_music, Mar6_TCD.display])
        run_cpu_tasks_in_parallel(tasks = [move1])
        print("Finish executing move1, moving on next move")
    elif (move == "2"):
        # run_cpu_tasks_in_parallel(tasks = [move2, buzzer.play_music, Mar6_TCD.display])
        run_cpu_tasks_in_parallel(tasks = [move2])
        print("Finish executing move2, moving on next move")
    elif (move == "3"):
        # run_cpu_tasks_in_parallel(tasks = [move3, buzzer.play_music, Mar6_TCD.display])
        run_cpu_tasks_in_parallel(tasks = [move3])
        print("Finish executing move3, moving on next move")
    elif (move == "4"):
        # run_cpu_tasks_in_parallel(tasks = [move4, buzzer.play_music, Mar6_TCD.display])
        run_cpu_tasks_in_parallel(tasks = [move4])
        print("Finish executing move4, moving on next move")
    elif (move == "5"):
        # run_cpu_tasks_in_parallel(tasks = [move5, buzzer.play_music, Mar6_TCD.display])
        run_cpu_tasks_in_parallel(tasks = [move5])
        print("Finish executing move5, moving on next move")
    elif (move == "6"):
        # run_cpu_tasks_in_parallel(tasks = [move6, buzzer.play_music, Mar6_TCD.display])
        run_cpu_tasks_in_parallel(tasks = [move6])
        print("Finish executing move6, moving on next move")
music.join()
display_TCD.join()
#-------------------------------END OF MAIN PROGRAM---------------------------------------