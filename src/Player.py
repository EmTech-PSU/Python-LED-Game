
class Player:

    #Constructor includes name, hits, misses, and the average
    def __init__(self, playerName, hits, misses, average):
        self.playerName = playerName
        self.hits = hits
        self.misses = misses
        self.average = getAverage()

    # method for hit & miss percentiale
    def getAverage(self):
        total = self.hits + self.misses
        averageHitPercent  = (total / self.hits)*100
        averageMissPercent = (total / self.misses)*100
        return averageHitPercent, averageMissPercent
        