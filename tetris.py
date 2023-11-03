import os

import sys

import matplotlib.pyplot as plt

import matplotlib as mpl

#import json

import network

import numpy as np

import outPutNeuron

wantedScore = 100

from pyboy import PyBoy,WindowEvent, botsupport

filename = "Tetris.gb"

pyboy = PyBoy(gamerom_file="Tetris.gb",game_wrapper=True)


tetris = pyboy.game_wrapper()
tetris.start_game()

pyboy.set_emulation_speed(0)

testNetwork = network.network(5, 3)

while not pyboy.tick():
    
    buffer = np.array( tetris.game_area())
    
    buffer = (buffer-np.min(buffer))/(np.max(buffer)-np.min(buffer))
    
    buffer = buffer.flatten()
    
    testNetwork.calcNetworkOutput(buffer)
    
    print(testNetwork.output)

        
pyboy.stop()
