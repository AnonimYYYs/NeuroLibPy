from Neuron import Neuron
from Synapse import Synapse

into1 = Synapse()
into2 = Synapse()

IN1 = Neuron(0, "lin")
IN2 = Neuron(0, "lin")

syn11 = Synapse(20)
syn12 = Synapse(-20)
syn21 = Synapse(20)
syn22 = Synapse(-20)

H1 = Neuron(-10)
H2 = Neuron(30)

syn1 = Synapse(20)
syn2 = Synapse(20)

OUT1 = Neuron(-30)

out1 = Synapse()

IN1.addInto(into1)
IN2.addInto(into2)

IN1.addOut(syn11)
IN1.addOut(syn12)
IN2.addOut(syn21)
IN2.addOut(syn22)

H1.addInto(syn11)
H1.addInto(syn21)
H2.addInto(syn12)
H2.addInto(syn22)

H1.addOut(syn1)
H2.addOut(syn2)

OUT1.addInto(syn1)
OUT1.addInto(syn2)

OUT1.addOut(out1)

into1.setValue(1)
into2.setValue(1)

IN1.pushValue()
IN2.pushValue()
H1.pushValue()
H2.pushValue()
OUT1.pushValue()

print(out1.getValue())