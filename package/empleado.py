class Empleado (Persona,Usuario):
    #CONSTRUCTOR
    def __init__(self,salario:float,horario:str):
        self.salario = salario
        self.horario = horario