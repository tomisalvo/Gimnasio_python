from modelo_gym import Crud
import re
from tkinter import messagebox, END
import sqlite3






    ###########################
    #                         #
    #  Formulario PRINCIPAL   #
    #                         #
    ########################### 
class Ingreso:

    def  __init__(self, entry_dni):
        self.entry_dni= entry_dni
        self.crud = Crud()



    def ingresar(self):
        cliente = self.entry_dni.get().strip() #OBTENGO EL DNI
        if not re.match(r"^\d{8}$", cliente):
            messagebox.showerror("Error", "El DNI debe tener exactamente 8 dígitos numéricos")
            self.entry_dni.delete(0, END)
            return  # corto la función si el DNI no es válido
    
        resultado = self.crud.select_alumno(cliente)

        if resultado:
                nombre, apellido = resultado
                messagebox.showinfo("Bienvenido", f"{nombre} {apellido}, disfrute su entrenamiento")
        else:
                messagebox.showerror("Aviso", "Acceso Denegado")

        self.entry_dni.delete(0, END)


########################
###  FORMULARIO ALTA ###
########################
class Alta_alumno:

    def __init__(self, entry_dni, entry_nombre, entry_apellido, entry_direccion, entry_telefono):       
        self.entry_dni = entry_dni
        self.entry_nombre =entry_nombre
        self.entry_apellido = entry_apellido
        self.entry_direccion = entry_direccion
        self.entry_telefono = entry_telefono
        self.crud = Crud()



    def guardar_alumno(self):
        dni = self.entry_dni.get()
        nombre =self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        try:
            self.crud.alta_alumno( dni, nombre, apellido, direccion, telefono)

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "DNI ya existente")

        self.entry_dni.delete(0, END)
        self.entry_nombre.delete(0, END)
        self.entry_apellido.delete(0, END)
        self.entry_direccion.delete(0, END)
        self.entry_telefono.delete(0, END)

              
##########################
### FORMULARIO DE BAJA ###
##########################
class Baja_alumno:
    def __init__(self, entry_dni):
        self.entry_dni= entry_dni
        self.crud = Crud()


    def buscar_baja(self):
        dni =self.entry_dni.get().strip()
        if not dni:
         messagebox.showwarning("Aviso", "Ingrese un DNI para buscar")
         return
    
        resultado= self.crud.select_alumno(dni)
      
        if resultado:
                nombre, apellido = resultado
                messagebox.showinfo("Cliente encontrado", f"DNI: {dni}\nNombre: {nombre}\nApellido: {apellido}")
                return resultado
        else:
                return None


    def eliminar(self):
        dni = self.entry_dni.get().strip()
        if not dni:
            messagebox.showwarning("Aviso", "Ingrese un DNI para eliminar cliente")
            return
        self.crud.eliminar_alumno(dni)
        self.entry_dni.delete(0, END)



##########################
##FORMULARIO CONSULTA ####
##########################

class Consulta_alumno:
    def __init__(self,entry_dni, valor_nombre, valor_apellido, valor_direccion, valor_telefono):
        self.entry_dni= entry_dni
        self.valor_nombre = valor_nombre
        self.valor_apellido = valor_apellido
        self.valor_direccion = valor_direccion
        self.valor_telefono = valor_telefono
        self.crud = Crud()
        
    def buscar_consulta(self):
        dni = self.entry_dni.get().strip()
        if not dni:
            messagebox.showwarning("Aviso", "Ingrese un DNI para buscar")
            return
    
        resultado = self.crud.consulta_alumno(dni)

        if resultado:
           nombre, apellido, direccion, telefono = resultado
           self.valor_nombre.config(text=nombre)
           self.valor_apellido.config(text=apellido)
           self.valor_direccion.config(text=direccion)
           self.valor_telefono.config(text=telefono)
        else:
            return None
            self.limpiar()

    def limpiar(self):
        self.entry_dni.delete(0, END)
        self.valor_nombre.config(text="")
        self.valor_apellido.config(text="")
        self.valor_direccion.config(text="")
        self.valor_telefono.config(text="")


#################
##  EDITAR ######
#################
class Modificacion_alumno:
    def __init__(self,form_edit, dni, entry_nombre, entry_apellido, entry_direccion, entry_telefono):
        self.dni = dni
        self.entry_nombre = entry_nombre
        self.entry_apellido = entry_apellido
        self.entry_direccion = entry_direccion
        self.entry_telefono = entry_telefono
        self.form_edit = form_edit
        self.crud = Crud()

    def editar_alumno(self):

                editar = messagebox.askquestion("Confirmar", "¿Está seguro de modificar la información?")
                if editar == "yes":

                    nombre = self.entry_nombre.get()
                    apellido = self.entry_apellido.get()
                    direccion = self.entry_direccion.get()
                    telefono = self.entry_telefono.get()

                    self.crud.modificacion_alumno(self.dni, nombre, apellido, direccion, telefono)
                    messagebox.showinfo("Éxito", "Datos actualizados correctamente")
                    self.form_edit.destroy()            
                else:
                    messagebox.showwarning("Cancelar", "La operación fue cancelada.")


##########################
##### Generar LISTADO ####
##########################
class Listar_alumnos:
    def __init__(self,text_resultados):
        self.text_resultados = text_resultados
        self.crud = Crud()


    def generar_listado(self):    
        self.text_resultados.delete("1.0", END)
        resultados = self.crud.mostrar_listado()
      

        if resultados:
            for dni, nombre, apellido in resultados:
                self.text_resultados.insert(END, f"{dni} - {nombre} {apellido}\n")
        else:
                self.text_resultados.insert(END, "No hay clientes registrados.\n")
