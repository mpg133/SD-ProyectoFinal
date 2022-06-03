#!/bin/bash

if [ -z $1 ]
then
    echo 'Usage: '
    echo './program.sh <visitor_name>'
else
    ps aux | grep 'main.py visitor_'$i | awk '{print $2}' | xargs -I{} kill -s SIGINT {} 2>/dev/null
fi
