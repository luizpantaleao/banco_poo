from banco import Banco
from pessoa import Cliente
from conta import ContaCorrente, ContaPoupanca

cliente1 = Cliente('Luiz', 20)
cliente2 = Cliente('Cleanto', 51)
cliente3 = Cliente('Gabriella', 22)

conta1 = ContaCorrente(1111, 12345)
conta2 = ContaPoupanca(2222, 23456)
conta3 = ContaCorrente(4444, 34567)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco = Banco()

banco.inserir_conta(conta1)
banco.inserir_conta(conta2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente1)
banco.inserir_cliente(cliente2)
banco.inserir_cliente(cliente3)

# CLIENTE 1

cliente1.conta.depositar(100)
if banco.autenticar(cliente1):
    cliente1.conta.sacar(100)
else:
    print('Falha na autenticação')

# CLIENTE 2

cliente2.conta.depositar(100)
if banco.autenticar(cliente2):
    cliente2.conta.sacar(100)
else:
    print('Falha na autenticação')

# CLIENTE 3

cliente3.conta.depositar(100)
if banco.autenticar(cliente3):
    cliente3.conta.sacar(100)
else:
    print('Falha na autenticação')
