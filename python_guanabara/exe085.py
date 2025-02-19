numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", 
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", 
    "dezoito", "dezenove", "vinte"
)

while True:
    n = int(input("Digite um nemero entre 0 e 20: "))
    if n >= 0 and n <= 20: 
        print(f"O numero digitado foi {numeros[n]}")
        
        continuar = str(input("Voce quer continuar [S/N] ?")).strip().upper()

        if continuar == "N":
            print("Saindo do sistema... bye!")
            break

