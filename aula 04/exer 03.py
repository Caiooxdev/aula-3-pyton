altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (M/F): ")

if sexo == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print("Peso ideal:", peso)