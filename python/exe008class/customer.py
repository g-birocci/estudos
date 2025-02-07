import uuid  # Importa a biblioteca uuid para gerar IDs únicos

class Cliente:
    def __init__(self, nome=str, telefone=str, email=str, morada=str):
        # Gera um ID único para o cliente usando uuid e limita a 6 caracteres
        self.id = str(uuid.uuid4())[:6]
        self.nome = nome  # Nome do cliente
        self.telefone = telefone  # Telefone do cliente
        self.email = email  # Email do cliente
        self.morada = morada  # Endereço do cliente

    @classmethod
    def from_dict(cls, dados):
        # Método de classe para criar um objeto Cliente a partir de um dicionário
        id = dados.get('id')  # Obtém o ID do dicionário
        nome = dados.get('nome')  # Obtém o nome do dicionário
        telefone = dados.get('telefone')  # Obtém o telefone do dicionário
        email = dados.get('email')  # Obtém o email do dicionário
        morada = dados.get('morada')  # Obtém o endereço do dicionário

        # Cria um objeto Cliente com os dados obtidos
        cliente = cls(nome, telefone, email, morada)
        cliente.id = id  # Define o ID do cliente
        return cliente

    def to_dict(self):
        # Converte o objeto Cliente em um dicionário
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'morada': self.morada
        }

    def __repr__(self):
        # Representação textual do objeto Cliente (usada para exibição)
        return f"Cliente(id={self.id}, nome={self.nome}, telefone={self.telefone}, email={self.email}, morada={self.morada})"