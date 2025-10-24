print("=== Calculadora de desayuno ===")

comida = input("¿Qué has tomado para comer? (tostada / churros / donut): ").strip().lower()

precio_comida = 0

if comida == "churros":
    precio_comida = 1.50
elif comida == "donut":
    precio_comida = 1.00
elif comida == "tostada":
    tipo_tostada = input("¿Tostada básica o especial? (basica / especial): ").strip().lower()
    if tipo_tostada == "basica":
        precio_comida = 1.20
    elif tipo_tostada == "especial":
        precio_comida = 1.60
    else:
        print("Error: tipo de tostada no válido.")
        exit()
else:
    print("Error: opción de comida no válida.")
    exit()

bebida = input("¿Qué has tomado para beber? (zumo / cafe): ").strip().lower()

precio_bebida = 0

if bebida == "zumo":
    precio_bebida = 1.80
elif bebida == "cafe":
    precio_bebida = 1.20
else:
    print("Error: opción de bebida no válida.")
    exit()

total = precio_comida + precio_bebida

print(f"El precio total de tu desayuno es: {total:.2f} €")
