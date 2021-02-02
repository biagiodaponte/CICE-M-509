from persona import Persona
from departamento import Departamento
# print(type(Persona),Persona)

class Empleado(Persona,Departamento):
    def __init__(self,nombre:str,apellido:str,fecha:str,dni:str,direccion:list,nombredepartamento, telefonodepartamento, salario,horario):
        self.datos_persona=Persona(nombre,apellido,fecha,dni,direccion)
        self.pertenece_departamento=Departamento(nombredepartamento, telefonodepartamento,self)
        self.salario=salario
        self.horario=horario
    def __str__(self):
        return f"Persona:\n{self.datos_persona}\nDepartamento:\n{self.pertenece_departamento}\nempleado:\nsalario: {self.salario}, horario: {self.horario}"

empleado1=Empleado("juan","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")
print(empleado1)

empleado2=Empleado("pepe","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")
print(empleado2)

empleado3=Empleado("sara","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
print(empleado3)

empleado4=Empleado("susana","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
print(empleado4)

empleado5=Empleado("ana","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
print(empleado5)

print(empleado5.pertenece_departamento.departYemplea)
print(empleado1.pertenece_departamento.departYemplea)



