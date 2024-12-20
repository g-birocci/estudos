def avista(produto):
    n = produto - (produto * 10)/100
    print(f"O valor a ser pago é £{n:.2f}")
    
def avista_cartao(produto):
    n = produto - (produto * 5)/100
    print(f"O valor a ser pago será de {n:.2f}")

def cartao2x(produto):
    n = produto / 2
    print(f"O valor de cada parcela será de £{n:.2f} por mês.")

def cartao(produto, vezes):
    n = produto + (produto * 20)/100
    n_pagar = n / vezes
    print(f"Você pagar £{n_pagar:.2f} por mês.")


print("--- loja de compras ---")
produto = float(input("Qual o preço do produto: "))
print(''' Escolha a forma de pagamento)
      1 -- à vista
      2 -- à vista no cartão (5% de desconto)
      3 -- 2x no cartão
      4 -- 3x ou mais (20% de juros)
      5 -- Sair ''')
op = str(input("Digite o numero da opção desejada: "))

sair = True
while sair:
    match op:
        case "1":
            avista(produto)
            break
        case "2":
            avista_cartao(produto)
            break
        case "3":
            cartao2x(produto)
            break
        case "4":
            vezes = int(input("Em quantas vezes vc quer parcelar? "))
            cartao(produto, vezes)
            break
        case "5":
            sair = False
        case _:
            print("opção invalida!")
