L = []
maior = 0
ind_maior = 0

for i in range(10):
  x = float(input("Digite um numero: "))
  L.append(x)

  # Na primeira iteração ou se encontrar um número maior, atualiza
  if i == 0 or x > maior:
    maior = x
    ind_maior = i

print(f"Numeros: {L}")
print(f"Maior numero: {maior}")
print(f"Indice maior numero: {ind_maior}")
