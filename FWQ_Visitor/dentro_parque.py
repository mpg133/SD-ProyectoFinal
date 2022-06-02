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



def createLoginConsumer(name):
    topic = "loginResponsesTopic"
    consumer = kc(topic, bootstrap_servers = BROKER)
    return consumer


def listenMsg(cons):
    msg = next(cons)
    return msg.value.decode('utf-8')

def parqueLogin(name, password):
    prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    cons = createLoginConsumer(name)
    prod.send('loginTopic', {'name' : name, 'password' : password})
    
    print("[LOGIN] Awaiting for info on Kafka Server topic = loginTopic")
    msg = json.loads(listenMsg(cons))
    print(msg['msg'])
    return msg['ok']



def entraAlParque(name):
    producer = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    consumer = kc(name+'TopicRecv', bootstrap_servers = BROKER)
    while True:
        producer.send(name+'Topic', {'ok':True, 'posicion' : 'casa tu madre jajajaj loloolooool'})
        time.sleep(1)


