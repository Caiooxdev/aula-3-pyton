#Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km
#Calcule o preço da passagem:
 #cobrando R$ 0,50 por km para viagens até 200 km
 #R$ 0,45 por km para viagens mais longas.
#Observação: Resolva usando apenas Estruturas de Decisão
#Completas.

km = float(input("que distância você deseja percorer: "))

if km <= 200:
  preço_pass = 0.50 * km 

else:
  preço_pass = 0.45 * km

print("R$",preço_pass)






















