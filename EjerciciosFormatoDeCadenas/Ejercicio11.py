import Validaciones

base = Validaciones.leer_numero_entero_con_minimo("Introduzca la base imponible:", "La base no puede ser menor que 1:", 1)

tipoIVA = input("Introduzca el tipo de IVA (general, reducido o superreducido): ")

while tipoIVA not in ["general", "reducido", "superreducido"]:
    tipoIVA = input("Tipo de IVA incorrecto. Introduzca (general, reducido o superreducido): ")

codigo_promocional = input("Introduzca el código promocional (nopro, mitad, meno5 o 5porc): ")

while codigo_promocional not in ["nopro", "mitad", "meno5", "5porc"]:
    codigo_promocional = input("Código incorrecto. Introduzca (nopro, mitad, meno5 o 5porc): ")

if tipoIVA == "general":
    porcentaje_iva = 21
elif tipoIVA == "reducido":
    porcentaje_iva = 10
else:  
    porcentaje_iva = 4

iva = base * porcentaje_iva / 100
precio_con_iva = base + iva

if codigo_promocional == "nopro":
    descuento = 0
    precio_final = precio_con_iva
elif codigo_promocional == "mitad":
    descuento = precio_con_iva / 2
    precio_final = precio_con_iva - descuento
elif codigo_promocional == "meno5":
    descuento = 5
    precio_final = precio_con_iva - descuento
else:  # 5porc
    descuento = precio_con_iva * 0.05
    precio_final = precio_con_iva - descuento

print(f"{'Base imponible':<20} {base:>10.2f}")
print(f"{'IVA (' + str(porcentaje_iva) + '%)':<20} {iva:>10.2f}")
print(f"{'Precio con IVA':<20} {precio_con_iva:>10.2f}")
print(f"{'Cód. promo. (' + codigo_promocional + '):':<20} {-descuento:>10.2f}")
print(f"{'TOTAL':<20} {precio_final:>10.2f}")