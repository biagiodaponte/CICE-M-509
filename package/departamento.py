

class Departamento():
    departYemplea=dict()
    def __init__(self, nombredepartamento, telefonodepartamento, empleadoobj):
        self.telefono=telefonodepartamento
        self.nombre=nombredepartamento
        if self.nombre not in self.departYemplea:
            self.departYemplea[self.nombre]=[]
        self.departYemplea[self.nombre].append(empleadoobj)
    def __str__(self):
        return f"nombre del departamento: {self.nombre}, telefono del departamento: {self.telefono}"