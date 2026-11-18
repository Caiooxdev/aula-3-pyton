# LABORATÓRIO 7 - FUNÇÕES
# QUESTÃO 6
#
# O que a questão pede:
# Crie uma função chamada multiplo(x, y).
# Ela recebe dois números e retorna True se o primeiro for múltiplo
# do segundo. Caso contrário, retorna False.
#
# Exemplo:
# print(multiplo(10, 5)) -> True

def multiplo(x, y):
    return x % y == 0

print(multiplo(10, 5))
