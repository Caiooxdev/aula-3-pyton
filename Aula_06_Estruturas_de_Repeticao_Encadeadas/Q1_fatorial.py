# ========================================
# LABORATÓRIO 06 - QUESTÃO 1
# Estruturas de repetição encadeadas
# ========================================
#
# PERGUNTA:
# Faça um programa que leia do usuário um número inteiro de 1 a 10
# e calcule o fatorial de todos os números de 1 até o número digitado.
# O fatorial de um número é o produto de todos os inteiros positivos
# de 1 até esse número.
# O programa deve exibir o fatorial de cada número individualmente.
# Caso o número digitado não seja válido, o programa deve mostrar:
# "Número inválido!".
#
# Exemplo da questão:
# Entrada: 3
# Resultado:
# Digite um número de 1 a 10: 3
# Fatorial de 1 = 1
# Fatorial de 2 = 2
# Fatorial de 3 = 6
#
# RESPOSTA:
#
n = int(input("Digite um número de 1 a 10: "))

if n < 1 or n > 10:
    print("Número inválido!")
else:
    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i
        print(f"Fatorial de {i} = {fatorial}")

# O QUE TREINA:
# - if/else
# - for
# - acumulador/produto
# - fatorial
