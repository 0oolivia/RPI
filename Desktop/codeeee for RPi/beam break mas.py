
import RPi.GPIO as GPIO
import time
LED =4
IR =17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def beamb_call(channel):
    if GPIO.input(IR):
        print("hey")
    else:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED, GPIO.LOW)
        print("ho")
        
GPIO.add_event_detect(IR, GPIO.BOTH, callback= beamb_call)

message = input(" press enter to quit")
GPIO.cleanup()