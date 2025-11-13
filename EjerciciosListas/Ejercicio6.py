lista = []

for i in range(15):
    numero = int(input(f"Introduce el numero {i+1}/15: "))
    lista.append(numero)

print("Lista original:", lista)

if len(lista) > 0:
    ultimo_elemento = lista[-1] 
    for i in range(len(lista) - 1, 0, -1):
        lista[i] = lista[i - 1]
    lista[0] = ultimo_elemento  

print("Lista rotada:", lista)