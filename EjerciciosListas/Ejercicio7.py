import random

numeros = [random.randint(0, 20) for _ in range(100)]

print("Números generados:")
print(*numeros)

valor_buscar = int(input("\nIngrese el valor a buscar: "))
valor_reemplazar = int(input("Ingrese el valor de reemplazo: "))

numeros_modificados = []
for numero in numeros:
    if numero == valor_buscar:
        numeros_modificados.append(f'"{valor_reemplazar}"')
    else:
        numeros_modificados.append(str(numero))

print("\nLista modificada:")
print(*numeros_modificados)