import random

numeros = [random.randint(0, 100) for _ in range(20)]

print("Lista original:")
print(numeros)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros_reorganizados = pares + impares

print("\nLista reorganizada (pares primero, impares después):")
print(numeros_reorganizados)

print(f"\nCantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")