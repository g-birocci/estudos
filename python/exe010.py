print("Welcome to the tip calculator!")
conta = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? (%) "))
div = int(input("How many people to split the bill? "))

pay = ((conta + (conta * (tip / 100))) / div)

if div > 1:
    print(f"O valor que cada pessoa irá pagar é £{pay:.2f}")
else:
    print(f"Você irá pagar £{pay:.2f}")