#!/usr/bin/python3

from movements import *
import os
import json
import grpc
from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition

import todo_pb2
import todo_pb2_grpc


import concurrent.futures as futures


def json_serializer(data):
    return json.dumps(data).encode('utf-8')

config = dotenv_values(".env")

VISITOR_IP = config['VISITOR_IP']
VISITOR_GRPC_IP = config['VISITOR_GRPC_IP']
VISITOR_GRPC_PORT = config['VISITOR_GRPC_PORT']
VISITOR_PORT=config['VISITOR_PORT']


def registrarVisitante(stub, name, password):
    msg = todo_pb2.RegVis(name=name, password=password)
    response = stub.registrarVisitante(msg)
    return response.id, response.name, response.ok, response.msg

def iniciarGrpcSecure():

        cert = open('client-cert.pem', 'rb').read()
        key = open('client-key.pem','rb').read()
        ca_cert = open('ca.pem','rb').read()
        
        channel_creds = grpc.ssl_channel_credentials(ca_cert,key,cert)


        channel = grpc.secure_channel(VISITOR_GRPC_IP +":"+VISITOR_GRPC_PORT,channel_creds)
        return todo_pb2_grpc.TodoStub(channel)

def main():
    global VISITOR_IP
    global VISITOR_GRPC_IP
    global VISITOR_PORT
    global VISITOR_GRPC_PORT
    
    name = "pepe"
    password = "12345"

    
    stub = iniciarGrpcSecure()
    
    id, name, ok, msg = registrarVisitante(stub, name, password)

    print(id)
    print(msg)

    print(moveNE([19,19]))
    

main()
