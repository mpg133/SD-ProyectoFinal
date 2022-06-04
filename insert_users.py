#!/usr/bin/python3

import sqlite3
import os
import random
import hashlib

conn = sqlite3.connect('database.db')
cur = conn.cursor()

pass_hash = hashlib.md5(bytes("asd", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("asd", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("qwe", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("qwe", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("zxc", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("zxc", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("a", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("a", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("b", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("b", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("c", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("c", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("d", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("d", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("e", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("e", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("f", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("f", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("g", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("g", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("h", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("h", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("i", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("i", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("j", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("j", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("k", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("k", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("l", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("l", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("m", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("m", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("n", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("n", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("o", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("o", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("p", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("p", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("q", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("q", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("r", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("r", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("s", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("s", "'+pass_hash+'")')

pass_hash = hashlib.md5(bytes("t", encoding="utf8")).hexdigest()
cur.execute('insert into visitor(name, password) values("t", "'+pass_hash+'")')

conn.commit()
conn.close()
