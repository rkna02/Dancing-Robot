"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
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


while True:
    for angle in range(80, 100, 5):  # 0 - 180 degrees, 5 degrees at a time.
        leg_left.angle = angle
        leg_right.angle = angle
        time.sleep(0.05)
    for angle in range(100, 80, -5): # 180 - 0 degrees, 5 degrees at a time.
        leg_left.angle = angle
        leg_right.angle =  angle
        time.sleep(0.05)



    for angle in range(90, 150, 10):  # 0 - 180 degrees, 5 degrees at a time.
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)
    for angle in range(150, 90, -10): # 180 - 0 degrees, 5 degrees at a time.
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)
