import maestro
import numpy as np
import time
import pause
chan=2
polo = maestro.Controller()

LED = polo.setTarget(chan,6000)
pause.seconds(3)
LED = polo.setTarget(chan,0000)

polo.close()