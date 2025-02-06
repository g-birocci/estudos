import uuid
class Parceiro:
    def __init__(self, nome_empresa: str, contacto: str, email: str, especialidades: list, projetos_em_construcao: list):
       
        self.id = id if id else str(uuid.uuid4())
        self.nome_empresa = nome_empresa
        self.contacto = contacto
        self.email = email
        self.especialidades = especialidades
        self.projetos_em_construcao = projetos_em_construcao

    @classmethod
    def from_dict(cls, dados):
        id = dados.get('id')
        nome_empresa = dados.get('nome_empresa')
        contacto = dados.get('contacto')
        email = dados.get('email')
        especialidades = dados.get('especialidades')
        projetos_em_construcao = dados.get('projetos_em_construcao')

        return cls(id, nome_empresa, contacto, email, especialidades, projetos_em_construcao)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome_empresa': self.nome_empresa,
            'contacto': self.contacto,
            'email': self.email,
            'especialidades': self.especialidades,
            'projetos_em_construcao': self.projetos_em_construcao
        }