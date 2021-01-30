
from package.persona import Persona
from package.usuario import Usuario
from package.empleado import Empleado
from package.departamento import Departamento


def main():

    yo = Persona('Isabel', 'Repetto', '12-02-1991', '56432865P', "Tailor's Court")
    print(f'Dia: {yo.getDia()}')
    print(f'Mes: {yo.getMes()}')
    print(f'Año: {yo.getAño()}')
    
    yo.setDia(22)
    print(f'\nDatos de Persona despues de modificar la fecha de nacimiento:\n{yo}')

    yo = Usuario('isargp@gmail.com', 'clavecita', False)
    print(f"Validacion: {yo.validacion('isargp@gmail.com', 'clavecita')}\n")

    emp0 = Empleado('Isabel', 'Repetto', '12-02-1991', '46372836P','Bristol','isargp@gmail.com', '2424g3vcc', False, 1240.0, '8:00-15:00' )
    emp1 = Empleado('Veronica', 'Salguero', '04-11-1993', '52343655H','Madrid','verosh@gmail.com', 'pepito', False, 1500.0, '8:00-16:00' )
    emp2 = Empleado('Patricia', 'Herresanchez', '13-08-1993', '36476888S','Segovia','patrihf@gmail.com', '44raton55', True, 1401.5, '8:00-15:30' )
    emp3 = Empleado('Benjamin', 'Peñaloza', '07-11-1986', '56151277P','Venezuela','benjaminp@gmail.com', 'chamos2020', False, 1240.0, '8:00-15:00' )
    emp4 = Empleado('Jose Antonio', 'Martinez', '15-07-1936', '02344327L','Andorra','joseantoniom@gmail.com', 'covid-19', True, 1612.25 ,'8:00-16:30' )
    emp5 = Empleado('Manuel', 'Gil', '01-03-1990', '46663236P','Madagascar','manuelg@gmail.com', 'alarmaaaa', True, 1401.5, '8:00-15:30' )
    emp6 = Empleado('John', 'Baileys', '22-05-1992', '291737637H','Manchester','johnb@gmail.com', 'muchodrama', False, 1500.0, '8:00-16:00' )
    emp7 = Empleado('Pepa', 'Pig', '24-04-1985', '98272133S','Durham on Sea','pepapig@gmail.com', 'oingoing', True, 1240.0, '8:00-15:00' )
    emp8 = Empleado('Dora', 'Exploradora', '31-01-1996', '92334657D','La isla de las tentaciones','doraexploradora@gmail.com', 'haymasvideosparati', False, 1401.5, '8:00-15:30' )
    
    
    departamento_programacion = Departamento('Programación Python', '911652637', [emp0,emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8])

    print(f'Media: {departamento_programacion.media_salarial():.2f}\n')
    print(f'Reporte salarial del departamento "{departamento_programacion.nombre}" ordenado de mayor a menor salario:\n{departamento_programacion.reporte_salarios()}')



main()