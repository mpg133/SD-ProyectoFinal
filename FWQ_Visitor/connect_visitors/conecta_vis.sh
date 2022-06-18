#!/bin/bash

if [ -z $1  ]
then
    echo 'Usage:'
    echo './program.sh <visitor_name>'
else
    mkfifo fifo_$1
    stdbuf -i0 -o0 bash < fifo_$1 &
    exec 3>fifo_$1 && rm -rf fifo_$1

    sleep 0.1

    echo "cd .." >&3
    echo "pwd > /dev/null" >&3
    echo "./main.py visitor_$1" >&3
    sleep 0.1
    echo "5" >&3
    sleep 0.1
    echo "$1" >&3
    sleep 0.1
    echo "$1" >&3
fi
