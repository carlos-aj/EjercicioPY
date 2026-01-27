with open("saludo.txt", "a") as f:
    f.write("\nEsta es la segunda línea.")

with open("saludo.txt", "r") as f:
    contenido = f.read()
    total_caracteres = len(contenido)

print(f"El archivo tiene {total_caracteres} caracteres.")