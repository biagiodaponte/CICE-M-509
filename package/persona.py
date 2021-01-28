import datetime

class Persona(object):
    #CONSTRUCTOR
    def __init__(self,nombre:str,apellido:str,fecha_nacimiento:datetime,dni:str,direccion:str)
    self.nombre = nombre
    self.apellido = apellido
    self.fecha_nacimiento = fecha_nacimiento
    self.dni = dni
    self.direccion = direccion  

    #imprimir nombre 
    def getNombreCompleto(self):
        self.nombre = nombre
        self.apellido = apellido
        res = nombre + apellido
        print(res)

    def fecha(self,dia,mes,anio):
        nueva = datetime.date(anio,mes,dia)
        print(nueva)

