arquivo = open("teste.txt", "r")


for linha in arquivo.readlines():
    print(linha, end="")
    arquivo.close()




#arquivo = open("teste.txt", "w")
#arquivo.write("vou para pernambuco ano que vem")
#arquivo.close()