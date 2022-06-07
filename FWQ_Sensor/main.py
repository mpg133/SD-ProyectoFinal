#!/usr/bin/python3

import os
import json
import random
import time
import signal

from kafka import KafkaProducer as kp

from dotenv import dotenv_values

import sys

def signalExit(signum, frame):
    os.system('rm -rf active_sensors/' + str(sensor_id) + ' 2>/dev/null')
    exit()

signal.signal(signal.SIGINT, signalExit)

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT


if len(sys.argv) >= 2:

    sensor_id = sys.argv[1]

else:
    attrs = os.listdir('fisic_attractions')
    attrs = [ int(a.replace('.json', '').replace('attr','')) for a in attrs ]
    sensor_id = attrs[random.randrange(0,len(attrs))]

timePassed = 0

while True:

    try:
        with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'r') as a:
            attr_queue = json.load(a)
        names = list(attr_queue.keys())

        prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
        prod.send('SensorsTopic', {'attr': sensor_id, 'people_count' : len(names)})

    except:
        pass
    
    timePassed = random.randrange(1,4)
    time.sleep(timePassed)
