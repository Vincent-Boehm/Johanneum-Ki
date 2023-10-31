import numpy as np

class network:
    def __init__(self) -> None:
        self.layers = 3
        self.fitness = 0
        
        self.weightsInput = np.random.uniform(-1,1,(10,180))
        self.weights1 = np.random.uniform(-1,1,(10,10))
        self.weights1 = np.random.uniform(-1,1,(10,10))
        
        pass    
    
    def calculateOutput(self,input:np.ndarray) -> np.ndarray:
        #activationFunction = np.vectorize(lambda x: 1/1 + np.exp(-x))
        
        def activationFunction(x:np.ndarray):
            return (1/(1 + np.exp(-x)))
        
        input = input.flatten()
        
        hiddenlayers = np.ndarray(10)
        
        for i in hiddenlayers:
            hiddenlayers[i] = np.dot(input,self.weightsInput[:,i])
        hiddenlayers = activationFunction(hiddenlayers)
        
        for i in hiddenlayers:
            hiddenlayers[i] = np.dot(input,self.weights1[:,i])
        hiddenlayers = activationFunction(hiddenlayers)      
          
        for i in hiddenlayers:
            hiddenlayers[i] = np.dot(input,self.weights2[:,i])
        hiddenlayers = activationFunction(hiddenlayers)
         
        outputlayer = [0,0,0]
        
        outputlayer[0] = activationFunction(outputlayer[0])
        outputlayer[1] = activationFunction(outputlayer[1])
        outputlayer[2] = activationFunction(outputlayer[2])
        
        return outputlayer