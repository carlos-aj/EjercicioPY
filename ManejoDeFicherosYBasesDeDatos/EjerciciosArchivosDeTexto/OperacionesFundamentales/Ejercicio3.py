lista = ["Cadena 1","Cadena 2", "Cadena 3"]

with open("lista_compra.txt", "w") as f:
    for elemento in lista:
        f.write(f"{elemento}\n")

with open("lista_compra.txt", "r") as f:
    contenido = f.read()
    print(contenido)