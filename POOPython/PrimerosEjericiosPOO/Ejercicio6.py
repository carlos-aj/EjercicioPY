class CuentaSimple:
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        self.saldo -= cantidad
    
    def obtener_saldo(self):
        return self.saldo

cuenta1 = CuentaSimple()

cuenta1.depositar(100)
cuenta1.retirar(50)
print(cuenta1.obtener_saldo())