#!/usr/bin/python3

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
        
        try:
            conn = sqlite3.connect('../database.db')
            cur = conn.cursor()

            pass_hash = hashlib.md5(bytes(request.password, encoding="utf8")).hexdigest()
            cur.execute('insert into visitor(name, password) values("' + request.name + '", "'+pass_hash+'")')
            conn.commit()

            cur.execute('select id from visitor where name = "'+request.name+'"')
            id_vis = cur.fetchall()
            id_vis = id_vis[0][0]
            conn.close()

            response.id = str(id_vis)
            response.name=request.name
            response.ok=True
            response.msg="Usuario registrado."

            print('Usuario "' + request.name + '" registrado.')
            
        except:
            response.ok = False
            response.msg = "ERROR al añadir a " + request.name + " al registro."
            
        return response

    def editarVisitante(self, request, context):
        
        response = todo_pb2.RegReturns()

        try:
            conn = sqlite3.connect('../database.db')
            cur = conn.cursor();
    
            #el nuevo nombre ya existe
            cur.execute('select * from visitor where name = "'+request.newName+'"')
            user = cur.fetchall()

            if len(user) >= 1:
                response.ok = False
                response.msg = "ERROR al editar usuario (nuevo nombre ocupado)."
                conn.close()
                return response

            #el usuario a editar no existe
            cur.execute('select * from visitor where name = "'+request.name+'"')
            user = cur.fetchall()
            if len(user) <= 0:
                response.ok = False
                response.msg = "ERROR al editar usuario (credenciales incorrectas)."
                conn.close()
                return response
            

            pass_hash = hashlib.md5(bytes(request.password, encoding="utf8")).hexdigest()
            new_pass_hash = hashlib.md5(bytes(request.newPassword, encoding="utf8")).hexdigest()

            cur.execute('update visitor set name = "'+request.newName+'", password = "'+new_pass_hash+'" where name = "'+request.name+'" and password = "'+pass_hash+'"')
            conn.commit()
            conn.close()

            print('Usuario "'+request.name+'" editado.')

            response.id = str(user[0][0])
            response.name = request.newName
            response.ok = True
            response.msg = "Usuario editado correctamente"

            return response

        except:
            print('mal')
            response.ok = False
            response.msg = "ERROR al editar usuario."

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
