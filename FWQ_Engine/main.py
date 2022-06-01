#!/usr/bin/python3

import os
import json

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition

from kafka import KafkaProducer as kp
from login import *

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
GRPC_WTS_IP = config['GRPC_WTS_IP']
GRPC_WTS_PORT = config['GRPC_WTS_PORT']

AFORO_MAX=config['AFORO_MAX']
AFORO=0


def loginConsumer():
    topic = "loginTopic"
    consumer = kc(topic, bootstrap_servers = KAFKA_IP + ":" + KAFKA_PORT)
    print("[LOGIN] Awaiting for info on Kafka Server topic = " + topic)
    return consumer

def listenMsg(cons):
    msg = next(cons)
    return msg.value.decode('utf-8')
     

def main():
    global ENGINE_IP
    global ENGINE_GRPC_IP
    global ENGINE_PORT
    global ENGINE_GRPC_PORT
    global AFORO_MAX
    
    lCons = loginConsumer()
    msg = listenMsg(lCons)
    print(msg)

main()
