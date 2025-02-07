import uuid #Gera numero de id aleatorio e verefica pra não repetir

class Cliente:
    def __init__(self, nome = str, telefone = str, email = str, morada = str):
        self.id = str(uuid.uuid4())[:6]
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.morada = morada

    @classmethod 
    def from_dict(cls, dados):
        id = dados.get('id')
        nome = dados.get('nome')
        telefone = dados.get('telefone')
        email = dados.get('email')
        morada = dados.get('morada')

        cliente = cls(id, nome, telefone, email, morada) #O id não é o primeiro parametro que ele espera, por isso eu deixei ele por ultimo(Evitar possivel erro)
        cliente.id = id
        return cliente
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'morada': self.morada
        }
    
    def __repr__(self):
        return f"Cliente(id = {self.id}, nome = {self.nome}, telefone = {self.telefone}, email = {self.email}, morada = {self.morada})"

