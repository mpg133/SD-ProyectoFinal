import grpc
import todo_pb2
import todo_pb2_grpc

from dotenv import dotenv_values

def iniciarGrpcSecure():
    #cert = open('client-cert.pem', 'rb').read()
    #key = open('client-key.pem','rb').read()
    #ca_cert = open('ca.pem','rb').read()
    
    #channel_creds = grpc.ssl_channel_credentials(ca_cert,key,cert)
    config = dotenv_values(".env")
    GRPC_WTS_IP = config['GRPC_WTS_IP']
    GRPC_WTS_PORT = config['GRPC_WTS_PORT']

    #channel = grpc.secure_channel(REGISTRY_GRPC_IP +":"+REGISTRY_GRPC_PORT,channel_creds)

    channel = grpc.insecure_channel(GRPC_WTS_IP +":"+GRPC_WTS_PORT)
    return todo_pb2_grpc.TodoStub(channel)


