print("=== Análisis de números ===")
print("Introduce números positivos (un número negativo termina la entrada)\n")

contador = 0
suma_impares = 0
contador_impares = 0
mayor_par = None

while True:
    numero = int(input("Introduce un número: "))

    if numero < 0:
        break 
    contador += 1

    if numero % 2 == 0: 
        if mayor_par is None or numero > mayor_par:
            mayor_par = numero
    else:  
        suma_impares += numero
        contador_impares += 1

print(f"\nCantidad de números introducidos: {contador}")

if contador_impares > 0:
    media_impares = suma_impares / contador_impares
    print(f"Media de los impares: {media_impares:.2f}")
else:
    print("No se introdujeron números impares.")

if mayor_par is not None:
    print(f"El mayor de los pares es: {mayor_par}")
else:
    print("No se introdujeron números pares.")
