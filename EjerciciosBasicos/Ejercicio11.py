horas = int(input("Introduzca las horas trabajadas:"))

if horas > 40:
    print(f"Vas a cobrar {40 * 12 + (horas - 40) * 16} euros")
else:
    print(f"Vas a cobrar {horas * 12} euros")