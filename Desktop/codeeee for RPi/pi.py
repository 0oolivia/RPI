import maestro
import pause
import numpy as np 
servo= maestro.Controller()
servo.setAccel(0,4)
start = servo.getPosition(0)
cueAB = [4500, 6900]
n = 10

for i in arange(0, n):
    if start == 6900:
        servo.setTarget(0,4500) #4500-6900 are safe so far but scared to go beyond:
        pause.seconds(4)
        servo.setTarget(0,6900)
        servo.setSpeed(0,10)
    else:
        servo.setTarget(0,6900)
        servo.close()
#x = servo.getPosition(1)

