class ConectaN:
    # Constantes para representar las fichas y el estado del tablero
    CASILLA_VACIA = 0
    FICHA_EQUIS = 1
    FICHA_CIRULO = 2

    def __init__(self, filas = 6, columnas = 7, cantidad_victoria = 4, modo_juego = 1):
        if ConectaN.validar_tamano_tablero(filas, columnas):
            raise ValueError("El tamaño mínimo del tablero es de 6x7")
        
        self._tablero = [
            [self.CASILLA_VACIA for _ in range(filas)]
            for _ in range(columnas)
        ]

        self._cantidad_victoria = cantidad_victoria
        self._modo_juego = modo_juego

    @property
    def tablero(self):
        return self._tablero
    
    @property
    def cantidad_victoria(self):
        return self._cantidad_victoria
    
    @property
    def modo_juego(self):
        return self._modo_juego
    
    @cantidad_victoria.setter
    def cantidad_victoria(self, cantidad_victoria):
        if len(self._tablero) > len(self._tablero[0]):
            maximo = len(self._tablero)
        else:
            maximo = len(self._tablero[0])

        if cantidad_victoria > maximo:
            raise ValueError(f"La cantidad de fichas para la victoria en este tablero no puede ser mayor a {maximo}")
        
        self.cantidad_victoria = cantidad_victoria
    
    @modo_juego.setter
    def modo_juego(self, modo_juego):
        self._modo_juego = modo_juego
        

    @staticmethod
    def validar_tamano_tablero(filas, columnas):
        if filas < 6 or columnas < 7:
            raise ValueError("El tamaño mínimo del tablero es de 4x4")