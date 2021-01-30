
from package.persona import Persona 
from package.usuario import Usuario
from package.departamento import Departamento


class Empleado(Persona, Usuario):

    def __init__(self, nombre, apellido, fecha_nacimiento, dni, direccion, email, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario

    def __str__(self):
        print(f'\nLos datos que hereda de Persona son: {Persona.nombre}-{Persona.apellido}-{Persona.fecha_nacimiento}-{Persona.dni}-{Persona.direccion}')
        print(f'\nLos datos que hereda de Usuario son: {Usuario.email}-{Usuario.clave}-{Usuario.activo}')
        print(f'\nLos datos propios de la clase Empleado son: {self.horario}-{self.salario}')