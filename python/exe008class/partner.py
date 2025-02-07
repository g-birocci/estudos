import uuid  # Importa a biblioteca uuid para gerar IDs únicos

class Parceiro:
    def __init__(self, nome_empresa: str, contacto: str, email: str, especialidades: list, projetos_em_construcao: list, id=None):
        # Gera um ID único para o parceiro, a menos que um ID seja fornecido
        self.id = id if id else str(uuid.uuid4())
        self.nome_empresa = nome_empresa  # Nome da empresa parceira
        self.contacto = contacto  # Contato da empresa
        self.email = email  # Email da empresa
        self.especialidades = especialidades  # Lista de especialidades da empresa
        self.projetos_em_construcao = projetos_em_construcao  # Lista de projetos em construção

    @classmethod
    def from_dict(cls, dados):
        # Método de classe para criar um objeto Parceiro a partir de um dicionário
        id = dados.get('id')  # Obtém o ID do dicionário
        nome_empresa = dados.get('nome_empresa')  # Obtém o nome da empresa
        contacto = dados.get('contacto')  # Obtém o contato
        email = dados.get('email')  # Obtém o email
        especialidades = dados.get('especialidades')  # Obtém a lista de especialidades
        projetos_em_construcao = dados.get('projetos_em_construcao')  # Obtém a lista de projetos

        # Cria um objeto Parceiro com os dados obtidos
        return cls(nome_empresa, contacto, email, especialidades, projetos_em_construcao, id)

    def to_dict(self):
        # Converte o objeto Parceiro em um dicionário
        return {
            'id': self.id,
            'nome_empresa': self.nome_empresa,
            'contacto': self.contacto,
            'email': self.email,
            'especialidades': self.especialidades,
            'projetos_em_construcao': self.projetos_em_construcao
        }