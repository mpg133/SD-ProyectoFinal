
from movements import *

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
    string = "+------------------------------------------------------------+\n"
    for x in range(len(mapa)):
        string += "|"
        for y in range(len(mapa[x])):
            if(int(mapa[x][y]) > 9):
                string += mapa[x][y] + ' '
            elif(int(mapa[x][y]) == 0):
                string += '   '
            elif(int(mapa[x][y]) < -9):
                string += mapa[x][y]
            elif(int(mapa[x][y]) < 0):
                string += mapa[x][y] + ' '
            else:
                string += mapa[x][y] + '  '
        string += "|\n"
    string += "+------------------------------------------------------------+"

    return string

def parqueLogin(name, password):
    prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    cons = kc("loginResponsesTopic", bootstrap_servers = BROKER)
    prod.send('loginTopic', {'name' : name, 'password' : password})
    
    print("Esperando respuesta del login...")
    msg = json.loads(next(cons).value.decode('utf-8'))
    print(msg['msg'])

    if msg['ok']:
        firstPos = msg['firstPos']
        return msg['ok'], firstPos, msg['id_vis']
    else:
        return msg['ok'], None, None


def entraAlParque(name, firstPos):
    producer = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    consumer = kc(name+'TopicRecv', bootstrap_servers = BROKER)

    producer.send(name+'Topic', {'ok':True, 'posX' : firstPos[0], 'posY' : firstPos[1]})
    time.sleep(1)

    pos = firstPos
    while True:
        producer.send(name+'Topic', {'ok':True, 'pos' : pos})
        msg = json.loads(next(consumer).value.decode('utf-8'))
        
        print(mapaToString(msg['mapa']))

        pos = moveAuto(msg['mapa'], pos, msg['attrs'])

        time.sleep(1)


