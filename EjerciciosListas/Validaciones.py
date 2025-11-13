def leer_numero_entero(mensaje="Introduce un numero:", error="No se introdujo un numero"):
    """Pide un numero entero por teclado, 
    hasta que no se introduzca tal numero 
    no saldrá del bucle
    """
    while(True):
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print(error)

def leer_numero_entero_con_minimo(mensaje="Introduce un numero mayor a {minimo}:", error="No se introdujo un numero mayor a {minimo}:", minimo=5):
    """Pide un numero entero mayor a un minimo 
    por teclado, hasta que no se introduzca 
    tal numero no saldrá del bucle
    """

    mensaje = mensaje.format(minimo=minimo)
    error = error.format(minimo=minimo)
    while(numero:= leer_numero_entero(mensaje, error)) < minimo:
        pass
    return numero

def leer_numero_entero_con_minimo_y_maximo(mensaje="Introduce un numero mayor a {minimo} y menor a {maximo}:", error="No se introdujo un numero mayor a {minimo} y mayor a {maximo}:", minimo = 0, maximo= 5):
    """Pide un numero entero mayor a un minimo 
    y menor a un maximo por teclado, hasta 
    que no se introduzca tal numero no 
    saldrá del bucle
    """
    
    mensaje = mensaje.format(minimo=minimo, maximo=maximo)
    error = error.format(minimo=minimo, maximo=maximo)

    while(numero:= leer_numero_entero(mensaje, error)) < minimo or numero > maximo:
        pass
    return numero

def leer_caracter(mensaje="Introduce un caracter:", error="No se introdujo un caracter"):
    """Pide un caracter por teclado, 
    hasta que no se introduzca tal 
    caracter no saldrá del bucle
    """

    try:
        caracter = input(mensaje)
        return caracter
    except IndexError:
        print(error)

def leer_caracter_especifico(mensaje="Introduce el caracter {caracter}:", error="No se ha introducido el caracter {caracter}:", caracterEspecifico="x"):
    """Pide un caracter en especifico
    hasta que no se introduzca tal caracter
    no saldrá del bucle
    """

    mensaje = mensaje.format(caracterEspecifico=caracterEspecifico)
    error = error.format(caracterEspecifico=caracterEspecifico)

    while((caracter:= leer_caracter(mensaje, error)) != caracterEspecifico):
        pass
    return caracter

def leer_caracter_multiple(mensaje="Introduce un caracter:", error="No se ha introducido un caracter válido:", caracteres_validos=["s", "n"]):
    """Pide un caracter que esté dentro de una lista de caracteres válidos
    hasta que no se introduzca un caracter válido no saldrá del bucle
    """
    
    while True:
        caracter = leer_caracter(mensaje, error)
        if caracter.lower() in caracteres_validos:
            return caracter.lower()
        print(error)

