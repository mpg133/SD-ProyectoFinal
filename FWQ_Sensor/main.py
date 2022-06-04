#!/usr/bin/python3

import os
import json
import random
import time
import signal

from kafka import KafkaProducer as kp

from dotenv import dotenv_values


def signalExit(signum, frame):
    os.system('rm -rf active_sensors/' + str(sensor_id) + ' 2>/dev/null')
    exit()

signal.signal(signal.SIGINT, signalExit)

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT

sensor_id = -1


attrs = os.listdir('fisic_attractions')
attrs = [ int(a.replace('.json', '').replace('attr','')) for a in attrs ]

active_sensors = os.listdir('active_sensors')
active_sensors = [int(a) for a in active_sensors]

if len(active_sensors) == 0:
    sensor_id = 1
else:
    for i in range(len(attrs)):
        if attrs[i] not in active_sensors:
            sensor_id = attrs[i]

if sensor_id != -1:
    os.system('touch active_sensors/' + str(sensor_id))
else:
    print('Todas las atracciones tienen un sensor activo')
    exit()

timePassed = 0

while True:

    try:
        with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'r') as a:
            attr_queue = json.load(a)
        names = list(attr_queue.keys())

        prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
        prod.send('SensorsTopic', {'attr': sensor_id, 'people_count' : len(names)})

        if len(names) > 0:
            attr_queue[names[0]] -= timePassed

        os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json')

        with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'w') as a:
            json.dump(attr_queue, a)

    except:
        pass
    
    timePassed = random.randrange(1,4)
    time.sleep(timePassed)
