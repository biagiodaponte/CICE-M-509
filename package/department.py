


#6.- Create a class Department with the next attributes:
#    name:str
#    telephone number: str

class Department:
    list_employee = []
    """
    def __init__(self, name, telephone_number):
        self.name = name
        self.telephone_number = telephone_number
    """
    def average_salary(self):
        employee_salary = ''
        length = len(employee_salary)
        average = sum(employee_salary) / length
        return average
    
    def employee_report(self):
        """
        dic = {'victor':25.000, 'carlos':19.500, 'kezaya':35.000, 'dakonte':50.000, 'versus':27.500, 'dariusdarik':20.500}
        salary = list(dic.values())
        salary.sort()
        print('Employee', '\t', 'Salary')
        for k in salary:
            name = list(dic.keys())[list(dic.values()).index(k)]
            if len(name) > 6:
                print(name, '\t', k)
            else:
                print(name, '\t\t', k)
        print('============================')
        return 'this is the employee report'
        """
        pass
        

    def __str__(self):
        pass

obj = Department()
print(obj.employee_report())






























