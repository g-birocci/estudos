import json  # Importa a biblioteca json para manipulação de arquivos JSON
import os  # Importa a biblioteca os para verificar a existência de arquivos
import uuid  # Importa a biblioteca uuid para gerar IDs únicos
from customer import Cliente  # Importa a classe Cliente
from lead import Lead  # Importa a classe Lead
from partner import Parceiro  # Importa a classe Parceiro

class NegocioConstrucao:
    def __init__(self):
        # Inicializa listas vazias para clientes, leads e parceiros
        self.clientes = []
        self.leads = []
        self.parceiros = []

    def adicionar_cliente(self, cliente):
        # Adiciona um cliente à lista, verificando se o ID já existe
        if any(c.id == cliente.id for c in self.clientes):
            raise ValueError("ID de cliente já existe.")
        self.clientes.append(cliente)

    def adicionar_lead(self, lead):
        # Adiciona um lead à lista, verificando se o ID já existe
        if any(l.id == lead.id for l in self.leads):
            raise ValueError("ID de lead já existe.")
        self.leads.append(lead)

    def adicionar_parceiro(self, parceiro):
        # Adiciona um parceiro à lista, verificando se o ID já existe
        if any(p.id == parceiro.id for p in self.parceiros):
            raise ValueError("ID de parceiro já existe.")
        self.parceiros.append(parceiro)

    def guardar_em_json(self, ficheiro):
        # Salva os dados das listas em um arquivo JSON
        data = {
            "clientes": [cliente.to_dict() for cliente in self.clientes],
            "leads": [lead.to_dict() for lead in self.leads],
            "parceiros": [parceiro.to_dict() for parceiro in self.parceiros]
        }
        with open(ficheiro, 'w') as f:
            json.dump(data, f, indent=4)  # Escreve os dados no arquivo JSON

    def carregar_de_json(self, ficheiro):
        # Carrega os dados de um arquivo JSON para as listas
        if not os.path.exists(ficheiro):
            raise FileNotFoundError("Ficheiro não encontrado.")

        with open(ficheiro, 'r') as f:
            data = json.load(f)  # Carrega os dados do arquivo JSON

        # Converte os dicionários em objetos Cliente, Lead e Parceiro
        self.clientes = [Cliente.from_dict(cliente) for cliente in data["clientes"]]
        self.leads = [Lead.from_dict(lead) for lead in data["leads"]]
        self.parceiros = [Parceiro.from_dict(parceiro) for parceiro in data["parceiros"]]

    def procurar_cliente_por_id(self, id):
        # Procura um cliente pelo ID e retorna o objeto correspondente
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None  # Retorna None se o cliente não for encontrado

    def listar_leads_por_estado(self, estado):
        # Retorna uma lista de leads com o estado especificado
        return [lead for lead in self.leads if lead.estado == estado]

    def listar_parceiros_por_especialidade(self, especialidade):
        # Retorna uma lista de parceiros com a especialidade especificada
        return [parceiro for parceiro in self.parceiros if especialidade in parceiro.especialidades]