#!/bin/bash

if [ -z $1 ]
then
    cat kafka_2.13-3.2.0/config/server.properties | grep -e '#' -e '^$' -v  > server.properties
    echo "Server kafka = 127.0.0.1:9092"
else
    cat kafka_2.13-3.2.0/config/server.properties | grep -e '#' -e '^$' -v | sed -e 's/127.0.0.1:9092/'$1'/g' > server.properties
    echo "Server kafka = "$1
fi

gnome-terminal -t zookeper --tab -- kafka_2.13-3.2.0/bin/zookeeper-server-start.sh kafka_2.13-3.2.0/config/zookeeper.properties
gnome-terminal -t kafka --tab -- kafka_2.13-3.2.0/bin/kafka-server-start.sh server.properties

