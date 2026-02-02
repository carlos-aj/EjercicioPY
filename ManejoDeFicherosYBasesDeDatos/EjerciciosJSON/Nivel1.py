import json

datos = {
    "autor": "Anonimo",  "version": 1.0
}

with open("config.json", "w") as archivojson:
    json.dump(datos, archivojson, indent = 2)

with open("config.json", "r") as archivojson:
    datos_leidos = json.load(archivojson)

print (datos_leidos["version"])