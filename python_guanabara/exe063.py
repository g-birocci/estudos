from datetime import date
ano_atual = date.today() #data de hoje
ano_hoje = ano_atual.year #apenas o ano
cont_M = 0
cont_m = 0

print("Bem-vindo")
for i in range(0, 6):
    ano = int(input("Digite a data do seu ano de nascimento: "))
    
    if (ano_hoje - ano >= 21):
        cont_M += + 1
    else:
        cont_m += +1

print(f"Temos {cont_M} maiores de idade.")
print(f"Temos {cont_m} menores de idade.")



    
