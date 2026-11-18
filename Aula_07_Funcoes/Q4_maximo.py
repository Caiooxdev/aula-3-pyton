# LABORATÓRIO 7 - FUNÇÕES
# QUESTÃO 4
#
# O que a questão pede:
# Crie uma função máximo(x, y) que retorne o maior de dois números.
# Ela também deve ter um parâmetro opcional "imprime", que por padrão
# é False. Quando imprime=True, deve imprimir o valor máximo.
#
# Exemplos:
# print(maximo(1, 2)) -> 2
# maximo(7, 20, True) -> imprime 20

def maximo(x, y, imprime=False):
    maior = x
    if y > maior:
        maior = y

    if imprime:
        print(maior)

    return maior

print(maximo(1, 2))
maximo(7, 20, True)
