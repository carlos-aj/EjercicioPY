cadena = input("")

lista_numeros = list(map(int, cadena.split()))

for i in range(lista_numeros[2]):
    a = i+1

    if a%lista_numeros[0] == 0 and a%lista_numeros[1] == 0:
        print("FizzBuzz")
    elif a%lista_numeros[0] == 0 and a%lista_numeros[1] != 0:
        print("Fizz")
    elif a%lista_numeros[0] != 0 and a%lista_numeros[1] == 0:
        print("Buzz")
    else:
        print(a)