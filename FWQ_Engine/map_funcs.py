#!/usr/bin/python3

from time import sleep
import sqlite3
import re
import random

import requests

import json

from dotenv import dotenv_values

config = dotenv_values(".env")
OPENWEATHER_API_KEY = config['OPENWEATHER_API_KEY']

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
    attrs_dict = {}
    for i in attrs:
        attrs_dict[str(i[0])] = {'time':i[1], 'region':i[2], 'status':i[3]}

    cur.execute('select * from visitor')
    attrs = cur.fetchall()
    vis_arr = []
    for i in attrs:
        vis_arr.append({'id':str(i[0]) , 'name' : str(i[1]), 'status' : str(i[3])})

    conn.close()

    return mapa, attrs_dict, vis_arr

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
    if newPos != -1 and int(mapa[newPos[0]][newPos[1]]) < 0:
        return mapa, pos

    if newPos == -1:
        mapa = [[m if m != '-'+str(id_vis) else '0' for m in fila] for fila in mapa]
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

def updateRegion(num):
    
    dic = {'Madrid': {'lat' : '40.4167047', 'lon' : '-3.7035825' }, 'Toronto':{'lat': '43.6534817' , 'lon': '-79.3839347' }, 'Paris': {'lat': '48.8588897' , 'lon': '2.320041'}, 'Oslo': {'lat': '59.9133301', 'lon': '10.7389701' }}
    ciudad = list(dic.keys())[num]

    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+dic[ciudad]['lat']+'&lon='+dic[ciudad]['lon']+'&appid='+OPENWEATHER_API_KEY)
    temp = float(round(json.loads(response.text)['main']['temp'] - 273.15, 2))

    if temp < 20 or temp > 40:
        conn = sqlite3.connect('../database.db')
        cur = conn.cursor()
        cur.execute('update attraction set status = 0 WHERE region = "'+ciudad+'"')
        conn.commit()
        conn.close()





