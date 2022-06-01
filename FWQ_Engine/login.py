#!/usr/bin/python3

import sqlite3
import hashlib


def login(name, password):
    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM visitor WHERE name = "' + name + '"')
    rows = cur.fetchall()
    if len(rows) < 1:
        conn.close()
        return False

    if rows[0][2] == hashlib.md5(bytes(password, encoding="utf8")).hexdigest():
        conn.close()
        return True

    return False


