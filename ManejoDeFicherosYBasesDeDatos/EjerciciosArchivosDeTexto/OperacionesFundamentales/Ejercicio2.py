with open("saludo.txt", "a") as f:
    f.write("\nEsta es la segunda línea.")

with open("saludo.txt", "rt") as f:
    contenido = f.read()
    print(contenido)