salario = float(input("Digite o salario: "))

if salario > 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15

print("Novo salario:", novo)