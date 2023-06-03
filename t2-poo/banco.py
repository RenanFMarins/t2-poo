from conta import Conta


class Banco:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.agencias = {}

    def adicionar_conta(self, conta):
        if conta.agencia not in self.agencias:
            self.agencias[conta.agencia] = []
        self.agencias[conta.agencia].append(conta)

    def listar_contas_por_agencia(self, agencia):
        if agencia in self.agencias:
            print(f"Contas da Agência {agencia}:")
            for conta in self.agencias[agencia]:
                print("Número da Conta:", conta.numero_conta)
                print("Saldo:", conta.saldo)
                
        else:
            print(f"A Agência {agencia} não possui contas.")