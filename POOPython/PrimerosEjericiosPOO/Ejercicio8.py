class CuentaBancaria:
    def __init__(self, num_cuenta, saldo = 0):
        self._saldo = saldo
        self._num_cuenta = num_cuenta

    @property
    def saldo(self):
        if self._saldo < 1:
            raise ValueError
        return self._saldo
    
    @property
    def num_cuenta(self):
        if self._saldo < 1:
            raise ValueError
        return self._num_cuenta
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @num_cuenta.setter
    def num_cuenta(self, num_cuenta):
        self._num_cuenta = num_cuenta

    def aplicar_agios(self):
        self._saldo -= self._saldo * 0.05

    def retirar_saldo(self, saldo_a_retirar) -> bool:
        if saldo_a_retirar > self._saldo:
            CuentaBancaria.aplicar_agios(self)
            return False
        else:
            self._saldo -= saldo_a_retirar
            return True

if __name__ == "__main__":
    cuenta1 = CuentaBancaria(1, 423)

    if cuenta1.retirar_saldo(5):
        print("Saldo retirado correctamente. Saldo actual: " , cuenta1.saldo)
    else:
        print("Saldo no retirado, aplicando agios. Saldo actual: " , cuenta1.saldo)

    
