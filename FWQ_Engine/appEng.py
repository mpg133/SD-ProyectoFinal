#!/usr/bin/python3

import requests

import subprocess

import json

from flask import Flask, jsonify,request
from dotenv import dotenv_values
from grpc_functs import *

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


def getRegistryOk():
    try:
        response = requests.get('http://localhost:5000/ok') 
    except:
        resp = jsonify({'ok':'0'})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp, 200
    
    resp = jsonify({'ok':'1'})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp, 200

def getWTSOk():
    try:
        stub=iniciarGrpcSecure()
        
        msg = todo_pb2.EngineReq()
        response = stub.requestWaitingTimes(msg)
        response = json.loads(response.times_string_dict.replace("'", "\""))
    except:
        resp = jsonify({'ok':'0'})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp, 200
    
    resp = jsonify({'ok':'1'})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp, 200


@app.route('/modules/<module>',methods = ['GET'])
def getModuleStatus(module):

    if module == 'Registry':
        return getRegistryOk()
    elif module == 'Engine':
        resp = jsonify({'ok':'1'})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    elif module == 'WTS':
        return getWTSOk()
    elif module == 'Sensor':

        sensorId = int(request.args['sensorId'])
        try:
            val = str(subprocess.check_output("ps aux | grep 'main.py "+str(sensorId) + "'", shell=True)).split("\\n")[0]
            val = val[-2:]
            val = int(val)
            print("\n\n\n"+'sensorrrrr: ' + str(val))
            if val == int(sensorId):
                resp = jsonify({'ok':'1'})
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp, 200

        except:
            resp = jsonify({'ok':'0'})
            resp.headers.add('Access-Control-Allow-Origin', '*')
            return resp, 200




if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['ENGINE_API_IP'], port=int(config['ENGINE_API_PORT']))
