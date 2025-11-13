import Validaciones

sabor = Validaciones.leer_caracter_multiple(
    mensaje="Elija un sabor (manzana, fresa o chocolate): ",
    error="Por favor, elija entre: manzana, fresa o chocolate",
    caracteres_validos=["manzana", "fresa", "chocolate"]
)

precio_base = 0

if sabor == "manzana":
    precio_base = 18.00
    print(f"Tarta de manzana: {precio_base:.2f} €")
elif sabor == "fresa":
    precio_base = 16.00
    print(f"Tarta de fresa: {precio_base:.2f} €")
elif sabor == "chocolate":
    tipo_chocolate = leer_caracter_multiple(
        mensaje="¿Qué tipo de chocolate quiere? (negro o blanco): ",
        error="Por favor, elija entre: negro o blanco",
        caracteres_validos=["negro", "blanco"]
    )
    
    if tipo_chocolate == "negro":
        precio_base = 14.00
        print(f"Tarta de chocolate negro: {precio_base:.2f} €")
    elif tipo_chocolate == "blanco":
        precio_base = 15.00
        print(f"Tarta de chocolate blanco: {precio_base:.2f} €")

nata = leer_caracter_multiple(
    mensaje="¿Quiere nata? (si o no): ",
    error="Por favor, responda con 'si' o 'no'",
    caracteres_validos=["si", "no"]
)

nombre = leer_caracter_multiple(
    mensaje="¿Quiere ponerle un nombre? (si o no): ",
    error="Por favor, responda con 'si' o 'no'",
    caracteres_validos=["si", "no"]
)

precio_total = precio_base

if nata == "si":
    precio_nata = 2.50
    precio_total += precio_nata
    print(f"Con nata: {precio_nata:.2f} €")

if nombre == "si":
    precio_nombre = 2.75
    precio_total += precio_nombre
    print(f"Con nombre: {precio_nombre:.2f} €")

print(f"Total: {precio_total:.2f} €")