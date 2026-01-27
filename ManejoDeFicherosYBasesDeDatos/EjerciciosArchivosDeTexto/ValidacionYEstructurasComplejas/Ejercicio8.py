try:
    with open("archivo_original.txt", "r") as f:
        contendido = f.read()

        with open("archivo_copia.txt", "wt") as f:
            f.write(contendido)

except FileNotFoundError as e:
    print(f"Error (Archivo no encontrado): {e}")