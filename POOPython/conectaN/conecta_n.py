class ConectaN:
    # Constantes para representar las fichas y el estado del tablero
    CASILLA_VACIA = 0
    FICHA_EQUIS = 1
    FICHA_CIRULO = 2
    
    # Constantes para colores de terminal
    RESET = '\033[0m'
    YELLOW_BG = '\033[43m'

    # Constructor de la clase ConectaN con parámetros para personalizar el juego 
    def __init__(self, filas = 6, columnas = 7, cantidad_victoria = 4, modo_juego = 1, jugador_1 = " ", jugador_2= ""):
        if not ConectaN.validar_tamano_tablero(filas, columnas):
            raise ValueError("El tamaño mínimo del tablero es de 6x7")
        
        # Tablero organizado como [fila][columna] para mayor intuición
        self._tablero = [
            [self.CASILLA_VACIA for _ in range(columnas)]
            for _ in range(filas)
        ]

        self._cantidad_victoria = cantidad_victoria
        self._modo_juego = modo_juego
        self._jugador_1 = jugador_1
        self._jugador_2 = jugador_2

    # Getters y Setters
    # Getter para el tablero
    @property
    def tablero(self):
        return self._tablero
    
    # Getter para la cantidad de fichas necesarias para ganar
    @property
    def cantidad_victoria(self):
        return self._cantidad_victoria
    
    # Getter para el modo de juego
    @property
    def modo_juego(self):
        return self._modo_juego
    
    # Getter para el jugador 1
    @property
    def jugador_1(self):
        return self._jugador_1

    # Getter para el jugador 2
    @property
    def jugador_2(self):
        return self._jugador_2

    # Setter para la cantidad de fichas necesarias para ganar con comprobación
    @cantidad_victoria.setter
    def cantidad_victoria(self, cantidad_victoria):
        # len(self._tablero) = filas, len(self._tablero[0]) = columnas
        filas = len(self._tablero)
        columnas = len(self._tablero[0])
        maximo = max(filas, columnas)

        if cantidad_victoria > maximo:
            raise ValueError(f"La cantidad de fichas para la victoria en este tablero no puede ser mayor a {maximo}")
        
        self._cantidad_victoria = cantidad_victoria
    
    # Setter para el modo de juego con comprobación
    @modo_juego.setter
    def modo_juego(self, modo_juego):
        if not ConectaN.validar_modo_juego(modo_juego):
            raise ValueError("Modo de juego no válido")
        self._modo_juego = modo_juego

    # Setter para el jugador 1
    @jugador_1.setter
    def jugador_1(self, jugador_1):
        self._jugador_1 = jugador_1

    # Setter para el jugador 2 con comprobación del modo de juego
    @jugador_2.setter
    def jugador_2(self, jugador_2):
        if self.modo_juego == 2:
            self._jugador_2 = "BOT"
        else:   
            self._jugador_2 = jugador_2

    # Métodos de validación
    # Validar tamaño del tablero
    @staticmethod
    def validar_tamano_tablero(filas, columnas):
        if filas < 6 or columnas < 7:
            raise ValueError("El tamaño mínimo del tablero es de 6x7")
        return True
    
    # Validar modo de juego
    @staticmethod
    def validar_modo_juego(modo_juego):
        if modo_juego < 1 or modo_juego > 2:
            raise ValueError("El modo de juego solo puede ser 1 o 2")
        return True
    
    # Pintar tablero
    def __str__(self):
        """Representación en cadena del tablero"""
        filas = len(self._tablero)
        columnas = len(self._tablero[0])
        
        resultado = ""
        
        # Números de columnas
        resultado += "  "
        for col in range(columnas):
            resultado += f"{col + 1:3}  "
        resultado += "\n"
        
        # Línea superior
        resultado += "┌" + "────┬" * (columnas - 1) + "────┐\n"
        
        # Filas del tablero (de arriba hacia abajo, como Conecta 4 real)
        for fila in range(filas):
            resultado += "│"
            for col in range(columnas):
                # Invertimos el índice de fila para mostrar la fila superior primero
                fila_invertida = filas - 1 - fila
                resultado += self._obtener_contenido_casilla(self._tablero[fila_invertida][col])
                if col < columnas - 1:
                    resultado += "│"
            resultado += "│\n"
            
            # Separadores entre filas (excepto la última)
            if fila < filas - 1:
                resultado += "├" + "────┼" * (columnas - 1) + "────┤\n"
        
        # Línea inferior
        resultado += "└" + "────┴" * (columnas - 1) + "────┘"
        
        return resultado

    # Metodo para obtener el contenido de una casilla
    def _obtener_contenido_casilla(self, valor):
        if valor == self.CASILLA_VACIA:
            return "    "
        elif valor == self.FICHA_EQUIS:
            return " X  "
        elif valor == self.FICHA_CIRULO:
            return " O  "
        return "    "
    
    # Método para mostrar el tablero resaltando la última columna jugada
    def mostrar_tablero_columna(self, columna_ultima_fila):
        filas = len(self._tablero)
        columnas = len(self._tablero[0])
        
        # Números de columnas
        print("  ", end="")
        for col in range(columnas):
            print(f"{col + 1:3}", end="  ")
        print()
        
        # Línea superior
        print("┌" + "────┬" * (columnas - 1) + "────┐")
        
        # Filas del tablero (de arriba hacia abajo)
        for fila in range(filas):
            print("│", end="")
            for col in range(columnas):
                # Invertimos el índice para mostrar la fila superior primero
                fila_invertida = filas - 1 - fila
                contenido = self._obtener_contenido_casilla(self._tablero[fila_invertida][col])
                
                # Resaltar columna si es la última donde se colocó una ficha
                if col == columna_ultima_fila:
                    print(f"{self.YELLOW_BG}{contenido}{self.RESET}", end="")
                else:
                    print(contenido, end="")
                    
                # Separador vertical (excepto última columna)
                if col < columnas - 1:
                    print("│", end="")
            print("│")
            
            # Separadores horizontales entre filas (excepto la última)
            if fila < filas - 1:
                print("├" + "────┼" * (columnas - 1) + "────┤")
        
        # Línea inferior
        print("└" + "────┴" * (columnas - 1) + "────┘")
    
    # Método para colocar una ficha en una columna, retornando la fila donde se colocó
    def _colocar_ficha(self, ficha, columna):
        if not ConectaN.columna_llena(columna):
            raise ValueError("Columna llena")
        
        for i in range(len(self.tablero)-1, -1, -1):
            if self.tablero[i][columna] == self.CASILLA_VACIA:
                self.tablero[i][columna] = ficha
                return i

    # Método para verificar si una columna está llena
    def columna_llena(self, columna):
        if columna < 0 or columna >= len(self.tablero[0]):
            return True
        return self[0][columna] != 0

class Juego:
    def main():
        return None
    
if __name__ == "__main__":
    Juego.main()
