
# 6.- Cree una clase Departamento con los siguientes atributos:
#     nombre:str
#     telefono:str


class Departamento():
    def __init__(self, departamento_nombre:str, departamento_telefono:str):

        self.departamento_nombre = departamento_nombre
        self.departamento_telefono = departamento_telefono
    def __str__(self):
        return f'\n Nombre del departamento: {self.departamento_nombre}\n Teléfono del departamento: {self.departamento_telefono}'

departamento = Departamento('Calidad','916374567')
print(departamento)