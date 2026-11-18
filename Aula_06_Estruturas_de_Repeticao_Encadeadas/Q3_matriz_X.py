# ========================================
# LABORATÓRIO 06 - QUESTÃO 3
# Estruturas de repetição encadeadas
# ========================================
#
# PERGUNTA:
# Faça um programa que leia do usuário um número inteiro de 1 a 10
# e mostre um X de # e " " (espaço) na tela.
# O X deve ter a diagonal principal e a diagonal secundária
# preenchidas com o caractere "#".
# Os outros espaços devem ser preenchidos com espaços.
# Caso o número digitado não seja válido, mostrar:
# "Número inválido!".
#
# EXEMPLO DA QUESTÃO:
# Entrada: 2
# Resultado:
# Digite um número de 1 a 10: 2
# ##
# ##
#
# A própria questão mostra também 15 e 10 como "Número inválido!",
# embora o texto diga "de 1 a 10". Essa diferença foi mantida aqui
# como observação para não esconder a inconsistência do enunciado.
#
# RESPOSTA (seguindo o texto "1 a 10"):
#
n = int(input("Digite um número de 1 a 10: "))

if n < 1 or n > 10:
    print("Número inválido!")
else:
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                print("#", end="")
            else:
                print(" ", end="")
        print()

# O QUE TREINA:
# - for dentro de for
# - índices de linha e coluna
# - condição
# - diagonais de uma matriz
