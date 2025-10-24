import Validaciones

print("Venta de entradas CineCampa")

num_entradas = int(input("Número de entradas: "))

dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]
while True:
    dia_semana = input("Día de la semana: ").lower().strip()
    if dia_semana in dias_validos:
        break
    else:
        print("Error: Introduce un día de la semana válido.")

tiene_tarjeta = Validaciones.leer_caracter_multiple("¿Tiene tarjeta CineCampa? (s/n): ", "Introduce 's' o 'n':", ["s", "n"])

precio_base = 8.00
precio_miercoles = 5.00
precio_pareja_jueves = 11.00

if dia_semana == "miércoles" or dia_semana == "miercoles":
    total = num_entradas * precio_miercoles
elif dia_semana == "jueves":
    parejas = num_entradas // 2
    individuales = num_entradas % 2
    total = (parejas * precio_pareja_jueves) + (individuales * precio_base)
else:
    total = num_entradas * precio_base

descuento = 0
if tiene_tarjeta == "s":
    descuento = total * 0.10
    total_final = total - descuento
else:
    total_final = total

print("\nAquí tiene sus entradas. Gracias por su compra.")
print(f"{'Entradas individuales':<35}{num_entradas:>8}")
print(f"{'Precio por entrada individual':<35}{precio_base:>5.2f} €")
print(f"{'Total':<35}{total:>8.2f} €")

if descuento > 0:
    print(f"{'Descuento':<35}{descuento:>8.2f} €")
    print(f"{'A pagar':<35}{total_final:>8.2f} €")
else:
    print(f"{'A pagar':<35}{total_final:>8.2f} €")