#!/bin/bash

echo 'REGISTRY_GRPC_PORT="50051"' > .env
echo 'REGISTRY_API_IP="0.0.0.0"' >> .env
echo 'REGISTRY_API_PORT="5000"' >> .env

if [ -z $1 ]
then
	./main.py
else
	sed -i 's/REGISTRY_GRPC_PORT="50051"/REGISTRY_GRPC_PORT="'$1'"/g' .env
	if [ -z $2 ]
	then
		./main.py
		exit
	else 
		sed -i 's/REGISTRY_API_IP="0.0.0.0"/REGISTRY_API_IP="'$2'"/g' .env	
	fi
	if [ -z $3 ]
	then
		./main.py
		exit
	else
		sed -i 's/REGISTRY_API_PORT="5000"/REGISTRY_API_PORT="'$3'"/g' .env
	fi
	./main.py
fi
