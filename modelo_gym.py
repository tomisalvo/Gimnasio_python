import sqlite3
import re
from regex_gym import patron1, patron2, patron3
from tkinter import messagebox
from peewee import *

db = SqliteDatabase("gimnasio1.db")

class BaseModel(Model):
    class Meta:
        database = db

class Alumnos(BaseModel):
    dni = IntegerField(primary_key = True)
    nombre = CharField()
    apellido = CharField()
    direccion = CharField()
    telefono = IntegerField()
db.connect()
db.create_tables([Alumnos])


class Crud():

    def alta_alumno(self, dni, nombre, apellido, direccion, telefono):
            alumno = Alumnos() 
            alumno.dni=int(dni)
            alumno.nombre=nombre
            alumno.apellido=apellido
            alumno.direccion=direccion
            alumno.telefono=int(telefono)
            alumno.save()
            messagebox.showinfo("Éxito", "Datos guardados correctamente")

    def eliminar_alumno(self,dni):
        try:
            alumno = Alumnos.get(Alumnos.dni == dni)
            alumno.delete_instance()
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente")
        except Alumnos.DoesNotExist:
            messagebox.showerror("Error", "No existe un alumno con ese DNI")

        

        

    def modificacion_alumno(self, dni, nombre, apellido, direccion, telefono):
        acutalizar= (Alumnos.update(nombre = nombre,
                                   apellido = apellido,
                                   direccion = direccion,
                                   telefono = telefono
                                   ).where(Alumnos.dni == dni)
                     )
        actualizar.execute()


    def consulta_alumno(self, dni):
        try:
            alumno = Alumnos.get(Alumnos.dni == dni)
            return (alumno.nombre, alumno.apellido, alumno.direccion, alumno.telefono)  
        except Alumnos.DoesNotExist:
            messagebox.showerror("Error", "No existe un alumno con ese DNI")
            return None


    def mostrar_listado(self):
        alumnos = Alumnos.select(Alumnos.dni, Alumnos.nombre, Alumnos.apellido)
        resultado = [(alumno.dni, alumno.nombre, alumno.apellido) for alumno in alumnos]
        return resultado


     
    def select_alumno(self, dni):
        try:
            alumno = Alumnos.get(Alumnos.dni == dni)
            return (alumno.nombre, alumno.apellido)
        except Alumnos.DoesNotExist:
            messagebox.showerror("Error", "No existe un alumno con ese DNI")
            return None