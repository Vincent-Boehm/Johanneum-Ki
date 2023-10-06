import numpy

import random

import math

class neuron:
    
    def __init__(self) -> None:
        
        self.weight = random.uniform(0.5,1.5)

        self.bias = random.uniform(-1,1)

        self.output = 0
        
    def calc_output(self,input):
        self.output = (1/1 + ((self.weight * input + self.bias) ))

    