horas = int(input("Ingrese la hora (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))

segundos_totales = horas * 3600 + minutos * 60
segundos_medianoche = 24 * 3600 - segundos_totales
print("Segundos hasta la medianoche:", segundos_medianoche)