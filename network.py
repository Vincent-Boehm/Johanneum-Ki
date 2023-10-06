import hiddenLayer
import neuron

import numpy

class network:
    def __init__(self,neuronPerLayer,amountOfLayers) -> None:

        self.neuronPerLayer = neuronPerLayer
        self.amountOfLayers = amountOfLayers
        
        self.hiddenLayers = []
        self.inputLayer = []
        self.outputLayer = []
        
        self.newBuffer = []

        # Create Input Layer
        self.inputLayer.append(hiddenLayer.layer(self.neuronPerLayer))

        #Create Hidden Layers
        for i in range(self.amountOfLayers):
            self.hiddenLayers.append(hiddenLayer.layer(self.neuronPerLayer))

    def calcNetworkOutput(self,screen):
        self.newBuffer = []
        
        for pixel in screen:
            if numpy.mean(screen[pixel]) > 0:
                self.newBuffer.append(1)
            else:
                self.newBuffer.append(0)
        
        self.newBuffer = numpy.reshape(self.newBuffer,(self.amountOfLayers,-1))
        
        
        for i in range(len(self.hiddenLayers)):
            if i == 0:
                self.hiddenLayers[i].calc_out(inputs=self.newBuffer[i])
            self.hiddenLayers[i].calc_out(inputs=self.hiddenLayers[i-1].output)
        pass

