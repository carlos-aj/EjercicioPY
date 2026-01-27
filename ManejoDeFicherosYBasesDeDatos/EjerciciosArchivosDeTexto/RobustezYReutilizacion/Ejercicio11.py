try:
    with open("archivo_original.txt", "wt") as f:
        f.write("Contenido de ejemplo.")

except FileNotFoundError as e:
    print(f"Error (Archivo no encontrado): {e}")
except PermissionError as e:
    print(f"Error (Permiso denegado): {e}")