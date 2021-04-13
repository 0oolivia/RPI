import RPi.GPIO as GPIO
import time
import maestro
#import pandas as pd
#assign variables
LED =4
IR =17
IR2 =27
#set up diff things
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
polo = maestro.Controller()
polo.setSpeed(0, 10)
polo.setAccel(0,4)
polo.setSpeed(1, 10)
polo.setAccel(1,4)
start = polo.getPosition(0)

bb1= GPIO.input(IR)== False
bb2= GPIO.input(IR2)== False

current=1
prev=0

#beam bre


mins = time.time() + 60*20
#i want to make this loop more frequently
#but i need the water reward to be at least 0.5sec
while time.time() < mins:
    if GPIO.input(IR)== False and prev == 0:
        polo.setTarget(0,6000)
        time.sleep(.5)
        polo.setTarget(0,992)
        prev = 1
        #current = 0
        time.sleep(.01)
        #initiate and only do once
    elif GPIO.input(IR2)== False and prev == 1:
        polo.setTarget(1,6000)
        time.sleep(.5)
        polo.setTarget(1,992)
        prev = 0
        #current = 1
        time.sleep(.01)
    else:
        print("heyo")
        time.sleep(.01)