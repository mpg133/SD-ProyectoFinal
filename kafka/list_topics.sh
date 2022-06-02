#!/bin/bash

kaf=$(ls | grep kafka_2.13)
$kaf/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
