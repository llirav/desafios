class ContaBancaria:
    def __init__(self, numero, saldo, titular):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular

    def sacar(self, saque):
        self.saldo -= saque
        return saque
    
    def depositar(self, deposito):
        self.saldo += deposito
        return deposito
    
    def saldo(self, saldoFinal):
        self.saldo = saldoFinal
        return saldoFinal
    
if __name__ == "__main__":
    conta1 = ContaBancaria(896574, 4000, "João")
    saque = int(input("Digite o valor que deseja sacar: "))
    deposito = int(input("Digite o valor que deseja depositar: "))
    saldoFinal = conta1.saldo - conta1.sacar(saque) + conta1.depositar(deposito)

    print(f"O valor do saque foi R${conta1.sacar(saque)}")
    print(f"O valor do depósito foi R${conta1.depositar(deposito)}")
    print(f"Sua conta ficou com R${saldoFinal}")