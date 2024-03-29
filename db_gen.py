#!/usr/bin/python3

import sqlite3
import os
import random

import json

os.system('rm -rf database.db 2>/dev/null')
os.system('rm -rf FWQ_Sensor/fisic_attractions/attr* 2>/dev/null')

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE visitor (id INTEGER PRIMARY KEY AUTOINCREMENT, name UNIQUE, password, status) ''')
cur.execute(''' CREATE TABLE attraction (id INTEGER PRIMARY KEY AUTOINCREMENT, wait_time, region, status) ''')
cur.execute(''' CREATE TABLE map ( id INTEGER PRIMARY KEY, content ) ''')

def main():
    mapa = ''
    id_attr = 1
    for i in range(20):
        for j in range(20):
            if random.randrange(0,100) < 4:
                #time = str(random.randrange(15,31))
                #time = str(0)
                time="50"
                if i < 10 and j < 10:
                    region = "Madrid"
                elif i < 10 and j >= 10:
                    region = "Toronto"
                elif i >= 10 and j < 10:
                    region = "Paris"
                elif i >= 10 and  j >= 10:
                    region = "Oslo"

                cur.execute(' INSERT into attraction (wait_time, region, status) values('+time+', "'+region+'", True)')

                os.system('echo {} > FWQ_Sensor/fisic_attractions/attr'+str(id_attr)+'.json')
                mapa += str(id_attr) + ' '
                id_attr += 1
            else:
                mapa += '0 '
        mapa += '\n'

    cur.execute(' INSERT into map(id, content) values(1, "'+mapa+'") ')
    conn.commit()
    conn.close()
    os.system('./insert_users.py')
    os.system('rm -rf FWQ_Sensor/avtive_sensors/*')
    os.system('ps aux | grep -E "main\.py|appEng\.py|appReg.py" | awk ' + "'" + '{print $2}'+ "'" +' | xargs -I{} kill {} 2>/dev/null')

main()
