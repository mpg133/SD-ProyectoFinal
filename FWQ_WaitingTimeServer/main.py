#!/usr/bin/python3

from kafka import KafkaConsumer as kc

from dotenv import dotenv_values

import json

from datetime import datetime, timedelta

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT

consumer = kc('SensorsTopic', bootstrap_servers = BROKER)

attrs = {}
start = datetime.now()
end = start

while True:
    if end - start >= timedelta(seconds=1):
        print(attrs)
        start = datetime.now()
    end = datetime.now()

    to_del = []
    for a in attrs:
        if attrs[a] == 0:
            to_del.append(a)

    for d in to_del:
        attrs.pop(d)

    msg = json.loads(next(consumer).value.decode('utf-8'))
    attrs[msg['attr']] = msg['people_count'] * 5

    