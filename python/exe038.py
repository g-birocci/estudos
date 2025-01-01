def vereficar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    

idade = int(input("Digite quanto anos de idade vc tem: "))
print(vereficar_maioridade(idade))
