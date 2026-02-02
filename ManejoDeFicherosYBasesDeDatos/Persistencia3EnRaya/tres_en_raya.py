import os

class TresEnRaya:
    # Constantes para representar las fichas y el estado del tablero
    CASILLA_VACIA = 0
    FICHA_EQUIS = 1
    FICHA_CIRCULO = 2

    def __init__(self):
        """Constructor que inicializa el tablero vacío."""
        self._tablero = [
            [self.CASILLA_VACIA for _ in range(3)]
            for _ in range(3)
        ]

    def guardar_tablero(self, nombre_archivo):
        """Método para guardar el estado actual del juego en un archivo.
        Params:
            nombre_archivo -- El nombre del archivo donde se guardará el estado del juego.
        """
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        encabezado = lineas[:3]
        encabezado = [linea if linea.endswith('\n') else linea + '\n' for linea in encabezado]
        
        with open(nombre_archivo, 'w') as archivo:
            archivo.writelines(encabezado)
            for fila in self._tablero:
                linea = ''.join(str(casilla) for casilla in fila)
                archivo.write(f"{linea}\n")

    @staticmethod
    def guardar_jugadores(jugador_1, jugador_2, nombre_archivo):
        """Método para guardar los nombres de los jugadores en un archivo.
        Params:
            jugador_1 -- Nombre del jugador 1 (X)
            jugador_2 -- Nombre del jugador 2 (O)
            nombre_archivo -- El nombre del archivo donde se guardarán los nombres de los jugadores.
        """
        with open(nombre_archivo, "wt") as archivo:
            archivo.write(f"{jugador_1}\n{jugador_2}\n")

    @staticmethod
    def guardar_turno(turno, nombre_archivo):
        """Método para guardar el turno actual en un archivo.
        Params:
            turno -- El turno actual (FICHA_EQUIS o FICHA_CIRCULO)
            nombre_archivo -- El nombre del archivo donde se guardará el turno actual.
        """
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

        if len(lineas) == 2:
            lineas.append(f"{turno}\n")
        else:
            lineas[2] = f"{turno}\n"

        with open(nombre_archivo, "w") as archivo:
            archivo.writelines(lineas)


    def nombre_jugadores(self):
        """Método para obtener los nombres de los jugadores.
        Returns:
            Una tupla con los nombres de los jugadores (jugador_X, jugador_O).
        """
        jugador_X = input("Ingrese el nombre del jugador X: ")
        jugador_O = input("Ingrese el nombre del jugador O: ")
        return jugador_X, jugador_O
    
    def colocar_ficha(self, ficha, x, y):
        """Metodo para colocar una ficha en el tablero.
        Params:
            ficha -- La ficha a colocar (FICHA_EQUIS o FICHA_CIRCULO)
            x -- La fila donde colocar la ficha (0-2)
            y -- La columna donde colocar la ficha (0-2)
        
        Returns:
            True si la ficha se colocó correctamente, False en caso contrario.
        
        Raises:
            ValueError si las coordenadas están fuera de rango o la casilla ya está ocupada.
        """
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("Coordenadas fuera de rango")
        if self._tablero[x][y] != 0:
            raise ValueError("La casilla ya está ocupada")
        
        self._tablero[x][y] = ficha
        
        return True
    
    def hay_ganador(self):
        """Método para verificar si hay un ganador en el juego.
        Returns:
            True si hay un ganador, False en caso contrario.
        """
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
    
    def cargar_juego(nombre_archivo):
        """Método para cargar el estado del juego desde un archivo.
        Params:
            nombre_archivo -- El nombre del archivo desde donde se cargará el estado del juego.
        
        Returns:
            Una lista con las líneas del archivo que representan el estado del juego."""
        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError(f"El archivo {nombre_archivo} no existe.")
        
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
        
        return lineas
        

    def juego_terminado(self):
        """Método para verificar si el juego ha terminado en empate.
        Returns:
            True si el juego ha terminado en empate, False en caso contrario.
        """
        for i in range(3):
            for j in range(3):
                if self._tablero[i][j] == 0:
                    return False

        return True

    def eliminar_archivo(self, archivo):
        os.remove(archivo)        

    def __str__(self):
        """Método para representar el tablero como una cadena de texto.
        Returns:
            Una cadena que representa el estado actual del tablero.
        """
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

class Juego:
    def main():
        while True:
            juego = TresEnRaya()
            turno = TresEnRaya.FICHA_EQUIS
            
            print("\nMenu:")
            print("1. Nuevo juego")
            print("2. Cargar juego")
            print("3. Salir")
            opcion = input("Seleccione una opción (1-3): ")

            if opcion == "3":
                print("¡Gracias por jugar!")
                break

            if opcion == "1":
                archivo = input("Introduzca el nombre de la partida:")
                if not archivo.endswith(".txt"):
                    archivo += ".txt"

                jugador_O, jugador_X = juego.nombre_jugadores()
                TresEnRaya.guardar_jugadores(jugador_X, jugador_O, archivo)

            elif opcion == "2":
                if not os.listdir():
                    print("No hay partidas guardadas.")
                    continue
                print("¿Que partida desea retomar?")
                count = 0

                for item in os.listdir():
                    if item.endswith(".txt"):
                        count += 1
                        print(f"{count}- {item}")

                archivo = input(f"Seleccione una de las partidas (1 - {count}):")

                archivos_txt = [item for item in os.listdir() if item.endswith(".txt")]
                try:
                    indice = int(archivo) - 1
                    if 0 <= indice < len(archivos_txt):
                        archivo = archivos_txt[indice]
                    else:
                        print("Índice fuera de rango.")
                        continue
                except ValueError:
                    print("Entrada inválida.")
                    continue
                    
                while(not os.path.exists(archivo)):
                    print("El archivo no existe. Intente de nuevo.")
                    archivo = input(f"Seleccione una de las partidas (1 - {count}):")

                try:
                    info_juego = TresEnRaya.cargar_juego(archivo)

                    jugador_X = info_juego[0].strip()
                    jugador_O = info_juego[1].strip()
                    turno = int(info_juego[2].strip())

                    juego._tablero = [
                        [int(casilla) for casilla in info_juego[i + 3].strip()]
                        for i in range(3)
                    ]
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                    continue
            
            else:
                print("Opción no válida.")
                continue
                
            while True:
                print(juego)
                if turno == TresEnRaya.FICHA_EQUIS:
                    print(f"Turno de {jugador_X}")
                else:
                    print(f"Turno de {jugador_O}")

                try:
                    print("Pulse S para guardar y salir.")
                    entrada = input("Ingrese la fila (1-3) o S para salir: ").strip().upper()

                    if entrada == 'S':
                        juego.guardar_turno(turno, archivo)
                        juego.guardar_tablero(archivo)
                        print("Juego guardado. Saliendo...")
                        break

                    x = int(entrada) - 1
                    y = int(input("Ingrese la columna (1-3): ")) - 1
                    
                    juego.colocar_ficha(turno, x, y)
                    juego.guardar_turno(turno, archivo)
                    juego.guardar_tablero(archivo)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

                if juego.hay_ganador():
                    juego.eliminar_archivo(archivo)
                    print(juego)
                    if turno == TresEnRaya.FICHA_EQUIS:
                        print(f"¡{jugador_X} ha ganado!")
                    else:
                        print(f"¡{jugador_O} ha ganado!")
                    break

                
                if juego.juego_terminado():
                    print(juego)
                    print("¡Empate!")
                    juego.eliminar_archivo(archivo)
                    break
                
                turno = TresEnRaya.FICHA_CIRCULO if turno == TresEnRaya.FICHA_EQUIS else TresEnRaya.FICHA_EQUIS
    
if __name__ == "__main__":
    Juego.main()