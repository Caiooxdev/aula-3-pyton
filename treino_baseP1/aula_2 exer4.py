#Faça um programa que pergunte quanto a pessoa ganha por hora e
#o número de horas trabalhas no mês. Calcule e mostre o total
#do salário no referido mês, sabendo-se que são descontados 11%
#para o imposto de renda, 8% para o INSS e 5% para o sindicato.
#Saída esperada:

valor_hora = float(input("valor por hora: "))
horas_traba = float(input("digite horas trabalhadas: "))
sala_bruto = valor_hora * horas_traba
ir = sala_bruto * 0.11 
inss = sala_bruto * 0.08
sindicato = sala_bruto * 0.05
sala_liquido = sala_bruto - ir - inss - sindicato

print(f" + sálario bruto: R$ {sala_bruto:.2f}")
print(f" - ir (11%): R$ {ir:.2f}")
print(f" - inss (8%): R$ {inss:.2f}")
print(f" - sindicato (5%): R$ {sindicato:.2f}")
print(F" + sala_liquido: R$ {sala_liquido:.2f}")








