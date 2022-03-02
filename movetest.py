while move3:
  resetto90()
  for angle in range(102, 2, -4):# turn right leg
        leg_right.angle =  angle
        time.sleep(0.05)
  for angle in range(90, 178, 4):# turn left leg
        leg_left.angle =  angle
        time.sleep(0.05)
        
  for angle in range(90, 150, 10):
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)
  for angle in range(150, 90, -10):
        foot_left.angle = angle
        foot_right.angle = 180-angle
        time.sleep(0.5)
        
  resetto90()
