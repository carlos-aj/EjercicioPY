combinacion_correcta = 1234

intentos = 4

print("=== Caja Fuerte ===")
print("Tienes 4 intentos para adivinar la combinación de 4 cifras.\n")

for i in range(intentos):
    intento = int(input(f"Introduce la combinación (intento {i+1}/{intentos}): "))

    if intento == combinacion_correcta:
        print("¡La caja fuerte se ha abierto!")
        break
    else:
        print("Lo siento, esa no es la combinación.\n")
else:
    print("Has agotado los 4 intentos. La caja fuerte sigue cerrada.")
