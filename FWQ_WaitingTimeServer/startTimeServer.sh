#!/bin/bash

cp .envTemplate .env

if [ -z $1 ]
then
	./main.py
else
	sed -i 's/KAFKA_IP="localhost"/KAFKA_IP="'$1'"/g' .env
	if [ -z $2 ]
	then
		./main.py
		exit
	else 
		sed -i 's/KAFKA_PORT="9092"/KAFKA_PORT="'$2'"/g' .env
			
	fi
	if [ -z $3 ]
	then
		./main.py
		exit
	else
		sed -i 's/GRPC_PORT="50052"/GRPC_PORT="'$3'"/g' .env
	fi
	if [ -z $4 ]
	then
		./main.py
		exit
	else
		sed -i 's/TIME_PERSON="5"/TIME_PERSON="'$4'"/g' .env
	fi
	if [ -z $5 ]
	then
		./main.py
		exit
	else
		sed -i 's/TIME_BASE_ATTR="55"/TIME_BASE_ATTR="'$5'"/g' .env
	fi
	
	
	./main.py
	
	
	
fi
