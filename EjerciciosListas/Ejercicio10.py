import random

lista_numeros = []
for i in range(10):
    numero = random.randint(0, 100)
    lista_numeros.append(numero)

print("Lista generada:", lista_numeros)

while True:
    try:
        numero_usuario = int(input("Introduce un número que esté en la lista: "))
        
        if numero_usuario in lista_numeros:
            print(f"¡Correcto! El número {numero_usuario} está en la lista.")
            break
        else:
            print(f"El número {numero_usuario} no está en la lista. Inténtalo de nuevo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

posicion_numero = lista_numeros.index(numero_usuario)
print(f"El número {numero_usuario} está en la posición {posicion_numero}")

rotaciones = 0
while lista_numeros[0] != numero_usuario:
    ultimo_elemento = lista_numeros.pop()
    lista_numeros.insert(0, ultimo_elemento)
    rotaciones += 1

print(f"Se realizaron {rotaciones} rotaciones hacia la derecha.")
print("Lista rotada:", lista_numeros)
