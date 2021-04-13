import RPi.GPIO as GPIO
import time
import maestro

IR =17  # N BACK L RELAY6 PO2
IR2 =27 # W FRONT L RE5 PO1
IR3 =22 # S FRONT R RELAY 7 PO3
IR4 =5 # E BACK R RE4 PO0

GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED,GPIO.OUT)
GPIO.setup(IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
polo = maestro.Controller()
#1000-4500 are safe so far but scared to go beyond:
polo.setTarget(6,3500)
time.sleep(.5)
polo.setTarget(6,4500)