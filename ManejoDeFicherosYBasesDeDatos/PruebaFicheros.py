import os

with open("hola.txt", "at") as f:
    f.write("Hola mundo!\n")

with open("hola.txt", "r") as f:
    contenido = f.read()
    print(contenido)

print(os.listdir())