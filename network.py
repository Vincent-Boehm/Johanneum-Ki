import numpy as np

class network:
    def __init__(self) -> None:
        self.layers = 3
        self.fitness = 0
        
        self.neurons
        
        # self.weightsInput = np.random.uniform(-1,1,(180))
        # self.weights1 = np.random.uniform(-1,1,(180))
        # self.weights1 = np.random.uniform(-1,1,(180))
        
        for x in self.layers:
            
        
        pass    
    
    def calculateOutput(self,input:np.ndarray) -> np.ndarray:
        #activationFunction = np.vectorize(lambda x: 1/1 + np.exp(-x))
        
        def activationFunction(x:np.ndarray):
            return (1/(1 + np.exp(-x)))
        
        input = input.flatten()
        
        
        
        
        return outputlayer