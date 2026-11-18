# FUNDAMENTOS DE ALGORITMOS - LABORATÓRIO 05
# QUESTÃO 5
#
# Pergunta:
# Maria precisa saber o total de cobaias utilizadas no laboratório e o
# percentual de cada tipo. Existem três tipos:
# C = coelho, R = rato, S = sapo.
#
# A primeira entrada é N, a quantidade de casos. Cada caso possui:
# quantidade de cobaias + tipo.
#
# Mostrar:
# Total: X cobaias
# Total de coelhos: X
# Total de ratos: X
# Total de sapos: X
# Percentual de coelhos: XX.XX %
# Percentual de ratos: XX.XX %
# Percentual de sapos: XX.XX %
#
# Exemplo:
# 10
# 10 C
# 6 R
# 15 S
# 5 C
# 14 R
# 9 C
# 6 R
# 8 S
# 5 C
# 14 R
#
# Resposta:

n = int(input())

coelhos = 0
ratos = 0
sapos = 0
total = 0

for i in range(n):
    quantidade = int(input())
    tipo = input().strip()

    total += quantidade

    if tipo == "C":
        coelhos += quantidade
    elif tipo == "R":
        ratos += quantidade
    elif tipo == "S":
        sapos += quantidade

percentual_coelhos = coelhos / total * 100
percentual_ratos = ratos / total * 100
percentual_sapos = sapos / total * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
