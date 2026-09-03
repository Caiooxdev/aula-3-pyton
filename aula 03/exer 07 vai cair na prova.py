km = float(input("Digite a distância em km: "))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print("Preço da passagem: R$", preco)