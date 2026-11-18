# ========================================
# LABORATÓRIO 06 - QUESTÃO 2
# Estruturas de repetição encadeadas
# ========================================
#
# PERGUNTA:
# Escreva um programa em Python que:
# 1. Peça ao usuário um número inteiro n entre 1 e 10.
# 2. Crie uma matriz n x n contendo apenas o número 0.
# 3. Exiba a matriz na tela se for possível.
#
# RESPOSTA:
#
n = int(input("Digite um número entre 1 e 10: "))

if n < 1 or n > 10:
    print("Número inválido!")
else:
    for i in range(n):
        for j in range(n):
            print(0, end=" ")
        print()

# O QUE TREINA:
# - for dentro de for
# - linhas e colunas
# - matriz
