#!/usr/bin/python3

from dotenv import dotenv_values
from math import sqrt
import random
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
   

    
    attrs=attrs.copy()
    try:
        attrs.pop(lastAt)
    except:
        pass

    keys = list(attrs.keys())
    rand_attr= keys[random.randrange(0,len(keys))]
    while int(attrs[str(rand_attr)]['tiempo']) > 60 or searchAttrById(mapa, rand_attr) == None:
        rand_attr= keys[random.randrange(0,len(keys))]
       
          
    #id_attr = getMinTimeAttraction(attrs, lastAt)
    return int(rand_attr), searchAttrById(mapa, rand_attr)


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
    done = False
    while not done:
        try:
            with open('../FWQ_Sensor/fisic_attractions/attr'+attr+'.json', 'r') as a:
                attr_queue = json.load(a)
            attr_queue[name] = 5
            os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+attr+'.json')
            with open('../FWQ_Sensor/fisic_attractions/attr'+attr+'.json', 'w') as a:
                json.dump(attr_queue, a)
            done=True
        except:
            pass


def timePassed(name, attr):
    out = False
    try:
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
    except:
        pass

    return out

    

def isInAttraction(name):
    done = False
    path = '../FWQ_Sensor/fisic_attractions/'
    files = os.listdir(path)
    files = [s for s in files if s[0:4] == 'attr']
    
    while not done:
        try:
            id_attr = -1
            for f in files:
                with open(path+f,'r') as jfile:
                    attr_queue = json.load(jfile)
                    if name in attr_queue.keys():
                        id_attr = int(f.replace('attr','').replace('.json', ''))
                        break
            done = True
        except:
            pass
    return id_attr


def moveAuto(mapa, pos, attrs, name, lastAt, toGo):
    if lastAt != -1:
        mapa = mapa.copy()
        attrs = attrs.copy()
        lastAtPos = searchAttrById(mapa, lastAt)
        mapa[lastAtPos[0]][lastAtPos[1]] = 0
        try:
            attrs.pop(lastAt)
        except:
            pass
            
    inAttr = isInAttraction(name)
    if int(inAttr) != -1:
        goOut = timePassed(name, inAttr)
        if not goOut:
            return pos, pos, inAttr, toGo
        else:
            
            toGo = -1
    
    if toGo != -1:
        if int(attrs[toGo]['tiempo']) >= 60:
            toGo = -1
        elif int(attrs[toGo]['status']) == 0:
            toGo = -1 
    
    if toGo == -1:
        
        _, toGo = getToGo(mapa, attrs, lastAt)
        #print("entra" + str(toGo))
        
    else:
        toGo=searchAttrById(mapa,toGo)
  
    #print("2: "+str(toGo))
    neight_occupied = neigh(mapa, pos, False)
    if toGo in neight_occupied:
        enterAttraction(name, mapa[toGo[0]][toGo[1]])
        return toGo, toGo, mapa[toGo[0]][toGo[1]], mapa[toGo[0]][toGo[1]]

    free = neigh(mapa, pos, True)
    
    # pos[0]<toGo[0] abajo | pos[0]>toGo[0] arriba | pos[1]<toGo[1] derecha | pos[1]>toGo[1] izquierda
    
    newPos = pos

    xDist = toGo[0] - pos[0]
    if xDist > int(MAP_SIZE/2):
        newPos = xDown(pos)
    elif xDist <= int(MAP_SIZE/2) and xDist > 0:
        newPos = xUp(pos)
    elif xDist > int(-MAP_SIZE/2) and xDist < 0:
        newPos = xDown(pos)
    elif xDist <= int(-MAP_SIZE/2):
        newPos = xUp(pos)


    yDist = toGo[1] - pos[1]
    if yDist > int(MAP_SIZE/2):
        newPos = yDown(newPos)
    elif yDist <= int(MAP_SIZE/2) and yDist > 0:
        newPos = yUp(newPos)
    elif yDist > int(-MAP_SIZE/2) and yDist < 0:
        newPos = yDown(newPos)
    elif yDist <= int(-MAP_SIZE/2):
        newPos = yUp(newPos)
  
    return (newPos if newPos in free else minDist(free, toGo)), toGo, lastAt, mapa[toGo[0]][toGo[1]]
