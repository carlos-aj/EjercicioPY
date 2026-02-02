import json

datos = {
    "programadores": [
        {"nombre": "Alice", "lenguajes": ["Python", "JavaScript"], "nivel": "senior"},
        {"nombre": "Bob", "lenguajes": ["Java", "C#"], "nivel": "junior"},
        {"nombre": "Charlie", "lenguajes": ["Go", "Rust"], "nivel": "mid-level"}
    ]
}

with open("datos_formato.json", "w") as archivo_json:
    json.dump(datos, archivo_json, indent=4)