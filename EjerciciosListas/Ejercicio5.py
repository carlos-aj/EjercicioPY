matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(len(matriz)):
    suma_fila = sum(matriz[i])
    print(f"Suma de la fila {i+1}: {suma_fila}")

print()

for j in range(len(matriz[0])):
    suma_columna = sum(matriz[i][j] for i in range(len(matriz)))
    print(f"Suma de la columna {j+1}: {suma_columna}")