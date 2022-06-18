#!/usr/bin/python3
from controller import *
from datetime import datetime
from flask import Flask, jsonify,request
from dotenv import dotenv_values


app = Flask(__name__)
users = []

#get all users
@app.route('/user',methods = ['GET'])
def getAllUsers():
    try:
        succes,data=seleccionaTodos()
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    if succes:
        return jsonify(data[0]), 200
    else:
        return jsonify({'ok': False,'msg' : 'Error al seleccionar usuarios'}), 400



#get user
@app.route('/user/<name>', methods=['GET'])
def getUser(name):
    print(name)
    try:
        succes,data=seleccionaUser('name')
    except:
        return jsonify({'ok': False,'msg' : 'Error en el acceso a la base de datos'}), 400

    if succes:
        return jsonify(data[0]), 200
    else:
        return jsonify({'ok': False,'msg' : 'Error al crear el usuario'}), 400


#create user
@app.route('/user',methods=['POST'])
def createUser():
    try:
        succes,data=registra(request.form.get('name'),request.form.get('password'))
    except:
        return jsonify({'ok': False,'msg' : 'Error al crear el usuario'}), 400

    if succes:
        return jsonify({'ok': True,'msg' : 'Usuario creado correctamente'}), 201
    else:
        return jsonify({'ok': False,'msg' : 'Error al crear el usuario'}), 400


#update user
@app.route('/user', methods=['PUT'])
def editUser():
    try:
        succes,data=edita(request.form.get('name'),request.form.get('password'),request.form.get('newName'),request.form.get('newPassword'))
    except:
        return jsonify({'ok': False,'msg' : 'Excepción al editar el usuario'}), 400
    if succes:

        return jsonify({'ok': True,'msg' : 'Usuario editado correctamente'}), 202
    else:
        return jsonify({'ok': False,'msg' : 'Error al editar el usuario'}), 400


@app.route('/user',methods=['DELETE'])
def deleteUser():
    try:
        succes,data=elimina(request.form.get('name'),request.form.get('password'))
    except:
        return jsonify({'ok': False,'msg' : 'Excepción al eliminar el usuario'}), 400

    if succes:
        return jsonify({'ok': True,'msg' : 'Usuario eliminado correctamente'}), 201
    else:
        return jsonify({'ok': False,'msg' : 'Error al eliminar el usuario'}), 400
    


if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['REGISTRY_API_IP'], port=int(config['REGISTRY_API_PORT']))
