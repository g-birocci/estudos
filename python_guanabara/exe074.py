n = int(input("Digite um numero interiro: "))

fibo = [0, 1]
contador = 2

while contador < n:
    next = fibo[-1] + fibo[-2] #soma dos ultimos termos
    fibo.append(next)
    contador += 1

print("Os primeiros", n, "termos da sequência de Fibonacci são:", fibo)