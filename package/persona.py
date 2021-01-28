

class Persona:
    def __init__(self , nombre:str,apellido:str,dni:str,fecha_de_nacimiento:str,direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni 
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.direccion = direccion

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


nombreapellido = Persona( 'Evander', 'Lopez', "00055m", "1-5-1850","povedilla")
print(nombreapellido)