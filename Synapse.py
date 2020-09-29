class Synapse:

    def __init__(self, weight = 1):
        self.value = 0
        self.weight = weight


    def changeWeight(self, weight):
        self.weight = weight

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return (self.value * self.weight)