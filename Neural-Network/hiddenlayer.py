import hiddenNeuron

class hiddenlayer():
    """Beschriebt eine "Schicht des Neuralen Netzwerks"
    """
    def __init__(self,depth,neuron_number,weight_list,bias_list) -> None:
        """_summary_

        Args:
            depth (int): Wie "tief" sich diese Schicht befindet, das heißt wie weit es von denn eingangs neuronen entfernt ist.
            neuron_number (int): Wie viele neuronen sich in dieser schicht befinden sollen.
            input_list (list): Liste der Listen für die Eingaben der Neuronen.
            weight_list (list): Liste der Listen für die Eingaben der Gewichtungen.
        """
        self.depth:int = depth
        self.neuron_number:int = neuron_number
        self.neurons = []
        
        self.input_list = []
        
        self.weight_list = weight_list
        self.bias_list = bias_list
        
        
        #Generiert Neuronen
        for number in range(self.neuron_number):
            self.neurons.append(hiddenNeuron.neuron(self.input_list[number],self.weight_list[number],self.bias_list[number]))