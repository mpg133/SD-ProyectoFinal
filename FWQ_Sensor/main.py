#!/usr/bin/python3

from kafka import KafkaProducer as kp

from dotenv import dotenv_values

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT

sensor_id = 1
ppl = []

prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
prod.send('Sensor' + sensor_id + 'Topic', {'people_waiting' : ppl})