#!/usr/bin/python3

from grpc_functs import *
from map_funcs import *
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

LOGED = []
AFORO_MAX=int(config['AFORO_MAX'])
AFORO=0

def exit_delete_topics(mapa, id_vis, name):
    updatePosition(mapa, id_vis, -1 , -1)
    LOGED.remove(name)
    global AFORO
    AFORO -= 1
    print("[CLOSING CONNECTION] Visitor \"" + name + "\" disconnected.")
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=BROKER)
        admin_client.delete_topics(topics=[name + 'Topic', name + 'TopicRecv'])
    except:
        exit(1)
    exit(1)


def handleVisitor(name, id_vis):
    consumer = kc(name + 'Topic', bootstrap_servers = BROKER, consumer_timeout_ms=3000)
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    print("[ESTABLISHED CONNECTION] Visitor \"" + name + "\" connected.")
    mapa = getMap()

    try:
        while True:
            msg = json.loads(next(consumer).value.decode('utf-8'))
            mapa, attrs = getMap()
            mapa, newPos = updatePosition(mapa, id_vis, msg['pos'], msg['next_pos'])
            time.sleep(0.2)

            producer.send(name+"TopicRecv", {'ok': True, 'mapa' : mapa , 'attrs' : attrs, 'new_pos': newPos})

            if not msg['ok']:
                break
    except:
        pass
    finally:
        exit_delete_topics(mapa, id_vis, name)


def askTimes(stub):
    msg = todo_pb2.EngineReq()
    response = stub.requestWaitingTimes(msg)
    response = json.loads(response.times_string_dict.replace("'", "\""))

    return response

def listenWTS():

    while True:

        try:
            stub=iniciarGrpcSecure()
            responseAttrs = askTimes(stub)

            conn = sqlite3.connect('../database.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM attraction')
            dbAttrs = cur.fetchall()

            for a in dbAttrs:
                if str(a[0]) in responseAttrs.keys() and a[1] != responseAttrs[str(a[0])] :
                    cur.execute('update attraction set wait_time = '+str(responseAttrs[str(a[0])])+' where id = ' + str(a[0]))
            conn.commit()
            conn.close()
        except:
            pass
        
        mapa, _ = getMap()
        print(mapaToString(mapa))
        try:
            time.sleep(1)    
        except:
            print("Adios :)")
       
        


def main():
    global AFORO_MAX
    global AFORO
    global LOGED

    new_thread = Thread(target=listenWTS)
    new_thread.start()


    login_consumer = kc("loginTopic", bootstrap_servers = BROKER)
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')

    while True:
        print("[LOGIN] Awaiting for info on Kafka Server")
        msg = json.loads(next(login_consumer).value.decode('utf-8'))
        time.sleep(0.1)

        aforoOk = AFORO_MAX > AFORO
        loginOk, id_vis = login(msg['name'], msg['password'])
        loginOk = loginOk and not msg['name'] in LOGED
        if loginOk and aforoOk:
            AFORO += 1
            LOGED.append(msg['name'])
            
            mapa, _ = getMap()
            firstPos = getRandomEmpty(mapa)
            producer.send("loginResponsesTopic", {'ok': True, 'firstPos' : firstPos, 'id_vis': id_vis, 'msg' : 'Login ok'})
            time.sleep(0.3)

            new_thread = Thread(target=handleVisitor, args=(msg['name'], id_vis))
            new_thread.start()

        else:
            producer.send("loginResponsesTopic", {'ok': False, 'msg' : 'ERROR login' if aforoOk else 'Aforo completo'})

main()
