franjas = ["17:00-18:00", "18:00-19:00", "19:00-20:00"]
dias = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES"]

horario = [
    [("POO", '\033[91m'), ("Análisis Datos", '\033[92m'), ("Análisis Datos", '\033[92m'), ("POO", '\033[91m'), ("Estructuras Control", '\033[94m')],
    [("POO", '\033[91m'), ("Entornos Python", '\033[93m'), ("Análisis Datos", '\033[92m'), ("POO", '\033[91m'), ("Estructuras Control", '\033[94m')],
    [("POO", '\033[91m'), ("Entornos Python", '\033[93m'), ("Análisis Datos", '\033[92m'), ("Análisis Datos", '\033[92m'), ("Estructuras Control", '\033[94m')]
]


print(f"\n{'HORA':^12}", end="")
for dia in dias:
    print(f"{dia:^20}", end="")
print()

for i, franja in enumerate(franjas):
    print(f"{franja:^12}", end="")

    for j, dia in enumerate(dias):
        asignatura, color = horario[i][j]
        print(f"{color}{asignatura:^20}{'\033[0m'}", end="")
    print()
