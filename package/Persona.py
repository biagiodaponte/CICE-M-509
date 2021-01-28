from datetime import *


class Persona(object):
    def __init__(self,nombre:str,apellido:str,fecha:str,dni:str,direccion:list):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha=datetime.strptime(fecha,"%d/%m/%Y")
        self.dni=dni
        self.direccion=direccion
    def __str__(self):
        fechastr=self.fecha.strftime("%d/%m/%Y")
        return f"nombre: {self.nombre}, apellido: {self.apellido}, fecha: {fechastr}, dni: {self.dni}, direccion: {self.direccion}"
    def getNombreCompleto(self):
        return self.nombre+" "+self.apellido
    def getDia(self):
        return self.fecha.day
    def getMes(self):
        return self.fecha.month
    def getAño(self):
        return self.fecha.year

    def setDia(self,dia):
        self.fecha=self.fecha.replace(day=dia)
    def setMes(self,mes):
        self.fecha=self.fecha.replace(month=mes)
    def setAño(self,año):
        self.fecha=self.fecha.replace(year=año)

javi1=Persona("javi","menendez","19/06/1998","123456789F",["Narvaez","51","4º","Izq"])
print(javi1)
print(javi1.getNombreCompleto())
print(javi1.getDia())
print(javi1.getMes())
print(javi1.getAño())

print(javi1.setDia(1))
print(javi1.setMes(11))
print(javi1.setAño(2019))

print(javi1.getDia())
print(javi1.getMes())
print(javi1.getAño())

# print("19/06/1998")
# hola=datetime.strptime("19/06/1998", "%d/%m/%Y")
# print(hola)
# print(hola.strftime("%d/%m/%Y"))