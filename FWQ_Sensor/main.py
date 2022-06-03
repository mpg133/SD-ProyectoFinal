#!/usr/bin/python3

import os
import json
import random
import time

from kafka import KafkaProducer as kp

from dotenv import dotenv_values

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT

sensor_id = 2

timePassed = 0

while True:
    with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'r') as a:
        attr_queue = json.load(a)
    names = list(attr_queue.keys())


    total_time = 0
    for name in names:
        total_time += attr_queue[name] if attr_queue[name] > 0 else 0

    prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    prod.send('SensorsTopic', {'attr': sensor_id, 'time' : total_time})



    if len(names) > 0:
        attr_queue[names[0]] -= timePassed

    os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json')
    with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'w') as a:
        json.dump(attr_queue, a)

    timePassed = random.randrange(1,4)
    time.sleep(timePassed)