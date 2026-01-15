class Rectangulo:
    def __init__(self, largo, ancho):
        if not Rectangulo._comprobar_positivo(ancho):
            raise ValueError("El ancho debe ser mayor que 0")
        if not Rectangulo._comprobar_positivo(largo):
            raise ValueError("El largo debe ser mayor que 0")
        self._largo = largo
        self._ancho = ancho

    @staticmethod
    def _comprobar_positivo(numero):
        return numero>0

    @property
    def largo(self):
        return self._largo
    
    @property
    def ancho(self):
        return self._ancho
    
    @largo.setter
    def largo(self, largo):
        if not Rectangulo._comprobar_positivo(largo):
            raise ValueError("El largo debe ser mayor a 0")
        self._largo = largo

    @ancho.setter
    def ancho(self, ancho):
        if not Rectangulo._comprobar_positivo(ancho):
            raise ValueError("El ancho debe ser mayor a 0")
        self._ancho = ancho

    def calcular_area(self):
        return self._largo * self._ancho
    
    def __str__(self):
        return f"Rectangulo {self._ancho} x {self._largo} = {self.calcular_area()}"

rec = Rectangulo(4, 5)
rec2 = Rectangulo(8, 10)

print(rec, rec2)
