
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.persona import Persona

def main():
    yo = Persona('Isabel', 'Repetto', '12-02-1991', '56432865P', "Tailor's Court")

    print(yo.getDia())
    print(yo.getMes())
    print(yo.getAño())
    yo.setDia(22)
    print(yo)

main()