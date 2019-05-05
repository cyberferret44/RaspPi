import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
for x in range(0, 100):
    print("LED 18 on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print("LED 23 on")
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    time.sleep(1)