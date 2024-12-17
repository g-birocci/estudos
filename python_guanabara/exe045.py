print("---- Banco de empréstimo ----")
casa = float(input("Qual o valor da casa que deseja comprar: "))
ordenado = float(input("Qual o valor do seu ordenado? "))
tempo_pagar = int(input("Em qauntos tempo vc quer pagar a casa ? (anos) "))

meses = tempo_pagar * 12
prestacao = casa / meses
pode = prestacao > (ordenado * 30) / 100
print(pode)

if prestacao > (ordenado * 30) / 100:
    print("Vc não pode financiar está casa *-*")
else: 
    print("Vc pode financiar a sua casa.")