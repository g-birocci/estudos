numeros = []

while True:
    print("\nMenu:")
    print("1. Adicionar um número")
    print("2. Remover um número")
    print("3. Listar números")
    print("4. Calcular a soma dos números")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = input("Digite um número para adicionar: ")
        if numero.replace('.', '', 1).isdigit(): #video explicando isso está no instagram (TI)
            numeros.append(float(numero))
            print(f"Número {numero} adicionado à lista.")
        else:
            print("Entrada inválida! Digite um número válido.")

    elif opcao == "2":
        numero = input("Digite um número para remover: ")
        if numero.replace('.', '', 1).isdigit():
            numero = float(numero)
            if numero in numeros:
                numeros.remove(numero)
                print(f"Número {numero} removido da lista.")
            else:
                print("O número não está na lista.")
        else:
            print("Entrada inválida! Digite um número válido.")

    elif opcao == "3":
        if numeros:
            print("Números na lista:", numeros)
        else:
            print("A lista está vazia.")

    elif opcao == "4":
        soma = sum(numeros)
        print("A soma dos números é:", soma)

    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida! Escolha uma opção válida do menu.")
