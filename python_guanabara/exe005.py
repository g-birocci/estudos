dado = input('Digite algo: ')

if dado.isdigit():
    print("O tipo primitivo do que você digitou é", type(int(dado)))
elif dado.replace('.', '', 1).isdigit():
    print("O tipo primitivo do que você digitou é", type(float(dado)))
elif dado.lower() in ['true', 'false']:
    print("O tipo primitivo do que você digitou é", type(bool(dado)))
else:
    print("O tipo primitivo do que você digitou é", type(dado))
