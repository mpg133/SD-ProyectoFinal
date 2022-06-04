#!/usr/bin/python3

import json
import os
import time

cont = 0

while True:
       
    fisic_attrs = os.listdir('FWQ_Sensor/fisic_attractions')
    fisic_attrs = [ int(f.replace('.json','').replace('attr','')) for f in fisic_attrs ]

    for id_attr in fisic_attrs:
        with open('FWQ_Sensor/fisic_attractions/attr'+str(id_attr)+'.json', 'r') as f:
            attr_queue = json.load(f)
        names = list(attr_queue.keys())

        if len(names) > 0:
            attr_queue[names[0]] -= 1

        os.system('rm -rf FWQ_Sensor/fisic_attractions/attr'+str(id_attr)+'.json')

        with open('FWQ_Sensor/fisic_attractions/attr'+str(id_attr)+'.json', 'w') as f:
            json.dump(attr_queue, f)


    time.sleep(1)
    print('Han pasado '+str(cont)+' segundos')
    cont += 1
    if cont >= 1000000:
        cont = 0

