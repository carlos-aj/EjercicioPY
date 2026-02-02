import json

datos = {
    "programadores": [
        {"nombre": "Alice", "lenguajes": ["Python", "JavaScript"], "nivel": "senior"},
        {"nombre": "Bob", "lenguajes": ["Java", "C#"], "nivel": "junior"},
        {"nombre": "Charlie", "lenguajes": ["Go", "Rust"], "nivel": "mid-level"}
    ]
}

with open("programadores.json", "w") as archivo_json:
    json.dump(datos, archivo_json, indent=4)

json_string = json.dumps(datos, indent=4)
print(json_string)