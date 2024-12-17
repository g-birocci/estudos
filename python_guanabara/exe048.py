from datetime import date
ano_nasc = int(input("Digite o seu ano de nascimento: "))

ano_atual = date.today() #data de hoje
ano_hoje = ano_atual.year #apenas o ano

idade = ano_hoje - ano_nasc
print(idade)

if idade < 17:
    n = 17 - idade
    print(f"Você ainda tem {n} anos pra se alistar")
elif idade <= 18:
    print("Você já pode se alistar")
elif idade > 18:
    n = idade - 18
    print(f"Você já passou {n} anos do prazo pra se alistar.")