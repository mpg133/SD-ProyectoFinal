#!/bin/bash

echo 'ENGINE_KAFKA_IP="localhost"' > .env
echo 'ENGINE_KAFKA_PORT="9092"' >> .env


if [ -z $1 ]
then
	./main.py
else
	sed -i 's/ENGINE_KAFKA_IP="localhost"/ENGINE_KAFKA_IP="'$1'"/g' .env
	if [ -z $2 ]
	then
		./main.py
		exit
	else
		sed -i 's/ENGINE_KAFKA_PORT="9092"/ENGINE_KAFKA_PORT="'$2'"/g' .env
	fi
	./main.py $3
fi


