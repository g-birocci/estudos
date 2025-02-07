import json
import os
import uuid
from customer import Cliente
from lead import Lead
from partner import Parceiro

class NegocioConstrucao:
    def __init__(self):
        self.clientes = []
        self.leads = []
        self.parceiros = []
        
    def adicionar_cliente(self, cliente):
        if any(c.id == cliente.id for c in self.clientes):
            raise ValueError("ID de cliente já existe.")
        self.clientes.append(cliente)

    def adicionar_lead(self, lead):
        if any(l.id == lead.id for l in self.leads):
            raise ValueError("ID de lead já existe.")
        self.leads.append(lead)

    def adicionar_parceiro(self, parceiro):
        if any(p.id == parceiro.id for p in self.parceiros):
            raise ValueError("ID de parceiro já existe.")
        self.parceiros.append(parceiro)

    def guardar_em_json(self, ficheiro):
        data = {
            "clientes": [cliente.to_dict() for cliente in self.clientes],
            "leads": [lead.to_dict() for lead in self.leads],
            "parceiros": [parceiro.to_dict() for parceiro in self.parceiros]
        }
        with open(ficheiro, 'w') as f:
            json.dump(data, f, indent=4)

    def carregar_de_json(self, ficheiro):
        if not os.path.exists(ficheiro):
            raise FileNotFoundError("Ficheiro não encontrado.")

        with open(ficheiro, 'r') as f:
            data = json.load(f)

        self.clientes = [Cliente.from_dict(cliente) for cliente in data["clientes"]]
        self.leads = [Lead.from_dict(lead) for lead in data["leads"]]
        self.parceiros = [Parceiro.from_dict(parceiro) for parceiro in data["parceiros"]]

    def procurar_cliente_por_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def listar_leads_por_estado(self, estado):
        return [lead for lead in self.leads if lead.estado == estado]

    def listar_parceiros_por_especialidade(self, especialidade):
        return [parceiro for parceiro in self.parceiros if especialidade in parceiro.especialidades]
