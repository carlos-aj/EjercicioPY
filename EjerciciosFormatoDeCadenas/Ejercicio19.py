import Validaciones

altura = Validaciones.leer_numero_entero_con_minimo(
    mensaje="Introduce la altura de la figura: ",
    error="La altura debe ser un número mayor a {minimo}: ",
    minimo=1
)

for fila in range(altura, 0, -1):
    print("*" * fila)