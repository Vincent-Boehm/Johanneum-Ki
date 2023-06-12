import numpy

import random

class neuron:
    
    def __init__(self) -> None:
        
        self.weights = numpy.random.rand(6)
        print(self.weights)
        self.output = 0
        
    def calc_output(self,inputs):
        self.output =  1/(1+(numpy.exp(-(numpy.dot(inputs,self.weights)))))
        
        