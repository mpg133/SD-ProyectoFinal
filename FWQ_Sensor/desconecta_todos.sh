#!/bin/bash

for pid in $(ps aux | grep 'main.py sensor' | awk '{print $2}')
do
    kill -s SIGINT $pid 2>/dev/null
done

rm -rf active_sensors/*
