
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from package.persona import Persona
from package.empleado import Empleado
from package.departamento import Departamento

# def main():
#     pass
# main()



departamento_calidad = Departamento ('calidad', '987654321')

empleado_1 = Empleado( 'Patricia', 'Herresanchez',' 15-09-71', '223233444T', 'iglesia 2', 'patricia@gmail.com','jfjfur123', True, 40000, 'partido')
empleado_2 = Empleado ('pepe', 'perez', '12-07-1980', '12345678K', 'real 30', 'pepe@gmail.com', '12345', True, 50000, 'mañana')
empleado_3 = Empleado ('maria', 'lopez', '18-10-1970', '176894045K', 'cordillera 39', 'maria@gmail.com', '67584', True, 45000, 'mañana')
empleado_4 = Empleado ('jose', 'martin', '22-07-1990', '123458765H', 'blanco 30', 'jose@gmail.com', '9875766', True, 30000, 'partido')
empleado_5 = Empleado ('ana', 'sanchez', '14-07-1985', '123484567P', 'Sepulveda 80', 'ana@gmail.com', '12678', True, 420000, 'tarde')
empleado_6 = Empleado ('eva', 'fernandez', '12-01-1986', '12398778L', 'corredera 10', 'eva@gmail.com', '129889', True, 55000, 'tarde')
empleado_7 = Empleado( 'Antonio', 'ruiz',' 15-09-67', '22765894T', 'lanuza 11', 'antonio@gmail.com','123423', True, 40000, 'partido')
empleado_8 = Empleado ('elena', 'rincon', '08-05-1980', '12345678K', 'arroyo 30', 'elena@gmail.com', '98745', True, 50000, 'mañana')
empleado_9 = Empleado ('mariano', 'rojo', '18-10-1990', '98756045K', 'la paz 99', 'mariano@gmail.com', '98764', True, 45000, 'tarde')
empleado_10 = Empleado ('luis', 'sanz', '29-12-1999', '123498675H', 'pinar 30', 'luis@gmail.com', '7658476', True, 30000, 'partido')

print (empleado_1.salario)
print(empleado_1)


# empleados_departamento_calidad = [[empleado_1], [empleado_4], [empleado_8]]

# media_salarial (empleados.departamento_calidad)


#?File "/Users/patricia/Desktop/practicas_cice/CICE-M-509/main.py", line 4, in <module>
    #?from persona import Persona
#?ModuleNotFoundError: No module named 'persona'

