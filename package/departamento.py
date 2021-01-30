

from empleado import Empleado
class Departamento:
    def __init__ (self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.empleados = []

    def __str__ (self):
        return f'''
        nombre : {self.nombre} 
        telefono : {self.telefono}
        '''

    def media_salarial (self):
        sumaempleados = 0
        for x in empleados.departamento[salario]:
            sumaempleados+= x
            media = sumaempleados/ (len (self))
        return media



print (media_salarial (empleados_departamento_calidad))


#Edite la clase Departamento y agregele metodos para el calculo de la media salarial 
#     del Departamento, tambien un metodo que imprima un reporte de los empledos y sus salarios,
#     ordenados de mayor a menor en funcion de sus salarios

# 