import uuid #Gera numero de id aleatorio e verefica pra não repetir
class Lead:

    def __init__(self, cliente_id , especialidade, parceiros, descricao, estado):
        self.id = str(uuid.uuid4())
        self.cliente_id = cliente_id
        self.especialidade = especialidade
        self.parceiros = parceiros
        self.descricao = descricao
        self.estado = estado

    @classmethod
    def from_dict(cls, dados):
        id = dados.get('id')
        cliente_id = dados.get('cliente_id')
        especialidade = dados.get('especialidade')
        parceiros = dados.get('parceiros')
        descricao = dados.get('descricao')
        estado = dados.get('estado')

        return cls(id, cliente_id, especialidade, parceiros, descricao, estado)
    
    def to_dict(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'especialidade': self.especialidade,
            'parceiros': self.parceiros,
            'descricao': self.descricao,
            'estado': self.estado
        }

    def __repr__(self):
        return f"lideres(id = {self.id}, cliente_id = {self.cliente_id}, especialidade = {self.especialidade}, parceiro = {self.parceiros}, descricao = {self.descricao}, estado = {self.estado})"
    