


#6.- Create a class Department with the next attributes:
#    name:str
#    telephone number: str
from employee import Employee

class Department:
    list_employee = []
    
    def __init__(self, name, telephone_number, employee_list):
        self.name = name
        self.telephone_number = telephone_number
        self.employee_list = employee_list
    
    def average_salary(self):
        employee_dic = {}
        for i in self.employee_list:
            employee_dic[i.__dict__['name']] = i.__dict__['salary']
        salary_list = list(employee_dic.values())
        length = len(salary_list)
        average = sum(salary_list) / length
        return f"The mean salary is {average}"

    def employee_report(self):
        employee_dic = {}
        for i in self.employee_list:
            employee_dic[i.__dict__['name']] = i.__dict__['salary']
        
        salary = list(employee_dic.values())
        salary.sort()
        print('Employee', '\t', 'Salary')
        for k in salary:
            name = list(employee_dic.keys())[list(employee_dic.values()).index(k)]
            if len(name) > 6:
                print(name, '\t', k)
            else:
                print(name, '\t\t', k)
        print('============================')
        return 'this is the employee report'
        

    def __str__(self):
        pass

"""
emp1 = Employee('Ava','Lord','F-010101-M','ava@gmail.com','AVALORD',35000,'10PM')
emp2 = Employee('Beast','Gard','M-101010-O','beas@gmail.com','bestCard',30000,'09PM')
emp3 = Employee('Cargan','Vex','M-101011-O','car@gmail.com','carGan',40000,'10AM')
emp4 = Employee('Della','Sart','F-010102-M','della@gmail.com','deSart',60000,'10PM')
emp5 = Employee('Ember','War','F-010103-M','ember@gmail.com','wArem',20000,'10AM')

obj = Department('HHRR', '917000222',[emp1,emp2,emp3,emp4,emp5])

print(obj.average_salary())
print(obj.employee_report())
"""





























