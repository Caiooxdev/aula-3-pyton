# LABORATÓRIO 7 - FUNÇÕES
# QUESTÃO 5
#
# O que a questão pede:
# Crie uma função chamada media que receba três notas e uma letra.
# Se a letra for A, calcule a média aritmética.
# Se a letra for P, calcule a média ponderada com pesos 5, 3 e 2.
# A média deve ser devolvida para a função principal e então impressa.
#
# Exemplos:
# media(2, 3, 4, "A") -> 3.0
# media(5, 4, 6, "P") -> 4.9

def media(n1, n2, n3, tipo):
    if tipo == "A":
        return (n1 + n2 + n3) / 3
    elif tipo == "P":
        return (n1 * 5 + n2 * 3 + n3 * 2) / 10

n1 = float(input())
n2 = float(input())
n3 = float(input())
tipo = input()

resultado = media(n1, n2, n3, tipo)
print(resultado)
