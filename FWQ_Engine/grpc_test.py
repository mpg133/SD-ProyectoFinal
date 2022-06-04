#!/usr/bin/python3

from grpc_functs import *

import json

import grpc
import todo_pb2
import todo_pb2_grpc


config = dotenv_values(".env")
GRPC_WTS_IP = config['GRPC_WTS_IP']
GRPC_WTS_PORT = config['GRPC_WTS_PORT']

channel = grpc.insecure_channel(GRPC_WTS_IP +":"+GRPC_WTS_PORT)

stub=todo_pb2_grpc.TodoStub(channel)

print('trying to connect to ' + str(GRPC_WTS_PORT))

mesg = todo_pb2.EngineReq()
response = stub.requestWaitingTimes(mesg)

response = json.loads(response.times_string_dict.replace("'", "\""))

print(response)