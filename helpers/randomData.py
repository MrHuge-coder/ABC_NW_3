import random


class RandomData:

    def __init__(self, f, l):
        if f <= l:
            self.first = f
            self.last = l
        else:
            self.first = l
            self.last = f

    def getSimple(self):
        return random.choice(range(1, self.last))

    def get(self):
        return round(random.random()) % (self.last - self.first + 1) + self.first
