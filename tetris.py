import os

import sys

from pyboy import PyBoy, WindowEvent, botsupport

import numpy as np

import network

pyboy = PyBoy(gamerom_file="Tetris.gb",game_wrapper=True)
pyboy.set_emulation_speed(0)

assert pyboy.cartridge_title() == "TETRIS"

tetris = pyboy.game_wrapper()

tetris.start_game(timer_div=0) 

neuralNetwork = network.network()


ticks:int = 0
while not pyboy.tick():
    ticks += 1
    
    #print(np.array(tetris.game_area()))
    
    if ticks % 24:
        gameArea = np.array(tetris.game_area(),dtype=np.uint32)
        
        gameArea = (gameArea-np.min(gameArea))/(np.max(gameArea)-np.min(gameArea))

        
        print(neuralNetwork.calculateOutput(gameArea))
        
        
        pass
    