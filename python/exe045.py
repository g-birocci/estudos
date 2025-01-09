utilizador_1 = {
  'nome': "João",
  'idade': 20,
  'email': "joao@example.com",
  'pagamento_realizado': True,
  'e_membro': False
}

utilizador_2 = {
  'nome': "",
  'idade': 20,
  'email': "joao@example.com",
  'pagamento_realizado': True,
  'e_membro': False
}

utilizador_3 = {
  'nome': "João",
  'idade': 16,
  'email': "joao@example.com",
  'pagamento_realizado': True,
  'e_membro': False
}

utilizador_4 = {
  'nome': "João",
  'idade': 20,
  'email': "",
  'pagamento_realizado': True,
  'e_membro': False
}

utilizador_5 = {
  'nome': "João",
  'idade': 20,
  'email': "joao@example.com",
  'pagamento_realizado': False,
  'e_membro': False
}

utilizador_6 = {
  'nome': "João",
  'idade': 20,
  'email': "joao@example.com",
  'pagamento_realizado': False,
  'e_membro': True
}

def validar_registo(cliente):

    if not cliente["nome"]:
        return "Registro falhou: Nome não pode ser vazio"
    if not cliente["email"]:
        return "Registro falhou: O email não poder vazio."
    if cliente["idade"] <= 17:
        return "Registro falhou: Vc tem que tem mais de 18 anos pra participar"
    if not cliente["pagamento_realizado"] and not cliente["e_membro"]:
        return "Registro falhou. Pagamento não realizado."

    return "Registro bem-sucedido"

# Testes
print(validar_registo(utilizador_1)) # Registo bem-sucedido

print(validar_registo(utilizador_2)) # Registo falhou: Nome não pode ser vazio

print(validar_registo(utilizador_3)) # Registo falhou: Idade deve ser maior ou igual a 18 anos

print(validar_registo(utilizador_4)) # Registo falhou: Email não pode ser vazio

print(validar_registo(utilizador_5)) # Registo falhou: Pagamento não realizado

print(validar_registo(utilizador_6)) # Registo bem-sucedido