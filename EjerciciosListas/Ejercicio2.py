import Validaciones

vector_inicial = []
vector_invertido = []

for i in range(0,5):
    vector_inicial.append(Validaciones.leer_numero_entero(f"Introduce el numero {i+1} de 5: "))
    vector_invertido = vector_inicial[::-1]
    
print("Vector inicial:")
print(" ".join(map(str, vector_inicial)))
print("Vector invertido:")
print(" ".join(map(str, vector_invertido)))
