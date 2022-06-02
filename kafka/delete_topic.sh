#!/bin/bash

if [ -z $1 ]
then
    echo "Usage: "
    echo ""
    echo "./delete_topic.sh <TOPIC_NAME>"
else
    kaf=$(ls | grep ^kafka_)
    kafka_2.13-3.2.0/bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic $1 --delete
fi
