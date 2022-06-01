#!/usr/bin/python3

from menu import *
from movements import *
from grpc_functs import *

def main():

    stub = iniciarGrpcSecure()
    
    while True:
        option = menuOption()
        if option == "1":
            name, password = askCreds()
            id, name, ok, msg = registrarVisitante(stub, name, password)
        elif option == "2":
            name, password, newName, newPassword = askNewCreds()
            id, name, ok, msg = editarVisitante(stub, name, password, newName, newPassword)

        print(id)
        print(msg)


main()
