

class Departamento():
    def __init__(self, nombredepartamento, telefonodepartamento):
        self.telefono=telefonodepartamento
        self.nombre=nombredepartamento
    def __str__(self):
        return f"nombre del departamento: {self.nombre}, telefono del departamento: {self.telefono}"