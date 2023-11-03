import numpy

import random

import math

class neuron:
    
    def __init__(self) -> None:
        self.weights = numpy.random.uniform(-2,2,(180))
        
    def calc_output(self,input:numpy.ndarray) -> float:
        input = input.flatten()
        return  1/(1 + math.e ** -(numpy.dot(self.weights,input)))
