
class Persona():   
    def __init__(self, nombre:str, apellido:str, fecha_de_nacimiento:str, dni:str, direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return f'\n{self.nombre}\n{self.apellido}\n{self.fecha_de_nacimiento}\n{self.dni}\n{self.direccion}\n'

    def getNombreCompleto(self):
        return self.nombre + ' ' + self.apellido
            


individuo = Persona('Ramon', 'De Pitis', '21-2-1968', '53728994T', 'Calle caballo' )

print(individuo)
print(individuo.getNombreCompleto())