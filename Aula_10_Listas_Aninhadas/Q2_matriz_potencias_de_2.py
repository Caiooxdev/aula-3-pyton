# LABORATÓRIO 10 - QUESTÃO 2
# PERGUNTA: Leia a ordem N de uma matriz quadrada (0 <= N <= 15).
# Construa e imprima uma matriz conforme o padrão do enunciado,
# reservando 4 casas para cada elemento.
# EXEMPLO: N=4
#    1   2   4   8
#    2   4   8  16
#    4   8  16  32
#    8  16  32  64
# O QUE TREINA: matriz N x N, potência e alinhamento.

n = int(input("Digite a ordem da matriz: "))
if 0 <= n <= 15:
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(2 ** (i + j))
        matriz.append(linha)

    for linha in matriz:
        for numero in linha:
            print("%4d" % numero, end="")
        print()
else:
    print("Número inválido!")

# EXPLICAÇÃO: i e j começam em zero; 2**(i+j) gera 1,2,4,8...
# Em cada linha, a sequência começa uma potência adiante.
