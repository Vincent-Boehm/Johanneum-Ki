import numpy

import random

class neuron:
    
    def __init__(self) -> None:
        
        self.weight = random.randrange(0.5,1.5)

        self.bias = random.randrange(-1,1) 

        self.output = 0
        
    def calc_output(self,input):
        self.output =  1/(1+(numpy.exp(self.weight * input + self.bias)))
