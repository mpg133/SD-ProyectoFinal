#!/usr/bin/python3
from controller import *
from datetime import datetime
from flask import Flask, jsonify,request
from dotenv import dotenv_values

from datetime import datetime



def logIntoFile(line):
    with open('log.txt', 'a') as logFile:
        logFile.write('\n')
        logFile.write(line)



app = Flask(__name__)
users = []

#get all users
@app.route('/user',methods = ['GET'])
def getAllUsers():
    try:
        success,data=seleccionaTodos()
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    if success:
        return jsonify(data[0]), 200
    else:
        return jsonify({'ok': False,'msg' : 'Error al seleccionar usuarios'}), 400



#get user
@app.route('/user/<name>', methods=['GET'])
def getUser(name):
    print(name)
    try:
        success,data=seleccionaUser('name')
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    if success:
        return jsonify(data[0]), 200
    else:
        return jsonify({'ok': False,'msg' : 'Error al crear el usuario'}), 400


#create user
@app.route('/user',methods=['POST'])
def createUser():

    #TODO falta la ip y los parametros/descripcion del evento en los logs
    dt = datetime.now()
    try:
        success,data=registra(request.form.get('name'),request.form.get('password'))
    except:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] '+request.remote_addr+' Error de registro de usuario via API')
        return jsonify({'ok': False,'msg' : 'Error al crear el usuario'}), 400

    if success:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ALTA] '+request.remote_addr+' via API: "' + request.form.get('name') + '"')
        return jsonify({'ok': True,'msg' : 'Usuario creado correctamente'}), 201
    else:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] '+request.remote_addr+' Error de registro de usuario via API')
        return jsonify({'ok': False,'msg' : 'Error al crear el usuario'}), 400


#update user
@app.route('/user', methods=['PUT'])
def editUser():

    #TODO falta la ip y los parametros/descripcion del evento en los logs
    dt = datetime.now()
    try:
        success,data=edita(request.form.get('name'),request.form.get('password'),request.form.get('newName'),request.form.get('newPassword'))
    except:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] '+request.remote_addr+' Error de modificacion de usuario via API')
        return jsonify({'ok': False,'msg' : 'Excepción al editar el usuario'}), 400

    if success:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', MODIFICACION] '+request.remote_addr+' via API: "' + request.form.get('name') + '" to "' + request.form.get('newName') + '"')
        return jsonify({'ok': True,'msg' : 'Usuario editado correctamente'}), 202
    else:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] '+request.remote_addr+' Error de modificacion de usuario via API')
        return jsonify({'ok': False,'msg' : 'Error al editar el usuario'}), 400


@app.route('/user',methods=['DELETE'])
def deleteUser():

    #TODO falta la ip y los parametros/descripcion del evento en los logs
    dt = datetime.now()
    try:
        success,data=elimina(request.form.get('name'),request.form.get('password'))
    except:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] '+request.remote_addr+' Error de eliminación de usuario via API')
        return jsonify({'ok': False,'msg' : 'Excepción al dar de baja el usuario'}), 400

    if success:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', BAJA] '+request.remote_addr+' via API: "' + request.form.get('name') + '"')
        return jsonify({'ok': True,'msg' : 'Usuario dado de baja correctamente'}), 201
    else:
        logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] '+request.remote_addr+' Error de eliminación de usuario via API')
        return jsonify({'ok': False,'msg' : 'Error al dar de baja el usuario'}), 400


if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['REGISTRY_API_IP'], port=int(config['REGISTRY_API_PORT']))
