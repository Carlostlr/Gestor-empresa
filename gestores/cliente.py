#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import pygubu



def client_treeview(builder):
    #con esto asignamos el scrollbar al widget correspondiente
    listbox = builder.get_object('list')
    scrollbar = builder.get_object('Scrollbar')
    listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=listbox.yview)


    #con esto obtenemos el widget e insertamos los elementos necesarios
    treeview=builder.get_object('list')
    treeview.insert("", tk.END, text="Elemento 1")
    treeview.insert("", tk.END, text="Elemento 2")
    treeview.insert("", tk.END, text="Elemento 3")
    treeview.insert("", tk.END, text="Elemento 4")


def client_save(builder):

    #creamos una lista en la que meteremos todos los valores obtenidos
    valores=[]
    comprobador=[]

    # obtenemos los valores que tenemos en cada campo
    value=builder.get_object('cod')
    #comprobamos que son numeros, introducirá true o false
    dato=value.get().isdigit()
    comprobador.append(dato)
    #añade el valor obtenido a la lista
    valores.append(value.get())

    #-----------------------------------------
    value=builder.get_object('nombre')
    dato=value.get().isalpha()
    comprobador.append(dato)
    valores.append(value.get().upper())

    #-----------------------------------------
    value=builder.get_object('empre')
    comprobador.append(True)
    valores.append(value.get().upper())

    #-----------------------------------------
    value=builder.get_object('direc')
    comprobador.append(True)
    valores.append(value.get().upper())

    #-----------------------------------------
    value=builder.get_object('cp')
    dato=value.get().isdigit()
    comprobador.append(dato)
    valores.append(value.get())

    #-----------------------------------------
    value=builder.get_object('pobl')
    dato=value.get().isalpha()
    comprobador.append(dato)
    valores.append(value.get().upper())

    #-----------------------------------------
    value=builder.get_object('prov')
    dato=value.get().isalpha()
    comprobador.append(dato)
    valores.append(value.get().upper())

    #-----------------------------------------
    value=builder.get_object('telf')
    dato=value.get().isdigit()
    comprobador.append(dato)
    valores.append(value.get())

    #-----------------------------------------
    value=builder.get_object('mail')
    dato=value.get()
    if "@" in dato:
        comprobador.append(True)
    else:
        comprobador.append(False)
    valores.append(value.get().upper())

    #-----------------------------------------
    value=builder.get_object('fax')
    dato=value.get().isdigit()
    comprobador.append(dato)
    valores.append(value.get())

    #-----------------------------------------
    #Hacemos un bucle para que nos devuelva la posicion de cada elemento que no sea correcto
    m=[i for i,x in enumerate(comprobador) if x==False]
    if m==[]:
        create(valores)
    else:
        print("no estan bien los valores: "+comprobador)

    ''' ahora hay que comprobar los datos y pasarlos al modulo de base de datos para guardarlos '''

def client_delete(builder):
    value=builder.get_object('cod')
    cod=value.get()

    print(cod)

def client_search():
    print("busca")
