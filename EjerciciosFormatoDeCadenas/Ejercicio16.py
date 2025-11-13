import Validaciones

n = Validaciones.leer_numero_entero_con_minimo(
    mensaje="Ingrese el número de filas para la pirámide (mínimo 1): ",
    error="Por favor, ingrese un número entero mayor o igual a 1.",
    minimo=1
)

for i in range(1, n + 1):
    fila = ""
    
    for j in range(1, i + 1):
        fila += str(j)
    
    for j in range(i - 1, 0, -1):
        fila += str(j)
    
    ancho_maximo = 2 * n - 1
    espacios_izquierda = (ancho_maximo - len(fila)) // 2
    
    print(" " * espacios_izquierda + fila)