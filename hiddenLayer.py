import neuron

import numpy

class layer:
    def __init__(self,size,depth,isLast) -> None:
        self.neurons = []
        self.depth = depth
        self.isLast = isLast
        
        self.output = []
        
        for x in range(size):
            self.neurons.append(neuron.neuron())
        
    def calc_out(self,inputs):
        for x in range(len(self.neurons)):
            self.neurons[x].calc_output(inputs)
            self.output.append(self.neurons[x].output)
    
    def back_prop(self,toChange):
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons[i].weights)):
                self.neurons[i].weights[j] *= toChange