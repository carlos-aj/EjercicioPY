import random

def generar_numeros_aleatorios():
    """
    Genera 10 números enteros aleatorios entre 0 y 200 (ambos incluidos)
    y los organiza de forma alterna: menores/iguales a 100 y mayores a 100
    """
    numeros = [random.randint(0, 200) for _ in range(10)]
    
    print("Array original:")
    print("+" + "-" * 9 + "+" + "-" * 5 * 10 + "+")
    print("| Índice |", end="")
    for i in range(10):
        print(f" {i:3d} |", end="")
    print()
    print("+" + "-" * 9 + "+" + "-" * 5 * 10 + "+")
    print("| Valor  |", end="")
    for valor in numeros:
        print(f" {valor:3d} |", end="")
    print()
    print("+" + "-" * 9 + "+" + "-" * 5 * 10 + "+")
    print()
    
    menores_iguales_100 = [num for num in numeros if num <= 100]
    mayores_100 = [num for num in numeros if num > 100]
    
    resultado = []
    i, j = 0, 0
    turno_menor = True  
    
    while i < len(menores_iguales_100) or j < len(mayores_100):
        if turno_menor:
            if i < len(menores_iguales_100):
                resultado.append(menores_iguales_100[i])
                i += 1
            elif j < len(mayores_100):
                resultado.append(mayores_100[j])
                j += 1
        else:
            if j < len(mayores_100):
                resultado.append(mayores_100[j])
                j += 1
            elif i < len(menores_iguales_100):
                resultado.append(menores_iguales_100[i])
                i += 1
        
        turno_menor = not turno_menor
    
    print("Array resultado:")
    print("+" + "-" * 9 + "+" + "-" * 5 * 10 + "+")
    print("| Índice |", end="")
    for i in range(10):
        print(f" {i:3d} |", end="")
    print()
    print("+" + "-" * 9 + "+" + "-" * 5 * 10 + "+")
    print("| Valor  |", end="")
    for valor in resultado:
        print(f" {valor:3d} |", end="")
    print()
    print("+" + "-" * 9 + "+" + "-" * 5 * 10 + "+")
    print()
    
    print(f"Números <= 100: {menores_iguales_100}")
    print(f"Números > 100: {mayores_100}")
    print(f"Array reorganizado: {resultado}")

if __name__ == "__main__":
    print("=" * 60)
    print("REORGANIZACIÓN ALTERNA DE NÚMEROS ALEATORIOS")
    print("=" * 60)
    print()
    
    generar_numeros_aleatorios()
    
    print()
    print("=" * 60)
