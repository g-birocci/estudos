from lead import Lead  # Importa a classe Lead
from customer import Cliente  # Importa a classe Cliente
from partner import Parceiro  # Importa a classe Parceiro
from construcao import NegocioConstrucao  # Importa a classe NegocioConstrucao

print("Bem-vindo!")  # Mensagem de boas-vindas
negocio = NegocioConstrucao()  # Cria uma instância da classe NegocioConstrucao

try:
    # Tenta carregar dados existentes do arquivo JSON
    negocio.carregar_de_json('dados.json')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    # Caso o arquivo não exista, inicia com listas vazias
    print("Nenhum dado anterior encontrado. Iniciando com lista vazia.")

while True:
    # Menu principal do sistema
    print('''
        Escolha a opção desejada!
        1 -- Cadastrar Cliente
        2 -- Cadastrar Líder
        3 -- Adicionar Parceiro
        4 -- Procurar Cliente
        5 -- Listar Líderes
        6 -- Listar Parceiros
        7 -- Sair
    ''')

    op = input("Escolha a opção desejada: ").strip()  # Solicita a escolha do usuário

    if op == '1':
        # Cadastra um novo cliente
        nome = input("Digite o nome do cliente: ").strip().title()

        while True:
            try:
                telemovel = input("Digite o número de telefone com 9 dígitos: ").strip()

                if len(telemovel) == 9 and telemovel.isdigit():
                    break
                else:
                    print("Número de telefone inválido. Precisa ter 9 dígitos.")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        email = input("Email: ")
        morada = input("Morada: ")

        cliente = Cliente(nome, telemovel, email, morada)  # Cria um objeto Cliente
        negocio.adicionar_cliente(cliente)  # Adiciona o cliente à lista
        negocio.guardar_em_json('dados.json')  # Salva as alterações no arquivo JSON

        print(f"Cliente {nome} cadastrado com sucesso! ID do cliente: {cliente.id}")

    elif op == '2':
        # Cadastra um novo lead
        cliente_id = input("Digite o id do cliente: ")
        especialidade = input("Especialidade: ")
        parceiros = input("Digite o nome dos parceiros separado por um virgugula ',' [gabriel,bruno]: ").split(',')
        descricao = input("Descrição: ")
        estado = input("Estado: ")

        lead = Lead(cliente_id, especialidade, parceiros, descricao, estado)  # Cria um objeto Lead
        negocio.adicionar_lead(lead)  # Adiciona o lead à lista
        negocio.guardar_em_json('dados.json')  # Salva as alterações no arquivo JSON

        print(f"Líder cadastrado com sucesso!")

    elif op == '3':
        # Adiciona um novo parceiro
        nome_empresa = input("Digite o nome da empresa: ")

        while True:
            try:
                contacto = input("Digite o número de telefone com 9 dígitos: ").strip()

                if len(contacto) == 9 and contacto.isdigit():
                    break
                else:
                    print("Número de telefone inválido. Precisa ter 9 dígitos.")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        
        email = input("Digite o email: ")
        especialidade = input("Digite a especialidade (Separado por vírgula): ").strip()
        projetos_em_construção = input("Digite os projetos em construção (separado por vírgula): ")

        parceiro = Parceiro(nome_empresa, contacto, email, especialidade, projetos_em_construção)  # Cria um objeto Parceiro
        negocio.adicionar_parceiro(parceiro)  # Adiciona o parceiro à lista
        negocio.guardar_em_json('dados.json')  # Salva as alterações no arquivo JSON

        print(f"Parceiro adicionado com sucesso!")

    elif op == '4':
        # Procura um cliente pelo ID
        cliente_id = input("Digite o seu ID: ")
        cliente = negocio.procurar_cliente_por_id(cliente_id)  # Procura o cliente

        if cliente:
            print(cliente)  # Exibe os dados do cliente
        else:
            print("Cliente não encontrado na base de dados.")

    elif op == '5':
        # Lista leads por estado
        estado = input("Digite o estado para filtrar líderes: ")
        leads = negocio.listar_leads_por_estado(estado)  # Obtém os leads com o estado especificado
        for lead in leads:
            print(lead)  # Exibe os leads

    elif op == '6':
        # Lista parceiros por especialidade
        especialidade = input("Digite a especialidade para filtrar parceiros: ")
        parceiros = negocio.listar_parceiros_por_especialidade(especialidade)  # Obtém os parceiros com a especialidade especificada
        for parceiro in parceiros:
            print(parceiro)  # Exibe os parceiros

    elif op == '7':
        # Sai do sistema
        print("Saindo do sistema. Até logo!")
        break
    else:
        # Opção inválida
        print("Opção inválida. Por favor, tente novamente.")