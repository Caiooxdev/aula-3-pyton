# FUNDAMENTOS DE ALGORITMOS - LABORATÓRIO 05
# QUESTÃO 6
#
# Pergunta:
# Um funcionário foi contratado em 2005 com salário inicial de R$ 5.000,00.
# Em 2006 recebeu aumento de 1,5% sobre o salário inicial.
# A partir de 2007, os aumentos salariais correspondem ao dobro do
# percentual do ano anterior.
#
# Faça um programa que receba um ano (ano > 2007) e determine o salário
# atual do funcionário.
#
# Exemplo:
# Entrada: 2012
# Saída: Salário de 2012: R$ 22322.18
#
# Resposta:

ano_desejado = int(input("Digite o ano desejado: "))

salario = 5000.00
percentual = 0.015

# 2006: 1,5% sobre o salário inicial
salario += 5000.00 * percentual

# A partir de 2007, o percentual dobra a cada ano
for ano in range(2007, ano_desejado + 1):
    percentual *= 2
    salario += salario * percentual

print(f"Salário de {ano_desejado}: R$ {salario:.2f}")
