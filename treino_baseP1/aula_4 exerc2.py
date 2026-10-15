#Escreva um algoritmo que leia três valores inteiros e
#diferentes e mostre-os em ordem decrescente.

a  = int(input("digite um número: "))
b = int(input("digite outro número: "))
c = int(input("digite mais um número: "))

if a > b and a > c and b > c:
    print(a,b,c)
elif a > b and a > c and c > b:
    print(a,c,b)
elif b > a and b > c and a > c:
    print(b,a,c)
elif b > a and b > c and c > a:
    print(b,c,a)
elif c > a and c > b and a > b:
    print(c,a,b)
else:
    print(c,b,a)
















