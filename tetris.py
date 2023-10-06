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

testNetwork = network.network(2304, 4)



# fig, ax = plt.subplots()

    
# plt.show()


# frames = 0


# line1, = ax.plot(0, 0)
while not pyboy.tick():
    
    frames += 1
    
    buffer = pyboy.botsupport_manager().screen().screen_ndarray()
    
    pyboy.set_emulation_speed(3)
    
    buffer = buffer.reshape(buffer.shape[0]*buffer.shape[1],buffer.shape[2])
    
    
    buffer = buffer[1::10]
    
    
    testNetwork.calcNetworkOutput(buffer)
    
    outputRight = outPutNeuron.neuron()
    outputLeft = outPutNeuron.neuron()
    outputDown = outPutNeuron.neuron()
    outputA = outPutNeuron.neuron()
    
    
    outputRight.calc_output(testNetwork.hiddenLayers[-1].output)
    outputLeft.calc_output(testNetwork.hiddenLayers[-1].output)
    outputDown.calc_output(testNetwork.hiddenLayers[-1].output)
    outputA.calc_output(testNetwork.hiddenLayers[-1].output)
    
    # # line1.set_xdata(frames)
    # # line1.set_ydata(outputRight.output.mean())
    # # plt.ion()
    
    # fig.canvas.draw()
    
    
    
    if outputRight.output.mean() > 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    if outputLeft.output.mean() > 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    if outputDown.output.mean() > 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    if outputA.output.mean() > 0.5:
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)

        
pyboy.stop()
