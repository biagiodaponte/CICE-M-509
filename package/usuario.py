class Usuario(object):
    #CONSTRUCTOR
    def __init__(self, email:str,clave:str,activo:bool)
        self.email = email 
        self.clave = clave 
        self.activo = activo

    def validacion(self, param_email, param_clave):
        self.email = email
        self.clave = clave 
        self.activo = False
        if(email == param_email and clave == param_clave):
            valido = True
            self.activo = True
        else:
            valido = False
            
        return valido
