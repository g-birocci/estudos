
def dobrar(lista):
    dobro_lista = [num * 2 for num in lista]
    return dobro_lista

numeros = (input("Digite a lista que deseja dobrar: "))
num_lista = list(map(int, numeros.split()))

total = dobrar(num_lista)
print("Lista dobrada:", total)
