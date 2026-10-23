M = []

somadiag = 0

for i in range(3):
    L = []
    for j in range(3):
        x = int(input(f"Digite o valor para a posição: "))
        L.append(x)
    M.append(L)

for i in range(3):
    for j in range(3):
        if i == j:
            somadiag += M[i][j]
        print(M[i][j], end=' ')
    print()

print(f"A soma dos elementos da diagonal principal é: {somadiag}")