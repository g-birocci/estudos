class MaquinaDinheiro:
    MOEDA = "R$"
    VALOR_MOEDAS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.lucro = 0
        self.dinheiro_recebido = 0

    def relatorio(self):
        print(f"Dinheiro: {self.MOEDA}{self.lucro}")

    def processar_moedas(self):
        print("Por favor, insira as moedas.")
        for moeda, valor in self.VALOR_MOEDAS.items():
            self.dinheiro_recebido += int(input(f"Quantas {moeda}? ")) * valor
        return self.dinheiro_recebido

    def realizar_pagamento(self, custo):
        self.processar_moedas()
        if self.dinheiro_recebido >= custo:
            troco = round(self.dinheiro_recebido - custo, 2)
            print(f"Aqui está seu troco: {self.MOEDA}{troco}.")
            self.lucro += custo
            self.dinheiro_recebido = 0
            return True
        else:
            print("Desculpe, dinheiro insuficiente. Dinheiro devolvido.")
            self.dinheiro_recebido = 0
            return False
