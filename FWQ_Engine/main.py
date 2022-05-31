import os
import json

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition

import grpc
import concurrent.futures as futures


import todo_pb2
import todo_pb2_grpc


def json_serializer(data):
    return json.dumps(data).encode('utf-8')

config = dotenv_values(".env")

ENGINE_IP = config['ENGINE_IP']
ENGINE_GRPC_IP = config['ENGINE_GRPC_IP']
ENGINE_GRPC_PORT = config['ENGINE_GRPC_PORT']
ENGINE_PORT=config['ENGINE_PORT']
AFORO_MAX=config['AFORO_MAX']
AFORO=0


def main():
    global ENGINE_IP
    global ENGINE_GRPC_IP
    global ENGINE_PORT
    global ENGINE_GRPC_PORT
    global AFORO_MAX
    
    
    print(ENGINE_IP)
    print(ENGINE_GRPC_IP)
    print(ENGINE_PORT)
    print(ENGINE_GRPC_PORT)
    print(AFORO_MAX)
    

main()