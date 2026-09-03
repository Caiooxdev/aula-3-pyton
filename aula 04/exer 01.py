preco = float(input("Digite o preço: "))
codigo = int(input("Digite o código de origem: "))

if codigo == 1:
    print(preco, "Sul")
elif codigo == 2:
    print(preco, "Norte")
elif codigo == 3:
    print(preco, "Leste")
elif codigo == 4:
    print(preco, "Oeste")
elif codigo == 5 or codigo == 6:
    print(preco, "Nordeste")
elif codigo == 7 or codigo == 8 or codigo == 9:
    print(preco, "Sudeste")
elif codigo >= 10 and codigo <= 20:
    print(preco, "Centro-Oeste")
elif codigo >= 25 and codigo <= 30:
    print(preco, "Nordeste")
else:
    print(preco, "Importado")