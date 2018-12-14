#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import tkinter as tk
from tkinter import messagebox
import pygubu
from gestores.bbdd.conexion import *
from conf_inicio import *
from general.archivos import *


# Creamos el objeto para la interface gráfica
class Aplication(pygubu.TkApplication):
    def __init__(self,root):
        #INTRODUCIMOS EL ROOT EN UNA VARIABLE
        self.master=root

        #creamos una variable para el numero de intentos, hay que crearla fuera de la funcion accede porque sino no se guarda el resultado
        self.intentos=0
#--------------------------- CREAMOS LAS FUNCIONES QUE CARGARÁN EL FRAME DE GESTION DE CADA BOTÓN ------------------------------

        def accede(builder):
            #creamos una lista en la que meteremos todos los valores obtenidos
            valores=[]
            # obtenemos los valores que tenemos en cada campo
            value=builder.get_object('user')
            #añade el valor obtenido a la lista
            valores.append(value.get())

            value=builder.get_object('passw')
            valores.append(value.get())

            value=builder.get_object('server')
            valores.append(value.get())

            acces=conex(valores)

            #comprobamos si hemos accedido a la base de datos correctamente o no
            if acces[0]==True:
                root.destroy()

                dexc(acces[1],acces[2])

                #con esto borramos la contraseña de la lista y guardamos el nombre y el servidor en el archivo acces para que al abrirlo lo ponga automaticamente
                valores.pop(1)

                str1=escribe("acces",valores)

                #Llamamos a la funcion del gestor
                gestor(valores[0])

            else:
                #como se ha fallado al poner alguno de los datos le suma 1 a la variable self.intentos, mientras sea el numero mas pequeño de 2 se podrá intentar acceder
                self.intentos=self.intentos+1
                if self.intentos<=2:
                    messagebox.showwarning("Alerta","Alguno de los datos introducidos no es correcto, por favor, intentalo de nuevo")
                else:
                    messagebox.showwarning("Alerta","Has fallado demasiadas veces, este programa se cerrará")
                    root.destroy()
#----------------------------- CARGAMOS LA GUI DEL FRAME DE LOS BOTONES -----------------------------------------


        #1: Creamos el constructor de pygubu
        self.builder=builder=pygubu.Builder()

        #2: Leemos el archivo .ui de interface grafica
        builder.add_from_file('gui/login.ui')

        #3: Creamos el widget usando un root como ventana
        self.mainwindow = builder.get_object('login-frame', self.master)

        #-----------------------------------------lectura del archivo acces-------------------------------------------

        # llamamos a la funcion acces para que nos cree/lea el archivo
        str1=lee("acces")

        try:
            # insertamos los valores guardados en cada campo
            value=builder.get_object('user')
            value.insert(0,str1[0])

            value=builder.get_object('server')
            value.insert(0,str1[1])

        except:
            print("No hay nada")
        #-----------------------------------------------------------------------------------------------------

        # configuramos la devolucion de las llamadas de los botones
        callbacks = {
            'accede': lambda:accede(builder)
        }

        builder.connect_callbacks(callbacks)


# creamos el root y la llamada al objeto
root=tk.Tk()
#le damos un titulo, que no se pueda redimensionar con 0,0 y le asignamos un icono
root.title("Gestor")
root.resizable(0,0)

# Obtiene los valores height and widht de la pantalla.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
windowWidth=windowWidth+300
windowHeight=windowHeight+300


# Obtiene la mitad del ancho/alto de la pantalla y el ancho/alto de la ventana
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Posiciona la ventana en el centro de la pantalla
root.geometry("+{}+{}".format(positionRight, positionDown))


app=Aplication(root)

root.mainloop()
