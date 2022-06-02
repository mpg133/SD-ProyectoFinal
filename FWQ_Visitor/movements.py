#!/usr/bin/python3

from dotenv import dotenv_values
from math import sqrt

config = dotenv_values(".env")
MAP_SIZE = int(config['MAP_SIZE'])


def xUp(pos):
    return [pos[0] + 1 if pos[0] < MAP_SIZE - 1 else 0, pos[1]]
def xDown(pos):
    return [pos[0] - 1 if pos[0] > 0 else MAP_SIZE - 1, pos[1]]
def yDown(pos):
    return [pos[0], pos[1] - 1 if pos[1] > 0 else MAP_SIZE - 1]
def yUp(pos):
    return [pos[0], pos[1] + 1 if pos[1] < MAP_SIZE - 1 else 0]

def getMinTimeAttraction(attrs):
    minTime = min(attrs.values())
    for n in attrs.keys():
        if attrs[n] == minTime:
            val = n
            break
    return val

def searchAttrById(mapa, att):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if(att == mapa[i][j]):
                return [i,j]

def neigh(mapa, pos, free):
    free_positions = []
    for i in range(-1,2):
        for j in range(-1,2):
            if free:
                if((i != 0 or j != 0) and mapa[pos[0]+i][pos[1]+j] == '0'):
                    free_positions.append([pos[0]+i,pos[1]+j])
            else:
                if((i != 0 or j != 0) and mapa[pos[0]+i][pos[1]+j] != '0'):
                    free_positions.append([pos[0]+i,pos[1]+j])

    return free_positions

def minDist(positions, target):
    min_dist = [positions[0], 10000000]
    for pos in positions:
        dist = [target[0] - pos[0], target[1] - pos[1]]
        dist = sqrt(dist[0]**2 + dist[1]**2)
        if min_dist[1] > dist:
            min_dist[0] = pos
            min_dist[1] = dist

    return min_dist[0]


def moveAuto(mapa, pos, attrs):
    id_attr = getMinTimeAttraction(attrs)
    toGo = searchAttrById(mapa, id_attr)
    occupied = neigh(mapa, pos, False)
    if toGo in occupied:
        return pos

    free = neigh(mapa, pos, True)
    
    # pos[0]<toGo[0] abajo | pos[0]>toGo[0] arriba | pos[1]<toGo[1] derecha | pos[1]>toGo[1] izquierda
    
    newPos = pos

    if pos[0] < toGo[0]:
        newPos = xUp(pos)
    elif pos[0] > toGo[0]:
        newPos = xDown(pos)

    if pos[1] < toGo[1]:
        newPos = yUp(newPos)
    elif pos[1] > toGo[1]:
        newPos = yDown(newPos)
        
    return newPos if newPos in free else minDist(free, toGo)
