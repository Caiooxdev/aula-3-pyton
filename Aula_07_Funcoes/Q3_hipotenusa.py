# LABORATÓRIO 7 - FUNÇÕES
# QUESTÃO 3
#
# O que a questão pede:
# Escreva uma função que receba como parâmetros os comprimentos dos
# dois lados mais curtos de um triângulo retângulo e retorne a hipotenusa,
# calculada pelo teorema de Pitágoras. Depois, leia os dois lados do usuário,
# use a função e exiba o resultado.
#
# Exemplo:
# Entrada: 3 e 4
# Saída: Hipotenusa: 5.00

def hipotenusa(a, b):
    return (a ** 2 + b ** 2) ** 0.5

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))

resultado = hipotenusa(lado1, lado2)

print(f"Hipotenusa: {resultado:.2f}")
