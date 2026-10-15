l = []
somopar = 0
somaindpar = 0



for i in range(10):
    x = int(input())
    l.append(x)
    if x % 2 == 0:
        somopar += x
    if i % 2 == 0:
        somaindpar += x 



print(l)
print(somopar)
print(somaindpar)

