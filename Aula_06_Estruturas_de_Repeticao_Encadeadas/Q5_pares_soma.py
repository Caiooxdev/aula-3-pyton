# ========================================
# LABORATÓRIO 06 - QUESTÃO 5
# Estruturas de repetição encadeadas
# ========================================
#
# PERGUNTA:
# Faça um programa que leia do usuário um número inteiro de 1 a 10
# e exiba todos os pares de números inteiros (i, j) onde i e j
# variam de 1 até o número digitado.
# Para cada par (i, j), o programa deve exibir a soma de i + j.
# Caso o número digitado não seja válido, mostrar:
# "Número inválido!".
#
# RESPOSTA:
#
n = int(input("Digite um número de 1 a 10: "))

if n < 1 or n > 10:
    print("Número inválido!")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"({i}, {j}) = {i + j}")

# O QUE TREINA:
# - for dentro de for
# - pares (i, j)
# - soma
# - repetição encadeada
