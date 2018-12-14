#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

# creamos/abrimos el archivo acces donde se guardará los datos de acceso menos la contraseña, lo leemos y cerramos el archivo
def lee(nombre):
    try:
        # leemos los datos del archivo acces.txt
        fin=open(nombre,"rb")
        list=pickle.load(fin)
        fin.close()

        # pendiente de investigar
        str=[i.rstrip() for i in list]
        return str

    except:
        # si al leer no existe el archivo con la excepcion creara el archivo y la lista vacia
        lst=['']
        fin=open(nombre,"wb")
        pickle.dump(lst,fin)
        fin.close()

        str=[]
        return str

def escribe(nombre,valores):
    fin=open(nombre, "wb")
    pickle.dump(valores,fin)
    fin.close()
