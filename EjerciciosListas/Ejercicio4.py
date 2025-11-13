lista = [{"Nombre": "", "Edad": 0}]
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

edadMayor = 0
alumnosMayores = []
alumnosMayoresEdad = []

while nombre != "*":
    lista.append({"Nombre": nombre, "Edad": edad})
    nombre = input("Introduce tu nombre: ")
    if nombre != "*":
        edad = int(input("Introduce tu edad: "))

for alumno in lista:
    if alumno["Edad"] > 18:
        alumnosMayoresEdad.append(alumno)
    if alumno["Edad"] > edadMayor:
        edadMayor = alumno["Edad"]
        alumnosMayores = [alumno]
    elif alumno["Edad"] == edadMayor:
        alumnosMayores.append(alumno)

print("Alumnos mayores de edad:")
for alumno in alumnosMayoresEdad:
    print(f"Nombre: {alumno['Nombre']} - Edad: {alumno['Edad']}")

print(f"Alumnos de edad máxima {edadMayor}:")
for alumno in alumnosMayores:
    print(f"Nombre: {alumno['Nombre']}")