import time
import board
import pulseio

#list of tone played, to be added
TONE = [262, #C4 
        294, #D4
        330, #E4
        349, #F4
        392, #G4
        440, #A4
        494] #B4
piezo = pulseio.PWMOut(board.A2, duty_cycle = 2**15, #turn on the piezo 
                    frequency= TONE[0], #start with the first tone 
                    varaibel_frequency = True)

while True:
    for f in TONE:
        piezo.frequency = f
        time.sleep(0.05)
    piezo.duty_cycle = 0 #turn off the piezo