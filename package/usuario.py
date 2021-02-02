# 5.- Cree una clase Usuario con los siguientes atributos:
#     email:str
#     clave:str
#     activo:bool

# 6.- Edite la clase Usuario y agregele un metodo:
#     def validacion(self, param_email, param_clave):
#         pass
#     la funcion validacion recibe 2 parametros externos -> param_email y param_clave  
#     y revisa si son iguales con los de la clase -> self.email y self.clave
#     tambien debera verificar si ese encuentra activo o no self.activo -> ( True o False )
#     y por ultimo devuelve True en caso de que sean iguales y False en caso de que no


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