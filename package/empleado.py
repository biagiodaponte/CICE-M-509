# 7.- Cree una clase Empleado que herede de Persona y Usuario, adicionalmente posea el atributo:
# #     salario:float
# #     horario:str

from persona import Persona
from usuario import Usuario

class Empleado(Persona, Usuario):
    
    def __init__(self, salario:float, horario:str, email, contraseña ):
        Usuario.__init__(self,  email, contraseña)
        self.salario = salario
        self.horario = horario

    def __str__(self):
        return f'\n Horario: {self.horario}\n Email: {self.email }\n Contraseña: {self.contraseña }\n Salario: {self.salario }'

e1 = Empleado('1400 euros','8:00 a 18:00', 'willyg.ginestal@gmail.com', '101010')

print('Información del empleado Guillermo Ginestal:\n',e1)