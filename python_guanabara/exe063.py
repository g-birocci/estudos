from datetime import date
ano_atual = date.today() #data de hoje
ano_hoje = ano_atual.year #apenas o ano

print("Bem-vindo")
for i in range(0, 6):
    ano = int(input("Digite a data do seu ano de nascimento: "))
     
    if (ano_hoje - ano >= 21):
        print(f"Quem nasceu em {ano} é maior de idade")
    else:
        print(f"Quem nasceu em {ano} é menor de idade.")



    
