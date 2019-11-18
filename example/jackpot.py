import RPi.GPIO as GPIO
import time

#pins for lights, this can increase if we add more lights
pinArray = [7,11,12,13,15,16]

#there are two board layout options
# board and BCM, most people use BOARD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#button
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#lights
for i in pinArray:
    GPIO.setup(i, GPIO.OUT)

#state of button
print(GPIO.input(18))




run = True
while(run):
    #button will start with a state of 1 aka True
    #when clicked button will change state to 0 aka False
    if GPIO.input(18) == False:
        print("BUTTON WAS PREESSED")
        for i in pinArray:
            #turn on button wait .2  seconds, turn off button
            #on
            GPIO.output(i, True)
            #wait .2
            time.sleep(.2)
            #turn off btn
            GPIO.output(i, False)
        run = False

#need this at the end of program 
GPIO.cleanup()


