# LABORATÓRIO 8 E 9 - LISTAS | QUESTÃO 3
# PERGUNTA: Implemente uma função chamada media que retorna a média
# de uma lista, independente do tamanho da lista.
#
# EXEMPLO DA QUESTÃO:
# print(media([5, 12, 15, 8])) -> 10.0
#
# RESPOSTA:

def media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)

print(media([5, 12, 15, 8]))

# EXPLICAÇÃO: o for soma todos os valores; len(lista) conta os itens.
# Média = soma / quantidade de itens.
# O QUE TREINA: def, return, lista, for, acumulador e len.
# OBSERVAÇÃO: o enunciado não especifica lista vazia; nesse caso,
# esta implementação gera ZeroDivisionError.
