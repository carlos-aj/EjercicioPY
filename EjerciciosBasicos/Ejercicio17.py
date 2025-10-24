nota1 = float(input("Introduce la nota del primer examen: "))
nota2 = float(input("Introduce la nota del segundo examen: "))

media = (nota1 + nota2) / 2

if media >= 5:
    print(f"Has aprobado con una media de {media:.2f}")
else:
    recuperacion = input("¿Cuál ha sido el resultado de la recuperación? (apto/no apto): ").strip().lower()
    
    if recuperacion == "apto":
        media = 5
        print(f"Has aprobado en la recuperación. Tu nota final es {media}")
    else:
        print(f"No has aprobado. Tu media sigue siendo {media:.2f}")
