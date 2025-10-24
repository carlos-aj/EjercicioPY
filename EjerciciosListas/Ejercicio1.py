import random

vector_numeros = []

for i in range(10):
    vector_numeros.append(int(random.randrange(1,10)))

for i in range(len(vector_numeros)):
    print(f"Normal: {vector_numeros[i]} - Cuadrado: {vector_numeros[i]**2} - Cubo: {vector_numeros[i]**3}")