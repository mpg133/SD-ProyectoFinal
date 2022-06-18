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
        mapa,attrsDict = getMap()
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    return jsonify({'mapa': mapa, 'attrs' : attrsDict}), 201


@app.route('/weather',methods = ['GET'])
def getWeather():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=48.872636&lon=2.776715&appid='+OPENWEATHER_API_KEY)
    #devuelve la temperatura en ºC:
    # ºK - 273.15 = ºC  
    return str(round(json.loads(response.text)['main']['temp'] - 273.15, 2))


if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['ENGINE_API_IP'], port=int(config['ENGINE_API_PORT']))
