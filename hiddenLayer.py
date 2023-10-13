import numpy

class layer:
    def __init__(self,size) -> None:
        
        self.output = numpy.empty(1,dtype=numpy.float16)

        self.weights = numpy.random.rand(576)
        
    def calc_out(self,inputs):
        
        print(inputs.shape)

        print("#")

        print(self.weights.shape)
        
        self.output = numpy.inner( inputs , self.weights)



        

            
    def back_prop(self,toChange):
        pass
        ##Todo