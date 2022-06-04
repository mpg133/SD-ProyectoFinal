#!/bin/bash

for i in $(ls fisic_attractions)
do
    ./main.py sensor &
    sleep 0.1
done
