#!/usr/bin/python3

from dentro_parque import *
from menu import *
from movements import *
from grpc_functs import *

from dotenv import dotenv_values
import json

from kafka.admin import KafkaAdminClient

import signal
import time

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT

name = ''
my_id = ''

def signalExit(signum, frame):
    print("\n\nEXIT")
    inAttr = str(isInAttraction(name))
    if inAttr != "-1":
        with open('../FWQ_Sensor/fisic_attractions/attr'+inAttr+'.json', 'r') as a:
            attr_queue = json.load(a)
        try:
            attr_queue.pop(name)
        except:
            pass
        os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+inAttr+'.json')
        with open('../FWQ_Sensor/fisic_attractions/attr'+inAttr+'.json', 'w') as a:
            json.dump(attr_queue, a)

    try:
        prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
        prod.send(name + 'Topic', {'ok' : False})
        admin_client = KafkaAdminClient(bootstrap_servers=BROKER)
        admin_client.delete_topics(topics=[name + 'Topic', name + 'TopicRecv'])
    except:
        exit(1)
    exit(1)

signal.signal(signal.SIGINT, signalExit)


def main():
    global name
    global my_id
    stub = iniciarGrpcSecure()
    
    option = "0"
    while option != "4":
        option = menuOption()

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
            name, password = askCreds()
            print('entrar al parque')
            loginOk, firstPos, my_id = parqueLogin(name, password)
            if(loginOk):
                entraAlParque(name, firstPos)
        elif option == "4":
            signalExit('','')



main()
