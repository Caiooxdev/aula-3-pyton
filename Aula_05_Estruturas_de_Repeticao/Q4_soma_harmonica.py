# FUNDAMENTOS DE ALGORITMOS - LABORATÓRIO 05
# QUESTÃO 4
#
# Pergunta:
# Faça um programa que leia um valor N inteiro e positivo, calcule e mostre
# o valor de E, conforme:
#
# E = 1 + 1/1 + 1/2 + 1/3 + ... + 1/N
#
# Exemplo:
# Entrada: 4
# Saída:
# Digite o número desejado: 4
# 3.083
#
# Resposta:

n = int(input("Digite o número desejado: "))

e = 1

for i in range(1, n + 1):
    e += 1 / i

print(f"{e:.3f}")
