class Estudiante:
    def __init__(self, nombre: str, nota1: float, nota2: float):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostrar_datos(self):
        return self.nombre + ' tiene un ' + str(self.calcular_media()) + ' de media.' 
    
est1 = Estudiante('Alex', 8 , 9)

print(est1.mostrar_datos())