# LABORATÓRIO 10 - QUESTÃO 1
# PERGUNTA: Preencha uma matriz M (2x2) solicitando os 4 elementos inteiros.
# Encontre o maior elemento e imprima outra matriz com cada valor multiplicado
# pelo maior. Use %3d para mostrar os números alinhados.
# EXEMPLO: entrada 5, 7, 8, 2 -> matriz resultante:
#  40  56
#  64  16
# O QUE TREINA: matriz 2x2, for dentro de for, max e formatação.

matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        numero = int(input(f"Digite o elemento da linha {i} e coluna {j}: "))
        linha.append(numero)
    matriz.append(linha)

maior = max(max(linha) for linha in matriz)
print("Matriz resultante:")
for i in range(2):
    for j in range(2):
        print("%3d" % (matriz[i][j] * maior), end="")
    print()

# EXPLICAÇÃO:
# O for externo percorre as linhas; o interno percorre as colunas.
# max encontra o maior número; multiplicamos cada posição por ele.
