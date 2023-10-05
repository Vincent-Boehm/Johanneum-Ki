import os

import sys

#import json

import network

import numpy as np

wantedScore = 100

from pyboy import PyBoy,WindowEvent, botsupport

filename = "Tetris.gb"

pyboy = PyBoy(gamerom_file="Tetris.gb",game_wrapper=True)

pyboy.set_emulation_speed(1)

tetris = pyboy.game_wrapper()
tetris.start_game()

testNetwork = network.network(20, 4)

while not pyboy.tick():
    buffer = pyboy.botsupport_manager().screen().screen_ndarray()
    print(buffer)
    testNetwork.calcNetworkOutput(buffer)
    if testNetwork.hiddenLayers[3].output[0] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    if testNetwork.hiddenLayers[3].output[1] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    if testNetwork.hiddenLayers[3].output[2] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    if testNetwork.hiddenLayers[3].output[3] >= 0.5:
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)

error = (tetris.score - wantedScore) ** 2
pyboy.stop()
