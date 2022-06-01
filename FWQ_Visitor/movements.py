#!/usr/bin/python3

from dotenv import dotenv_values

config = dotenv_values(".env")
MAP_SIZE = int(config['MAP_SIZE'])


def moveN(pos):
    return [pos[0], pos[1] + 1 if pos[1] < MAP_SIZE - 1 else 0]

def moveS(pos):
    return [pos[0], pos[1] - 1 if pos[1] > 0 else MAP_SIZE - 1]

def moveE(pos):
    return [pos[0] + 1 if pos[0] < MAP_SIZE - 1 else 0, pos[1]]

def moveW(pos):
    return [pos[0] - 1 if pos[0] > 0 else MAP_SIZE - 1, pos[1]]

def moveNW(pos):
    return moveW(moveN(pos))
def moveNE(pos):
    return moveE(moveN(pos))
def moveSW(pos):
    return moveW(moveS(pos))
def moveSE(pos):
    return moveE(moveS(pos))
