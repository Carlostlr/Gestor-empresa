# Importamos las librerias necesarias
import tkinter as tk
import pygubu

from gestores.cliente import *
from gestores.ajuste import *
from gestores.articulo import *
from gestores.factura import *
from gestores.pedido import *
from gestores.proveedor import *


# Creamos el objeto para la interface gráfica
class Aplication(pygubu.TkApplication):
    def __init__(self,root):
        #INTRODUCIMOS EL ROOT EN UNA VARIABLE
        self.master=root

#--------------------------- CREAMOS LAS FUNCIONES QUE CARGARÁN EL FRAME DE GESTION DE CADA BOTÓN ------------------------------

        def client():
            # destruimos el frame que ya existe
            self.mainwindow.destroy()

            #1: Creamos el constructor de pygubu
            self.builder=builder=pygubu.Builder()

            #2: Leemos el archivo .ui de interface grafica
            builder.add_from_file('gui/cliente.ui')

            #3: Creamos el widget usando un root como ventana
            self.mainwindow=builder.get_object('Gestor', self.master)

            #llamamos a la funcion para asignar el scrollbar al treeview
            client_treeview(builder)

            # configuramos la devolucion de las llamadas de los botones pasando por parámetro el builder
            callbacks = {
                'save': lambda:client_save(builder),
                'delete': lambda:client_delete(builder),
                'search': client_search
            }
            builder.connect_callbacks(callbacks)


        def art():
            self.mainwindow.destroy()
            #1: Creamos el constructor de pygubu
            self.builder=builder=pygubu.Builder()

            #2: Leemos el archivo .ui de interface grafica
            builder.add_from_file('gui/articulo.ui')

            #3: Creamos el widget usando un root como ventana
            self.mainwindow = builder.get_object('Gestor', self.master)

        def prov():
            self.mainwindow.destroy()
            #1: Creamos el constructor de pygubu
            self.builder=builder=pygubu.Builder()

            #2: Leemos el archivo .ui de interface grafica
            builder.add_from_file('gui/proveedor.ui')

            #3: Creamos el widget usando un root como ventana
            self.mainwindow = builder.get_object('Gestor', self.master)

        def pedi():
            self.mainwindow.destroy()
            #1: Creamos el constructor de pygubu
            self.builder=builder=pygubu.Builder()

            #2: Leemos el archivo .ui de interface grafica
            builder.add_from_file('gui/pedido.ui')

            #3: Creamos el widget usando un root como ventana
            self.mainwindow = builder.get_object('Gestor', self.master)

        def fact():
            self.mainwindow.destroy()
            #1: Creamos el constructor de pygubu
            self.builder=builder=pygubu.Builder()

            #2: Leemos el archivo .ui de interface grafica
            builder.add_from_file('gui/factura.ui')

            #3: Creamos el widget usando un root como ventana
            self.mainwindow = builder.get_object('Gestor', self.master)

        def ajust():
            self.mainwindow.destroy()
            #1: Creamos el constructor de pygubu
            self.builder=builder=pygubu.Builder()

            #2: Leemos el archivo .ui de interface grafica
            builder.add_from_file('gui/ajuste.ui')

            #3: Creamos el widget usando un root como ventana
            self.mainwindow = builder.get_object('Gestor', self.master)


#----------------------------- CARGAMOS LA GUI DEL FRAME DE LOS BOTONES -----------------------------------------


        #1: Creamos el constructor de pygubu
        self.builder=builder=pygubu.Builder()

        #2: Leemos el archivo .ui de interface grafica
        builder.add_from_file('gui/opciones.ui')

        #3: Creamos el widget usando un root como ventana
        self.mainwindow = builder.get_object('Button', self.master)

        # configuramos la devolucion de las llamadas de los botones
        callbacks = {
            'client': client,
            'art': art,
            'prov': prov,
            'pedi': pedi,
            'fact': fact,
            'ajust': ajust
        }

        builder.connect_callbacks(callbacks)

        # creamos el frame de la parte de gestion
        self.mainwindow=tk.Frame(self.master,height=400,width=600,bd=2)
        self.mainwindow.grid(row=0,column=1,padx=10,pady=10)

        #Hacemos que el tamaño del frame sea estático y no dinámico
        self.mainwindow.grid_propagate(False)

        # creamos un label con el titulo de bienvenido
        tk.Label(self.mainwindow, text="Bienvenido, seleccione una de las\n opciones para empezar.",font=("Arial",20)).grid(row=1,column=2,padx=70,pady=150)



# creamos el root y la llamada al objeto
root=tk.Tk()
app=Aplication(root)
root.mainloop()
