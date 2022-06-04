#!/bin/bash

gnome-terminal --tab --title=Engine -- bash -c 'cd FWQ_Engine; ./main.py; bash'
sleep 1
gnome-terminal --tab --title=Registry -- bash -c 'cd FWQ_Registry; ./main.py'
sleep 1
gnome-terminal --tab --title=WTS -- bash -c 'cd FWQ_WaitingTimeServer; ./main.py'
sleep 1
gnome-terminal --tab --title=Sensor -- bash -c 'cd FWQ_Sensor; ./enciende_todos.sh; bash ; ./desconecta_todos.sh'
sleep 1
gnome-terminal --tab -- bash -c 'cd FWQ_Visitor/connect_visitors ; ./enciende_todos.sh'

