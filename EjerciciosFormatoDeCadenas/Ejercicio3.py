cadena = input("Introduce una cadena de texto: ")
subcadena = input("Introduce una subcadena a buscar: ")

if subcadena in cadena[0:len(subcadena)]:
    print("La cadena empienza por la subcadena.")