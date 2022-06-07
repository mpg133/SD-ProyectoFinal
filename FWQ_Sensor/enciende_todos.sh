#!/bin/bash

for i in $(ls fisic_attractions)
do
    ./main.py $(echo $i | sed 's/.json//g;s/attr//g') sensor &
    sleep 0.1
done
