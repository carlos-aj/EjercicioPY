import random

def mostrar_mesas(mesas):
    """Muestra el estado actual de las mesas"""
    print("\n" + "─" * 77)
    print("│ Mesa nº  │", end="")
    for i in range(1, len(mesas) + 1):
        print(f" {i:2} │", end="")
    print()
    print("├─────────┼" + "────┼" * len(mesas))
    print("│Ocupación │", end="")
    for ocupacion in mesas:
        print(f" {ocupacion:2} │", end="")
    print()
    print("─" * 77)

def inicializar_mesas(num_mesas=10):
    """Inicializa las mesas con valores aleatorios entre 0 y 4"""
    return [random.randint(0, 4) for _ in range(num_mesas)]

def buscar_mesa_libre(mesas):
    """Busca la primera mesa completamente libre (0 personas)"""
    for i, ocupacion in enumerate(mesas):
        if ocupacion == 0:
            return i
    return -1

def buscar_mesa_con_hueco(mesas, grupo):
    """Busca la primera mesa donde quepa el grupo"""
    for i, ocupacion in enumerate(mesas):
        if ocupacion + grupo <= 4:
            return i
    return -1

mesas = inicializar_mesas(10)

print("¡Bienvenido al sistema de gestión de mesas del restaurante!")
mostrar_mesas(mesas)

while True:
    try:
        grupo = int(input("\n¿Cuántos son? (Introduzca -1 para salir del programa): "))
        
        if grupo == -1:
            print("¡Gracias por usar nuestro sistema!")
            break
        
        if grupo > 4:
            print(f"Lo siento, no admitimos grupos de {grupo}, haga grupos de 4 personas como máximo e intente de nuevo")
            continue
        
        if grupo <= 0:
            print("El número de personas debe ser mayor que 0")
            continue
        
        mesa_libre = buscar_mesa_libre(mesas)
        
        if mesa_libre != -1:
            mesas[mesa_libre] = grupo
            print(f"Por favor, siéntense en la mesa número {mesa_libre + 1}.")
        else:
            mesa_con_hueco = buscar_mesa_con_hueco(mesas, grupo)
            
            if mesa_con_hueco != -1:
                mesas[mesa_con_hueco] += grupo
                print(f"Por favor, siéntense en la mesa número {mesa_con_hueco + 1}.")
            else:
                print("Lo siento, en estos momentos no tenemos sitio.")
                continue
        
        mostrar_mesas(mesas)
        
    except ValueError:
        print("Por favor, introduzca un número válido.")
    except KeyboardInterrupt:
        print("\n¡Gracias por usar nuestro sistema!")
        break