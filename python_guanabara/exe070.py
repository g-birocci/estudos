
sair = True
while sair:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))
    
    voltar = True
    while voltar:
        print("-" * 30)
        print("Escolha o que vc deseja fazer com esse numeros.")
        print("1- Somar")
        print("2- Subtrair")
        print("3- Maior numero")
        print("4 -Novos numeros")
        print("5- Sair")
        escolha = str(input("Digite a opção: "))

        match escolha:
            case "1":
                soma = n1 + n2
                print(f"A soma dos numeros é: {soma}.")
            case "2":
                subtracao = n1 - n2
                print(f"A subtração dos numeros é: {subtracao}.")

            case "3":
                if n1 > n2:
                    print(f"O numero {n1} é o maior.")
                elif n1 < n2:
                    print(f"O numero {n2} é o maior.")
                else:
                    print(f"Os numeros {n1} e {n2} são igiais.")

            case "4":
                voltar = False   

            case "5":
                voltar = False
                sair = False
