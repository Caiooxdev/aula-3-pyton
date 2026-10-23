#Construa um algoritmo que, tendo como dados de entrada o preço
#de um produto e seu código de origem, mostre o preço junto de
#sua procedência. Caso o código não seja nenhum dos
#especificados, o produto deve ser encarado como importado.
#Siga a tabela de códigos:


preço = float(input("valor do produto: "))
codigo = int(input("digite o codigo: "))

if codigo == 1:
    print(codigo,"Sul")
elif codigo == 2:
    print(codigo,"Norte")
elif codigo == 3:
    print(codigo,"Leste")
elif codigo == 4:
    print(codigo,"Oeste")
elif codigo == 5 or codigo == 6:
    print(codigo,"Nordeste")
elif  codigo == 7 or codigo == 8 or codigo == 9:
    print(codigo,"Sudeste")
elif codigo  >= 10 and codigo <= 20:
    print(codigo,"Centro-Oeste")
elif codigo >= 25 and codigo <= 30:
    print(codigo,"Nordeste")
else:
    print("produto importado")




















