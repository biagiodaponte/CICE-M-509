
class Persona():   
    def __init__(self, nombre:str, apellido:str, fecha_de_nacimiento:str, dni:str, direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return f'\n {self.nombre} {self.apellido} {self.fecha_de_nacimiento} {self.dni} {self.direccion} \n'
            


individuo = Persona('Ramon', 'De Pitis', '21-2-1968', '53728994T', 'Calle caballo' )

print(individuo)