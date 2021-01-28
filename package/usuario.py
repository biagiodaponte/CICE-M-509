email = ""
clave = ""
activo = False

def validacion(self, param_email, param_clave):
    self.email = email
    self.clave = clave 
    if(email == param_email and clave == param_clave):
        valido = True
        self.activo = True
    else:
        valido = False
        
    return valido
