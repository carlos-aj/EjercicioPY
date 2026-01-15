class TresEnRaya:
    # Constantes para representar las fichas y el estado del tablero
    CASILLA_VACIA = 0
    FICHA_EQUIS = 1
    FICHA_CIRULO = 2

    # Constructor de la clase TresEnRaya inicializando el tablero vacío
    def __init__(self):
        self._tablero = [
            [self.CASILLA_VACIA for _ in range(3)]
            for _ in range(3)
        ]
    
    # Método para colocar una ficha en el tablero, verificando validez de la jugada
    def colocar_ficha(self, ficha, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("Coordenadas fuera de rango")
        if self._tablero[x][y] != 0:
            raise ValueError("La casilla ya está ocupada")
        
        self._tablero[x][y] = ficha
        
        return True
    
    # Método para verificar si hay un ganador en el juego
    def hay_ganador(self):
        for i in range(3):
            if self._tablero[i][0] == self._tablero[i][1] == self._tablero[i][2] != 0:
                return True
    
        for j in range(3):
            if self._tablero[0][j] == self._tablero[1][j] == self._tablero[2][j] != 0:
                return True
    
        if self._tablero[0][0] == self._tablero[1][1] == self._tablero[2][2] != 0:
            return True
        
        if self._tablero[0][2] == self._tablero[1][1] == self._tablero[2][0] != 0:
            return True
        
        return False
    
    # Método para verificar si el juego ha terminado en empate
    def juego_terminado(self):
        for i in range(3):
            for j in range(3):
                if self._tablero[i][j] == 0:
                    return False

        return True

    # Método para representar el estado actual del tablero como una cadena
    def __str__(self):
        resultado = "    1   2   3\n"
        resultado += "  " + "-" * 13 + "\n"
        
        for i in range(3):
            resultado += f"{i+1} |"
            for j in range(3):
                if self._tablero[i][j] == 0:
                    resultado += "   |"
                elif self._tablero[i][j] == 1:
                    resultado += " X |"
                elif self._tablero[i][j] == 2:
                    resultado += " O |"
            resultado += "\n"
            resultado += "  " + "-" * 13 + "\n"
        
        return resultado

# Clase para manejar la lógica del juego en la consola
class Juego:
    def main():
        juego = TresEnRaya()
        turno = TresEnRaya.FICHA_EQUIS
        
        while True:
            print(juego)
            if turno == TresEnRaya.FICHA_EQUIS:
                print("Turno de X")
            else:
                print("Turno de O")
            
            try:
                x = int(input("Ingrese la fila (1-3): ")) - 1
                y = int(input("Ingrese la columna (1-3): ")) - 1
                juego.colocar_ficha(turno, x, y)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            
            if juego.hay_ganador():
                print(juego)
                if turno == TresEnRaya.FICHA_EQUIS:
                    print("¡X ha ganado!")
                else:
                    print("¡O ha ganado!")
                break
            
            if juego.juego_terminado():
                print(juego)
                print("¡Empate!")
                break
            
            turno = TresEnRaya.FICHA_CIRULO if turno == TresEnRaya.FICHA_EQUIS else TresEnRaya.FICHA_EQUIS
    
if __name__ == "__main__":
    Juego.main()