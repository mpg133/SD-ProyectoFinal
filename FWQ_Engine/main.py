#!/usr/bin/python3

import os
import json

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition

from kafka import KafkaProducer as kp


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


def handleVisitante():

    topic = "loginTopic"
    consumer = kc(topic, bootstrap_servers = ENGINE_PORT)
    print("[LOGIN] Awaiting for info on Kafka Server topic = " + topic)

def listenMsg(cons):
    msg = next(cons)
    return msg.value.decode('utf-8')
     

def main():
    global ENGINE_IP
    global ENGINE_GRPC_IP
    global ENGINE_PORT
    global ENGINE_GRPC_PORT
    global AFORO_MAX
    
    
    handleVisitante()

main()
