import Validaciones

while True:
    altura = Validaciones.leer_numero_entero("Introduce la altura de la X: ")
    
    if altura >= 3 and altura % 2 == 1:
        break
    else:
        print("Error: La altura debe ser un número impar mayor o igual a 3")

print(f"\nDibujando X de altura {altura}:")
for i in range(altura):
    linea = ""
    for j in range(altura):
        if j == i or j == altura - 1 - i:
            linea += "*"
        else:
            linea += " "
    print(linea)