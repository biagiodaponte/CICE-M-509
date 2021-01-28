class Persona():
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:str, dni:str,direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.fnacimiento = fecha_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return f'\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Fecha de nacimiento: {self.fnacimiento} \n Dni: {self.dni} \n Direccion: {self.direccion}\n'

    def getNombreCompleto(self):
        return self.nombre +' '+ self.apellido

    def getDia(self):
        dia = self.fnacimiento.split('/')
        return dia[0]
    def getMes(self):
        mes = self.fnacimiento.split('/')
        return mes[1]
    def getAño(self):
        año = self.fnacimiento.split('/')
        return año[2]

anonimo = Persona('Guillermo', 'Ginestal','7/03/89','204290350Y','Calle Avila' )

print(anonimo)
print(anonimo.getNombreCompleto())
print(anonimo.getDia())
print(anonimo.getMes())
print(anonimo.getAño())