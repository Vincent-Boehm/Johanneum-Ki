import sys


class inputLayer():
    def __init__(self) -> None:
        self.outputs = []
    
    def readScreen(self,grid):
        for x in len(grid):
            
            if grid[x][0] >= 1 or grid[x][1] >= 1 or grid[x][2] >= 1:
                self.outputs[x] = 1
            else:
                self.outputs[x] = 0
            
        print(self.outputs)