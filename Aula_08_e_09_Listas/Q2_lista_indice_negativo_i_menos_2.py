# LABORATÓRIO 8 E 9 - LISTAS | QUESTÃO 2
# PERGUNTA: Qual será a saída do seguinte código em Python?
#
# a = [1, 2, 3, 4, 5]
# for i in range(1, 5):
#     a[i-2] = a[i]
# for i in range(0, 5):
#     print(a[i], end=" ")
#
# RESPOSTA: alternativa C -> 3 4 2 4 2
# EXPLICAÇÃO: i=1: a[-1]=a[1] (último vira 2).
# i=2: a[0]=a[2] (primeiro vira 3).
# i=3: a[1]=a[3] (segundo vira 4).
# i=4: a[2]=a[4] (terceiro vira 2, pois a[4] já mudou).
# O QUE TREINA: índices negativos, atualização sequencial de lista.

a = [1, 2, 3, 4, 5]
for i in range(1, 5):
    a[i-2] = a[i]
for i in range(0, 5):
    print(a[i], end=" ")
