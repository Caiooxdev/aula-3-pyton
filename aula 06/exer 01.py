totalprimos = 0

n = int(input(("Digite a quantidade de números: ")))
for i in range(n):
   primos = 0
   x = int(input("digite um número: "))
if x > 1: 
   primos = 1
   for j in range(2, x):
         if x % j == 0:
              primos=0
              break
         totalprimos += primos

         print(f"o total de números primos: {totalprimos}")