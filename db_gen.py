#!/usr/bin/python3

import sqlite3
import os
import random

os.system('rm -rf database.db 2>/dev/null')

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE visitor (id INTEGER PRIMARY KEY AUTOINCREMENT, name UNIQUE, password ) ''')
cur.execute(''' CREATE TABLE attraction (id INTEGER PRIMARY KEY AUTOINCREMENT, wait_time ) ''')
cur.execute(''' CREATE TABLE map ( id INTEGER PRIMARY KEY, content ) ''')

# HACER MAPA EN UN STRING SEPARADO POR ALGUN SIMBOLO Y UTILIZAR SPLIT PARA TRANSFORMARLO


def main():
    mapa = ''
    id_attr = 1
    for i in range(20):
        for j in range(20):
            if random.randrange(0,30) == 0:
                cur.execute(' INSERT into attraction (wait_time) values('+str(30)+')')
                mapa += str(id_attr) + ' '
                id_attr += 1
            else:
                mapa += '0 '
        mapa += '\n'

    cur.execute(' INSERT into map(id, content) values(1, "'+mapa+'") ')
    conn.commit()
    conn.close()


main()
