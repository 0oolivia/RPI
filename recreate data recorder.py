import RPi.GPIO as GPIO
import time
import maestro
import pandas as pd
#assign variables
LED =4
IR =17
#set up diff things
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
polo = maestro.Controller()
polo.setSpeed(0,10)
polo.setAccel(0,4)
start = polo.getPosition(0)

mins = time.time() + 60*10
#i want to make this loop more frequently
#but i need the water reward to be at least 0.5sec
while time.time() < mins:
    if GPIO.input(IR):
        print("hey")
    else:
        polo.setTarget(0,6000)
        time.sleep(.5)
        polo.setTarget(0,992)


