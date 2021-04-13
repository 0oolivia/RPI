import RPi.GPIO as GPIO
import time
import maestro
#import pandas as pd
#assign variables
LED =4
IR =17  # N BACK L RELAY6 PO2
IR2 =27 # W FRONT L RE5 PO1
IR3 =22 # S FRONT R RELAY 7 PO3
IR4 =5 # E BACK R RE4 PO0 
#set up diff things
GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED,GPIO.OUT)
GPIO.setup(IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
polo = maestro.Controller()
polo.setSpeed(0, 10)
polo.setAccel(0,4)
polo.setSpeed(1, 10)
polo.setAccel(1,4)
polo.setSpeed(2, 10)
polo.setAccel(2,4)
polo.setSpeed(3, 10)
polo.setAccel(3,4)
start = polo.getPosition(0)

#set the start point (idk it's for switching back and forth probably will need to find 
prev=1


mins = time.time() + 60*20
#i want to make this loop more frequently
#but i need the water reward to be at least 0.5sec
while time.time() < mins:
    if (GPIO.input(IR)== False and prev ==1) or (GPIO.input(IR3)== False and prev == 1):
        print("good")
        prev = 0
        time.sleep(1)
    if (GPIO.input(IR2)== False and prev == 0):
        polo.setTarget(1,6000)
        time.sleep(.5)
        polo.setTarget(1,992)
        prev = 1
        time.sleep(.01)
    elif (GPIO.input(IR4)== False and prev == 0):
        polo.setTarget(0,6000)
        time.sleep(.5)
        polo.setTarget(0,992)
        prev = 1
        time.sleep(.01)
    elif (GPIO.input(IR2)== False and prev == 1) or (GPIO.input(IR4)== False and prev == 1):
        print("wrong")
        time.sleep(.01)
    elif (GPIO.input(IR)== False and prev == 0) or (GPIO.input(IR3)==False and prev == 0):
        print("wrong")
        time.sleep(.01)
    #else:
       #print("heyo")
       #time.sleep(.01) 
    



