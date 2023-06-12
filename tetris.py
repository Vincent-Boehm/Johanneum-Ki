import os

import sys

import json

wantedScore = 100

from pyboy import PyBoy,WindowEvent

filename = "Tetris.gb"

pyboy = PyBoy(gamerom_file="Tetris.gb",game_wrapper=True)

pyboy.set_emulation_speed(1)

tetris = pyboy.game_wrapper()
tetris.start_game()

while not pyboy.tick():
    pass

error = (tetris.score - wantedScore) ** 2
pyboy.stop()
