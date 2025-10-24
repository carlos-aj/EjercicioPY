print("Este programa resuelve ecuaciones de primer grado del tipo ax + b = 0")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))

if a != 0:
    x = -b / a
    print(f"La solución de la ecuación es: x = {x}")
else:
    if b == 0:
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene solución.")