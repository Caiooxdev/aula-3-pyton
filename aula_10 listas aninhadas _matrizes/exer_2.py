import random 

M = [] 
for i in range(10):
    linha = []
    for j in range(15):
        L = random.randint(0, 9)
        linha.append(L)

for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end=' ')
    print()