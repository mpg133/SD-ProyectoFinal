import time

from kafka import KafkaProducer as kp
from kafka import KafkaConsumer as kc

from dotenv import dotenv_values
from menu import *

import json

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT

def mapaToString(mapa):
    string = "+--------------------------------------------------------------+\n"
    for x in range(len(mapa)):
        string += "|  "
        for y in range(len(mapa[x])):
            if(int(mapa[x][y]) > 9):
                string += mapa[x][y] + ' '
            elif(int(mapa[x][y]) == 0):
                string += '   '
            else:
                string += mapa[x][y] + '  '
        string += "|  "
        string += "\n"

    string += "+--------------------------------------------------------------+"

    return string

def parqueLogin(name, password):
    prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    cons = kc("loginResponsesTopic", bootstrap_servers = BROKER)
    prod.send('loginTopic', {'name' : name, 'password' : password})
    
    print("Esperando respuesta del login...")
    msg = json.loads(next(cons).value.decode('utf-8'))
    print(msg['msg'])
    return msg['ok']



def entraAlParque(name):
    producer = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    consumer = kc(name+'TopicRecv', bootstrap_servers = BROKER)

    producer.send(name+'Topic', {'ok':True, 'posX' : 'x', 'posY' : 'y'})
    time.sleep(1)

    while True:
        producer.send(name+'Topic', {'ok':True, 'posX' : 'x', 'posY' : 'y'})
        msg = json.loads(next(consumer).value.decode('utf-8'))
        print(mapaToString(msg['mapa']))

        time.sleep(1)


