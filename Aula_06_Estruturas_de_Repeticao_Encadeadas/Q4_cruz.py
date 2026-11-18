# ========================================
# LABORATÓRIO 06 - QUESTÃO 4
# Estruturas de repetição encadeadas
# ========================================
#
# PERGUNTA:
# Faça um programa que peça ao usuário para digitar um número inteiro
# de 1 a 10 e desenhe uma cruz usando o caractere + com base na entrada.
# O tamanho da cruz deve ser baseado em um número inteiro positivo
# fornecido pelo usuário, que determina o comprimento dos braços da cruz.
# Caso o número digitado não seja válido, mostrar:
# "Número inválido!".
#
# OBSERVAÇÃO:
# O print da questão não mostra um exemplo de saída. Portanto, o modelo
# abaixo interpreta "comprimento dos braços" como n posições para cada
# lado do centro, formando uma cruz de tamanho (2*n - 1).
#
# RESPOSTA:
#
n = int(input("Digite um número de 1 a 10: "))

if n < 1 or n > 10:
    print("Número inválido!")
else:
    tamanho = 2 * n - 1
    meio = tamanho // 2

    for i in range(tamanho):
        for j in range(tamanho):
            if i == meio or j == meio:
                print("+", end="")
            else:
                print(" ", end="")
        print()

# O QUE TREINA:
# - for dentro de for
# - matriz
# - linha e coluna
# - desenho de padrões
