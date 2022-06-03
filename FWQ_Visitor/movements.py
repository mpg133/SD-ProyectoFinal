#!/usr/bin/python3

from dotenv import dotenv_values
from math import sqrt

import os
import json

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

def getMinTimeAttraction(attrs, lastAt):
    minTime = min(attrs.values())
    for n in attrs.keys():
        if attrs[n] == minTime and int(n) != lastAt:
            val = n
            break
    return val

def getToGo(mapa, attrs, lastAt):
    id_attr = getMinTimeAttraction(attrs, lastAt)
    return id_attr, searchAttrById(mapa, id_attr)


def searchAttrById(mapa, att):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if(str(att) == mapa[i][j]):
                return [i,j]

def neigh(mapa, pos, free):
    free_positions = []
    for i in range(-1,2):
        for j in range(-1,2):
            neigh = [pos[0]+i, pos[1]+j]
            neigh[0] = 19 if neigh[0] < 0 else (0 if neigh[0] > 19 else neigh[0])
            neigh[1] = 19 if neigh[1] < 0 else (0 if neigh[1] > 19 else neigh[1])
                
            if free:
                if((i != 0 or j != 0) and mapa[neigh[0]][neigh[1]] == '0'):
                    free_positions.append([neigh[0],neigh[1]])
            else:
                if((i != 0 or j != 0) and mapa[neigh[0]][neigh[1]] != '0'):
                    free_positions.append([neigh[0],neigh[1]])

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


def enterAttraction(name, attr):
    with open('../FWQ_Sensor/fisic_attractions/attr'+attr+'.json', 'r') as a:
        attr_queue = json.load(a)
    attr_queue[name] = 5
    os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+attr+'.json')
    with open('../FWQ_Sensor/fisic_attractions/attr'+attr+'.json', 'w') as a:
        json.dump(attr_queue, a)

def timePassed(name, attr):
    #print(name + ' in ' + str(attr))
    out = False
    with open('../FWQ_Sensor/fisic_attractions/attr'+str(attr) + '.json', 'r') as a:
        attr_queue = json.load(a)
    if attr_queue[name] <= 0:
        try:
            attr_queue.pop(name)
        except:
            pass
        out = True

        os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+str(attr)+'.json')
        with open('../FWQ_Sensor/fisic_attractions/attr' + str(attr) + '.json', 'w') as a:
            json.dump(attr_queue, a)

    return out
    

def isInAttraction(name):
    path = '../FWQ_Sensor/fisic_attractions/'
    files = os.listdir(path)
    files = [s for s in files if s[0:4] == 'attr']
    for f in files:
        with open(path+f,'r') as jfile:
            attr_queue = json.load(jfile)
            if name in attr_queue.keys():
                id_attr = f[4:]
                id_attr = id_attr[:-5]
                return int(id_attr)
    return -1


def moveAuto(mapa, pos, attrs, name, lastAt):
    if lastAt != -1:
        mapa = mapa.copy()
        attrs = attrs.copy()
        lastAtPos = searchAttrById(mapa, lastAt)
        #print("\nlastAtt: " + str(lastAt))
        #print("lastAtPos: " + str(lastAtPos))
        mapa[lastAtPos[0]][lastAtPos[1]] = 0
        try:
            attrs.pop(lastAt)
        except:
            pass
            
    inAttr = isInAttraction(name)
    if inAttr != -1:
        goOut = timePassed(name, inAttr)
        if not goOut:
            return pos, pos, inAttr

    id_attr, toGo = getToGo(mapa, attrs, lastAt)
    occupied = neigh(mapa, pos, False)
    if toGo in occupied:
        #return pos
        enterAttraction(name, mapa[toGo[0]][toGo[1]])
        return toGo, toGo, mapa[toGo[0]][toGo[1]]

    free = neigh(mapa, pos, True)
    
    # pos[0]<toGo[0] abajo | pos[0]>toGo[0] arriba | pos[1]<toGo[1] derecha | pos[1]>toGo[1] izquierda
    
    newPos = pos
    #print("pos: " + str(pos))
    #print("toGo: " + str(toGo))

    if pos[0] < toGo[0]:
        newPos = xUp(pos)
    elif pos[0] > toGo[0]:
        newPos = xDown(pos)

    if pos[1] < toGo[1]:
        newPos = yUp(newPos)
    elif pos[1] > toGo[1]:
        newPos = yDown(newPos)
        
    return newPos if newPos in free else minDist(free, toGo), toGo, lastAt
