
class Persona(object):
    def __init__ (self, nombre, apellido, fecha_de_nacimiento, dni, direccion ):
        self.nombre = nombre
        self.apellido = apellido
        self.__fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__ (self):
        return f'''
        nombre : {self.nombre} 
        apellido : {self.apellido}
        fecha de nacimiento : {self.__fecha_de_nacimiento }
        DNI : {self.dni} 
        direccion : {self.direccion}
        '''

    def getNombreCompleto (self):
        return f' El nombre completo de la persona es:  {self.nombre}  {self.apellido}'

    def getDia(self):
        dia_1 = self.__fecha_de_nacimiento.split ('-')
        return dia_1[0]
    def getMes(self):
        mes = self.__fecha_de_nacimiento.split ('-')
        return mes [1]
    def getAño(self):
        año = self.__fecha_de_nacimiento.split ('-')
        return año [2]

    def setDia(self, dia):
        fecha = self.__fecha_de_nacimiento.split ('-') 
        fecha [0] = dia
        #TODO: Solo te falto la asignacion de la nueva fecha a al atributo __fecha_de_nacimiento
        #TODO: self.__fecha_de_nacimiento = fecha [0] +'-'+ fecha[1]  +'-'+ fecha[2]
        #return  str (dia) +'-'+ fecha [1]+'-'+fecha [2]

    def setMes(self, mes):
        fecha = self.__fecha_de_nacimiento.split ('-') 
        fecha [1] = mes
        #return  fecha [0] +'-'+ str (mes)+'-'+fecha [2]

    def setAño(self, año):
        fecha = self.__fecha_de_nacimiento.split ('-') 
        fecha [2] = año
        #return  fecha [0] +'-'+ fecha [1]+'-'+str (año)

    def setFecha_De_Nacimiento (self, nueva_fecha_de_nacimiento):
        self.__fecha_de_nacimiento = nueva_fecha_de_nacimiento

albita = Persona ('alba', 'Herresanchez', '12-05-2002', '1234565', 'torrejon')



# print (albita)
# print (albita.getDia())
# print (albita.getMes ())
# print (albita.getAño ())
# print (albita.setDia(25))
# print (albita.setMes(9))
# print (albita.setAño(2005))

#?print (getNombreCompleto(albita))  # POR QUÉ ME DA NameError: name 'getNombreCompleto' is not defined, SI EN LA GUIA SI ME FUNCIONA

#!¿POR QUÉ EL SET ME DA NONE?, NO DEBERIA CAMBIAR LA FECHA DE NACIMIENTO CON LOS NUEVOS PARAMETROS???
#TODO: Revisa la nota que de teje en la linea 35 de este fichero
