#!/usr/bin/python3

import requests

import json

from datetime import datetime
from flask import Flask, jsonify,request
from dotenv import dotenv_values

from map_funcs import getMap

app = Flask(__name__)
users = []

config = dotenv_values(".env")

OPENWEATHER_API_KEY = config['OPENWEATHER_API_KEY']

#get all users
@app.route('/map',methods = ['GET'])
def getMapApi():
    try:
        mapa, attrsDict, vis_arr = getMap()
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    return jsonify({'mapa': mapa, 'attrs' : attrsDict, 'visitors': vis_arr}), 201


@app.route('/weather/<ciudad>',methods = ['GET'])
def getWeather(ciudad):
    dic =  {'Madrid': {'lat' : '40.4167047', 'lon' : '-3.7035825' },
            'Toronto':{'lat': '43.6534817' , 'lon': '-79.3839347' },
            'Paris': {'lat': '48.8588897' , 'lon': '2.320041'}, 
            'Oslo': {'lat': '59.9133301', 'lon': '10.7389701' }}
    #`https://api.openweathermap.org/data/2.5/weather?q=${location}&units=imperial&appid=895284fb2d2c50a520ea537456963d9c`

    response= requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+dic[ciudad]['lat']+'&lon='+dic[ciudad]['lon']+'&appid='+OPENWEATHER_API_KEY)
    
    #devuelve la temperatura en ºC:
    # ºK - 273.15 = ºC  
    return str(round(json.loads(response.text)['main']['temp'] - 273.15, 2))
    


if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['ENGINE_API_IP'], port=int(config['ENGINE_API_PORT']))
