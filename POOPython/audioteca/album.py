from cancion import Cancion
import copy

class Album:
    # Constructor normal
    def __init__(self, canciones, contador):
        self._canciones = canciones
        self._contador = contador

    # Constructor valores por defecto
    @classmethod
    def album_default(cls, canciones = None, contador = 0):
        if canciones is None:
            canciones = []
        return cls(canciones, contador)
    
    # Constructor copia
    @classmethod
    def album_copia(cls, copia_album):
        return copy.copy(copia_album)
    
    # Getters y Setters
    # Getter canciones
    @property
    def canciones(self):
        return self._canciones
    
    # Getter contador
    @property
    def contador(self):
        return self._contador
    
    # Setter canciones
    @canciones.setter
    def canciones(self, canciones):
        self._canciones = canciones

    # Setter contador
    @contador.setter
    def contador(self, contador):
        self._contador = contador

    # Metodos principales
    # Obtener numero de canciones
    def get_numero_canciones(self):
        return len(self.canciones)
    
    # Obtener canción por su número
    def dame_cancion(self, numero_cancion):
        if not self.canciones or numero_cancion < 0 or numero_cancion >= len(self.canciones):
            raise ValueError("Canción no existente")
        
        return self.canciones[numero_cancion]
    
    # Añadir canción
    def agrega(self, cancion):
        if not isinstance(cancion, Cancion):
            raise ValueError("Solo se pueden agregar objetos de tipo Cancion")
        
        if self._canciones is None:
            self._canciones = []
        
        self._canciones.append(cancion)
        return True
    
    # Eliminar canción
    def elimina(self, numero_cancion):
        if not self.canciones or numero_cancion < 0 or numero_cancion >= len(self.canciones):
            raise ValueError("Canción no existente")
        
        del self.canciones[numero_cancion]
        return True

    # Grabar canción
    def graba_cancion(self, numero_cancion, cancion):
        if not isinstance(cancion, Cancion):
            raise ValueError("Solo se pueden grabar objetos de tipo Cancion")
        
        if not self.canciones or numero_cancion < 0 or numero_cancion >= len(self.canciones):
            raise ValueError("Canción no existente")
        
        self.canciones[numero_cancion] = cancion
        return True
    
    # Representacion en cadena
    def __str__(self):
        return f"Album con {self.get_numero_canciones()} canciones, contador: {self._contador}"
    
class MainAudioteca:
    def main():
        print("=== PRUEBAS DE LA CLASE ALBUM ===\n")
        
        # Crear canciones para las pruebas
        cancion1 = Cancion("Bohemian Rhapsody", "Queen")
        cancion2 = Cancion("Imagine", "John Lennon")
        cancion3 = Cancion("Hotel California", "Eagles")
        
        # 1. Constructores
        print("1. CONSTRUCTORES")
        print("-" * 15)
        album1 = Album([cancion1, cancion2], 2)
        album2 = Album.album_default([cancion3], 1)
        album_copia = Album.album_copia(album1)
        
        print(f"Album 1: {album1}")
        print(f"Album 2: {album2}")
        print(f"Album copia: {album_copia}")
        
        # 2. Propiedades
        print("\n2. PROPIEDADES")
        print("-" * 15)
        print(f"Canciones de album1: {album1.get_numero_canciones()}")
        print(f"Contador de album1: {album1.contador}")
        print(f"Primera canción: {album1.dame_cancion(0)}")
        
        # 3. Setters
        print("\n3. SETTERS")
        print("-" * 10)
        album1.contador = 5
        print(f"Album1 después de cambiar contador: {album1}")
        
        # 4. Métodos principales
        print("\n4. MÉTODOS PRINCIPALES")
        print("-" * 20)
        album_test = Album.album_default()
        print(f"Album vacío: {album_test}")
        
        # Agregar canción
        resultado = album_test.agrega(cancion1)
        print(f"Agregar canción - Éxito: {resultado} - {album_test}")
        
        # Grabar canción
        resultado = album_test.graba_cancion(0, cancion2)
        print(f"Grabar canción - Éxito: {resultado} - Primera canción: {album_test.dame_cancion(0)}")
        
        # Eliminar canción
        resultado = album_test.elimina(0)
        print(f"Eliminar canción - Éxito: {resultado} - {album_test}")
        
        # 5. Prueba de errores
        print("\n5. PRUEBA DE ERRORES")
        print("-" * 19)
        try:
            album_test.agrega("No es una canción")
        except ValueError as e:
            print(f"Error al agregar string capturado correctamente: {e}")
        
        try:
            album_vacio = Album.album_default()
            album_vacio.dame_cancion(0)
        except ValueError as e:
            print(f"Error en álbum vacío capturado correctamente: {e}")
    
if __name__ == "__main__":
    MainAudioteca.main()