

class User (object):
    def __init__(self,email:str,clave:str,activo:bool):
        self.email=email
        self.clave=clave
        self.activo=activo
    def __str__(self):
        activostr="online" if self.activo==True else "ofline"
        return f"email: {self.email}, clave: {self.clave}, activo: {activostr}"

user1=User("qwerty@asdf","123456",True)
print(user1)