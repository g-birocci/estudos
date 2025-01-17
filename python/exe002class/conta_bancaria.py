class Conta_banco():
    def __init__(self, nome, n_conta, saldo):
        self.lista_de_contas = []
        self.lista_de_historico = []
        self.nome = nome
        self.n_conta = n_conta
        self.saldo = saldo
        pass

    def criar_conta(self, obj_conta ):
        self.lista_de_contas.append(obj_conta)

    def depositar(self,conta, valor_deposito):
        self.conta = conta
        self.valor_deposito = valor_deposito


    def saque(self, conta_digitada):
        for conta in self.lista_de_contas:
            if conta_digitada == conta:

    def consultar_saldo():
        pass