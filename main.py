import time
import board
import pwmio
import pulseio
import simpleio
from adafruit_motor import servo

#define correct center angles:
clegl = 90
clegr = 102
cfootl = 92
cfootr = 90 #not used in moves yet, test later

def resetto90():
    leg_left.angle = clegl
    leg_right.angle = clegr
    foot_left.angle = cfootl
    foot_right.angle = cfootr

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


#dance moves
move1 = False
move2 = False
move3 = False
move4 = True
move5 = False
move6 = False
music = False

count = 0

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

#-------------------------------------------------
count = 0
while move2:
    resetto90()
    
    #right foot up
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
    #left foot up    
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
    
#-------------------------------------------------
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
    
#-------------------------------------------------
count4=0
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
        move4 = False
        resetto90()

#-------------------------------------------------
#muisc

# Define pin connected to piezo buzzer.
PIEZO_PIN = board.A1
PIEZO_PIN = board.A1

#Pachelbel's Canon

NOTE_B0=31
NOTE_C1=33
NOTE_CS1=35
NOTE_D1=37
NOTE_DS1=39
NOTE_E1=41
NOTE_F1=44
NOTE_FS1=46
NOTE_G1=49
NOTE_GS1=52
NOTE_A1=55
NOTE_AS1=58
NOTE_B1=62
NOTE_C2=65
NOTE_CS2=69
NOTE_D2=73
NOTE_DS2=78
NOTE_E2=82
NOTE_F2=87
NOTE_FS2=93
NOTE_G2=98
NOTE_GS2=104
NOTE_A2=110
NOTE_AS2=117
NOTE_B2=123
NOTE_C3=131
NOTE_CS3=139
NOTE_D3=147
NOTE_DS3=156
NOTE_E3=165
NOTE_F3=175
NOTE_FS3=185
NOTE_G3=196
NOTE_GS3=208
NOTE_A3=220
NOTE_AS3=233
NOTE_B3=247
NOTE_C4=262
NOTE_CS4=277
NOTE_D4=294
NOTE_DS4=311
NOTE_E4=330
NOTE_F4=349
NOTE_FS4=370
NOTE_G4=392
NOTE_GS4=415
NOTE_A4=440
NOTE_AS4=466
NOTE_B4=494
NOTE_C5=523
NOTE_CS5=554
NOTE_D5=587
NOTE_DS5=622
NOTE_E5=659
NOTE_F5=698
NOTE_FS5=740
NOTE_G5=784
NOTE_GS5=831
NOTE_A5=880
NOTE_AS5=932
NOTE_B5=988
NOTE_C6=1047
NOTE_CS6=1109
NOTE_D6=1175
NOTE_DS6=1245
NOTE_E6=1319
NOTE_F6=1397
NOTE_FS6=1480
NOTE_G6=1568
NOTE_GS6=1661
NOTE_A6=1760
NOTE_AS6=1865
NOTE_B6=1976
NOTE_C7=2093
NOTE_CS7=2217
NOTE_D7=2349
NOTE_DS7=2489
NOTE_E7=2637
NOTE_F7=2794
NOTE_FS7=2960
NOTE_G7=3136
NOTE_GS7=3322
NOTE_A7=3520
NOTE_AS7=3729
NOTE_B7=3951
NOTE_C8=4186
NOTE_CS8=4435
NOTE_D8=4699
NOTE_DS8=4978
REST=0



# change this to make the song slower or faster
tempo = 200


melody = [NOTE_C5,4,
  NOTE_F5,4, NOTE_F5,8, NOTE_G5,8, NOTE_F5,8, NOTE_E5,8,
  NOTE_D5,4, NOTE_D5,4, NOTE_D5,4,
  NOTE_G5,4, NOTE_G5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
  NOTE_E5,4, NOTE_C5,4, NOTE_C5,4,
  NOTE_A5,4, NOTE_A5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8,
  NOTE_F5,4, NOTE_D5,4, NOTE_C5,8, NOTE_C5,8,
  NOTE_D5,4, NOTE_G5,4, NOTE_E5,4,

  NOTE_F5,2, NOTE_C5,4,
  NOTE_F5,4, NOTE_F5,8, NOTE_G5,8, NOTE_F5,8, NOTE_E5,8,
  NOTE_D5,4, NOTE_D5,4, NOTE_D5,4,
  NOTE_G5,4, NOTE_G5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
  NOTE_E5,4, NOTE_C5,4, NOTE_C5,4,
  NOTE_A5,4, NOTE_A5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8,
  NOTE_F5,4, NOTE_D5,4, NOTE_C5,8, NOTE_C5,8,
  NOTE_D5,4, NOTE_G5,4, NOTE_E5,4,
  NOTE_F5,2, NOTE_C5,4
]

#sizeof gives the number of bytes, each int value is composed of two bytes (16 bits)
#there are two values per note (pitch and duration), so for each note there are four bytes
notes = len(melody)/2

# this calculates the duration of a whole note in ms
wholenote = (60* 4) / tempo

divider = 0
noteDuration = 0
while music:
    time.sleep(1000)
    
    # iterate over the notes of the melody.
    # Remember, the array is twice the number of notes (notes + durations)
    for i in range (0,notes*2,2):

        # calculates the duration of each note
        divider = melody[i + 1]
          # regular note, just proceed
        noteDuration = (wholenote) / divider
      
        #we only play the note for 90% of the duration, leaving 10% as a pause
        simpleio.tone(PIEZO_PIN, melody[i], duration = noteDuration)

         #Wait for the specief duration before playing the next note.
        time.sleep(noteDuration)
