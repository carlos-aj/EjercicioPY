class Empleado:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def nombre_completo(self):
        return self.nombre + " " + self.apellidos
    
emp1 = Empleado('Alex', 'Cabrera')

print(emp1.nombre_completo())