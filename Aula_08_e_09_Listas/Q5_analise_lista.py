# LABORATÓRIO 8 E 9 - LISTAS | QUESTÃO 5
# PERGUNTA ORIGINAL:
# Implemente uma função chamada analise que recebe uma lista e retorna
# a media, mediana, o valor mínimo e o máximo respectivamente,
# independente do tamanho da lista.
# EXEMPLO: print(analise([2, 5, 7, -2, 8]))
# SAÍDA: (4.0, 5, -2, 8)
# O QUE TREINA: funções, listas, ordenação, média, mediana, min e max.

def analise(lista):
    ordenada = sorted(lista)
    n = len(ordenada)
    media = sum(ordenada) / n

    if n % 2 == 1:
        mediana = ordenada[n // 2]
    else:
        mediana = (ordenada[n // 2 - 1] + ordenada[n // 2]) / 2

    return (media, mediana, min(lista), max(lista))

print(analise([2, 5, 7, -2, 8]))

# EXPLICAÇÃO:
# sorted coloca os números em ordem crescente sem alterar a lista original.
# Média = soma / quantidade.
# Mediana = valor do meio (ímpar) ou média dos dois do meio (par).
# return devolve os quatro valores na ordem pedida.
# Pressupõe lista não vazia, pois não há média de lista vazia.
