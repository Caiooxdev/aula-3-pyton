valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas = float(input("Digite o numero de horas trabalhadas no mes: "))

bruto = valor_hora * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print("+ Salario Bruto: R$", bruto)
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("+ Salario liquido: R$", liquido)