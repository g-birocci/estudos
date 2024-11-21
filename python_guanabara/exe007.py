teste = input("Digite algo aqui: ")

print("O tipo primitivo desse valor é ", type(teste)) #tem que declarar a variavel para vereficar em baixo.
print("É um número? ", teste.isnumeric())
print("Só tem espaços? ", teste.isspace())
print("É alfabético? ", teste.isalpha())
print("É alfanumérico? ", teste.isalnum())
print("Está em maiúsculas? ", teste.isupper())
print("Está em minúsculas? ", teste.islower())
print("Está capitalizada (primeira letra maiúscula)? ", teste.istitle())

#posso usar isso para vereficar os criterios de uma senha.