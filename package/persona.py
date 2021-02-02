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

    def setDia(self, hdia=None):
        dia = self.fnacimiento.split('/')
        if hdia == None:
            return dia[0]
        else:
            return hdia

    def setMes(self, hmes=None):
        mes = self.fnacimiento.split('/')
        if hmes == None:
            return mes[1]
        else:
            return hmes
    
    def setAño(self, haño=None):
        año = self.fnacimiento.split('/')
        if haño == None:
            return año[2]
        else:
            return haño

anonimo = Persona('Guillermo', 'Ginestal','7/03/1989','204290350Y','Calle Avila' )

print(anonimo)
print(anonimo.getNombreCompleto())
print(anonimo.getDia())
print(anonimo.getMes())
print(anonimo.getAño())
print(anonimo.setDia(16))
print(anonimo.setDia(12))
print(anonimo.setDia(1988))

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


class Departamento():
    def __init__(self, departamento_nombre:str, departamento_telefono:str):

        self.departamento_nombre = departamento_nombre
        self.departamento_telefono = departamento_telefono
    def __str__(self):
        return f'\n Nombre del departamento: {self.departamento_nombre}\n Teléfono del departamento: {self.departamento_telefono}'

departamento = Departamento('Calidad','916374567')
print(departamento)

class Empleado(Persona, Usuario):
    
    def __init__(self, salario:float, horario:str, email, contraseña ):
        Usuario.__init__(self,  email, contraseña)
        self.salario = salario
        self.horario = horario
    #def __float__(self):
    #    return f'\n Salario: {self.salario}

    def __str__(self):
        return f'\n Horario: {self.horario} {self.email } {self.contraseña } {self.salario }'

e1 = Empleado(1235,18, 'email', 'contraseña')

print('AQUI ES CHAMITO:',e1)
