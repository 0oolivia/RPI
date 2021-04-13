
import RPi.GPIO as GPIO
import time
LED =4
IR =17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(IR, GPIO.IN)



if GPIO.input(IR):
    print("hey")
else:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)

message = input(" press enter to quit")
GPIO.cleanup()