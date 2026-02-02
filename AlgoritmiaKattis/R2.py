cadena = input("")

lista_numeros = list(map(int, cadena.split()))

r_2 = 2 * lista_numeros[1] - lista_numeros[0]

print(r_2)