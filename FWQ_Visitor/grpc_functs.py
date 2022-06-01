import grpc
import todo_pb2
import todo_pb2_grpc

from dotenv import dotenv_values

def registrarVisitante(stub, name, password):
    msg = todo_pb2.RegVis(name=name, password=password)
    response = stub.registrarVisitante(msg)
    return response.id, response.name, response.ok, response.msg

def editarVisitante(stub, name, password, newName, newPassword):
    msg = todo_pb2.EditVis(name=name, password=password, newName=newName, newPassword=newPassword)
    response = stub.editarVisitante(msg)
    return response.id, response.name, response.ok, response.msg

def iniciarGrpcSecure():
    cert = open('client-cert.pem', 'rb').read()
    key = open('client-key.pem','rb').read()
    ca_cert = open('ca.pem','rb').read()
    
    channel_creds = grpc.ssl_channel_credentials(ca_cert,key,cert)

    config = dotenv_values(".env")
    REGISTRY_GRPC_IP = config['REGISTRY_GRPC_IP']
    REGISTRY_GRPC_PORT = config['REGISTRY_GRPC_PORT']

    channel = grpc.secure_channel(REGISTRY_GRPC_IP +":"+REGISTRY_GRPC_PORT,channel_creds)
    return todo_pb2_grpc.TodoStub(channel)


