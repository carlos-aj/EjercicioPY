import Validaciones

altura = int(Validaciones.leer_numero_entero_con_minimo("Introduzca la altura de la bandera en cm:", "La altura no puede ser 0 o menor:", 1))
anchura = int(Validaciones.leer_numero_entero_con_minimo("Introduzca la anchura de la bandera en cm:", "La anchura no puede ser 0 o menor:", 1))

bordado = Validaciones.leer_caracter_multiple("¿Quiere escudo bordado? (s/n)", "Respuesta no válida. ¿Quiere escudo bordado? (s/n)", ["s", "n"])

print("Gracias. Aqui tiene su desglose de su compra:")
print(f"{'Bandera de ' + str(altura*anchura) + ' cm2:':<25}{altura*anchura*0.01:>6.2f} €")
if bordado == "s":
    print(f"{'Con escudo:':<25}{2.50:>6.2f} €")
else:
    print(f"{'Sin escudo:':<25}{0.00:>6.2f} €")

print(f"{'Gastos de envío:':<25}{3.25:>6.2f} €")
total = (altura*anchura*0.01) + (2.50 if bordado == "s" else 0) + 3.25
print(f"{'Total:':<25}{total:>6.2f} €")