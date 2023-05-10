import hiddenlayer

import random

class neural_netwrk():
    def __init__(self,hiddenLayers,hiddenLayerSize,inputLayer,outputLayer,startingInputs,startingWeights) -> None:
        self.hiddenLayers = hiddenLayers
        self.hiddenLayerSize = hiddenLayerSize
        self.inputLayer = inputLayer
        self.outputLayer = outputLayer
        
        self.startingWeights = startingWeights
        self.startingInputs = startingInputs
        
        
        self.layers = []
        for layers in self.hiddenLayers:
            self.layers.append(hiddenlayer.hiddenlayer(layers,self.hiddenLayerSize,self.startingInputs,self.startingWeights,random.randint(10,size=(hiddenLayerSize))))