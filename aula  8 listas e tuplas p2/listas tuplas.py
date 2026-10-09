T = [11,7, 2, 0]
print(min(T))
"""

menor = T[0]
for valor in T:
    if valor < menor:
        menor = valor

print(menor)
"""