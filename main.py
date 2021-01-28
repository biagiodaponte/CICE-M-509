
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.persona import Persona

def main():
    objeto = Persona( 'Evander', 'Lopez', "00055m", "19-7-1992","povedilla")
    

    objeto.getDia()
    print(objeto.getDia())
    print(objeto.getMes())
    print(objeto.getAño())
main()
