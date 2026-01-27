import os

print(os.listdir())

archivo = input("Introduzca el nombre del archivo que desea buscar: ")

if os.path.exists(archivo):
    print(f"El archivo {archivo} existe")