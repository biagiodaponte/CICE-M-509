
for package.persona import Persona
for package.usuario import Usuario

class Empleado:
    def __init__ (self, nombre, apellido, fecha_de_nacimiento, dni, direccion, email, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario

    def __str__ (self):
        return Persona.__str__(self) + '\n' + Usuario.__str__(self)

empleado_1 = Empleado( 'Paticia', 'Herresanchez',' 15-09-71', '223233444', 'iglesia 2', 'jfjfjffj@jfjfj','jfjfur123', True, 40000, 'partido')

print (empleado.salario)