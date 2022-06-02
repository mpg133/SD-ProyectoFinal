#!/bin/bash

kaf=$(ls | grep kafka_2.13)

if [ -z $1 ]
then
    cat $kaf/config/server.properties | grep -e '#' -e '^$' -v  > server.properties
    echo "Server kafka = 127.0.0.1:9092"
else
    cat $kaf/config/server.properties | grep -e '#' -e '^$' -v | sed -e 's/127.0.0.1:9092/'$1'/g' > server.properties
    echo "Server kafka = "$1
fi

gnome-terminal -t zookeper --tab -- $kaf/bin/zookeeper-server-start.sh $kaf/config/zookeeper.properties
sleep 1
gnome-terminal -t kafka --tab -- $kaf/bin/kafka-server-start.sh server.properties

