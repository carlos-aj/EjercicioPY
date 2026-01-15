import copy

class Punto:
    # Constructor normal
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    # Constructor punto valores por defecto
    @classmethod
    def punto_default(cls, x = 0 , y = 0):
        return cls(x,y)
    
    # Constructor punto copia
    @classmethod
    def punto_copia(cls, copia_punto):
        return copy.copy(copia_punto)

    # Getters y Setters
    # Getter x
    @property
    def x(self):
        return self._x
    
    # Getter y
    @property
    def y(self):
        return self._y
    
    # Setter x
    @x.setter
    def x(self, x):
        self._x = x

    # Setter y
    @y.setter
    def y(self, y):
        self._y = y

    # Representacion en cadena
    def __str__(self):
        return f"X: {self._x} Y: {self._y}"
    
    # Metodo de comparacion
    def __eq__(self, otro_punto):
        if isinstance(otro_punto, Punto):
            return self._x == otro_punto._x and self._y == otro_punto._y
        return False
        
class MainPunto:
    def main():
        print("=== PRUEBAS DE LA CLASE PUNTO ===\n")
        
        # 1. Constructores
        print("1. CONSTRUCTORES")
        print("-" * 15)
        punto1 = Punto(3, 5)
        punto_default = Punto.punto_default()
        punto_custom = Punto.punto_default(10, 20)
        punto_copia = Punto.punto_copia(punto1)
        
        print(f"Punto normal: {punto1}")
        print(f"Punto default: {punto_default}")
        print(f"Punto custom: {punto_custom}")
        print(f"Punto copia: {punto_copia}")
        
        # 2. Propiedades
        print("\n2. PROPIEDADES")
        print("-" * 15)
        print(f"Coordenada X de punto1: {punto1.x}")
        print(f"Coordenada Y de punto1: {punto1.y}")
        
        # 3. Setters
        print("\n3. SETTERS")
        print("-" * 10)
        punto1.x = 7
        punto1.y = 9
        print(f"Punto1 después de cambiar coordenadas: {punto1}")
        
        # 4. Comparación
        print("\n4. COMPARACIÓN")
        print("-" * 14)
        punto_a = Punto(5, 5)
        punto_b = Punto(5, 5)
        punto_c = Punto(3, 4)
        
        print(f"Punto A: {punto_a}")
        print(f"Punto B: {punto_b}")
        print(f"Punto C: {punto_c}")
        print(f"¿A == B? {punto_a == punto_b}")
        print(f"¿A == C? {punto_a == punto_c}")
            
if __name__ == "__main__":
    MainPunto.main()