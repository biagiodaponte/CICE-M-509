
class Departamento:
    def __init__ (self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__ (self):
        return f'''
        nombre : {self.nombre} 
        telefono : {self.telefono}
        '''