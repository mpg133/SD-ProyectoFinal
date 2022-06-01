#!/usr/bin/python3

from menu import *
from movements import *
from grpc_functs import *

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition
from kafka import KafkaProducer as kp

import json


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
            config = dotenv_values('.env')
            prod = kp(bootstrap_servers=config['ENGINE_KAFKA_IP'] +':'+config['ENGINE_KAFKA_PORT'], value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all', retries=3)
            prod.send('loginTopic', 'wewewewe')





main()
