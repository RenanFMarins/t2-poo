class Historico:
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, tipo, valor):
        self.transacoes.append({"Tipo": tipo, "Valor": valor})

    def imprimir_transacoes(self):
        print("Histórico:")
        for transacao in self.transacoes:
            tipo = transacao["Tipo"]
            valor = transacao["Valor"]
            print(f"{tipo}: R${valor:.2f}")
