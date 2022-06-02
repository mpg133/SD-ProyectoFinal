#!/usr/bin/python3

from dentro_parque import *
from menu import *
from movements import *
from grpc_functs import *

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition

import json

import signal

def handler(signum, frame):
    prod.send('Topic', {'name' : name, 'password' : password})
    exit(0)

signal.signal(signal.SIGINT, handler)


config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT;


def createLoginConsumer():
    topic = "loginResponsesTopic"
    consumer = kc(topic, bootstrap_servers = BROKER)
    print("[LOGIN] Awaiting for info on Kafka Server topic = " + topic)
    return consumer

def listenMsg(cons):
    msg = next(cons)
    return msg.value.decode('utf-8')


def main():

    stub = iniciarGrpcSecure()
    
    option = "0"
    while option != "4":
        option = menuOption()
        if option == "4": break

        if option == "1":
            name, password = askCreds()
            id, name, ok, msg = registrarVisitante(stub, name, password)
            print(id)
            print(msg)
        elif option == "2":
            name, password, newName, newPassword = askNewCreds()
            id, name, ok, msg = editarVisitante(stub, name, password, newName, newPassword)
            print(id)
            print(msg)
        elif option == "3":
            print('entrar al parque')
            entraAlParque()



main()
