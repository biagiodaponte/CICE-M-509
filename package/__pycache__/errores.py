

try:
    edad = int(input("escribe tu edad:"))
    if edad>18:
        print("eres adulto")

    else:
        print("eres un baby")
except ValueError:
    print("debes ingresar un numero")