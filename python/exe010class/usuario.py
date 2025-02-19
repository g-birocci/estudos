import json
class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        return f"Nome: {self.nome}\nEmail: {self.email}"
    
    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email
        }
