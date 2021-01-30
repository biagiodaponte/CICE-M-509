
import pandas as pd

class Departamento():

    def __init__(self, nombre, telefono, lista_empleados):
        self.nombre = nombre
        self.telefono = telefono
        self.empleados = lista_empleados

    def crea_dataframe_empleado(self):
        nombres_emp = []
        salario_emp = []
        for empleado in self.empleados:
            nombres_emp.append(empleado.nombre) 
            salario_emp.append(empleado.salario)
        diccionario_de_datos = {'Nombre': nombres_emp, 'Salario': salario_emp}
        return pd.DataFrame(diccionario_de_datos)

    def media_salarial(self):
        return self.crea_dataframe_empleado()['Salario'].mean()

    def reporte_salarios(self):
        return self.crea_dataframe_empleado().sort_values('Salario', ascending=False)