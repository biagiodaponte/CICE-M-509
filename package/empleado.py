
from .persona import Persona
from .usuario import Usuario

class Empleado(Persona, Usuario):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion, email, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario
        self.departamento = 'sin asignar'

    def __str__ (self):
        return Persona.__str__(self) + '\n' + Usuario.__str__(self) + '\n' #+ 'salario:' {self.salario} + '\n' + 'horario:' {self.horario} +'\n' + 'departamento:' {self.departamento}
