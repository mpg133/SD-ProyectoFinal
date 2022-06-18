#!/usr/bin/python3

from controller import *
import hashlib

import sqlite3
import os
import json
import grpc
import time
import concurrent.futures as futures
from dotenv import dotenv_values

import todo_pb2
import todo_pb2_grpc

from datetime import datetime


os.system("./appReg.py &")

def json_serializer(data):
    return json.dumps(data).encode('utf-8')


config = dotenv_values(".env")

REGISTRY_GRPC_PORT = config['REGISTRY_GRPC_PORT']

def logIntoFile(line):
    with open('log.txt', 'a') as logFile:
        logFile.write('\n')
        logFile.write(line)


class TodoServicer(todo_pb2_grpc.TodoServicer):

    def registrarVisitante(self, request, context):
    
        #TODO falta la ip y los parametros/descripcion del evento en los logs

        response = todo_pb2.RegReturns()
        ok, resp = registra(request.name, request.password)
        response.ok = ok
        
        dt = datetime.now()

        if ok:
            response.id = resp[0]
            response.name = resp[1]
            response.msg = "Usuario registrado."
            logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ALTA] via GRPC: "' + resp[1] + '"')
        else:
            response.id="-1"
            response.name="null"
            response.msg = resp[0]
            logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] Error de registro de usuario via GRPC')

        return response


    def editarVisitante(self, request, context):

        #TODO falta la ip y los parametros/descripcion del evento en los logs

        response = todo_pb2.RegReturns()
        ok, resp = edita(request.name, request.password, request.newName, request.newPassword)
        response.ok = ok
        
        dt = datetime.now()

        if ok:
            response.id = resp[0]
            response.name = resp[1]
            response.msg = resp[2]
            logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', MODIFICACION] via GRPC "' + resp[1] + '"')
            print('Usuario "'+request.name+'" editado')
        else:
            response.id = "-1"
            response.name = "null"
            response.msg=resp[0]
            logIntoFile('[' + dt.strftime('%d/%m/%Y, %H:%M:%S') + ', ERROR] Error de modificacion de usuario via GRPC')
            print('Error al editar usuario')

        return response



def main():
    try:
        open('../database.db', 'rb').close()
    except:
        os.system('cd ..; ./db_gen.py')

    global REGISTRY_GRPC_PORT
    global REGISTRY_GRPC_IP
    

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoServicer(), server)
    options = (('grpc.ssl_target_name_override', "cn.from.cert.com",),)
    
    ca_cert = open("client-cert.pem",'rb').read()
    private_key = open("server-key.pem", 'rb').read()
    certificate_chain = open("server-cert.pem", 'rb').read()
    
    credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)],
        root_certificates=ca_cert,
        require_client_auth=True
    )
  
    server.add_secure_port('[::]:' + REGISTRY_GRPC_PORT, credentials)
    server.start()

    print('Starting server. Listening on port ' + REGISTRY_GRPC_PORT)

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        os.system("ps aux | grep appReg.py | awk '{print $2}' | xargs -I{} kill -9 {} 2>/dev/null")
        server.stop(1)
    

    


main()
