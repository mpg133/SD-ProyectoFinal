#!/usr/bin/python3

import requests

import json

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
        response = jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 400

    response = jsonify({'mapa': mapa, 'attrs' : attrsDict, 'visitors': vis_arr})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 201



if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['ENGINE_API_IP'], port=int(config['ENGINE_API_PORT']))
