# LABORATÓRIO 8 E 9 - LISTAS | QUESTÃO 1
# PERGUNTA: Qual será a saída do seguinte código em Python?
#
# a = [1, 2, 3, 4, 5]
# for i in range(1, 5):
#     a[i-1] = a[i]
# for i in range(0, 5):
#     print(a[i], end=" ")
#
# RESPOSTA: alternativa D -> 2 3 4 5 5
# EXPLICAÇÃO: range(1,5) gera 1,2,3,4. Em cada volta, o elemento
# da posição anterior recebe o valor da posição atual.
# A lista termina [2,3,4,5,5].
# O QUE TREINA: índices, atribuição em listas, for, range.

a = [1, 2, 3, 4, 5]
for i in range(1, 5):
    a[i-1] = a[i]
for i in range(0, 5):
    print(a[i], end=" ")
