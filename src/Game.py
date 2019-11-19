import RPi.GPIO as GPIO
import time

class Game:
    game_num = 0
    p1LED = 18
    p2LED = 11
    p1Button = 7
    p2Button = 22
    ledArrAsc = [12,13,15,16]
    ledArrDes = [16,15,13,12]
    timeSleep = 1.5

    #setup board, button, and pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for i in ledArrAsc:
        GPIO.setup(i,GPIO.OUT)

    #def getAverage(self, hits, misses):
     #   total = hits + misses
      #  averageHitPercent  = (total / hits)*100
       #return averageHitPercent, averageMissPercent
    
    #Constructor includes name, hits, misses, and the average
    def __init__(self, p1Name, p1Hits, p1Misses, p1Average, p2Name, p2Hits, p2Misses, p2Average):
        self.p1Name = p1Name
        self.p1Hits = p1Hits
        self.p1Misses = p1Misses
       # self.p1Average = getAverage(self, self.p1Hits, self.p1Misses)
        self.p2Name = p2Name
        self.p2Hits = p2Hits
        self.p2Misses = p2Misses
       # self.p2Average = getAverage(self, self.p2Hits, self.p2Misses)
        Game.game_num += 1


   

    def detectHitP1():
        startTime = time.time()
        while (time.time() - startTime) <= timeSleep:
            if (GPIO.input(p1Button) == False):
                p1Hits += 1
                timeSleep = timeSleep * 0.75
            else:
                p1Misses += 1
    
    def detectHitP2():
        startTime = time.time()
        while (time.time() - startTime) <= timeSleep:
            if (GPIO.input(p2Button) == False):
                p2Hits += 1
                timeSleep = timeSleep * 0.75
            else:
                p2Misses += 1
    
    def hasWon():
        if (p1Hits == 10) or (p2Hits == 10):
            return True
        else:
            return False

    
    def runGame():
        while not(hasWon()):
            for i in ledArrAsc:
                GPIO.output(i,True)
                time.sleep(timeSleep)
                GPIO.output(i,False)
            GPIO.output(p1LED,True)
            detectHitP1()
            GPIO.output(p1LED,False)
            for i in ledArrDes:
                GPIO.output(i,True)
                time.sleep(timeSleep)
                GPIO.output(i,False)
            GPIO.output(p2LED,True)
            detectHitP2()
            GPIO.output(p2LED,False)

            

            


