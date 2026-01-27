listado_csv = []

with open("datos.csv", "r") as f:
    for linea in f:
        datos = linea.split(",")
        
        if len(datos) == 3:
            registro = {
                "nombre": datos[0],
                "cantidad": int(datos[1]),
                "precio": float(datos[2])
            }
            
            listado_csv.append(registro)

print(listado_csv)
