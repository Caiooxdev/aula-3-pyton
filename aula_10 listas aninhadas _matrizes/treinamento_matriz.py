matriz = []

for linha in range(3):
    numeros = []

    for coluna in range(3):
        numeros.append(linha + coluna)

    matriz.append(numeros)

print(matriz)