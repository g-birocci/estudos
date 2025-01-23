class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.0
        self.__historico_transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__registrar_transacao("Depósito", valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__registrar_transacao("Saque", valor)
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        return self.__saldo

    def exibir_historico(self):
        print("Histórico de Transações:")
        for transacao in self.__historico_transacoes:
            print(transacao)

    def __registrar_transacao(self, tipo, valor):
        self.__historico_transacoes.append(f"{tipo}: R${valor:.2f}")
