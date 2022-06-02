#!/usr/bin/python3

import os
import json

from threading import Thread, Event

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition
from kafka.admin import KafkaAdminClient

from kafka import KafkaProducer as kp
from login import *
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT
GRPC_WTS_IP = config['GRPC_WTS_IP']
GRPC_WTS_PORT = config['GRPC_WTS_PORT']

AFORO_MAX=config['AFORO_MAX']
AFORO=0


def createLoginConsumer():
    topic = "loginTopic"
    consumer = kc(topic, bootstrap_servers = BROKER)
    return consumer

def listenMsg(cons):
    print("[LOGIN] Awaiting for info on Kafka Server")
    msg = next(cons)
    return msg.value.decode('utf-8')

def exit_delete_topics(name):
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=BROKER)
        admin_client.delete_topics(topics=[name + 'Topic', name + 'TopicRecv'])
    except:
        exit(1)
    exit(1)

def handleVisitor(name):

    consumer = kc(name + 'Topic', bootstrap_servers = BROKER, consumer_timeout_ms=3000)
    try:
        while True:
            msg = json.loads(listenMsg(consumer))
            print(msg)
            if not msg['ok']:
                break
    except:
        exit_delete_topics(name)
            



def main():
   
    login_consumer = createLoginConsumer()
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')

    msg = json.loads(listenMsg(login_consumer))

    if login(msg['name'], msg['password']):
        time.sleep(0.1)
        producer.send("loginResponsesTopic", {'ok': True, 'msg' : 'login ok'})
        handleVisitor(msg['name'])

    else:
        time.sleep(0.1)
        producer.send("loginResponsesTopic", {'ok': False, 'msg' : 'ERROR login'})

main()
