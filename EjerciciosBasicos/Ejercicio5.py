print("Introduzca la operacion que desee realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Operación (1/2/3/4): ")
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

if operacion == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacion == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacion == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operacion == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: División por cero no permitida.")
else:
    print("Operación no válida.")

