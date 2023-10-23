import numpy as np

class network:
    def __init__(self) -> None:
        self.layers = 5
        
        self.weights1 = np.random.rand(18,10) + 0.5
        self.weights2 = np.random.rand(18,10) + 0.5
        self.weights3 = np.random.rand(18,10) + 0.5
        self.weights4 = np.random.rand(18,10) + 0.5
        self.weights5 = np.random.rand(18,10) + 0.5
        pass    
    
    def calculateOutput(self,input:np.ndarray) -> np.ndarray:
        activationFunction = np.vectorize(lambda x: 1/1-np.e**-x)
        
        
        hiddenlayers = input * self.weights1
        hiddenlayers = activationFunction(hiddenlayers)
        
        hiddenlayers = hiddenlayers * self.weights2
        hiddenlayers = activationFunction(hiddenlayers)
        
        hiddenlayers = hiddenlayers * self.weights3
        hiddenlayers = activationFunction(hiddenlayers)
        
        hiddenlayers = hiddenlayers * self.weights4
        hiddenlayers = activationFunction(hiddenlayers)
        
        hiddenlayers = hiddenlayers * self.weights5
        hiddenlayers = activationFunction(hiddenlayers)
        
        return hiddenlayers