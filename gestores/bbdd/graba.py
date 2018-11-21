import sqlite3

def create():
    # creamos la base de datos con el cursor
    miconexion=sqlite3.connect("apuntes")
    micursor=miconexion.cursor()

    datos=[(self.valor1,self.valor2,self.valor3)]

    micursor.executemany("INSERT INTO "+self.tabla+" VALUES(?,?,?)",datos)

    miconexion.commit()

    miconexion.close()
