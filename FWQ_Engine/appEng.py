#!/usr/bin/python3

from datetime import datetime
from flask import Flask, jsonify,request
from dotenv import dotenv_values

from map_funcs import getMap

app = Flask(__name__)
users = []

#get all users
@app.route('/map',methods = ['GET'])
def getMapApi():
    try:
        mapa,attrsDict = getMap()
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    return jsonify(mapa), 201


if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['ENGINE_API_IP'], port=int(config['ENGINE_API_PORT']))
