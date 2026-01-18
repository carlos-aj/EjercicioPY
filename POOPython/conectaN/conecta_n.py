import random
import time

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
        # Representación en cadena del tablero
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
        
        # Filas del tablero (mostramos desde fila 0 hasta fila última - sin inversión)
        for fila in range(filas):
            resultado += "│"
            for col in range(columnas):
                # Sin inversión - fila 0 se muestra arriba, fila 5 se muestra abajo
                resultado += self._obtener_contenido_casilla(self._tablero[fila][col])
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
        
        # Filas del tablero (sin inversión - fila 0 arriba, fila 5 abajo)
        for fila in range(filas):
            print("│", end="")
            for col in range(columnas):
                contenido = self._obtener_contenido_casilla(self._tablero[fila][col])
                
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
    def colocar_ficha(self, ficha, columna):
        if self.columna_llena(columna):
            return False
        
        # Buscar desde la fila más baja (índice más alto) hacia arriba
        for i in range(len(self._tablero)-1, -1, -1):
            if self._tablero[i][columna] == self.CASILLA_VACIA:
                self._tablero[i][columna] = ficha
                return i
        return False

    # Método para verificar si una columna está llena
    def columna_llena(self, columna):
        if columna < 0 or columna >= len(self._tablero[0]):
            return True
        # Una columna está llena si la fila superior (índice 0) tiene una ficha
        return self._tablero[0][columna] != self.CASILLA_VACIA
    
    # Encuentra la fila donde se encuentra la primera ficha del número dado en la columna especificada
    def _encontrar_fila_ficha(self, tablero, columna, numero):
        for fila in range(len(tablero)):
            if tablero[fila][columna] == numero:
                return fila
        return -1

    # Cuenta fichas consecutivas en una dirección específica desde una posición inicial
    def _contar_fichas_direccion(self, tablero, fila_inicio, col_inicio, direccion_fila, direccion_col, numero):
        contador = 0
        filas = len(tablero)
        columnas = len(tablero[0])
        
        fila, col = fila_inicio, col_inicio
        
        while (0 <= fila < filas and 
               0 <= col < columnas and 
               tablero[fila][col] == numero):
            contador += 1
            fila += direccion_fila
            col += direccion_col
            
        return contador
    
    # Verifica si hay una línea de n fichas en una dirección específica y su opuesta
    def _verificar_linea_direccion(self, tablero, fila_ficha, columna, numero, direccion_fila, direccion_col, numero_fichas_linea):
        # Contar en la dirección positiva (sin incluir la ficha central)
        contador_positivo = self._contar_fichas_direccion(
            tablero, fila_ficha + direccion_fila, columna + direccion_col, 
            direccion_fila, direccion_col, numero
        )
        
        # Contar en la dirección negativa (sin incluir la ficha central)
        contador_negativo = self._contar_fichas_direccion(
            tablero, fila_ficha - direccion_fila, columna - direccion_col, 
            -direccion_fila, -direccion_col, numero
        )
        
        # Total: fichas en ambas direcciones + la ficha central
        contador_total = contador_positivo + contador_negativo + 1
        
        return contador_total >= numero_fichas_linea

    # Comprueba si hay n fichas en línea después de colocar una ficha en la columna especificada.
    def comprobar_linea(self, columna, numero):
        # Encontrar la fila donde está la ficha
        fila_ficha = self._encontrar_fila_ficha(self._tablero, columna, numero)
        
        if fila_ficha == -1:
            return False
        
        # Definir las direcciones a verificar: (direccion_fila, direccion_col)
        direcciones = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal principal (\)
            (1, -1)   # Diagonal secundaria (/)
        ]
        
        # Verificar cada dirección
        for direccion_fila, direccion_col in direcciones:
            if self._verificar_linea_direccion(
                self._tablero, fila_ficha, columna, numero, 
                direccion_fila, direccion_col, self._cantidad_victoria
            ):
                return True
        
        return False

    # Obtiene las posiciones de las fichas que forman la línea ganadora
    def obtener_posiciones_victoria(self, columna, numero):
        fila_ficha = self._encontrar_fila_ficha(self._tablero, columna, numero)
        
        if fila_ficha == -1:
            return []
        
        filas = len(self._tablero)
        columnas = len(self._tablero[0])
        
        # Verificar horizontal
        posiciones = [(fila_ficha, columna)]
        
        for col in range(columna - 1, -1, -1):
            if self._tablero[fila_ficha][col] == numero:
                posiciones.append((fila_ficha, col))
            else:
                break
        
        for col in range(columna + 1, columnas):
            if self._tablero[fila_ficha][col] == numero:
                posiciones.append((fila_ficha, col))
            else:
                break
        
        if len(posiciones) >= self._cantidad_victoria:
            return posiciones
        
        # Verificar vertical
        posiciones = [(fila_ficha, columna)]
        for fila in range(fila_ficha + 1, filas):
            if self._tablero[fila][columna] == numero:
                posiciones.append((fila, columna))
            else:
                break
        
        if len(posiciones) >= self._cantidad_victoria:
            return posiciones
        
        # Verificar diagonal principal
        posiciones = [(fila_ficha, columna)]
        
        fila, col = fila_ficha - 1, columna - 1
        while fila >= 0 and col >= 0:
            if self._tablero[fila][col] == numero:
                posiciones.append((fila, col))
                fila -= 1
                col -= 1
            else:
                break
        
        fila, col = fila_ficha + 1, columna + 1
        while fila < filas and col < columnas:
            if self._tablero[fila][col] == numero:
                posiciones.append((fila, col))
                fila += 1
                col += 1
            else:
                break
        
        if len(posiciones) >= self._cantidad_victoria:
            return posiciones
        
        # Verificar diagonal secundaria
        posiciones = [(fila_ficha, columna)]
        
        fila, col = fila_ficha - 1, columna + 1
        while fila >= 0 and col < columnas:
            if self._tablero[fila][col] == numero:
                posiciones.append((fila, col))
                fila -= 1
                col += 1
            else:
                break
        
        fila, col = fila_ficha + 1, columna - 1
        while fila < filas and col >= 0:
            if self._tablero[fila][col] == numero:
                posiciones.append((fila, col))
                fila += 1
                col -= 1
            else:
                break
        
        if len(posiciones) >= self._cantidad_victoria:
            return posiciones
        
        return []

    # Muestra el tablero marcando las casillas ganadoras con color verde
    def marcar_victoria(self, columna, numero):
        filas = len(self._tablero)
        columnas = len(self._tablero[0])
        
        posiciones_victoria = self.obtener_posiciones_victoria(columna, numero)
        
        GREEN_BG = '\033[42m'
        
        resultado = ""
        
        # Números de columnas
        resultado += "  "
        for col in range(columnas):
            resultado += f"{col + 1:3}  "
        resultado += "\n"
        
        # Línea superior
        resultado += "┌" + "────┬" * (columnas - 1) + "────┐\n"
        
        # Filas del tablero (sin inversión - fila 0 arriba, fila 5 abajo)
        for fila in range(filas):
            resultado += "│"
            for col in range(columnas):
                contenido = self._obtener_contenido_casilla(self._tablero[fila][col])
                
                if (fila, col) in posiciones_victoria:
                    resultado += f"{GREEN_BG}{contenido}{self.RESET}"
                else:
                    resultado += contenido
                    
                if col < columnas - 1:
                    resultado += "│"
            resultado += "│\n"
            
            # Separadores entre filas (excepto la última)
            if fila < filas - 1:
                resultado += "├" + "────┼" * (columnas - 1) + "────┤\n"
        
        # Línea inferior
        resultado += "└" + "────┴" * (columnas - 1) + "────┘"
        
        print(resultado)

    # Simula colocar una ficha temporalmente y cuenta el máximo de fichas en línea
    def fichas_en_linea(self, ficha, columna):
        fila_simulada = -1
        for i in range(len(self._tablero)-1, -1, -1):
            if self._tablero[i][columna] == self.CASILLA_VACIA:
                fila_simulada = i
                break
        
        if fila_simulada == -1:
            return 0
        
        # Colocar temporalmente la ficha
        self._tablero[fila_simulada][columna] = ficha
        
        # Encontrar el máximo número de fichas en línea
        max_fichas = 1
        for longitud in range(2, max(len(self._tablero), len(self._tablero[0])) + 1):
            if self.comprobar_linea(columna, ficha):
                max_fichas = longitud
            else:
                break
        
        # Quitar la ficha temporal
        self._tablero[fila_simulada][columna] = self.CASILLA_VACIA
        
        return max_fichas

    # Comprueba si quedan casillas libres
    def hay_casillas_libres(self):
        for fila in self._tablero:
            for casilla in fila:
                if casilla == self.CASILLA_VACIA:
                    return True
        return False

    # Comprueba si el juego ha terminado y retorna el resultado
    def comprobar_fin_juego(self, columna, numero):
        ganador = self.comprobar_linea(columna, numero)
        casillas_libres = self.hay_casillas_libres()

        if not casillas_libres:
            print("FIN DE JUEGO")
            print("No quedan casillas libres")
            return True
         
        if ganador:
            self.marcar_victoria(columna, numero)
            print("FIN DE JUEGO")
            return True
        
        return False

class Juego:
    # Solicita tamaño de tablero con validaciones
    @staticmethod
    def solicitar_tamano_tablero():
        # Validación directa sin módulo externo
        while True:
            try:
                filas = int(input("Introduce el número de filas (mínimo 6): "))
                if filas < 6:
                    print("Error: El número de filas debe ser al menos 6. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Debes introducir un número entero válido.")
        
        while True:
            try:
                columnas = int(input("Introduce el número de columnas (mínimo 7): "))
                if columnas < 7:
                    print("Error: El número de columnas debe ser al menos 7. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Debes introducir un número entero válido.")
        
        return filas, columnas

    # Solicita numero de fichas en linea para victoria con validacion
    @staticmethod
    def solicitar_cantidad_victoria(filas, columnas):
        maximo = max(filas, columnas)
        
        while True:
            try:
                cantidad = int(input(f"Introduce el número de fichas para ganar (4-{maximo}): "))
                if cantidad < 4:
                    print("Error: El número mínimo de fichas para ganar es 4. Inténtalo de nuevo.")
                    continue
                if cantidad > maximo:
                    print(f"Error: El número máximo de fichas para ganar en este tablero es {maximo}. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Debes introducir un número entero válido.")
        
        return cantidad

    # Solicita el modo de juego, si es un jugador solicita la dificultad de la maquina
    @staticmethod
    def solicitar_modo_juego():
        print("MODO DE JUEGO")
        print("-------------")
        print("1. Un jugador")
        print("2. Dos jugadores")
        
        while True:
            try:
                modo_juego = int(input("Elije un modo de juego (1-2): "))
                if modo_juego not in [1, 2]:
                    print("Error: Debes elegir 1 o 2. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Debes introducir un número entero válido.")
        
        dificultad = None
        if modo_juego == 1:
            print("Selecciona la dificultad:")
            print("1. Nivel 1")
            print("2. Nivel 2")
            
            while True:
                try:
                    dificultad = int(input("Elije la dificultad (1-2): "))
                    if dificultad not in [1, 2]:
                        print("Error: Debes elegir 1 o 2. Inténtalo de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Error: Debes introducir un número entero válido.")
        
        return (modo_juego, dificultad)

    # Solicita el nombre de los jugadores, en caso de ser contra la maquina solo solicita uno
    @staticmethod
    def solicitar_nombre_jugadores(modo_juego):
        while True:
            jugador1 = input("Introduce el nombre del jugador 1: ").strip()
            if jugador1:
                break
            print("Error: El nombre no puede estar vacío. Inténtalo de nuevo.")
        
        jugador2 = None
        if modo_juego == 2:
            while True:
                jugador2 = input("Introduce el nombre del jugador 2: ").strip()
                if jugador2:
                    break
                print("Error: El nombre no puede estar vacío. Inténtalo de nuevo.")
        
        return jugador1, jugador2

    # Obtiene la columna elegida por el jugador humano con validación
    @staticmethod
    def obtener_jugada_humano(turno, n_columnas, juego):
        while True:
            try:
                columna = int(input(f"{turno[1]} Introduzca la columna (1-{n_columnas}): "))
                if 1 <= columna <= n_columnas:
                    if not juego.columna_llena(columna-1):
                        return columna - 1
                    else:
                        print("¡La columna está llena! Elige otra columna.")
                else:
                    print(f"Error: Debes introducir un número entre 1 y {n_columnas}.")
            except ValueError:
                print("Error: Debes introducir un número válido.")

    @staticmethod
    # Obtiene jugada aleatoria de la máquina para nivel 1
    def obtener_jugada_maquina_nivel1(n_columnas, juego):
        columnas_disponibles = [i for i in range(n_columnas) if not juego.columna_llena(i)]
        if not columnas_disponibles:
            return None
        return random.choice(columnas_disponibles)

    @staticmethod
    # Obtiene jugada inteligente de la máquina para nivel 2
    def obtener_jugada_maquina_nivel2(n_columnas, juego):
        columnas_disponibles = [i for i in range(n_columnas) if not juego.columna_llena(i)]
        if not columnas_disponibles:
            return None
        
        mejor_columna = None
        
        # 1. Intentar ganar
        for col in columnas_disponibles:
            fichas_maquina = juego.fichas_en_linea(ConectaN.FICHA_CIRULO, col)
            if fichas_maquina >= juego.cantidad_victoria:
                mejor_columna = col
                break

        # 2. Bloquear al jugador
        if mejor_columna is None:
            for col in columnas_disponibles:
                fichas_jugador = juego.fichas_en_linea(ConectaN.FICHA_EQUIS, col)
                if fichas_jugador >= juego.cantidad_victoria:
                    mejor_columna = col
                    break

        # 3. Buscar la mejor jugada
        if mejor_columna is None:
            max_fichas = 0
            for col in columnas_disponibles:
                fichas_maquina = juego.fichas_en_linea(ConectaN.FICHA_CIRULO, col)
                if fichas_maquina > max_fichas:
                    max_fichas = fichas_maquina
                    mejor_columna = col

        # 4. Jugada aleatoria como último recurso
        if mejor_columna is None:
            mejor_columna = random.choice(columnas_disponibles)

        return mejor_columna

    # Controla el flujo del juego para dos jugadores
    @staticmethod
    def juego_dos_jugadores(juego, jugador1, jugador2):
        ficha_jugador1 = (ConectaN.FICHA_EQUIS, jugador1.upper())
        ficha_jugador2 = (ConectaN.FICHA_CIRULO, jugador2.upper())
        turno = ficha_jugador1
        
        n_columnas = len(juego._tablero[0])
        
        print(juego)
        
        while True:
            columna = Juego.obtener_jugada_humano(turno, n_columnas, juego)
            juego.colocar_ficha(turno[0], columna)
            juego.mostrar_tablero_columna(columna)
            
            if juego.comprobar_fin_juego(columna, turno[0]):
                if juego.comprobar_linea(columna, turno[0]):
                    print(f"{turno[1]} HA GANADO")
                break

            turno = ficha_jugador2 if turno == ficha_jugador1 else ficha_jugador1

    # Controla el flujo del juego para un jugador contra la máquina
    @staticmethod
    def juego_solitario(juego, jugador1, nivel):        
        ficha_jugador1 = (ConectaN.FICHA_EQUIS, jugador1.upper())
        ficha_maquina = (ConectaN.FICHA_CIRULO, "LA MAQUINA")
        turno = ficha_jugador1
        
        n_columnas = len(juego._tablero[0])

        print(juego)

        while True:
            if turno[0] == ConectaN.FICHA_CIRULO:  # Turno de la máquina
                time.sleep(2)
                
                if nivel == 1:
                    columna = Juego.obtener_jugada_maquina_nivel1(n_columnas, juego)
                else: 
                    columna = Juego.obtener_jugada_maquina_nivel2(n_columnas, juego)
                
                if columna is None:
                    print("FIN DE JUEGO")
                    print("No hay columnas disponibles")
                    break
            else:  # Turno del jugador
                columna = Juego.obtener_jugada_humano(turno, n_columnas, juego)

            juego.colocar_ficha(turno[0], columna)
            juego.mostrar_tablero_columna(columna)
            
            if juego.comprobar_fin_juego(columna, turno[0]):
                if juego.comprobar_linea(columna, turno[0]):
                    print(f"{turno[1]} HA GANADO")
                break

            turno = ficha_maquina if turno == ficha_jugador1 else ficha_jugador1
        
    # Función principal del juego
    @staticmethod
    def main():
        print("=== CONECTA N ===")
        
        # Configuración del juego
        filas, columnas = Juego.solicitar_tamano_tablero()
        cantidad_victoria = Juego.solicitar_cantidad_victoria(filas, columnas)
        modo_juego, dificultad = Juego.solicitar_modo_juego()
        jugador1, jugador2 = Juego.solicitar_nombre_jugadores(modo_juego)
        
        # Crear el juego
        try:
            juego = ConectaN(filas, columnas, cantidad_victoria, modo_juego, jugador1, jugador2)
            
            # Iniciar el juego según el modo
            if modo_juego == 1:
                Juego.juego_solitario(juego, jugador1, dificultad)
            else:
                Juego.juego_dos_jugadores(juego, jugador1, jugador2)
                
        except ValueError as e:
            print(f"Error al crear el juego: {e}")
    
if __name__ == "__main__":
    Juego.main()
