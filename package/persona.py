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

    # def setDia(self,dia):
    #     self.fnacimiento = self.fnacimiento.replace(dia = dia)
    # def setMes(self,mes):
    #     self.fnacimiento = self.fnacimiento.replace(mes = mes)
    # def setAño(self,año):
    #     self.fnacimiento = self.fnacimiento(año = año)

anonimo = Persona('Guillermo', 'Ginestal','7/03/1989','204290350Y','Calle Avila' )

    

print(anonimo)
print(anonimo.getNombreCompleto())
print(anonimo.getDia())
print(anonimo.getMes())
print(anonimo.getAño())
# print(anonimo.setDia(1))
# print(anonimo.setMes(11))
# print(anonimo.setAño(2019))

class Usuario:
    email = 'willyg.ginestal@gmail.com'
    contraseña = '101010'
    activo = True
    
    def __init__(self, email, contraseña):
        self.email = email
        self.contraseña = contraseña

    def validation(self, param_email, param_contraseña):
        if (self.email == param_email) and (self.contraseña == param_contraseña):
            return True
        else:
            return False
    
    
anonimo = Usuario('menganito@gmail.com', 'contra')
print(anonimo.validation('willyg.ginestal@gmail.com', '101010'))
