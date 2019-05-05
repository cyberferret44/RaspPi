import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
for x in range(0, 100):
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(24,GPIO.LOW)
    time.sleep(1)

    # all on
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    time.sleep(1)