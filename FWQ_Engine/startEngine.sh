#!/bin/bash

if [ -z $1 ]
then
	./main.py
else
	grep 'KAFKA_IP' .envTemplate | sed 's/localhost/'$1'/g' > .env
	if [ -z $2 ]
	then
		./main.py
		exit
	else 
		grep 'KAFKA_PORT' .envTemplate | sed 's/9092/'$2'/g' >> .env	
	fi
	if [ -z $3 ]
	then
		./main.py
		exit
	else
		grep 'GRPC_WTS_IP' .envTemplate | sed 's/localhost/'$3'/g' >> .env
	fi
	if [ -z $4 ]
	then
		./main.py
		exit
	else
		grep 'GRPC_WTS_PORT' .envTemplate | sed 's/50052/'$4'/g' >> .env
	fi
	if [ -z $5 ]
	then 
		./main.py
		exit
	else
		grep 'AFORO_MAX' .envTemplate | sed 's/12/'$5'/g' >> .env
	fi
	
	./main.py
	
	
fi
