from dataclasses import dataclass
import numpy as np 

class neuron():
    """Basicly this represents a single neuron, wich basicly outputs a vector"""
    def __init__(self,inputs: list, weights: list,bias:float) -> None:
        self.inputs = inputs
        self.weights = weights
        self.output = 0
        self.bias = bias
    
    def calc_Output(self):
        for input,weight in zip(self.inputs,self.weights):
            self.output += input * weight + self.bias
        self.output = 1/(1+pow(2.718281828459045,-self.output))