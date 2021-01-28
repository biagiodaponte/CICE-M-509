class Persona():
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:str, dni:str,direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.fnacimiento = fecha_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return f'\n {self.nombre}  {self.apellido} \n'


anonimo = Persona('Guillermo', 'Ginestal','7/03/89','204290350Y','calle' )

print(anonimo)