#!/bin/bash

for i in $(ps aux | grep 'python3 ./main.py visitor' | awk '{print $2}')
do
    kill -s SIGINT $i 2>/dev/null
    sleep 0.5
done
