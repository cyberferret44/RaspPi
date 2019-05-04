import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for x in range(0, 100) :
    GPIO.setup(18,GPIO.OUT)
    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(18,GPIO.LOW)