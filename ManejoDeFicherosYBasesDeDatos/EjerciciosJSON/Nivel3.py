import json

datos = {
    "productos": [
        {"nombre":"Laptop", "precio": 1200,},
        {"nombre":"Smartphone", "precio": 800,},
        {"nombre":"Tablet", "precio": 400,},
        {"nombre":"Monitor", "precio": 300,}
    ]
}

with open("productos.json", "w") as archivo_json:
    json.dump(datos, archivo_json, indent=4)

with open("productos.json", "r") as archivo_json:
    datos_leidos = json.load(archivo_json)

for producto in datos_leidos["productos"]:
    if producto["precio"] > 1000:
        print(producto)
