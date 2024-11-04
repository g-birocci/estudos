def epar(num):
    if num %2 == 0:
        return True
    else:
        return False

num = int(input("Digite um numero: "))
print(epar(num))