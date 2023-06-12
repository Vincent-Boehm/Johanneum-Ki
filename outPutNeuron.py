import numpy

import random

class neuron:
    
    def __init__(self) -> None:
        
        self.weight = random.random()
        print(self.weight)
        self.output = 0
        
    def calc_output(self,inputs):
        
        self.output =  1/(1+(numpy.exp(-(numpy.dot(self.weight,inputs)))))
        
        #Output Neuron Only
        self.output = 1/(1+numpy.exp(-numpy.sum(self.output ) / 10))
    