from punto import Punto
import copy
import math

class Rombo:
    # Constructor normal
    def __init__(self, centro, lado, diagonal):
        if not Rombo._comprobar_negativo(lado) or not Rombo._comprobar_negativo(diagonal):
            raise ValueError("El lado y la diagonal no pueden ser menor a 0")
        self._centro = centro
        self._lado = lado
        self._diagonal = diagonal

    # Constructor valores por defecto
    @classmethod
    def rombo_default(cls, lado = 0, diagonal = 0):
        return cls(Punto.punto_default(), lado, diagonal)

    # Constructor copia
    @classmethod
    def rombo_copia(cls, copia_rombo):
        return copy.deepcopy(copia_rombo)
    
    # Constructor con centro en el origen
    @classmethod
    def rombo_origen(cls, x, y, lado, diagonal):
        return cls(Punto(x,y), lado, diagonal)
    
    # Getters y Setters
    # Getter centro
    @property
    def centro(self):
        return self._centro
    
    # Getter lado
    @property
    def lado(self):
        return self._lado
    
    # Getter diagonal
    @property
    def diagonal(self):
        return self._diagonal
    
    # Setter centro
    @centro.setter
    def centro(self, centro):
        self._centro = centro
    
    # Setter lado
    @lado.setter
    def lado(self, lado):
        if not Rombo._comprobar_negativo(lado):
            raise ValueError("El lado no puede ser menor a 0")
        self._lado = lado

    # Setter diagonal
    @diagonal.setter
    def diagonal(self, diagonal):
        if not Rombo._comprobar_negativo(diagonal):
            raise ValueError("La diagonal no puede ser menor a 0")
        self._diagonal = diagonal    

    # Metodo para obtener la diagonal faltante
    def get_diagonal_faltante(self):
        return 2 * math.sqrt(self._lado ** 2 - (self._diagonal / 2 ) ** 2)

    # Metodo para obtener el area
    def get_area(self):
        return (self._diagonal * self.get_diagonal_faltante()) / 2
    
    # Metodo para obtener el perimetro
    def get_perimetro(self):
        return self._lado * 4

    # Representacion en cadena
    def __str__(self):
        return f"Centro: {self.centro._x}, {self.centro._y} Lado: {self._lado} Diagonal: {self.diagonal}"
    
    # Metodo de comparacion
    def __eq__(self, otro_rombo):
        if isinstance(otro_rombo, Rombo):
            return self._centro == otro_rombo._centro and self._lado == otro_rombo._lado and self._diagonal == otro_rombo._diagonal
        return False

    # Metodo estatico de comprobacion >= 0
    @staticmethod
    def _comprobar_negativo(numero):
        return numero >= 0
    
class MainRombo:
    def main():
        print("=== PRUEBAS DE LA CLASE ROMBO ===\n")
        
        # 1. Constructores
        print("1. CONSTRUCTORES")
        print("-" * 15)
        centro1 = Punto(3, 5)
        rombo1 = Rombo(centro1, 10, 8)
        rombo_default = Rombo.rombo_default()
        rombo_custom = Rombo.rombo_default(15, 12)
        rombo_copia = Rombo.rombo_copia(rombo1)
        rombo_origen = Rombo.rombo_origen(7, 8, 20, 16)
        
        print(f"Rombo normal: {rombo1}")
        print(f"Rombo default: {rombo_default}")
        print(f"Rombo custom: {rombo_custom}")
        print(f"Rombo copia: {rombo_copia}")
        print(f"Rombo origen: {rombo_origen}")
        
        # 2. Propiedades
        print("\n2. PROPIEDADES")
        print("-" * 15)
        print(f"Centro del rombo1: {rombo1.centro}")
        print(f"Lado del rombo1: {rombo1.lado}")
        print(f"Diagonal del rombo1: {rombo1.diagonal}")
        
        # 3. Cálculos
        print("\n3. CÁLCULOS")
        print("-" * 12)
        print(f"Diagonal faltante del rombo1: {rombo1.get_diagonal_faltante():.2f}")
        print(f"Área del rombo1: {rombo1.get_area():.2f}")
        print(f"Perímetro del rombo1: {rombo1.get_perimetro()}")
        
        # 4. Setters
        print("\n4. SETTERS")
        print("-" * 10)
        nuevo_centro = Punto(10, 15)
        rombo1.centro = nuevo_centro
        rombo1.lado = 25
        rombo1.diagonal = 20
        print(f"Rombo1 después de cambiar centro, lado y diagonal: {rombo1}")
        print(f"Nueva diagonal faltante: {rombo1.get_diagonal_faltante():.2f}")
        print(f"Nueva área: {rombo1.get_area():.2f}")
        print(f"Nuevo perímetro: {rombo1.get_perimetro()}")
        
        # 5. Comparación
        print("\n5. COMPARACIÓN")
        print("-" * 14)
        rombo_a = Rombo(Punto(5, 5), 10, 8)
        rombo_b = Rombo(Punto(5, 5), 10, 8)
        rombo_c = Rombo(Punto(3, 4), 15, 12)
        
        print(f"Rombo A: {rombo_a}")
        print(f"Rombo B: {rombo_b}")
        print(f"Rombo C: {rombo_c}")
        print(f"¿A == B? {rombo_a == rombo_b}")
        print(f"¿A == C? {rombo_a == rombo_c}")
        
        # 6. Prueba de error (valores negativos)
        print("\n6. PRUEBA DE ERROR")
        print("-" * 17)
        try:
            rombo_error = Rombo(Punto(0, 0), -5, 10)
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")
        
        try:
            rombo_error2 = Rombo(Punto(0, 0), 10, -5)
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")
    
if __name__ == "__main__":
    MainRombo.main()