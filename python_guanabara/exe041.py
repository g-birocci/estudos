from datetime import date #pegar a data da maquina

ano = int(input("Digite o ano que deseja saber se é bissextos: "))

if ano == 0:
    ano = date.today().year #Está função pega a data do deu computador

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"Este ano {ano} é bissexto. ")
else:
    print(f"Este ano {ano} não é bissexto. ")