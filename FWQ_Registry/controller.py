import sqlite3
import hashlib


def registra(name, password):

    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()

    try:
        pass_hash = hashlib.md5(bytes(password, encoding="utf8")).hexdigest()

        cur.execute('insert into visitor(name, password) values("' + name + '", "'+pass_hash+'")')

        conn.commit()

        cur.execute('select id from visitor where name = "'+name+'"')
        id_vis = cur.fetchall()
        id_vis = id_vis[0][0]

        conn.close()
        return True, [str(id_vis), name]
    except:
        return False, ["ERROR al añadir a " + name + " al registro."]



def edita(name, password, newName, newPassword):
    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()

    #el nuevo nombre ya existe
    cur.execute('select * from visitor where name = "'+newName+'"')
    user = cur.fetchall()
    if len(user) >= 1:
        conn.close()
        return False, ["ERROR al editar visitante (nuevo nombre ocupado)."]

    #el usuario a editar no existe
    cur.execute('select * from visitor where name = "'+name+'"')
    user = cur.fetchall()
    if len(user) <= 0:
        conn.close()
        return False, ["ERROR al editar visitante (credenciales incorrectas)."]

    pass_hash = hashlib.md5(bytes(password, encoding="utf8")).hexdigest()
    new_pass_hash = hashlib.md5(bytes(newPassword, encoding="utf8")).hexdigest()

    try:
        cur.execute('update visitor set name = "'+newName+'", password = "'+new_pass_hash+'" where name = "'+name+'" and password = "'+pass_hash+'"')
        conn.commit()
        conn.close()
    except:
        return False, ["ERROR al editar usuario. (excepcion)"]

    return True, [str(user[0][0]), newName, 'Visitante editado correctamente.']






