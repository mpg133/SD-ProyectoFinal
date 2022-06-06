#!/usr/bin/python3

from kafka import KafkaConsumer as kc

import concurrent.futures as futures
from datetime import datetime, timedelta
from dotenv import dotenv_values

import json

import grpc
import todo_pb2
import todo_pb2_grpc



class TodoServicer(todo_pb2_grpc.TodoServicer):
    def requestWaitingTimes(self, request, context):
        global attrs
        response = todo_pb2.WaitingTimes(times_string_dict=str(attrs))
        return response

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT
GRPC_PORT = config['GRPC_PORT']
TIME_PERSON = config['TIME_PERSON']
TIME_BASE_ATTR = config['TIME_BASE_ATTR']

consumer = kc('SensorsTopic', bootstrap_servers = BROKER)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
todo_pb2_grpc.add_TodoServicer_to_server(TodoServicer(), server)

########
#options = (('grpc.ssl_target_name_override', "cn.from.cert.com",),)

ca_cert = open("client-cert2.pem",'rb').read()
private_key = open("server-key2.pem", 'rb').read()
certificate_chain = open("server-cert2.pem", 'rb').read()

credentials = grpc.ssl_server_credentials(
    [(private_key, certificate_chain)],
    root_certificates=ca_cert,
    require_client_auth=True
)

server.add_secure_port('[::]:' + GRPC_PORT, credentials)
######

server.start()
print('Starting server. Listening on port ' + GRPC_PORT)


attrs = {}
start = datetime.now()
end = start
while True:
    
    to_del = []
    for a in attrs:
        if attrs[a] == 0:
            to_del.append(a)
    for d in to_del:
        attrs.pop(d)

    msg = json.loads(next(consumer).value.decode('utf-8'))

    attr_id = str(msg['attr'])

    if attr_id in attrs.keys():
        attrs.pop(attr_id)
    
    if msg['people_count'] != 0:
        attrs[attr_id] = msg['people_count'] * int(TIME_PERSON) + int(TIME_BASE_ATTR)

    if end - start >= timedelta(seconds=1):
        print(attrs)
        start = datetime.now()
    end = datetime.now()



    