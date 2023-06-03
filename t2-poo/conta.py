from historico import Historico


class Conta:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def transfere_para(self, outra_conta, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            outra_conta.deposito(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso para a conta {outra_conta.numero_conta}.")
        else:
            print("Saldo insuficiente para transferência.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        print(f"Saldo atual: R${self.saldo:.2f}")