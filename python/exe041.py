def validar_registo(usuario):
  
  nome_valido = bool(usuario['nome'])
  idade_valida = usuario['idade'] >= 18
  email_valido = bool(usuario['email'])
  pagamento_valido = usuario['pagamento_realizado'] or (usuario['e_membro'] and not usuario['pagamento_realizado'])

  if nome_valido and idade_valida and email_valido and pagamento_valido:
    return "Registro bem-sucedido!"
  else:
    motivos = []
    if not nome_valido:
      motivos.append("Nome inválido.")
    if not idade_valida:
      motivos.append("Idade inválida. Deve ser maior ou igual a 18 anos.")
    if not email_valido:
      motivos.append("Email inválido.")
    if not pagamento_valido:
      motivos.append("Pagamento não realizado.")

    return "Registro falhou: " + ", ".join(motivos)

# Testes
print(validar_registo(utilizador_1))
# ... outros testes ...
check = input("Digite o seu nome de usuario: ")
checK = validar_registo(check)
print(checK)

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
