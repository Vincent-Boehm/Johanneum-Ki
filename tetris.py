import os

import sys

import matplotlib.pyplot as plt

import matplotlib as mpl

#import json

import network

import numpy as np

import jsonpickle

wantedScore = 100

from pyboy import PyBoy,WindowEvent, botsupport

filename = "Tetris.gb"

pyboy = PyBoy(gamerom_file="Tetris.gb",game_wrapper=True,disable_renderer=False)

networkName = "jarvis.json"

tetris = pyboy.game_wrapper()
tetris.start_game()

pyboy.set_emulation_speed(0)

if os.path.exists(networkName) == False:
    testNetwork = network.network(10, 6)
else:
    with open(networkName,"r") as file:
        buffer = file.read()
        testNetwork = jsonpickle.decode(buffer)
        testNetwork = testNetwork[0]
        
fig,ax = plt.subplots()

ticks = 0

iterations_since_boot = 0

while not pyboy.tick():
    ticks += 1
    
    buffer = np.array( tetris.game_area())
    
    buffer = (buffer-np.min(buffer))/(np.max(buffer)-np.min(buffer))
    
    buffer = buffer.flatten()
    
    testNetwork.calcNetworkOutput(buffer)
    
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    
    if testNetwork.output[0]>= 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
        
    if testNetwork.output[1] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        
    if testNetwork.output[2] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
        
    if testNetwork.output[3] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        
    if tetris.game_over():
        testNetwork.fitness = tetris.score + (ticks / 60)
        
        print(testNetwork.fitness)
        
        if os.path.exists(networkName) == False:
            with open(networkName,"w+") as file:
                
                toWrite = []
                toWrite.append(testNetwork)
                file.write(jsonpickle.encode(toWrite))
        else:
            with open(networkName,"r+") as file:
                
                toWrite = jsonpickle.decode(file.read())
                
                toWrite.append(testNetwork)
                
                toWrite.sort(key=lambda x: x.fitness,reverse=True)
                
                file.truncate(0)
                file.seek(0)
                file.write(jsonpickle.encode(toWrite))
                
                testNetwork = toWrite[0]
                print(testNetwork.fitness)
                
                
        testNetwork.train(2)
        
        ticks = 0
        tetris.reset_game(timer_div=0)
        
pyboy.stop()
