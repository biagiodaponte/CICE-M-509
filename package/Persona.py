# from datetime import *


class Persona(object):
    def __init__(self,nombre:str,apellido:str,fecha:str,dni:str,direccion:list):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha=fecha
        # self.fecha=datetime.strptime(fecha,"d%/m%/Y%").date()
        self.dni=dni
        self.direccion=direccion
    def __str__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}, fecha: {self.fecha}, dni: {self.dni}, direccion: {self.direccion}"
    def getNombreCompleto(self):
        return self.nombre+" "+self.apellido

javi1=Persona("javi","menendez","19/06/1998","123456789F",["Narvaez","51","4º","Izq"])
print(javi1)
print(javi1.getNombreCompleto())
# print("19/06/1998")
# print(datetime.strptime(r"19/06/1998",r"d%/m%/Y%"))