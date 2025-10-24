cadena = input("Introduce una cadena:")
resultado = ""

cadena = cadena.split(" ")

for i in range(len(cadena)):
    cadena[i] = cadena[i].capitalize()
    
resultado = " ".join(cadena)

print(resultado)