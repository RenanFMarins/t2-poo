from banco import Banco
from conta import Conta


class Cliente:
    def __init__(self, nome, numero_conta):
        self.nome = nome
        self.numero_conta = numero_conta

    def exibir_cliente(self):
        print("Cliente:", self.nome)
        print("Número da Conta:", self.numero_conta)


