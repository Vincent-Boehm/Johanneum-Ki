import hiddenLayer
import neuron

class network:
    def __init__(self,neuronPerLayer,amountOfLayers) -> None:

        self.neuronPerLayer = neuronPerLayer
        self.amountOfLayers = amountOfLayers
        
        self.hiddenLayers = []
        self.inputLayer = []
        self.outputLayer = []

        # Create Input Layer
        self.inputLayer.append(hiddenLayer.layer(self.neuronPerLayer))

        #Create Hidden Layers
        for i in range(self.amountOfLayers):
            self.hiddenLayers.append(hiddenLayer.layer(self.neuronPerLayer))

    def calcNetworkOutput(self,screen):
        for i in range(len(self.hiddenLayers)):
            if i == 0:
                self.hiddenLayers[i].calc_out(screen)
            self.hiddenLayers[i].calc_out(self.hiddenLayers[i-1].output)
        pass

