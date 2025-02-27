class Cafeteira:
    def __init__(self):
        self.recursos = {"água": 300, "leite": 200, "café": 100}
    
    def relatorio(self):
        print(f"Água: {self.recursos['água']}ml")
        print(f"Leite: {self.recursos['leite']}ml")
        print(f"Café: {self.recursos['café']}g")
    
    def tem_recurso_suficiente(self, bebida):
        for ingrediente, quantidade in bebida.ingredientes.items():
            if self.recursos[ingrediente] < quantidade:
                print(f"Desculpe, não há {ingrediente} suficiente.")
                return False
        return True
    
    def fazer_cafe(self, pedido):
        for ingrediente, quantidade in pedido.ingredientes.items():
            self.recursos[ingrediente] -= quantidade
        print(f"Aqui está o seu {pedido.nome} Aproveite!")
