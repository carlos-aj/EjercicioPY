import Validaciones

cadena = input("Introduce una cadena:")
               
caracter1 = Validaciones.leer_caracter()
caracter2 = Validaciones.leer_caracter()

for i in range(len(cadena)):
    if cadena[i] == caracter1:
        cadena = cadena[:i] + caracter2 + cadena[i+1:]

print(cadena)