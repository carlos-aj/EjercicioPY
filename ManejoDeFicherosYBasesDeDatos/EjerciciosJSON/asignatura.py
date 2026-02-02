import copy

class Asignatura:
    # Constructor normal
    def __init__(self, nombre, horas):
        if not Asignatura._comprobar_negativo(horas):
            raise ValueError("Las horas no pueden ser negativas")
        
        self._nombre = nombre
        self._horas = horas

    # Constructor copia
    @classmethod
    def asignatura_copia(cls, copia_asignatura):
        return copy.copy(copia_asignatura)
    
    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre
    
    # Getter horas
    @property
    def horas(self):
        return self._horas
    
    # Setter nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Setter horas
    @horas.setter
    def horas(self, horas):
        if not Asignatura._comprobar_negativo(horas):
            raise ValueError("Las horas no pueden ser negativas")
        
        self._horas = horas
    
    # Metodos principales
    def __str__(self):
        return f"Nombre: {self._nombre}, horas: {self._horas}"
    
    # Metodo de comparacion
    def __eq__(self, otra_asignatura):
        if isinstance(otra_asignatura, Asignatura):
            return self._nombre == otra_asignatura._nombre and self._horas == otra_asignatura._horas
        return False
    
    # Metodo estatico de comprobacion >= 0
    @staticmethod
    def _comprobar_negativo(numero):
        return numero >= 0
    
class MainAsignatura:
    def main():
        print("=== PRUEBAS DE LA CLASE ASIGNATURA ===\n")
        
        # 1. Constructores
        print("1. CONSTRUCTORES")
        print("-" * 15)
        asignatura1 = Asignatura("Programación", 120)
        asignatura2 = Asignatura("Matemáticas", 180)
        asignatura_copia = Asignatura.asignatura_copia(asignatura1)
        
        print(f"Asignatura 1: {asignatura1}")
        print(f"Asignatura 2: {asignatura2}")
        print(f"Asignatura copia: {asignatura_copia}")
        
        # 2. Propiedades
        print("\n2. PROPIEDADES")
        print("-" * 15)
        print(f"Nombre de asignatura1: {asignatura1.nombre}")
        print(f"Horas de asignatura1: {asignatura1.horas}")
        
        # 3. Setters
        print("\n3. SETTERS")
        print("-" * 10)
        asignatura1.nombre = "Programación Orientada a Objetos"
        asignatura1.horas = 150
        print(f"Asignatura1 después de cambiar nombre y horas: {asignatura1}")
        
        # 4. Comparación
        print("\n4. COMPARACIÓN")
        print("-" * 14)
        asignatura_a = Asignatura("Física", 100)
        asignatura_b = Asignatura("Física", 100)
        asignatura_c = Asignatura("Química", 90)
        
        print(f"Asignatura A: {asignatura_a}")
        print(f"Asignatura B: {asignatura_b}")
        print(f"Asignatura C: {asignatura_c}")
        print(f"¿A == B? {asignatura_a == asignatura_b}")
        print(f"¿A == C? {asignatura_a == asignatura_c}")
        
        # 5. Prueba de error (horas negativas)
        print("\n5. PRUEBA DE ERROR")
        print("-" * 17)
        try:
            asignatura_error = Asignatura("Asignatura Error", -10)
        except ValueError as e:
            print(f"Error en constructor capturado correctamente: {e}")
        
        try:
            asignatura_test = Asignatura("Test", 50)
            asignatura_test.horas = -20
        except ValueError as e:
            print(f"Error en setter capturado correctamente: {e}")
    
if __name__ == "__main__":
    MainAsignatura.main()