#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importamos el modulo para PostgreSQL
import psycopg2

def conex(valores):
    #intentamos la conexion con los datos recogidos del formulario y si es correcto devolvera True, si no es correcto devolvera False
    try:
        connection=psycopg2.connect(user = valores[0],
                                      password = valores[1],
                                      host = valores[2],
                                      port = "5432",
                                      database = "postgres")
        cursor=connection.cursor()

        return True,connection,cursor

    except (Exception, psycopg2.Error) as error :
        valor=[False]
        return valor

def dexc(connection,cursor):
    #Intentamos cerrar la conexion si los datos de acceso son correctos, sino no cerrara nada
    try:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL ha cerrado la conexion")
    except:
        print("¡¡¡¡¡¡¡¡PostgreSQL NO ha cerrado la conexion!!!!!!!!!!!!")
