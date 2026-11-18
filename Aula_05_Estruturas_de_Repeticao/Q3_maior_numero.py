# FUNDAMENTOS DE ALGORITMOS - LABORATÓRIO 05
# QUESTÃO 3
#
# Pergunta:
# Faça um programa que leia uma quantidade de números que será digitada
# pelo usuário. Em seguida, digite todos os números, conforme quantidade
# previamente informada, e exiba o maior deles.
#
# Exemplo:
# 5
# 10
# 8
# 7
# 15
# 2
# Resultado: Maior número digitado: 15
#
# Resposta:

quantidade = int(input("Entre com a quantidade de números que serão digitados: "))

maior = None

for i in range(1, quantidade + 1):
    numero = int(input(f"número {i}: "))

    if maior is None or numero > maior:
        maior = numero

print(f"Maior número digitado: {maior}")
