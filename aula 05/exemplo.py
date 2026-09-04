N =  int(input("Digite um número inteiro: "))

x = 1 

soma = 0
while x <= N:
     #print(x) 
    print(f"antes de somar\nx = {x} - soma = {soma}")
    soma += x 
    x += 1 # -> x = x + 1
print(f"depois de somar\nx = {x} - soma = {soma}")

print(f"soma total = {soma}")












