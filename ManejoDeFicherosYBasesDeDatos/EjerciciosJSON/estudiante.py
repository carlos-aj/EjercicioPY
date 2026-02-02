from asignatura import Asignatura
import copy

class Estudiante:
    # Constructor normal
    def __init__(self, nombre, apellido_1, apellido_2, lista_asignaturas):
        self._nombre = nombre
        self._apellido_1 = apellido_1
        self._apellido_2 = apellido_2
        self._lista_asignaturas = lista_asignaturas
    
    # Constructor copia
    @classmethod
    def estudiante_copia(cls, copia_estudiante):
        return copy.deepcopy(copia_estudiante)
    
    # Getters y Setters
    # Getter nombre
    @property
    def nombre(self):
        return self._nombre
    
    # Getter apellido 1
    @property
    def apellido_1(self):
        return self._apellido_1
    
    # Getter apellido 2
    @property
    def apellido_2(self):
        return self._apellido_2
    
    # Getter lista asignaturas
    @property
    def lista_asignaturas(self):
        return self._lista_asignaturas
    
    # Setter nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Setter apellido 1
    @apellido_1.setter
    def apellido_1(self, apellido_1):
        self._apellido_1 = apellido_1
        
    # Setter apellido 2
    @apellido_2.setter
    def apellido_2(self, apellido_2):
        self._apellido_2 = apellido_2

    # Setter lista asignaturas
    @lista_asignaturas.setter
    def lista_asignaturas(self, lista_asignaturas):
        self._lista_asignaturas = lista_asignaturas

    # Metodos principales
    # Añadir asignatura
    def anade_asignatura(self, asignatura):
        if self.get_numero_horas_matriculadas() + asignatura.horas > 30:
            return False
        
        self.lista_asignaturas.append(asignatura)
        return True
    
    # Obtener numero de asignaturas matriculadas
    def get_numero_asignaturas_matriculadas(self):
        return len(self.lista_asignaturas)
    
    # Obtener numero de horas matriculadas
    def get_numero_horas_matriculadas(self):
        total_horas = 0
        for i in self.lista_asignaturas:
            total_horas += i.horas

        return total_horas
    
    # Obtener asignatura por posicion
    def get_asignatura(self, posicion):
        if not self.lista_asignaturas or posicion < 0 or posicion >= len(self.lista_asignaturas):
            raise ValueError("Asignatura no existente")
        
        return self.lista_asignaturas[posicion]
    
    # Representacion en cadena
    def __str__(self):
        return f"Nombre: {self._nombre} {self._apellido_1} {self._apellido_2}, Asignaturas: {[str(asig) for asig in self._lista_asignaturas]}"
    
    # Metodo de comparacion
    def __eq__(self, otro_estudiante):
        if isinstance(otro_estudiante, Estudiante):
            return (self._nombre == otro_estudiante._nombre and
                    self._apellido_1 == otro_estudiante._apellido_1 and
                    self._apellido_2 == otro_estudiante._apellido_2 and
                    self._lista_asignaturas == otro_estudiante._lista_asignaturas)
        return False
    
class MainEstudiante:
    def main():
        print("=== PRUEBAS DE LA CLASE ESTUDIANTE ===\n")
        
        # 1. Constructores
        print("1. CONSTRUCTORES")
        print("-" * 15)
        asig1 = Asignatura("Programación", 10)
        asig2 = Asignatura("Matemáticas", 8)
        asig3 = Asignatura("Física", 6)
        
        estudiante1 = Estudiante("Juan", "Pérez", "García", [asig1, asig2])
        estudiante2 = Estudiante("María", "López", "Martín", [asig3])
        estudiante_copia = Estudiante.estudiante_copia(estudiante1)
        
        print(f"Estudiante 1: {estudiante1}")
        print(f"Estudiante 2: {estudiante2}")
        print(f"Estudiante copia: {estudiante_copia}")
        
        # 2. Propiedades
        print("\n2. PROPIEDADES")
        print("-" * 15)
        print(f"Nombre: {estudiante1.nombre}")
        print(f"Apellido 1: {estudiante1.apellido_1}")
        print(f"Apellido 2: {estudiante1.apellido_2}")
        print(f"Lista de asignaturas: {[str(asig) for asig in estudiante1.lista_asignaturas]}")
        
        # 3. Métodos de información
        print("\n3. MÉTODOS DE INFORMACIÓN")
        print("-" * 25)
        print(f"Número de asignaturas matriculadas: {estudiante1.get_numero_asignaturas_matriculadas()}")
        print(f"Número de horas matriculadas: {estudiante1.get_numero_horas_matriculadas()}")
        
        # 4. Obtener asignatura por posición
        print("\n4. OBTENER ASIGNATURA")
        print("-" * 20)
        try:
            asignatura_pos_0 = estudiante1.get_asignatura(0)
            print(f"Asignatura en posición 0: {asignatura_pos_0}")
            asignatura_pos_1 = estudiante1.get_asignatura(1)
            print(f"Asignatura en posición 1: {asignatura_pos_1}")
        except ValueError as e:
            print(f"Error: {e}")
        
        # 5. Añadir asignaturas
        print("\n5. AÑADIR ASIGNATURAS")
        print("-" * 19)
        asig4 = Asignatura("Química", 7)
        resultado = estudiante1.anade_asignatura(asig4)
        print(f"¿Se añadió Química? {resultado}")
        if resultado:
            print(f"Estudiante1 después de añadir Química: {estudiante1}")
            print(f"Nuevas horas totales: {estudiante1.get_numero_horas_matriculadas()}")
        
        # Intentar añadir una asignatura que exceda el límite
        asig5 = Asignatura("Historia", 10)
        resultado2 = estudiante1.anade_asignatura(asig5)
        print(f"¿Se añadió Historia (excede límite)? {resultado2}")
        
        # 6. Setters
        print("\n6. SETTERS")
        print("-" * 10)
        estudiante1.nombre = "Juan Carlos"
        estudiante1.apellido_1 = "Pérez-González"
        estudiante1.apellido_2 = "García-López"
        print(f"Estudiante1 después de cambiar nombres: {estudiante1}")
        
        nueva_lista = [Asignatura("Inglés", 5)]
        estudiante1.lista_asignaturas = nueva_lista
        print(f"Estudiante1 con nueva lista de asignaturas: {estudiante1}")
        
        # 7. Comparación
        print("\n7. COMPARACIÓN")
        print("-" * 14)
        estudiante_a = Estudiante("Ana", "Ruiz", "Moreno", [Asignatura("Arte", 4)])
        estudiante_b = Estudiante("Ana", "Ruiz", "Moreno", [Asignatura("Arte", 4)])
        estudiante_c = Estudiante("Luis", "Ruiz", "Moreno", [Asignatura("Arte", 4)])
        
        print(f"Estudiante A: {estudiante_a}")
        print(f"Estudiante B: {estudiante_b}")
        print(f"Estudiante C: {estudiante_c}")
        print(f"¿A == B? {estudiante_a == estudiante_b}")
        print(f"¿A == C? {estudiante_a == estudiante_c}")
        
        # 8. Prueba de errores
        print("\n8. PRUEBA DE ERRORES")
        print("-" * 18)
        try:
            asignatura_error = estudiante2.get_asignatura(5)  # Posición que no existe
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")
        
        try:
            asignatura_error2 = estudiante2.get_asignatura(-1)  # Posición negativa
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")
    
if __name__ == "__main__":
    MainEstudiante.main()

    