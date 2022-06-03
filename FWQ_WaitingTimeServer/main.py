#!/usr/bin/python3

from kafka import KafkaConsumer as kc

from dotenv import dotenv_values

import json

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT

consumer = kc('SensorsTopic', bootstrap_servers = BROKER)

while True:
    msg = json.loads(next(consumer).value.decode('utf-8'))
    print('attr: ' + str(msg['attr']) + ' -> ' + str(msg['time']) + ':00')