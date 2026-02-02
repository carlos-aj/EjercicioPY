from estudiante import Estudiante
from asignatura import Asignatura

import json

asig1 = Asignatura("Programación", 10)
asig2 = Asignatura("Matemáticas", 8)
asig3 = Asignatura("Física", 6)
        
estudiante1 = Estudiante("Juan", "Pérez", "García", [asig1, asig2])
estudiante2 = Estudiante("María", "López", "Martín", [asig3])

estudiantes = [estudiante1, estudiante2]

lista_diccionarios = []

for estudiante in estudiantes:
    diccionario_estudiante = {
        "nombre": estudiante.nombre,
        "apellido_1": estudiante.apellido_1,
        "apellido_2": estudiante.apellido_2,
        "asignaturas": [
            {"nombre": asignatura.nombre, "horas": asignatura.horas}
            for asignatura in estudiante.lista_asignaturas
        ]
    }
    lista_diccionarios.append(diccionario_estudiante)

with open("estudiantes.json", "w", encoding="utf-8") as archivo_json:
    json.dump(lista_diccionarios, archivo_json, indent=4)

with open("estudiantes.json", "r", encoding="utf-8") as archivo_json:
    datos_leidos = json.load(archivo_json)

nuevos_estudiantes = []
for diccionario_estudiante in datos_leidos:
    asignaturas = [
        Asignatura(asig["nombre"], asig["horas"])
        for asig in diccionario_estudiante["asignaturas"]
    ]
    estudiante = Estudiante(
        diccionario_estudiante["nombre"],
        diccionario_estudiante["apellido_1"],
        diccionario_estudiante["apellido_2"],
        asignaturas
    )
    nuevos_estudiantes.append(estudiante)

for estudiante in nuevos_estudiantes:
    print(estudiante)