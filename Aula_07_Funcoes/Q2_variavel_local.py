# LABORATÓRIO 7 - FUNÇÕES
# QUESTÃO 2
# PERGUNTA: Qual será a saída do seguinte código em Python?
# RESPOSTA: 6 (alternativa c)
# EXPLICAÇÃO: f2 cria um x local igual a 3; 1 + 2 + 3 = 6.

x = 5

def f1():
    global x
    x = 4

def f2(a, b):
    x = 3
    return a + b + x

f1()
total = f2(1, 2)
print(total)
