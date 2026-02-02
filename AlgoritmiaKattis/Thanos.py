planetas = int(input(""))

for i in range(planetas):
    cadena = input("")
    datos = list(map(int, cadena.split()))

    if datos[0] <= datos[2]:
        contador = 1
    else:
        contador = 0
    
    while datos[0]<=datos[2]:
        datos[0] = datos[0]*datos[1]
        if datos[0] <= datos[2] :
            contador = contador + 1  

    print(contador)
