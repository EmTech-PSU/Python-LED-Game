import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setwarnings(False)


try:
    for i in range(50):
        GPIO.output(7,True)
        GPIO.output(11,True)
        GPIO.output(12,True)
        GPIO.output(13,True)
        GPIO.output(15,True)
        GPIO.output(16,True)
        time.sleep(1)
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(12,False)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,False)
        time.sleep(1)

finally:
    GPIO.cleanup()
