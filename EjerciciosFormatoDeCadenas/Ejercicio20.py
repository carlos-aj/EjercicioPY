import Validaciones

altura = Validaciones.leer_numero_entero_con_minimo(
    mensaje="Introduce la altura de la figura: ",
    error="La altura debe ser un número mayor a {minimo}: ",
    minimo=1
)

for fila in range(altura, 0, -1):
    if fila == altura:
        # Primera fila: todos asteriscos
        print("*" * fila)
    elif fila == 1:
        # Última fila: solo un asterisco
        print("*")
    else:
        # Filas intermedias: solo asteriscos en los extremos (hueco)
        print("*" + " " * (fila - 2) + "*")