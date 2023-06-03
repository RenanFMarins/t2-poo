from conta import Conta
from banco import Banco
from cliente import Cliente
from historico import Historico



banco = Banco("Meu Banco")


conta1 = Conta("123", "001")
conta2 = Conta("456", "001")
conta3 = Conta("789", "002")


banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)


banco.listar_contas_por_agencia("001")

cliente1 = Cliente("João", banco)
cliente1.exibir_cliente()


historico = Historico()


historico.registrar_transacao("Transferência", 500)


historico.imprimir_transacoes()