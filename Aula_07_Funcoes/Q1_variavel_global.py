# LABORATÓRIO 7 - FUNÇÕES
# QUESTÃO 1
# PERGUNTA: Qual será a saída do seguinte código em Python?
# RESPOSTA: 7 (alternativa d)
# EXPLICAÇÃO: f1 altera o x global para 4; f2 usa esse x: 1 + 2 + 4 = 7.

x = 5

def f1():
    global x
    x = 4

def f2(a, b):
    global x
    return a + b + x

f1()
total = f2(1, 2)
print(total)
