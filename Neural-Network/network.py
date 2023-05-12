import hiddenLayer

import random

class neuralNetwork():
    def __init__(self,hiddenLayers,hiddenLayerSize,inputLayer,outputLayer) -> None:
        self.hiddenLayers = hiddenLayers
        self.hiddenLayerSize = hiddenLayerSize
        self.inputLayer = inputLayer
        self.outputLayer = outputLayer
        
        
        self.layers = []
        for layers in self.hiddenLayers:
            self.layers.append(hiddenLayer.hiddenlayer(layers,self.hiddenLayerSize,0,random.randint(10,size=(hiddenLayerSize))))