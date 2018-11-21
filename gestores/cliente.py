import tkinter as tk
import pygubu

from gestores.bbdd.graba import *

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

    # obtenemos los valores que tenemos en cada campo
    value=builder.get_object('cod')
    valores.append(value.get())

    value=builder.get_object('nombre')
    valores.append(value.get())

    value=builder.get_object('empre')
    valores.append(value.get())

    value=builder.get_object('direc')
    valores.append(value.get())

    value=builder.get_object('cp')
    valores.append(value.get())

    value=builder.get_object('pobl')
    valores.append(value.get())

    value=builder.get_object('prov')
    valores.append(value.get())

    value=builder.get_object('telf')
    valores.append(value.get())

    value=builder.get_object('mail')
    valores.append(value.get())

    value=builder.get_object('fax')
    valores.append(value.get())

    print(valores)
    ''' ahora hay que comprobar los datos y pasarlos al modulo de base de datos para guardarlos '''

def client_delete(builder):
    value=builder.get_object('cod')
    cod=value.get()

    print(cod)

def client_search():
    print("busca")
