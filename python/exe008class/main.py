from lead import Lead
from customer import Cliente
from partner import Parceiro
from construcao import NegocioConstrucao

print("Bem-vindo!")
negocio = NegocioConstrucao()

try:
    negocio.carregar_de_json('dados.json')  # Tenta carregar dados existentes
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Nenhum dado anterior encontrado. Iniciando com lista vazia.")
    
while True:
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
    
    op = input("Escolha a opção desejada: ")

    if op == '1':
        nome = input("Digite o nome do cliente: ")
        telemovel = input("Telemóvel: ")
        email = input("Email: ")
        morada = input("Morada: ")

        cliente = Cliente(nome, telemovel, email, morada)
        negocio.adicionar_cliente(cliente)
        negocio.guardar_em_json('dados.json')  

        print(f"Cliente {nome} cadastrado com sucesso! ID do cliente: {cliente.id}")

    elif op == '2':
        cliente_id = input("Digite o id do cliente: ")
        especialidade = input("Especialidade: ")
        parceiros = input("Digite o nome dos parceiros separado por um virgugula ',' [gabriel,bruno]: ").split(',')
        descricao = input("Descrição: ")
        estado = input("Estado: ")

        lead = Lead(cliente_id, especialidade, parceiros, descricao, estado)
        negocio.adicionar_lead(lead)

        negocio.guardar_em_json('dados.json')  

        print(f"Líder cadastrado com sucesso!")

    elif op == '3':
        nome_empresa = input("Digite o nome da empresa: ")
        contacto = input("Digite o contato: ").split()
        email = input("Digite o email: ")
        especialidade = input("Digite a especialidade (Separado por vírgula): ").strip()
        projetos_em_construção = input("Digite os projetos em construção (separado por vírgula): ")

        parceiro = Parceiro(nome_empresa, contacto, email, especialidade, projetos_em_construção)
        negocio.adicionar_parceiro(parceiro)
        negocio.guardar_em_json('dados.json')  # Salva as alterações no JSON

        print(f"Parceiro adicionado com sucesso!")

    elif op == '4':
        cliente_id = input("Digite o seu ID: ")
        cliente = negocio.procurar_cliente_por_id(cliente_id)  # Usa o método correto

        if cliente:
            print(cliente)
        else:
            print("Cliente não encontrado na base de dados.")

    elif op == '5':
        estado = input("Digite o estado para filtrar líderes: ")
        leads = negocio.listar_leads_por_estado(estado)
        for lead in leads:
            print(lead)

    elif op == '6':
        especialidade = input("Digite a especialidade para filtrar parceiros: ")
        parceiros = negocio.listar_parceiros_por_especialidade(especialidade)
        for parceiro in parceiros:
            print(parceiro)

    elif op == '7':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")