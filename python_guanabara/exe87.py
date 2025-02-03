from random import randint
M = m = 0
tupla = tuple(randint(0, 100) for _ in range(5))
print(tupla)

M = m = tupla[0]
for n in tupla:
    if n > M:
        M = n
    if n < m:
        m = n

print(f"O maior numero é {M}.")
print(f"O menor numero é {m}.")