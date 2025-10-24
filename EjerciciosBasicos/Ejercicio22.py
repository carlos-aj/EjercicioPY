print("=== Calculadora de media ===")
print("Introduce números positivos. Para terminar, escribe un número negativo.\n")

suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número: "))

    if numero < 0:
        break  
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"\nLa media de los {contador} números introducidos es: {media:.2f}")
else:
    print("\nNo se introdujeron números positivos.")
