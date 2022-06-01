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

def json_serializer(data):
    return json.dumps(data).encode('utf-8')


config = dotenv_values(".env")

REGISTRY_GRPC_PORT = config['REGISTRY_GRPC_PORT']
REGISTRY_GRPC_IP = config['REGISTRY_GRPC_IP']

class TodoServicer(todo_pb2_grpc.TodoServicer):
    
    def registrarVisitante(self, request, context):
        response = todo_pb2.RegReturns()
        ok, resp = registra(request.name, request.password)
        response.ok = ok
        
        if ok:
            response.id = resp[0]
            response.name = resp[1]
            response.msg = "Usuario registrado."
            print('Usuario "' + request.name + '" registrado.')
        else:
            response.id="-1"
            response.name="null"
            response.msg = resp[0]

        return response


    def editarVisitante(self, request, context):
        response = todo_pb2.RegReturns()
        ok, resp = edita(request.name, request.password, request.newName, request.newPassword)
        response.ok = ok

        if ok:
            response.id = resp[0]
            response.name = resp[1]
            response.msg = resp[2]
            print('Usuario "'+request.name+'" editado.')
        else:
            response.id = "-1"
            response.name = "null"
            response.msg=resp[0]

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
        server.stop(1)
    

    


main()
