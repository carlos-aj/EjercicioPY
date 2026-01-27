import os

with open("latin.txt", "wb") as f:
    f.write(b'\xff\xfe\x00\x48\x00\x6f\x00\x6c\x00\x61')

with open("latin.txt", "r", encoding = "utf8") as f:
    try:
        contenido = f.read()
        print(contenido)
    except UnicodeDecodeError as e:
        print(f"Error de codificación: {e}")