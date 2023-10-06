import neuron

import numpy

class layer:
    def __init__(self,size) -> None:
        self.neurons = []
        
        self.output = numpy.empty(1)
        
        for x in range(size):
            self.neurons.append(neuron.neuron())
        
    def calc_out(self,inputs):
        
        inputs = numpy.reshape(inputs,(1,-1))
        
        self.output = numpy.empty(1,dtype=numpy.float16)
        
        for x in range(0,len(self.neurons)):
            self.neurons[x].calc_output(1)
            self.output = numpy.append(self.output,self.neurons[x].output,axis=None)
            
    def back_prop(self,toChange):
        pass
        ##Todo