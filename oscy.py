import maestro
import numpy as np
import time
polo = maestro.Controller()

merp=[]
while GPIO.input(IR):
    merp.append(polo.getPosition(5))
    perp = merp[-20:]
    print(perp)
    time.sleep(0.5)