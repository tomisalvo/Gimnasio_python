from tkinter import Label
from tkinter import Entry
from tkinter import Menu
from tkinter import Toplevel
from tkinter import Button
from tkinter import Text
from tkinter import END
from tkinter import Tk
from tkinter.messagebox import *
from tkinter import ttk
from controlador_gym import Ingreso, Alta_alumno, Baja_alumno, Consulta_alumno, Modificacion_alumno, Listar_alumnos



########################
###  FORMULARIO ALTA ###
########################

class Alta:
    def __init__(self, master):  #master llama a la ventana principal (root)
        self.form = Toplevel(master) #Creamos una nueva ventana con toplevel (root es la principal)
        self.form.title("Formulario de Alta") #Nombre de la ventana
        self.formulario_alta()


    def formulario_alta(self):        

        self.label_dni = Label(self.form, text = "D.N.I.")
        self.label_dni.grid(row=0, column=0, sticky="w")
        self.label_nombre = Label(self.form, text="Nombre") 
        self.label_nombre.grid(row=1, column=0, sticky="w")
        self.label_apellido= Label(self.form, text="Apellido")
        self.label_apellido.grid(row=2, column=0, sticky="w")
        self.label_direccion = Label(self.form, text="Dirección")
        self.label_direccion.grid(row=3, column=0, sticky="w")
        self.label_telefono = Label(self.form, text="Telefono")
        self.label_telefono.grid(row=4, column=0, sticky="w")
 

        self.entry_dni= Entry(self.form)
        self.entry_dni.grid(row=0, column=1)
        self.entry_nombre = Entry(self.form)  
        self.entry_nombre.grid(row=1, column=1) 
        self.entry_apellido= Entry(self.form)
        self.entry_apellido.grid(row=2, column=1)
        self.entry_direccion= Entry(self.form)
        self.entry_direccion.grid(row=3, column=1)
        self.entry_telefono= Entry(self.form)
        self.entry_telefono.grid(row=4, column=1)


    ### BOTOTNES ALTA ###

        self.boton_guardar = Button(self.form, text="Guardar", command=lambda: Alta_alumno(self.entry_dni, 
                                                                                    self.entry_nombre,
                                                                                    self.entry_apellido,
                                                                                    self.entry_direccion,
                                                                                    self.entry_telefono).guardar_alumno()
                                                                                    )
        self.boton_guardar.grid(row=7, column=1)
        self.boton_salir = Button(self.form, text="Salir", command =self.form.destroy) 
        self.boton_salir.grid( row=7, column = 7)




##########################
### FORMULARIO DE BAJA ###
##########################

class Baja:
    def __init__(self, master):
        self.form = Toplevel(master) #Creamos una nueva ventana con toplevel (root es la principal)
        self.form.title("Formulario de Baja") #Nombre de la ventana
        self.formulario_baja()

    def formulario_baja(self):      

        self.label_dni = Label(self.form, text = "D.N.I.")
        self.label_dni.grid(row=0, column=0, sticky="w")


        self.entry_dni= Entry(self.form)
        self.entry_dni.grid(row=0, column=1)



        self.boton_buscar= Button(self.form, text="Buscar", command=Baja_alumno(self.entry_dni).buscar_baja)
        self.boton_buscar.grid(row=0, column=3)
        self.boton_eliminar = Button(self.form, text="Eliminar", command=Baja_alumno(self.entry_dni).eliminar)
        self.boton_eliminar.grid(row=6, column=1)
        self.boton_salir = Button(self.form, text="Salir", command =self.form.destroy) 
        self.boton_salir.grid( row=6, column = 7)



##########################
##FORMULARIO CONSULTA ####
##########################
class Consulta:
    def __init__(self, master):
        self.form = Toplevel(master) 
        self.form.title("Formulario de Consulta") 
        self.formulario_consulta()

    def formulario_consulta(self):

        label_dni = Label(self.form, text = "D.N.I.")
        label_dni.grid(row=0, column=0, sticky="w")
    
        self.entry_dni = Entry(self.form)
        self.entry_dni.grid(row=0, column=1)

        label_nombre = Label(self.form, text = "Nombre")
        label_nombre.grid(row=1, column=0, sticky="w")
        self.valor_nombre = Label(self.form, text="")
        self.valor_nombre.grid(row=1, column=1, sticky="w")

        label_apellido = Label(self.form, text = "Apellido")
        label_apellido.grid(row=2, column=0, sticky="w")
        self.valor_apellido = Label(self.form, text="")
        self.valor_apellido.grid(row=2, column=1, sticky="w")

        label_direccion = Label(self.form, text = "Direccion")
        label_direccion.grid(row=3, column=0, sticky="w")
        self.valor_direccion = Label(self.form, text="")
        self.valor_direccion.grid(row=3, column=1, sticky="w")

        label_telefono = Label(self.form, text = "Telefono")
        label_telefono.grid(row=4, column=0, sticky="w")
        self.valor_telefono = Label(self.form, text="")
        self.valor_telefono.grid(row=4, column=1, sticky="w")

   
    
        ## BOTONES ##

        self.boton_buscar=Button(self.form, text="Buscar", command=Consulta_alumno(self.entry_dni,
                                                                                   self.valor_nombre,
                                                                                   self.valor_apellido,
                                                                                   self.valor_direccion,
                                                                                   self.valor_telefono).buscar_consulta)
        self.boton_buscar.grid(row=0, column=3)
        self.boton_limpiar=Button(self.form, text="Limpiar", command=Consulta_alumno(self.entry_dni,
                                                                                     self.valor_nombre,
                                                                                     self.valor_apellido,
                                                                                     self.valor_direccion,
                                                                                     self.valor_telefono).limpiar)
        self.boton_limpiar.grid(row=6, column=3)
        self.boton_editar=Button(self.form, text="Editar", command=lambda:Modificacion(self.form)) 
        self.boton_editar.grid(row=6, column=1) 
        self.boton_salir=Button(self.form, text="Salir", command=self.form.destroy)
        self.boton_salir.grid(row=8, column=3)



########################
##### MODIFICACION #####
########################
class Modificacion:
    def __init__(self,form):
        self.form_edit = Toplevel(form)
        self.form_edit.title("Editar Cliente")
        self.editar()

    def editar(self):
            
         
        label_nombre = Label(self.form_edit, text="Nombre") 
        label_nombre.grid(row=1, column=0, sticky="w")
        label_apellido= Label(self.form_edit, text="Apellido")
        label_apellido.grid(row=2, column=0, sticky="w")
        label_direccion = Label(self.form_edit, text="Dirección")
        label_direccion.grid(row=3, column=0, sticky="w")
        label_telefono = Label(self.form_edit, text="Telefono")
        label_telefono.grid(row=4, column=0, sticky="w")
            
        self.entry_nombre = Entry(self.form_edit)  
        self.entry_nombre.grid(row=1, column=1) 
        self.entry_apellido= Entry(self.form_edit)
        self.entry_apellido.grid(row=2, column=1)
        self.entry_direccion= Entry(self.form_edit)
        self.entry_direccion.grid(row=3, column=1)
        self.entry_telefono= Entry(self.form_edit)
        self.entry_telefono.grid(row=4, column=1)
    


            
        self.boton_guardar=Button(self.form_edit, text="Guardar", command=lambda:Modificacion_alumno(self.entry_nombre,
                                                                                                     self.entry_apellido,
                                                                                                     self.entry_direccion,
                                                                                                     self.entry_telefono,
                                                                                                     self.dni,
                                                                                                     self.form_edit
                                                                                                     ).editar_alumno()
                                  )
        self.boton_guardar.grid(row=5, column=1)
        self.boton_cancelar=Button(self.form_edit, text="Cancelar", command=self.form_edit.destroy)
        self.boton_cancelar.grid(row=5, column=2)




##########################
##### Generar LISTADO ####
##########################
class Listado:
    def __init__(self, master):
        self.form = Toplevel(master) 
        self.form.title("Generar Listado") 
        self.listar_clientes()
    
        
    def listar_clientes(self):
        self.text_resultados = Text(self.form, width=50, height=15)
        self.text_resultados.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.boton_mostrar = Button(self.form, text="Mostrar Clientes", command=Listar_alumnos(self.text_resultados).generar_listado)
        self.boton_mostrar.grid(row=0, column=0, padx=10, pady=10)
        self.boton_salir = Button (self.form, text= "Salir", command = self.form.destroy)
        self.boton_salir.grid(row=0, column =3)


###########################
#                         #
#  Formulario PRINCIPAL   #
#                         #
########################### 

class Principal():
    def __init__ (self) -> None:
        self.root = Tk()
        self.root.title("Gimnasio")
        self.formulario_principal()

    def formulario_principal(self):

        ### LABELS ####
        self.label_saludo = Label(self.root, text ="POR FAVOR INGRESE SU DNI" )
        self.label_saludo.grid(row=0, column=0, sticky="w")
        self.entry_dni= Entry(self.root)
        self.entry_dni.grid(row=0, column=2)

        self.ingreso = Ingreso(self.entry_dni)


        self.boton_ingresar= Button(self.root, text="Ingresar", command=self.ingreso.ingresar)
        self.boton_ingresar.grid(row=3, column=2)


        self.menubar = Menu(self.root)
        self.menu_cliente = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Cliente", menu=self.menu_cliente)
        self.menu_cliente.add_command(label="Alta", command=lambda:Alta(self.root))
        self.menu_cliente.add_command(label="Baja", command=lambda:Baja(self.root))
        self.menu_cliente.add_command(label="Consulta", command=lambda:Consulta(self.root))
        self.menu_cliente.add_command(label="Listado", command=lambda:Listado(self.root))
        self.menu_cliente.add_command(label="salir", command=self.root.quit)

        self.root.config(menu=self.menubar)
        self.root.mainloop()

Principal()


