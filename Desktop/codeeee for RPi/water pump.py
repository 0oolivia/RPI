import maestro
#import numpy as np
import time
#with new pololus make sure u go to serial settings, change to dual port, apply, reset
polo = maestro.Controller()
polo.setSpeed(0,9)
polo.setAccel(0,4)
start = polo.getPosition(0)

polo.setTarget(0,6000)
time.sleep(1)
polo.setTarget(0,992)

polo.setTarget(1,6000)
time.sleep(1)
polo.setTarget(1,992)

polo.setTarget(2,6000)
time.sleep(1)
polo.setTarget(2,992)

polo.setTarget(3,6000)
time.sleep(1)
polo.setTarget(3,992)
