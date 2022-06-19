#!/bin/bash

ps aux | grep main.py | awk '{print $2}' | xargs -I{} kill -s SIGKILL {} 2>/dev/null
./db_gen.py

gnome-terminal --tab --title=Engine -- bash -c 'cd FWQ_Engine; ./startEngine.sh; bash'
gnome-terminal --tab --title=WTS -- bash -c 'cd FWQ_WaitingTimeServer; ./startTimeServer.sh'
sleep 0.1
gnome-terminal --tab --title=Registry -- bash -c 'cd FWQ_Registry; ./startRegistry.sh'
sleep 0.1
gnome-terminal --tab --title=Sensor -- bash -c 'cd FWQ_Sensor; ./enciende_todos.sh; bash ; ./desconecta_todos.sh'
sleep 0.1
gnome-terminal --tab -- bash -c 'cd FWQ_Visitor/connect_visitors ; ./enciende_todos.sh; cd ../.. ; ./time_pass.py'

watch -n 0.1 "sqlite3 database.db 'select * from attraction'"
