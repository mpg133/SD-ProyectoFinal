#!/usr/bin/python3

from get_bd import *
import os
import json
from threading import Thread

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition
from kafka.admin import KafkaAdminClient

from kafka import KafkaProducer as kp
from login import *
import time

import signal

def signalExit(signum, frame):
    print("\n\nEXIT")
    exit(1)
signal.signal(signal.SIGINT, signalExit)

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT
GRPC_WTS_IP = config['GRPC_WTS_IP']
GRPC_WTS_PORT = config['GRPC_WTS_PORT']

AFORO_MAX=int(config['AFORO_MAX'])
AFORO=0

def exit_delete_topics(name):
    print("Visitor '" + name + "' disconnected.")
    global AFORO
    AFORO -= 1
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=BROKER)
        admin_client.delete_topics(topics=[name + 'Topic', name + 'TopicRecv'])
    except:
        exit(1)
    exit(1)

def handleVisitor(name):
    consumer = kc(name + 'Topic', bootstrap_servers = BROKER, consumer_timeout_ms=3000)
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    print("Visitor '" + name + "' connected.")
    try:
        while True:
            #print("Visitor '" + name + "' connected. Waiting response...")
            msg = json.loads(next(consumer).value.decode('utf-8'))
            #print(msg)
            
            time.sleep(0.3)
            mapa = getMap()
            producer.send(name+"TopicRecv", {'ok': True, 'mapa' : mapa })

            if not msg['ok']:
                AFORO -= 1
                exit_delete_topics(name)
    except:
        exit_delete_topics(name)
            


def main():
   
    login_consumer = kc("loginTopic", bootstrap_servers = BROKER)
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')

    while True:
        print("[LOGIN] Awaiting for info on Kafka Server")
        msg = json.loads(next(login_consumer).value.decode('utf-8'))

        if login(msg['name'], msg['password']):

            global AFORO_MAX
            global AFORO
            if AFORO_MAX > AFORO :
                AFORO += 1
                time.sleep(0.1)

                producer.send("loginResponsesTopic", {'ok': True, 'msg' : 'Login ok'})

                new_thread = Thread(target=handleVisitor, args={msg['name']})
                new_thread.start()
            else:
                time.sleep(0.1)
                producer.send("loginResponsesTopic", {'ok': False, 'msg' : 'Aforo completo'})


        else:
            time.sleep(0.1)
            producer.send("loginResponsesTopic", {'ok': False, 'msg' : 'ERROR login'})

main()
