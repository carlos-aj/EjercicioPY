with open("saludo.txt", "wt") as f:
    f.write("Hola, me encanta Python")

with open("saludo.txt", "rt") as f:
    contenido = f.read()
    print(contenido)