def cifrar_archivo(archivo_origen, archivo_destino, clave):
    """
    Cifra un archivo de texto usando cifrado César
    """
    try:
        with open(archivo_origen, 'r', encoding='utf-8') as archivo_in:
            texto = archivo_in.read()
        
        texto_cifrado = ""
        for caracter in texto:
            caracter_cifrado = chr(ord(caracter) + clave)
            texto_cifrado += caracter_cifrado
        
        with open(archivo_destino, 'w', encoding='utf-8') as archivo_out:
            archivo_out.write(texto_cifrado)
        
        print(f"Archivo cifrado guardado en: {archivo_destino}")
        return True
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_origen} no existe")
        return False
    except Exception as e:
        print(f"Error al cifrar archivo: {e}")
        return False

def descifrar_archivo(archivo_origen, archivo_destino, clave):
    """
    Descifra un archivo de texto cifrado con César
    """
    try:
        with open(archivo_origen, 'r', encoding='utf-8') as archivo_in:
            texto_cifrado = archivo_in.read()
        
        texto_descifrado = ""
        for caracter in texto_cifrado:
            caracter_descifrado = chr(ord(caracter) - clave)
            texto_descifrado += caracter_descifrado
        
        with open(archivo_destino, 'w', encoding='utf-8') as archivo_out:
            archivo_out.write(texto_descifrado)
        
        print(f"Archivo descifrado guardado en: {archivo_destino}")
        return True
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_origen} no existe")
        return False
    except Exception as e:
        print(f"Error al descifrar archivo: {e}")
        return False

def main():
    print("=== CIFRADO/DESCIFRADO CÉSAR ===")
    
    try:
        clave = int(input("Ingrese la clave numérica para el cifrado: "))
    except ValueError:
        print("Error: La clave debe ser un número entero")
        return
    
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Cifrar archivo")
        print("2. Descifrar archivo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            archivo_origen = input("Ingrese el nombre del archivo a cifrar: ").strip()
            archivo_destino = input("Ingrese el nombre del archivo cifrado (salida): ").strip()
            cifrar_archivo(archivo_origen, archivo_destino, clave)
        
        elif opcion == "2":
            archivo_origen = input("Ingrese el nombre del archivo cifrado: ").strip()
            archivo_destino = input("Ingrese el nombre del archivo descifrado (salida): ").strip()
            descifrar_archivo(archivo_origen, archivo_destino, clave)
        
        elif opcion == "3":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()