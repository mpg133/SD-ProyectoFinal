#!/bin/bash

echo 'MAP_SIZE=20' > .env
echo 'REGISTRY_GRPC_IP="localhost"' >> .env
echo 'REGISTRY_GRPC_PORT="50051"' >> .env
echo 'ENGINE_KAFKA_IP="localhost"' >> .env
echo 'ENGINE_KAFKA_PORT="9092"' >> .env
echo 'API_URL="http://localhost:5000"'>> .env


if [ -z $1 ]
then
	./main.py
else
	sed -i 's/REGISTRY_GRPC_IP="localhost"/REGISTRY_GRPC_IP="'$2'"/g' .env
	if [ -z $2 ]
	then
		./main.py
		exit
	else 
		sed -i 's/REGISTRY_GRPC_PORT="50051"/REGISTRY_GRPC_PORT="'$3'"/g' .env
	fi
	if [ -z $3 ]
	then
		./main.py
		exit
	else
		sed -i 's/REGISTRY_KAFKA_IP="localhost"/REGISTRY_KAFKA_IP="'$4'"/g' .env
	fi
	if [ -z $4 ]
	then
		./main.py
		exit
	else
		sed -i 's/REGISTRY_KAFKA_PORT="9092"/REGISTRY_KAFKA_PORT="'$5'"/g' .env
	fi
	if [ -z $5 ]
	then
		./main.py
		exit
	
	fi
	./main.py
fi
