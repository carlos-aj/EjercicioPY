class NIF:
    #Constructor normal
    def __init__(self, numero_DNI, letra):
        if not NIF._comprobar_letra(letra):
            raise ValueError("Letra no válida")
        
        if not NIF._comprobar_positivo(numero_DNI):
            raise ValueError("El numero de DNI debe ser mayor a 0")

        self._numero_DNI = numero_DNI
        self._letra = letra

    #Constructor valores por defecto
    @classmethod
    def dni_default(cls, numero_DNI = 0, letra = " "):
        return cls(numero_DNI, letra)
    
    #Getters y Setters
    #Getter numero_DNI
    @property
    def numero_DNI(self):
        return self._numero_DNI
    
    #Getter letra
    @property
    def letra(self):
        return self._letra
    
    #Setter numero_DNI
    @numero_DNI.setter
    def numero_DNI(self, numero_DNI):
        if not NIF._comprobar_positivo(numero_DNI):
            raise ValueError("El numero de DNI debe ser mayor a 0")
        
        self._numero_DNI = numero_DNI

    #Setter letra
    @letra.setter
    def letra(self, letra):
        if not NIF._comprobar_letra(letra):
            raise ValueError("Letra no válida")
        
        self._letra = letra.upper()

    #Metodo estatico de comprobacion > 0
    @staticmethod
    def _comprobar_positivo(numero):
        return numero > 0
    
    #Metodo estatico de comprobacion letra valida
    @staticmethod
    def _comprobar_letra(letra):
        letras_dni_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    
        if not isinstance(letra, str) or len(letra) != 1:
            return False
        
        if letra.upper() not in letras_dni_validas:
            return False
        
        return True

    #Metodo estatico para sacar la letra del dni
    @staticmethod
    def _sacar_letra(dni):
        lista_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        resto = dni % 23

        letra = lista_letras[resto]
        return letra
    
    #Metodo estatico para leer un NIF desde entrada
    @staticmethod
    def leer():
        try:
            dni = int(input("Introduzca el dni: "))
            letra = NIF._sacar_letra(dni)
            return NIF(dni, letra)
        except ValueError:
            print("DNI inválido")
            return None

    #Representacion en cadena
    def __str__(self):
        return f"{self._numero_DNI} - {self._letra}"
    
class MainNIF:
    def main():
        print("=== PRUEBAS DE LA CLASE NIF ===\n")
        
        # 1. PRUEBAS DE CONSTRUCTORES
        print("1. PRUEBAS DE CONSTRUCTORES")
        print("-" * 30)
        
        # Constructor normal
        try:
            nif1 = NIF(12345678, "Z")
            print(f"NIF válido: {nif1}")
        except ValueError as e:
            print(f"Error: {e}")
        
        # Constructor con dni_default
        try:
            nif_default = NIF.dni_default(12345678, "Z")
            print(f"NIF default: {nif_default}")
        except ValueError as e:
            print(f"Error en default: {e}")
        
        print("\n2. PRUEBAS DE MÉTODO _sacar_letra()")
        print("-" * 35)
        
        # Probar el cálculo de letras
        dnis_prueba = [12345678, 87654321, 11111111, 22222222, 99999999]
        for dni in dnis_prueba:
            letra = NIF._sacar_letra(dni)
            print(f"DNI {dni} -> Letra: {letra}")
        
        print("\n3. PRUEBAS DE VALIDACIÓN DE DNI COMPLETO")
        print("-" * 42)
        
        # Crear NIFs con letras correctas calculadas
        for dni in [12345678, 87654321, 11111111]:
            letra_correcta = NIF._sacar_letra(dni)
            try:
                nif = NIF(dni, letra_correcta)
                print(f"NIF correcto: {nif}")
            except ValueError as e:
                print(f"Error inesperado: {e}")
        
        print("\n4. PRUEBAS DE PROPIEDADES (GETTERS/SETTERS)")
        print("-" * 44)
        
        nif = NIF(12345678, "Z")
        print(f"NIF inicial: {nif}")
        print(f"Número DNI: {nif.numero_DNI}")
        print(f"Letra: {nif.letra}")
        
        # Cambiar número DNI
        nuevo_dni = 87654321
        nif.numero_DNI = nuevo_dni
        print(f"Después de cambiar DNI: {nif}")
        
        # Cambiar letra
        nif.letra = "x"  # Minúscula para probar conversión
        print(f"Después de cambiar letra: {nif}")
        
        print("\n5. PRUEBAS DE VALIDACIONES (ERRORES)")
        print("-" * 38)
        
        # Constructor con DNI negativo
        try:
            nif_error = NIF(-123, "T")
        except ValueError as e:
            print(f"Error DNI negativo: {e}")
        
        # Constructor con DNI cero
        try:
            nif_error = NIF(0, "T")
        except ValueError as e:
            print(f"Error DNI cero: {e}")
        
        # Constructor con letra inválida
        try:
            nif_error = NIF(12345678, "Ñ")
        except ValueError as e:
            print(f"Error letra inválida: {e}")
        
        # Constructor con letra no string
        try:
            nif_error = NIF(12345678, 123)
        except ValueError as e:
            print(f"Error letra no string: {e}")
        
        # Setter DNI negativo
        nif = NIF(12345678, "Z")
        try:
            nif.numero_DNI = -456
        except ValueError as e:
            print(f"Error setter DNI negativo: {e}")
        
        # Setter letra inválida
        try:
            nif.letra = "1"  # Número en lugar de letra
        except ValueError as e:
            print(f"Error setter letra inválida: {e}")
        
        print("\n6. PRUEBAS DE CASOS ESPECIALES")
        print("-" * 32)
        
        # DNI con letra correcta vs incorrecta
        dni_test = 12345678
        letra_correcta = NIF._sacar_letra(dni_test)
        letra_incorrecta = "A" if letra_correcta != "A" else "B"
        
        print(f"Para DNI {dni_test}:")
        print(f"Letra correcta calculada: {letra_correcta}")
        
        try:
            nif_correcto = NIF(dni_test, letra_correcta)
            print(f"Con letra correcta: {nif_correcto}")
        except ValueError as e:
            print(f"Error inesperado: {e}")
        
        try:
            nif_incorrecto = NIF(dni_test, letra_incorrecta)
            print(f"Con letra incorrecta: {nif_incorrecto}")
        except ValueError:
            print(f"Correctamente rechazado con letra incorrecta ({letra_incorrecta})")
        
        print("\n7. VERIFICAR TODAS LAS LETRAS DEL ALGORITMO")
        print("-" * 43)
        
        # Verificar que el algoritmo funciona para todos los restos (0-22)
        print("Verificación algoritmo DNI (resto -> letra):")
        for resto in range(23):
            dni_ejemplo = resto + 1000000  # DNI base + resto
            letra = NIF._sacar_letra(dni_ejemplo)
            print(f"Resto {resto:2d} -> Letra {letra} (DNI ejemplo: {dni_ejemplo})")
        
        
if __name__ == "__main__":
    MainNIF.main()