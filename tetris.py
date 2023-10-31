import os

import sys

import jsonpickle

from pyboy import PyBoy, WindowEvent, botsupport

import numpy as np

import network

#File name not code name
networkName = "Jarvis.json"

pyboy = PyBoy(gamerom_file="Tetris.gb",game_wrapper=True)
pyboy.set_emulation_speed(0)

assert pyboy.cartridge_title() == "TETRIS"

tetris = pyboy.game_wrapper()

tetris.start_game(timer_div=0) 


# Todo change it to only import the best one from the files and make the network from that
neuralNetwork = network.network()

learningRate = 1


ticks:int = 0

networkResults:np.ndarray = np.ones(3)

networkResults[0] = 0
networkResults[1] = 0
networkResults[2] = 0

while not pyboy.tick():
    ticks += 1
    
    #print(np.array(tetris.game_area()))
    
    if ticks % 24:
        gameArea = np.array(tetris.game_area(),dtype=np.uint32)
        
        gameArea = (gameArea-np.min(gameArea))/(np.max(gameArea)-np.min(gameArea))
        
        networkResults = neuralNetwork.calculateOutput(gameArea)
        
        
        pass
    
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    
    if networkResults[0] > 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    if networkResults[1] > 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    if networkResults[2] > 0.5:
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    
    if tetris.game_over():
        neuralNetwork.fitness = tetris.fitness + tetris.level
        file = jsonpickle.encode(neuralNetwork)
        
        with open(networkName,"w+") as outFile:
            outFile.write(file)
            
            # neuralNetwork.weights1 = neuralNetwork.weights1 +  (np.random.uniform(-1,1,(18,10)) * learningRate)
            # neuralNetwork.weights2 = neuralNetwork.weights2 +  (np.random.uniform(-1,1,(18,10)) * learningRate)
            # neuralNetwork.weights3 = neuralNetwork.weights3 +  (np.random.uniform(-1,1,(18,10)) * learningRate)
            
            # neuralNetwork.outputLayerweights1 = neuralNetwork.outputLayerweights1 +  (np.random.uniform(-1,1,180) * learningRate)
            # neuralNetwork.outputLayerweights2 = neuralNetwork.outputLayerweights2 +  (np.random.uniform(-1,1,180) * learningRate)
            # neuralNetwork.outputLayerweights3 = neuralNetwork.outputLayerweights3 +  (np.random.uniform(-1,1,180) * learningRate)
            tetris.reset_game(timer_div=0)