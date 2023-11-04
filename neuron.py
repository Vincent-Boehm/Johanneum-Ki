import numpy

import random

import math

class neuron:
    
    def __init__(self) -> None:
        self.weights = numpy.random.uniform(-2,2,(10))
        
        
    def calc_output(self,input:numpy.ndarray) -> float:
        input = input.flatten()
        
        return  numpy.tanh(numpy.dot(input,self.weights))

    def train(self,learningrate):
        
        self.weights = self.weights + (numpy.random.uniform(-0.2,0.2,self.weights.shape) * learningrate)