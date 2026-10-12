#Escreva um programa que pergunte o salário de um funcionário
#Calcule o valor do aumento de salário sabendo que:
 #Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais a R$ 1250,00, aumento de 15%.
#Imprima o novo salário.
#Observação: Resolva usando apenas Estruturas de Decisão
#Completas.




salário = float(input("digite seu salário: "))
if salário > 1250.00:
   nov_salar = salário * 1.10 
      
else:
   nov_salar = salário * 1.15
   
print(f"R$: {nov_salar:.2f}")