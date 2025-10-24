hora = int(input("Ingrese la hora en formato 24 horas (0-23): "))
minuto = int(input("Ingrese los minutos (0-59): "))

if 0 <= hora < 24 and 0 <= minuto < 60:
    if 6 <= hora < 12:
        print("Buenos días")
    elif 12 <= hora < 20:
        print("Buenas tardes")
    else:
        print("Buenas noches")
else:
    print("Hora o minutos no válidos.")
