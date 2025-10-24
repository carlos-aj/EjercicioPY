print("1 - Programador junior")
print("2 - Programador senior")
print("3 - Jefe de proyecto")

cargo = int(input("Introduce el cargo del empleado (1-3): "))
dias_viaje = int(input("¿Cuántos días ha estado de viaje visitando clientes? "))

print("\nEstado civil:")
print("1 - Soltero")
print("2 - Casado")
estado_civil = int(input("Introduce su estado civil (1-2): "))

sueldos_base = {1: 950, 2: 1200, 3: 1600}
nombres_cargo = {1: "Programador junior", 2: "Prog. senior", 3: "Jefe de proyecto"}

sueldo_base = sueldos_base[cargo]

dietas = dias_viaje * 30

sueldo_bruto = sueldo_base + dietas

if estado_civil == 1:
    porcentaje_irpf = 25
else:  
    porcentaje_irpf = 20

retencion_irpf = sueldo_bruto * (porcentaje_irpf / 100)

sueldo_neto = sueldo_bruto - retencion_irpf

print("-"*33)
print(f"| {'Sueldo base':<20} {sueldo_base:8.2f} |")
print(f"| {'Dietas (' + str(dias_viaje) + ' viajes)':<20} {dietas:8.2f} |")
print("|" + "-"*31 + "|")
print(f"| {'Sueldo bruto':<20} {sueldo_bruto:8.2f} |")
print(f"| {'Retención IRPF (' + str(porcentaje_irpf) + '%)':<20} {retencion_irpf:8.2f} |")
print("|" + "-"*31 + "|")
print(f"| {'Sueldo neto':<20} {sueldo_neto:8.2f} |")
print("-"*33)