from dataclasses import dataclass

class neuron():
    """Ein Neuron, had eine liste von eingaben, und eine liste von gewichten und eine Voreingenommenheit. Dammit rechnen wir dann denn ausgangs wert."""
    def __init__(self,inputs: list, weights: list,bias:float) -> None:
        self.inputs = inputs
        self.weights = weights
        self.output = 0
        self.bias = bias
    
    def calc_Output(self):
        """Matrix Multiplikation, das heist für alle eingabe werte die existieren, rechne Eingabe * Gewichtung + Voreingenommenheit. Dies wird danach in eine sigmoid funktion gebracht(Akitvations Funktion)
        """
        for input,weight in zip(self.inputs,self.weights):
            self.output += input * weight + self.bias
        #Sigmoid Funktion
        self.output = 1/(1+pow(2.718281828459045,-self.output))