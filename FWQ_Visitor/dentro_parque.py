from kafka import KafkaProducer as kp
from dotenv import dotenv_values
from menu import *
prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT;

def entraAlParque():
    try:
        name, password = askCreds()
        prod.send('loginTopic', {'name' : name, 'password' : password})
        cons = createLoginConsumer()
        msg = listenMsg(cons)
        print(msg)
    except:
        print('Error al conectar con el engine.')


