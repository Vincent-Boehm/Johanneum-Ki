import neuron

import numpy

class layer:
    def __init__(self,size) -> None:
        self.neurons = []
        
        self.output = numpy.empty(1)
        
        for x in range(size):
            self.neurons.append(neuron.neuron())
        
    def calc_out(self,inputs):
        
        inputs.flatten()
        
        self.output = numpy.empty(1,dtype=numpy.float16)
        
        for x in range(0,len(self.neurons)):
            numpy.append(self.output,self.neurons[x].calc_output(inputs))

    def back_prop(self,toChange):
        pass
        ##Todo