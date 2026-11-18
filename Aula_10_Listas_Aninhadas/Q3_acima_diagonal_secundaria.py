# LABORATÓRIO 10 - QUESTÃO 3
# PERGUNTA: Crie uma matriz M[12][12] de inteiros aleatórios de 0 a 10
# com randint(0,10). Leia S ou M. Calcule SOMA (S) ou MÉDIA (M) apenas
# dos elementos ACIMA da diagonal secundária (área verde do desenho).
# Exiba a matriz com %3d e o resultado. Use apenas números inteiros.
# EXEMPLOS do Moodle: seed(10), S -> Resultado da conta: 324
#                       seed(20), M -> Resultado da conta: 4
# O QUE TREINA: matriz 12x12, randint, diagonal secundária, soma e média inteira.

from random import randint

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(randint(0, 10))
    matriz.append(linha)

operacao = input().upper()
print(operacao)
print("Matriz criada:")
soma = 0
quantidade = 0
for i in range(12):
    for j in range(12):
        print("%3d" % matriz[i][j], end="")
        if i + j < 11:  # ACIMA da diagonal secundária
            soma += matriz[i][j]
            quantidade += 1
    print()

if operacao == "S":
    resultado = soma
else:
    resultado = soma // quantidade  # divisão inteira, como o enunciado pede
print("Resultado da conta:", resultado)

# EXPLICAÇÃO: a diagonal secundária é i+j==11 (índices 0 a 11).
# Acima: i+j<11. A média usa // para não produzir casas decimais.
# Para testar seed(10), antes de criar a matriz execute:
# from random import seed; seed(10)
