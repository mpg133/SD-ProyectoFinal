#!/usr/bin/python3

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
            
        #select max(id) from attraction order by id

        response = todo_pb2.RegReturns()
        
        try:
            response.ok=True
            response.name=request.name
            response.id="2"
            response.msg="correcto"
            print('Usuario correcto.')

            return response

        except:
            response.ok = False
            response.msg = "ERROR al añadir a " + request.name + " al registro."
            
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
