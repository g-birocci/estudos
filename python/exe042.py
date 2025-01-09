def verificar_falsy_truthy(valores):
    falsy = []
    truthy = []

    for dados in valores:
        if dados:
            truthy.append(dados)
        else:
            falsy.append(dados)
            
    return falsy, truthy

valores = [
    0, 1, "", "Python", [], [1, 2], {}, {
        "chave": "valor"
    }, None, True, False
]

falsy, truthy = verificar_falsy_truthy(valores)
print("Falsy:", falsy)
print("Truthy:", truthy)
