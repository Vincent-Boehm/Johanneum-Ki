import neuron

import numpy

import InputNeuron

class layer:
    def __init__(self,size,isInput=False) -> None:
        self.neurons = []
        
        self.output = []
        if isInput == False:
            for x in range(size):
                self.neurons.append(neuron.neuron())
        else:
            for x in range(size):
                self.neurons.append(InputNeuron.inputneuron())
        
    def calc_out(self,inputs:numpy.ndarray):
        
        inputs.flatten()
        
        self.output = []
        self.output = numpy.array(self.output)
        
        for x in range(0,len(self.neurons)):
            self.output = numpy.append(self.output,self.neurons[x].calc_output(inputs))

        
    def back_prop(self,toChange):
        pass
        ##Todo