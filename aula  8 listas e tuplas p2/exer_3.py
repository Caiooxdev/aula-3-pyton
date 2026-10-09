L = []
maior = 0
ind_maior = 0 
for i in range(10):
   x = int(input())
   L.append(x)
   if x > maior:
       maior = x
       ind_maior = i
print(f"numeros: {L}")
print(f"maior numero: {maior}")
print(f"índice do maior numero: {ind_maior}")