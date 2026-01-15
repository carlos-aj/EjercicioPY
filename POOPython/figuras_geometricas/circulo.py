from punto import Punto
import math
import copy

class Circulo:
    # Constructor normal
    def __init__(self, centro, radio):
        if not Circulo._comprobar_negativo(radio):
            raise ValueError("El radio no puede ser negativo")
        self._centro = centro
        self._radio = radio

    # Constructor valores por defecto
    @classmethod
    def circulo_default(cls, radio = 0):
        return cls(Punto.punto_default(), radio)
    
    # Constructor copia
    @classmethod
    def circulo_copia(cls, copia_circulo):
        return copy.deepcopy(copia_circulo)
    
    # Constructor con centro en el origen
    @classmethod
    def circulo_origen(cls, x, y, radio):
        return cls(Punto(x,y), radio)
    
    # Getters y Setters
    # Getter centro
    @property
    def centro(self):
        return self._centro
    
    # Getter radio
    @property
    def radio(self):
        return self._radio
    
    # Setter centro
    @centro.setter
    def centro(self, centro):
        self._centro = centro

    # Setter radio
    @radio.setter
    def radio(self, radio):
        if not Circulo._comprobar_negativo(radio):
            raise ValueError("El radio no puede ser menor que 0")
        self._radio = radio

    # Metodos principales
    def get_area(self):
        return (math.pi * self._radio ** 2)

    # Metodo para obtener la circunferencia
    def get_circunferencia(self):
        return (2 * math.pi * self._radio)
    
    # Representacion en cadena
    def __str__(self):
        return f"Centro: {self.centro._x}, {self.centro._y} Radio: {self._radio}"
    
    # Metodo de comparacion
    def __eq__(self, otro_circulo):
        if isinstance(otro_circulo, Circulo):
            return self._centro == otro_circulo._centro and self._radio == otro_circulo._radio
        return False

    # Metodo estatico de comprobacion >= 0
    @staticmethod
    def _comprobar_negativo(numero):
        return numero >= 0
    
class MainCirculo:
    def main():
        print("=== PRUEBAS DE LA CLASE CIRCULO ===\n")
        
        # 1. Constructores
        print("1. CONSTRUCTORES")
        print("-" * 15)
        centro1 = Punto(3, 5)
        circulo1 = Circulo(centro1, 10)
        circulo_default = Circulo.circulo_default()
        circulo_custom = Circulo.circulo_default(15)
        circulo_copia = Circulo.circulo_copia(circulo1)
        circulo_origen = Circulo.circulo_origen(7, 8, 20)
        
        print(f"Círculo normal: {circulo1}")
        print(f"Círculo default: {circulo_default}")
        print(f"Círculo custom: {circulo_custom}")
        print(f"Círculo copia: {circulo_copia}")
        print(f"Círculo origen: {circulo_origen}")
        
        # 2. Propiedades
        print("\n2. PROPIEDADES")
        print("-" * 15)
        print(f"Centro del círculo1: {circulo1.centro}")
        print(f"Radio del círculo1: {circulo1.radio}")
        
        # 3. Cálculos
        print("\n3. CÁLCULOS")
        print("-" * 12)
        print(f"Área del círculo1: {circulo1.get_area():.2f}")
        print(f"Circunferencia del círculo1: {circulo1.get_circunferencia():.2f}")
        
        # 4. Setters
        print("\n4. SETTERS")
        print("-" * 10)
        nuevo_centro = Punto(10, 15)
        circulo1.centro = nuevo_centro
        circulo1.radio = 25
        print(f"Círculo1 después de cambiar centro y radio: {circulo1}")
        print(f"Nueva área: {circulo1.get_area():.2f}")
        print(f"Nueva circunferencia: {circulo1.get_circunferencia():.2f}")
        
        # 5. Comparación
        print("\n5. COMPARACIÓN")
        print("-" * 14)
        circulo_a = Circulo(Punto(5, 5), 10)
        circulo_b = Circulo(Punto(5, 5), 10)
        circulo_c = Circulo(Punto(3, 4), 15)
        
        print(f"Círculo A: {circulo_a}")
        print(f"Círculo B: {circulo_b}")
        print(f"Círculo C: {circulo_c}")
        print(f"¿A == B? {circulo_a == circulo_b}")
        print(f"¿A == C? {circulo_a == circulo_c}")
        
        # 6. Prueba de error (radio negativo)
        print("\n6. PRUEBA DE ERROR")
        print("-" * 17)
        try:
            circulo_error = Circulo(Punto(0, 0), -5)
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")
    
if __name__ == "__main__":
    MainCirculo.main()
    
    