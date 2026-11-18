T = [11, 7, 2, 4]

# Começamos por assumir que o primeiro elemento é o menor provisório
menor = T[0]

for valor in T:
  if valor < menor:
    menor = valor  # Atualiza se encontrar um valor ainda menor

print(menor)