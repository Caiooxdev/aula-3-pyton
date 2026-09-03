ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nasc
print("Idade:", idade)

if idade >= 16:
    print("Pode votar")

if idade >= 18:
    print("Pode tirar CNH")