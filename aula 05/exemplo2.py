
N = int(input("Digite a quantidade de valores para somar : "))

cont = 0 
soma= 0

x = 1 

while x != 0:
    x = int(input("Digite um valor: "))
    soma += x
    cont += 1

    print(f"A soma total é {soma}")