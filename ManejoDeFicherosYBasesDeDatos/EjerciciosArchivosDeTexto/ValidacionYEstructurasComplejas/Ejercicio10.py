with open("archivo_original.txt", "r") as f:
    contenido = f.read()

palabras = contenido.split()
total_palabras = len(palabras)

print(f"Número total de palabras encontradas: {total_palabras}")
print(f"\nPalabras: {palabras}")
