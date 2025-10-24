dia = input("Ingrese el día de la semana (lunes, martes, miercoles, jueves o viernes): ")
dia = dia.lower()

if dia == "lunes" or dia == "jueves":
    print("La asignatura a primera hora es: Programación orientada a objetos.")
elif dia == "martes" or dia == "miercoles":
    print("La asignatura a primera hora es: Análisis de datos en Python.")
elif dia == "viernes":
    print("La asignatura a primera hora es: Estructuras de control en Python.")
else:
    print("Día inválido, inténtelo de nuevo.")