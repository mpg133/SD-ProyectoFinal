#!/usr/bin/python3

import sqlite3
import os
import random

os.system('rm -rf database.db 2>/dev/null')

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE visitor (id INTEGER PRIMARY KEY AUTOINCREMENT, name UNIQUE, password ) ''')
cur.execute(''' CREATE TABLE attraction (id INTEGER PRIMARY KEY AUTOINCREMENT, wait_time ) ''')
cur.execute(''' CREATE TABLE map ( x, y, content ) ''')

def main():
    id_attr = 1
    for i in range(20):
        for j in range(20):
            if random.randrange(0,30) == 0:
                cur.execute(' INSERT into attraction (wait_time) values('+str(30)+')')
                cur.execute(' INSERT into map (x, y, content) values('+str(i)+', '+str(j)+', '+str(id_attr)+')')
                id_attr += 1
            else:
                cur.execute(' INSERT into map (x, y, content) values('+str(i)+', '+str(j)+', '+str(0)+')')
    conn.commit()
    conn.close()


main()
