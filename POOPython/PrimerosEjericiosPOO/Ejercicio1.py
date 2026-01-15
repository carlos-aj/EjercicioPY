class RectanguloBasico():
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho

    def calcular_area(self):
        return self._largo * self._ancho


rec1 = RectanguloBasico(2,4)
print(rec1.calcular_area());

    
