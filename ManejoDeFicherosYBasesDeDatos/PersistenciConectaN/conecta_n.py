import os
import random
import time

class ConectaN:
    # Constantes para representar las fichas y el estado del tablero
    CASILLA_VACIA = 0
    FICHA_EQUIS = 1
    FICHA_CIRCULO = 2
    
    # Constantes para colores de terminal
    RESET = '\033[0m'
    YELLOW_BG = '\033[43m'

    def __init__(self, filas = 6, columnas = 7, cantidad_victoria = 4, modo_juego = 1, jugador_1 = " ", jugador_2= ""):
        """Constructor de la clase ConectaN. Inicializa el tablero y los parámetros del juego.
        Params:
            filas (int): Número de filas del tablero.
            columnas (int): Número de columnas del tablero.
            cantidad_victoria (int): Número de fichas en línea necesarias para ganar.
            modo_juego (int): Modo de juego (1 para un jugador, 2 para dos jugadores).
            jugador_1 (str): Nombre del jugador 1.
            jugador_2 (str): Nombre del jugador 2.
            
        Raises:
            ValueError: Si el tamaño del tablero es menor que 6x7 o si el modo de juego no es válido.
        """
        if not ConectaN.validar_tamano_tablero(filas, columnas):
            raise ValueError("El tamaño mínimo del tablero es de 6x7")
        
        # Tablero organizado como [fila][columna] para mayor intuición
        self._tablero = [
            [self.CASILLA_VACIA for _ in range(columnas)]
            for _ in range(filas)
        ]

        if not ConectaN.validar_modo_juego(modo_juego):
            raise ValueError("Modo de juego no válido")

        self._cantidad_victoria = cantidad_victoria
        self._modo_juego = modo_juego
        self._jugador_1 = jugador_1
        self._jugador_2 = jugador_2

    # Getters y Setters
    @property
    def tablero(self):
        """Metodo getter para el tablero del juego.
         Returns:
            list: El tablero del juego.
        """
        return self._tablero
    
    @property
    def cantidad_victoria(self):
        """Metodo getter para la cantidad de fichas necesarias para ganar.
         Returns:
            int: La cantidad de fichas necesarias para ganar.
        """
        return self._cantidad_victoria
    
    @property
    def modo_juego(self):
        """Metodo getter para el modo de juego.
         Returns:
            int: El modo de juego.
        """
        return self._modo_juego
    
    @property
    def jugador_1(self):
        """Metodo getter para el jugador 1.
         Returns:
            str: El nombre del jugador 1.
        """
        return self._jugador_1

    @property
    def jugador_2(self):
        """Metodo getter para el jugador 2.
         Returns:
            str: El nombre del jugador 2.
        """
        return self._jugador_2

    @cantidad_victoria.setter
    def cantidad_victoria(self, cantidad_victoria):
        """Metodo setter para la cantidad de fichas necesarias para ganar con comprobación.
        Params:
            cantidad_victoria (int): La cantidad de fichas necesarias para ganar.
        
        Raises:
            ValueError: Si la cantidad de fichas para la victoria es mayor que el máximo permitido.
        """
        filas = len(self._tablero)
        columnas = len(self._tablero[0])
        maximo = max(filas, columnas)

        if cantidad_victoria > maximo:
            raise ValueError(f"La cantidad de fichas para la victoria en este tablero no puede ser mayor a {maximo}")
        
        self._cantidad_victoria = cantidad_victoria
    
    @modo_juego.setter
    def modo_juego(self, modo_juego):
        """Metodo setter para el modo de juego con comprobación.
        Params:
            modo_juego (int): El modo de juego.
        Raises:
            ValueError: Si el modo de juego no es válido.
        """
        if not ConectaN.validar_modo_juego(modo_juego):
            raise ValueError("Modo de juego no válido")
        self._modo_juego = modo_juego

    @jugador_1.setter
    def jugador_1(self, jugador_1):
        """Metodo setter para el jugador 1.
        Params:
            jugador_1 (str): El nombre del jugador 1.
        """
        self._jugador_1 = jugador_1

    @jugador_2.setter
    def jugador_2(self, jugador_2):
        """Metodo setter para el jugador 2. Si el modo de juego es 2, se asigna "BOT".
        Params:
            jugador_2 (str): El nombre del jugador 2.
        """
        if self.modo_juego == 2:
            self._jugador_2 = "BOT"
        else:   
            self._jugador_2 = jugador_2

    # Métodos de validación
    @staticmethod
    def validar_tamano_tablero(filas, columnas):
        """Método estático para validar el tamaño del tablero.
        Params:
            filas (int): Número de filas del tablero.
            columnas (int): Número de columnas del tablero.

        Raises:
            ValueError: Si el tamaño del tablero es menor que 6x7.

        Returns:
            bool: True si el tamaño es válido."""
        if filas < 6 or columnas < 7:
            raise ValueError("El tamaño mínimo del tablero es de 6x7")
        return True
    
    @staticmethod
    def validar_modo_juego(modo_juego):
        """Método estático para validar el modo de juego.
        Params:
            modo_juego (int): Modo de juego.
        
        Raises:
            ValueError: Si el modo de juego no es válido.
        
        Returns:
            bool: True si el modo de juego es válido.
        """
        if modo_juego < 1 or modo_juego > 2:
            raise ValueError("El modo de juego solo puede ser 1 o 2")
        return True
    
    def __str__(self):
        """Método para representar el tablero como una cadena de texto.
        Returns:
            str: Representación en cadena del tablero.
        """
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

    def _obtener_contenido_casilla(self, valor):
        """Método para obtener el contenido de una casilla.
        Params:
            valor (int): Valor de la casilla.

        Returns:
            str: Representación en cadena del contenido de la casilla.
        """
        if valor == self.CASILLA_VACIA:
            return "    "
        elif valor == self.FICHA_EQUIS:
            return " X  "
        elif valor == self.FICHA_CIRCULO:
            return " O  "
        return "    "
    
    def colocar_ficha(self, ficha, columna):
        """Método para colocar una ficha en una columna.
        Params:
            ficha (int): Valor de la ficha a colocar.
            columna (int): Índice de la columna donde colocar la ficha.

        Returns:
            bool: True si se colocó la ficha correctamente, False si la columna está llena.
        """
        if self.columna_llena(columna):
            return False
        
        # Buscar desde la fila más baja (índice más alto) hacia arriba
        for i in range(len(self._tablero)-1, -1, -1):
            if self._tablero[i][columna] == self.CASILLA_VACIA:
                self._tablero[i][columna] = ficha
                return True
        return False

    def columna_llena(self, columna):
        """Método para verificar si una columna está llena.
        Params:
            columna (int): Índice de la columna a verificar.

        Returns:
            bool: True si la columna está llena, False en caso contrario.
        """
        if columna < 0 or columna >= len(self._tablero[0]):
            return True
        # Una columna está llena si la fila superior (índice 0) tiene una ficha
        return self._tablero[0][columna] != self.CASILLA_VACIA
    
    def _encontrar_fila_ficha(self, tablero, columna, numero):
        """Encuentra la fila donde se encuentra la ficha en la columna especificada.
        Params:
            tablero (list): El tablero del juego.
            columna (int): Índice de la columna a buscar.
            numero (int): Valor de la ficha a buscar.
        
        Returns:
            int: Índice de la fila donde se encuentra la ficha, o -1 si no se encuentra.
        """
        for fila in range(len(tablero)):
            if tablero[fila][columna] == numero:
                return fila
        return -1

    def _contar_fichas_direccion(self, tablero, fila_inicio, col_inicio, direccion_fila, direccion_col, numero):
        """Cuenta las fichas en una dirección específica desde una posición inicial.
        Params:
            tablero (list): El tablero del juego.
            fila_inicio (int): Fila inicial para comenzar a contar.
            col_inicio (int): Columna inicial para comenzar a contar.
            direccion_fila (int): Dirección de fila (1, 0, -1).
            direccion_col (int): Dirección de columna (1, 0, -1).
            numero (int): Valor de la ficha a contar.
        
        Returns:
            int: Número de fichas contadas en la dirección especificada.
        """
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
    
    def _verificar_linea_direccion(self, tablero, fila_ficha, columna, numero, direccion_fila, direccion_col, numero_fichas_linea):
        """Verifica si hay una línea de n fichas en una dirección específica y su opuesta.
        Params:
            tablero (list): El tablero del juego.
            fila_ficha (int): Fila de la ficha central.
            columna (int): Columna de la ficha central.
            numero (int): Valor de la ficha a verificar.
            direccion_fila (int): Dirección de fila (1, 0, -1).
            direccion_col (int): Dirección de columna (1, 0, -1).
            numero_fichas_linea (int): Número de fichas necesarias para ganar.

        Returns:
            bool: True si hay una línea de n fichas, False en caso contrario.
        """
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

    def comprobar_linea(self, columna, numero):
        """Comprueba si hay n fichas en línea después de colocar una ficha en la columna especificada.
        Params:
            columna (int): Columna donde se colocó la ficha.
            numero (int): Valor de la ficha colocada.

        Returns:
            bool: True si hay una línea de n fichas, False en caso contrario.
        """
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

    def obtener_posiciones_victoria(self, columna, numero):
        """Obtiene las posiciones de las fichas que forman la línea ganadora.
        Params:
            columna (int): Columna donde se colocó la ficha.
            numero (int): Valor de la ficha colocada.
        
        Returns:
            list: Lista de tuplas con las posiciones de las fichas que forman la línea ganadora.
        """
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

    def fichas_en_linea(self, ficha, columna):
        """Calcula el máximo número de fichas en línea que se formarían al colocar una ficha en la columna especificada.
        Params:
            ficha (int): Valor de la ficha a colocar.
            columna (int): Índice de la columna donde se colocaría la ficha.
        
        Returns:
            int: Máximo número de fichas en línea que se formarían.
        """
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

    def hay_casillas_libres(self):
        """Verifica si hay casillas libres en el tablero.
        Returns:
            bool: True si hay casillas libres, False en caso contrario.
        """
        for fila in self._tablero:
            for casilla in fila:
                if casilla == self.CASILLA_VACIA:
                    return True
        return False

    def hay_fin_juego(self, columna, numero):
        """Comprueba si el juego ha terminado por victoria o empate.
        Params:
            columna (int): Columna donde se colocó la ficha.
            numero (int): Valor de la ficha colocada.
        
        Returns:
            str: 'victoria' si hay ganador, 'empate' si no hay casillas libres, None si continúa.
        """
        if self.comprobar_linea(columna, numero):
            return 'victoria'
        
        if not self.hay_casillas_libres():
            return 'empate'
        
        return None

    def obtener_jugada_maquina_nivel1(self):
        """Método para obtener jugada aleatoria de la máquina para nivel 1.
        Returns:
            int: Índice de la columna seleccionada por la máquina, o None si no hay columnas disponibles.
        """
        n_columnas = len(self._tablero[0])
        columnas_disponibles = [i for i in range(n_columnas) if not self.columna_llena(i)]
        if not columnas_disponibles:
            return None
        return random.choice(columnas_disponibles)

    def obtener_jugada_maquina_nivel2(self):
        """Método para obtener jugada inteligente de la máquina para nivel 2.
        Returns:
            int: Índice de la columna seleccionada por la máquina, o None si no hay columnas disponibles.
        """
        n_columnas = len(self._tablero[0])
        columnas_disponibles = [i for i in range(n_columnas) if not self.columna_llena(i)]
        if not columnas_disponibles:
            return None
        
        mejor_columna = None
        
        # 1. Intentar ganar
        for col in columnas_disponibles:
            fichas_maquina = self.fichas_en_linea(self.FICHA_CIRCULO, col)
            if fichas_maquina >= self._cantidad_victoria:
                mejor_columna = col
                break

        # 2. Bloquear al jugador
        if mejor_columna is None:
            for col in columnas_disponibles:
                fichas_jugador = self.fichas_en_linea(self.FICHA_EQUIS, col)
                if fichas_jugador >= self._cantidad_victoria:
                    mejor_columna = col
                    break

        # 3. Buscar la mejor jugada
        if mejor_columna is None:
            max_fichas = 0
            for col in columnas_disponibles:
                fichas_maquina = self.fichas_en_linea(self.FICHA_CIRCULO, col)
                if fichas_maquina > max_fichas:
                    max_fichas = fichas_maquina
                    mejor_columna = col

        # 4. Jugada aleatoria como último recurso
        if mejor_columna is None:
            mejor_columna = random.choice(columnas_disponibles)

        return mejor_columna

class Juego:
    @staticmethod
    def mostrar_tablero_columna(juego, columna_ultima_fila):
        """Método para mostrar el tablero resaltando la última columna jugada.
        Params:
            juego (ConectaN): Instancia del juego.
            columna_ultima_fila (int): Índice de la última columna donde se colocó una ficha.
        """
        filas = len(juego._tablero)
        columnas = len(juego._tablero[0])
        YELLOW_BG = '\033[43m'
        RESET = '\033[0m'
        
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
                contenido = juego._obtener_contenido_casilla(juego._tablero[fila][col])
                
                # Resaltar columna si es la última donde se colocó una ficha
                if col == columna_ultima_fila:
                    print(f"{YELLOW_BG}{contenido}{RESET}", end="")
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

    @staticmethod
    def marcar_victoria(juego, columna, numero):
        """Marca la línea ganadora en el tablero resaltándola.
        Params:
            juego (ConectaN): Instancia del juego.
            columna (int): Columna donde se colocó la ficha.
            numero (int): Valor de la ficha colocada.
        """
        filas = len(juego._tablero)
        columnas = len(juego._tablero[0])
        RESET = '\033[0m'
        GREEN_BG = '\033[42m'
        
        posiciones_victoria = juego.obtener_posiciones_victoria(columna, numero)
        
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
                contenido = juego._obtener_contenido_casilla(juego._tablero[fila][col])
                
                if (fila, col) in posiciones_victoria:
                    resultado += f"{GREEN_BG}{contenido}{RESET}"
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

    @staticmethod
    def solicitar_tamano_tablero():
        """Método para solicitar el tamaño del tablero con validaciones."""
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

    @staticmethod
    def solicitar_cantidad_victoria(filas, columnas):
        """Método para solicitar la cantidad de fichas necesarias para ganar con validaciones.
        Params:
            filas (int): Número de filas del tablero.
            columnas (int): Número de columnas del tablero.
        
        Returns:
            int: Cantidad de fichas necesarias para ganar."""
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

    @staticmethod
    def solicitar_modo_juego():
        """Método para solicitar el modo de juego con validaciones."""
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

    def solicitar_nombre_jugadores(modo_juego):
        """Método para solicitar los nombres de los jugadores con validaciones.
        Params:
            modo_juego (int): Modo de juego (1 para un jugador, 2 para dos jugadores).
        
        Returns:
            tuple: Nombres de los jugadores.
        """
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

    @staticmethod
    def guardar_jugadores(nombre_archivo, jugador_1, jugador_2, cantidad_victoria, dificultad=0):
        """Guarda los nombres de los jugadores y configuración del juego en un archivo de texto.
        Params:
            nombre_archivo (str): Nombre del archivo donde se guardarán los datos.
            jugador_1 (str): Nombre del jugador 1.
            jugador_2 (str): Nombre del jugador 2.
            cantidad_victoria (int): Cantidad de fichas necesarias para ganar.
            dificultad (int): Dificultad del bot (0 si es 2 jugadores).
        """
        with open(nombre_archivo, "wt") as archivo:
            archivo.write(f"{jugador_1}\n{jugador_2}\n0\n{cantidad_victoria}\n{dificultad}\n")

    @staticmethod
    def guardar_turno(nombre_archivo, turno):
        """Guarda el turno actual en un archivo de texto.
        Params:
            nombre_archivo (str): Nombre del archivo donde se guardará el turno actual.
            turno (int): Turno actual.
        """
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

        # El turno está en la línea 3 (índice 2)
        if len(lineas) >= 3:
            lineas[2] = f"{turno}\n"
        else:
            # Esto no debería suceder, pero por seguridad
            while len(lineas) < 3:
                lineas.append("\n")
            lineas[2] = f"{turno}\n"

        with open(nombre_archivo, "w") as archivo:
            archivo.writelines(lineas)

    def eliminar_archivo(archivo):
        """Elimina un archivo del sistema.
        Params:
            archivo (str): Nombre del archivo a eliminar.
        """
        if os.path.exists(archivo):
            os.remove(archivo)

    def cargar_juego(nombre_archivo):
        """Carga el estado del juego desde un archivo de texto.
        Params:
            nombre_archivo (str): Nombre del archivo desde donde se cargará el juego.
        
        Returns:
            list: Líneas del archivo cargado.
        """
        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError(f"El archivo {nombre_archivo} no existe.")
        
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
        
        return lineas

    @staticmethod
    def obtener_jugada_humano(turno, n_columnas, juego):
        """Método para obtener la jugada del jugador humano con validaciones.
        Params:
            turno (tuple): Tupla con la ficha y el nombre del jugador.
            n_columnas (int): Número de columnas del tablero.
            juego (ConectaN): Instancia del juego.
        
        Returns:
            int: Índice de la columna seleccionada por el jugador, o None si quiere salir.
        """
        while True:
            try:
                print("Pulse S para guardar y salir.")
                entrada = input(f"{turno[1]} Introduzca la columna (1-{n_columnas}) o S para salir: ").strip().upper()
                
                if entrada == 'S':
                    return None
                
                columna = int(entrada)
                if 1 <= columna <= n_columnas:
                    if not juego.columna_llena(columna-1):
                        return columna - 1
                    else:
                        print("¡La columna está llena! Elige otra columna.")
                else:
                    print(f"Error: Debes introducir un número entre 1 y {n_columnas}.")
            except ValueError:
                print("Error: Debes introducir un número válido o 'S' para salir.")

    @staticmethod
    def juego_dos_jugadores(juego, jugador1, jugador2, archivo="partida_guardada.txt"):
        """Método para controlar el flujo del juego para dos jugadores.
        
        Params:
            juego (ConectaN): Instancia del juego.
            jugador1 (str): Nombre del jugador 1.
            jugador2 (str): Nombre del jugador 2.
            archivo (str): Nombre del archivo donde se guardará la partida.
        """
        ficha_jugador1 = (ConectaN.FICHA_EQUIS, jugador1.upper())
        ficha_jugador2 = (ConectaN.FICHA_CIRCULO, jugador2.upper())
        turno = ficha_jugador1
        
        n_columnas = len(juego._tablero[0])
        
        print(juego)
        
        while True:
            columna = Juego.obtener_jugada_humano(turno, n_columnas, juego)
            
            if columna is None:
                Juego.guardar_turno(archivo, 1 if turno == ficha_jugador1 else 2)
                Juego.guardar_tablero(juego._tablero, archivo)
                print("Juego guardado. Saliendo...")
                break
            
            juego.colocar_ficha(turno[0], columna)
            Juego.mostrar_tablero_columna(juego, columna)
            Juego.guardar_turno(archivo, 1 if turno == ficha_jugador1 else 2)
            Juego.guardar_tablero(juego._tablero, archivo)
            
            resultado = juego.hay_fin_juego(columna, turno[0])
            if resultado:
                if resultado == 'victoria':
                    Juego.marcar_victoria(juego, columna, turno[0])
                    print("FIN DE JUEGO")
                    print(f"{turno[1]} HA GANADO")
                elif resultado == 'empate':
                    print("FIN DE JUEGO")
                    print("No quedan casillas libres")
                Juego.eliminar_archivo(archivo)
                break

            turno = ficha_jugador2 if turno == ficha_jugador1 else ficha_jugador1

    @staticmethod
    def juego_solitario(juego, jugador1, nivel, archivo="partida_guardada.txt"):        
        """Método para controlar el flujo del juego para un jugador contra la máquina.
        Params:
            juego (ConectaN): Instancia del juego.
            jugador1 (str): Nombre del jugador 1.
            nivel (int): Nivel de dificultad de la máquina.
            archivo (str): Nombre del archivo donde se guardará la partida.
        """
        ficha_jugador1 = (ConectaN.FICHA_EQUIS, jugador1.upper())
        ficha_maquina = (ConectaN.FICHA_CIRCULO, "LA MAQUINA")
        turno = ficha_jugador1
        
        n_columnas = len(juego._tablero[0])

        print(juego)

        while True:
            if turno[0] == ConectaN.FICHA_CIRCULO:  # Turno de la máquina
                time.sleep(2)
                
                if nivel == 1:
                    columna = juego.obtener_jugada_maquina_nivel1()
                else: 
                    columna = juego.obtener_jugada_maquina_nivel2()
                
                if columna is None:
                    print("FIN DE JUEGO")
                    print("No hay columnas disponibles")
                    Juego.eliminar_archivo(archivo)
                    break
            else:  # Turno del jugador
                columna = Juego.obtener_jugada_humano(turno, n_columnas, juego)
                
                if columna is None:
                    Juego.guardar_turno(archivo, 1 if turno == ficha_jugador1 else 2)
                    Juego.guardar_tablero(juego._tablero, archivo)
                    print("Juego guardado. Saliendo...")
                    break

            juego.colocar_ficha(turno[0], columna)
            Juego.mostrar_tablero_columna(juego, columna)
            Juego.guardar_turno(archivo, 1 if turno == ficha_jugador1 else 2)
            Juego.guardar_tablero(juego._tablero, archivo)
            
            resultado = juego.hay_fin_juego(columna, turno[0])
            if resultado:
                if resultado == 'victoria':
                    Juego.marcar_victoria(juego, columna, turno[0])
                    print("FIN DE JUEGO")
                    print(f"{turno[1]} HA GANADO")
                elif resultado == 'empate':
                    print("FIN DE JUEGO")
                    print("No quedan casillas libres")
                Juego.eliminar_archivo(archivo)
                break

            turno = ficha_maquina if turno == ficha_jugador1 else ficha_jugador1
    
    @staticmethod
    def guardar_tablero(tablero, nombre_archivo):
        """Guarda el estado actual del tablero en un archivo de texto.
        Params:
            tablero (list): El tablero del juego.
            nombre_archivo (str): Nombre del archivo donde se guardará el tablero.
        """
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        # Ahora el encabezado son las primeras 5 líneas: jugador1, jugador2, turno, cantidad_victoria, dificultad
        encabezado = lineas[:5]
        encabezado = [linea if linea.endswith('\n') else linea + '\n' for linea in encabezado]

        with open(nombre_archivo, 'w') as fichero:
            fichero.writelines(encabezado)
            for fila in tablero:
                linea = ''.join(str(casilla) for casilla in fila)
                fichero.write(linea + '\n')

    # Función principal del juego
    @staticmethod
    def main():
        print("=== CONECTA N ===")
        
        while True:
            print("\nMenú:")
            print("1. Nuevo juego")
            print("2. Cargar juego")
            print("3. Salir")
            opcion = input("Seleccione una opción (1-3): ").strip()

            if opcion == "3":
                print("¡Gracias por jugar!")
                break

            archivo = None
            
            if opcion == "1":
                archivo = input("Introduzca el nombre de la partida: ").strip()
                if not archivo.endswith(".txt"):
                    archivo += ".txt"

                # Configuración del juego
                filas, columnas = Juego.solicitar_tamano_tablero()
                cantidad_victoria = Juego.solicitar_cantidad_victoria(filas, columnas)
                modo_juego, dificultad = Juego.solicitar_modo_juego()
                jugador1, jugador2 = Juego.solicitar_nombre_jugadores(modo_juego)
                
                # Guardar los jugadores con toda la configuración
                Juego.guardar_jugadores(archivo, jugador1, jugador2 if jugador2 else "BOT", 
                                       cantidad_victoria, dificultad if dificultad else 0)
                
                # Crear el juego
                try:
                    juego = ConectaN(filas, columnas, cantidad_victoria, modo_juego, jugador1, jugador2)
                    
                    # Iniciar el juego según el modo
                    if modo_juego == 1:
                        Juego.juego_solitario(juego, jugador1, dificultad, archivo)
                    else:
                        Juego.juego_dos_jugadores(juego, jugador1, jugador2, archivo)
                        
                except ValueError as e:
                    print(f"Error al crear el juego: {e}")

            elif opcion == "2":
                # Listar partidas guardadas
                archivos_txt = [item for item in os.listdir() if item.endswith(".txt")]
                
                if not archivos_txt:
                    print("No hay partidas guardadas.")
                    continue
                
                print("\n¿Qué partida desea retomar?")
                for i, item in enumerate(archivos_txt, 1):
                    print(f"{i}- {item}")

                try:
                    seleccion = input(f"Seleccione una de las partidas (1-{len(archivos_txt)}): ").strip()
                    indice = int(seleccion) - 1
                    
                    if 0 <= indice < len(archivos_txt):
                        archivo = archivos_txt[indice]
                    else:
                        print("Índice fuera de rango.")
                        continue
                except ValueError:
                    print("Entrada inválida.")
                    continue
                
                # Cargar la partida desde el archivo
                try:
                    print(f"\nCargando partida desde {archivo}...")
                    info_juego = Juego.cargar_juego(archivo)

                    jugador1 = info_juego[0].strip()
                    jugador2 = info_juego[1].strip()
                    turno = int(info_juego[2].strip())
                    cantidad_victoria = int(info_juego[3].strip())
                    dificultad = int(info_juego[4].strip())

                    # Cargar el tablero (ahora empieza en la línea 6, índice 5)
                    filas = len(info_juego) - 5
                    columnas = len(info_juego[5].strip())
                    
                    # Determinar modo de juego
                    modo_juego = 1 if jugador2.upper() == "BOT" else 2
                    
                    # Crear el juego con las dimensiones y configuración del tablero cargado
                    juego = ConectaN(filas, columnas, cantidad_victoria, modo_juego, jugador1, jugador2)
                    
                    # Cargar el estado del tablero
                    juego._tablero = [
                        [int(casilla) for casilla in info_juego[i + 5].strip()]
                        for i in range(filas)
                    ]
                    
                    print("Partida cargada exitosamente.")
                    print(juego)
                    
                    # Continuar el juego
                    if modo_juego == 1:
                        Juego.juego_solitario(juego, jugador1, dificultad, archivo)
                    else:
                        Juego.juego_dos_jugadores(juego, jugador1, jugador2, archivo)
                        
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                    continue
                except (IndexError, ValueError) as e:
                    print(f"Error al cargar la partida: El archivo puede estar corrupto. {e}")
                    continue
                
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
    
if __name__ == "__main__":
    Juego.main()
