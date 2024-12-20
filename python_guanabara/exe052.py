print("--- Calcular o seu IMC ---")
massa = float(input("Digite o seu peso: "))
altura = float(input("Digite o a sua altura: "))

imc = massa / (altura * altura)

if imc < 18.5:
    print(f"Você abaixo do peso seu imc é {imc:.2f}.")
elif imc < 24.9:
    print(f"Você está peso normal seu imc é {imc:.2f}.")
elif imc < 29.9:
    print(f"vc está com exesso de peso seu IMC é {imc:.2f}.")
elif imc == 30:
    print(f"Você está obeso, seu IMC é {imc:.2f}.")
elif imc < 34.9:
    print(f"Você está obesso casse I, seu IMC é{imc:.2f}.")
elif imc < 39.9:
    print(f"Você está onesso classe II, seu IMC é {imc:2.f}.")
else:
    print(f"Você está obeso mórbido, seu IMC é {imc:.2f}")
