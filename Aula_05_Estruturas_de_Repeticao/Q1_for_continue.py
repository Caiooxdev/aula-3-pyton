# FUNDAMENTOS DE ALGORITMOS - LABORATÓRIO 05
# QUESTÃO 1
#
# Pergunta:
# Qual será a saída do seguinte código em Python?
#
# for i in range(5):
#     if i == 4:
#         continue
#     else:
#         print(i, end=" ")
# else:
#     print("Aqui", end=" ")
#
# Resposta:
# Alternativa C
# Saída: 0 1 2 3 Aqui
#
# Explicação:
# range(5) gera 0, 1, 2, 3, 4.
# Quando i vale 4, continue pula essa volta e o 4 não é impresso.
# Como o for termina normalmente, o else do for é executado.
