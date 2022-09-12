from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f'AGÊNCIA: {self.agencia}')
        print(f'CONTA: {self.conta}')
        print(f'SALDO: {self.saldo}')
        print(20*'-')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, limite=100):
        super().__init__(agencia, conta, saldo=0)
        self.limite = limite

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            self.detalhes()
        else:
            print('Limite insuficiente')


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta, saldo=0)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.detalhes()
        else:
            print('Saldo insuficiente')
