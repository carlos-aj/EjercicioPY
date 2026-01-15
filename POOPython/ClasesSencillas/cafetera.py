class Cafetera:
    #Constructor básico
    def __init__(self, capacidad_maxima: int = 1000, cantidad_actual: int = 0):
        if not Cafetera._comprobar_positivo(capacidad_maxima):
            raise ValueError("La capacidad maxima debe de ser mayor a 0")
        if not Cafetera._comprobar_no_negativo(cantidad_actual):
            raise ValueError("La cantidad actual debe ser mayor o igual a 0")
        self._capacidad_maxima = capacidad_maxima
        self._cantidad_actual = cantidad_actual

    #Constrctor que crea una cafetera llena
    @classmethod
    def cafetera_llena(cls, capacidad_maxima):
        return cls(capacidad_maxima, capacidad_maxima)
    
    #Constructor que crea una cafetera con valores personalizados
    @classmethod
    def cafetera_custom(cls, capacidad_maxima, cantidad_actual):
        if cantidad_actual > capacidad_maxima:
            cantidad_actual = capacidad_maxima

        return cls(capacidad_maxima, cantidad_actual)
    
    #Getters y Setters
    #Getter capacidad_maxima
    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima
    
    #Getter cantidad_actual
    @property
    def cantidad_actual(self):
        return self._cantidad_actual
    
    #Setter capacidad_maxima
    @capacidad_maxima.setter
    def capacidad_maxima(self, capacidad_maxima):
        if not Cafetera._comprobar_positivo(capacidad_maxima):
            raise ValueError("La capacidad no puede ser menor a 0")
        self._capacidad_maxima = capacidad_maxima

    #Setter cantidad_actual
    @cantidad_actual.setter
    def cantidad_actual(self, cantidad_actual):
        if not Cafetera._comprobar_no_negativo(cantidad_actual):
            raise ValueError("La cantidad actual no puede ser menor a 0")
        self._cantidad_actual = cantidad_actual

    #Metodo estatico de comprobacion > 0
    @staticmethod
    def _comprobar_positivo(numero):
        return numero > 0
        
    #Metodo estatico de comprobacion >= 0
    @staticmethod
    def _comprobar_no_negativo(numero):
        return numero >= 0

    #Metodos principales
    #Metodo llenar cafetera
    def llenar_cafetera(self):
        self._cantidad_actual = self._capacidad_maxima

    #Metodo servir taza, devuelve la cantidad servida, si no hay suficiente devuelve lo que queda
    def servir_taza(self, cantidad: int):
        if self._cantidad_actual < cantidad:
            servido = self._cantidad_actual
            self._cantidad_actual = 0
            return servido
        
        self._cantidad_actual -= cantidad
        return cantidad
    
    #Metodo vaciar cafetera
    def vaciar_cafetera(self):
        self._cantidad_actual = 0

    #Metodo agregar cafe
    def agregar_cafe(self, cantidad: int):
        self._cantidad_actual += cantidad

    #Representacion en cadena
    def __str__(self):
        return f"{self._capacidad_maxima} | {self._cantidad_actual}"

class MainCafetera:
    def main():
        print("=== PRUEBAS DE LA CLASE CAFETERA ===\n")
        
        # 1. PRUEBAS DE CONSTRUCTORES
        print("1. PRUEBAS DE CONSTRUCTORES")
        print("-" * 30)
        
        # Constructor básico
        cafetera_basica = Cafetera()
        print(f"Cafetera básica: {cafetera_basica}")
        print(f"Capacidad máxima: {cafetera_basica.capacidad_maxima}")
        print(f"Cantidad actual: {cafetera_basica.cantidad_actual}")
        
        # Constructor cafetera_llena
        cafetera_llena = Cafetera.cafetera_llena(800)
        print(f"Cafetera llena: {cafetera_llena}")
        
        # Constructor cafetera_custom
        cafetera_custom = Cafetera.cafetera_custom(1500, 2000)  # Se ajustará a 1500
        print(f"Cafetera custom (ajustada): {cafetera_custom}")
        
        cafetera_custom2 = Cafetera.cafetera_custom(1000, 500)
        print(f"Cafetera custom (normal): {cafetera_custom2}")
        
        print("\n2. PRUEBAS DE MÉTODOS PRINCIPALES")
        print("-" * 35)
        
        # Crear cafetera para pruebas
        cafetera = Cafetera(1000, 300)
        print(f"Cafetera inicial: {cafetera}")
        
        # Llenar cafetera
        print("\nPrueba llenar_cafetera():")
        cafetera.llenar_cafetera()
        print(f"Después de llenar: {cafetera}")
        
        # Servir tazas
        print("\nPruebas servir_taza():")
        servido = cafetera.servir_taza(200)
        print(f"Servir 200ml - Servido: {servido}ml - Estado: {cafetera}")
        
        servido = cafetera.servir_taza(900)  # Más de lo disponible
        print(f"Servir 900ml (excede) - Servido: {servido}ml - Estado: {cafetera}")
        
        # Agregar café
        print("\nPrueba agregar_cafe():")
        cafetera.agregar_cafe(400)
        print(f"Agregar 400ml: {cafetera}")
        
        # Vaciar cafetera
        print("\nPrueba vaciar_cafetera():")
        cafetera.vaciar_cafetera()
        print(f"Después de vaciar: {cafetera}")
        
        print("\n3. PRUEBAS DE PROPIEDADES (SETTERS)")
        print("-" * 38)
        
        # Cambiar capacidad máxima
        print("Prueba setter capacidad_maxima:")
        cafetera.capacidad_maxima = 1200
        print(f"Nueva capacidad máxima: {cafetera}")
        
        # Cambiar cantidad actual
        print("Prueba setter cantidad_actual:")
        cafetera.cantidad_actual = 600
        print(f"Nueva cantidad actual: {cafetera}")
        
        print("\n4. PRUEBAS DE VALIDACIONES (ERRORES)")
        print("-" * 38)
        
        try:
            # Constructor con capacidad negativa
            cafetera_error = Cafetera(-100, 50)
        except ValueError as e:
            print(f"Error capacidad negativa: {e}")
        
        try:
            # Constructor con cantidad negativa
            cafetera_error = Cafetera(1000, -50)
        except ValueError as e:
            print(f"Error cantidad negativa: {e}")
        
        try:
            # Setter capacidad negativa
            cafetera.capacidad_maxima = -200
        except ValueError as e:
            print(f"Error setter capacidad negativa: {e}")
        
        try:
            # Setter cantidad negativa
            cafetera.cantidad_actual = -100
        except ValueError as e:
            print(f"Error setter cantidad negativa: {e}")
        
        print("\n5. PRUEBAS DE CASOS LÍMITE")
        print("-" * 30)
        
        # Cafetera con capacidad mínima
        cafetera_min = Cafetera(1, 0)
        print(f"Cafetera mínima: {cafetera_min}")
        cafetera_min.llenar_cafetera()
        print(f"Mínima llena: {cafetera_min}")
        servido = cafetera_min.servir_taza(1)
        print(f"Servir todo (1ml): servido={servido}, estado={cafetera_min}")
        
        # Servir cuando está vacía
        print("Servir de cafetera vacía:")
        servido = cafetera_min.servir_taza(100)
        print(f"Servido de vacía: {servido}ml")

if __name__ == "__main__":
    MainCafetera.main()
