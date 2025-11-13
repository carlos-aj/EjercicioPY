import Validaciones

notas = []
media = 0
mayor = -1
menor = 11

for i in range(10):
    notas.append(Validaciones.leer_numero_entero_con_minimo_y_maximo(f"Introduce la nota 0-10 {i+1}/10:", "La nota de debe de ser entre 0 y 10. Intentalo de nuevo:", 0, 10))
    media += notas[i]
    if notas[i] > mayor:
        mayor = notas[i]
    if notas[i] < menor:
        menor = notas[i]

print("Notas introducidas:")
print(" ".join(map(str,notas)))
print(f"La media de las notas es: {media/10}")
print(f"La nota mayor es: {mayor}")
print(f"La nota menor es: {menor}")