#!/usr/bin/python3

from kafka import KafkaConsumer as kc

from dotenv import dotenv_values

import json

from datetime import datetime, timedelta

import todo_pb2
import todo_pb2_grpc


class TodoServicer(todo_pb2_grpc.TodoServicer):
    def requestWaitingTimes(self, request, context):
        global attrs
        response = todo_pb2.WaitingTimes(str(attrs))
        return response


config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT

consumer = kc('SensorsTopic', bootstrap_servers = BROKER)

attrs = {}
start = datetime.now()
end = start


#PONER GRPC A ESCUCHAR AQUI

while True:

    to_del = []
    for a in attrs:
        if attrs[a] == 0:
            to_del.append(a)
    for d in to_del:
        attrs.pop(d)

    msg = json.loads(next(consumer).value.decode('utf-8'))

    attr_id = int(msg['attr'])

    if attr_id in attrs.keys():
        attrs.pop(attr_id)
    
    if msg['people_count'] != 0:
        attrs[attr_id] = msg['people_count'] * 5

    if end - start >= timedelta(seconds=1):
        print(attrs)
        start = datetime.now()
    end = datetime.now()



    