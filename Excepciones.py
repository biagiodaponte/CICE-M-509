
#! Excepciones personalizadas de Python

class CiceError( Exception):
    def __init__(self, msg, nombre):
        self.msg = msg
        self.nombre = nombre

    def __str__(self):
        return f'hola {self.nombre}, {self.msg}'

def mi_funcion(algo = None):
    try:
        if algo == None:
            raise CiceError('Parametros no pueden ser de tipo None, por favor agrege un parametro correcto', 'Pablo')
    except CiceError as e:
        print(e)
    else:
        pass

mi_funcion(None)