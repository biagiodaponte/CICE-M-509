
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.employee import Employee
from package.department import Department

def main():
    emp1 = Employee('Ava','Lord','F-010101-M','ava@gmail.com','AVALORD',35000,'10PM')
    emp2 = Employee('Beast','Gard','M-101010-O','beas@gmail.com','bestCard',30000,'09PM')
    emp3 = Employee('Cargan','Vex','M-101011-O','car@gmail.com','carGan',40000,'10AM')
    emp4 = Employee('Della','Sart','F-010102-M','della@gmail.com','deSart',60000,'10PM')
    emp5 = Employee('Ember','War','F-010103-M','ember@gmail.com','wArem',20000,'10AM')

    obj = Department('HHRR', '917000222',[emp1,emp2,emp3,emp4,emp5])

    return obj.employee_report()

main()
