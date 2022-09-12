class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.contas = []
        self.clientes = []

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente.nome)

    def autenticar(self, cliente):
        if cliente.nome not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True
