def check_number(n1):
    if n1 == 0:
        return "Zero"
    elif n1 > 0:
        return "Positivo"
    elif n1 < 0:
        return "Negativo"
    
n1 = int(input("Digite um numero: "))
print(check_number(n1))
