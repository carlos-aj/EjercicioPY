import copy

class Cancion:
    # Constructor normal
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    # Constructor valores por defecto
    @classmethod
    def cancion_default(cls, titulo = " ", autor = " "):
        return cls(titulo, autor)
    
    # Constructor copia
    @classmethod
    def cancion_copia(cls, copia_cancion):
        return copy.copy(copia_cancion)
    
    # Getters y Setters
    # Getter titulo
    @property
    def titulo(self):
        return self._titulo
    
    # Getter autor
    @property
    def autor(self):
        return self._autor
    
    # Setter titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    # Setter autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor
    
    # Representacion en cadena
    def __str__(self):
        return f"{self._titulo} - {self._autor}"