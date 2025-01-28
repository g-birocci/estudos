first = int(input("Digite o primeiro elemento: "))
razao = int(input("Razão: "))
n = int(input("Quantos elementos você quer exibir inicialmente? "))

pa = []
contador = 0
total = 0
termo = first
mais = n

# Loop principal
while mais != 0:
    total += mais  # Atualiza o total de termos a exibir
    while contador < total:  # Calcula os termos da PA até o total desejado
        pa.append(termo)
        termo += razao
        contador += 1
    print(f"Os primeiros {total} elementos da PA são: {pa}")
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print("Progressão Aritmética finalizada!")
