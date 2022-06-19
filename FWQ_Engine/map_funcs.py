#!/usr/bin/python3

import sqlite3
import re
import random

def getMap():
   
    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM map WHERE id = 1')
    query = cur.fetchall()[0][1]
    query = query.split("\n")
    mapa = []
    for i in range(len(query)):
        mapa.append(query[i].split(' '))
        mapa[i] = [m for m in mapa[i] if m != '' ]
    mapa = [m for m in mapa if m != []]
    
    cur.execute('select * from attraction')
    attrs = cur.fetchall()
   
    diccionario = {}

    for i in attrs:
        id = str(i[0])
        tiempo = str(i[1])
        region = str(i[2])
        status = str(i[3])
        diccionario[id] =  {'tiempo': tiempo,'region': region,'status': status}
    #print(str(diccionario))    


    cur.execute('select * from visitor')
    attrs = cur.fetchall()
    vis_arr = []
    for i in attrs:
        vis_arr.append({'id':str(i[0]) , 'name' : str(i[1]), 'status' : str(i[3])})

    conn.close()
    
    return mapa, diccionario, vis_arr

def saveMap(mapa, vis, visStatus):
    string = ''
    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            string += mapa[x][y]+' '
        string += "\n"

    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()
    cur.execute('update map set content ="'+string+'" where id = 1')
    
    if visStatus != None:
        cur.execute('update visitor set status = "'+str(visStatus)+'" where id = '+str(vis))

    conn.commit()
    conn.close()


def updatePosition(mapa, id_vis, pos, newPos):
    
    visStatus = None
    mapa = mapa.copy()
    if newPos != -1 and int(mapa[newPos[0]][newPos[1]]) < 0:
        return mapa, pos

    if newPos == -1:
        mapa = [ m if m != '-'+str(id_vis) else '0' for m in mapa]
        saveMap(mapa, id_vis, 'disconnected')
        return 
        

    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            if mapa[x][y] == "-"+str(id_vis):
                mapa[x][y] = '0'
            if x == newPos[0] and y == newPos[1]:
                if mapa[x][y] == '0':
                    visStatus = "walking"
                    mapa[x][y] = "-"+str(id_vis)
                else:
                    visStatus = str(mapa[x][y])
   
    saveMap(mapa, id_vis, visStatus)
    
    return mapa, newPos

def getRandomEmpty(mapa):
    x = random.randrange(0,19)
    y = random.randrange(0,19)

    while mapa[x][y] != '0':
        x = random.randrange(0,19)
        y = random.randrange(0,19)
        
    return [x,y]
