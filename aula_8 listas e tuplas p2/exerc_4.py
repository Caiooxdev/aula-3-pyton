l = []
somapar = 0
somaindpar = 0

# 1. Pedir os 10 números ao usuário e guardar na lista
for i in range(10):
  x = int(input("Digite um numero: "))
  l.append(x)

# 2. Percorrer a lista já preenchida para somar
for indice in range(len(l)):
  # Soma dos elementos que são pares (o valor guardado dentro da lista)
  if l[indice] % 2 == 0:
    somapar += l[indice]

  # Soma dos elementos cujos ÍNDICES são pares (0, 2, 4, 6, 8)
  if indice % 2 == 0:
    somaindpar += l[indice]

# 3. Mostrar os resultados esperados
print("Numeros:", l)
print("Soma elementos pares:", somapar)
print("Soma elementos indice par:", somaindpar)