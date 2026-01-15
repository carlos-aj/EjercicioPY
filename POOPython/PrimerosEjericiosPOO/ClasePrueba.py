from typing import Self

class Alumno():
    def __init__(self, nombre: str, apellidos: str, edad: int):
        if edad < 1:
            raise ValueError
        
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if edad > 1:
            raise ValueError
        self._edad = edad

    def __str__(self):
        return self._nombre+" "+self._apellidos+" "+ str(self._edad)
   
    def __eq__(self, other: Self):
        if(isinstance(other, Alumno)):
            return str(self) == str(other)
        raise TypeError
    
    def __lt__(self, other: Self):
        if(isinstance(other, Alumno)):
            return self._edad < other._edad
        raise TypeError

al1 = Alumno('Alex', 'Cabrera', 5)
al2 = Alumno('Carlos', 'Arana', 20)
al3 = Alumno('Pedro', 'Casado', 30)

al1.edad

alumnado = [al1, al2, al3]

alumnado.sort()
for a in alumnado:
    print(a)

if al1 == al2:
    print("Son lo mismo")
else:
    print("No son lo mismo")