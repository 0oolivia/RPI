import maestro
import pause
import numpy as np 
servo= maestro.Controller()
servo.setAccel(0,4)
start = servo.getPosition(0)
cueAB = [4500, 6900]

n = 10
x= np.random.choice([4500,6900], size=n, replace='True')


for i in x:
    servo.setTarget(0, i) #4500-6900 are safe so far but scared to go beyond:
    pause.seconds(2)
    servo.setSpeed(0,10)
    LED = servo.setTarget(2,6000)
    pause.seconds(1)
    LED = servo.setTarget(2,0)
    print(i)
    
servo.close()


