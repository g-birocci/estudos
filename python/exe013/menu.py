class ItemMenu:
    def __init__(self, nome, custo, ingredientes):
        self.nome = nome
        self.custo = custo
        self.ingredientes = ingredientes

class Menu:
    def __init__(self):
        self.menu = [
            ItemMenu("Latte", 2.5, {"água": 200, "leite": 150, "café": 24}),
            ItemMenu("Espresso", 1.5, {"água": 50, "leite": 0, "café": 18}),
            ItemMenu("Cappuccino", 3.0, {"água": 250, "leite": 50, "café": 24})
        ]
    
    def obter_itens(self):
        return ", ".join([item.nome for item in self.menu])
    
    def encontrar_bebida(self, nome):
        for item in self.menu:
            if item.nome.lower() == nome.lower():
                return item
        return None
