from math import exp


def linear(x):                                # "lin"
    return x

def sigmoid(x):                               # "sig"
    return 1/(1 + exp(-x))

def giperbolicTan(x):                         # "gtn"
    return (exp(2 * x) - 1) / (exp(2 * x) + 1)



class Neuron:

    def __init__(self, hidden, neuronType = "sig"):
        self.hidden = hidden
        self.neuronType = neuronType
        self.intoSynapses = []
        self.outSynapses = []

    def addInto(self, toAdd):
        self.intoSynapses.append(toAdd)

    def addOut(self, toAdd):
        self.outSynapses.append(toAdd)

    def doCalculate(self, value):
        if(self.neuronType == "sig"):
            return(sigmoid(value))
        elif(self.neuronType == "gtn"):
            return(giperbolicTan(value))
        else:
            return(linear(value))

    def pushValue(self):
        z = 0
        for syn in self.intoSynapses:
            z += syn.getValue()
        z = self.doCalculate(z + self.hidden)
        for syn in self.outSynapses:
            syn.setValue(z)