print("=== Contador de números positivos y negativos ===")

positivos = 0
negativos = 0

for i in range(1, 11):
    numero = float(input(f"Introduce el número {i}: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nNúmeros positivos: {positivos}")
print(f"Números negativos: {negativos}")
