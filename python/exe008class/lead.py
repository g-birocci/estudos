import uuid  # Importa a biblioteca uuid para gerar IDs únicos

class Lead:
    def __init__(self, cliente_id, especialidade, parceiros, descricao, estado):
        # Gera um ID único para o lead usando uuid
        self.id = str(uuid.uuid4())
        self.cliente_id = cliente_id  # ID do cliente associado ao lead
        self.especialidade = especialidade  # Especialidade do lead (ex.: "canalização")
        self.parceiros = parceiros  # Lista de parceiros associados ao lead
        self.descricao = descricao  # Descrição do lead
        self.estado = estado  # Estado do lead (ex.: "não contactado")

    @classmethod
    def from_dict(cls, dados):
        # Método de classe para criar um objeto Lead a partir de um dicionário
        id = dados.get('id')  # Obtém o ID do dicionário
        cliente_id = dados.get('cliente_id')  # Obtém o ID do cliente
        especialidade = dados.get('especialidade')  # Obtém a especialidade
        parceiros = dados.get('parceiros')  # Obtém a lista de parceiros
        descricao = dados.get('descricao')  # Obtém a descrição
        estado = dados.get('estado')  # Obtém o estado

        # Cria um objeto Lead com os dados obtidos
        lead = cls(cliente_id, especialidade, parceiros, descricao, estado)
        lead.id = id  # Define o ID do lead (usando o ID carregado do JSON)
        return lead

    def to_dict(self):
        # Converte o objeto Lead em um dicionário
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'especialidade': self.especialidade,
            'parceiros': self.parceiros,
            'descricao': self.descricao,
            'estado': self.estado
        }

    def __repr__(self):
        # Representação textual do objeto Lead (usada para exibição)
        return f"Lead(id={self.id}, cliente_id={self.cliente_id}, especialidade={self.especialidade}, parceiros={self.parceiros}, descricao={self.descricao}, estado={self.estado})"