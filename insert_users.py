#!/usr/bin/python3

import sqlite3
import os
import random
import hashlib

conn = sqlite3.connect('database.db')
cur = conn.cursor()

pass_hash = hashlib.md5(bytes("asd", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("asd", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("qwe", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("qwe", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("zxc", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("zxc", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("a", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("a", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("b", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("b", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("c", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("c", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("d", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("d", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("e", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("e", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("f", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("f", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("g", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("g", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("h", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("h", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("i", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("i", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("j", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("j", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("k", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("k", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("l", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("l", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("m", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("m", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("n", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("n", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("o", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("o", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("p", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("p", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("q", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("q", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("r", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("r", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("s", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("s", "'+pass_hash+'", "disconnected")')

pass_hash = hashlib.md5(bytes("t", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password, status) values("t", "'+pass_hash+'", "disconnected")')

conn.commit()
conn.close()
