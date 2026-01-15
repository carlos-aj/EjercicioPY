class Suma():
    def __init__(self, n1 = 2, n2 = 4):
        self._n1 = n1
        self._n2 = n2

    def obtener_suma(self):
        return self._n1 + self._n2

sum1 = Suma()

print(sum1.obtener_suma())