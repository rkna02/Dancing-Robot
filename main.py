"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D9.
top = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
top1 = servo.Servo(top)

# create a PWMOut object on Pin D10.
foot = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
foot1 = servo.Servo(foot)


while True:
    for angle in range(80, 100, 5):  # 0 - 180 degrees, 5 degrees at a time.
        top1.angle = angle
        time.sleep(0.05)
    for angle in range(100, 80, -5): # 180 - 0 degrees, 5 degrees at a time.
        top1.angle = angle
        time.sleep(0.05)


    for angle in range(70, 120, 10):  # 0 - 180 degrees, 5 degrees at a time.
        foot1.angle = angle
        time.sleep(0.5)
    for angle in range(120, 70, -10): # 180 - 0 degrees, 5 degrees at a time.
        foot1.angle = angle
        time.sleep(0.5)



