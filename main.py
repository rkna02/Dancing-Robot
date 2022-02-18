"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import pulseio
import simpleio
from adafruit_motor import servo

def resetto90():
    leg_left.angle = 90
    leg_right.angle = 90
    foot_left.angle = 90
    foot_right.angle = 90


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


move1 = True
move2 = False
move3 = False
move4 = False
move5 = False
move6 = False

while move1:
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
        time.sleep(0.5)
    for angle in range(150, 90, -10):
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)
    time.sleep(3)
    resetto90()
    time.sleep(0.05)
    move1 = False

move2 = True
while move2:

    for angle in range(90, 50, -10):
        #foot_left.angle = angle
        leg_right.angle = angle
        time.sleep(0.5)



    for angle in range(90, 20, -10):
        #foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)
    for angle in range(150, 90, -60):
        foot_left.angle = angle
        time.sleep(0.5)

    for angle in range(20, 90, 10):
        #foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)

    for angle in range(50, 90, 10):
        #leg_left.angle = angle
        leg_right.angle =  angle
        time.sleep(0.5)
        resetto90()
        time.sleep(1)
        move2= False

# Define pin connected to piezo buzzer.
PIEZO_PIN = board.A1

# Define a list of tones/music notes to play.
TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4


# Main loop will go through each tone in order up and down.
while True:
    # Play tones going from start to end of list.
    for i in range(len(TONE_FREQ)):
        simpleio.tone(PIEZO_PIN, TONE_FREQ[i], duration=0.5)
    # Then play tones going from end to start of list.
    for i in range(len(TONE_FREQ)-1, -1, -1):
        simpleio.tone(PIEZO_PIN, TONE_FREQ[i], duration=0.5)
        time.sleep(1000)
