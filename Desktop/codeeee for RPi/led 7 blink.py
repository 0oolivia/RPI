import RPi.GPIO as GPIO
import time
LED =4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED, GPIO.LOW)


GPIO.cleanup()
    
    

