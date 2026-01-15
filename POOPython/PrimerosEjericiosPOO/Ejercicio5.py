class Contador:
    def __init__(self, conteo = 0):
        self.conteo = conteo

    def incrementar(self):
         self.conteo += 1
    
    def decrementar(self):
        self.conteo -= 1
    
    def obtener_valor(self):
        return self.conteo
    
num = Contador()

num.incrementar()
num.incrementar()
num.incrementar()
num.incrementar()
num.incrementar()
num.incrementar()
num.incrementar()
num.incrementar()

num.decrementar()
num.decrementar()
num.decrementar()

print(num.obtener_valor())