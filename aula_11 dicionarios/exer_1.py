def procurachave(dicionario, valor):
   L = []
   for chave in dicionario:
      if dicionario[chave] == valor:
         L.append(chave)
   return L

dict = {

   'alpha': 1,
   'bravo': 2,
   'charlie': 1,
   'delta': 4,
   'echo': 5
}
print(procurachave(dict, 1))  # Saída: ['alpha', 'charlie']