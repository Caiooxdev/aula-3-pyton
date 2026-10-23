import random

numeros = {}
for i in range(21):
    numeros[i] = 0
    
for i in range(100):
    x = random.randint(0, 20)
    numeros[x] += 1

print(numeros)
            