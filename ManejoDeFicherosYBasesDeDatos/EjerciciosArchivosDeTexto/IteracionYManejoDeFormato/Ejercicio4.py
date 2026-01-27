with open("perfiles.txt", "w", encoding="utf-8") as archivo:
    nombres = input("Introduce nombre(s) separados por comas: ").split(",")
    edades = input("Introduce edad(es) separadas por comas: ").split(",")
    ciudades = input("Introduce ciudad(es) separadas por comas: ").split(",")

    archivo.write(f"nombre: {nombres}\n")
    archivo.write(f"edad: {edades}\n")
    archivo.write(f"ciudad: {ciudades}\n")
    archivo.write("\n")

