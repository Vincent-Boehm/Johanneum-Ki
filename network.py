import hiddenLayer
import neuron

import numpy

class network:
    def __init__(self,neuronPerLayer,amountOfLayers) -> None:

        self.neuronPerLayer = neuronPerLayer
        self.amountOfLayers = amountOfLayers
        
        self.hiddenLayers = []
        
        self.fitness = 0
        
        self.output = []
        
        self.outputNeuron0 = neuron.neuron()
        self.outputNeuron1 = neuron.neuron()
        self.outputNeuron2 = neuron.neuron()
        self.outputNeuron3 = neuron.neuron()

        #Create Hidden Layers
        for i in range(self.amountOfLayers):
            if i == 0:
                self.hiddenLayers.append(hiddenLayer.layer(self.neuronPerLayer,isInput=True))
            else:
                self.hiddenLayers.append(hiddenLayer.layer(self.neuronPerLayer))

    def calcNetworkOutput(self,screen:numpy.ndarray):
        
        self.output = []
        
        for i in range(len(self.hiddenLayers)):
            if i == 0:
                self.hiddenLayers[i].calc_out(screen)
            else:
                self.hiddenLayers[i].calc_out(inputs=self.hiddenLayers[i-1].output)

        
        self.output.append(self.outputNeuron0.calc_output(self.hiddenLayers[-1].output))
        self.output.append(self.outputNeuron1.calc_output(self.hiddenLayers[-1].output))
        self.output.append(self.outputNeuron2.calc_output(self.hiddenLayers[-1].output))
        self.output.append(self.outputNeuron3.calc_output(self.hiddenLayers[-1].output))
        
        pass
    def train(self,learningrate:float):
        for x in range(len(self.hiddenLayers)):
            self.hiddenLayers[x].train(learningrate)
        pass

