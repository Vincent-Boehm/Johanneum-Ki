import numpy

import random

import math

class neuron:
    
    def __init__(self) -> None:
        
        self.weight = numpy.random.uniform(-2,2,(180))

        self.bias = random.uniform(-10,10)

        self.output = 0
        
    def calc_output(self,input:numpy.ndarray):
        
        self.output =  1/(1 + numpy.exp(-(numpy.dot(input,self.weight))))
