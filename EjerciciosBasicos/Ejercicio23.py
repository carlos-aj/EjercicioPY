print("=== Serie de Fibonacci ===")

n = int(input("¿Cuántos términos quieres mostrar?: "))

if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    a, b = 0, 1  
    print("\nLos primeros", n, "términos de la serie de Fibonacci son:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  
    print()
