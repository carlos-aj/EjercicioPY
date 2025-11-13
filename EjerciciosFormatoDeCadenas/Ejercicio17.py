import Validaciones

altura = Validaciones.leer_numero_entero_con_minimo(
    mensaje="Introduce la altura de la U (mínimo 3): ",
    error="La altura debe ser al menos 3",
    minimo=3
)

for i in range(altura - 1):
    print("*" + " " * (altura - 2) + "*")

espacios_base = altura - 3  
if espacios_base >= 0:  
    print(" " + "*" * espacios_base)
