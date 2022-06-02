#!/usr/bin/python3

import sqlite3
import re

def regexReplace(match):
    if match.group() is not None:

        return match.group()
def getMap():
    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM map WHERE id = 1')
    query = cur.fetchall()[0][1]
    query = query.split("\n")
    mapa = []
    for i in range(len(query)):
        mapa.append(query[i].split(' '))
        mapa[i] = [m for m in mapa[i] if m != '' ]
    mapa = [m for m in mapa if m != []]

    return mapa
