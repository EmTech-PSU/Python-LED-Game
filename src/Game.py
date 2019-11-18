class Game:
    game_num = 0

    #Constructor includes name, hits, misses, and the average
    def __init__(self, p1Name, p1Hits, p1Misses, p1Average, p2Name, p2Hits, p2Misses, p2Average):
        self.p1Name = p1Name
        self.p1Hits = p1Hits
        self.p1Misses = p1Misses
        self.p1Average = getAverage(self, self.p1Hits, self.p1Misses)
        self.p2Name = p2Name
        self.p2Misses = p2Misses
        self.p2Average = getAverage()
        Game.game_num += 1


    # method for hit & miss percentiale
    def getAverage(self, hits, misses):
        total = hits + misses
        averageHitPercent  = (total / hits)*100
        averageMissPercent = (total / misses)*100
        return averageHitPercent, averageMissPercent